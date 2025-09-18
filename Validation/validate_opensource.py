#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validate_opensource.py  (Transformers-native backend)
---------------------------------------------------------
Validation using ONLY gold tools, run fully in-process with Hugging Face
Transformers (no vLLM, no OpenAI server). Reuses the same ReAct loop and
tool-execution design as evaluation_llama3_8b.py.

Key features:
- Loads tools from function_rewritten_files.json; pairs each MATH problem with its gold tool(s)
- ReAct loop with caching of duplicate tool calls, per-problem wall-clock timeout
- Local "judge" also uses the same HF model (YES/NO)
- Live NDJSON logging + merged JSON
- Backend switch: default "transformers"; still supports "openai" if you want

Requirements:
  pip install -U transformers accelerate datasets

Usage (example):
  python validate_opensource.py \
    --tools-json /data2/.../function_rewritten_files.json \
    --model meta-llama/Meta-Llama-3-8B-Instruct \
    --judge-model meta-llama/Meta-Llama-3-8B-Instruct \
    --backend transformers \
    --num-workers 1 \
    --problem-timeout 180 --call-timeout 120 \
    --out /data2/.../validation_llama3_8b_gold_full.json
"""

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

from datasets import load_dataset

# Optional OpenAI client (only if --backend openai)
try:
    import openai
    from openai import (
        APIError, RateLimitError, APIConnectionError, APITimeoutError,
        BadRequestError, AuthenticationError,
    )
except Exception:
    openai = None

# Optional Transformers (used if --backend transformers)
try:
    import torch
    from transformers import AutoTokenizer, AutoModelForCausalLM
    _HAS_TF = True
except Exception:
    _HAS_TF = False

# ─────────────────────────── CLI ────────────────────────────
P = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
P.add_argument("--tools-json", type=str,
               default="/data2/hyeonjechoi/math_predefined/Test_MATH/function_tools/function_rewritten_files.json",
               help="JSON with list of gold tools; each has 'source_problem' mapping to a MATH problem.")
P.add_argument("--split", type=str, default="train", help="HF split for problem+solution")
P.add_argument("--num-examples", type=int, default=None, help="limit number of problems")
P.add_argument("--model", type=str, default="meta-llama/Meta-Llama-3-8B-Instruct", help="solver model id")
P.add_argument("--judge-model", type=str, default="meta-llama/Meta-Llama-3-8B-Instruct", help="grading model id")
P.add_argument("--backend", type=str, choices=["transformers","openai"], default="transformers",
               help="Inference backend. 'transformers' runs in-process; 'openai' expects OPENAI_BASE_URL.")
P.add_argument("--device", type=str, default="cuda", help="Device when using transformers (e.g., cuda, cuda:0, cpu)")
P.add_argument("--transformers-dtype", type=str, default="bfloat16", choices=["float16","bfloat16","float32"],
               help="Dtype for model weights when using transformers.")
P.add_argument("--max-tokens", type=int, default=512, help="max new tokens per generation")
P.add_argument("--out", type=str,
               default="/data2/hyeonjechoi/math_predefined/Test_MATH/Evaluation/validation_llama3_8b_gold_full.json",
               help="final merged pretty JSON output")
P.add_argument("--live-ndjson", type=str,
               default="/data2/hyeonjechoi/math_predefined/Test_MATH/Evaluation/validation_llama3_8b_gold_full.ndjson",
               help="live JSONL log (appended)")
P.add_argument("--num-workers", type=int, default=1, help="Parallel workers. Use 1 with transformers to avoid OOM.")
P.add_argument("--api-key-vars", type=str, default="mppre_1,mppre_2,mppre_3,mppre_4",
               help="Env var names for OpenAI API keys (only used if --backend openai)")
P.add_argument("--sleep", type=float, default=0.7)
P.add_argument("--max-retries", type=int, default=5)
P.add_argument("--retry-backoff", type=float, default=0.8)
P.add_argument("--problem-timeout", type=float, default=120.0, help="wall-clock seconds per problem")
P.add_argument("--call-timeout", type=float, default=60.0, help="best-effort per-call timeout (openai only)")
args = P.parse_args()

# ───────────────────────── regex & prompts ──────────────────────────
# Accepts: ANSWER:  ..., Answer: ..., Final Answer: ..., **Answer:** ... (last match wins)
ANS_RE = re.compile(r"(?im)^\s*(?:\*+)?\s*(?:final\s+answer|answer)\s*[:：\-]\s*(.+?)\s*$")
# Optional LaTeX fallback if the model writes \boxed{...}
BOXED_RE = re.compile(r"\\boxed\{([^}]+)\}")

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
    ANSWER: <numeric answer>
    IMPORTANT: The final line MUST start with exactly: ANSWER:
""")

