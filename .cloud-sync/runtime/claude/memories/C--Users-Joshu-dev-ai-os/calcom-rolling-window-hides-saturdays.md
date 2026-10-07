---
name: calcom-rolling-window-hides-saturdays
description: The cal.com session link only shows 6 business days out, so students can see at most one Saturday and often can't book the weekend they want.
metadata:
  type: project
---

`cal.com/joshua-jtx5ud/session-link` is configured `periodType: ROLLING`, `periodDays: 6`,
`periodCountCalendarDays: null` — six **business** days ahead. Weekends inside that span are
visible but don't count toward the six, so a student browsing on a Tuesday sees exactly one
Saturday and cannot advance the calendar past the following Wednesday.

Event length is 70 min with no `slotInterval`, so slots stack in 70-minute steps from the start
of each availability window. A short Saturday window therefore yields a single bookable time.

Payment is Stripe `ON_BOOKING`, **$45 USD**, `refundPolicy: never`. Canadian students hit a
foreign-currency card charge at the booking step — this is why e-transfer requests come up
(see [[whitney-wilson-scheduling]]).

**Why:** "Scheduling is broken" reports from students are usually this config, not a bug.
**How to apply:** Before debugging a student's booking complaint, pull the event config
(`https://cal.com/api/trpc/public/event?input={"json":{"username":"joshua-jtx5ud","eventSlug":"session-link","isTeamEvent":false,"org":null}}`)
and the real slot list, and compare against the student's timezone.
