# How a consultation is identified, and why

Evidence base: 241 events on Joshua's primary Google Calendar, 2026-05-14 through
2026-10-11 (pulled 2026-09-11). 70 were consultations. 171 were everything else:
paid `<Name> session` bookings from LSAT U, `LSAT Session between Joshua and …`
bookings from Cal.com, `Reduced Rate between …`, `Complimentary session between …`,
bare-name manual sessions, church, webinars, "booked off".

## The rule

```
^Consultation\s+between\s+Joshua\s+and\s+(.+)$
```

applied to the event title (`summary`).

| Signal | Matches | False positives |
|---|---|---|
| **Title starts with `Consultation`** | 70 | **0** |
| iCalUID ends `@Cal.com` | 74 | 4 (`Complimentary session between Joshua and …`, a free session, not a consult) |
| Description contains `cal.com/booking` | 93 | 23 (the 4 complimentary + 19 paid `LSAT Session` / `Reduced Rate` bookings that came through Cal.com but were stamped `@google.com`) |
| Description blurb `LSAT strategy call: to assess your baseline…` | 70 | 0, but it is the Cal.com event-type description; rewording it in Cal.com would silently drop every match |

The title is the only signal that is both perfect on the data and visible to Joshua
every day (so a change would be noticed). The original skill required all three of
the first rows together; the extra two add nothing and would mislead anyone who
loosened the rule to "any Cal.com booking".

## What every matched event looks like

- Title spelled `Consultation  between Joshua and <Name>` with **two spaces** after
  "Consultation", all 70 times. Cal.com builds it from the event-type name, which
  carries a trailing space. `\s+` in the regex survives a future fix.
- `<Name>` is whatever the prospect typed on the Cal.com form: 50 full names, 20
  first-name-only, several with a trailing space (`'Zeina '`, `'Sandra Kooh '`).
  Strip it. First name = first token.
- Exactly one attendee without `"self": true`. That is the student. Their email is
  the only reliable address; the description repeats it but do not parse it from there.
- `iCalUID` is `<bookingUid>@Cal.com`. The same `bookingUid` is in the reschedule
  link (`https://cal.com/booking/<bookingUid>?changes=true`). It is the stable key
  for the run log.
- `start.timeZone` is always `America/Toronto`; duration always 30 minutes.
- `hangoutLink` / `location` carry the Google Meet URL.
- `status` is `confirmed`. A cancelled Cal.com booking does **not** appear in
  `events list` at all unless `showDeleted` is set; `events get` on its id returns
  `status: cancelled`. This is why the send step re-fetches by id rather than
  trusting the earlier list.

## The sanity check

If the title matches but the `iCalUID` is not `@Cal.com`, the event was made by
hand (never happened in 241 events, but a test event or a manual booking would
look like this). `find` and `schedule` list it as **flagged** instead of silently
including or dropping it; `schedule --include-flagged` schedules it anyway.

## Near misses worth knowing

- `Complimentary session between Joshua and Emily Khym` (Cal.com, free follow-up
  session): not a consultation. Sending "before our consultation today" to
  someone who already had the consultation reads as a mistake.
- `LSAT Session   between Joshua and Lydia Lee` (Cal.com paid session, three
  spaces): not a consultation.
- `Joshua Fisseha - 30 minutes meeting` (another scheduler, no `@` in the UID):
  not a consultation.
- `Adriana — Transcript Intake/Review`: not a consultation.