SYS_JUDGE = textwrap.dedent("""\
    You are an automated grader for math-contest problems.
    Reply YES if the student's answer is fully correct, otherwise reply NO.
    Reply with ONLY YES or NO.""")

# ───────────────────── tool loader & cache ─────────────────────
def _resolve_tool_path(file_field: str, tools_root: Path, override_dir: Optional[Path]) -> Path:
    cand = Path(file_field)
    if cand.is_absolute() and cand.exists():
        return cand
    cand2 = (tools_root / file_field).resolve()
    if cand2.exists():
        return cand2
    if override_dir:
        cand3 = (override_dir / file_field).resolve()
        if cand3.exists():
            return cand3
    cand4 = (tools_root / "function_total" / file_field).resolve()
    if cand4.exists():
        return cand4
    if not file_field.endswith(".py"):
        return _resolve_tool_path(file_field + ".py", tools_root, override_dir)
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

def _load_callable(t: Dict[str, Any], tools_root: Path, override_dir: Optional[Path]) -> Any:
    if "_impl" in t:
        return t["_impl"]
    file_field = t.get("function")
    if not isinstance(file_field, str):
        raise TypeError(f"tool['function'] must be a filename string; got {type(file_field)}")
    py_path = _resolve_tool_path(file_field, tools_root, override_dir)
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
             tools_root: Path, override_dir: Optional[Path]) -> Any:
    fn = _load_callable(t, tools_root, override_dir)
    return fn(**(kwargs or {}))

def strip_impl(t: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in t.items() if k != "_impl"}

# ─────────────────── canonical cache key helpers ───────────────────
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

# ───────────────────── backends (OpenAI vs Transformers) ─────────────────────
def _sleep_with_jitter(base: float, attempt: int):
    delay = base * (2 ** attempt) * (0.75 + random.random() * 0.5)
    time.sleep(delay)

# ---- OpenAI-style (only if args.backend == "openai") ----
def safe_chat_openai(client, *, model: str, messages: List[dict],
                     temperature: float = 0.0, max_retries: int = 5, backoff: float = 0.8,
                     max_tokens: int = 512, request_timeout: float = 60.0):
    local = client.with_options(timeout=request_timeout)
    for attempt in range(max_retries + 1):
        try:
            return local.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens
            )
        except (RateLimitError, APIConnectionError, APITimeoutError, APIError):
            if attempt >= max_retries:
                return None
            _sleep_with_jitter(backoff, attempt)
        except (BadRequestError, AuthenticationError):
            return None
        except Exception:
            if attempt >= max_retries:
                return None
            _sleep_with_jitter(backoff, attempt)

# ---- Transformers-native (default) ----
class _HFMsg:
    def __init__(self, content: str):
        self.content = content
    def model_dump(self):
        return {"role": "assistant", "content": self.content}

class _HFChoice:
    def __init__(self, msg: _HFMsg):
        self.message = msg

class _HFRsp:
    def __init__(self, text: str):
        self.choices = [_HFChoice(_HFMsg(text))]

def _dtype_of(s: str):
    if not _HAS_TF:
        return None
    s = s.lower()
    if s == "float16":
        return torch.float16
    if s == "bfloat16":
        return torch.bfloat16
    return torch.float32

