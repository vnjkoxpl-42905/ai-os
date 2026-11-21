"""Skill usage across every local Claude and Codex session log.

Only deliberate actions count:
  claude_skill  - Claude Skill tool invocations
  claude_open   - Claude tool_use lines (Read/Bash/etc.) whose input opens skills/<x>/SKILL.md
  codex_open    - Codex function_call/custom_tool_call lines whose arguments open skills/<x>/SKILL.md
  claude_meter  - ~/.claude.json skillUsage lifetime counter (includes /slash invocations)
Each open counts once per session. Sessions opening more than BULK distinct skills are audits.
Mentions in injected context (skill listings, hook output, instructions) are ignored because
only tool-call lines are inspected.
"""
import collections
import json
import re
from pathlib import Path

HOME = Path.home()
BULK = 10
SKILL_CALL = re.compile(r'"name":"Skill","input":\{"skill":"([^"]+)"')
SKILL_PATH = re.compile(r'skills(?:\\\\|\\|/)+([a-z0-9][a-z0-9-]*)(?:\\\\|\\|/)+SKILL\.md')


def scan(root, is_claude):
    calls, opens = collections.Counter(), collections.Counter()
    sessions = bulk = 0
    for f in root.rglob("*.jsonl"):
        sessions += 1
        seen = set()
        with open(f, encoding="utf-8", errors="replace") as handle:
            for line in handle:
                if is_claude:
                    if '"type":"tool_use"' not in line:
                        continue
                    for m in SKILL_CALL.finditer(line):
                        calls[m.group(1).split(":")[-1]] += 1
                    # only the tool_use input, not tool results or text
                    for chunk in re.findall(r'"type":"tool_use".*?"input":(\{.*?\})', line):
                        seen.update(m.group(1) for m in SKILL_PATH.finditer(chunk))
                else:
                    if '"function_call"' not in line and '"custom_tool_call"' not in line:
                        continue
                    if '"function_call_output"' in line or '"custom_tool_call_output"' in line:
                        continue
                    seen.update(m.group(1) for m in SKILL_PATH.finditer(line))
        if len(seen) > BULK:
            bulk += 1
            continue
        for name in seen:
            opens[name] += 1
    return sessions, bulk, calls, opens


c_sessions, c_bulk, c_calls, c_opens = scan(HOME / ".claude" / "projects", True)
x_sessions, x_bulk, _, x_opens = scan(HOME / ".codex" / "sessions", False)
meter = {k.split(":")[-1]: v["usageCount"]
         for k, v in json.load(open(HOME / ".claude.json", encoding="utf-8"))["skillUsage"].items()}

names = set(c_calls) | set(c_opens) | set(x_opens) | set(meter)
table = {n: {"claude_skill": c_calls.get(n, 0), "claude_open": c_opens.get(n, 0),
             "codex_open": x_opens.get(n, 0), "claude_meter": meter.get(n, 0)} for n in sorted(names)}
json.dump({"claude_sessions": c_sessions, "claude_bulk": c_bulk, "codex_sessions": x_sessions,
           "codex_bulk": x_bulk, "table": table}, open("usage_all.json", "w"), indent=1)
print(f"Claude sessions {c_sessions} (bulk excluded {c_bulk}); Codex sessions {x_sessions} (bulk excluded {x_bulk})")
print(f"distinct skills with any deliberate use: {len(names)}")


def score(v):
    return max(v["claude_skill"], v["claude_meter"]) + v["claude_open"] + v["codex_open"]


for n, v in sorted(table.items(), key=lambda kv: -score(kv[1])):
    print(f"{score(v):>4}  {n:<34} {v}")
