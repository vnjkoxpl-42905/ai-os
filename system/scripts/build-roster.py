#!/usr/bin/env python3
"""Generate students/roster.generated.md — the canonical student list.

It exists because there was no canonical roster: "email everyone on my list"
had to be answered by scraping the live admin Passes page, which has no email
column, forcing a cross-tab match by hand.

Everything here is derived from files already in the brain:
  - folder slug + frontmatter (name, email, status) from students/<slug>/<slug>.md
  - session count and last-session date from the Gemini transcript inventory

Booking state is read LIVE from the backend (booking_passes via the admin JWT --
see lsatu_api.py), because the backend is the authority for it and a local copy
goes stale silently. Scanning local files for a /book/ slug, which this script
used to do, was actively wrong: it reported a link for a pass that had since
been revoked, and could not see passes that were never written down.

Still NOT known here, and left "?" rather than guessed:
  - last contact          -> Gmail owns this

If the backend is unreachable the roster still builds, marked clearly as
local-only, rather than failing or silently emitting stale booking state.

Usage:
    python3 system/scripts/build-roster.py            # write the file
    python3 system/scripts/build-roster.py --check    # print, write nothing
    python3 system/scripts/build-roster.py --offline  # skip the backend
"""
import os
import re
import subprocess
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_roster_shared import (  # noqa: E402
    frontmatter, slugify as slug, build_indexes, usable_passes,
)

try:
    from lsatu_api import client, BackendUnavailable
except ImportError:  # helper missing; behave as if offline
    client = None

    class BackendUnavailable(Exception):
        pass

BRAIN = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STUDENTS = f"{BRAIN}/students"
OUT = f"{STUDENTS}/roster.generated.md"
INVENTORY = f"{BRAIN}/system/scripts/transcript-inventory.py"




# How long an "active" student can go untaught before the record is questioned.
# Deliberately conservative: an active student with nothing owed is the NORMAL
# pay-per-session case, so only real silence is worth flagging. Tune here.
QUIET_DAYS = 60


def quiet_days(last):
    """Days since a student was last taught. 0 when unknown, so unknown never flags."""
    import datetime
    try:
        d = datetime.date.fromisoformat(last)
    except (ValueError, TypeError):
        return 0
    return (datetime.date.today() - d).days




def live_passes():
    """-> (by_email, by_name, usable, error).

    Booking passes straight from the backend. Only `active` and `exhausted`
    passes count; `revoked` ones are dropped, because a revoked slug is a dead
    link and reporting it as a booking link is exactly the bug this replaced.

    Matching to a folder is by email first, then by name, because the two
    disagree in practice (Ethan is ethantrie@gmail.com in the backend and
    trie@usc.edu in his folder).
    """
    if client is None:
        return {}, {}, [], "lsatu_api helper unavailable"
    try:
        rows = client().get(
            "booking_passes",
            select="booking_slug,student_email,student_name,status,total_credits,used_credits",
        )
    except BackendUnavailable as e:
        return {}, {}, [], str(e)

    # Matching lives in build_roster_shared so this and build-live-status.py
    # cannot drift. A student matching in one view but not the other is exactly
    # the bug class this work has been clearing.
    by_email, by_name = build_indexes(rows)
    return by_email, by_name, usable_passes(rows), None


def sessions():
    """-> {slug: (count, last_date)} from the transcript inventory."""
    try:
        import json
        raw = subprocess.run([sys.executable, INVENTORY, "--json"],
                             capture_output=True, text=True, timeout=120, check=True).stdout
        rows = json.loads(raw)
    except Exception as e:
        print(f"warning: transcript inventory unavailable ({e}); session columns will be '?'",
              file=sys.stderr)
        return {}
    agg = {}
    for r in rows:
        s = r.get("student")
        if not s:
            continue
        c, last = agg.get(s, (0, ""))
        d = r.get("date") or ""
        agg[s] = (c + 1, max(last, d))
    return agg


