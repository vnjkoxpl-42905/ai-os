---
title: Pre-consultation check-in log
type: operating-layer
record_kind: primary
tags: [operating-layer, correspondence, consultations]
created: 2026-09-11
status: active
subject: Pre-consultation check-in log
aliases: [PRE-CONSULT-LOG]
---

# Pre-consultation check-in log

One row per Cal.com consultation the `pre-consultation-check-in` skill has
handled. Written by `scripts/checkin.py`; safe to read, do not hand-edit rows
(the script rewrites the table). To stop a scheduled send, run
`checkin.py cancel --event-id <id>` rather than deleting the row.

**Status meanings**

- `scheduled` — a one-shot Windows task exists and will send 30 minutes before the consultation
- `sent` / `sent-late` — the email went out (late = fired after T-30 but still before the start, e.g. the laptop was asleep)
- `sent-now` — T-30 had already passed when the skill ran, so it sent immediately
- `cancelled` — the booking disappeared or was cancelled before the send; nothing sent
- `moved` — the start time changed; the old task was replaced (a new `scheduled` row follows)
- `missed` — the task could not run before the consultation started; nothing sent
- `failed` — the send errored; see Note and logs/checkin.log
- `cancelled-by-joshua` — Joshua opted this one out; the skill will not re-create it

Related: [[send-ledger]] gets one row when a send is scheduled and one when it goes out.

## Log

| Consultation (Toronto) | Student | Email | Status | Fires at | Task | Note | Event ID | iCalUID |
|---|---|---|---|---|---|---|---|---|
