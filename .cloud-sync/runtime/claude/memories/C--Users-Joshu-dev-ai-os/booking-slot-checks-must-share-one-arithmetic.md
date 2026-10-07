---
name: booking-slot-checks-must-share-one-arithmetic
description: "That time was just taken" with nothing taken means the slot list and the DB predicate disagree; every LSAT U slot check reads booking_availability_config (buffer 10, notice 1440, window 45) and the shared booking_slot_is_clear().
metadata:
  type: project
---

On 2026-09-10 Sandra hit "That time was just taken" five times from her pass link. Zero
redemptions existed. Cause: the slot list and the edge guard required a 15-minute gap next to
an existing booking, but `redeem_booking_pass_v2` and the `no_overlapping_bookings` EXCLUDE
constraint buffered both rows (30 min effective). 15 of her 109 visible slots were traps: the
first slot after and last slot before each existing session.

Fixed 2026-09-11 (PR #115, migration `20260911000000_booking_policy_mirrors_calcom.sql`,
ADR `docs/adr/0010-one-buffer-counted-once.md`):
- Buffer **10 min** (Joshua's number), notice 1440, window 45 calendar days, all in
  `booking_availability_config` row 1. SQL reads it via `booking_buffer_minutes()`; edge code
  via `get_booking_availability()` -> `parseAvailability()` / `loadAvailability()`.
- One predicate `booking_slot_is_clear(start, end, before, after, ...)` used by the pass RPC
  and all three single-session RPCs. Busy rows are never buffered; only the probe is.
- EXCLUDE constraint buffers each row by a literal **5 min** (GiST needs IMMUTABLE). Changing
  the buffer means re-creating `booking_buffered_range` and rebuilding the constraint.
- One `generateSlots({ policy, hours, nowMs, busy })` in `_shared/bookingCore.ts`; the
  single session and consultation delegate to it. Pitch = length + buffer (80 min), stepping
  from each range start. `is_slot_bookable` enforces the same grid.
- Date overrides live in `booking_availability_overrides` (a date's rows replace weekly
  hours; null times close the day). Admin write path `set_booking_availability_overrides`.
  No admin UI yet.

**Why:** Two independent implementations of "is this slot free?" will drift. The student
sees the list; the database has the last word; they must be the same function of the same
numbers.
**How to apply:** Any change to buffer, pitch, notice, window or hours goes in the config row
or the overrides table, never in code constants. To prove a change, run the generator locally
against `get_booking_availability()` + live busy data, then feed every slot through
`is_slot_bookable(start, 70) AND booking_slot_is_clear(...)` and require 100% acceptance.
See [[calcom-pending-bookings-are-unpaid]] for the Cal.com-side failure mode.
