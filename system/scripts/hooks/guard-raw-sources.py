"""Claude Code PreToolUse hook: archived evidence under raw/sources/ is never edited.

Blocks Write, Edit and MultiEdit on a file that already exists under raw/sources/.
New files (archiving a new source) and PROVENANCE.md notes are allowed. Exit code 2
blocks the tool call and shows the reason to Claude. Shell commands are not covered;
`py system/scripts/wiki-maintenance.py --evidence` catches those changes afterwards.
"""
import json
import os
import sys
from pathlib import Path

ARCHIVE = Path(__file__).resolve().parents[3] / "raw" / "sources"


def blocked(file_path, cwd):
    if not file_path:
        return False
    path = Path(file_path)
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
    payload = json.load(sys.stdin)
    tool_input = payload.get("tool_input") or {}
    target = tool_input.get("file_path") or tool_input.get("notebook_path")
    if blocked(target, payload.get("cwd")):
        print(f"Blocked: {target} is archived evidence under raw/sources/ and is never edited. "
              "Archive a changed version as a new file or folder, or add a note to PROVENANCE.md.",
              file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
