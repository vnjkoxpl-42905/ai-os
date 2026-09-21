import os
import re

files = {
    "AGENTS.md": r"C:\Users\Joshu\dev\ai-os\AGENTS.md",
    "GEMINI.md": r"C:\Users\Joshu\dev\ai-os\GEMINI.md",
    "CLAUDE.md": r"C:\Users\Joshu\dev\ai-os\CLAUDE.md"
}

for name, path in files.items():
    print(f"\n==========================================")
    print(f"HEADINGS IN {name} ({os.path.getsize(path)} bytes)")
    print(f"==========================================")
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
    for i, l in enumerate(lines):
        if l.startswith("#"):
            print(f"L{i+1}: {l.strip()}")
