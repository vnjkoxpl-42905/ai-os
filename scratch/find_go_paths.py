import os, re

ls_path = r"C:\Users\Joshu\AppData\Local\Programs\antigravity\resources\bin\language_server.exe"

with open(ls_path, "rb") as f:
    data = f.read()

# Search for .go file paths
matches = re.findall(rb"[a-zA-Z0-9_\.\-\/]+\/[a-zA-Z0-9_\-]+\.go", data)
print(f"Found {len(matches)} .go file paths")
agent_go = [m.decode('utf-8', errors='ignore') for m in matches if any(k in m.lower() for k in ["agent", "custom", "skill", "mcp"])]
print(f"Agent/Skill/MCP .go paths: {len(agent_go)}")
for p in sorted(list(set(agent_go)))[:30]:
    print(" ", p)

