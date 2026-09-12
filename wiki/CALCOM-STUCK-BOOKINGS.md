---
title: Cal.com stuck bookings
type: runbook
created: 2026-09-08
updated: 2026-09-11
tags: [runbook, calcom, payments, scheduling]
---

# Cal.com stuck bookings

When a student says scheduling or payment "isn't working", first ask **which link**. A
`/book/<name>-<code>` link is LSAT U, not Cal.com; see [[LSATU-BOOKING-POLICY]]. For a
Cal.com link, this is almost always the cause.

## What happens

`session-link` charges Stripe **on booking** ($45 USD). The flow is: pick a slot, fill the form,
press **Pay to book**, land on `cal.com/payment/<uuid>` with Stripe card fields. That page holds
the slot for **30 minutes only**:

> "This slot is held for you for 29:54 — after that, someone else may book it."

Miss that window and three things are true at once:

1. The payment link is dead. The uuid is not stored on the booking and API v2 exposes no
   payments endpoint, so **it cannot be recovered or re-sent**.
2. `cal.com/booking/<uid>` shows "awaiting payment" with only *Add to calendar* and *Cancel*.
   **There is no Pay button** on any unpaid booking. Verified against a control booking.
3. The dead booking **keeps holding the slot**, hiding it from everyone else. Cal.com sends
   no host notification, so it is invisible from this side.

## The check

```
node scripts/calcom-pending-sweep.mjs           # report
node scripts/calcom-pending-sweep.mjs --cancel  # release future slots
```

Run it when a student reports trouble, and periodically — these accumulate and silently eat
availability. Past-dated pending bookings cannot be cancelled by cal.com and block nothing;
leave them.

## The only fix

Cancel the stale booking and have the student **book again**. That issues a fresh 30-minute
link. There is no way to revive the old one. The 30-minute deadline is not settable through the
API — only in the cal.com dashboard under the paid event's settings.

## Config as of 2026-09-08

- Schedule 681247 "Working Hours", **America/Toronto**. Mon 14:00–20:00, Tue/Thu 13:00–19:30,
  Wed 13:00–19:00, Fri 13:00–19:30, Sat 14:00–17:00. Sunday closed.
- Event type 4753558, 70 min, no slot interval, so slots step 70 minutes from each window start
  and fill around existing bookings.
- Booking window widened 2026-09-08 from **6 business days** to **45 calendar days**. The old
  setting meant students saw barely one week ahead and at most one Saturday, which is what made
  weekend booking so hard.
- Date override: **2026-09-19 20:00–21:10 ET** for [[../students/fernande-charleus/fernande-charleus]].

## History

2026-09-08 — Whitney Wilson lost two bookings this way (Sep 10 and Sep 12) within four minutes
of each other and emailed asking to e-transfer instead. Eight older ones found from Lydia (3),
atamaami (2), Bella, Vinay and ocebate, going back to May.
