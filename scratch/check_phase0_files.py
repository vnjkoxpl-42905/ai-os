import os

files = [
    r"C:\Users\Joshu\dev\ai-os\AGENTS.md",
    r"C:\Users\Joshu\dev\ai-os\GEMINI.md",
    r"C:\Users\Joshu\dev\ai-os\CLAUDE.md",
    r"C:\Users\Joshu\dev\ai-os\projects\lsatu\AGENTS.md",
    r"C:\Users\Joshu\dev\ai-os\projects\lsatu\GEMINI.md",
    r"C:\Users\Joshu\dev\ai-os\projects\lsatu\CLAUDE.md",
    r"C:\Users\Joshu\dev\ai-os\.gemini\README.md",
    r"C:\Users\Joshu\.gemini\config\skills.json",
    r"C:\Users\Joshu\.gemini\config\mcp_config.json",
    r"C:\Users\Joshu\.gemini\config\config.json"
]

print("=== File Existence & Size Check ===")
for f in files:
    if os.path.exists(f):
        print(f"EXISTS: {f} ({os.path.getsize(f)} bytes)")
    else:
        print(f"NOT PRESENT: {f}")
