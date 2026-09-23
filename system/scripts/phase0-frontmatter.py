"""Phase 0 — frontmatter foundations for the curated second-brain notes.

Additive and non-destructive: never overwrites or reorders an existing key.
For each curated note it ensures these keys EXIST (appending only the missing
ones to the note's frontmatter block, or creating a block if there is none):

  type       kept if present; else inferred from folder + filename
  subject    the canonical thing the note is about (title / H1 / filename)
  updated    kept if present; else git last-commit date; else file mtime
  aliases    seeded ([] by default; name variants for people; known synonyms)
  lifecycle  person notes only: active|former, derived from existing `status`
             (lapsed/former -> former, everything else -> active). The nuanced
             `status` line is left untouched — the roster's conflict checks
             read those specific values (prospect/lapsed/active).

Generated files (*.generated.md) are skipped: they are rebuilt from source, so
hand-added frontmatter would be discarded on the next rebuild.

Usage:
  phase0-frontmatter.py --dirs students            # apply to one folder
  phase0-frontmatter.py --dirs students --dry-run  # show planned changes only
  phase0-frontmatter.py --all                      # apply to all curated dirs
  phase0-frontmatter.py --all --dry-run
"""
import argparse
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CURATED = ["students", "corpus", "context", "decisions", "wiki",
           "references", "research", "handoffs", "brainstorms"]

# Folder -> default type when a note carries none. Uses the vocabulary already
# present in the vault; does not invent new type names beyond what a folder
# clearly is.
FOLDER_TYPE = {
    "context": "operating-layer",
    "decisions": "reference",
    "references": "reference",
    "research": "research",
    "handoffs": "handoff",
    "brainstorms": "brainstorm",
    "wiki": "operating-layer",
    "corpus": "teaching-notes",
}

# Filename-stem -> type inside students/. Falls back to folder rules otherwise.
STUDENT_FILE_TYPE = {
    "open-loops": "open-loops",
    "teaching-notes": "teaching-notes",
    "transcripts": "transcript-index",
    "assignment-log": "assignment-log",
}

# Conservative alias seeds for concept notes whose retrieval was known to miss.
CONCEPT_ALIASES = {
    "comparative passages": ["comparative reading", "comp passages", "dual passages"],
}


def git_date(path: Path) -> str | None:
    try:
        out = subprocess.run(
            ["git", "-C", str(ROOT), "log", "-1", "--format=%as", "--", str(path)],
            capture_output=True, text=True, timeout=15)
        d = out.stdout.strip()
        return d or None
    except Exception:
        return None


def mtime_date(path: Path) -> str:
    return datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc).strftime("%Y-%m-%d")


def split_frontmatter(text: str):
    """Return (fm_lines, body, had_fm). fm_lines excludes the --- fences."""
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            fm = text[4:end + 1]
            body = text[end + 4:]
            if body.startswith("\n"):
                body = body[1:]
            return fm.splitlines(), body, True
    return [], text, False


def existing_keys(fm_lines):
    keys = set()
    for ln in fm_lines:
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):", ln)
        if m:
            keys.add(m.group(1))
    return keys


def get_val(fm_lines, key):
    for ln in fm_lines:
        m = re.match(rf"^{re.escape(key)}:\s*(.*)$", ln)
        if m:
            return m.group(1).strip()
    return None


def humanize(stem: str) -> str:
    s = re.sub(r"[-_]+", " ", stem)
    s = re.sub(r"^\d{4}-\d{2}-\d{2}\s*", "", s)  # strip leading date
    return s.strip().title() if s.islower() else s.strip()


# H1s that are export boilerplate, not a real subject.
GENERIC_H1 = {"notes", "summary", "transcript", "meeting notes", "session notes"}


def clean_subject(s: str) -> str:
    s = s.replace("—", "-").replace("–", "-")  # no em/en dashes (voice rule)
    s = re.sub(r"[^\w\s\-&/,.:'()]+", "", s, flags=re.UNICODE)  # drop emoji etc.
    s = re.sub(r"\s+", " ", s)  # collapse the gaps a stripped char leaves
    return s.strip(" -")


def _strip_emoji(s: str) -> str:
    return clean_subject(s)


def first_h1(body: str) -> str | None:
    for ln in body.splitlines():
        m = re.match(r"^#\s+(.*)", ln)
        if m:
            cleaned = _strip_emoji(m.group(1))
            if cleaned and cleaned.lower() not in GENERIC_H1:
                return cleaned
            return None  # first heading is boilerplate; fall back to filename
    return None


DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})")


