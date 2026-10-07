"""Rename notes that graphify's sanitizer turned into hidden dotfiles.

A node label like `.claude/plugin-name.local.md settings pattern` sanitizes to a
filename with a leading dot. Obsidian does not display it, `ls *.md` does not
match it, and shell globs silently skip it — so the note exists, carries real
edges, and is invisible to every consumer. Batch 3 shipped one of these and it
was only found by reconciling two file counts that disagreed by one.

Fixing the built vault by hand is not enough: the label is still dotted in the
graph, so the next rebuild recreates the hidden file. This runs as a pipeline
step after the vault export, and is idempotent.

The label itself is deliberately left alone — `.claude/...` is the accurate name
for the concept, and rewriting it to satisfy a filesystem convention would make
the graph lie about what the file is called.
"""
import json
import re
import sys
from pathlib import Path

RUN = Path(__file__).resolve().parent
VAULT = RUN.parent / "vault-b3"
CANVAS = VAULT / "graph.canvas"


def main():
    hidden = sorted(p for p in VAULT.iterdir()
                    if p.name.startswith(".") and p.suffix == ".md")
    if not hidden:
        print("no hidden notes — nothing to do")
        return 0

    renames = {}
    for p in hidden:
        new_stem = p.stem.lstrip(".")
        if not new_stem:
            print(f"  SKIP {p.name}: strips to an empty name")
            continue
        target = VAULT / f"{new_stem}.md"
        if target.exists():
            # A previous run renamed this note, then a rebuild regenerated the
            # dotted original — so both exist and the vault is one note over
            # count. The freshly exported dotfile is authoritative; the
            # un-dotted leftover is stale output from the prior build. Replace
            # it. Refusing here instead leaves a duplicate that inflates every
            # count and silently diverges from the graph.
            print(f"  replacing stale {target.name} with fresh export")
            target.unlink()
        p.rename(target)
        renames[p.stem] = new_stem
        print(f"  renamed {p.name} -> {target.name}")

    if not renames:
        return 0

    # Repoint every inbound wikilink. Missing this leaves dead links that look
    # like extraction gaps rather than a rename artifact.
    repointed = 0
    for f in list(VAULT.glob("*.md")) + ([CANVAS] if CANVAS.exists() else []):
        text = original = f.read_text(errors="replace")
        for old, new in renames.items():
            text = text.replace(f"[[{old}]]", f"[[{new}]]")
            text = text.replace(f"[[{old}|", f"[[{new}|")
            if f == CANVAS:
                text = text.replace(f"{old}.md", f"{new}.md")
        if text != original:
            f.write_text(text)
            repointed += 1

    if CANVAS.exists():
        try:
            json.loads(CANVAS.read_text())
        except json.JSONDecodeError as e:
            print(f"  ERROR: canvas is no longer valid JSON: {e}")
            return 1

    print(f"renamed {len(renames)} note(s), repointed links in {repointed} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
