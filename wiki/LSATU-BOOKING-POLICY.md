---
title: LSAT U booking policy
type: runbook
created: 2026-09-11
updated: 2026-09-11
tags: [runbook, lsatu, booking, calcom, scheduling]
---

# LSAT U booking policy

Every LSAT U booking page (pass link `/book/<slug>`, in-app `/schedule`, single session
`/book/session`, consultation `/book/consultation`) offers slots from **one generator** and the
database accepts them with **one predicate**, both reading the same numbers. Mirrors the Cal.com
`session-link` event as of 2026-09-10.

## The numbers (booking_availability_config, row 1)

| Setting | Value | Cal.com session-link |
|---|---|---|
| Buffer between any two events | **10 min**, counted once | 0 (not yet changed) |
| Minimum notice | 24 h | 24 h |
| Booking window | 45 calendar days, rolling | 45 calendar days, rolling |
| Slot pitch | length + buffer = **80 min** from each range start | 70 min |
| Hours | `booking_availability` (Working Hours, America/Toronto) | schedule 681247 |
| Date overrides | `booking_availability_overrides` (2026-09-19 20:00–21:10 seeded) | same |

The consultation keeps its own Cal.com shape (30 min, 30/30 buffers, 5 business days) in
`booking_event_types`.

## Changing something

- Hours: the Weekly Hours editor in the teacher schedule, or `set_booking_availability`.
- A one-off day (open a Saturday evening, close a day): `set_booking_availability_overrides`
  via SQL for now. There is **no admin UI for overrides yet**.
- Buffer, notice, window: `UPDATE booking_availability_config SET ... WHERE id = 1`. If the
  buffer changes, also re-create `booking_buffered_range` with half the new value and rebuild
  `no_overlapping_bookings` (migration `20260911000000_booking_policy_mirrors_calcom.sql`
  says how).

## When a student reports "That time was just taken"

1. Confirm nothing was booked: `booking_pass_redemptions` for the pass, `booking_link_hits`
   for their attempts (per-minute counts by action).
2. Prove list = database: run the generator locally against `get_booking_availability()` and
   live busy data, feed every slot through `is_slot_bookable(start, 70) AND
   booking_slot_is_clear(start, end, 10, 10)`. Anything rejected is the bug.
3. A day full on LSAT U but open on Cal.com is a stale `schedule_events` row; compare with
   `gws calendar events list` for that day. The pull sync tombstones these after a clean run.

## History

2026-09-10 — Sandra Kooh, five failed attempts. The list required 15 min next to a booking,
the RPC and constraint required 30. 15 of 109 visible slots were traps. Fixed 2026-09-11 in
PR #115; every generated slot verified against the live database (134/134, 134/134, 26/26).
Two phantom "Andrew" Saturdays (09-12, 09-19) were also hiding all Saturday slots.
