import os, re

ls_path = r"C:\Users\Joshu\AppData\Local\Programs\antigravity\resources\bin\language_server.exe"

with open(ls_path, "rb") as f:
    data = f.read()

target = b"MODEL_PLACEHOLDER_M318"
pos = 0
found = []
while True:
    pos = data.find(target, pos)
    if pos == -1:
        break
    found.append(pos)
    pos += len(target)

print(f"Found {len(found)} occurrences of {target.decode('utf-8')}")
for p in found:
    chunk = data[max(0, p-150):min(len(data), p+250)]
    printable = "".join(chr(b) if 32 <= b <= 126 else " " for b in chunk)
    print(f"\nOffset {p}:\n{printable}")

