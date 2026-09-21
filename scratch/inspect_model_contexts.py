import os, re

ls_path = r"C:\Users\Joshu\AppData\Local\Programs\antigravity\resources\bin\language_server.exe"

with open(ls_path, "rb") as f:
    data = f.read()

keywords = [
    b"Gemini 3.8 Flash",
    b"Gemini 3.7 Flash",
    b"Gemini 3.6 Flash",
    b"Gemini 3.1 Pro",
    b"Gemini 3.1 Flash",
    b"claude-sonnet",
    b"claude-opus",
    b"gpt-oss-120b",
    b"gpt-oss-20b",
    b"Claude 4",
    b"Sonnet 4",
    b"Opus 4"
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
    print(f"\n=== Keyword: {kw.decode('utf-8')} ({len(found)} occurrences) ===")
    for p in found[:3]:
        start = max(0, p - 100)
        end = min(len(data), p + 200)
        chunk = data[start:end]
        printable = "".join(chr(b) if 32 <= b <= 126 else " " for b in chunk)
        print(f"Offset {p}:\n  {printable.strip()}")

