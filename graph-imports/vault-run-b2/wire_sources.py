"""Give every batch-2 concept note a clickable ## Source section.

Batch 2 has a two-hop provenance chain the docs run and batch 1 did not:

    concept note  ->  distillate  ->  raw Gemini transcript

The distillate is what was extracted from; the raw transcript is the untouched
evidence. Both belong in the note, because the distillate is a lossy summary and
any claim worth challenging has to be checkable against the transcript.

The distillate -> raw mapping is read from each distillate's own `source:`
frontmatter rather than derived by string surgery, so a distillate that was ever
filed under a different path still resolves.

A concept that appeared in several distillates gets all of them — that list is
itself information (it shows which concepts are load-bearing across the corpus).
"""
import json
import re
from pathlib import Path

VAULT_ROOT = Path("/Users/joshuaf/ai-os")
DISTILLATES = VAULT_ROOT / "graph-imports/distillates"
NOTES = VAULT_ROOT / "graph-imports/vault-b2"
EXTRACT = Path("graphify-out/.graphify_extract.json")

MARKER = "## Source"


def vault_link(rel_path):
    """Vault-relative path -> Obsidian wikilink target.

    Only markdown drops its extension. Obsidian resolves [[a/b]] to b.md, so a
    non-.md source must keep its suffix or the link dangles.
    """
    p = Path(rel_path)
    return str(p.with_suffix("")) if p.suffix.lower() == ".md" else str(p)


def build_raw_map():
    """distillate path (relative to DISTILLATES) -> raw transcript path (vault-relative)."""
    raw_map = {}
    for p in DISTILLATES.rglob("*.md"):
        rel = str(p.relative_to(DISTILLATES))
        m = re.search(r"^source:\s*(.+?)\s*$", p.read_text(), re.MULTILINE)
        if not m:
            continue
        raw = m.group(1).strip().strip("\"'")
        if (VAULT_ROOT / raw).exists():
            raw_map[rel] = raw
    return raw_map


def main():
    nodes = json.loads(EXTRACT.read_text())["nodes"]
    raw_map = build_raw_map()
    print(f"distillate -> raw transcript map: {len(raw_map)}/125 resolved")

    # label -> ordered unique distillate paths
    by_label = {}
    for n in nodes:
        srcs = n.get("source_files") or ([n["source_file"]] if n.get("source_file") else [])
        clean = []
        for s in srcs:
            if s and s not in clean and (DISTILLATES / s).exists():
                clean.append(s)
        if clean:
            by_label[n.get("label", n["id"])] = clean

    wired = skipped = already = 0
    unresolved_raw = 0
    unmatched = []

    for note in NOTES.glob("*.md"):
        # Community overviews are _COMMUNITY_*. Do not filter on a bare leading
        # underscore: real concept labels can start with one too.
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
        if len(srcs) > 1:
            lines.append(
                f"Appears in {len(srcs)} sessions — a concept this recurrent is "
                f"load-bearing across the corpus.\n\n"
            )
        for s in srcs:
            distillate_rel = f"graph-imports/distillates/{s}"
            raw = raw_map.get(s)
            if raw:
                lines.append(
                    f"- [[{vault_link(distillate_rel)}]] "
                    f"— raw: [[{vault_link(raw)}]]\n"
                )
            else:
                unresolved_raw += 1
                lines.append(f"- [[{vault_link(distillate_rel)}]]\n")

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
    if unresolved_raw:
        print(f"  {unresolved_raw} source lines had no resolvable raw transcript")
    if unmatched:
        print(f"unmatched titles ({len(unmatched)}), first 15:")
        for u in unmatched[:15]:
            print(f"  {u}")
    print(f"coverage: {total}/{total + skipped} concept notes carry a source link")


if __name__ == "__main__":
    main()
