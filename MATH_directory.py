#!/usr/bin/env python3
"""
MATH_directory.py
Extract **multiple** reusable Python-tool functions from the
qwedsacf/competition_math dataset using GPT-4o.
"""

import argparse, os, json, time
from collections import defaultdict
from datasets import load_dataset
from tqdm import tqdm
from openai import OpenAI

# --------------------------------------------------------------------- #
# 1. CLI
# --------------------------------------------------------------------- #
parser = argparse.ArgumentParser(
    description="Extract function tools from the MATH dataset with GPT-4o."
)
parser.add_argument("--max-examples", type=int, default=12_500,
                    help="How many dataset examples to process")
parser.add_argument("--sleep", type=float, default=1.0,
                    help="Seconds to sleep between OpenAI calls "
                         "(be kind to the rate limits)")
args = parser.parse_args()

# --------------------------------------------------------------------- #
# 2. OpenAI client  (expects $OPENAI_API_KEY)
# --------------------------------------------------------------------- #
client = OpenAI()

# --------------------------------------------------------------------- #
# 3. Dataset
# --------------------------------------------------------------------- #
dataset = load_dataset("qwedsacf/competition_math", split="train")

# --------------------------------------------------------------------- #
# 4. Config
# --------------------------------------------------------------------- #
ALLOWED_TYPES = {"int", "float", "str", "bool", "list", "tuple", "dict", "set"}

# --------------------------------------------------------------------- #
# 5. Prompt
# --------------------------------------------------------------------- #
def make_tool_prompt(problem: str, solution: str) -> str:
    """
    Ask GPT-4o to return a *list* of reusable helper functions in JSON.
    """
    return f"""
You are a Python function‐generator for a math-solver system.

**Task**
Extract every *reusable* helper function that appears implicitly in the
following solved problem.  Each function should capture a general
mathematical operation (e.g. “count the number of integers in an interval”,
“compute the number of ways to arrange k indistinguishable items among n bins”,
etc.).  Aim for **multiple small functions** if the solution has several
distinct steps.

**Output format**
Return a **JSON array**.  Each element is an object with **exactly** these keys:
- "name"        – concise snake_case identifier
- "description" – what the function does
- "inputs"      – dict {{"param": "<python_type>"}}
                 allowed types: {sorted(ALLOWED_TYPES)}
- "function"    – full Python `def` (no explanations)

Example (array with two functions):
[
  {{
    "name": "common_divisors",
    "description": "Return sorted list of common divisors of a and b.",
    "inputs": {{"a": "int", "b": "int"}},
    "function": "def common_divisors(a: int, b: int):\\n    ...return divs"
  }},
  {{
    "name": "integer_points_in_interval",
    "description": "Number of integers in the open interval (lo, hi].",
    "inputs": {{"lo": "int", "hi": "int"}},
    "function": "def integer_points_in_interval(lo: int, hi: int):\\n    ...return count"
  }}
]

If **no reusable function** can be identified, output an *empty array* `[]`.
Do NOT wrap the JSON in markdown fences.
---
Problem:
{problem}

Solution:
{solution}
"""

# --------------------------------------------------------------------- #
# 6. Helpers
# --------------------------------------------------------------------- #
def strict_types_ok(tool_obj: dict) -> bool:
    try:
        return all(t in ALLOWED_TYPES for t in tool_obj["inputs"].values())
    except Exception:
        return False

def attach_provenance(tool: dict, problem: str, solution: str) -> dict:
    tool["source_problem"]  = problem
    tool["source_solution"] = solution
    return tool

# --------------------------------------------------------------------- #
# 7. Extraction loop
# --------------------------------------------------------------------- #
tools_by_type_level = defaultdict(lambda: defaultdict(list))
tools_total         = []

for item in tqdm(dataset.select(range(args.max_examples)),
                 desc="Extracting tools"):
    problem, solution = item["problem"], item["solution"]
    prob_type         = item.get("type",   "Unknown").strip()
    prob_level        = item.get("level",  "Level ?").strip()

    prompt = make_tool_prompt(problem, solution)

    try:
        resp = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        raw_reply = resp.choices[0].message.content.strip()

        if not raw_reply:
            continue

        # Parse JSON (expect array)
        try:
            maybe_list = json.loads(raw_reply)
        except json.JSONDecodeError:
            print("⚠️ JSON decode error; raw reply:\n", raw_reply)
            continue

        # Accept either a single object or a list
        tools_list = maybe_list if isinstance(maybe_list, list) else [maybe_list]

        for tool in tools_list:
            required_keys = {"name", "description", "inputs", "function"}
            if not required_keys.issubset(tool):
                continue
            if not strict_types_ok(tool):
                continue

            tool = attach_provenance(tool, problem, solution)
            tools_by_type_level[prob_type][prob_level].append(tool)
            tools_total.append(tool)

    except Exception as e:
        print("⚠️ OpenAI error:", e)
        continue
    finally:
        time.sleep(args.sleep)

# --------------------------------------------------------------------- #
# 8. Save results
# --------------------------------------------------------------------- #
out_dir = "function_tools"
os.makedirs(out_dir, exist_ok=True)

#   a) structured by type / level
for typ, levels in tools_by_type_level.items():
    typ_dir = os.path.join(out_dir, typ.replace("&", "and").replace(" ", "_"))
    os.makedirs(typ_dir, exist_ok=True)
    for lvl, tl in levels.items():
        fname = os.path.join(typ_dir, f"{lvl.replace(' ', '_')}.json")
        with open(fname, "w") as f:
            json.dump(tl, f, indent=2)

#   b) unified list
with open(os.path.join(out_dir, "function_tools_total.json"), "w") as f:
    json.dump(tools_total, f, indent=2)

print(f"✅ Processed {args.max_examples} examples.")
print(f"📁 Tools organised in: {out_dir}/")
print(f"📄 Unified file: {out_dir}/function_tools_total.json "
      f"({len(tools_total)} total functions)")
