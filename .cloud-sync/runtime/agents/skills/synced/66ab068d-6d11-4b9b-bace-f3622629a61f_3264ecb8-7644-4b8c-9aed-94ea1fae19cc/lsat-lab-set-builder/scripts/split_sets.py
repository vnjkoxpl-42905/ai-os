#!/usr/bin/env python3
"""Split an LSAT question CSV into evenly sized practice sets (file order).

Usage:
    python3 split_sets.py questions.csv --size 100 --out ./out_dir

Writes Set_1.csv ... Set_N.csv into the output dir and prints a summary
(count + PT range) for each set, plus a JSON target list per set that the
browser step can use to tick checkboxes.

Expected CSV columns: file, practiceTest, section, question, questionType,
difficulty, stem (only practiceTest/section/question are required).
"""
import argparse
import csv
import json
import os


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv_path")
    ap.add_argument("--size", type=int, default=100, help="questions per set (default 100)")
    ap.add_argument("--out", default=".", help="output directory")
    args = ap.parse_args()

    with open(args.csv_path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    if not rows:
        raise SystemExit("No rows found in CSV.")

    os.makedirs(args.out, exist_ok=True)
    fieldnames = list(rows[0].keys())
    n = len(rows)
    size = args.size
    chunks = [rows[i:i + size] for i in range(0, n, size)]

    print(f"Total questions: {n} -> {len(chunks)} sets of <= {size}\n")
    for s, chunk in enumerate(chunks, 1):
        out_csv = os.path.join(args.out, f"Set_{s}.csv")
        with open(out_csv, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            w.writerows(chunk)

        # Target keys for the browser step: "TEST-S-Q" with PT stripped.
        targets = [
            f"{r['practiceTest'].replace('PT', '')}-{r['section']}-{r['question']}"
            for r in chunk
        ]
        out_json = os.path.join(args.out, f"Set_{s}_targets.json")
        with open(out_json, "w", encoding="utf-8") as f:
            json.dump(targets, f)

        first = chunk[0]["practiceTest"]
        last = chunk[-1]["practiceTest"]
        print(f"Set {s}: {len(chunk):>3} q | {first} -> {last} | {out_csv}")


if __name__ == "__main__":
    main()
