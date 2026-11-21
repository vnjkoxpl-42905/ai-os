#!/usr/bin/env python3
"""Antigravity PreToolUse hook: archived evidence under raw/sources/ is never edited.

Blocks write_to_file and replace_file_content on a file that already exists under raw/sources/.
New files (archiving a new source) and PROVENANCE.md notes are allowed.
"""
import json
import os
import sys
from pathlib import Path

ARCHIVE = Path(__file__).resolve().parents[2] / "raw" / "sources"


def is_blocked(file_path, cwd=""):
    if not file_path:
        return False
    p = str(file_path).strip().strip('\'"')
    if p.startswith("\\\\?\\"):
        p = p[4:]
    path = Path(os.path.expandvars(os.path.expanduser(p)))
    if not path.is_absolute():
        path = Path(cwd or os.getcwd()) / path
    path = Path(os.path.normcase(os.path.abspath(path)))
    archive = Path(os.path.normcase(os.path.abspath(ARCHIVE)))
    if archive not in path.parents:
        return False
    if path.name.lower() == "provenance.md":
        return False
    return path.exists()


def main():
    try:
        raw = sys.stdin.read()
        if not raw.strip():
            print(json.dumps({"decision": "allow"}))
            return
        payload = json.loads(raw)
    except Exception:
        print(json.dumps({"decision": "allow"}))
        return

    tool_call = payload.get("toolCall") or {}
    args = tool_call.get("args") or {}
    tool_input = payload.get("tool_input") or {}

    target = (
        args.get("TargetFile")
        or args.get("path")
        or tool_input.get("file_path")
        or tool_input.get("notebook_path")
        or ""
    )
    cwd = args.get("Cwd") or payload.get("cwd") or ""

    if is_blocked(target, cwd):
        reason = (
            f"Blocked: {target} is archived evidence under raw/sources/ and is never edited. "
            "Archive a changed version as a new file or folder, or add a note to PROVENANCE.md."
        )
        print(json.dumps({"decision": "deny", "reason": reason}))
        return

    print(json.dumps({"decision": "allow"}))


if __name__ == "__main__":
    main()
