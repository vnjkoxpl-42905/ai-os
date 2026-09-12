#!/usr/bin/env python3
"""Inventory the Gemini session transcripts and map them to student folders.

Read-only. Writes nothing, moves nothing — it prints a report that the `ingest`
skill (and a human) act on. It exists because the mapping step is the expensive
part: transcript filenames are inconsistent ("Dakota", "sofia", "LSAT Session
between Joshua and Meghan Mullins", "Meeting started <date>"), and every past
session re-derived that mapping by hand.

Filename shapes actually present in raw/data-about-me/transcripts/:
    <Name> - <YYYY_MM_DD HH_MM TZ> - Notes by Gemini.docx
    <Kind> between Joshua and <Name> - <date> - Notes by Gemini.docx
    Meeting started <date> - Notes by Gemini.docx        <- no name, unresolvable

Usage:
    python3 system/scripts/transcript-inventory.py            # summary
    python3 system/scripts/transcript-inventory.py --unmatched  # only the gaps
    python3 system/scripts/transcript-inventory.py --json      # machine-readable
    python3 system/scripts/transcript-inventory.py --text <file.docx>  # dump one transcript as text

--text exists because neither python-docx nor pandoc is installed on the
Windows box; a .docx is a zip with word/document.xml inside, and that is all a
reader needs.
"""
import json
import os
import re
import sys
import unicodedata
import zipfile

# The vault root is two levels up from this file (system/scripts/), so the
# script works on any machine. AI_OS_ROOT overrides it if the layout ever moves.
BRAIN = os.environ.get(
    "AI_OS_ROOT",
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
)
TRANSCRIPTS = f"{BRAIN}/raw/data-about-me/transcripts"
STUDENTS = f"{BRAIN}/students"

# The date stamp is the one reliable anchor. Everything after it is an artifact
# label that varies ("Notes by Gemini", "Chat", "Recording-captions"), so match
# the stamp itself and treat the remainder as the artifact kind.
DATE_RE = re.compile(r"\s*-?\s*(\d{4})_(\d{2})_(\d{2})\s+(\d{2})_(\d{2})\s+\w+\s*-?\s*", re.I)
ARTIFACT_RE = re.compile(r"^(Notes by Gemini|Chat|Recording-captions|Transcript)$", re.I)
BETWEEN_RE = re.compile(r"^(?P<kind>.*?)\bbetween Joshua and\b\s*(?P<name>.+)$", re.I)
MEETING_RE = re.compile(r"^Meeting started\b", re.I)


def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


FORMER = os.path.join(STUDENTS, "non-students")


def student_dirs():
    """Current student folders plus former ones under students/non-students/.

    Former students moved there on 2026-09-10 and are excluded from every
    sweep, but a transcript of theirs still needs to *resolve* -- otherwise it
    surfaces as "no student folder" every run and tempts a session to create
    a duplicate folder for someone who already has a record.
    """
    out = {}
    for base in (STUDENTS, FORMER):
        if not os.path.isdir(base):
            continue
        for n in sorted(os.listdir(base)):
            p = os.path.join(base, n)
            if os.path.isdir(p) and not n.startswith("_") and n != "non-students":
                out[n] = p
    return out


def is_former(slug_, dirs):
    return slug_ in dirs and dirs[slug_].startswith(FORMER)


def parse(fname):
    """-> dict(subject, kind, artifact, date, time, raw)"""
    stem = os.path.splitext(fname)[0]
    m = DATE_RE.search(stem)
    date = f"{m.group(1)}-{m.group(2)}-{m.group(3)}" if m else None
    time = f"{m.group(4)}:{m.group(5)}" if m else None
    if m:
        head = stem[:m.start()].strip()
        tail = stem[m.end():].strip()
    else:
        head, tail = stem.strip(), ""
    artifact = tail if ARTIFACT_RE.match(tail) else (tail or "unknown")
    head = re.sub(r"\s*-\s*$", "", head).strip()

    if MEETING_RE.match(head) or not head:
        return dict(subject=None, kind="meeting", artifact=artifact,
                    date=date, time=time, raw=head or stem)
    b = BETWEEN_RE.match(head)
    if b:
        kind = re.sub(r"\s+", " ", b.group("kind")).strip() or "session"
        return dict(subject=re.sub(r"\s+", " ", b.group("name")).strip(),
                    kind=kind.lower(), artifact=artifact, date=date, time=time, raw=head)
    return dict(subject=re.sub(r"\s+", " ", head).strip(), kind="session",
                artifact=artifact, date=date, time=time, raw=head)


def load_aliases():
    """Parse students/_aliases.md -> {alias_slug: folder_slug}.

    Only the '## Aliases' section is a mapping; the other sections are human
    notes about names deliberately without folders.
    """
    path = os.path.join(STUDENTS, "_aliases.md")
    out = {}
    if not os.path.isfile(path):
        return out
    section = None
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.startswith("## "):
                section = line.strip().lower()
                continue
            if section == "## aliases":
                m = re.match(r"\s*-\s*(.+?)\s*->\s*([a-z0-9-]+)\s*$", line)
                if m:
                    out[slug(m.group(1))] = m.group(2)
            elif section and section.startswith("## prospects"):
                # Consulted but never taught, so no student record. Still prospects
                # on the same path as everyone else -- see CONTEXT.md. Mapped to
                # None so they stop surfacing as unresolved every run.
                m = re.match(r"\s*-\s*([^—-]+?)\s*(?:—.*)?$", line)
                if m:
                    out[slug(m.group(1))] = None
    return out


