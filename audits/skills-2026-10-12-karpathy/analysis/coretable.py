"""For each core skill, compare every loaded copy with its runtime catalog copy."""
import re
import sys
from pathlib import Path

HOME = Path.home()
V = HOME / "dev" / "ai-os"
CORE = """pickup wrapup session-handoff audit level-up consultation-inquiry-drafts consultation-followup-drafts
inbound-tutoring-replies transcript-intake post-session-recap guided-drill-assignment lsat-u-platform-actions
tutorocean-profile-fill prompt-architect-refiner accommodations-email assign-lsatu-work booking-link
send-booking-link superwhisper bootcamp-builder bootcamp-parity-audit lsat-u-voice lsat-u-architecture
lsat-u-topic-builder lsatu-cc-handoff lovable-prompt lovable-migrate morning-brief pull-submissions
lsat-lab-mega-set lsat-lab-transcribe lsat-lab-sync lsat-lab-lecture-transcribe resume chat-export watch
youtube-full ingest second-brain second-brain-ingest second-brain-query second-brain-lint grill-me grilling
grill-with-docs chief-of-staff karpathy-teach impeccable herdr kling-cli""".split()
LOADED = {
    "claude": [("~claude", HOME / ".claude/skills"), ("proj", V / ".claude/skills")],
    "codex": [("~agents", HOME / ".agents/skills"), ("~codex", HOME / ".codex/skills"), ("proj", V / ".agents/skills")],
}
CONTRACT = re.compile(r"\n## (?:Local|Current AI OS) execution contract[^\n]*\n.*?(?=\n## |\n# |\Z)", re.S)


def text(p):
    return p.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n") if p.is_file() else None


def norm(t):
    t = CONTRACT.sub("\n", t)
    t = re.sub(r"\n## Workflow\n", "\n", t)
    return re.sub(r"\s+", " ", t).strip()


def state(loaded, cat):
    if loaded is None:
        return "."
    if cat is None:
        return "NOCAT"
    if loaded == cat:
        return "="
    if norm(loaded) == norm(cat):
        return "~c"
    if re.search(r"compatibility dispatcher|This is a pointer", loaded + "\n" + cat):
        return "disp"
    return "DIFF"


rows = []
for name in CORE:
    cells = []
    for rt, roots in LOADED.items():
        cat = text(V / "skills" / rt / name / "SKILL.md")
        for label, root in roots:
            cells.append(f"{rt[:2]}{label}:{state(text(root / name / 'SKILL.md'), cat)}")
    print(f"{name:<30} " + "  ".join(f"{c:<16}" for c in cells))
print("\nlegend: = identical | ~c only execution-contract preamble differs | DIFF substantive | disp dispatcher/pointer pair | NOCAT no catalog copy | . not installed")
