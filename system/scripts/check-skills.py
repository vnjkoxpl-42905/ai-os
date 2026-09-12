#!/usr/bin/env python3
"""Validate the skills DB model (replaces the old 'expect exactly 11' check).

Activation model (changed 2026-07-17, Joshua's call): a project activates a DB skill
by COPYING it into `.claude/skills/<name>/` (or `.agents/skills/`), not symlinking.
Copies are real files — portable, committable, no dead links on another machine.
The tradeoff: a copy does not auto-follow DB edits. This script's (e) check exists
because of that tradeoff — it flags copies that have drifted from their DB source.
Symlinks are still tolerated (not an error) for any that predate the change or for
the unrelated vendor-plugin mechanism in the DB itself (skills/claude/_snapshots
pattern), which this script does not touch.

Checks:
  (a) every activation in an active root resolves to real content (no broken symlink);
  (b) no skill lives in an active root un-mirrored (real dir with no DB counterpart);
  (c) INDEX.md covers every top-level DB skill;
  (d) no duplicate canonical name within a subtree;
  (e) a copied (non-symlink) activation's SKILL.md matches its DB source byte-for-byte
      — catches silent drift after the DB is edited but the activation isn't re-synced.
  (f) every multi-segment path cited in CLAUDE.md / AGENTS.md resolves on disk
      — routing maps that point at moved or deleted files send sessions hunting.
  (g) no UNDECLARED claude/codex asymmetry. The two subtrees are intentionally unequal,
      so the legitimate split is declared in skills/PARITY.md and only new drift fails.
Exit 0 = PASS, 1 = FAIL.
"""
import os, re, sys, filecmp

BRAIN = "/Users/joshuaf/ai-os"
DB = f"{BRAIN}/skills"
HOME = os.path.expanduser("~")
SPECIAL = {"_snapshots", "_project-forks", "_inactive", "README.md", "INDEX.md"}

# Active roots to audit (only those that exist are checked).
ACTIVE_ROOTS = [
    f"{HOME}/.claude/skills",
    f"{HOME}/.agents/skills",
    f"{BRAIN}/.claude/skills",
    f"{BRAIN}/.agents/skills",
    f"{BRAIN}/projects/email-hq/.claude/skills",
]

def db_names(sub):
    base = os.path.join(DB, sub)
    if not os.path.isdir(base):
        return set()
    return {n for n in os.listdir(base)
            if n not in SPECIAL and (os.path.isdir(os.path.join(base, n)) or os.path.islink(os.path.join(base, n)))}

