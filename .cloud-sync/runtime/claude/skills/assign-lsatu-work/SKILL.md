---
name: assign-lsatu-work
description: 'Use whenever Joshua wants anything done on LSAT U headlessly: no browser, no Lovable. Covers assigning an Activity, guided drill, homework set or timed PT section to one or many students ("assign this to Celia", "give Lydia the Negation Station", "put PT156.S2 on Avneet due Friday", "assign RRC to Celia, Lydia and Dakota"); messaging a student ("tell Celia to start with PT105.S2"); reading progress ("how is Celia doing", "what does Lydia have", "who is overdue", "who has gone quiet", "Celia''s weakest question types"); and accounts and upkeep: signups ("who signed up"), access ("give Venusa access", "turn on drills for X"), archiving, due dates, unassigning, booking passes ("how many sessions does Sandra have left"), notifications and messages ("who messaged me", "show my thread with Celia"). The one place for any LSAT U platform operation.'
---


## Local execution contract (2026-10-10)

Use current project assign-lsatu-work and sibling ai-os-projects/lsatu app instructions. AI OS is a Git repository. Respect actual current user authorization, not a historical person-count approval rule. Preserve dry-run, exact artifact/student identity, duplicate guards and read-after-write; archive/revoke/unsend require explicit deletion scope.

## Workflow

# Assign work on LSAT U

Assign work, message students, and read how they are doing on LSAT U, all
from the command line. No browser, no clicking. For complete interactive
Classroom lessons, use the local `lsat-u-lessons` MCP or its direct Node
fallback documented in the AI OS `lsat-u-platform-actions` skill. Both paths
post through LSAT U's authenticated API and need no Lovable publish.

## Authorization

Joshua pre-authorized this on 2026-09-07: **a single named student is a go.**
Run it, then report. Do not stop to ask permission first.

Confirm before running when:

- assigning to **3 or more students at once** — each one emails a real person
- the student name is **ambiguous** (the script refuses and lists the matches)
- the student is **Thaniuska Vivas** or **Amanda** — no platform account found
- Joshua names someone absent from [[STUDENT-PLATFORM-IDENTITY-MAP]]

This is a deliberate, narrow exception to his global "draft, never send" rule.
That rule still holds for email, posts, and anything outside LSAT U.

## The command

Everything goes through one command: `system/scripts/lsatu` in the vault
(`C:\Users\Joshu\dev\ai-os`). Run it with bash from the vault root.

**Never** `cd projects/lsatu` and run `scripts/assign.ts` directly. That
checkout is on whatever branch another session left it on, sometimes with an
uncommitted `assign.ts` that is missing flags. On 2026-09-23 it had no
`--section`, `--due` or `--set`. The wrapper runs writes from
`projects/.lsatu-ops`, a detached worktree it fast-forwards to `origin/main`
before every run. It refuses to run if that copy has local edits.

**Writes**

```bash
system/scripts/lsatu assign --student "Celia" --activity "Read, Recall, Colour"
system/scripts/lsatu assign --student "Lydia" --drill "main-conclusion-1"
system/scripts/lsatu assign --student "Dakota" --message "Start with PT105.S2 before Thursday."
system/scripts/lsatu assign --student "Avneet" --section PT156.S2 --due 2026-09-26
system/scripts/lsatu assign --student "Avneet" --set "PT156.S2 (LR)"
```

**Many students at once.** The wrapper resolves every name first, and one bad
name stops the batch before anyone is emailed. The 3+ confirmation rule above
still applies.

```bash
system/scripts/lsatu assign-many "Celia, Lydia, Dakota" --drill "main-conclusion-1" --due 2026-09-26
```

**Reads.** These never write, so they are safe any time and need no confirmation:

```bash
system/scripts/lsatu status "Celia"            # open work, overdue flags, last seen, recent sections
system/scripts/lsatu qtypes "Celia" --days 30  # accuracy by question type, weakest first
system/scripts/lsatu sections "Celia"          # recent timed sections with BR scores
system/scripts/lsatu overdue                   # every past-due unfinished item, all students
system/scripts/lsatu quiet --days 7            # students with open work, not seen in N days
system/scripts/lsatu students                  # every account, email, last seen
system/scripts/lsatu inbox --days 7            # messages students sent you, newest first
system/scripts/lsatu thread "Celia"            # the full message thread with one student
```

