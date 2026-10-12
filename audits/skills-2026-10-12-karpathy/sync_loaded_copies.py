"""Make loaded skill copies match their runtime catalog copy, with backups and hash receipts.

Claude Code loads ~/.claude/skills before the vault's .claude/skills (verified 2026-10-12: the session
listing showed the home copy's bootcamp-builder description). Codex loads ~/.agents/skills,
~/.codex/skills and the vault's .agents/skills. A skill whose copies all equal the catalog behaves the
same whichever copy a runtime picks.

Only skills named on the command line are touched. Only existing installs are updated (no new
activations). Files present in the catalog are copied over; extra files in an install are left alone.
Every overwritten file is backed up first. Re-running with identical inputs changes nothing.

usage: python sync_loaded_copies.py [--dry-run] skill [skill ...]
"""
import hashlib
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

HOME = Path.home()
VAULT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
BACKUP = HERE / "backups"
TARGETS = {
    "claude": [("home-claude", HOME / ".claude/skills"), ("vault-claude", VAULT / ".claude/skills")],
    "codex": [("home-agents", HOME / ".agents/skills"), ("home-codex", HOME / ".codex/skills"),
              ("vault-agents", VAULT / ".agents/skills")],
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main(argv):
    dry = "--dry-run" in argv
    skills = [a for a in argv if not a.startswith("--")]
    receipts = []
    for skill in skills:
        for runtime, roots in TARGETS.items():
            src = VAULT / "skills" / runtime / skill
            if not (src / "SKILL.md").is_file():
                continue
            for label, root in roots:
                dest = root / skill
                if not (dest / "SKILL.md").is_file():
                    continue
                for f in sorted(p for p in src.rglob("*") if p.is_file()):
                    rel = f.relative_to(src)
                    target = dest / rel
                    before = sha(target) if target.is_file() else None
                    after = sha(f)
                    if before == after:
                        continue
                    receipts.append({"skill": skill, "install": label, "file": str(rel).replace("\\", "/"),
                                     "before": before, "after": after})
                    if dry:
                        continue
                    if before is not None:
                        backup = BACKUP / label / skill / rel
                        if not backup.exists():  # keep the first original if re-run
                            backup.parent.mkdir(parents=True, exist_ok=True)
                            shutil.copy2(target, backup)
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(f, target)
                    assert sha(target) == after, target
    mode = "dry-run" if dry else "applied"
    print(f"{mode}: {len(receipts)} file writes across {len({(r['skill'], r['install']) for r in receipts})} installs")
    for r in receipts:
        print(f"  {r['install']:<13} {r['skill']:<26} {r['file']:<40} {'new' if r['before'] is None else 'overwrite'}")
    if not dry and receipts:
        log = HERE / "sync-receipts.json"
        prior = json.loads(log.read_text(encoding="utf-8")) if log.exists() else []
        prior.append({"at": datetime.now().isoformat(timespec="seconds"), "writes": receipts})
        log.write_text(json.dumps(prior, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1:])
