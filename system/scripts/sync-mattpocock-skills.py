"""Keep every installed mattpocock/skills copy in step with GitHub.

Which skills: every entry in ~/.agents/.skill-lock.json whose source is
mattpocock/skills (installed by the `skills` CLI).

Where copies live on this machine (plain copies, not links):
  ~/.agents/skills/<name>, ~/.claude/skills/<name>, and in the vault
  .claude/skills, .agents/skills, skills/{claude,codex,gemini}/<name>.

Compare-and-swap: a copy is replaced only when it still matches the upstream
version we last installed (recorded in the state file) or already matches the
new one. A copy that was edited locally is left alone and reported, so a
deliberate adaptation (e.g. the vault's grill-with-docs) is never overwritten.

Usage: python sync-mattpocock-skills.py [--dry-run] [--adopt]
  --adopt  first run only: treat copies whose SKILL.md matches upstream except
           for frontmatter as clean. Without it, unknown copies are skipped.
"""
import hashlib, io, json, os, shutil, subprocess, sys, tarfile, datetime, pathlib

HOME = pathlib.Path.home()
VAULT = pathlib.Path(__file__).resolve().parents[2]
LOCK = HOME / ".agents" / ".skill-lock.json"
STATE = HOME / ".agents" / "mattpocock-sync-state.json"
LOG = VAULT / "system" / "logs" / "mattpocock-skill-sync.log"
REPO = "mattpocock/skills"
ROOTS = [HOME / ".agents/skills", HOME / ".claude/skills", VAULT / ".claude/skills",
         VAULT / ".agents/skills", VAULT / "skills/claude", VAULT / "skills/codex",
         VAULT / "skills/gemini"]
# Deliberate local rewrites: never replaced, reported quietly as KEEP.
KEEP = {"grill-me"}  # why: skills/PARITY.md
DRY = "--dry-run" in sys.argv
ADOPT = "--adopt" in sys.argv


def tree_hash(files):
    h = hashlib.sha256()
    for rel in sorted(files):
        h.update(rel.encode()); h.update(b"\0"); h.update(files[rel]); h.update(b"\0")
    return h.hexdigest()


def read_dir(d):
    out = {}
    for p in d.rglob("*"):
        if p.is_file() and "__pycache__" not in p.parts:
            out[p.relative_to(d).as_posix()] = p.read_bytes().replace(b"\r\n", b"\n")
    return out


def fetch_upstream():
    sha = subprocess.check_output(["gh", "api", f"repos/{REPO}/commits/main", "--jq", ".sha"], text=True).strip()
    raw = subprocess.check_output(["gh", "api", f"repos/{REPO}/tarball/{sha}"])
    skills = {}
    with tarfile.open(fileobj=io.BytesIO(raw)) as tf:
        for m in tf.getmembers():
            if not m.isfile():
                continue
            parts = m.name.split("/")[1:]  # drop the tarball's top folder
            if len(parts) >= 4 and parts[0] == "skills":
                skill_dir = "/".join(parts[:3])  # skills/<group>/<name>
                skills.setdefault(skill_dir, {})["/".join(parts[3:])] = tf.extractfile(m).read()
    return sha, skills


_past = {}


def past_versions(path):
    """Every SKILL.md text this file has had upstream (for --adopt)."""
    if path not in _past:
        shas = subprocess.check_output(["gh", "api", f"repos/{REPO}/commits?path={path}&per_page=100",
                                        "--jq", ".[].sha"], text=True).split()
        _past[path] = set()
        for s in shas:
            try:
                raw = subprocess.check_output(["gh", "api", f"repos/{REPO}/contents/{path}?ref={s}",
                                               "-H", "Accept: application/vnd.github.raw"])
                _past[path].add(raw.replace(b"\r\n", b"\n"))
            except subprocess.CalledProcessError:
                pass
    return _past[path]


def main():
    lock = json.loads(LOCK.read_text(encoding="utf-8"))
    mine = {k: v for k, v in lock["skills"].items() if v.get("source") == REPO}
    state = json.loads(STATE.read_text(encoding="utf-8")) if STATE.exists() else {"skills": {}}
    sha, upstream = fetch_upstream()
    lines, changed = [], False
    for name, entry in sorted(mine.items()):
        skill_dir = os.path.dirname(entry["skillPath"].replace("\\", "/"))
        new = upstream.get(skill_dir)
        if new is None:
            lines.append(f"GONE upstream: {name} ({skill_dir})"); continue
        new_h = tree_hash(new)
        prev_h = state["skills"].get(name)
        for root in ROOTS:
            d = root / name
            if not d.is_dir() or d.is_symlink():
                continue
            cur = read_dir(d)
            cur_h = tree_hash(cur)
            if cur_h == new_h:
                continue
            clean = prev_h is not None and cur_h == prev_h
            if not clean and ADOPT and "SKILL.md" in cur and "SKILL.md" in new:
                body = lambda b: b.split(b"\n---", 1)[-1]
                clean = body(cur["SKILL.md"]) == body(new["SKILL.md"]) or \
                    cur["SKILL.md"] in past_versions(skill_dir + "/SKILL.md")
            if not clean:
                lines.append(f"{'KEEP local rewrite' if name in KEEP else 'SKIP locally edited (review)'}: {d}"); continue
            lines.append(f"UPDATE {d}")
            if not DRY:
                for rel in cur:
                    if rel not in new:
                        (d / rel).unlink()
                for rel, data in new.items():
                    (d / rel).parent.mkdir(parents=True, exist_ok=True)
                    (d / rel).write_bytes(data)
            changed = True
        state["skills"][name] = new_h
        if not DRY:
            entry["updatedAt"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    new_upstream = sorted(n.split("/")[-1] for n in upstream
                          if n.split("/")[1] != "deprecated" and n.split("/")[-1] not in mine)
    if new_upstream:
        lines.append("NOT INSTALLED (new upstream, not auto-added): " + ", ".join(new_upstream))
    stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    report = f"[{stamp}] {REPO}@{sha[:7]} {'(dry run) ' if DRY else ''}{len(mine)} skills\n" + "".join(f"  {l}\n" for l in lines)
    print(report, end="")
    if not DRY:
        state["commit"] = sha
        STATE.write_text(json.dumps(state, indent=2), encoding="utf-8")
        if changed:
            LOCK.write_text(json.dumps(lock, indent=2), encoding="utf-8")
        LOG.parent.mkdir(parents=True, exist_ok=True)
        with LOG.open("a", encoding="utf-8") as f:
            f.write(report)


if __name__ == "__main__":
    main()
