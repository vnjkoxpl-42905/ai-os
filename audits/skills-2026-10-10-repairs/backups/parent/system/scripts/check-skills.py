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
  (h) effective Claude/Codex skill availability has no undeclared one-runtime drift;
  (i) active instruction scopes have both CLAUDE.md and AGENTS.md;
  (j) Codex agent TOML files are valid, complete, and activated from the catalog.
Exit 0 = PASS, 1 = FAIL.
"""
from project_paths import project_path, VAULT_ROOT
import os, re, sys, filecmp, tomllib, subprocess
from pathlib import Path

BRAIN = str(Path(__file__).resolve().parents[2])
DB = os.path.join(BRAIN, "skills")
HOME = str(Path.home())
SPECIAL = {"_snapshots", "_project-forks", "_inactive", "README.md", "INDEX.md"}

# Active roots to audit (only those that exist are checked).
PROJECT_ACTIVE_ROOTS = [
    os.path.join(BRAIN, ".claude", "skills"),
    os.path.join(BRAIN, ".agents", "skills"),
    str(project_path("email-hq", ".claude", "skills")),
]

# Home-level roots also contain skills installed and managed by external plugins.
# They are included when comparing effective Claude/Codex availability, but they
# are not required to be mirrored into this project's catalog.
RUNTIME_ACTIVE_ROOTS = {
    "claude": [os.path.join(HOME, ".claude", "skills"),
               os.path.join(BRAIN, ".claude", "skills")],
    "codex": [os.path.join(HOME, ".agents", "skills"),
              os.path.join(BRAIN, ".agents", "skills")],
}

def db_names(sub):
    base = os.path.join(DB, sub)
    if not os.path.isdir(base):
        return set()
    return {n for n in os.listdir(base)
            if n not in SPECIAL and (os.path.isdir(os.path.join(base, n)) or os.path.islink(os.path.join(base, n)))}


def entrypoints_match(first, second):
    """Resolve valid local links so documented relocation is not content drift."""
    first, second = Path(first), Path(second)
    a = first.read_text(encoding="utf-8").replace("\r\n", "\n")
    b = second.read_text(encoding="utf-8").replace("\r\n", "\n")
    if a == b:
        return True
    pattern = r"\]\(([^)]+)\)"
    left, right = list(re.finditer(pattern, a)), list(re.finditer(pattern, b))
    if len(left) != len(right):
        return False
    if re.sub(pattern, "](<link>)", a) != re.sub(pattern, "](<link>)", b):
        return False
    for x, y in zip(left, right):
        t1, t2 = x.group(1), y.group(1)
        if t1 == t2:
            continue
        if any(re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", t) for t in (t1, t2)):
            return False
        p1, _, anchor1 = t1.partition("#")
        p2, _, anchor2 = t2.partition("#")
        r1, r2 = (first.parent / p1).resolve(), (second.parent / p2).resolve()
        if anchor1 != anchor2 or r1 != r2 or not r1.exists():
            return False
    return True

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
    for root in PROJECT_ACTIVE_ROOTS:
        if not os.path.isdir(root):
            continue
        for n in os.listdir(root):
            if n.startswith("."):
                continue
            p = os.path.join(root, n)
            if os.path.islink(p):
                if not os.path.exists(p):
                    fails.append(f"broken activation symlink: {root}/{n}")
                elif n not in all_db:
                    fails.append(f"activation not represented in DB: {root}/{n} -> {os.path.realpath(p)}")
            elif os.path.isdir(p):
                # real dir in an active root: must be mirrored in DB by name
                if n not in all_db:
                    fails.append(f"un-mirrored skill in active root: {root}/{n} (not in DB)")
                    continue
                # (e) drift check: copied activation's SKILL.md vs its DB source
                sub = "codex" if ".agents" in Path(root).parts else "claude"
                db_dir = os.path.join(DB, sub, n)
                act_skf = os.path.join(p, "SKILL.md")
                db_skf = os.path.join(db_dir, "SKILL.md")
                if os.path.isfile(act_skf) and os.path.isfile(db_skf):
                    if not entrypoints_match(act_skf, db_skf):
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
    remote_ids = set()
    remote = subprocess.run(["git", "-C", BRAIN, "remote", "get-url", "origin"], capture_output=True, text=True)
    match = re.search(r"github\.com[:/]([^/]+/[^/\s]+?)(?:\.git)?$", remote.stdout.strip())
    if match:
        remote_ids.add(match.group(1))
    for fname in ("CLAUDE.md", "AGENTS.md"):
        fpath = os.path.join(BRAIN, fname)
        if not os.path.isfile(fpath):
            fails.append(f"routing file missing: {fname}")
            continue
        with open(fpath, encoding="utf-8") as f:
            text = f.read()
        for cand in sorted(set(re.findall(r"`([^`\s]+/[^`\s]+)`", text))):
            if cand.startswith("http") or cand in remote_ids or any(c in cand for c in "<>*{}|"):
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
        pairs = {}
        pair_file = Path(DB) / "runtime-pairs.toml"
        if pair_file.exists():
            pairs = tomllib.loads(pair_file.read_text(encoding="utf-8")).get("pairs", {})
            for claude_name, codex_name in pairs.items():
                if claude_name not in claude_db or codex_name not in codex_db:
                    fails.append(f"missing paired runtime skill: {claude_name} -> {codex_name}")
                else:
                    declared.update((claude_name, codex_name))
        for n in sorted((claude_db - codex_db) - declared):
            fails.append(f"undeclared parity drift: skills/claude/{n} has no codex counterpart "
                         f"(activate for both, or declare in skills/PARITY.md)")
        for n in sorted((codex_db - claude_db) - declared):
            fails.append(f"undeclared parity drift: skills/codex/{n} has no claude counterpart "
                         f"(activate for both, or declare in skills/PARITY.md)")

        # (h) effective runtime parity. Project activations can satisfy a skill
        # absent from the home-level root and vice versa. External plugin skills
        # do not have to live in this DB, but unexplained one-runtime availability
        # is still drift worth surfacing.
        effective = {}
        for runtime, roots in RUNTIME_ACTIVE_ROOTS.items():
            names = set()
            for root in roots:
                if os.path.isdir(root):
                    names.update(
                        n for n in os.listdir(root)
                        if not n.startswith(".")
                        and os.path.isfile(os.path.join(root, n, "SKILL.md"))
                    )
            effective[runtime] = names
        for claude_name, codex_name in pairs.items():
            if (claude_name in effective["claude"]) != (codex_name in effective["codex"]):
                fails.append(f"incomplete paired activation: Claude {claude_name} / Codex {codex_name}")
        for n in sorted((effective["claude"] - effective["codex"]) - declared):
            fails.append(f"undeclared activation drift: {n} is available to Claude but not Codex")
        for n in sorted((effective["codex"] - effective["claude"]) - declared):
            fails.append(f"undeclared activation drift: {n} is available to Codex but not Claude")

    # (i) instruction twins. Frozen, imported, and vendor reference material is
    # not an active project scope and is intentionally excluded.
    ignored_parts = {".git", "archive", "graph-imports", "node_modules", "raw", "reference", "_snapshots", "anthropic-capture"}
    for current, dirs, files in os.walk(BRAIN):
        dirs[:] = [d for d in dirs if d not in ignored_parts]
        present = set(files)
        if "CLAUDE.md" in present and "AGENTS.md" not in present:
            fails.append(f"missing AGENTS.md peer: {os.path.relpath(current, BRAIN)}")
        if "AGENTS.md" in present and "CLAUDE.md" not in present:
            fails.append(f"missing CLAUDE.md peer: {os.path.relpath(current, BRAIN)}")

    # (j) project-scoped Codex agents.
    agent_catalog = os.path.join(BRAIN, "agents", "codex")
    agent_active = os.path.join(BRAIN, ".codex", "agents")
    if os.path.isdir(agent_catalog):
        for name in sorted(n for n in os.listdir(agent_catalog) if n.endswith(".toml")):
            source = os.path.join(agent_catalog, name)
            try:
                with open(source, "rb") as handle:
                    data = tomllib.load(handle)
            except (OSError, tomllib.TOMLDecodeError) as exc:
                fails.append(f"invalid Codex agent TOML: agents/codex/{name}: {exc}")
                continue
            for field in ("name", "description", "developer_instructions"):
                if not data.get(field):
                    fails.append(f"Codex agent missing {field}: agents/codex/{name}")
            activated = os.path.join(agent_active, name)
            if not os.path.isfile(activated):
                fails.append(f"Codex agent not activated: .codex/agents/{name}")
            elif not filecmp.cmp(source, activated, shallow=False):
                fails.append(f"stale Codex agent activation: .codex/agents/{name}")

    if fails:
        for msg in fails:
            print(f"skills: FAIL — {msg}", file=sys.stderr)
        print(f"skills: FAIL ({len(fails)} problems)", file=sys.stderr)
        sys.exit(1)
    print(f"skills: PASS (claude={len(claude_db)} codex={len(codex_db)} DB skills; "
          f"activations resolve; INDEX complete)")

if __name__ == "__main__":
    main()
