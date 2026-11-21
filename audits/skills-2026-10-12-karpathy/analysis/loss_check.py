"""For each pending overwrite, print lines that exist only in the loaded copy (would be lost)."""
import re
import sys
from pathlib import Path

HOME = Path.home()
V = HOME / "dev" / "ai-os"
ROOTS = {"home-claude": (HOME / ".claude/skills", "claude"), "home-agents": (HOME / ".agents/skills", "codex"),
         "home-codex": (HOME / ".codex/skills", "codex")}
CONTRACT_HDR = re.compile(r"^## (Local|Current AI OS) execution contract")


def lines(p):
    out, skip = [], False
    for ln in p.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n").split("\n"):
        if CONTRACT_HDR.match(ln):
            skip = True
            continue
        if skip and (ln.startswith("## ") or ln.startswith("# ")):
            skip = False
        if skip or not ln.strip() or ln.strip() == "## Workflow":
            continue
        out.append(re.sub(r"\s+", " ", ln.strip()))
    return out


for skill in sys.argv[1:]:
    for label, (root, rt) in ROOTS.items():
        loaded = root / skill / "SKILL.md"
        cat = V / "skills" / rt / skill / "SKILL.md"
        if not (loaded.is_file() and cat.is_file()):
            continue
        cat_set = set(lines(cat))
        only = [ln for ln in lines(loaded) if ln not in cat_set]
        if only:
            print(f"\n## {skill} [{label}] {len(only)} loaded-only lines")
            for ln in only[:14]:
                print("   - " + ln[:210])
