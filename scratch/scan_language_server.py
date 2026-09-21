import os, re

ls_path = r"C:\Users\Joshu\AppData\Local\Programs\antigravity\resources\bin\language_server.exe"
print(f"Inspecting {ls_path} ({os.path.getsize(ls_path)} bytes)...")

with open(ls_path, "rb") as f:
    data = f.read()

print("File loaded. Searching for model strings...")

keywords = [
    b"MODEL_PLACEHOLDER",
    b"Gemini 3.",
    b"Gemini 2.",
    b"Claude Sonnet",
    b"Claude Opus",
    b"GPT-OSS",
    b"gemini-3.",
    b"gemini-2.",
    b"claude-",
    b"thinking_level",
    b"thinkingLevel",
    b"reasoning_level",
    b"reasoningLevel",
    b"HIGH",
    b"MEDIUM",
    b"LOW"
]

for kw in keywords[:7]:
    pos = 0
    matches = set()
    while True:
        pos = data.find(kw, pos)
        if pos == -1:
            break
        # extract string around pos
        start = max(0, pos - 40)
        end = min(len(data), pos + 100)
        chunk = data[start:end]
        # find printable ASCII/UTF-8
        printable = "".join(chr(b) if 32 <= b <= 126 else " " for b in chunk)
        matches.add(printable.strip())
        pos += len(kw)
        if len(matches) > 15:
            break
    print(f"\nKeyword {kw.decode('utf-8')}: found {len(matches)} matches")
    for m in list(matches)[:8]:
        print("  ", m)

