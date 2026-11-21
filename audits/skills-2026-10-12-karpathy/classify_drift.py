"""Classify every home skill copy that differs from its runtime catalog copy.

  catalog-superset : nothing in the loaded copy is missing from the catalog (sync is lossless)
  stale-only       : the loaded copy's unique lines are all known-stale (dead paths, provider swaps,
                     old execution-contract preambles)
  loaded-newer     : vendor metadata shows the loaded copy is the newer upstream version
  review           : the loaded copy has unique content that needs a decision
Writes drift-classes.json.
"""
import json
import re
from pathlib import Path

HOME = Path.home()
V = Path(__file__).resolve().parents[2]
ROOTS = [("home-claude", HOME / ".claude/skills", "claude"), ("home-agents", HOME / ".agents/skills", "codex"),
         ("home-codex", HOME / ".codex/skills", "codex")]
DISPATCH = re.compile(r"compatibility dispatcher|This is a pointer")
CONTRACT = re.compile(r"^## (Local|Current AI OS) execution contract")
STALE = re.compile(r"~/ai-os\b|~/\.Codex|/Users/joshuaf|Codex-in-chrome|projects/lsatu/|archive/wiki-pre-rebuild|"
                   r"Ctrl\+Space|Vault root: `~/ai-os/`|\bCodex\.ai\b|academy\.codex\.com")
VERSION = re.compile(r"^\s*version:\s*([\d.]+)", re.M)


def norm_lines(text):
    out, skip = [], False
    for ln in text.replace("\r\n", "\n").split("\n"):
        if CONTRACT.match(ln):
            skip = True
            continue
        if skip and ln.startswith(("## ", "# ")):
            skip = False
        s = re.sub(r"\s+", " ", ln.strip())
        if skip or not s or s == "## Workflow":
            continue
        out.append(s)
    return out


def ver(text):
    m = VERSION.search(text)
    return tuple(int(x) for x in m.group(1).split(".")) if m else None


result = {}
for label, root, rt in ROOTS:
    for skf in sorted(root.glob("*/SKILL.md")):
        cat = V / "skills" / rt / skf.parent.name / "SKILL.md"
        if not cat.is_file():
            continue
        a = skf.read_text(encoding="utf-8", errors="replace")
        b = cat.read_text(encoding="utf-8", errors="replace")
        if a.replace("\r\n", "\n") == b.replace("\r\n", "\n") or DISPATCH.search(a + b):
            continue
        cat_set = set(norm_lines(b))
        only = [ln for ln in norm_lines(a) if ln not in cat_set]
        if not only:
            cls = "catalog-superset"
        elif ver(a) and ver(b) and ver(a) > ver(b):
            cls = "loaded-newer"
        elif all(STALE.search(ln) or ln.startswith("description:") for ln in only):
            cls = "stale-only"
        else:
            cls = "review"
        result.setdefault(cls, []).append({"install": label, "skill": skf.parent.name, "unique_lines": len(only),
                                           "sample": only[:4]})
json.dump(result, open(Path(__file__).parent / "drift-classes.json", "w", encoding="utf-8"), indent=1)
for cls, rows in result.items():
    print(f"{cls:<17} {len(rows)}")
