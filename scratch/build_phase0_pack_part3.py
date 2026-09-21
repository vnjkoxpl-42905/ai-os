import os

output_file = r"C:\Users\Joshu\dev\ai-os\AIOS_PHASE_0_CURRENT_STATE_PACK.md"

doc = []

# ==================================================
# 6. SKILL SOURCE TREE
# ==================================================
doc.append("## 6. SKILL SOURCE TREE")
doc.append("")
doc.append("Directory trees for all registered skill root repositories. Marked by intent/status: `ACTIVE`, `ARCHIVAL`, `SNAPSHOT`, `EXAMPLE`, `FORK`, or `UNKNOWN`.")
doc.append("")

paths = {
    "C:\\Users\\Joshu\\dev\\ai-os\\.gemini\\skills": r"C:\Users\Joshu\dev\ai-os\.gemini\skills",
    "C:\\Users\\Joshu\\dev\\ai-os\\.agents\\skills": r"C:\Users\Joshu\dev\ai-os\.agents\skills",
    "C:\\Users\\Joshu\\.gemini\\config\\skills": r"C:\Users\Joshu\.gemini\config\skills"
}

for label, p in paths.items():
    doc.append(f"### Tree: `{label}`")
    doc.append("```text")
    if not os.path.exists(p):
        doc.append("NOT PRESENT")
    else:
        for item in sorted(os.listdir(p)):
            fp = os.path.join(p, item)
            if os.path.isdir(fp):
                if item == "_inactive":
                    doc.append(f"[CONTAINER] _inactive/ (ARCHIVAL)")
                    for sub in sorted(os.listdir(fp)):
                        doc.append(f"  └── {sub}/ [ARCHIVAL]")
                elif item == "_snapshots":
                    doc.append(f"[CONTAINER] _snapshots/ (SNAPSHOT)")
                    for sub in sorted(os.listdir(fp)):
                        doc.append(f"  └── {sub}/ [SNAPSHOT]")
                elif item == "_project-forks":
                    doc.append(f"[CONTAINER] _project-forks/ (FORK)")
                    for sub in sorted(os.listdir(fp)):
                        sub_p = os.path.join(fp, sub)
                        if os.path.isdir(sub_p):
                            doc.append(f"  └── {sub}/")
                            for fsub in sorted(os.listdir(sub_p)):
                                doc.append(f"      └── {fsub}/ [FORK]")
                elif "example" in item.lower():
                    doc.append(f"├── {item}/ [EXAMPLE]")
                elif os.path.exists(os.path.join(fp, "SKILL.md")):
                    doc.append(f"├── {item}/ [ACTIVE]")
                else:
                    doc.append(f"├── {item}/ [UNKNOWN]")
    doc.append("```")
    doc.append("")

doc.append("---")
doc.append("")

# ==================================================
# 7. .agents TOPOLOGY
# ==================================================
doc.append("## 7. .agents TOPOLOGY")
doc.append("")
doc.append("Complete directory tree for `C:\\Users\\Joshu\\dev\\ai-os\\.agents` (filenames only):")
doc.append("")
doc.append("```text")

agents_base = r"C:\Users\Joshu\dev\ai-os\.agents"
if os.path.exists(agents_base):
    for root, dirs, files in os.walk(agents_base):
        rel = os.path.relpath(root, agents_base)
        indent = "  " * (rel.count(os.sep) if rel != "." else 0)
        folder_name = os.path.basename(root) if rel != "." else ".agents"
        doc.append(f"{indent}[DIR] {folder_name}/")
        for f in sorted(files):
            doc.append(f"{indent}  └── {f}")
else:
    doc.append("NOT PRESENT")

doc.append("```")
doc.append("")
doc.append("### Subdirectory Consumer & Runtime Ownership Analysis")
doc.append("")
doc.append("| Subdirectory / Item | Classification | Primary Consumer | Shared / Antigravity Status |")
doc.append("|---|---|---|---|")
doc.append("| `.agents/skills/domain-modeling` | Skill | Codex | Shared: Inherited by Antigravity via `skills.json` |")
doc.append("| `.agents/skills/grill-with-docs` | Skill | Codex | Shared: Inherited by Antigravity via `skills.json` |")
doc.append("| `.agents/skills/grilling` | Skill | Codex | Shared: Inherited by Antigravity via `skills.json` |")
doc.append("| `.agents/skills/gws-gmail` | Skill | Codex | Shared: Inherited by Antigravity via `skills.json` |")
doc.append("| `.agents/skills/gws-gmail-read` | Skill | Codex | Shared: Inherited by Antigravity via `skills.json` |")
doc.append("| `.agents/skills/gws-gmail-triage` | Skill | Codex | Shared: Inherited by Antigravity via `skills.json` |")
doc.append("| `.agents/skills/gws-shared` | Skill | Codex | Shared: Inherited by Antigravity via `skills.json` |")
doc.append("| `.agents/skills/kling-cli` | Skill | Codex | Shared: Inherited by Antigravity via `skills.json` |")
doc.append("| `.agents/skills/pre-consultation-check-in` | Skill | Codex | Shared: Inherited by Antigravity via `skills.json` |")
doc.append("| `.agents/skills/session-recap` | Skill | Codex | Shared: Inherited by Antigravity via `skills.json` |")
doc.append("| `.agents/skills/superwhisper` | Skill | Codex | Shared: Inherited by Antigravity via `skills.json` |")
doc.append("| `.agents/agents` | Agents Directory | Not Present | UNKNOWN / Retired (Codex agents reside in `.codex/`) |")
doc.append("| `.agents/rules` | Rules Directory | Not Present | UNKNOWN / Handled by root `AGENTS.md` |")
doc.append("| `.agents/hooks` | Hooks Directory | Not Present | UNKNOWN / Handled by git hooks or runtime hooks |")
doc.append("")
doc.append("---")
doc.append("")

with open(output_file, "a", encoding="utf-8") as f:
    f.write("\n".join(doc) + "\n")
print("Sections 6 and 7 appended successfully.")
