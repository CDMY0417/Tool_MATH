#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Build a filtered tool list from validation results.

Reads a validation NDJSON (produced by validate_llama3_8b_gold.py) and emits a
JSON list containing ONLY the tools that were:
  - provided as gold tools for a problem,
  - actually used by the model on that problem, and
  - the model's final answer was correct.

Output tool entries preserve the original fields:
  name, description, inputs, function, source_problem, source_solution

Usage:
  python build_filtered_tools_from_validation.py \
    --in /data2/.../validation_llama3_8b_gold_full.ndjson \
    --out /data2/.../function_tools_filtered_Llama3_8b.json
"""

import argparse, json, re
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple

# Fallback regexes to extract tool names from turns content if needed
OBS_ACT_RE = re.compile(r'Action\s*:\s*\{[^}]*"name"\s*:\s*"([A-Za-z0-9_]+)"', re.M)
OBS_RE = re.compile(r"Observation\s*\(\s*([A-Za-z0-9_]+)\s*,\s*\{", re.M)

def normalize_text(s: str) -> str:
    import re as _re
    return _re.sub(r"\s+", " ", (s or "")).strip()

def load_ndjson(path: Path) -> List[Dict[str, Any]]:
    items: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
                if isinstance(obj, dict):
                    items.append(obj)
            except Exception:
                # skip malformed lines
                pass
    return items

def extract_used_tool_names_from_turns(turns: List[Dict[str, Any]]) -> Set[str]:
    names: Set[str] = set()
    for t in (turns or []):
        content = t.get("content") or ""
        for m in OBS_RE.finditer(content):
            names.add(m.group(1))
        for m in OBS_ACT_RE.finditer(content):
            names.add(m.group(1))
    return names

def strip_impl_fields(t: Dict[str, Any]) -> Dict[str, Any]:
    # Keep exactly the canonical fields we want in the output file
    keep = ("name", "description", "inputs", "function", "source_problem", "source_solution")
    out = {}
    for k in keep:
        if k in t:
            out[k] = t[k]
    return out

def main():
    ap = argparse.ArgumentParser(description="Filter validated (correct + used gold) tools into a consolidated JSON.")
    ap.add_argument("--in", dest="inp", required=True,
                    help="Path to validation NDJSON (e.g., validation_llama3_8b_gold_full.ndjson)")
    ap.add_argument("--out", dest="out", required=True,
                    help="Path to write filtered JSON (e.g., function_tools_filtered_Llama3_8b.json)")
    args = ap.parse_args()

    inp_path = Path(args.inp)
    out_path = Path(args.out)

    records = load_ndjson(inp_path)
    kept: List[Dict[str, Any]] = []

    # Use a set to dedupe by (name, source_problem) so we keep one entry per tool/problem pair
    seen: Set[Tuple[str, str]] = set()

    kept_cnt = 0
    total = 0

    for r in records:
        total += 1
        if not r.get("is_correct"):
            continue

        # Get used tool names (prefer provided list; fallback to parsing turns)
        used: Set[str] = set(r.get("used_tool_names") or [])
        if not used:
            used = extract_used_tool_names_from_turns(r.get("turns") or [])

        if not used:
            # no tools used → skip
            continue

        tools: List[Dict[str, Any]] = r.get("tools") or []
        if not tools:
            continue

        # gold tools for the record are in r["tools"]; select only those that were actually used
        for t in tools:
            nm = t.get("name")
            if not nm or nm not in used:
                continue

            # Build a clean tool entry
            clean = strip_impl_fields(t)

            # Some tool JSONs may not carry source_solution; try to preserve if present in tool
            # Otherwise, we cannot reconstruct it here (we don't have MATH mapping in this script)
            sp = normalize_text(clean.get("source_problem", ""))
            key = (nm, sp)
            if key in seen:
                continue

            # Only keep if it has the essential fields
            if "name" in clean and "function" in clean and "source_problem" in clean:
                kept.append(clean)
                seen.add(key)
                kept_cnt += 1

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(kept, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"[done] wrote {len(kept)} tool entries to: {out_path}")
    print(f"[info] scanned {total} validation records, kept only (correct + used gold tools).")

if __name__ == "__main__":
    main()
