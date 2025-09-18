#!/usr/bin/env python3
# ─────────────────────────────────────────────────────────────────────────────
#  MATH_ReAct_prompt_file.py   (resilient workers + retryable API calls)
#  - Never abort an entire worker on a per-problem error
#  - All OpenAI calls are retried with exponential backoff + jitter
#  - On final failure, mark problem as wrong_null_answer and continue
#  - Preserves: duplicate-call cache, live NDJSON, part files, merged JSON
# ─────────────────────────────────────────────────────────────────────────────

from __future__ import annotations
import argparse, ast, hashlib, json, os, random, re, textwrap, time
from pathlib import Path
from typing import Any, Dict, List, Tuple, Optional
import types
import importlib.util
import math as _math
import json as _json
from collections import defaultdict
import multiprocessing as mp

import openai
from openai import (  # v1 exceptions
    APIError, RateLimitError, APIConnectionError, APITimeoutError,
    BadRequestError, AuthenticationError,
)
from datasets import load_dataset

# ─────────────────────────── CLI ────────────────────────────
P = argparse.ArgumentParser()
P.add_argument("--num-examples", type=int, default=100)
P.add_argument("--split",        type=str, default="train")
P.add_argument("--tools-file",   type=str,
               default="/data2/hyeonjechoi/math_predefined/Test_MATH/"
                       "function_tools/function_rewritten_files.json",
               help="JSON with tools; each tool['function'] is a filename like a61z27.py")
P.add_argument("--functions-dir", type=str, default=None,
               help="Optional directory to resolve tool files. If omitted, we try: "
                    "(1) absolute path in JSON, (2) relative to tools-file dir, "
                    "(3) <tools-file dir>/function_total/")
P.add_argument("--out",          type=str, default="MATH_ReAct_prompt_file.json",
               help="Final merged pretty JSON array")
P.add_argument("--live-ndjson",  type=str, default=None,
               help="Path to write streaming JSON Lines (NDJSON). "
                    "Default: same as --out but with .ndjson suffix.")
P.add_argument("--sleep",        type=float, default=0.7)
P.add_argument("--model",        type=str, default="gpt-4o-mini",
               help="model that *solves* the problems with ReAct")
P.add_argument("--judge-model",  type=str, default="gpt-4o-mini",
               help="model that judges correctness")
P.add_argument("--num-workers",  type=int, default=4,
               help="number of worker processes (ideally = number of API keys)")
P.add_argument("--api-key-vars", type=str, default="mppre_1,mppre_2,mppre_3,mppre_4",
               help="comma-separated env var names containing OpenAI API keys")
# NEW: retry controls
P.add_argument("--max-retries", type=int, default=5,
               help="max retries for each OpenAI API call")
P.add_argument("--retry-backoff", type=float, default=0.8,
               help="initial backoff seconds for retries (exponential with jitter)")
args = P.parse_args()
if args.live_ndjson is None:
    args.live_ndjson = str(Path(args.out).with_suffix(".ndjson"))

# ───────────────────────── regex & prompts ──────────────────────────
ANS_RE = re.compile(r"^ANSWER\s*:\s*(.+)$", re.M)
ACT_RE = re.compile(r"^Action\s*:\s*({.*})\s*$", re.M)

SYS_SOLVER = textwrap.dedent("""\
    You are an expert competition-math solver.
    For every turn output *exactly one* line beginning with “Thought: …”.
    If you need a tool, follow IMMEDIATELY with ONE line:
    Action: { "name": "<tool>", "arguments": { … } }
    Then WAIT for the Observation line before thinking again.
    Never call a tool with the same arguments twice – reuse the prior Observation.
    If you have already called a tool with the same name and identical arguments, DO NOT call it again; reuse the cached Observation verbatim and move forward.
    Finish with:
    ANSWER: <numeric answer>""")