**Accounts, access, and Classroom upkeep** (`system/scripts/lsatu-admin.mjs`, same
admin login, calls the same `admin-manage-users` / `booking-pass-admin` edge
functions the dashboard calls):

```bash
system/scripts/lsatu signups --days 30                  # who joined, and what access each has (NO ACCESS YET = waiting on you)
system/scripts/lsatu access "Venusa"                    # show every flag, on and off
system/scripts/lsatu access "Venusa" --template standard   # trial | standard | full, exactly the dashboard templates
system/scripts/lsatu access "Venusa" --grant drill,activity --revoke chat
system/scripts/lsatu archive "Name" --reason "finished"   # and: unarchive "Name"
system/scripts/lsatu items "Celia"                      # her open Classroom items WITH ids
system/scripts/lsatu due <item-id> 2026-09-30           # move a due date
system/scripts/lsatu unassign <item-id>                 # hide from her Classroom (archived; her work stays)
system/scripts/lsatu passes ["Celia"]                   # booking passes: used / total / owed
system/scripts/lsatu notifications                      # your unread admin notifications
system/scripts/lsatu read "Celia"                       # mark your thread with her read
```

**Review queues:**

```bash
system/scripts/lsatu drafts [--status draft|approved|posted|all]   # AI TA drafts waiting on you
system/scripts/lsatu draft <id>                          # full text
system/scripts/lsatu draft-set <id> approved|rejected|posted
system/scripts/lsatu draft-send <id>                     # message it to the student, then mark posted
system/scripts/lsatu uploads [--all]                     # student uploads not yet reviewed
system/scripts/lsatu upload-review <id> parsed|needs_review|failed
system/scripts/lsatu notes [--all]                       # session notes waiting on a match
system/scripts/lsatu note-resolve <ledger-id> "Celia"    # file the note under her
system/scripts/lsatu note-discard <ledger-id> [--reason ".."]
system/scripts/lsatu scan-notes                          # scan Drive for new session notes now
system/scripts/lsatu plans "Lydia"                       # her weekly plans and items
```

**Unsend a message:**

```bash
system/scripts/lsatu thread "Adriana" --ids          # message ids
system/scripts/lsatu unsend <message-id> [--dry-run]
system/scripts/lsatu unsend-last "Adriana" [--dry-run]   # your most recent message to her
```

This removes only your own messages, never a student's. It reports whether
she has already opened the thread: if she has not, she never sees the
message. A plain message makes no bell entry and no email, so removing it
removes every trace. An assignment's email cannot be recalled, and unsending
its inbox message does not unassign the work; use `unassign` for that.
Deleting is permanent, so confirm with Joshua every time unless he named the
message in this turn.

**Multi-line text is refused on purpose.** On Windows the npx shim cuts an
argument at the first newline and drops everything after it, `--dry-run`
included. On 2026-09-23 a "dry run" of `draft-send` really sent Adriana Varea
the first line of a draft. The wrapper now refuses any multi-line argument.
Messages must be one line until `assign.ts` reads its text from a file.

Every write here takes `--dry-run`. Flag short names: practice, drill,
classroom, bootcamp, analytics, schedule, waj, journal, flagged, chat, export,
ta, activity. Templates always leave the "paying student" defaults on, the
same as the dashboard does.

**Go without asking:** every read, `access` grants for one named student,
`due`, and `read`. **Confirm first:** `archive`, `unarchive`, `unassign`,
`--all-off`, and any `--revoke`, because each of these takes something away
from a real student. **Not available here on purpose:** deleting a student
(permanent), changing admin roles, and anything that edits app code or the
database schema. Those stay with Joshua in the dashboard or Lovable.

**Other platform jobs that already have a home:** one-off booking links and
new passes go through the `booking-link` skill (`scripts/booking-link.ts`).
Accommodations emails use the `accommodations-email` skill.

Add `--json` to any read when you want to compute on the output. `overdue` and
`quiet` include former students, because the platform has no "former" flag.
Cross-check `students/roster.generated.md` before acting on either list.

