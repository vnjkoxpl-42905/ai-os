import os
import json
import hashlib

output_path = r"C:\Users\Joshu\dev\ai-os\AIOS_PHASE_0_CURRENT_STATE_PACK.md"

def read_file_verbatim(p):
    if not os.path.exists(p):
        return "NOT PRESENT\n"
    with open(p, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()

def get_hash(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

print("Gathering raw instruction files...")

# 1. Root instruction files
agents_root = read_file_verbatim(r"C:\Users\Joshu\dev\ai-os\AGENTS.md")
gemini_root = read_file_verbatim(r"C:\Users\Joshu\dev\ai-os\GEMINI.md")
claude_root = read_file_verbatim(r"C:\Users\Joshu\dev\ai-os\CLAUDE.md")

# 2. LSAT U instruction files
agents_lsatu = read_file_verbatim(r"C:\Users\Joshu\dev\ai-os\projects\lsatu\AGENTS.md")
gemini_lsatu = read_file_verbatim(r"C:\Users\Joshu\dev\ai-os\projects\lsatu\GEMINI.md")
claude_lsatu = read_file_verbatim(r"C:\Users\Joshu\dev\ai-os\projects\lsatu\CLAUDE.md")

# 3. Gemini workspace router
readme_gemini = read_file_verbatim(r"C:\Users\Joshu\dev\ai-os\.gemini\README.md")

# 4. Config files
skills_json = read_file_verbatim(r"C:\Users\Joshu\.gemini\config\skills.json")
mcp_config_json = read_file_verbatim(r"C:\Users\Joshu\.gemini\config\mcp_config.json")
config_json = read_file_verbatim(r"C:\Users\Joshu\.gemini\config\config.json")

print("Files read successfully.")
