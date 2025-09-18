#!/usr/bin/env python3
# rewrite_tools_with_deletion_marker.py
#
#  • Python ≥3.8  • openai-python ≥1.0
#  • Model may delete a tool by returning {"__delete__": true}
#  • Two JSON files are stream-saved after EACH LLM result:
#        1) function_tools_total_rewritten.json  (full registry, deletions removed)
#        2) function_tools_sample_diff.json      (only sampled tools; rewritten = null if deleted)
# ------------------------------------------------------------------------------

import argparse, asyncio, ast, json, os, random, sys, textwrap
from pathlib import Path
from typing import Any, Dict, List, Optional

from openai import AsyncOpenAI
from jsonschema import validate
from tqdm import tqdm

# ─────────────────────────── configuration ────────────────────────────
ROOT = Path("/data2/hyeonjechoi/math_predefined/Test_MATH/function_tools")
SRC      = ROOT / "function_tools_total.json"
DST_FULL = ROOT / "function_tools_total_rewritten.json"
DST_DIFF = ROOT / "function_tools_sample_diff.json"

MODEL          = "gpt-4o"
TEMPERATURE    = 0.2
TIMEOUT        = 60         # seconds for one call
MAX_CONCURRENCY = 8         # parallel LLM calls

SYSTEM_PROMPT = """\
You are an expert Python API documenter and refactorer.

For each TOOL object:
1. If the *description* is unclear, lacks parameter info, or is problem-specific,
   rewrite it so that
     • it starts with an imperative verb,
     • it lists & explains every parameter,
     • it is general enough for any valid input.
2. If you change the description, update the `inputs` dict and the Python
   `function` signature so that parameter names & types MATCH exactly.
   Types must be valid Python type hints (e.g. int, float, List[int]).
3. If the tool is **entirely** problem-specific and unsuitable for reuse,
   return the JSON object:  { "__delete__": true }   (nothing else).
4. NEVER modify the `source_problem` or `source_solution` fields.

Return *only* a JSON object with the same keys
(name, description, inputs, function, source_problem, source_solution)
or the delete marker above. No markdown, no commentary.
"""

SCHEMA = {
    "type": "object",
    "properties": {
        "name":            {"type": "string"},
        "description":     {"type": "string"},
        "inputs":          {"type": "object"},
        "function":        {"type": "string"},
        "source_problem":  {"type": "string"},
        "source_solution": {"type": "string"}
    },
    "required": ["name","description","inputs","function",
                 "source_problem","source_solution"]
}

# ─────────────────────────── helpers ────────────────────────────
def safe_parse(code: str) -> Optional[ast.AST]:
    try:
        return ast.parse(textwrap.dedent(code))
    except SyntaxError:
        return None

def sig_matches_inputs(tree: ast.AST, inputs: Dict[str, Any]) -> bool:
    fns = [n for n in tree.body if isinstance(n, ast.FunctionDef)]
    if not fns:
        return False
    args = [a.arg for a in fns[0].args.args]
    return set(args) == set(inputs.keys())

def validate_tool(tool: Dict[str, Any], original: Dict[str, Any]) -> None:
    validate(instance=tool, schema=SCHEMA)
    if (tool["source_problem"] != original["source_problem"] or
        tool["source_solution"] != original["source_solution"]):
        raise ValueError("source_problem/solution altered")
    ast_mod = safe_parse(tool["function"])
    if ast_mod is None or not sig_matches_inputs(ast_mod, tool["inputs"]):
        raise ValueError("function signature ≠ inputs dict")

def write_json(path: Path, obj: Any) -> None:
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2))

# ─────────────────────────── LLM wrapper ────────────────────────────
client = AsyncOpenAI()

async def rewrite_one(tool: Dict[str, Any]) -> Dict[str, Any]:
    prompt_obj = json.dumps(tool, ensure_ascii=False, indent=2)
    resp = await client.chat.completions.create(
        model = MODEL,
        temperature = TEMPERATURE,
        timeout = TIMEOUT,
        response_format = {"type": "json_object"},
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",
             "content": f"Rewrite if needed (or delete) and reply with JSON only:\n\n{prompt_obj}"}
        ]
    )
    return json.loads(resp.choices[0].message.content)

# ─────────────────────────── main async ────────────────────────────
async def main(sample_n: Optional[int]) -> None:
    original: List[Dict[str, Any]] = json.loads(SRC.read_text())
    total = len(original)

    # choose indices to process
    if sample_n and sample_n < total:
        idx_sample = set(random.sample(range(total), sample_n))
        print(f"✂️  Sampling {len(idx_sample)}/{total} tools")
    else:
        idx_sample = set(range(total))
        print(f"🔄  Rewriting ALL {total} tools")

    # full registry initially same as original
    full_out: List[Optional[Dict[str, Any]]] = original.copy()
    diff_out: List[Dict[str, Any]] = []

    # initial write to disk
    write_json(DST_FULL, full_out)        # no deletions yet
    write_json(DST_DIFF, diff_out)

    sem = asyncio.Semaphore(MAX_CONCURRENCY)

    async def worker(i: int):
        async with sem:
            orig = original[i]
            try:
                new_tool = await rewrite_one(orig)  # dict with data OR delete marker
                if isinstance(new_tool, dict) and new_tool.get("__delete__") is True:
                    # deletion
                    rewritten_entry = None
                    full_out[i] = None
                else:
                    validate_tool(new_tool, orig)
                    rewritten_entry = new_tool
                    full_out[i] = new_tool
            except Exception as e:
                print(f"[WARN] idx {i} «{orig['name']}»: keep original ({e})",
                      file=sys.stderr)
                rewritten_entry = orig
                full_out[i] = orig

            diff_out.append({
                "name": orig["name"],
                "original": orig,
                "rewritten": rewritten_entry  # may be None
            })

            write_json(DST_FULL, [t for t in full_out if t is not None])
            write_json(DST_DIFF, diff_out)

    tasks = [asyncio.create_task(worker(i)) for i in idx_sample]

    for fut in tqdm(asyncio.as_completed(tasks),
                    total=len(tasks), desc="LLM"):
        await fut

    print(f"✅  Finished.\n    Full registry → {DST_FULL}\n    Diff log     → {DST_DIFF}")

# ─────────────────────────── CLI bootstrap ────────────────────────────
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Rewrite / delete sampled tools with streaming updates.")
    parser.add_argument("-n","--num_functions", type=int,
                        help="Random sample size (default: all)")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    random.seed(args.seed)
    if not os.getenv("OPENAI_API_KEY"):
        sys.exit("OPENAI_API_KEY not set")

    asyncio.run(main(args.num_functions))
