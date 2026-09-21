import os

output_file = r"C:\Users\Joshu\dev\ai-os\AIOS_PHASE_0_CURRENT_STATE_PACK.md"

doc = []

# ==================================================
# 12. PHASE-0 SUMMARY
# ==================================================
doc.append("## 12. PHASE-0 SUMMARY")
doc.append("")

doc.append("### A. EXACT RAW FILES CAPTURED")
doc.append("The following raw control-plane files were captured in full verbatim text without truncation:")
doc.append("1. `C:\\Users\\Joshu\\dev\\ai-os\\AGENTS.md` (13,951 bytes)")
doc.append("2. `C:\\Users\\Joshu\\dev\\ai-os\\GEMINI.md` (11,764 bytes)")
doc.append("3. `C:\\Users\\Joshu\\dev\\ai-os\\CLAUDE.md` (13,946 bytes)")
doc.append("4. `C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\\AGENTS.md` (8,556 bytes)")
doc.append("5. `C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\\GEMINI.md` (1,368 bytes)")
doc.append("6. `C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu\\CLAUDE.md` (12,992 bytes)")
doc.append("7. `C:\\Users\\Joshu\\dev\\ai-os\\.gemini\\README.md` (1,333 bytes)")
doc.append("8. `C:\\Users\\Joshu\\.gemini\\config\\skills.json` (160 bytes)")
doc.append("9. `C:\\Users\\Joshu\\.gemini\\config\\mcp_config.json` (984 bytes)")
doc.append("10. `C:\\Users\\Joshu\\.gemini\\config\\config.json` (11,662 bytes)")
doc.append("")

doc.append("### B. CURRENT ACTIVE INSTRUCTION STACK")
doc.append("- **Root Session (`dev\\ai-os`):** Concurrently injects `C:\\Users\\Joshu\\GEMINI.md` (~450 tok), `dev\\ai-os\\AGENTS.md` (~3,400 tok), and `dev\\ai-os\\GEMINI.md` (~2,900 tok). Base rule text is ~85% identical across `AGENTS.md` and `GEMINI.md`.")
doc.append("- **Subtree Session (`dev\\ai-os\\projects\\lsatu`):** Injects root rules plus `projects\\lsatu\\GEMINI.md` (~350 tok) and `projects\\lsatu\\AGENTS.md` (~2,100 tok). Causes a direct operational contradiction: Root dictates the **95% Rule** (ask until confident), while subproject dictates the **Maximum Autonomy Rule** (never ask questions, implement directly).")
doc.append("")

doc.append("### C. CURRENT ACTIVE SKILL SOURCES")
doc.append("Antigravity actively aggregates skills across three configured source locations:")
doc.append("1. `C:\\Users\\Joshu\\.gemini\\config\\skills` (Global system skills)")
doc.append("2. `C:\\Users\\Joshu\\dev\\ai-os\\.gemini\\skills` (Workspace Gemini skills, including recursive indexing into `_snapshots` and `_inactive`)")
doc.append("3. `C:\\Users\\Joshu\\dev\\ai-os\\.agents\\skills` (Cross-runtime Codex skill directory, leaking 11 Codex skills into Gemini)")
doc.append("- **Runtime Exposure:** 85 skills exposed in prompt context; 98 skills suppressed due to context token budget limits.")
doc.append("")

doc.append("### D. CURRENT ANTIGRAVITY PROJECTS")
doc.append("1. `ai-os` (ID: `1e181e2e-860b-48c6-9209-540e3e7a1965`): ACTIVE, root path `file:///c%3A/Users/Joshu/dev/ai-os`, branch `main`, sandbox `false`, auto-execution eager.")
doc.append("2. `c:` (ID: `2a2e3dc0-5f6e-44f5-9cb4-5ad0c5a2a95b`): INACTIVE / ARCHIVED (`.bak`), root path `file:///c%3A/`.")
doc.append("")

doc.append("### E. DUPLICATED PHYSICAL FILES")
doc.append("1. **Browser Verification Suite:** 10 scripts in `C:\\Users\\Joshu\\Tools\\LSATU-Agent` have identical byte-for-byte SHA-256 duplicates in `C:\\Users\\Joshu\\dev\\ai-os\\.gemini\\skills\\lsat-u-browser-verification\\scripts\\`.")
doc.append("2. **Root Instructions:** `AGENTS.md` and `GEMINI.md` duplicate identical identity, routing tables, and guardrail text (~85% content match).")
doc.append("3. **Skill Snapshots:** 37 skills inside `_snapshots/` and 9 skills inside `_project-forks/` duplicate or fork skills residing directly in `.gemini/skills/`.")
doc.append("")

doc.append("### F. UNKNOWN / UNVERIFIED ITEMS")
doc.append("1. The exact mathematical or chronological algorithm Antigravity uses to select which 85 skills are displayed in `<skills>` and which 98 are suppressed.")
doc.append("2. Whether Antigravity supports a native directory exclusion pattern (such as `.skillignore`) to ignore underscore containers (`_snapshots`, `_inactive`).")
doc.append("3. Whether the 18 `.toml` files in `.gemini/agents/` are capable of being ingested natively by Antigravity or if they require manual session instantiation via `define_subagent`.")
doc.append("")

doc.append("### G. DIFFERENCES BETWEEN LIVE STATE AND ANTIGRAVITY_RUNTIME_AUDIT_INPUT.md")
doc.append("- **Status:** **Zero discrepancies.** The live state verified in this Phase 0 report perfectly aligns with `ANTIGRAVITY_RUNTIME_AUDIT_INPUT.md`. The verified process PIDs, directory footprints, 29 DevTools MCP tools, and cross-runtime leak through `skills.json` are fully confirmed.")
doc.append("")

doc.append("### H. DIFFERENCES BETWEEN LIVE STATE AND GEMINI_ANTIGRAVITY_COMPLETE_BREAKDOWN.md")
doc.append("1. **DevTools Tool Count:** `GEMINI_ANTIGRAVITY_COMPLETE_BREAKDOWN.md` listed 31 tools based on upstream documentation; the live machine state strictly contains **29 tool schema JSON files** in `C:\\Users\\Joshu\\.gemini\\antigravity\\mcp\\chrome-devtools`.")
doc.append("2. **Runtime Isolation:** The breakdown document described the Gemini workspace as strictly quarantined from Codex; live inspection revealed that `C:\\Users\\Joshu\\.gemini\\config\\skills.json` explicitly bridges `C:/Users/Joshu/dev/ai-os/.agents/skills` into Gemini context.")
doc.append("3. **Agent Subtree Ingestion:** The breakdown document described 18 subagents as active; live context proves only `self` and `research` are loaded in prompt context, with the 18 TOML files sitting unlinked in `.gemini/agents/`.")
doc.append("")

with open(output_file, "a", encoding="utf-8") as f:
    f.write("\n".join(doc) + "\n")
print("Section 12 appended successfully. Complete Phase 0 Pack is finished!")
