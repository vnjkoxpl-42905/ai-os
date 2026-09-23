"""Phase 1 — the top-level retrieval manifest.

Generates `wiki/manifest.generated.md`: one line per curated note with its
subject and a one-sentence summary, grouped by area. This is the "wiki that
directs the agent" — read it first to locate the right note, then open only
that note instead of blind-searching the whole vault. Token-efficient by design.

Complements the hand-authored `wiki/index.md` (a small curated hub of the most
important pages). This file is COMPLETE coverage and regenerated, never
hand-edited — it carries the .generated.md suffix so the frontmatter pass skips
it and Obsidian/agents know it is machine-owned.

Reads the Phase 0 frontmatter (subject, type, lifecycle). Summary is the first
real sentence of the body, so notes with a good opening line get a good summary;
the rest are seeds to enrich later (same policy as aliases).

Usage:  build-manifest.py            # write the manifest
        build-manifest.py --dry-run  # print stats only
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CURATED = ["students", "corpus", "context", "decisions", "wiki",
           "references", "research", "handoffs", "brainstorms"]
OUT = ROOT / "wiki" / "manifest.generated.md"

AREA_TITLE = {
    "students": "Students",
    "corpus": "Corpus — LSAT teaching knowledge",
    "context": "Context — who Joshua is, the business, priorities",
    "decisions": "Decisions",
    "wiki": "Wiki — operating layer",
    "references": "References — methods and how-it-works",
    "research": "Research — external teardowns",
    "handoffs": "Handoffs — session records",
    "brainstorms": "Brainstorms — design and planning",
}


def clean(s: str) -> str:
    s = s.replace("—", "-").replace("–", "-")
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def split_fm(text: str):
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            return text[4:end + 1], text[end + 4:].lstrip("\n")
    return "", text


def fm_val(fm: str, key: str):
    m = re.search(rf"(?m)^{re.escape(key)}:\s*(.*)$", fm)
    return m.group(1).strip() if m else None


SENT_END = re.compile(r"(?<=[.!?])\s")


def summary(body: str) -> str:
    """First real sentence of the body: skip headings, blockquotes, lists,
    tables, code fences, images, and bare wikilink rosters."""
    in_code = False
    for raw in body.splitlines():
        ln = raw.strip()
        if ln.startswith("```"):
            in_code = not in_code
            continue
        if in_code or not ln:
            continue
        if ln[0] in "#>|-*" or ln.startswith("!["):
            continue
        # a line that is only wikilinks/separators is a roster, not prose
        if re.fullmatch(r"[\[\]\|\w\s,.·&/'()-]*", ln) and "[[" in ln and " " not in re.sub(r"\[\[[^\]]*\]\]", "", ln):
            continue
        text = clean(re.sub(r"\[\[([^\]|]*\|)?([^\]]*)\]\]", r"\2", ln))  # unwrap wikilinks
        text = re.sub(r"[*_`]", "", text)  # drop md emphasis
        if not text:
            continue
        first = SENT_END.split(text, 1)[0]
        if len(first) > 160:
            first = first[:157].rsplit(" ", 1)[0] + "…"
        return first
    return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    sections = {}
    counts = {}
    for d in CURATED:
        base = ROOT / d
        rows = []
        for path in sorted(base.rglob("*.md")):
            if path.name.endswith(".generated.md"):
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            fm, body = split_fm(text)
            subject = clean(fm_val(fm, "subject") or path.stem)
            typ = fm_val(fm, "type") or "note"
            life = fm_val(fm, "lifecycle")
            rel = path.relative_to(ROOT)
            summ = summary(body)
            tag = f"`{typ}`"
            if life:
                tag += f" · `{life}`"
            line = f"- [[{rel}|{subject}]] — {tag}" + (f" — {summ}" if summ else "")
            rows.append((str(rel), line))
        rows.sort()
        sections[d] = [r[1] for r in rows]
        counts[d] = len(rows)

    total = sum(counts.values())
    lines = [
        "---",
        "type: operating-layer",
        "subject: Retrieval manifest",
        "aliases: [manifest, directory, index-of-everything]",
        "generated: true",
        "---",
        "",
        "# Retrieval manifest (generated)",
        "",
        "**Generated file — do not hand-edit.** Rebuild with "
        "`python3 system/scripts/build-manifest.py`.",
        "",
        f"Complete directory of every curated note ({total} notes): subject, "
        "type, and a one-line summary, grouped by area. Read this first to find "
        "where something lives, then open just that note. This is the agent's "
        "routing map; the curated hub is [[index]].",
        "",
    ]
    for d in CURATED:
        if not sections[d]:
            continue
        lines.append(f"## {AREA_TITLE.get(d, d)} ({counts[d]})")
        lines.append("")
        lines.extend(sections[d])
        lines.append("")

    text = "\n".join(lines)
    if args.dry_run:
        print(f"manifest: {total} notes across {sum(1 for d in CURATED if sections[d])} areas")
        for d in CURATED:
            if sections[d]:
                print(f"  {d:12s} {counts[d]}")
        # show a few sample lines
        print("\nsample lines:")
        for d in ("context", "corpus", "students"):
            if sections[d]:
                for ln in sections[d][:2]:
                    print("  " + ln[:160])
        return 0

    OUT.write_text(text, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} — {total} notes, "
          f"{len(text.splitlines())} lines")
    return 0


if __name__ == "__main__":
    sys.exit(main())
