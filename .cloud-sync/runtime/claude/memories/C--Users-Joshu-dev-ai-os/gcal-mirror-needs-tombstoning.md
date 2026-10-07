---
name: gcal-mirror-needs-tombstoning
description: "schedule_events rows synced from Google were never marked deleted when the event vanished from the calendar; two phantom \"Andrew\" Saturdays blocked all Saturday slots. gcal-sync-pull now tombstones after a clean full-window pass."
metadata: 
  node_type: memory
  type: project
  originSessionId: 42293442-2c4d-4ca9-a5bb-5b3746a4b627
  modified: 2026-09-11T03:40:15.319Z
---

`gcal_sync_state.sync_token` is null, so every `gcal-sync-pull` run is a windowed full list
(now-14d .. now+90d). Google does not return deleted or shortened-series occurrences as
`cancelled` on a windowed list, so mirrored rows outlived their events. Found 2026-09-11: two
"Andrew" occurrences (2026-09-12, 2026-09-19, synced 2026-06-22) blocked every Saturday slot
while Cal.com offered the day.

Fix (PR #115): after a full-window pass with no sync token and no write errors, rows with
`source='google'` inside the window whose `google_event_id` was not returned get
`deleted_at`/`status='cancelled'`. Rows LSAT U wrote itself are left to their reconcilers.
Note `gcal-sync-pull` overwrites `source` to `google` on every upsert, so LSAT U-booked
sessions also carry `source='google'` after a sync; that is fine because `loadBusyIntervals`
now also reads booked redemptions directly.

**Why:** A stale mirror row is invisible from the calendar and silently eats availability.
**How to apply:** If a day is "mysteriously full" on LSAT U but open on Cal.com, compare
`schedule_events` (deleted_at null, in range) against `gws calendar events list` for that day
before touching code. See [[booking-slot-checks-must-share-one-arithmetic]].