def init_hf_model(model_id: str, device: str, dtype_str: str):
    if not _HAS_TF:
        raise RuntimeError("Transformers is not installed. pip install transformers accelerate")
    tok = AutoTokenizer.from_pretrained(model_id, use_fast=True, token=os.environ.get("HF_TOKEN"))
    if tok.chat_template is None and not hasattr(tok, "apply_chat_template"):
        # Fallback to raw formatting if template missing (rare)
        pass
    dtype = _dtype_of(dtype_str)
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype=dtype,
        device_map=None
    )
    model.eval()
    if device and device != "auto":
        model.to(device)
    return tok, model

def hf_chat_once(tok, model, device: str, messages: List[dict], max_new_tokens: int = 512,
                 temperature: float = 0.0) -> str:
    # Build prompt with chat template if available (Llama 3 supports it)
    if hasattr(tok, "apply_chat_template"):
        prompt = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    else:
        # Very simple fallback: concatenate roles
        parts = []
        for m in messages:
            parts.append(f"{m.get('role','user').upper()}: {m.get('content','')}")
        parts.append("ASSISTANT:")
        prompt = "\n".join(parts)

    inputs = tok(prompt, return_tensors="pt")
    if device:
        inputs = {k: v.to(device) for k, v in inputs.items()}
    with torch.no_grad():
        out = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=bool(temperature and temperature > 0.0),
            temperature=temperature if temperature and temperature > 0.0 else 1.0,
            eos_token_id=tok.eos_token_id
        )
    gen = out[0][inputs["input_ids"].shape[1]:]
    text = tok.decode(gen, skip_special_tokens=True)
    return text

def safe_chat_transformers(hf_pack, *, model: str, messages: List[dict],
                           temperature: float = 0.0, max_retries: int = 5, backoff: float = 0.8,
                           max_tokens: int = 512, request_timeout: float = 60.0):
    # request_timeout is not enforced in-process; we rely on per-problem wallclock checks.
    tok, mdl, device = hf_pack
    for attempt in range(max_retries + 1):
        try:
            txt = hf_chat_once(tok, mdl, device, messages, max_new_tokens=max_tokens,
                               temperature=temperature)
            return _HFRsp(txt)
        except Exception:
            if attempt >= max_retries:
                return None
            _sleep_with_jitter(backoff, attempt)

# ───────────────────── judge wrapper ─────────────────────
def llm_grade_openai(client, ans: str, official: str, judge_model: str,
                     max_retries: int, backoff: float, max_tokens: int, request_timeout: float) -> bool:
    judge_msgs = [
        {"role": "system", "content": SYS_JUDGE},
        {"role": "user",
         "content": f"Official solution:\n{official}\n\nStudent answer:\n{ans}\n\nIs the student's answer correct?"}
    ]
    rsp = safe_chat_openai(client, model=judge_model, messages=judge_msgs,
                           temperature=0, max_retries=max_retries, backoff=backoff,
                           max_tokens=max_tokens, request_timeout=request_timeout)
    if rsp is None:
        return False
    content = (rsp.choices[0].message.content or "").strip().upper()
    return content.startswith("YES")

def llm_grade_transformers(hf_pack, ans: str, official: str, judge_model_unused: str,
                           max_retries: int, backoff: float, max_tokens: int, request_timeout: float) -> bool:
    judge_msgs = [
        {"role": "system", "content": SYS_JUDGE},
        {"role": "user",
         "content": f"Official solution:\n{official}\n\nStudent answer:\n{ans}\n\nIs the student's answer correct?"}
    ]
    rsp = safe_chat_transformers(hf_pack, model="", messages=judge_msgs,
                                 temperature=0, max_retries=max_retries, backoff=backoff,
                                 max_tokens=max_tokens, request_timeout=request_timeout)
    if rsp is None:
        return False
    content = (rsp.choices[0].message.content or "").strip().upper()
    return content.startswith("YES")

