import os, re

asar_path = r"C:\Users\Joshu\AppData\Local\Programs\antigravity\resources\app.asar"
print(f"Checking {asar_path}...")

with open(asar_path, "rb") as f:
    data = f.read()

print(f"Read {len(data)} bytes.")

# Search for model strings or patterns
patterns = [
    rb"gemini-[0-9\.]+[a-zA-Z0-9\.\-_]*",
    rb"claude-[0-9\.]+[a-zA-Z0-9\.\-_]*",
    rb"gpt-[0-9\.]+[a-zA-Z0-9\.\-_]*",
    rb"Gemini 3\.[0-9]+[a-zA-Z0-9\.\-_ ]*",
    rb"Gemini 2\.[0-9]+[a-zA-Z0-9\.\-_ ]*",
    rb"Claude Sonnet [0-9\.]+[a-zA-Z0-9\.\-_ ]*",
    rb"Claude Opus [0-9\.]+[a-zA-Z0-9\.\-_ ]*",
    rb"GPT-OSS[a-zA-Z0-9\.\-_ ]*",
    rb"thinking[lL]evel",
    rb"reasoning[lL]evel"
]

for pat in patterns:
    matches = set(re.findall(pat, data, re.IGNORECASE))
    decoded = sorted([m.decode('utf-8', errors='ignore') for m in matches])[:30]
    print(f"\nPattern {pat}: found {len(matches)} matches")
    print(decoded[:20])

