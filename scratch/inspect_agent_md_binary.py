import os, re

ls_path = r"C:\Users\Joshu\AppData\Local\Programs\antigravity\resources\bin\language_server.exe"

with open(ls_path, "rb") as f:
    data = f.read()

# Find offsets of "agent.md"
target = b"agent.md"
pos = 0
found = []
while True:
    pos = data.find(target, pos)
    if pos == -1:
        break
    found.append(pos)
    pos += len(target)

print(f"Found {len(found)} occurrences of agent.md")
for p in found:
    start = max(0, p - 300)
    end = min(len(data), p + 500)
    chunk = data[start:end]
    printable = "".join(chr(b) if 32 <= b <= 126 else " " for b in chunk)
    print(f"\n================ Offset {p} ================")
    # print non-empty lines
    lines = [l.strip() for l in printable.split("   ") if len(l.strip()) > 3]
    for l in lines[:15]:
        print(" ", l)

