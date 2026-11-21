#!/usr/bin/env python3
"""PreToolUse guard for the recap-agent: refuse Bash commands that would post, assign, message or send.

The recap-agent prepares drafts only. Claude Code passes the pending tool call as JSON on stdin; exit
code 2 blocks it and the stderr text goes back to the agent. This guards direct Bash calls. It does not
stop an agent that writes its own script and runs it, which is why the agent also has no send tools and
every run is followed by a reviewer and by Joshua's approval.
"""
import json
import re
import sys

READ_ONLY_LSATU = {"items", "passes", "pass-detail", "signups", "notifications"}

BLOCKED = [
    (r"\bgws\s+(?!calendar\b)\S+", "gws is limited to calendar reads for the recap agent"),
    (r"lsatu-mcp-call|lsatu-assign-existing-cli|lsatu-work-plan|lsatu-lesson-mcp|lsatu-reading-center-notify",
     "posting and assigning tools are withheld from the recap agent"),
    (r"accommodations-email|send\.py", "sending email is withheld from the recap agent"),
    (r"\bgit\s+push\b", "pushing is withheld from the recap agent"),
]


def check(command: str) -> str | None:
    for pattern, reason in BLOCKED:
        if re.search(pattern, command, re.I):
            return reason
    for m in re.finditer(r"lsatu-admin\.mjs\s+([A-Za-z-]+)", command):
        if m.group(1).lower() not in READ_ONLY_LSATU:
            return f"lsatu-admin '{m.group(1)}' changes the platform; only read commands are allowed"
    return None


def main() -> int:
    try:
        event = json.load(sys.stdin)
    except Exception:
        return 0
    if event.get("tool_name") != "Bash":
        return 0
    command = (event.get("tool_input") or {}).get("command", "")
    reason = check(command)
    if reason:
        print(f"Blocked for the recap agent: {reason}. List this under 'For Joshua to approve' and stop.", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
