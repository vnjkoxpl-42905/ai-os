---
name: lsatu-content-lives-in-postgres
description: LSAT U Activity copy lives in Postgres, not the repo — a git push never changes what a student reads; use npm run content:push.
metadata:
  type: project
---

Student-facing Activity copy is a jsonb column, `activities.instructions`, plus a
per-student snapshot in `activity_assignments.instructions` taken at assign time.
The repo file `read-recall-colour-section.instructions.json` is read only by
ActivityLab, SectionLibraryPanel and tests. **Pushing code to main never changes
what a student sees.**

**Why:** for months, copy was edited in Lovable straight into Postgres while the
repo file stood still, so the two drifted badly in both directions. Discovered
2026-09-07 when a push to main appeared to do nothing.

**How to apply:** from `projects/lsatu`, edit the JSON, then `npm run
content:push` and it is live in seconds. `npm run content:diff` shows the diff
without writing; `npm run content:pull` takes the database copy back into the
file. Commit the file afterwards so git holds the record. Migrations are no
longer needed for wording.

Two traps found the hard way. The library door row carries an *older* briefing
than the twelve section rows, so pull follows the majority, never the door.
And completed assignments are deliberately never rewritten: a graded run keeps
the words it was graded under.

`guard_activity_assignment_immutables` returns early for admins, so these writes
need no DDL. A migration must disable that trigger only because it runs with no
`auth.uid()`.

See also [[assigning-activities-is-pre-authorized]].
