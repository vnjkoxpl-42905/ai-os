"""Shared student/booking-pass logic for the roster and live-status generators.

One matcher, used by both. Two copies would drift, and a student silently
matching in one view but not the other is exactly the class of bug this whole
line of work has been cleaning up.

See CONTEXT.md for the vocabulary: a booking pass is the only record of owed
sessions, and its student_email is never authoritative for contact.
"""
import os
import re
import unicodedata


def slugify(s):
    """'C. Alexander' -> 'c-alexander'."""
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def frontmatter(path):
    """Flat scalar YAML frontmatter, which is all these files use."""
    if not os.path.isfile(path):
        return {}
    out = {}
    with open(path, encoding="utf-8", errors="replace") as f:
        if f.readline().strip() != "---":
            return {}
        for line in f:
            if line.strip() == "---":
                break
            m = re.match(r"^([a-zA-Z_][\w-]*):\s*(.*)$", line)
            if m:
                out[m.group(1).strip()] = m.group(2).strip().strip('"').strip("'")
    return out


def student_dirs(students_root):
    """-> {slug: path} for real student folders (underscore-prefixed are not students)."""
    out = {}
    if not os.path.isdir(students_root):
        return out
    for n in sorted(os.listdir(students_root)):
        p = os.path.join(students_root, n)
        if os.path.isdir(p) and not n.startswith("_"):
            out[n] = p
    return out


def usable_passes(rows):
    """Passes that can actually be booked against: active or exhausted, with a slug.

    Revoked passes are excluded everywhere. A revoked slug is a dead link, and
    reporting one as a student's booking link is a real bug that shipped once.
    """
    return [r for r in rows
            if r.get("status") in ("active", "exhausted") and r.get("booking_slug")]


def build_indexes(rows):
    """-> (by_email, by_name) over usable passes."""
    by_email, by_name, first_hits = {}, {}, {}
    for r in usable_passes(rows):
        if r.get("student_email"):
            by_email[r["student_email"].strip().lower()] = r
        n = slugify(r.get("student_name"))
        if n:
            by_name[n] = r
            first_hits.setdefault(n.split("-")[0], []).append(r)
    # First-name fallback only when exactly one pass claims that first name, so
    # two students sharing one never cross-match. The folder title is often
    # shorter than the backend's ("Ethan" vs "Ethan Trie").
    for first, hits in first_hits.items():
        if len(hits) == 1 and first not in by_name:
            by_name[first] = hits[0]
    return by_email, by_name


def match_pass(slug, name, email, rows):
    """Find this student's booking pass, or None. Email first, then name."""
    by_email, by_name = build_indexes(rows)
    if email:
        p = by_email.get(email.strip().lower())
        if p:
            return p
    return by_name.get(slug) or by_name.get(slugify(name))
