import os
import json

p = r"C:\Users\Joshu\.gemini\antigravity\brain\3c03d32c-fd9f-45cb-82ce-11890d7fc349\.system_generated\logs\transcript.jsonl"
with open(p, "r", encoding="utf-8") as fh:
    for line in fh:
        d = json.loads(line)
        if "tool_calls" in d and d["tool_calls"]:
            print(json.dumps(d["tool_calls"][0], indent=2))
            break