def main():
    fails = []
    # DB structure
    for sub in ("claude", "codex"):
        if not os.path.isdir(os.path.join(DB, sub)):
            fails.append(f"DB subtree missing: skills/{sub}")
    claude_db = db_names("claude")
    codex_db = db_names("codex")

    # (d) duplicate canonical names within a subtree — filesystem guarantees uniqueness,
    # but validate SKILL.md name matches dir name where a SKILL.md exists.
    for sub, names in (("claude", claude_db), ("codex", codex_db)):
        for n in names:
            # Vendor entries are symlinks whose dir name may be disambiguated
            # (e.g. discord-access -> plugin skill named 'access'); skip name check.
            if os.path.islink(os.path.join(DB, sub, n)):
                continue
            real = os.path.realpath(os.path.join(DB, sub, n))
            skf = os.path.join(real, "SKILL.md")
            if os.path.isfile(skf):
                with open(skf, encoding="utf-8", errors="replace") as f:
                    head = f.read(1200)
                m = re.search(r"(?mi)^name:\s*(.+)$", head)
                if m and m.group(1).strip().strip('"').strip("'") != n:
                    fails.append(f"name mismatch: skills/{sub}/{n} declares '{m.group(1).strip()}'")

    # (a)+(b) active roots
    all_db = claude_db | codex_db
    for root in ACTIVE_ROOTS:
        if not os.path.isdir(root):
            continue
        for n in os.listdir(root):
            if n.startswith("."):
                continue
            p = os.path.join(root, n)
            if os.path.islink(p):
                if not os.path.exists(p):
                    fails.append(f"broken activation symlink: {root}/{n}")
                elif f"{BRAIN}/skills/" not in os.path.realpath(p):
                    fails.append(f"activation not into DB: {root}/{n} -> {os.path.realpath(p)}")
            elif os.path.isdir(p):
                # real dir in an active root: must be mirrored in DB by name
                if n not in all_db:
                    fails.append(f"un-mirrored skill in active root: {root}/{n} (not in DB)")
                    continue
                # (e) drift check: copied activation's SKILL.md vs its DB source
                sub = "codex" if "/.agents/" in root else "claude"
                db_dir = os.path.join(DB, sub, n)
                act_skf = os.path.join(p, "SKILL.md")
                db_skf = os.path.join(db_dir, "SKILL.md")
                if os.path.isfile(act_skf) and os.path.isfile(db_skf):
                    if not filecmp.cmp(act_skf, db_skf, shallow=False):
                        fails.append(f"stale activation copy: {root}/{n} differs from skills/{sub}/{n} — re-copy from DB")

    # (c) INDEX coverage
    idx = os.path.join(DB, "INDEX.md")
    if not os.path.isfile(idx):
        fails.append("INDEX.md missing")
    else:
        with open(idx, encoding="utf-8") as f:
            itext = f.read()
        indexed = set(re.findall(r"^- \*\*(?:[a-z0-9-]+: )?([^*]+)\*\*", itext, re.M))
        for sub, names in (("claude", claude_db), ("codex", codex_db)):
            for n in names:
                if n not in indexed:
                    fails.append(f"INDEX missing DB skill: {sub}/{n}")

    # (f) dead paths in the routing maps. Only multi-segment paths (a/b) are checked;
    # bare fragments like `codex/` are prose, not routing targets.
    for fname in ("CLAUDE.md", "AGENTS.md"):
        fpath = os.path.join(BRAIN, fname)
        if not os.path.isfile(fpath):
            fails.append(f"routing file missing: {fname}")
            continue
        with open(fpath, encoding="utf-8") as f:
            text = f.read()
        for cand in sorted(set(re.findall(r"`([^`\s]+/[^`\s]+)`", text))):
            if cand.startswith("http") or any(c in cand for c in "<>*{}|"):
                continue
            p = cand.rstrip("/")
            if p.startswith("~"):
                p = os.path.expanduser(p)
            ap = p if p.startswith("/") else os.path.join(BRAIN, p)
            if not os.path.exists(ap):
                fails.append(f"dead path in {fname}: `{cand}`")

    # (g) undeclared claude/codex asymmetry, measured against skills/PARITY.md.
    parity = os.path.join(DB, "PARITY.md")
    if not os.path.isfile(parity):
        fails.append("PARITY.md missing (skill asymmetry baseline)")
    else:
        with open(parity, encoding="utf-8") as f:
            ptext = f.read()
        # A bare "- name" list cannot carry the reason each split needs, and a
        # baseline without reasons is a snapshot rather than a decision (that is
        # exactly how the 2026-07-19 baseline went unaudited). So names are read
        # from `backticks` anywhere in the file, which lets each entry sit beside
        # its justification in prose. Only tokens that name a real skill count —
        # that ignores the incidental backticks (paths, flags, MCP servers)
        # without needing them escaped, and a typo'd name simply fails to
        # declare, surfacing as undeclared drift rather than passing silently.
        known = claude_db | codex_db
        declared = {t for t in re.findall(r"`([A-Za-z0-9][A-Za-z0-9._-]*)`", ptext)
                    if t in known}
        for n in sorted((claude_db - codex_db) - declared):
            fails.append(f"undeclared parity drift: skills/claude/{n} has no codex counterpart "
                         f"(activate for both, or declare in skills/PARITY.md)")
        for n in sorted((codex_db - claude_db) - declared):
            fails.append(f"undeclared parity drift: skills/codex/{n} has no claude counterpart "
                         f"(activate for both, or declare in skills/PARITY.md)")

    if fails:
        for msg in fails:
            print(f"skills: FAIL — {msg}", file=sys.stderr)
        print(f"skills: FAIL ({len(fails)} problems)", file=sys.stderr)
        sys.exit(1)
    print(f"skills: PASS (claude={len(claude_db)} codex={len(codex_db)} DB skills; "
          f"activations resolve; INDEX complete)")

if __name__ == "__main__":
    main()
