import os
import re

files = {
    "root_gemini": r"C:\Users\Joshu\dev\ai-os\GEMINI.md",
    "root_agents": r"C:\Users\Joshu\dev\ai-os\AGENTS.md",
    "lsatu_gemini": r"C:\Users\Joshu\dev\ai-os\projects\lsatu\GEMINI.md",
    "lsatu_agents": r"C:\Users\Joshu\dev\ai-os\projects\lsatu\AGENTS.md",
    "lsatu_claude": r"C:\Users\Joshu\dev\ai-os\projects\lsatu\CLAUDE.md",
}

topics = [
    "github", "lovable", "supabase", "backend", "obsidian", "wiki",
    "student", "browser", "push", "remote"
]

print("=== Source of Truth Quotes ===")
for fname, p in files.items():
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8", errors="ignore") as fh:
            text = fh.read()
        for t in topics:
            matches = [line.strip() for line in text.splitlines() if t in line.lower()]
            if matches:
                print(f"\n--- {fname} on '{t}' ({len(matches)} mentions) ---")
                for m in matches[:3]:
                    print(f"  * {m}")
