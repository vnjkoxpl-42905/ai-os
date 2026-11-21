#!/usr/bin/env python3
"""Which students have a post-session recap due, for the Recap band mod.

Read-only. Prints one JSON object:
{ok, error, days, students: [{slug, name, email, latest, due, recapped, assigned}]}

A student is current when a transcript is filed in students/<slug>/transcript-downloads/
within the last DAYS days (default 45). Only the most recent transcript counts.
A recap is due when that transcript's date is later than the newest recap on record.
A recap is on record when students/<slug>/recaps/ holds a file whose front matter
session_date (or filename date) is on or after the transcript date, or when
wiki/recap-ledger.md has a row naming the student and a date on or after it.
"""
import json
import os
import re
import subprocess
import sys
import time
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STUDENTS = ROOT / "students"
DAYS = int(sys.argv[1]) if len(sys.argv) > 1 else 45
DATE = re.compile(r"(\d{4}-\d{2}-\d{2})")


def roster():
    out = {}
    path = STUDENTS / "roster.generated.md"
    if not path.exists():
        return out
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\| \[\[([^/|\]]+)/[^|\]]*\\?\|([^\]]+)\]\] \| ([^|]*) \|", line)
        if m:
            out[m.group(1)] = (m.group(2).strip(), m.group(3).strip())
    return out


def ledger_dates(slug):
    path = ROOT / "wiki" / "recap-ledger.md"
    found = []
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.startswith("|") and slug in line.lower() and "recap made" in line.lower():
                found += DATE.findall(line)
    return found


def recap_dates(folder, slug):
    found = []
    rdir = folder / "recaps"
    if rdir.is_dir():
        for f in rdir.glob("*.md"):
            head = f.read_text(encoding="utf-8", errors="ignore")[:600]
            m = re.search(r"session_date:\s*(\d{4}-\d{2}-\d{2})", head) or DATE.search(f.name)
            if m:
                found.append(m.group(1))
    return found + ledger_dates(slug)


RECENT_DAYS = 7
STALE_SECONDS = 1800


def homework(folder, slug, refresh):
    """(items, latest_added) from the already-assigned index, refreshed from LSAT U when stale."""
    idx = folder / "homework" / "already-assigned" / "index.md"
    old = not idx.exists() or "latest_added:" not in idx.read_text(encoding="utf-8", errors="ignore")[:400]
    if refresh and not os.environ.get("RECAP_NO_REFRESH") and (old or time.time() - idx.stat().st_mtime > STALE_SECONDS):
        try:
            subprocess.run([sys.executable, "-I", str(ROOT / "system/scripts/build-homework-folders.py"), slug],
                           capture_output=True, timeout=60,
                           env={**os.environ, "RECAP_NO_REFRESH": "1"})
        except Exception:
            pass
    if not idx.exists():
        return None, ""
    head = idx.read_text(encoding="utf-8", errors="ignore")[:400]
    n = re.search(r"^items:\s*(\d+)", head, re.M)
    a = re.search(r"^latest_added:\s*(\d{4}-\d{2}-\d{2})", head, re.M)
    return (int(n.group(1)) if n else None), (a.group(1) if a else "")


def main():
    names = roster()
    cutoff = (date.today() - timedelta(days=DAYS)).isoformat()
    rows = []
    for folder in sorted(p for p in STUDENTS.iterdir() if p.is_dir()):
        slug = folder.name
        tdir = folder / "transcript-downloads"
        if slug.startswith(("_", ".")) or slug == "non-students" or not tdir.is_dir():
            continue
        dates = sorted(m.group(1) for f in tdir.glob("*.md") if (m := re.match(r"(\d{4}-\d{2}-\d{2})", f.name)))
        if not dates or dates[-1] < cutoff:
            continue
        latest = dates[-1]
        done = recap_dates(folder, slug)
        name, email = names.get(slug, (slug.replace("-", " ").title(), ""))
        page = folder / f"{slug}.md"
        if not email and page.exists():
            m = re.search(r"^email:\s*(\S+@\S+)", page.read_text(encoding="utf-8", errors="ignore")[:800], re.M)
            email = m.group(1) if m else ""
        recent = latest >= (date.today() - timedelta(days=RECENT_DAYS)).isoformat()
        count, last_added = homework(folder, slug, recent)
        rows.append({
            "slug": slug,
            "name": name,
            "email": email,
            "latest": latest,
            "due": not any(d >= latest for d in done),
            "recapped": max(done) if done else None,
            "assigned": count,
            "lastAssigned": last_added or None,
            "needsHomework": recent and last_added < latest,
        })
    rows.sort(key=lambda r: (not (r["due"] or r["needsHomework"]), not r["due"], r["name"].lower()))
    print(json.dumps({"ok": True, "days": DAYS, "students": rows}))


try:
    main()
except Exception as e:  # keep the band alive on any failure
    print(json.dumps({"ok": False, "error": str(e)[:200], "students": []}))
