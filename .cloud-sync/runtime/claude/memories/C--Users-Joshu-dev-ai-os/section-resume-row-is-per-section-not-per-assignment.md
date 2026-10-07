---
name: section-resume-row-is-per-section-not-per-assignment
description: "Full-section resume rows in bootcamp_kv: homework runs are keyed drill::assignment::<id> since PR #124 (2026-09-11); Testing Centre sits still share drill::section::pt<N>-s<M>; a row with elapsed_ms >= budget opens on the buzzer, never on 00:00."
metadata: 
  node_type: memory
  type: project
  originSessionId: 925cea80-b503-484b-b5fa-2f663e9a4370
  modified: 2026-09-11T17:06:28.273Z
---

Homework assignments of a section get their own resume row,
`drill::assignment::<assignmentId>`, since PR #124 (branch
`fix/drill-resume-stale-clock`, 2026-09-11). A section sat outside an
assignment still uses `drill::section::pt<N>-s<M>`, shared by every such sit
and overwritten by the next one (by design: one row per section, latest run).

The 2026-09-11 test-account row (`pt156-s2`, in_progress, elapsed_ms 2,100,000,
1 attempt, index 0) was explained by three code paths, any of which suffice:
a 4Hz snapshot writer (see [[timer-context-is-new-every-tick]]), a snapshot
whose read predated the completion write landing after it (store now
serialises per row), and a reload during blind review re-mounting a fresh sit
over a finished assignment row (row now sealed at mount). Which one produced
that exact row was not confirmed; there is no service key on this machine.

**How to apply:** a row with `elapsed_ms >= budget` is restored on the Time's
up prompt with its answers kept, never as an open drill at 00:00. Never delete
`bootcamp_kv` rows to "fix" a resume; the row is the only record of an
unsubmitted sitting.
