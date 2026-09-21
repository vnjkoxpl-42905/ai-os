import os, re

ls_path = r"C:\Users\Joshu\AppData\Local\Programs\antigravity\resources\bin\language_server.exe"

with open(ls_path, "rb") as f:
    data = f.read()

# Search for Go function names containing agent.md or AgentConfig or CustomAgent
matches = re.findall(rb"(?:[a-zA-Z0-9_\.\/]+\.(?:[A-Z][a-zA-Z0-9_]*agent[a-zA-Z0-9_]*|[a-z_]*agent\.md[a-zA-Z0-9_]*|WriteAgent|FormatAgent|LoadAgent|ParseAgent)[a-zA-Z0-9_]*)", data, re.IGNORECASE)

print(f"Found {len(matches)} matching Go symbols")
unique = sorted(list(set(m.decode('utf-8', errors='ignore') for m in matches)))
for u in unique[:40]:
    print(" ", u)

