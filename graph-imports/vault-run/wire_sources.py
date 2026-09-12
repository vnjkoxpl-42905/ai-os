"""Give every concept note a clickable ## Source section.

The generated stub carries `source_file:` in frontmatter as inert text. Nothing to
click, nothing for Claude to follow. This run has an advantage the docs run did not:
the sources are already inside the vault, so the link points at the live file
instead of a copied mirror.

A concept that appeared in several files gets all of them — that list is itself
information (it shows which concepts are load-bearing across the corpus).
"""
import json
import re
from pathlib import Path

VAULT_ROOT = Path("/Users/joshuaf/ai-os")
NOTES = VAULT_ROOT / "graph-imports/vault"
EXTRACT = Path("graphify-out/.graphify_extract.json")

MARKER = "## Source"


def vault_link(abs_path):
    """Absolute path -> Obsidian wikilink target, vault-relative.

    Only markdown drops its extension. Obsidian resolves [[a/b]] to b.md, so a
    .html or .pdf source must keep its suffix or the link dangles.
    """
    rel = Path(abs_path).relative_to(VAULT_ROOT)
    return str(rel.with_suffix("")) if rel.suffix.lower() == ".md" else str(rel)


def main():
    nodes = json.loads(EXTRACT.read_text())["nodes"]

    # label -> ordered unique source files
    by_label = {}
    for n in nodes:
        srcs = n.get("source_files") or ([n["source_file"]] if n.get("source_file") else [])
        clean = []
        for s in srcs:
            if s and s not in clean and Path(s).exists():
                clean.append(s)
        if clean:
            by_label[n.get("label", n["id"])] = clean

    wired = skipped = already = 0
    unmatched = []

    for note in NOTES.glob("*.md"):
        # Community overviews are _COMMUNITY_*. Do not filter on a bare leading
        # underscore: real concept labels start with one too (the curriculum's
        # _question-feature-index/ nodes), and they would silently go unwired.
        if note.name.startswith("_COMMUNITY_"):
            continue
        text = note.read_text()
        if MARKER in text:
            already += 1
            continue

        m = re.search(r"^# (.+)$", text, re.MULTILINE)
        if not m:
            skipped += 1
            continue
        title = m.group(1).strip()

        srcs = by_label.get(title)
        if not srcs:
            unmatched.append(title)
            skipped += 1
            continue

        lines = [f"\n{MARKER}\n"]
        if len(srcs) == 1:
            lines.append(f"- [[{vault_link(srcs[0])}]]\n")
        else:
            lines.append(
                f"Appears in {len(srcs)} files — a concept this recurrent is "
                f"load-bearing across the corpus.\n\n"
            )
            for s in srcs:
                lines.append(f"- [[{vault_link(s)}]]\n")

        # insert before the trailing tag line so tags stay last
        tag_line = re.search(r"\n(#graphify/[^\n]*)\s*$", text)
        if tag_line:
            text = text[:tag_line.start()] + "\n" + "".join(lines) + "\n" + tag_line.group(1) + "\n"
        else:
            text = text.rstrip() + "\n" + "".join(lines)

        note.write_text(text)
        wired += 1

    total = wired + already
    print(f"wired {wired} notes ({already} already had a Source section)")
    print(f"skipped {skipped}")
    if unmatched:
        print(f"unmatched titles ({len(unmatched)}), first 15:")
        for u in unmatched[:15]:
            print(f"  {u}")
    print(f"coverage: {total}/{total + skipped} concept notes carry a source link")


if __name__ == "__main__":
    main()
