#!/usr/bin/env python3
"""Count native Notes by Gemini Docs in Drive that are not yet filed locally.

Read-only. Prints one JSON object for the Transcripts band mod:
{ok, error, days, total, filed, items: [{id, name, student, date}]}
A Doc counts as filed when a file named YYYY-MM-DD-<student>-... exists in any
students/*/transcript-downloads/ (including _other-sessions). Matching is by
session date plus the first name in the Doc title, because exports do not
record the Doc ID.
"""
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DAYS = int(sys.argv[1]) if len(sys.argv) > 1 else 30


def fail(msg):
    print(json.dumps({"ok": False, "error": msg, "items": []}))
    sys.exit(0)


shim = shutil.which("gws")
if not shim:
    fail("gws CLI not found on PATH")
# Run the CLI's node entry point directly: the .cmd shim goes through cmd.exe,
# which mangles the JSON --params (a ">" in the query becomes a redirect).
# The first gws on PATH can be a wrapper .cmd with no node_modules beside it
# (WindowsApps), so look in every PATH folder and the known npm prefixes.
import os

home = Path.home()
dirs = [Path(shim).parent, *(Path(d) for d in os.environ.get("PATH", "").split(os.pathsep) if d),
        home / "AppData" / "Roaming" / "npm", home / "tools" / "npm", home / "dev" / "tools" / "node"]
run_js = next((d / "node_modules" / "@googleworkspace" / "cli" / "run.js" for d in dirs
               if (d / "node_modules" / "@googleworkspace" / "cli" / "run.js").exists()), None)
node = shutil.which("node")
if not (node and run_js):
    fail("gws node entry point not found; the .cmd shim cannot carry this query")
gws_cmd = [node, str(run_js)]

since = (datetime.now(timezone.utc) - timedelta(days=DAYS)).strftime("%Y-%m-%dT%H:%M:%S")
params = {
    "q": "name contains 'Notes by Gemini' and mimeType='application/vnd.google-apps.document' "
         f"and createdTime > '{since}' and trashed=false",
    "pageSize": 100,
    "orderBy": "createdTime desc",
    "fields": "files(id,name,createdTime)",
}
try:
    r = subprocess.run([*gws_cmd, "drive", "files", "list", "--params", json.dumps(params)],
                       capture_output=True, text=True, timeout=60, encoding="utf-8")
except Exception as e:  # timeout or spawn failure
    fail(f"gws failed to run: {e}")
out = r.stdout
start = out.find("{")
if r.returncode != 0 or start < 0:
    fail((r.stderr or out).strip()[:300] or "gws returned no data")
try:
    files = json.loads(out[start:]).get("files", [])
except ValueError:
    fail("could not read gws output")

local = [p.name.lower() for p in ROOT.glob("students/*/transcript-downloads/*.md")]
# _other-sessions is flat: its exports sit directly in the folder, not in transcript-downloads/.
local += [p.name.lower() for p in ROOT.glob("students/_other-sessions/*.md")]


def slug_matches(filename, date, first):
    """True when the filename's slug (the part after the date) is the Doc's first name,
    by prefix either way: Yahunatan/Yahunathan, or a short slug like ore for Oreoluwa."""
    slug = re.split(r"-notes-|-recap|\.md", filename[len(date) + 1:], maxsplit=1)[0]
    slug = re.sub(r"[^a-z0-9]", "", slug.split("-")[0])
    if not slug or not first:
        return False
    return slug.startswith(first[:4]) or (len(slug) >= 3 and first.startswith(slug))

items, filed = [], 0
for f in files:
    name = f.get("name", "")
    m = re.search(r"(\d{4})/(\d{2})/(\d{2})", name)
    date = f"{m.group(1)}-{m.group(2)}-{m.group(3)}" if m else f.get("createdTime", "")[:10]
    first = re.split(r"\s+(?:session\b|-\s)|\s+-\s", name, maxsplit=1)[0].strip().split(" ")[0].lower()
    first = re.sub(r"[^a-z0-9]", "", first)
    if first in ("meeting", ""):
        student = ""
        hit = any(n.startswith(date + "-") for n in local)
    else:
        student = first
        hit = any(n.startswith(date + "-") and slug_matches(n, date, first) for n in local)
        if not hit:
            # Titles like "Booking (...) between Joshua and Sabrina" lead with a label, not a name:
            # try every word of the title against the filename slug.
            words = [re.sub(r"[^a-z0-9]", "", w) for w in name.lower().split()]
            hit = any(n.startswith(date + "-") and slug_matches(n, date, w)
                      for n in local
                      for w in words if len(w) >= 4 and w not in ("notes", "gemini", "session", "joshua"))
    if hit:
        filed += 1
    else:
        items.append({"id": f["id"], "name": name, "student": student, "date": date})

print(json.dumps({"ok": True, "days": DAYS, "total": len(files), "filed": filed, "items": items}))
