import os
import json
import glob
from collections import Counter

brain_dir = r"C:\Users\Joshu\.gemini\antigravity\brain"
conv_folders = [f for f in glob.glob(os.path.join(brain_dir, "*")) if os.path.isdir(f) and not os.path.basename(f).startswith(".")]

tool_usage = Counter()
mcp_tool_usage = Counter()

recent_convs = sorted(conv_folders, key=lambda x: os.path.getmtime(x), reverse=True)[:30]

for c in recent_convs:
    transcript_path = os.path.join(c, ".system_generated", "logs", "transcript.jsonl")
    if os.path.exists(transcript_path):
        try:
            with open(transcript_path, "r", encoding="utf-8", errors="ignore") as fh:
                for line in fh:
                    if not line.strip():
                        continue
                    try:
                        entry = json.loads(line)
                        t_calls = entry.get("tool_calls", [])
                        if t_calls:
                            for tc in t_calls:
                                name = tc.get("name", "unknown")
                                tool_usage[name] += 1
                                if "mcp" in name.lower():
                                    mcp_tool_usage[name] += 1
                    except json.JSONDecodeError:
                        pass
        except Exception:
            pass

print("Top Tools used across last 30 conversations:")
for name, cnt in tool_usage.most_common(20):
    print(f"  - {name}: {cnt}")

print("\nMCP Tools specifically used:")
for name, cnt in mcp_tool_usage.most_common(10):
    print(f"  - {name}: {cnt}")
