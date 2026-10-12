"""Inventory every SKILL.md across runtime roots and the catalog; check frontmatter and local links.

Run: uv run --with pyyaml python inventory.py > inventory.json
"""
import json, os, re, sys
from pathlib import Path
import yaml

HOME = Path.home()
VAULT = HOME / "dev" / "ai-os"
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

ROOTS = {
    "claude:global": HOME / ".claude" / "skills",
    "claude:project": VAULT / ".claude" / "skills",
    "codex:global-agents": HOME / ".agents" / "skills",
    "codex:global-codex": HOME / ".codex" / "skills",
    "codex:project": VAULT / ".agents" / "skills",
    "gemini:project": VAULT / ".gemini" / "skills",
    "db:claude": VAULT / "skills" / "claude",
    "db:codex": VAULT / "skills" / "codex",
    "db:gemini": VAULT / "skills" / "gemini",
}
SKIP = {"_snapshots", "_project-forks", "_inactive", "_retired"}
KNOWN_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools",
              "argument-hint", "disable-model-invocation", "user-invocable", "model", "context",
              "agent", "hooks", "version", "when_to_use", "when-to-use"}


def split_frontmatter(text):
    if not text.startswith("---"):
        return None, text
    m = re.match(r"^---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(\r?\n|$)", text, re.S)
    if not m:
        return None, text
    return m.group(1), text[m.end():]


def local_links(body):
    out = []
    for target in re.findall(r"\]\(([^)\s]+)\)", body):
        if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
            continue
        out.append(target.split("#")[0])
    return out


def scan_skill(root_key, root, entry):
    d = root / entry
    rec = {"root": root_key, "dir": entry, "path": str(d), "symlink": d.is_symlink(), "issues": []}
    skf = d / "SKILL.md"
    if not skf.is_file():
        rec["issues"].append("no SKILL.md" + (" (broken symlink)" if d.is_symlink() and not d.exists() else ""))
        return rec
    raw = skf.read_bytes()
    rec["bytes"] = len(raw)
    text = raw.decode("utf-8", errors="replace")
    if raw.startswith(b"\xef\xbb\xbf"):
        rec["issues"].append("UTF-8 BOM before frontmatter")
        text = text.lstrip("﻿")
    rec["lines"] = text.count("\n") + 1
    fm, body = split_frontmatter(text)
    if fm is None:
        rec["issues"].append("no frontmatter")
        return rec
    try:
        data = yaml.safe_load(fm)
    except yaml.YAMLError as exc:
        rec["issues"].append("YAML error: " + str(exc).replace("\n", " ")[:200])
        data = None
    if not isinstance(data, dict):
        if data is not None:
            rec["issues"].append("frontmatter is not a mapping")
        return rec
    name = data.get("name")
    desc = data.get("description")
    rec["name"] = name
    rec["description"] = desc if isinstance(desc, str) else None
    rec["keys"] = sorted(map(str, data.keys()))
    unknown = [k for k in data if k not in KNOWN_KEYS]
    if unknown:
        rec["unknown_keys"] = unknown
    if not name:
        rec["issues"].append("missing name")
    elif not isinstance(name, str):
        rec["issues"].append(f"name not a string: {name!r}")
    else:
        if len(name) > 64:
            rec["issues"].append(f"name >64 chars ({len(name)})")
        if not NAME_RE.match(name):
            rec["issues"].append(f"name not kebab-case: {name!r}")
        if name != entry and not d.is_symlink():
            rec["issues"].append(f"name {name!r} != dir {entry!r}")
    if desc is None or (isinstance(desc, str) and not desc.strip()):
        rec["issues"].append("missing description")
    elif not isinstance(desc, str):
        rec["issues"].append(f"description not a string ({type(desc).__name__})")
    else:
        rec["desc_len"] = len(desc)
        if len(desc) > 1024:
            rec["issues"].append(f"description >1024 chars ({len(desc)})")
        if re.search(r"[<>]", desc):
            rec["issues"].append("description contains < or >")
    broken = []
    for target in local_links(body):
        if not target:
            continue
        p = (skf.parent / target)
        if not p.exists():
            broken.append(target)
    if broken:
        rec["broken_links"] = broken[:20]
        rec["issues"].append(f"{len(broken)} broken relative link(s)")
    return rec


def main():
    out = []
    for key, root in ROOTS.items():
        if not root.is_dir():
            continue
        for entry in sorted(os.listdir(root)):
            if entry.startswith(".") or entry in SKIP or entry.endswith(".md") or entry.endswith(".toml"):
                continue
            p = root / entry
            if not (p.is_dir() or p.is_symlink()):
                continue
            out.append(scan_skill(key, root, entry))
    # plugin skills
    cache = HOME / ".claude" / "plugins" / "cache"
    if cache.is_dir():
        for skf in cache.rglob("SKILL.md"):
            d = skf.parent
            rec = scan_skill("claude:plugin", d.parent, d.name)
            rec["plugin_path"] = str(d.relative_to(cache))
            out.append(rec)
    json.dump(out, sys.stdout, indent=1, default=str)


main()
