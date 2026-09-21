import os
import re

files_to_check = [
    r"C:\Users\Joshu\dev\ai-os\AGENTS.md",
    r"C:\Users\Joshu\dev\ai-os\GEMINI.md",
    r"C:\Users\Joshu\dev\ai-os\CLAUDE.md",
    r"C:\Users\Joshu\dev\ai-os\projects\lsatu\AGENTS.md",
    r"C:\Users\Joshu\dev\ai-os\projects\lsatu\GEMINI.md",
    r"C:\Users\Joshu\dev\ai-os\projects\lsatu\CLAUDE.md",
    r"C:\Users\Joshu\dev\ai-os\.gemini\README.md",
    r"C:\Users\Joshu\GEMINI.md"
]

print("=== Scanning for Stale Mac/Linux Paths ===")
mac_patterns = [r"/Users/joshuaf", r"/Users/Joshu", r"~/Documents", r"~/ai-os", r"~/\.claude"]

for f in files_to_check:
    if os.path.exists(f):
        with open(f, "r", encoding="utf-8", errors="ignore") as fh:
            lines = fh.readlines()
        for idx, line in enumerate(lines):
            for pat in mac_patterns:
                if re.search(pat, line, re.IGNORECASE):
                    print(f"{os.path.basename(f)}:L{idx+1} [Pattern: {pat}]: {line.strip()[:100]}")
