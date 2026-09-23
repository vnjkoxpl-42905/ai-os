#!/usr/bin/env python3
"""Send Joshua's accommodations email with the LSAC Qualified Professional Form attached.

Usage:
  python send.py --to EMAIL --first NAME [--item TEXT ...] [--dry-run | --draft]

With no --item, the standard four accommodations are used. Any item that
mentions the experimental section gets the "Other" note appended.
"""
import argparse
import html
import shutil
import subprocess
import sys
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


def render(first, items):
    lis = []
    for item in items:
        if "experimental" in item.lower() and "other" not in item.lower():
            item += OTHER_NOTE
        lis.append(f'<li style="margin-left:15px">{html.escape(item)}</li>')
    body = BODY.read_text(encoding="utf-8")
    return body.replace("{FIRST}", html.escape(first)).replace("{ITEMS}", "".join(lis)).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--to", required=True)
    ap.add_argument("--first", required=True)
    ap.add_argument("--item", action="append", help="accommodation line; repeat for each")
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true")
    mode.add_argument("--draft", action="store_true")
    a = ap.parse_args()

    if not PDF.exists():
        sys.exit(f"Attachment missing: {PDF}")
    body = render(a.first.strip(), a.item or DEFAULT_ITEMS)
    gws = shutil.which("gws") or sys.exit("gws CLI not found on PATH")
    cmd = [gws, "gmail", "+send", "--to", a.to, "--subject", SUBJECT,
           "--body", body, "--html", "-a", str(PDF)]
    if a.dry_run:
        cmd.append("--dry-run")
    if a.draft:
        cmd.append("--draft")
    print(body)
    print("---")
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    print(r.stdout)
    if r.returncode:
        print(r.stderr, file=sys.stderr)
    sys.exit(r.returncode)


if __name__ == "__main__":
    main()
