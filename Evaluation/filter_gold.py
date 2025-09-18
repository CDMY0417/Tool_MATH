#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
filter_gold.py
--------------
Filter the rewritten tool set using an evaluation log:

Rules
1) If a problem is incorrect (is_correct == False), remove ALL functions
   whose source_problem matches that problem.
2) If a problem is correct (is_correct == True), keep ONLY the functions that
   were actually called in the evaluation turns; erase all unused functions.

Inputs (defaults match your paths):
  --eval-json   /data2/hyeonjechoi/math_predefined/Test_MATH/ReAct/MATH_ReAct_prompt_file.json
  --tools-json  /data2/hyeonjechoi/math_predefined/Test_MATH/function_tools/function_rewritten_files.json

Output (default):
  --out-json    /data2/hyeonjechoi/math_predefined/Test_MATH/Evaluation/function_tools_filtered.json

Usage:
  python filter_gold.py
  # or with explicit paths:
  python filter_gold.py --eval-json .../MATH_ReAct_prompt_file.json \
                        --tools-json .../function_rewritten_files.json \
                        --out-json .../function_tools_filtered.json
"""

from __future__ import annotations
import argparse
import json
import re
from pathlib import Path
from typing import Dict, List, Set


# ------------------------------ Defaults ------------------------------

DEFAULT_EVAL = "/data2/hyeonjechoi/math_predefined/Test_MATH/ReAct/MATH_ReAct_prompt_file.json"
DEFAULT_TOOLS = "/data2/hyeonjechoi/math_predefined/Test_MATH/function_tools/function_rewritten_files.json"
DEFAULT_OUT = "/data2/hyeonjechoi/math_predefined/Test_MATH/Evaluation/function_tools_filtered.json"


# ------------------------------ Helpers ------------------------------

_WS_RE = re.compile(r"\s+")

def norm_text(s: str) -> str:
    """Whitespace-normalize problem text so we can match safely."""
    return _WS_RE.sub(" ", s).strip()


_ACTION_TOOL_RE = re.compile(
    r'Action:\s*\{\s*"name"\s*:\s*"([^"]+)"', flags=re.IGNORECASE
)
_OBS_TOOL_RE = re.compile(
    r'Observation\s*\(\s*([A-Za-z0-9_]+)\s*,', flags=re.IGNORECASE
)

def extract_used_tools_from_turns(turns: List[dict]) -> Set[str]:
    """
    Parse 'turns' to recover tool names that were actually called.
    We look for both 'Action: {"name":"..."}' in assistant content and
    'Observation (tool_name, ...)' lines as a fallback.
    """
    used = set()
    for t in turns or []:
        content = t.get("content") or ""
        # Prefer explicit Action lines
        for m in _ACTION_TOOL_RE.finditer(content):
            used.add(m.group(1))
        # Fallback: Observation lines (mirrors earlier actions)
        for m in _OBS_TOOL_RE.finditer(content):
            used.add(m.group(1))
    return used


# ------------------------------ Core logic ------------------------------

def build_problem_usage_index(eval_items: List[dict]) -> Dict[str, dict]:
    """
    From the evaluation JSON, return a dict:
      key = normalized problem text
      val = {
        "is_correct": bool,
        "used_tools": set(str),   # tool names that were called at least once
      }

    If the same problem appears multiple times, we OR the correctness
    and union the used tool names (conservative: keep only if there exists
    a correct run; otherwise it will be dropped).
    """
    idx: Dict[str, dict] = {}
    for item in eval_items:
        problem = norm_text(item.get("problem", ""))
        if not problem:
            continue
        is_correct = bool(item.get("is_correct", False))
        used_names = extract_used_tools_from_turns(item.get("turns", []))

        if problem not in idx:
            idx[problem] = {"is_correct": is_correct, "used_tools": set(used_names)}
        else:
            # If any run is correct, treat the problem as correct
            idx[problem]["is_correct"] = idx[problem]["is_correct"] or is_correct
            idx[problem]["used_tools"].update(used_names)

    return idx


def filter_tools(
    all_tools: List[dict],
    usage_idx: Dict[str, dict],
) -> List[dict]:
    """
    Apply the filtering rules to the tools list.

    Keep a tool T iff:
      - Its source_problem exists in usage_idx, and
      - usage_idx[source_problem]["is_correct"] is True, and
      - T["name"] is in usage_idx[source_problem]["used_tools"]

    Everything else is dropped.
    """
    kept: List[dict] = []
    dropped_incorrect = 0
    dropped_unused = 0
    no_eval_entry = 0

    for tool in all_tools:
        sp = norm_text(tool.get("source_problem", ""))
        name = tool.get("name", "")

        usage = usage_idx.get(sp)
        if usage is None:
            # No evaluation entry for this problem → cannot verify, drop
            no_eval_entry += 1
            continue

        if not usage["is_correct"]:
            # Incorrect problem → remove entirely
            dropped_incorrect += 1
            continue

        if name not in usage["used_tools"]:
            # Correct problem, but this particular function wasn't called → erase
            dropped_unused += 1
            continue

        kept.append(tool)

    # Simple summary for user
    print(f"[filter] kept {len(kept)} tools")
    print(f"[filter] dropped (incorrect problems): {dropped_incorrect}")
    print(f"[filter] dropped (unused functions on correct problems): {dropped_unused}")
    print(f"[filter] dropped (no evaluation entry): {no_eval_entry}")
    return kept


# ------------------------------ CLI ------------------------------

def main():
    ap = argparse.ArgumentParser(
        description="Filter tool JSON using evaluation correctness & actually-used tools."
    )
    ap.add_argument("--eval-json", default=DEFAULT_EVAL, type=Path,
                    help="Evaluation JSON (ReAct run with turns and correctness).")
    ap.add_argument("--tools-json", default=DEFAULT_TOOLS, type=Path,
                    help="Rewritten functions JSON to be filtered.")
    ap.add_argument("--out-json", default=DEFAULT_OUT, type=Path,
                    help="Output filtered tools JSON.")
    args = ap.parse_args()

    # Load files
    eval_items = json.loads(args.eval_json.read_text(encoding="utf-8"))
    all_tools = json.loads(args.tools_json.read_text(encoding="utf-8"))

    # Build usage index from evaluation
    usage_idx = build_problem_usage_index(eval_items)

    # Filter tools by rules
    filtered = filter_tools(all_tools, usage_idx)

    # Write output
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(filtered, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[filter] wrote filtered tools → {args.out_json}")


if __name__ == "__main__":
    main()
