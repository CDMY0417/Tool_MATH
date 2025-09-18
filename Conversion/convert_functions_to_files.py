#!/usr/bin/env python3
import os
import sys
import json
import argparse
import secrets
import string

ALPHABET = string.ascii_lowercase + string.digits  # 36 chars
ID_LEN = 6


def gen_id(used_ids: set) -> str:
    """Generate a unique 6-char id from [a-z0-9], avoiding collisions with used_ids."""
    while True:
        token = ''.join(secrets.choice(ALPHABET) for _ in range(ID_LEN))
        if token not in used_ids:
            used_ids.add(token)
            return token


def ensure_newline(s: str) -> str:
    return s if s.endswith("\n") else s + "\n"


def main():
    p = argparse.ArgumentParser(description="Convert JSON 'function' strings to .py files and rewrite JSON to reference filenames.")
    p.add_argument("input_json", help="Path to function_rewritten.json")
    p.add_argument("--out-json", default=None,
                   help="Output JSON filename (default: <input_stem>_filenames.json in the same folder)")
    p.add_argument("--out-dirname", default="function_total",
                   help="Directory name to hold the generated .py files (created next to input JSON)")
    args = p.parse_args()

    input_json = os.path.abspath(args.input_json)
    if not os.path.isfile(input_json):
        print(f"ERROR: input JSON not found: {input_json}", file=sys.stderr)
        sys.exit(1)

    base_dir = os.path.dirname(input_json)
    out_dir = os.path.join(base_dir, args.out_dirname)
    os.makedirs(out_dir, exist_ok=True)

    # Decide output JSON path
    if args.out_json is None:
        stem = os.path.splitext(os.path.basename(input_json))[0]
        out_json = os.path.join(base_dir, f"{stem}_filenames.json")
    else:
        out_json = os.path.abspath(args.out_json)

    # Seed used_ids with any existing 6-char basenames already in out_dir (defensive)
    used_ids = set()
    try:
        for fname in os.listdir(out_dir):
            if fname.endswith(".py") and len(fname) == ID_LEN + 3:
                used_ids.add(os.path.splitext(fname)[0])
    except FileNotFoundError:
        pass  # out_dir might not exist yet (handled above by makedirs)

    # Load JSON
    with open(input_json, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"ERROR: Failed to parse JSON: {e}", file=sys.stderr)
            sys.exit(1)

    if not isinstance(data, list):
        print("ERROR: Top-level JSON must be a list of objects.", file=sys.stderr)
        sys.exit(1)

    # Process entries
    rewritten = []
    total = len(data)
    for idx, obj in enumerate(data, start=1):
        if not isinstance(obj, dict):
            print(f"WARNING: Skipping non-object at index {idx-1}", file=sys.stderr)
            continue

        if "function" not in obj:
            print(f"WARNING: Missing 'function' at index {idx-1}; leaving as-is.", file=sys.stderr)
            rewritten.append(obj)
            continue

        code = obj["function"]
        if not isinstance(code, str):
            print(f"WARNING: 'function' is not a string at index {idx-1}; leaving as-is.", file=sys.stderr)
            rewritten.append(obj)
            continue

        # Generate unique filename
        token = gen_id(used_ids)
        py_name = f"{token}.py"
        py_path = os.path.join(out_dir, py_name)

        # Write code to file
        try:
            with open(py_path, "w", encoding="utf-8", newline="\n") as pf:
                pf.write(ensure_newline(code))
        except OSError as e:
            print(f"ERROR: Failed writing {py_path}: {e}", file=sys.stderr)
            sys.exit(1)

        # Replace the function string with the filename
        new_obj = dict(obj)
        new_obj["function"] = py_name
        rewritten.append(new_obj)

        # Lightweight progress every 1000 items
        if idx % 1000 == 0 or idx == total:
            print(f"Processed {idx}/{total}")

    # Write rewritten JSON atomically
    tmp_out = out_json + ".tmp"
    try:
        with open(tmp_out, "w", encoding="utf-8") as outf:
            json.dump(rewritten, outf, ensure_ascii=False, indent=2)
        os.replace(tmp_out, out_json)
    except OSError as e:
        print(f"ERROR: Failed writing output JSON: {e}", file=sys.stderr)
        sys.exit(1)

    print("\nDone.")
    print(f"Python files directory: {out_dir}")
    print(f"Rewritten JSON:         {out_json}")


if __name__ == "__main__":
    main()
