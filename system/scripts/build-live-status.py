#!/usr/bin/env python3
"""Regenerate students/<slug>/live-status.generated.md from the live backend.

These mirrors used to be written by hand. They drifted immediately: Lexi's said
"Remaining sessions: 5 of 5, verified 2026-07-19" while the backend already had
used_credits=1. A hand-typed count is the failure mode the no-running-totals
rule in students/README.md exists to prevent.

The split this enforces (see CONTEXT.md):
  arrangement  -> what they bought. Authored in <slug>.md. Permanent. Not here.
  live status  -> what remains right now. Mirrored here. Never hand-edited.

Only writes files matching `*.generated.md`, per the primary/mirror convention:
a file without that marker is primary and precious.

Usage:
    python3 system/scripts/build-live-status.py           # write
    python3 system/scripts/build-live-status.py --check   # report, write nothing
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_roster_shared import student_dirs, frontmatter, match_pass  # noqa: E402

BRAIN = "/Users/joshuaf/ai-os"
STUDENTS = f"{BRAIN}/students"


def render(name, p, stamp):
    """Render one mirror. `p` is the matched booking pass, or None."""
    lines = [
        "---",
        f"title: {name} Live Status",
        "type: generated-mirror",
        "generated: true",
        "source_of_truth: live systems",
        f"status: {'active-booking-pass' if p and p.get('status') == 'active' else 'no-active-pass'}",
        "---",
        "",
        f"# {name} Live Status",
        "",
        "**Generated file, do not hand-edit.** Rebuild with"
        " `python3 system/scripts/build-live-status.py`.",
        "",
        "Calendar, Gmail, and payment state remain authoritative for their own domains;"
        " this mirrors the LSAT U booking backend only.",
        "",
        "## Booking pass",
        "",
    ]
    if not p:
        lines += [
            "No booking pass. **This is normal, not a gap**: it means no sessions are",
            "owed. Sessions are scheduled individually through their Cal.com link.",
            "A pass exists only when a package has been bought and sessions remain.",
        ]
    else:
        total = p.get("total_credits")
        used = p.get("used_credits")
        remaining = (total - used) if isinstance(total, int) and isinstance(used, int) else "?"
        lines += [
            f"- URL: https://lsatprep.study/book/{p.get('booking_slug')}",
            f"- Status: {p.get('status')}",
            f"- Session length: {p.get('session_length_minutes') or '?'} minutes",
            f"- Remaining sessions: {remaining} of {total}",
            f"- Expiry: {p.get('expires_at') or 'none'}",
        ]
        if p.get("status") == "exhausted" or remaining == 0:
            lines += ["",
                      "**No owed sessions left.** The page tells them they have used all",
                      "their sessions, so do not send this link until credits are added."]
        if p.get("status") == "revoked":
            lines += ["", "**Revoked. This link is dead and must not be sent.**"]
    lines += ["", f"Source: LSAT U `booking_passes`, read {stamp}.", ""]
    return "\n".join(lines)


def main():
    check = "--check" in sys.argv[1:]
    try:
        from lsatu_api import client, BackendUnavailable
        c = client()
        passes = c.get("booking_passes",
                       select="booking_slug,student_email,student_name,status,"
                              "total_credits,used_credits,session_length_minutes,expires_at")
    except Exception as e:
        print(f"backend unavailable ({e}); refusing to rewrite mirrors from stale data",
              file=sys.stderr)
        return 1

    import datetime
    stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    written = skipped = 0
    for slug, path in student_dirs(STUDENTS).items():
        fm = frontmatter(os.path.join(path, f"{slug}.md"))
        name = fm.get("title") or slug.replace("-", " ").title()
        p = match_pass(slug, name, fm.get("email", ""), passes)
        out = os.path.join(path, "live-status.generated.md")
        text = render(name, p, stamp)
        if check:
            state = (p or {}).get("status", "no pass")
            print(f"  {slug:18s} {state}")
            skipped += 1
            continue
        with open(out, "w", encoding="utf-8") as f:
            f.write(text)
        written += 1
    if check:
        print(f"{skipped} students inspected, nothing written")
    else:
        print(f"wrote {written} live-status mirrors")
    return 0


if __name__ == "__main__":
    sys.exit(main())
