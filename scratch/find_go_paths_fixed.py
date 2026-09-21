import os, re

ls_path = r"C:\Users\Joshu\AppData\Local\Programs\antigravity\resources\bin\language_server.exe"

with open(ls_path, "rb") as f:
    data = f.read()

matches = re.findall(rb"[a-zA-Z0-9_\.\-\/]+\/[a-zA-Z0-9_\-]+\.go", data)
print(f"Found {len(matches)} .go file paths")
agent_go = [m.decode('utf-8', errors='ignore') for m in matches if any(k in m.lower() for k in [b"agent", b"custom", b"skill", b"mcp", b"cortex"])]
print(f"Agent/Skill/MCP/Cortex .go paths: {len(agent_go)}")
for p in sorted(list(set(agent_go)))[:50]:
    print(" ", p)

