import os

def clean_rebuild():
    output_file = r"C:\Users\Joshu\dev\ai-os\AIOS_PHASE_0_CURRENT_STATE_PACK.md"
    
    def read_file(p):
        if not os.path.exists(p):
            return "NOT PRESENT\n"
        with open(p, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()

    # Section 1 files
    agents_root = read_file(r"C:\Users\Joshu\dev\ai-os\AGENTS.md")
    gemini_root = read_file(r"C:\Users\Joshu\dev\ai-os\GEMINI.md")
    claude_root = read_file(r"C:\Users\Joshu\dev\ai-os\CLAUDE.md")

    # Section 2 files
    agents_lsatu = read_file(r"C:\Users\Joshu\dev\ai-os\projects\lsatu\AGENTS.md")
    gemini_lsatu = read_file(r"C:\Users\Joshu\dev\ai-os\projects\lsatu\GEMINI.md")
    claude_lsatu = read_file(r"C:\Users\Joshu\dev\ai-os\projects\lsatu\CLAUDE.md")

    # Section 3 file
    readme_gemini = read_file(r"C:\Users\Joshu\dev\ai-os\.gemini\README.md")

    # Section 4 files
    skills_json = read_file(r"C:\Users\Joshu\.gemini\config\skills.json")
    mcp_config_json = read_file(r"C:\Users\Joshu\.gemini\config\mcp_config.json")
    config_json = read_file(r"C:\Users\Joshu\.gemini\config\config.json")

    doc = []

    doc.append("# AIOS Phase 0: Current-State Freeze for External Architect")
    doc.append("")
    doc.append("**Document Role:** Raw Control-Plane Evidence Report  ")
    doc.append("**Timestamp:** 2026-09-20T02:00:00-04:00  ")
    doc.append("**Host Machine:** `J` (Windows 11 Home, Build 26100)  ")
    doc.append("**Workspace Root:** `C:\\Users\\Joshu\\dev\\ai-os`  ")
    doc.append("**Investigation Type:** READ-ONLY Forensic Freeze (No modifications made)  ")
    doc.append("")
    doc.append("---")
    doc.append("")

    # 1. RAW ROOT INSTRUCTIONS
    doc.append("## 1. RAW ROOT INSTRUCTIONS")
    doc.append("")
    doc.append("### 1.1 C:\\Users\\Joshu\\dev\\ai-os\\AGENTS.md")
    doc.append("`````markdown")
    doc.append(agents_root.rstrip())
    doc.append("`````")
    doc.append("")
    doc.append("### 1.2 C:\\Users\\Joshu\\dev\\ai-os\\GEMINI.md")
    doc.append("`````markdown")
    doc.append(gemini_root.rstrip())
    doc.append("`````")
    doc.append("")
    doc.append("### 1.3 C:\\Users\\Joshu\\dev\\ai-os\\CLAUDE.md")
    doc.append("`````markdown")
    doc.append(claude_root.rstrip())
    doc.append("`````")
    doc.append("")
    doc.append("---")
    doc.append("")

    # 2. LSAT U INSTRUCTIONS
    doc.append("## 2. LSAT U INSTRUCTIONS")
    doc.append("")
    doc.append("### 2.1 C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\\AGENTS.md")
    doc.append("`````markdown")
    doc.append(agents_lsatu.rstrip())
    doc.append("`````")
    doc.append("")
    doc.append("### 2.2 C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\\GEMINI.md")
    doc.append("`````markdown")
    doc.append(gemini_lsatu.rstrip())
    doc.append("`````")
    doc.append("")
    doc.append("### 2.3 C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\\CLAUDE.md")
    doc.append("`````markdown")
    doc.append(claude_lsatu.rstrip())
    doc.append("`````")
    doc.append("")
    doc.append("### 2.4 Nested Instruction Files Inside C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu")
    doc.append("")
    doc.append("| Nested File Path | Scope / Subtree Affected | Precedence Relative to Parent Instruction Files |")
    doc.append("|---|---|---|")
    doc.append("| `C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\\.agents\\skills\\notebooklm\\AGENTS.md` | NotebookLM skill execution context within Codex runtime | Subordinate to `projects\\lsatu\\AGENTS.md`; governs when NotebookLM skill is activated |")
    doc.append("| `C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\\.agents\\skills\\notebooklm\\CLAUDE.md` | NotebookLM skill execution context within Claude Code runtime | Subordinate to `projects\\lsatu\\CLAUDE.md`; governs NotebookLM CLI skill commands |")
    doc.append("| `C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\\.agents\\skills\\second-brain\\references\\agent-configs\\gemini.md` | Template / reference document for Second Brain vault configuration | Pure reference file; does not execute as an active runtime instruction file |")
    doc.append("| `C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\\.claude\\skills\\notebooklm\\AGENTS.md` | NotebookLM skill execution context within Claude Code runtime | Subordinate to `projects\\lsatu\\CLAUDE.md`; twin copy of skill documentation |")
    doc.append("| `C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\\.claude\\skills\\notebooklm\\CLAUDE.md` | NotebookLM skill execution context within Claude Code runtime | Subordinate to `projects\\lsatu\\CLAUDE.md`; twin copy of skill documentation |")
    doc.append("| `C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\\.claude\\skills\\second-brain\\references\\agent-configs\\gemini.md` | Template / reference document for Second Brain vault configuration | Pure reference file; does not execute as an active runtime instruction file |")
    doc.append("")
    doc.append("---")
    doc.append("")

    # 3. GEMINI WORKSPACE ROUTER
    doc.append("## 3. GEMINI WORKSPACE ROUTER")
    doc.append("")
    doc.append("### C:\\Users\\Joshu\\dev\\ai-os\\.gemini\\README.md")
    doc.append("`````markdown")
    doc.append(readme_gemini.rstrip())
    doc.append("`````")
    doc.append("")
    doc.append("---")
    doc.append("")

    # 4. GLOBAL ANTIGRAVITY CONFIG
    doc.append("## 4. GLOBAL ANTIGRAVITY CONFIG")
    doc.append("")
    doc.append("### 4.1 C:\\Users\\Joshu\\.gemini\\config\\skills.json")
    doc.append("`````json")
    doc.append(skills_json.rstrip())
    doc.append("`````")
    doc.append("")
    doc.append("### 4.2 C:\\Users\\Joshu\\.gemini\\config\\mcp_config.json")
    doc.append("`````json")
    doc.append(mcp_config_json.rstrip())
    doc.append("`````")
    doc.append("")
    doc.append("### 4.3 C:\\Users\\Joshu\\.gemini\\config\\config.json")
    doc.append("`````json")
    doc.append(config_json.rstrip())
    doc.append("`````")
    doc.append("")
    doc.append("---")
    doc.append("")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(doc) + "\n")
    print("Clean rebuild part 1 written.")

clean_rebuild()
