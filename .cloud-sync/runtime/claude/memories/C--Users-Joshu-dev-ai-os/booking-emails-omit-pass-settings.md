---
name: booking-emails-omit-pass-settings
description: "Booking-link emails say the credit count and the link, nothing about session length or expiry."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 408b39cb-98e7-46e4-bc0b-29988419dc94
  modified: 2026-09-08T22:58:04.742Z
---

In a student booking email, give the name, how many sessions they have, and the
link. Do not mention session length (70 min), expiry, or any other booking-pass
field.

**Why:** those are admin settings. The student sees session length on the booking
page when she picks a time, so in the email it is detail she did not ask for and
has to read past to reach the link. Joshua cut it from the Sandra draft on
2026-09-08.

**How to apply:** shape is "You're set up on LSAT U with N sessions." + the link +
one line that the same calendar is under Schedule in-app + "let me know if a time
you need isn't showing." Full entry in `wiki/COPY-CORRECTIONS.md`.

Related: [[lsatu-copy-corrections-log]] · [[no-em-dashes-no-filler-in-joshuas-writing]]