def transcript_subject(stem: str) -> str:
    """`2025-05-24-rachael-notes-by-gemini` -> `Rachael — 2025-05-24 session`."""
    m = DATE_RE.match(stem)
    date = m.group(1) if m else None
    name = stem
    if date:
        name = stem[len(date):].lstrip("-")
    name = re.sub(r"-notes-by-gemini$", "", name)
    name = re.sub(r"[-_]+", " ", name).strip().title()
    return f"{name} — {date} session" if date else (name or stem)


def infer_type(rel: Path, stem: str) -> str:
    top = rel.parts[0]
    if top == "students":
        if stem in STUDENT_FILE_TYPE:
            return STUDENT_FILE_TYPE[stem]
        if stem.endswith("-notes-by-gemini") or "transcript-downloads" in rel.parts \
                or "_other-sessions" in rel.parts:
            return "transcript"
        # primary person note: <slug>/<slug>.md
        if len(rel.parts) >= 2 and rel.parts[-2] == stem:
            return "person"
        return "notes"
    return FOLDER_TYPE.get(top, "notes")


def is_person(rel: Path, stem: str, typ: str) -> bool:
    return typ == "person"


def derive_lifecycle(status: str | None) -> str:
    s = (status or "").strip().lower()
    return "former" if s in ("former", "lapsed") else "active"


def seed_aliases(subject: str, is_person_note: bool, name: str | None) -> list[str]:
    key = (subject or "").strip().lower()
    if key in CONCEPT_ALIASES:
        return CONCEPT_ALIASES[key]
    if is_person_note and name:
        toks = name.split()
        if len(toks) >= 2:
            return [toks[0]]  # first-name alias
    return []


def fmt_aliases(aliases: list[str]) -> str:
    if not aliases:
        return "aliases: []"
    inner = ", ".join(aliases)
    return f"aliases: [{inner}]"


def process(path: Path, dry: bool):
    rel = path.relative_to(ROOT)
    stem = path.stem
    text = path.read_text(encoding="utf-8", errors="replace")
    fm_lines, body, had_fm = split_frontmatter(text)
    have = existing_keys(fm_lines)

    typ = get_val(fm_lines, "type") or infer_type(rel, stem)
    is_transcript = typ == "transcript"
    if is_transcript:
        subject = get_val(fm_lines, "subject") \
            or get_val(fm_lines, "title") or transcript_subject(stem)
    else:
        subject = get_val(fm_lines, "subject") \
            or get_val(fm_lines, "title") or first_h1(body) or humanize(stem)
    # strip surrounding quotes from a title-derived subject, normalize dashes
    subject = clean_subject(subject.strip().strip('"').strip("'"))
    # For a dated transcript, the session date is a more meaningful `updated`
    # than the bulk-import commit date.
    fname_date = DATE_RE.match(stem)
    if is_transcript and fname_date:
        updated = get_val(fm_lines, "updated") or fname_date.group(1)
    else:
        updated = get_val(fm_lines, "updated") or git_date(path) or mtime_date(path)
    person = is_person(rel, stem, typ)
    name = get_val(fm_lines, "title") if person else None

    additions = []
    if "type" not in have:
        additions.append(f"type: {typ}")
    if "subject" not in have:
        additions.append(f"subject: {subject}")
    if "updated" not in have:
        additions.append(f"updated: {updated}")
    if "aliases" not in have:
        additions.append(fmt_aliases(seed_aliases(subject, person, name)))
    if person and "lifecycle" not in have:
        additions.append(f"lifecycle: {derive_lifecycle(get_val(fm_lines, 'status'))}")

    if not additions:
        return None  # nothing to do

    if had_fm:
        new_fm = fm_lines + additions
        new_text = "---\n" + "\n".join(new_fm) + "\n---\n" + body
    else:
        new_text = "---\n" + "\n".join(additions) + "\n---\n\n" + text

    if not dry:
        path.write_text(new_text, encoding="utf-8")
    return additions


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dirs", nargs="*", default=None)
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--show", type=int, default=8, help="how many changed files to print")
    args = ap.parse_args()

    dirs = CURATED if args.all else (args.dirs or [])
    if not dirs:
        print("specify --dirs <folder...> or --all")
        return 2

    changed = skipped_gen = untouched = 0
    samples = []
    for d in dirs:
        base = ROOT / d
        for path in sorted(base.rglob("*.md")):
            if path.name.endswith(".generated.md"):
                skipped_gen += 1
                continue
            adds = process(path, args.dry_run)
            if adds is None:
                untouched += 1
            else:
                changed += 1
                if len(samples) < args.show:
                    samples.append((path.relative_to(ROOT), adds))

    verb = "would change" if args.dry_run else "changed"
    print(f"\n{verb}: {changed}   already-complete: {untouched}   "
          f"skipped .generated.md: {skipped_gen}\n")
    for rel, adds in samples:
        print(f"  {rel}")
        for a in adds:
            print(f"      + {a}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
