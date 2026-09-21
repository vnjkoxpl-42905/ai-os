import os, re

ls_path = r"C:\Users\Joshu\AppData\Local\Programs\antigravity\resources\bin\language_server.exe"

with open(ls_path, "rb") as f:
    data = f.read()

target = b"workspace_uris"
pos = 0
found = []
while True:
    pos = data.find(target, pos)
    if pos == -1:
        break
    found.append(pos)
    pos += len(target)

print(f"Found {len(found)} occurrences of workspace_uris")
for p in found:
    chunk = data[max(0, p-100):min(len(data), p+200)]
    printable = "".join(chr(b) if 32 <= b <= 126 else " " for b in chunk)
    print(f"Offset {p}:\n  {printable.strip()}")