When you are unsure what a student already has, run `status` before
assigning. One call catches both double-assigns and the overdue pile.

Flags: `--schedule YYYY-MM-DD` unlocks the work that morning. `--due YYYY-MM-DD`
is due at the end of that local day and shows on the card and the calendar
strip. `--dry-run` resolves the student and the work and writes nothing — use it
when the name is at all uncertain.

**Dates are absolute.** "Due Saturday" means look up the date of the coming
Saturday and pass that. On 2026-09-10 (a Thursday) Saturday was 2026-09-12; a
handoff once carried 09-13, which is the Sunday.

To pace a student over several days, run the command once per day with a
`--schedule` on each. Each run is its own assignment, its own row, and its own
email, so she is told about each day rather than handed a block.

Every assignment lands on the home calendar strip and the cell opens that
assignment — scheduled work on its unlock day, unscheduled work on the day you
assigned it. Nothing needs to be written by hand to put work on the calendar;
if an assignment is missing from the band, that is a bug to fix in
`useClassroomHome`, not something to patch into `classroom_items`.

Always `--dry-run` first for a student you have not assigned to before in this
session. It costs one second and it is the only cheap way to catch a wrong
account.

## Why a script and not a direct DB write

`scripts/assign.ts` calls the app's **own** `assignWork()` from
`src/lib/assignWork.ts`. Assigning touches seven tables — the assignment
snapshot, `classroom_items`, the conversation and its participants, `messages`,
`notifications` — plus the email edge function, and it rolls the whole thing
back if the classroom item or notify throws. There is no RPC and no edge
function for it; it is client-side code.

So never hand-write these rows. A second implementation drifts from the UI the
first time the app changes, and produces assignments subtly unlike the ones
Joshua makes by clicking.

## Credentials

Read from the AI OS root `.env`. The vault is a git repo, but `.env` is git-ignored:

- `LSATPREP_ADMIN_EMAIL`, `LSATPREP_ADMIN_PASSWORD` — already set

Never put a credential in `../ai-os-projects/lsatu/.env`. That file **is tracked in git**
and would be committed. The script signs in as Joshua and works under normal
admin RLS, the same permission path the UI uses.

`SUPABASE_SERVICE_ROLE_KEY` is deliberately **not** used even when present: it
bypasses RLS on every write, so a script running as service_role would hide an
RLS regression instead of hitting it. The script warns and falls back.

## Expected output

```
Assign "Read, Recall, Colour" → Celia <celiacutler@gmail.com>
Assigned. id=e83e2193-…
  inbox ok · bell ok · email ok
```

A notify channel reading `FAILED` is **not** an assignment failure — the work is
in her Classroom and only a message went missing. Report it, do not re-run.

## Failure modes

**`duplicate key … activity_assignments_active_unique`** — she already holds an
active assignment for this Activity. Not a bug; the DB refusing a double-assign.
Check what she has before re-trying (below).

**`"X" is ambiguous`** — the script lists every matching account and stops.
Pick the full name or the email. Never guess: a misdirected assignment is
silent, because she simply never sees it.

**Sign-in failed** — the credentials in the AI OS root `.env` are wrong or the account
gained MFA.

## Checking what a student already has

`system/scripts/lsatu status "Celia"` lists every open classroom item with its
type, status, assign date and due date, and flags anything overdue.

## A PT section as timed homework

`--section PT156.S2` (also accepts `PT156-S2`, `pt 156 s 2`) assigns one
Logical Reasoning section to run under the real 35:00 section clock, with the
official PrepTest header, exactly like a section inside a practice test.

What the script does, verified end to end on 2026-09-10 on
`joshua.fisseha01@gmail.com` (the test account):

1. Reads `public/data/PT156-S2-LR.json` and builds the qids
   `PT156-S2-Q1 … Q25` in order. No file → it lists the sections that PT does
   have and stops. Only LR sections are loaded; there is no RC/LG file set.
2. Finds or creates the homework set titled **`PT156.S2 (LR)`** with exactly
   those qids and `estimated_minutes = 35`. One set per section, reused; a
   same-title set with different questions stops the run.
