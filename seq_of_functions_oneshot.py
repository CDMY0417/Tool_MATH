#!/usr/bin/env python
"""
gold_trace_pipeline.py  –  MATH → tool-call traces (1-shot exemplar, random sampling)

Usage
-----
export OPENAI_API_KEY=...
python gold_trace_pipeline.py --num-examples 10 --split train
"""

import os, re, json, textwrap, argparse, random
from pathlib import Path
from importlib import util as import_util
from types import FunctionType

from datasets import load_dataset
from tqdm import tqdm
from openai import OpenAI            # v1 client (>=1.0.0)

# ---------------------------------------------------------------------------
# Default paths & CLI
# ---------------------------------------------------------------------------

DEFAULT_TOOLS = "/data2/hyeonjechoi/math_predefined/Test_MATH/function_tools/function_tools_total.json"
DEFAULT_OUT   = "/data2/hyeonjechoi/math_predefined/Test_MATH/seq_of_functions.json"
HF_NAME       = "qwedsacf/competition_math"
MODEL         = "gpt-4o-mini"

ap = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
ap.add_argument("--tools", default=DEFAULT_TOOLS, help="JSON with ALL extracted tools")
ap.add_argument("--out",   default=DEFAULT_OUT,  help="Output file (JSON)")
ap.add_argument("--split", default="train",      help="HF split (train|test|valid)")
ap.add_argument("--num-examples", type=int, default=None,
                help="Randomly sample this many target problems (after exemplar)")
args = ap.parse_args()

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def normalise(txt: str) -> str:
    return re.sub(r"\s+", " ", txt).strip()

def load_tools(path):
    with open(path, "r", encoding="utf-8") as fh:
        tools = json.load(fh)
    idx = {}
    for t in tools:
        idx.setdefault(normalise(t["source_problem"]), []).append(t)
    return idx

def build_prompt(problem, solution, tools):
    SYSTEM = ("You convert a worked maths solution into an ordered list of function calls. "
              "Use *only* the provided tools and reply with a JSON object "
              "like {'sequence':[ ... ]}.")
    USER = textwrap.dedent(f"""
        • Problem:
        {problem}

        • Worked solution:
        {solution}

        • Available tools (JSON):
        {json.dumps(tools, indent=2)}

        Format exactly:
        {{
          "sequence":[
            {{"call":"fn_name","args":{{…}}}},
            …
          ]
        }}
    """)
    return [
        {"role":"system","content":SYSTEM},
        {"role":"user",  "content":USER}
    ]

# ---------------------------------------------------------------------------
# 1-shot exemplar
# ---------------------------------------------------------------------------

EXEMPLAR = {
    "problem": r"Find all the integer roots of\n\[x^3 - 3x^2 - 13x + 15 = 0.\]Enter all the integer roots, separated by commas.",
    "solution": r"By the Integer Root Theorem, the possible integer roots are all the divisors of 15 (including negative divisors), which are $-15,$ $-5,$ $-3,$ $-1,$ $1,$ $3,$ $5,$ and $15.$  Checking, we find that the only integer roots are $\boxed{-3,1,5}.$",
    "tools": [
        {
            "name": "integer_divisors",
            "description": "Return a list of all positive and negative divisors of an integer n.",
            "inputs": {"n": "int"},
            "function": "def integer_divisors(n: int):\n    divisors = []\n    for i in range(1, abs(n) + 1):\n        if n % i == 0:\n            divisors.extend([i, -i])\n    return divisors"
        },
        {
            "name": "check_polynomial_root",
            "description": "Check if a given integer is a root of the polynomial x^3 - 3x^2 - 13x + 15.",
            "inputs": {"x": "int"},
            "function": "def check_polynomial_root(x: int):\n    return x**3 - 3*x**2 - 13*x + 15 == 0"
        }
    ],
    "trace": [
        {"call":"integer_divisors",    "args":{"n":15}},
        {"call":"check_polynomial_root","args":{"x":1}},
        {"call":"check_polynomial_root","args":{"x":-1}},
        {"call":"check_polynomial_root","args":{"x":3}},
        {"call":"check_polynomial_root","args":{"x":-3}},
        {"call":"check_polynomial_root","args":{"x":5}},
        {"call":"check_polynomial_root","args":{"x":-5}},
        {"call":"check_polynomial_root","args":{"x":15}},
        {"call":"check_polynomial_root","args":{"x":-15}}
    ]
}
EXEMPLAR_ASSIST = json.dumps({"sequence": EXEMPLAR["trace"]}, indent=2)

# ---------------------------------------------------------------------------
# OpenAI tool schema (object with key "sequence")
# ---------------------------------------------------------------------------

TOOL_SCHEMA = [{
    "type": "function",
    "function": {
        "name": "emit_call_sequence",
        "description": "Return the ordered tool-call list",
        "parameters": {
            "type":"object",
            "properties": {
                "sequence": {
                    "type":"array",
                    "items":{
                        "type":"object",
                        "properties":{
                            "call":{"type":"string"},
                            "args":{"type":"object"}
                        },
                        "required":["call","args"]
                    }
                }
            },
            "required":["sequence"]
        }
    }
}]

client = OpenAI()   # uses $OPENAI_API_KEY

def call_llm(messages):
    resp = client.chat.completions.create(
        model       = MODEL,
        messages    = messages,
        tools       = TOOL_SCHEMA,
        tool_choice = {"type":"function","function":{"name":"emit_call_sequence"}},
        temperature = 0.0,
    )
    args_json = resp.choices[0].message.tool_calls[0].function.arguments
    return json.loads(args_json)["sequence"]

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    tool_index = load_tools(args.tools)

    print("⤵  Loading dataset from HuggingFace…")
    dataset = load_dataset(HF_NAME, split=args.split)

    if args.num_examples:
        rand = random.Random(42)
        dataset = rand.sample(list(dataset), args.num_examples)

    out = []
    out.append({"problem":EXEMPLAR["problem"],
                "solution":EXEMPLAR["solution"],
                "tools":EXEMPLAR["tools"],
                "trace":EXEMPLAR["trace"]})

    for row in tqdm(dataset, desc="Building traces"):
        prob, sol = row["problem"], row["solution"]
        tools = tool_index.get(normalise(prob), [])
        if not tools:
            continue

        # Few-shot prompt = exemplar + target
        messages = [
            {"role":"system","content":"You are a helpful assistant."},
            {"role":"user",   "content": textwrap.dedent(f"""
                • Problem:
                {EXEMPLAR['problem']}

                • Worked solution:
                {EXEMPLAR['solution']}

                • Available tools:
                {json.dumps(EXEMPLAR['tools'], indent=2)}
            """)},
            {"role":"assistant","content":EXEMPLAR_ASSIST},
        ]
        messages += build_prompt(prob, sol, tools)

        try:
            trace = call_llm(messages)
        except Exception as e:
            print(f"\n⚠️  LLM call failed: {e}")
            continue

        out.append({"problem":prob, "solution":sol, "tools":tools, "trace":trace})

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    with open(args.out,"w",encoding="utf-8") as fh:
        json.dump(out, fh, indent=2)
    print(f"✅  Saved {len(out)} entries → {args.out}")

if __name__ == "__main__":
    main()
