import os, re

ls_path = r"C:\Users\Joshu\AppData\Local\Programs\antigravity\resources\bin\language_server.exe"

with open(ls_path, "rb") as f:
    data = f.read()

print(f"Loaded {len(data)} bytes")

# Extract all strings matching model names and enums
model_strings = set()
# Look for strings containing Flash, Pro, Sonnet, Opus, GPT, Claude, Gemini
pats = [
    rb"[A-Za-z0-9\.\-_ ]{3,40}(?:Flash|Pro|Sonnet|Opus|GPT|Claude|Gemini)[A-Za-z0-9\.\-_ \(\)]{0,30}",
    rb"MODEL_[A-Za-z0-9_]+",
    rb"gemini-[0-9\.\-a-z_]+",
    rb"claude-[0-9\.\-a-z_]+",
    rb"gpt-[0-9\.\-a-z_]+"
]

for p in pats:
    for m in re.finditer(p, data):
        s = m.group(0).decode('utf-8', errors='ignore').strip()
        if len(s) >= 4 and any(k in s.lower() for k in ["gemini", "claude", "sonnet", "opus", "gpt", "flash", "pro", "placeholder"]):
            model_strings.add(s)

print(f"Found {len(model_strings)} raw model-related strings")

# Filter and organize
models_sorted = sorted(list(model_strings))
print("\n=== MODEL ENUMS & PLACEHOLDERS ===")
for s in models_sorted:
    if s.startswith("MODEL_"):
        print(s)

print("\n=== DISPLAY NAMES & MODEL IDENTIFIERS ===")
for s in models_sorted:
    if any(s.startswith(p) for p in ["Gemini", "Claude", "GPT", "gemini-", "claude-", "gpt-"]):
        print(s)

