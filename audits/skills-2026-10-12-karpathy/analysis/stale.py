"""Count known-stale references in every installed and catalog SKILL.md.

Each pattern names a path or fact verified absent/wrong on this machine on 2026-10-12.
Output: stale.json {root: {skill: {pattern: count}}} plus a direction table for drifted pairs.
"""
import json
import re
from pathlib import Path

HOME = Path.home()
V = HOME / "dev" / "ai-os"
PATTERNS = {
    "~/ai-os root": re.compile(r"~/ai-os(?![-\w])"),
    "~/ai-os-projects": re.compile(r"~/ai-os-projects"),
    "mac /Users/joshuaf": re.compile(r"/Users/joshuaf"),
    "dead archive wiki-pre-rebuild": re.compile(r"archive/wiki-pre-rebuild-2026-07-16"),
    "corrupted .Codex dir": re.compile(r"~/\.Codex|\.Codex/"),
    "superwhisper Ctrl+Space": re.compile(r"Ctrl\+Space"),
    "auto push without asking": re.compile(r"commit and push without asking", re.I),
}
ROOTS = {
    "claude:global": HOME / ".claude/skills", "claude:project": V / ".claude/skills",
    "codex:agents": HOME / ".agents/skills", "codex:codex": HOME / ".codex/skills",
    "codex:project": V / ".agents/skills",
    "db:claude": V / "skills/claude", "db:codex": V / "skills/codex",
}
out = {}
for label, root in ROOTS.items():
    out[label] = {}
    for skf in sorted(root.glob("*/SKILL.md")):
        text = skf.read_text(encoding="utf-8", errors="replace")
        hits = {k: len(p.findall(text)) for k, p in PATTERNS.items() if p.search(text)}
        if hits:
            out[label][skf.parent.name] = hits
json.dump(out, open("stale.json", "w"), indent=1)
for label, skills in out.items():
    total = sum(sum(h.values()) for h in skills.values())
    print(f"{label:<15} skills with stale refs: {len(skills):>3}  total hits: {total}")
print()
for loaded, cat in (("claude:global", "db:claude"), ("codex:agents", "db:codex"), ("codex:codex", "db:codex")):
    worse_loaded = sorted(n for n, h in out[loaded].items() if sum(h.values()) > sum(out[cat].get(n, {}).values())
                          and (ROOTS[cat] / n / "SKILL.md").is_file())
    worse_cat = sorted(n for n, h in out[cat].items() if sum(h.values()) > sum(out[loaded].get(n, {}).values())
                       and (ROOTS[loaded] / n / "SKILL.md").is_file())
    print(f"{loaded} staler than {cat}: {' '.join(worse_loaded)}")
    print(f"{cat} staler than {loaded}: {' '.join(worse_cat)}\n")