SYS_JUDGE = textwrap.dedent("""\
    You are an automated grader for math-contest problems.
    Reply YES if the student's answer is fully correct, otherwise reply NO.
    Reply with ONLY YES or NO.""")

# ───────────────────── file resolution & import ─────────────────────
def _resolve_tool_path(file_field: str, tools_dir: Path, override_functions_dir: Optional[Path]) -> Path:
    cand = Path(file_field)
    if cand.is_absolute() and cand.exists():
        return cand
    cand2 = (tools_dir / file_field).resolve()
    if cand2.exists():
        return cand2
    if override_functions_dir:
        cand3 = (override_functions_dir / file_field).resolve()
        if cand3.exists():
            return cand3
    cand4 = (tools_dir / "function_total" / file_field).resolve()
    if cand4.exists():
        return cand4
    if not file_field.endswith(".py"):
        return _resolve_tool_path(file_field + ".py", tools_dir, override_functions_dir)
    raise FileNotFoundError(f"Cannot locate tool file for: {file_field}")

_module_cache: Dict[Path, types.ModuleType] = {}

def _import_module_from_path(py_path: Path) -> types.ModuleType:
    if py_path in _module_cache:
        return _module_cache[py_path]
    mod_name = "toolmod_" + hashlib.sha1(str(py_path).encode("utf-8")).hexdigest()
    spec = importlib.util.spec_from_file_location(mod_name, py_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not create spec for {py_path}")
    module = importlib.util.module_from_spec(spec)
    module.__dict__.setdefault("math", _math)
    spec.loader.exec_module(module)
    _module_cache[py_path] = module
    return module

def _load_callable(t: Dict[str, Any], tools_dir: Path, override_functions_dir: Optional[Path]) -> Any:
    if "_impl" in t:
        return t["_impl"]
    file_field = t.get("function")
    if not isinstance(file_field, str):
        raise TypeError(f"tool['function'] must be a filename string; got {type(file_field)}")
    py_path = _resolve_tool_path(file_field, tools_dir, override_functions_dir)
    module = _import_module_from_path(py_path)
    fn_name = t.get("name")
    if not isinstance(fn_name, str) or not fn_name:
        raise ValueError("tool['name'] must be a non-empty string")
    try:
        fn = getattr(module, fn_name)
    except AttributeError:
        raise AttributeError(
            f"Function '{fn_name}' not found in module '{py_path.name}'. "
            f"Ensure the file defines: def {fn_name}(...):"
        )
    t["_impl"] = fn
    return fn

def run_tool(t: Dict[str, Any], kwargs: Dict[str, Any],
             tools_dir: Path, override_functions_dir: Optional[Path]) -> Any:
    fn = _load_callable(t, tools_dir, override_functions_dir)
    return fn(**(kwargs or {}))

def strip_impl(t: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in t.items() if k != "_impl"}

# ────────────────────── canonical cache key helpers ─────────────────────
MAX_DUP_OBS = 2

def _canon_args(obj):
    if isinstance(obj, dict):
        return {k: _canon_args(obj[k]) for k in sorted(obj)}
    if isinstance(obj, (list, tuple)):
        return [_canon_args(x) for x in obj]
    if isinstance(obj, float) and obj.is_integer():
        return int(obj)
    return obj

def _key_for_call(name: str, args: dict) -> tuple[str, str]:
    canon = _canon_args(args or {})
    return (name, _json.dumps(canon, separators=(",", ":"), sort_keys=True))

# ───────────────────────── Retryable OpenAI calls ─────────────────────────
def _sleep_with_jitter(base: float, attempt: int):
    # exponential + jitter in [0.75, 1.25] range
    delay = base * (2 ** attempt) * (0.75 + random.random() * 0.5)
    time.sleep(delay)

def safe_chat(client: openai.Client, *, model: str, messages: List[dict],
              temperature: float = 0.0, max_retries: int = 5, backoff: float = 0.8):
    """
    Wrapper for client.chat.completions.create with retries.
    Returns response on success, or None on final failure (caller must handle).
    """
    for attempt in range(max_retries + 1):
        try:
            return client.chat.completions.create(model=model, messages=messages, temperature=temperature)
        except (RateLimitError, APIConnectionError, APITimeoutError, APIError) as e:
            if attempt >= max_retries:
                return None
            _sleep_with_jitter(backoff, attempt)
        except (BadRequestError, AuthenticationError) as e:
            # Don't retry; these won't improve
            return None
        except Exception:
            if attempt >= max_retries:
                return None
            _sleep_with_jitter(backoff, attempt)

def llm_grade(client: openai.Client, ans: str, official: str, judge_model: str,
              max_retries: int, backoff: float) -> bool:
    judge_msgs = [
        {"role": "system", "content": SYS_JUDGE},
        {"role": "user",
         "content": f"Official solution:\n{official}\n\nStudent answer:\n{ans}\n\nIs the student's answer correct?"}
    ]
    rsp = safe_chat(client, model=judge_model, messages=judge_msgs,
                    temperature=0, max_retries=max_retries, backoff=backoff)
    if rsp is None:
        # Fail open as incorrect (but crucially, do NOT crash the worker)
        return False
    content = (rsp.choices[0].message.content or "").strip().upper()
    return content.startswith("YES")

# ───────────────────────── writer (live NDJSON) ─────────────────────────
def writer_entry(live_path: str, q: mp.Queue):
    """Appends one JSON object per line as results arrive."""
    p = Path(live_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    try:
        with open(p, "a", encoding="utf-8") as f:
            while True:
                item = q.get()
                if item is None or (isinstance(item, dict) and item.get("type") == "STOP"):
                    break
                if isinstance(item, dict) and item.get("type") == "result":
                    rec = item["data"]
                    f.write(json.dumps(rec, ensure_ascii=False) + "\n")
                    f.flush()
                    os.fsync(f.fileno())
    except Exception as e:
        # Writer should never kill the run
        print(f"[writer] ERROR (continuing): {e}", flush=True)

# ───────────────────────── worker main loop ─────────────────────────
def worker_run(shard_id: int,
               api_key: str,
               jobs: List[Dict[str, Any]],
               tools_dir_str: str,
               override_functions_dir_str: Optional[str],
               out_part_path: str,
               sleep_time: float,
               solve_model: str,
               judge_model: str,
               max_retries: int,
               retry_backoff: float,
               live_q: Optional[mp.Queue] = None):
    """
    Each job = {"row": row_dict, "tools": [tool_dict,...]}
    Writes partial results to out_part_path (JSON array) incrementally.
    Streams each finished result to live_q (if provided) as JSONL record.
    Returns stats dict for this shard.
    """
    prefix = f"[W{shard_id}]"
    print(f"{prefix} Starting with {len(jobs)} problems.", flush=True)

    client = openai.Client(api_key=api_key)
    tools_dir = Path(tools_dir_str)
    override_functions_dir = Path(override_functions_dir_str).resolve() if override_functions_dir_str else None

    results: List[Dict[str, Any]] = []
    call_cache: Dict[Tuple[str, str], Any] = {}
    correct = total = 0
    stats = {
        "correct_with_tools": 0,
        "correct_no_tools": 0,
        "wrong_nonnull_with_tools": 0,
        "wrong_nonnull_no_tools": 0,
        "wrong_null_answer": 0,
    }

    def save_part():
        try:
            Path(out_part_path).parent.mkdir(parents=True, exist_ok=True)
            Path(out_part_path).write_text(json.dumps(results, indent=2), encoding="utf-8")
        except Exception as e:
            print(f"{prefix} WARN: could not write part file ({e})", flush=True)

    for idx, job in enumerate(jobs, 1):
        try:
            row = job["row"]
            tools = job["tools"]
            prob, sol = row["problem"], row["solution"]
            tb_view = [{k: t[k] for k in ("name", "description", "inputs")} for t in tools]
            header  = f"Here are the available tools:\n```json\n{json.dumps(tb_view, indent=2)}\n```"

            msgs  = [{"role": "system", "content": SYS_SOLVER},
                     {"role": "user",   "content": header},
                     {"role": "user",   "content": prob}]
            turns: List[Dict[str, Any]] = []
            idle, answered = 0, False

            used_tools = False
            num_tool_actions = 0
            dup_counts = defaultdict(int)

            print(f"{prefix} 🔢  Problem {idx}/{len(jobs)}", flush=True)

            for _ in range(16):
                rsp = safe_chat(client, model=solve_model, messages=msgs,
                                temperature=0, max_retries=max_retries, backoff=retry_backoff)
                if rsp is None:
                    note = "Observation: ERROR – LLM request failed repeatedly; skipping this problem."
                    msgs.append({"role": "user", "content": note})
                    turns.append({"role": "user", "content": note})
                    break

                msg  = rsp.choices[0].message
                text = msg.content or ""
                # message payload may not always have model_dump(); fallback to dict
                if hasattr(msg, "model_dump"):
                    turns.append(msg.model_dump())
                else:
                    turns.append({"role": "assistant", "content": text})

                m = ACT_RE.search(text)
                if m:
                    raw = m.group(1)
                    try:
                        call = json.loads(raw)
                    except json.JSONDecodeError:
                        try:
                            call = ast.literal_eval(raw)
                        except Exception as e:
                            err = f"Observation: ERROR – malformed Action JSON ({e})."
                            msgs += [{"role": "user", "content": err}]
                            turns.append({"role": "user", "content": err}); time.sleep(sleep_time)
                            idle += 1
                            if idle >= 2:
                                remind = ("Reminder – output exactly one Thought line and don’t "
                                          "repeat an identical tool call; use the cached Observation instead.")
                                msgs += [{"role": "user", "content": remind}]
                                turns.append({"role": "user", "content": remind}); idle = 0
                            continue

                    if not isinstance(call, dict) or "name" not in call:
                        err = ("Observation: ERROR – Action must be a JSON object with "
                               '"name" and "arguments" keys.')
                        msgs += [{"role": "user", "content": err}]
                        turns.append({"role": "user", "content": err}); time.sleep(sleep_time)
                        idle += 1
                        if idle >= 2:
                            remind = ("Reminder – output exactly one Thought line and don’t "
                                      "repeat an identical tool call; use the cached Observation instead.")
                            msgs += [{"role": "user", "content": remind}]
                            turns.append({"role": "user", "content": remind}); idle = 0
                        continue

                    args_dict = call.get("arguments", {}) or {}
                    key = _key_for_call(call["name"], args_dict)
                    dup_counts[key] += 1

                    if key in call_cache:
                        obs = call_cache[key]
                        if dup_counts[key] == 1:
                            note = f"Observation (cached): {obs}"
                        elif dup_counts[key] <= MAX_DUP_OBS:
                            note = (f"Observation (cached-duplicate #{dup_counts[key]}): {obs}\n"
                                    f"Reminder: You've already called {call['name']} with the same arguments. "
                                    "Do not call it again; reuse this Observation and move forward.")
                        else:
                            note = (f"Observation (cached-duplicate #{dup_counts[key]}): {obs}\n"
                                    "STOP: Identical Action detected repeatedly. Further identical Actions "
                                    "will be ignored. Proceed to the next reasoning step or output ANSWER.")

                        idle += 1
                        msgs += [{"role": "user", "content": note}]
                        turns.append({"role": "user", "content": note}); time.sleep(sleep_time)
                        if idle >= 2:
                            remind = ("Reminder – output exactly one Thought line and don’t "
                                      "repeat an identical tool call; use the cached Observation instead.")
                            msgs += [{"role": "user", "content": remind}]
                            turns.append({"role": "user", "content": remind}); idle = 0
                        continue
                    else:
                        try:
                            tool = next(t for t in tools if t["name"] == call["name"])
                            obs  = run_tool(tool, args_dict, tools_dir, override_functions_dir)
                            num_tool_actions += 1
                            used_tools = True
                        except StopIteration:
                            obs = f"ERROR: tool '{call['name']}' not found among provided tools."
                        except Exception as e:
                            obs = f"ERROR: {e}"

                        call_cache[key] = obs
                        note = f"Observation ({call['name']}, {_json.dumps(_canon_args(args_dict), separators=(',',':'), sort_keys=True)}): {obs}"
                        msgs += [{"role": "user", "content": note}]
                        turns.append({"role": "user", "content": note}); time.sleep(sleep_time)
                        idle = 0
                        continue

                m = ANS_RE.search(text)
                if m:
                    answered  = True
                    model_ans = m.group(1).strip()
                    is_corr   = llm_grade(client, model_ans, sol, judge_model,
                                          max_retries=max_retries, backoff=retry_backoff)
                    correct  += bool(is_corr)
                    total    += 1

                    if is_corr and used_tools:
                        bucket = "correct_with_tools"; stats[bucket] += 1
                    elif is_corr and not used_tools:
                        bucket = "correct_no_tools"; stats[bucket] += 1
                    elif (not is_corr) and used_tools:
                        bucket = "wrong_nonnull_with_tools"; stats[bucket] += 1
                    else:
                        bucket = "wrong_nonnull_no_tools"; stats[bucket] += 1

                    print(f"{prefix}    Finished {'✅' if is_corr else '❌'} ({bucket})", flush=True)

                    record = {
                        "problem": prob, "solution": sol,
                        "model_answer": model_ans, "is_correct": bool(is_corr),
                        "used_tools": used_tools, "num_tool_actions": num_tool_actions,
                        "tools": [strip_impl(t) for t in tools],
                        "turns": turns
                    }
                    results.append(record)
                    save_part()
                    if live_q is not None:
                        try:
                            live_q.put({"type": "result", "data": record})
                        except Exception:
                            pass
                    break

                # no progress → nudge
                idle += 1
                if idle == 2:
                    remind = ("Reminder – output exactly one Thought line and don’t "
                              "repeat an identical tool call; use the cached Observation instead.")
                    msgs += [{"role": "user", "content": remind}]
                    turns.append({"role": "user", "content": remind}); idle = 0
                else:
                    msgs += [{"role": "assistant", "content": text}]
                time.sleep(sleep_time)

            if not answered:
                total += 1
                stats["wrong_null_answer"] += 1
                print(f"{prefix}    Finished ❌ (no valid ANSWER line)", flush=True)
                record = {
                    "problem": prob, "solution": sol,
                    "model_answer": None, "is_correct": False,
                    "used_tools": used_tools, "num_tool_actions": num_tool_actions,
                    "tools": [strip_impl(t) for t in tools],
                    "turns": turns
                }
                results.append(record)
                save_part()
                if live_q is not None:
                    try:
                        live_q.put({"type": "result", "data": record})
                    except Exception:
                        pass

        except Exception as e:
            # Hard fail for *this* problem only; move on to the next
            print(f"{prefix} ERROR (problem-level, continuing): {e}", flush=True)
            record = {
                "problem": job.get("row", {}).get("problem", ""),
                "solution": job.get("row", {}).get("solution", ""),
                "model_answer": None, "is_correct": False,
                "used_tools": False, "num_tool_actions": 0,
                "tools": [strip_impl(t) for t in job.get("tools", [])],
                "turns": [{"role": "system", "content": f"ERROR: {e}"}]
            }
            results.append(record)
            save_part()
            if live_q is not None:
                try:
                    live_q.put({"type": "result", "data": record})
                except Exception:
                    pass

    return {
        "correct_with_tools": stats["correct_with_tools"],
        "correct_no_tools": stats["correct_no_tools"],
        "wrong_nonnull_with_tools": stats["wrong_nonnull_with_tools"],
        "wrong_nonnull_no_tools": stats["wrong_nonnull_no_tools"],
        "wrong_null_answer": stats["wrong_null_answer"],
        "correct": correct,
        "total": total,
        "out_part_path": out_part_path,
    }

# ────────────────────────────── parent main ──────────────────────────────
def _worker_entry(shard_id, api_key, chunk, tools_dir_str, override_functions_dir_str,
                  out_part_path, sleep_time, solve_model, judge_model, max_retries, retry_backoff, conn, live_q):
    try:
        ret = worker_run(shard_id, api_key, chunk, tools_dir_str,
                         override_functions_dir_str, out_part_path,
                         sleep_time, solve_model, judge_model,
                         max_retries, retry_backoff, live_q)
        conn.send(ret)
    except Exception as e:
        # Never crash the parent; just report empty stats for this shard
        conn.send({
            "correct_with_tools": 0, "correct_no_tools": 0,
            "wrong_nonnull_with_tools": 0, "wrong_nonnull_no_tools": 0,
            "wrong_null_answer": 0, "correct": 0, "total": 0,
            "out_part_path": out_part_path,
        })
        print(f"[W{shard_id}] ERROR (worker-level): {e}", flush=True)
    finally:
        conn.close()

def main():
    rand = random.Random(42)

    tools_path = Path(args.tools_file).resolve()
    tools_dir = tools_path.parent
    TOOLS: List[Dict[str, Any]] = json.loads(tools_path.read_text(encoding="utf-8"))

    BY_PROB: Dict[str, List[Dict[str, Any]]] = {}
    for t in TOOLS:
        BY_PROB.setdefault(t.get("source_problem", "")[:120], []).append(t)

    print("📚  Loading MATH dataset …", flush=True)
    dataset = load_dataset("qwedsacf/competition_math", split=args.split)
    all_rows = list(dataset)
    matching_rows = [row for row in all_rows if BY_PROB.get(row["problem"][:120])]
    total_matching = len(matching_rows)
    print(f"🔎 Problems with ≥1 extracted function: {total_matching}", flush=True)
    if total_matching == 0:
        print("No problems match (no tools found). Exiting.", flush=True)
        return

    rand.shuffle(matching_rows)
    if args.num_examples > 0 and args.num_examples < total_matching:
        samples = matching_rows[:args.num_examples]
        print(f"🧪 Evaluating a subset: {len(samples)} / {total_matching} matching problems "
              f"(set --num-examples 0 to run all).", flush=True)
    else:
        samples = matching_rows
        print(f"🧪 Evaluating ALL matching problems: {len(samples)}", flush=True)

    # Build jobs (row + its tools)
    jobs_all: List[Dict[str, Any]] = []
    for row in samples:
        tools = BY_PROB.get(row["problem"][:120], [])
        jobs_all.append({"row": row, "tools": tools})

    # Keys & workers
    var_names = [v.strip() for v in (args.api_key_vars or "").split(",") if v.strip()]
    keys = [os.environ.get(v) for v in var_names]
    keys = [k for k in keys if k]
    if not keys:
        raise SystemExit("No API keys found. Set them in env vars named by --api-key-vars.")
    num_workers = min(args.num_workers, len(keys), max(1, len(jobs_all)))
    if num_workers < args.num_workers:
        print(f"⚠️  Reducing workers to {num_workers} (limited by available keys / jobs).", flush=True)

    # Shard jobs
    chunks: List[List[Dict[str, Any]]] = [[] for _ in range(num_workers)]
    for i, job in enumerate(jobs_all):
        chunks[i % num_workers].append(job)

    out_path = Path(args.out).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    live_path = Path(args.live_ndjson).resolve() if args.live_ndjson else None
    override_functions_dir = args.functions_dir

    ctx = mp.get_context("spawn")

    # Start writer (if live file requested)
    live_q = None
    writer_proc = None
    if live_path is not None:
        live_q = ctx.Queue(maxsize=1000)
        writer_proc = ctx.Process(target=writer_entry, args=(str(live_path), live_q))
        writer_proc.daemon = False
        writer_proc.start()
        print(f"🟢 Live NDJSON appending to: {live_path}", flush=True)

    # Pipes for worker stats
    parent_conns = []
    procs = []
    for i in range(num_workers):
        api_key = keys[i % len(keys)]
        out_part = f"{str(out_path)}.part{i+1}.json"
        parent_conn, child_conn = ctx.Pipe(False)
        parent_conns.append(parent_conn)
        p = ctx.Process(
            target=_worker_entry,
            args=(i+1, api_key, chunks[i], str(tools_dir), override_functions_dir,
                  out_part, args.sleep, args.model, args.judge_model,
                  args.max_retries, args.retry_backoff, child_conn, live_q)
        )
        p.daemon = False
        p.start()
        procs.append(p)
        child_conn.close()

    # Aggregate stats
    merged_parts = []
    agg = {
        "correct_with_tools": 0,
        "correct_no_tools": 0,
        "wrong_nonnull_with_tools": 0,
        "wrong_nonnull_no_tools": 0,
        "wrong_null_answer": 0,
        "correct": 0,
        "total": 0,
    }

    for pc in parent_conns:
        ret = pc.recv()
        pc.close()
        merged_parts.append(ret["out_part_path"])
        for k in agg.keys():
            if k in ret:
                agg[k] += ret[k]

    for p in procs:
        p.join()

    # Tell writer to stop and join
    if writer_proc is not None and live_q is not None:
        try:
            live_q.put({"type": "STOP"})
            writer_proc.join()
        except Exception:
            pass

    # Merge into final pretty JSON
    full: List[Dict[str, Any]] = []
    # Prefer reading from live NDJSON if it exists
    used_live = False
    if live_path is not None and live_path.exists():
        try:
            with open(live_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    full.append(json.loads(line))
            used_live = True
        except Exception as e:
            print(f"⚠️  Could not read live NDJSON '{live_path}': {e}. Falling back to parts.", flush=True)

    if not used_live:
        for part in merged_parts:
            try:
                part_data = json.loads(Path(part).read_text(encoding="utf-8"))
                full.extend(part_data)
            except Exception as e:
                print(f"⚠️  Could not read part '{part}': {e}", flush=True)

    Path(out_path).write_text(json.dumps(full, indent=2), encoding="utf-8")

    # Final breakdown
    corr_total = agg["correct_with_tools"] + agg["correct_no_tools"]
    wrong_total = (agg["wrong_nonnull_with_tools"] +
                   agg["wrong_nonnull_no_tools"] +
                   agg["wrong_null_answer"])
    acc = 100.0 * agg["correct"] / max(agg["total"], 1)
    print("\nBreakdown (merged):")
    print(f"  ✓ Correct (total)              : {corr_total}")
    print(f"    • Correct w/ tools           : {agg['correct_with_tools']}")
    print(f"    • Correct w/o tools          : {agg['correct_no_tools']}")
    print(f"  ✗ Wrong (total)                : {wrong_total}")
    print(f"    • Wrong (non-null w/ tools)  : {agg['wrong_nonnull_with_tools']}")
    print(f"    • Wrong (non-null w/o tools) : {agg['wrong_nonnull_no_tools']}")
    print(f"    • Wrong (null answer)        : {agg['wrong_null_answer']}")
    print(f"\nFinal Accuracy : {acc:.2f}%  (correct / total = {agg['correct']}/{agg['total']})")
    print(f"📝  Full log saved to {out_path}", flush=True)
    if live_path is not None:
        print(f"🟢  Live NDJSON was written to {live_path}", flush=True)

if __name__ == "__main__":
    main()
