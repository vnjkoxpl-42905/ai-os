#!/usr/bin/env python3
"""Send Joshua's accommodations email with the LSAC Qualified Professional Form attached.

Usage:
  python send.py --to EMAIL --first NAME [--slug SLUG] [--item TEXT ...] [--dry-run | --draft]

With no --item, the standard four accommodations are used. Any item that
mentions the experimental section gets the "Other" note appended.
A real send (or draft) is logged to wiki/send-ledger.md in the ai-os vault,
and to students/<slug>/open-loops.md when that folder exists.
Works from any folder: paths resolve from this file and the vault is found
at ~/dev/ai-os (Windows) or ~/ai-os (Mac), or $AI_OS_ROOT.
"""
import argparse
import html
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
BODY = HERE / "assets" / "body.html"
PDF = HERE / "assets" / "2026-2027-qualified-professional-form_final_accessible.pdf"
SUBJECT = "Request for Accommodations"
DEFAULT_ITEMS = [
    "100% extra time (double time)",
    "Stop/start breaks",
    "Permission to read aloud",
    "Removal of Experimental Section",
]
OTHER_NOTE = ' (Has to be written under "Other")'


def vault():
    for c in (os.environ.get("AI_OS_ROOT"), "~/dev/ai-os", "~/ai-os"):
        if c and (Path(c).expanduser() / "wiki" / "send-ledger.md").exists():
            return Path(c).expanduser()
    return None


def render(first, items):
    lis = []
    for item in items:
        if "experimental" in item.lower() and "other" not in item.lower():
            item += OTHER_NOTE
        lis.append(f'<li style="margin-left:15px">{html.escape(item)}</li>')
    body = BODY.read_text(encoding="utf-8")
    return body.replace("{FIRST}", html.escape(first)).replace("{ITEMS}", "".join(lis)).strip()


def log(root, slug, to, items, msg_id, status):
    now = datetime.now()
    custom = "default 4 items" if items == DEFAULT_ITEMS else "items: " + "; ".join(items)
    row = (f"| {now:%Y-%m-%d %H:%M} | {slug} | {SUBJECT} (QP form attached) | {status} {now:%Y-%m-%d} "
           f"| to {to}; skill accommodations-email; {custom}; Msg {msg_id} |\n")
    with open(root / "wiki" / "send-ledger.md", "a", encoding="utf-8") as f:
        f.write(row)
    folder = root / "students" / slug
    if folder.is_dir():
        verb = "Sent" if status == "sent" else "Drafted"
        with open(folder / "open-loops.md", "a", encoding="utf-8") as f:
            f.write(f"- [{now:%Y-%m-%d}] {verb} accommodations email + QP form. Loop: confirm they "
                    "registered for a test date and submitted before the accommodation deadline.\n")
        return f"logged to send-ledger and students/{slug}/open-loops.md"
    return "logged to send-ledger (no student folder)"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--to", required=True)
    ap.add_argument("--first", required=True)
    ap.add_argument("--slug", help="student folder name; defaults to the first name, lowercased")
    ap.add_argument("--item", action="append", help="accommodation line; repeat for each")
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true")
    mode.add_argument("--draft", action="store_true")
    a = ap.parse_args()

    if not re.fullmatch(r"[^@\s,]+@[^@\s,]+\.[^@\s,]+", a.to):
        sys.exit(f"Not a single email address: {a.to}")
    if not PDF.exists():
        sys.exit(f"Attachment missing: {PDF}")
    items = a.item or DEFAULT_ITEMS
    body = render(a.first.strip(), items)
    gws = shutil.which("gws") or sys.exit("gws CLI not found on PATH")
    cmd = [gws, "gmail", "+send", "--to", a.to, "--subject", SUBJECT,
           "--body", body, "--html", "-a", PDF.name]  # gws only attaches files under its cwd
    if a.dry_run:
        cmd.append("--dry-run")
    if a.draft:
        cmd.append("--draft")
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", cwd=PDF.parent)
    if r.returncode:
        print(r.stdout)
        print(r.stderr, file=sys.stderr)
        sys.exit(r.returncode)
    if a.dry_run:
        print(f"DRY RUN OK: would send to {a.to} as '{a.first}', {len(items)} items, PDF attached.")
        return
    out = json.loads(r.stdout[r.stdout.index("{"):])
    msg_id = out.get("message", out).get("id", "?")
    status = "drafted" if a.draft else "sent"
    root = vault()
    slug = a.slug or a.first.strip().lower().replace(" ", "-")
    note = log(root, slug, a.to, items, msg_id, status) if root else "NOT LOGGED: vault not found"
    print(f"{status.upper()}: {a.to} ({a.first}), Msg {msg_id}; {note}")


if __name__ == "__main__":
    main()
