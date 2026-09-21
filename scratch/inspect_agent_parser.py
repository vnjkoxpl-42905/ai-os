import os, re

ls_path = r"C:\Users\Joshu\AppData\Local\Programs\antigravity\resources\bin\language_server.exe"

with open(ls_path, "rb") as f:
    data = f.read()

keywords = [
    b"agent.md",
    b".agents/agents",
    b"custom_agents",
    b"agent_behavior",
    b"sandbox_mode",
    b"enabled_tools",
    b"mcp_servers"
]

for kw in keywords:
    pos = 0
    found = []
    while True:
        pos = data.find(kw, pos)
        if pos == -1:
            break
        found.append(pos)
        pos += len(kw)
    print(f"\nKeyword: {kw.decode('utf-8')} ({len(found)} occurrences)")
    for p in found[:5]:
        start = max(0, p - 80)
        end = min(len(data), p + 160)
        chunk = data[start:end]
        printable = "".join(chr(b) if 32 <= b <= 126 else " " for b in chunk)
        print(f"Offset {p}:\n  {printable.strip()}")