# ───────────────────────── writer (live NDJSON) ─────────────────────────
def writer_entry(live_path: str, q: mp.Queue):
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
        print(f"[writer] ERROR (continuing): {e}", flush=True)

# ───────────────────────── helpers ─────────────────────────
def normalize_problem(s: str) -> str:
    return re.sub(r"\s+", " ", s or "").strip()

# ───────────────────────── worker main loop ─────────────────────────
def worker_run(shard_id: int,
               backend: str,
               api_key: Optional[str],
               hf_pack,  # (tok, model, device) or None
               jobs: List[Dict[str, Any]],
               tools_dir_str: str,
               override_functions_dir_str: Optional[str],
               out_part_path: str,
               sleep_time: float,
               solve_model: str,
               judge_model: str,
               max_retries: int,
               retry_backoff: float,
               max_tokens: int,
               problem_timeout: float,
               call_timeout: float,
               live_q: Optional[mp.Queue] = None):

    prefix = f"[W{shard_id}]"
    print(f"{prefix} Starting with {len(jobs)} problems.", flush=True)

    # Backend clients
    if backend == "openai":
        if openai is None:
            raise RuntimeError("openai package not available; install openai or use --backend transformers")
        client = openai.Client(api_key=api_key)
        chat_fn = lambda **kw: safe_chat_openai(client, **kw)
        grade_fn = lambda ans, sol: llm_grade_openai(client, ans, sol, judge_model,
                                                     max_retries, retry_backoff, max_tokens, call_timeout)
    else:
        # transformers
        chat_fn = lambda **kw: safe_chat_transformers(hf_pack, **kw)
        grade_fn = lambda ans, sol: llm_grade_transformers(hf_pack, ans, sol, judge_model,
                                                           max_retries, retry_backoff, max_tokens, call_timeout)

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
            prob = job["problem"]
            sol  = job["solution"]
            tools = job["tools"]

            used_tool_names = set()
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
            started_at = time.time()

            for _ in range(16):
                # Check problem wall-clock timeout BEFORE each turn
                if time.time() - started_at > problem_timeout:
                    note = f"Observation: TIMEOUT — exceeded {problem_timeout:.0f}s for this problem; skipping."
                    msgs.append({"role": "user", "content": note})
                    turns.append({"role": "user", "content": note})
                    break

                rsp = chat_fn(model=solve_model, messages=msgs,
                              temperature=0, max_retries=max_retries, backoff=retry_backoff,
                              max_tokens=max_tokens, request_timeout=call_timeout)
                if rsp is None:
                    note = "Observation: ERROR – LLM request failed repeatedly; skipping this problem."
                    msgs.append({"role": "user", "content": note})
                    turns.append({"role": "user", "content": note})
                    break

                msg  = rsp.choices[0].message
                text = msg.content or ""
                if hasattr(msg, "model_dump"):
                    turns.append(msg.model_dump())
                else:
                    turns.append({"role": "assistant", "content": text})

                # Action parsing & execution
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
                            used_tool_names.add(tool["name"])
                            obs  = run_tool(tool, args_dict, Path("."), None)
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

                # Answer detection (permissive)
                answered_flag = False
                model_ans = None
                m_iter = list(ANS_RE.finditer(text))
                if m_iter:
                    answered_flag = True
                    model_ans = m_iter[-1].group(1).strip()
                else:
                    b = BOXED_RE.search(text)
                    if b:
                        answered_flag = True
                        model_ans = b.group(1).strip()

                if answered_flag:
                    is_corr = grade_fn(model_ans, sol)
                    correct  += bool(is_corr)
                    total    += 1

                    if is_corr and used_tools:
                        stats["correct_with_tools"] += 1
                    elif is_corr and not used_tools:
                        stats["correct_no_tools"] += 1
                    elif (not is_corr) and used_tools:
                        stats["wrong_nonnull_with_tools"] += 1
                    else:
                        stats["wrong_nonnull_no_tools"] += 1

                    print(f"{prefix}    Finished {'✅' if is_corr else '❌'} "
                          f"({'correct_with_tools' if is_corr and used_tools else 'correct_no_tools' if is_corr else 'wrong_nonnull_with_tools' if used_tools else 'wrong_nonnull_no_tools'})",
                          flush=True)

                    record = {
                        "problem": prob, "solution": sol,
                        "model_answer": model_ans, "is_correct": bool(is_corr),
                        "used_tools": used_tools, "num_tool_actions": num_tool_actions,
                        "used_tool_names": sorted(used_tool_names),
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
                    answered = True
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
                    "used_tool_names": sorted(used_tool_names),
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
            print(f"{prefix} ERROR (problem-level, continuing): {e}", flush=True)
            record = {
                "problem": job.get("problem",""),
                "solution": job.get("solution",""),
                "model_answer": None, "is_correct": False,
                "used_tools": False, "num_tool_actions": 0,
                "used_tool_names": [],
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

# ───────────────────────── parent main ─────────────────────────
def _worker_entry(shard_id, backend, api_key, hf_pack, chunk, tools_dir_str, override_functions_dir_str,
                  out_part_path, sleep_time, solve_model, judge_model,
                  max_retries, retry_backoff, max_tokens, problem_timeout, call_timeout,
                  conn, live_q):
    try:
        ret = worker_run(shard_id, backend, api_key, hf_pack, chunk, tools_dir_str, override_functions_dir_str,
                         out_part_path, sleep_time, solve_model, judge_model,
                         max_retries, retry_backoff, max_tokens, problem_timeout, call_timeout, live_q)
        conn.send(ret)
    except Exception as e:
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

    tools_path = Path(args.tools_json)
    TOOLS = json.loads(tools_path.read_text(encoding="utf-8"))
    by_src: Dict[str, List[dict]] = defaultdict(list)
    for t in TOOLS:
        sp = normalize_problem(t.get("source_problem",""))
        if sp:
            by_src[sp].append(t)

    print(f"🟡  Loaded gold tools for {len(by_src)} problems.", flush=True)
    print("📚  Loading MATH dataset …", flush=True)
    ds = load_dataset("qwedsacf/competition_math", split=args.split)
    SOLN = {normalize_problem(r["problem"]): r["solution"] for r in ds}

    # Build validation jobs (problems that have ≥1 gold tool)
    jobs_all: List[Dict[str, Any]] = []
    kept = 0; dropped = 0
    for r in ds:
        prob = r["problem"]
        pnorm = normalize_problem(prob)
        if pnorm in by_src:
            kept += 1
            jobs_all.append({
                "problem": prob,
                "solution": SOLN.get(pnorm, ""),
                "tools": by_src[pnorm],  # golds only
            })
        else:
            dropped += 1
    print(f"⚙️  Validation set: {kept} with gold | dropped (no gold): {dropped}", flush=True)

    rand.shuffle(jobs_all)
    if args.num_examples is not None:
        jobs_all = jobs_all[:args.num_examples]

    # Backend setup
    backend = args.backend
    hf_pack = None
    if backend == "transformers":
        # Single GPU works best with one worker to avoid OOM
        if not _HAS_TF:
            raise SystemExit("Transformers not available. Install with: pip install -U transformers accelerate")
        print(f"🔧  Loading HF model '{args.model}' on device '{args.device}' ({args.transformers_dtype}) …", flush=True)
        tok, mdl = None, None
        try:
            tok, mdl = init_hf_model(args.model, args.device, args.transformers_dtype)
        except Exception as e:
            raise SystemExit(f"Failed to load HF model: {e}")
        hf_pack = (tok, mdl, args.device)

    # Determine workers & API keys (API keys only for openai backend)
    if backend == "openai":
        var_names = [v.strip() for v in (args.api_key_vars or "").split(",") if v.strip()]
        keys = [os.environ.get(v) for v in var_names]
        keys = [k for k in keys if k]
        if not keys:
            raise SystemExit("No API keys found for openai backend. Set them via --api-key-vars.")
        num_workers = min(args.num_workers, len(keys), max(1, len(jobs_all)))
        key_ring = keys
    else:
        num_workers = min(1 if args.num_workers is None else args.num_workers, max(1, len(jobs_all)))
        if num_workers > 1:
            print("⚠️  With --backend transformers, multiple workers will each load the model (high VRAM).", flush=True)
        key_ring = [None] * num_workers

    print(f"[main] Shard planning with {num_workers} worker(s).", flush=True)
    chunks: List[List[Dict[str, Any]]] = [[] for _ in range(num_workers)]
    for i, job in enumerate(jobs_all):
        chunks[i % num_workers].append(job)

    out_path = Path(args.out).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    live_path = Path(args.live_ndjson).resolve() if args.live_ndjson else None

    ctx = mp.get_context("spawn")
    live_q = None
    writer_proc = None
    if live_path is not None:
        live_q = ctx.Queue(maxsize=1000)
        writer_proc = ctx.Process(target=writer_entry, args=(str(live_path), live_q))
        writer_proc.daemon = False
        writer_proc.start()
        print(f"🟢 Live NDJSON appending to: {live_path}", flush=True)

    parent_conns = []
    procs = []
    for i in range(num_workers):
        api_key = key_ring[i % len(key_ring)] if backend == "openai" else None
        out_part = f"{str(out_path)}.part{i+1}.json"
        parent_conn, child_conn = ctx.Pipe(False)
        parent_conns.append(parent_conn)
        p = ctx.Process(
            target=_worker_entry,
            args=(i+1, backend, api_key, hf_pack, chunks[i], ".", None,
                  out_part, args.sleep, args.model, args.judge_model,
                  args.max_retries, args.retry_backoff, args.max_tokens,
                  args.problem_timeout, args.call_timeout,
                  child_conn, live_q)
        )
        p.daemon = False
        p.start()
        procs.append(p)
        child_conn.close()

    merged_parts = []
    for pc in parent_conns:
        _ = pc.recv()
        pc.close()
        merged_parts.append(f"{str(out_path)}.part{len(merged_parts)+1}.json")

    for p in procs:
        p.join()

    if writer_proc is not None and live_q is not None:
        try:
            live_q.put({"type": "STOP"})
            writer_proc.join()
        except Exception:
            pass

    # Merge results
    full: List[Dict[str, Any]] = []
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
        for part_path in sorted(out_path.parent.glob(out_path.name + ".part*.json")):
            try:
                part_data = json.loads(Path(part_path).read_text(encoding="utf-8"))
                full.extend(part_data)
            except Exception as e:
                print(f"⚠️  Could not read part '{part_path}': {e}", flush=True)

    Path(out_path).write_text(json.dumps(full, indent=2), encoding="utf-8")

    # ───────── Simple breakdown ─────────
    total = len(full)
    corr = sum(1 for r in full if r.get("is_correct"))
    wrong = total - corr
    acc = 100.0 * corr / max(total, 1)
    correct_with_tools = sum(1 for r in full if r.get("is_correct") and r.get("used_tools"))
    correct_no_tools   = sum(1 for r in full if r.get("is_correct") and not r.get("used_tools"))

    def pct(x, d):
        return f"{x} ({100.0 * x / max(d,1):.1f}%)"

    print("\nBreakdown (merged):")
    print(f"  ✓ Correct (total)   : {pct(corr, total)}")
    print(f"    • Correct w/ tools: {pct(correct_with_tools, total)}")
    print(f"    • Correct w/o tools: {pct(correct_no_tools, total)}")
    print(f"  ✗ Wrong (total)     : {pct(wrong, total)}")

    print(f"\nFinal Accuracy : {acc:.2f}%  (correct / total = {corr}/{total})")
    print(f"📝  Full log saved to {out_path}", flush=True)
    if live_path is not None:
        print(f"🟢  Live NDJSON was written to {live_path}", flush=True)

if __name__ == "__main__":
    main()