def main():
    args = sys.argv[1:]
    check = "--check" in args
    sess = sessions()

    if "--offline" in args:
        by_email, by_name, usable, err = {}, {}, [], "skipped (--offline)"
    else:
        by_email, by_name, usable, err = live_passes()
    if err:
        print(f"warning: booking state unavailable ({err}); roster will be local-only",
              file=sys.stderr)

    rows = []
    claimed = set()
    for slug_ in sorted(os.listdir(STUDENTS)):
        d = os.path.join(STUDENTS, slug_)
        if not os.path.isdir(d) or slug_.startswith("_") or slug_ == "non-students":
            continue
        fm = frontmatter(os.path.join(d, f"{slug_}.md"))
        count, last = sess.get(slug_, (0, ""))
        email = fm.get("email") or ""
        name = fm.get("title") or slug_.replace("-", " ").title()

        p = by_email.get(email.strip().lower()) if email else None
        if not p:
            p = by_name.get(slug_) or by_name.get(slug(name))
        if p:
            claimed.add(id(p))

        rows.append(dict(
            slug=slug_,
            name=name,
            email=email or "?",
            status=fm.get("status") or "?",
            sessions=count,
            last=last or "?",
            book=(p or {}).get("booking_slug") or "",
            pass_status=(p or {}).get("status") or "",
            credits=("{}/{}".format((p or {}).get("used_credits"), (p or {}).get("total_credits"))
                     if p else ""),
            backend_email=((p or {}).get("student_email") or ""),
        ))

    orphans = [p for p in usable if id(p) not in claimed]

    lines = [
        "---",
        "title: Student roster",
        "type: operating-layer",
        "tags: [students, operating-layer, generated]",
        "generated: true",
        "status: active",
        "---",
        "",
        "# Student roster",
        "",
        "**Generated file — do not hand-edit.** Rebuild with:",
        "",
        "```",
        "python3 system/scripts/build-roster.py",
        "```",
        "",
        "Name, email, and status come from the student's own `<slug>.md`",
        "frontmatter (primary, authored). Sessions and last-session come from the",
        "Gemini transcript inventory. To correct a name or email, edit the student's",
        "page and regenerate; editing this file does nothing.",
        "",
        "**Booking columns are read live** from the backend's `booking_passes` on each",
        "rebuild, so they are as fresh as the last run and never a stale local copy.",
        "Revoked passes are not shown: a revoked slug is a dead link.",
        "",
        "Last-contact is deliberately absent. Gmail owns it.",
        "",
        (f"{len(rows)} student folders. Booking state: **LOCAL-ONLY, backend unavailable**"
         f" ({err})." if err else f"{len(rows)} student folders. Booking state read live."),
        "",
        "| Student | Email | Status | Sessions | Last session | Booking link | Pass | Credits |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for r in rows:
        book = f"/book/{r['book']}" if r["book"] else ("?" if err else "**none**")
        lines.append(f"| [[{r['slug']}/{r['slug']}\\|{r['name']}]] | {r['email']} | "
                     f"{r['status']} | {r['sessions'] or '-'} | {r['last']} | "
                     f"{book} | {r['pass_status'] or '-'} | {r['credits'] or '-'} |")

    if not err:
        exhausted = [r for r in rows if r["pass_status"] == "exhausted"]
        if exhausted:
            lines += ["", "## Booking pass exhausted", "",
                      "Has a live link, but no credits left. The page tells them"
                      " \"you've used all your sessions\".", ""]
            lines += [f"- [[{r['slug']}/{r['slug']}\\|{r['name']}]] ({r['credits']} used)"
                      for r in exhausted]

        nolink = [r for r in rows if not r["book"]]
        if nolink:
            lines += ["", "## No booking pass (normal)", "",
                      "**Not a gap.** No pass means no sessions are owed. These students"
                      " schedule individual sessions through their Cal.com link; a pass"
                      " exists only when a package has been bought and sessions remain."
                      " Listed so it is clear there is no link to send them, not as a"
                      " to-do.", ""]
            lines += [f"- [[{r['slug']}/{r['slug']}\\|{r['name']}]]" for r in nolink]

        # Status is authored (a judgment), so it is never overwritten here --
        # but evidence that contradicts it gets surfaced. Yahunatan sat as
        # `prospect` while holding 9 owed sessions and nothing caught it.
        conflicts = []
        for r in rows:
            st = (r["status"] or "").lower()
            owed = 0
            if r["credits"]:
                try:
                    u, t = (int(x) for x in r["credits"].split("/"))
                    owed = max(0, t - u)
                except ValueError:
                    owed = 0
            if st == "prospect" and (owed or r["sessions"]):
                why = []
                if owed:
                    why.append(f"{owed} owed session{'s' if owed != 1 else ''}")
                if r["sessions"]:
                    why.append(f"{r['sessions']} taught")
                conflicts.append((r, "recorded as prospect but has " + " and ".join(why)))
            elif st == "lapsed" and owed:
                conflicts.append((r, f"recorded as lapsed but is owed {owed} sessions"))
            elif st == "active" and not owed and quiet_days(r["last"]) > QUIET_DAYS:
                conflicts.append((r, f"recorded as active but owed nothing and not taught"
                                     f" since {r['last']} ({quiet_days(r['last'])} days)"))
        if conflicts:
            lines += ["", "## Status disagrees with the evidence", "",
                      "Status is your judgment and is never auto-corrected. These are"
                      " flagged because the record and the evidence point different ways.",
                      ""]
            lines += [f"- [[{r['slug']}/{r['slug']}\\|{r['name']}]]: {why}"
                      for r, why in conflicts]

        mism = [r for r in rows
                if r["backend_email"] and r["email"] != "?"
                and r["backend_email"].strip().lower() != r["email"].strip().lower()]
        if mism:
            lines += ["", "## Email disagrees with the backend", "",
                      "The folder and the booking pass hold different addresses. Confirm"
                      " which is current before sending anything.", ""]
            lines += [f"- [[{r['slug']}/{r['slug']}\\|{r['name']}]]: folder `{r['email']}`"
                      f" vs backend `{r['backend_email']}`" for r in mism]

        if orphans:
            lines += ["", "## Passes with no student folder", "",
                      "Usable booking passes that match nobody in `students/`. Either a"
                      " missing folder or a leftover test row.", ""]
            lines += [f"- `{p.get('booking_slug')}` — {p.get('student_name')}"
                      f" ({p.get('student_email') or 'no email'}), {p.get('status')}"
                      for p in orphans]

    missing = [r for r in rows if r["email"] == "?"]
    if missing:
        lines += ["", "## Missing an email", "",
                  "Cannot be contacted from the brain until the address is added to the"
                  " student's frontmatter.", ""]
        lines += [f"- [[{r['slug']}/{r['slug']}\\|{r['name']}]]" for r in missing]

    lines += ["", "## Known gaps", "",
              "Transcripts exist for people with no student folder. See the"
              " `## Unresolved` section of [[_aliases]] and run"
              " `python3 system/scripts/transcript-inventory.py --unmatched`.", ""]

    text = "\n".join(lines)
    if check:
        print(text)
        return 0
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {OUT} ({len(rows)} students, {len(missing)} missing email)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
