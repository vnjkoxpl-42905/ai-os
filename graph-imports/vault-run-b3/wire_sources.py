"""Give every batch-3 concept note a clickable ## Source section.

Batch 3's provenance is one hop, not batch 2's two:

    concept note  ->  skill file

There is no distillate layer; the skill markdown IS the source. But batch 3 has
a wrinkle batch 2 did not: the corpus was deduplicated by content hash before
extraction, so 253 byte-identical files were dropped. Their paths are NOT lost
— each canonical file carries its dropped twins as `aliases` in the corpus
manifest, and they are emitted here as "also at" links.

That matters because the dedup was almost entirely claude/ vs codex/ mirrors.
A note whose source has an alias is telling you the concept is live in BOTH
runtimes; a note with no alias is telling you it exists in only one. Dropping
the aliases would silently destroy that signal.
"""
import json
import re
from pathlib import Path

VAULT_ROOT = Path("/Users/joshuaf/ai-os")
SKILLS = VAULT_ROOT / "skills"
NOTES = VAULT_ROOT / "graph-imports/vault-b3"
EXTRACT = Path("graphify-out/.graphify_extract.json")
CORPUS = Path("graphify-out/.b3_corpus.json")

MARKER = "## Source"


def vault_link(rel_path):
    """Vault-relative path -> Obsidian wikilink target.

    Only markdown drops its extension. Obsidian resolves [[a/b]] to b.md, so a
    non-.md source must keep its suffix or the link dangles.
    """
    p = Path(rel_path)
    return str(p.with_suffix("")) if p.suffix.lower() == ".md" else str(p)


def to_rel(src):
    """Agent-written source path -> vault-relative path, or None if it escapes.

    Agents were told to write absolute paths, but tolerate a few shapes rather
    than silently dropping a real source over a leading-slash difference.
    """
    s = str(src).strip()
    for prefix in (str(VAULT_ROOT) + "/", "./"):
        if s.startswith(prefix):
            s = s[len(prefix):]
            break
    if s.startswith("skills/"):
        rel = s
    elif (SKILLS / s).exists():
        rel = f"skills/{s}"
    else:
        return None
    return rel if (VAULT_ROOT / rel).exists() else None


def build_alias_map():
    """vault-relative canonical path -> list of vault-relative dropped twins."""
    corpus = json.loads(CORPUS.read_text())
    alias_map = {}
    for canon, v in corpus.items():
        rel = to_rel(canon)
        if not rel:
            continue
        twins = [to_rel(a) for a in v.get("aliases", [])]
        alias_map[rel] = [t for t in twins if t]
    return alias_map


def main():
    nodes = json.loads(EXTRACT.read_text())["nodes"]
    alias_map = build_alias_map()
    print(f"canonical -> alias map: {len(alias_map)} entries, "
          f"{sum(len(v) for v in alias_map.values())} dropped twins recoverable")

    # label -> ordered unique vault-relative skill paths
    by_label = {}
    for n in nodes:
        srcs = n.get("sources") or n.get("source_files") or (
            [n["source_file"]] if n.get("source_file") else [])
        clean = []
        for s in srcs:
            rel = to_rel(s)
            if rel and rel not in clean:
                clean.append(rel)
        if clean:
            by_label[n.get("label", n["id"])] = clean

    wired = skipped = already = 0
    unmatched = []

    for note in NOTES.glob("*.md"):
        # Community overviews are _COMMUNITY_*. Do not filter on a bare leading
        # underscore: real concept labels can start with one too.
        if note.name.startswith("_COMMUNITY_") or note.name == "INDEX.md":
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
                f"Appears in {len(srcs)} skill files — a concept this recurrent "
                f"is load-bearing across the catalog.\n\n"
            )
        for s in srcs:
            twins = alias_map.get(s, [])
            if twins:
                also = ", ".join(f"[[{vault_link(t)}]]" for t in twins)
                lines.append(f"- [[{vault_link(s)}]] — also at: {also}\n")
            else:
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
    denom = total + skipped
    if denom:
        print(f"coverage: {total}/{denom} concept notes carry a source link")


if __name__ == "__main__":
    main()