def match_student(subject, dirs, aliases=None):
    """Map a transcript subject to a student folder. Returns (slug, how) or (None, why).

    Deliberately conservative: exact slug, then first-name, then containment.
    An ambiguous first name (two students named Sofia) returns None so a human
    decides rather than the script silently picking one.
    """
    if not subject:
        return None, "no subject in filename"
    s = slug(subject)
    if aliases and s in aliases:
        target = aliases[s]
        if target is None:
            return None, "prospect, no record"
        return (target, "alias") if target in dirs else (None, f"alias -> missing folder '{target}'")
    if s in dirs:
        return s, "exact"
    first = s.split("-")[0]
    hits = [d for d in dirs if d == first or d.startswith(first + "-")]
    if len(hits) == 1:
        return hits[0], "first-name"
    if len(hits) > 1:
        return None, f"ambiguous: {', '.join(hits)}"
    hits = [d for d in dirs if first and (first in d.split("-"))]
    if len(hits) == 1:
        return hits[0], "contains"
    if len(hits) > 1:
        return None, f"ambiguous: {', '.join(hits)}"
    return None, "no student folder"


def docx_text(path):
    """Paragraph text of a .docx, one paragraph per line, no dependencies."""
    with zipfile.ZipFile(path) as z:
        xml = z.read("word/document.xml").decode("utf-8", "replace")
    paras = re.split(r"</w:p>", xml)
    out = []
    for para in paras:
        text = "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", para))
        if text.strip():
            out.append(text)
    return "\n".join(out)


def docx_words(path):
    """Rough word count from a .docx without any third-party dependency."""
    try:
        with zipfile.ZipFile(path) as z:
            xml = z.read("word/document.xml").decode("utf-8", "replace")
    except Exception:
        return None
    text = re.sub(r"<[^>]+>", " ", xml)
    return len(text.split())


def main():
    args = set(sys.argv[1:])
    if "--text" in sys.argv:
        target = sys.argv[sys.argv.index("--text") + 1]
        if not os.path.isabs(target) and not os.path.isfile(target):
            target = os.path.join(TRANSCRIPTS, target)
        sys.stdout.reconfigure(encoding="utf-8")
        print(docx_text(target))
        return 0
    if not os.path.isdir(TRANSCRIPTS):
        print(f"no transcript dir: {TRANSCRIPTS}", file=sys.stderr)
        return 1
    dirs = student_dirs()
    aliases = load_aliases()
    rows = []
    for f in sorted(os.listdir(TRANSCRIPTS)):
        if f.startswith(".") or not f.lower().endswith((".docx", ".txt")):
            continue
        p = os.path.join(TRANSCRIPTS, f)
        info = parse(f)
        sl, how = match_student(info["subject"], dirs, aliases)
        rows.append(dict(file=f, **info, student=sl, match=how,
                         former=bool(sl and is_former(sl, dirs)),
                         words=docx_words(p) if f.lower().endswith(".docx") else None,
                         bytes=os.path.getsize(p)))

    if "--json" in args:
        print(json.dumps(rows, indent=2))
        return 0

    matched = [r for r in rows if r["student"] and not is_former(r["student"], dirs)]
    former = [r for r in rows if r["student"] and is_former(r["student"], dirs)]
    declared = [r for r in rows if not r["student"] and r["match"] == "prospect, no record"]
    unmatched = [r for r in rows if not r["student"] and r["match"] != "prospect, no record"]

    if "--unmatched" not in args:
        print(f"transcripts: {len(rows)} files, {len(matched)} mapped, "
              f"{len(former)} former students, {len(declared)} prospects (no record), "
              f"{len(unmatched)} unmapped, {len(dirs)} student folders\n")
        by = {}
        for r in matched:
            by.setdefault(r["student"], []).append(r)
        print("MAPPED")
        for s in sorted(by):
            ds = sorted(x["date"] or "?" for x in by[s])
            print(f"  {s:20s} {len(by[s]):2d}  {ds[0]} .. {ds[-1]}")
        print()
        if former:
            byf = {}
            for r in former:
                byf.setdefault(r["student"], []).append(r)
            print("FORMER (students/non-students/ -- record exists, excluded from sweeps)")
            for s in sorted(byf):
                ds = sorted(x["date"] or "?" for x in byf[s])
                print(f"  {s:20s} {len(byf[s]):2d}  {ds[0]} .. {ds[-1]}")
            print()

    print("UNMAPPED (needs a decision — new student folder, alias, or skip)")
    for r in sorted(unmatched, key=lambda x: (x["match"], x["subject"] or "")):
        subj = r["subject"] or "(none)"
        print(f"  {subj:28s} {r['kind']:14s} {r['date'] or '?':10s}  {r['match']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
