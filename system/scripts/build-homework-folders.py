#!/usr/bin/env python3
"""Write students/<slug>/homework/already-assigned/index.md for each current student.

Read-only against LSAT U (uses `lsatu items`). Lists every note, drill, bootcamp
module, activity and homework set assigned to the student, with status and dates.
Internal only: never posted to students. Re-run to refresh.

Usage: py -I system/scripts/build-homework-folders.py [slug ...]
"""
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LSATU = ROOT / "system" / "scripts" / "lsatu"
BASH = "C:/Program Files/Git/bin/bash.exe"
ITEM = re.compile(r"^\s+([0-9a-f-]{36})\s+\[([^\]]+)\]\s+(.*)$")


def current():
    r = subprocess.run([sys.executable, "-I", str(ROOT / "system/scripts/recap-status.py"), "90"],
                       capture_output=True, text=True, encoding="utf-8")
    return json.loads(r.stdout)["students"]


def items(email):
    r = subprocess.run([BASH, str(LSATU), "items", email], capture_output=True, text=True,
                       encoding="utf-8", timeout=120, cwd=ROOT)
    if r.returncode != 0 or "item(s)" not in r.stdout:
        raise RuntimeError(f"lsatu failed for {email}: {(r.stderr or r.stdout)[:120]}")
    rows = []
    for line in r.stdout.splitlines():
        m = ITEM.match(line)
        if m:
            parts = [p.strip() for p in m.group(3).split("·")]
            added = next((p[6:] for p in parts if p.startswith("added ")), "")
            rows.append((m.group(1), m.group(2), [p for p in parts if not p.startswith("added ")], added))
    return rows


def write(s, rows):
    out = ROOT / "students" / s["slug"] / "homework" / "already-assigned"
    out.mkdir(parents=True, exist_ok=True)
    lines = [
        "---",
        f"title: Already assigned to {s['name']}",
        f"student: {s['slug']}",
        f"items: {len(rows)}",
        f"latest_added: {max((r[3] for r in rows if r[3]), default='')}",
        f"refreshed: {date.today().isoformat()}",
        "internal: true",
        "---",
        "",
        f"# Already assigned to {s['name']}",
        "",
        "Read from LSAT U (`lsatu items`). Internal only. The recap check reads this before",
        "proposing homework, so a topic here is not assigned again.",
        "Open the student's work at https://lsatprep.study (Teacher view, student's assigned work).",
        "",
        "| Kind | Title | Status | Due | Added | Item ID |",
        "|---|---|---|---|---|---|",
    ]
    for item_id, kind, parts, added in rows:
        title = parts[0] if parts else ""
        rest = parts[1:]
        due = next((p[4:] for p in rest if p.startswith("due ")), "")
        status = next((p for p in rest if p in ("assigned", "in_progress", "completed", "submitted")), "")
        extra = [p for p in rest if p != status and not p.startswith(("due ", "unlocks "))]
        if extra:
            title = f"{title} · {' · '.join(extra)}"
        lines.append(f"| {kind} | {title} | {status} | {due} | {added} | `{item_id}` |")
    (out / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return len(rows)


def main():
    only = set(sys.argv[1:])
    for s in current():
        if only and s["slug"] not in only:
            continue
        if not s["email"]:
            print(f"{s['slug']}: no email, skipped")
            continue
        try:
            print(f"{s['slug']}: {write(s, items(s['email']))} items")
        except Exception as e:
            print(f"{s['slug']}: FAILED {e}")


main()