3. Calls the app's own `assignWork({ kind: 'homework_set' })`: assignment row,
   classroom item (with `due_at`), inbox message, bell, email.
4. Turns on `has_classroom_access` and `has_drill_access` if either was off,
   because the set opens at `/classroom/:id` and runs at `/drill`.

Expected output:

```
Assign "PT156.S2 (LR)" → josh <joshua.fisseha01@gmail.com>  (due 2026-09-13)
  25 questions, timed 35:00 · set reused (ff0fe127-…)
Assigned. id=04e154c8-…
  inbox ok · bell ok · email ok
```

**Already assigned:** the script says
`already has "PT156.S2 (LR)" (in_progress, assigned 2026-09-10)` and stops. A
set can be re-issued only after that copy is `completed`. Do not work around
it by making a second set.

**Why the timer is real:** `src/lib/drillRunSpec.ts` `singleSectionOf()` sees
that every qid is one PT+section and runs it as `full-section` (35-minute
countdown) instead of `type-drill` (a stopwatch). Shipped with `--section` in
PR #113, merged 2026-09-11.

`--set "<title or id>"` assigns any existing homework set, timed or not, with
the same guards.

## Read, Recall, Colour specifically

Assign the title **"Read, Recall, Colour"** — the section-library door. She then
picks any of 12 seeded sections (PT1.S3, PT21.S3, PT101.S2, PT102.S3, PT103.S1,
PT104.S1, PT105.S1, PT105.S2, PT106.S2, PT112.S4, PT134.S3, PT140.S1), 25 min
each. Every attempt is kept; re-running saves a new attempt.

The script prefers the exact title, so it resolves to the door rather than one
of the 12 sections. Pass a `read-recall-colour-pt*-s*` slug only to pin her to
one section deliberately.

## One headless backend, never Lovable for content

Decided by Joshua on 2026-09-23 and refined 2026-09-29. `system/scripts/lsatu`
is the headless path for work assignments, messaging, and student data. The
local `lsat-u-lessons` MCP wraps `system/scripts/lsatu-admin.mjs post-lesson`
for interactive lesson assignment and exact HTML verification. It is a local
wrapper over the same authenticated backend, not a hosted connector or an app
deploy. Lovable is only for changing the app's own code.

## The hosted connector (MCP): exists, not used

LSAT U also runs a real MCP server, `lsat-u-mcp` v0.3.0, at
`https://atrcqxpmqrynmtvvyjju.supabase.co/functions/v1/mcp`. Verified live on
2026-09-23: it returns 401 without a token and serves OAuth discovery. The
source is `src/lib/mcp/` in the app repo, deployed as the `mcp` edge function.

- **Connect:** claude.ai → Settings → Connectors → add a custom connector with
  that URL, then sign in with an LSAT U account. There is no key to paste.
- **Who gets the admin tools:** any account with the `admin` role in
  `user_roles`. To grant someone access, give their account that role; remove
  the role to revoke it. Students who connect see only their own data.
- **Tools today:** `find_students`, `list_students`, `list_homework_sets`,
  `assign_homework`, `assign_passage_map_homework`, `post_classroom_note`,
  `send_note`, `get_assignment_status`, plus the student-side `get_my_profile`,
  `list_my_homework` and `list_my_classroom_items`.
- **In the CLI but not the connector:** activities, guided drills, bootcamps,
  timed `--section` with due dates, and every analytics read. Adding them
  means app code plus a Lovable deploy, which needs Joshua's credit
  confirmation first.

On this laptop, use the CLI: it does more and costs nothing. The connector is
for when Joshua is away from the laptop, or when someone else needs access.

Running `vite-node` inside the app repo rewrites
`supabase/functions/mcp/index.ts` with a local path (the `@lovable.dev/mcp-js`
Vite plugin). Never commit that change. The wrapper restores the file after
each run.

## Related

Vault: `wiki/ASSIGN-AN-ACTIVITY.md` (the browser path and what fires),
`wiki/STUDENT-PLATFORM-IDENTITY-MAP.md` (which account is which student —
33 platform accounts, 20 real students, 13 unmatched).
