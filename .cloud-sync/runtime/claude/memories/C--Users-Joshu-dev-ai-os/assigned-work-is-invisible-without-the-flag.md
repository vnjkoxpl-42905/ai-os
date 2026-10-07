---
name: assigned-work-is-invisible-without-the-flag
description: "On LSAT U a student missing a feature flag sees assigned work as absent, not locked, so check reachability whenever work is assigned."
metadata: 
  node_type: memory
  type: project
  originSessionId: 763f2bd6-f34e-4336-b164-2d9ce5e6c18f
  modified: 2026-09-08T18:36:01.704Z
---

Assigning work on LSAT U does not mean the student can reach it. Every route
sits behind a `ProtectedRoute` feature flag, and Classroom's own feed filters
rows on the same flag, so a missing flag is not a locked door: the work is
simply not on their page, and the direct link answers "Not open yet."

The failure is silent on both sides. Joshua sees a successful assign; the
student sees an empty portal. Ivory Johnson lost a day to it on 2026-09-08 with
three RRC sections and `has_activity_access` off, and the only detector was his
own email with a screenshot.

**Why:** flags are granted by hand in subsets (his had classroom, drill, chat
and schedule but not activity), and the paid-grant set is only applied on
payment, so a hand-built account can be missing exactly one.

**How to apply:** when work is assigned by any path, confirm the student can
open it in the same breath. `scripts/assign.ts` now grants the needed flag at
the write; `scripts/access-audit.ts` sweeps for everything that arrives another
way (admin UI, Lovable-side writes, hand-run SQL). Run the audit before telling
a student their work is there. More generally, when a surface is gated AND its
feed filters on the same flag, a write into it needs a reachability guarantee,
not a hope.

Related: [[assigning-activities-is-pre-authorized]], [[lsatu-content-lives-in-postgres]]
