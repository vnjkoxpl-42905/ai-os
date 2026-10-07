---
name: accommodations-email-is-auto-send
description: "Accommodations email/scale to X" means run the accommodations-email skill and send right away; the wording is fixed and the script logs itself.
metadata:
  type: feedback
---

The "Request for Accommodations" email is a pre-approved template. If Joshua names students with accommodations in any wording, run the `accommodations-email` skill and send without re-confirming. Superwhisper often transcribes "skill" as "scale", so "the accommodations scale" means this skill. Only the first name and, if he gives one, the accommodations list change. The experimental-section item always carries `(Has to be written under "Other")`.

**Why:** Joshua approved it on 2026-09-23 as a reusable send for future students. He asked for it to be universal and easy to trigger. He turned down a restructured six-step rewrite and kept his own wording, including the doubled "Thanks".

**How to apply:** don't redraft or tidy the email. Look up each address (roster first, then Gmail headers), then run `scripts/send.py`: a dry run, then the real send, one student per email. The script writes the send-ledger and open-loops rows itself. Ask only when an address is missing or two addresses conflict. It works like [[pre-consult-check-in-is-auto-send]].
