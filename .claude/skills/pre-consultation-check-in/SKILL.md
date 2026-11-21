---
name: pre-consultation-check-in
description: >-
  Schedule and send Joshua's "Consultation check-in" email 30 minutes before each
  upcoming Cal.com consultation, from his Google Calendar, with a run log so nothing
  is sent twice. Use this whenever Joshua mentions pre-consult emails, consultation
  check-ins or reminders, "who has a consultation coming up", "schedule the check-ins
  for the next N days", "did X get their check-in", "cancel the check-in for X", or
  asks what consultations are on the calendar this week. Also use it when he asks to
  look at the calendar for consultations even if he does not say "email": this skill
  is how consultations are found and how their coverage is reported. Not for paid
  tutoring sessions ("Sofia session"), not for post-consultation follow-ups (that is
  consultation-followup-drafts), not for booking links.
---

# Pre-consultation check-in

Thirty minutes before a consultation, the prospect gets a short email from Joshua:
"Just checking in before our consultation today…". It has gone out 201 times with
that exact wording. This skill finds the consultations, registers one Windows
scheduled task per consultation at T-30, and that task (a plain Python script, no
LLM) re-verifies the booking and sends. Joshua granted standing permission on
2026-09-11 for this email to go out without a per-send approval, so the skill's job
is to be exact and to leave a clear record, not to ask.

Everything runs through one script:

```
python "C:\Users\Joshu\dev\ai-os\.agents\skills\pre-consultation-check-in\scripts\checkin.py" <command>
```

| Command | What it does |
|---|---|
| `find --days 5` | List consultations in the window and whether each is already covered |
| `schedule --days 5` | Register the T-30 task for every uncovered one (sends immediately if T-30 already passed) |
| `status` | Every row in the log with its Task Scheduler state |
| `cancel --event-id <id> --reason "..."` | Remove a scheduled send and mark it so it is never re-created |
| `send --event-id <id> [--dry-run]` | What the task runs. Use `--dry-run` to see the exact email for one event |

Add `--json` to `find`, `schedule`, `status` when you want to read the result
programmatically. Use `--dry-run` on `schedule` when Joshua asks what *would* happen.

## What counts as a consultation

Title matches `^Consultation\s+between\s+Joshua\s+and\s+(.+)$`. That is the whole
rule. Verified 2026-09-11 against 241 calendar events: 70 of 70 consultations match,
0 of 171 other events match. `<Name> session`, `LSAT Session between…`,
`Complimentary session between…`, `Reduced Rate between…` are all something else,
even though most of them also came through Cal.com. The script applies the rule; you
never re-derive it. Read `references/identification.md` before proposing any change
to it, because the two "extra" signals in the old version of this skill (Cal.com link
in the description, `@Cal.com` UID) each produce false positives on real data.

A title match with a non-Cal.com UID is **flagged**, not scheduled. It has never
happened on a real booking. If Joshua made a consultation by hand and wants it
covered, run `schedule --include-flagged`.

## Workflow

1. **Work out the window.** Default is 5 days from now. Map his phrasing:
   "today" → `--until <today YYYY-MM-DD>`; "tomorrow" → `--until <tomorrow>`;
   "next three days" → `--days 3`; "this week" / "through Friday" → `--until <that
   date>`. Dates are America/Toronto; the script handles the conversion.
2. **Run `find`.** Show him the list as-is: start time, name, email, coverage
   (`new`, `covered (scheduled)`, `covered (sent)`, `moved`, `opted out`), and
   timing (`fires 2026-09-14 13:30`, `send now`, `past`). If he only asked who is
   coming up or who is already covered, stop here.
3. **Run `schedule`** with the same window. Do not ask for confirmation first; the
   permission is standing. The one exception: flagged events. Tell him about those
   and only add `--include-flagged` if he says so.
4. **Report** the actions line by line (scheduled / sent now / skipped, with the
   fire time and address) and point at `wiki/PRE-CONSULT-LOG.md`. If anything says
   `failed`, quote the `why` and read `logs/checkin.log`.

`schedule` is safe to run repeatedly. It reads the log first and skips anything
already `scheduled` or `sent` for the same booking (`iCalUID`) at the same start
time. Running it every morning for the next 5 days is the intended pattern.

## What happens at T-30

The task runs `send --event-id <id>` under Joshua's login (so `gws` can reach the
keyring). Before sending it re-fetches the event, because a booking can change
between scheduling and firing:

- Booking cancelled or gone → logs `cancelled`, sends nothing, deletes its task.
- Start time moved to later → registers a new task at the new T-30, logs `moved`.
- Start time moved to within 30 minutes → sends now.
- Consultation already started → logs `missed`, sends nothing. A check-in that
  arrives after the meeting began is worse than none.
- Already `sent` in the log → refuses to double-send.
- Otherwise sends via `gws gmail +send` as a **new email** (never a reply; see
  `references/email.md` for why), logs `sent` (or `sent-late` if the laptop was
  asleep and the task caught up), appends to `wiki/send-ledger.md`, and deletes
  its own task.

The task is set to wake the laptop, to run as soon as possible if it missed its
time, and to expire at the consultation start. It is a one-shot; this skill never
creates a recurring task.

## Reading and changing state

- `wiki/PRE-CONSULT-LOG.md`: one row per booking, rewritten by the script. Status
  meanings are at the top of that file. This is the answer to "who did we already
  do".
- `wiki/send-ledger.md`: append-only; one `scheduled` row when a task is created,
  one `sent` / `failed` row when it fires.
- `logs/checkin.log` (in this skill folder): every run, including crashes inside
  the scheduled task, which has no console.
- `status` joins the log with Task Scheduler: `task:Ready` means it will fire,
  `task:absent` on a `scheduled` row means the task is gone and needs
  re-scheduling (run `schedule` again).
- To stop one: `cancel --event-id <id> --reason "..."`. The row becomes
  `cancelled-by-joshua` and future `schedule` runs leave it alone unless `--force`.

## The email

Fixed text, first name substituted. Subject `Consultation check-in`. The full
message, its provenance, and the reasons it is a new thread rather than a reply
are in `references/email.md`. Do not compose a variant by hand and do not send
it through any other path; if Joshua wants different wording, change `SUBJECT`
and `BODY` in `scripts/checkin.py` and the reference together.

## Machine facts

- Windows only, this laptop. Python: the Python312 install (the script re-invokes
  itself with `pythonw.exe` from the same folder). `gws` is called through
  `C:\Users\Joshu\dev\tools\node\node.exe` directly, so PATH and cmd.exe quoting
  never matter inside a scheduled task. `tzdata` is installed for `zoneinfo`.
- On the MacBook `find` works (falls back to `gws` on PATH) but `schedule` needs
  a launchd equivalent that does not exist yet. Say so rather than improvising.
- `gws` auth expired or laptop off through the whole T-30 → start window: the row
  ends up `failed` or `missed`. Tell Joshua which prospects that hit; he can send
  by hand.
- Test evidence: on 2026-09-11 a test booking to `contact+preconsult-test@` was
  scheduled, fired from Task Scheduler, verified, sent, and logged end to end.
