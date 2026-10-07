---
name: student-work-must-be-preserved
description: Completed student work on LSAT U is never to be lost, modified, or broken by a change; preserving it outranks the change.
metadata:
  type: feedback
---

Work a student has already completed on LSAT U must not be lost, altered, or
rendered unreadable by anything I ship. Attempts, sessions, flags, wrong answers,
assignments, in-progress and finished practice-test sittings, RRC submissions,
scores and history are the student's record of their own effort. Preserving them
outranks whatever change is being made.

**Why:** the record is the product. A student pays for coaching and the platform
is where that work lives between sessions; PRODUCT.md's first principle is that
every number traces to real stored data. Silently dropping or rewriting a
completed sitting destroys evidence of hours of a real person's work and cannot
be regenerated. Joshua stated this directly on 2026-09-09 after a push incident,
as a rule rather than a preference.

**How to apply:**
- Changing a persisted shape (a localStorage run, a Supabase row, a stored
  config) means adding an OPTIONAL field with a fallback for records written
  before it existed. Never make an existing record unreadable. Example: adding
  `sectionSeconds` to `PracticeTestRun` on 2026-09-09 kept it optional and read
  it through `practiceTestRunSectionSeconds`, which falls back to the old
  absolute reading for runs stored earlier.
- A value already resolved for an in-flight sitting is frozen. Do not let a
  later settings change move the clock, the score basis, or the question set
  under work already underway.
- Destructive controls get a confirm, not a single click, and deletion is the
  student's choice rather than a side effect.
- Never run a migration, cleanup, backfill, or reset against student tables to
  make a change easier. Ask first, every time.
- When a refactor touches stored data, say plainly in the report what happens to
  records written before it.

Related: [[lsatu-content-lives-in-postgres]], [[ai-os-safety-rules]],
[[push-only-your-own-commits]].
