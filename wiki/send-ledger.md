---
title: Send ledger
type: operating-layer
record_kind: primary
tags: [operating-layer, correspondence]
created: 2026-07-20
status: active
subject: Send ledger
updated: 2026-07-20
aliases: []
---

# Send ledger

Append-only record of every outbound message Jay 2 drafts or sends on Joshua's
behalf. One line per message, newest at the bottom.

It exists to answer one question that was previously unanswerable: **"did X get
their email yet?"** That question has gone unanswered before because sends were
logged only in each student's `open-loops.md`, which requires already knowing
who to check. This is the single surface you can scan.

## Rules

- **Append only.** Never edit or delete a past line. A wrong line gets a new
  line below it correcting the record, the same way a ledger works.
- **Log the truth, not the intent.** `drafted` and `sent` are different states.
  A draft that was never approved stays `drafted` forever. If a send fails, log
  `failed` with the reason.
- **Log at the moment it happens,** not in a batch at the end. A crashed session
  must not lose the record of something that actually went out.
- **This is a mirror of Gmail, not the authority.** Gmail owns what was really
  sent. On any disagreement Gmail wins — but this tells you where to look.
- Every skill that drafts or sends to a student or prospect writes here:
  `send-booking-link`, `morning-brief`, `consultation-inquiry-drafts`,
  `consultation-followup-drafts`, `inbound-tutoring-replies`,
  `pre-consultation-check-in` (writes `scheduled` when a T-30 task is
  registered and `sent` / `failed` when it fires; the per-booking state lives
  in [[PRE-CONSULT-LOG]]).
- The per-student `open-loops.md` entry still gets written too. That one carries
  the follow-up loop; this one carries the answer to "was it sent".

## Format

```
| YYYY-MM-DD HH:MM | recipient | what it was | drafted \| sent \| failed | note |
```

`recipient` is the student folder slug where one exists, otherwise the name or
address. `note` carries the reason on `failed`, or the approval on `sent`.
`scheduled` means a future send has been registered with the machine and will
go out without a further approval (pre-consultation check-ins only).

## Ledger

| When | Recipient | What | Status | Note |
|---|---|---|---|---|
| 2026-07-20 00:00 | — | ledger created | — | no sends recorded before this date; earlier sends exist only in per-student `open-loops.md` |
| 2026-07-20 03:11 | c-alexander | Booking link email | drafted | Joshua approved exact copy; scheduled for 2026-07-20 08:00 EDT after live verification that the pass is active with 1 credit |
| 2026-09-08 18:56 | sandra | booking link (/book/sandra-wc4kt2xjhcbxc4bqbytas9qmad) | sent 2026-09-09 | 10 credits. First draft cut per COPY-CORRECTIONS (no session length or expiry in booking emails) and deleted. Msg 1a0845859ba8b240 |
| 2026-09-11 00:5x | sandra | booking error reply (Re: Your scheduling link) | sent 2026-09-11 | Confirmed nothing booked, link unchanged, offered to add her time by hand. Msg 1a08ed89657937e6. Shape recorded in teaching-voice.md "When something on his side broke". |
| 2026-09-11 15:44 | test-preconsult | pre-consult check-in (consult 2026-09-11 16:16) | scheduled | fires 2026-09-11 15:46 via Task Scheduler \LSATU\PreConsult\PreConsult_2026-09-11_1616_Test-Preconsult; to contact+preconsult-test@aspiringattorneys.com |
| 2026-09-11 15:46 | test-preconsult | pre-consult check-in (consult 2026-09-11 16:16) | sent 2026-09-11 | auto-send at T-30 via pre-consultation-check-in; Msg 1a0920193499db80 |
| 2026-09-11 15:47 | test-cancelled | pre-consult check-in (consult 2026-09-11 16:47) | scheduled | fires 2026-09-11 16:17 via Task Scheduler \LSATU\PreConsult\PreConsult_2026-09-11_1647_Test-Cancelled; to contact+preconsult-test@aspiringattorneys.com |
| 2026-09-11 15:48 | test-moved | pre-consult check-in (consult 2026-09-11 16:57) | scheduled | fires 2026-09-11 16:27 via Task Scheduler \LSATU\PreConsult\PreConsult_2026-09-11_1657_Test-Moved; to contact+preconsult-test@aspiringattorneys.com |
| 2026-09-11 15:48 | test-moved | pre-consult check-in (consult 2026-09-11 18:28) | cancelled | test of manual cancel |
| 2026-09-11 15:49 | test-reconcile | pre-consult check-in (consult 2026-09-11 17:09) | scheduled | fires 2026-09-11 16:39 via Task Scheduler \LSATU\PreConsult\PreConsult_2026-09-11_1709_Test-Reconcile; to contact+preconsult-test@aspiringattorneys.com |
| 2026-09-11 16:05 | adriana-varea | "Today's session" (asked if 5:10 pm works, apologised for last-second notice) | sent 2026-09-11 | to adrianavarea9@gmail.com; calendar event moved 5:00→5:10; Msg 1a0922af54c53896 |
| 2026-09-11 16:30 | zeina-borji | consultation follow-up (consult 2026-09-10) | sent 2026-09-11 | reply in her thread "Meeting setup and extra"; template wiki/CONSULTATION-FOLLOW-UP-TEMPLATE.md + 7Sage line + "Sunday works for me"; Msg 1a0927209dcf2bb4 |
| 2026-09-11 16:50 | venusa-laveaux | consultation follow-up (consult 2026-09-11 13:00) | sent 2026-09-11 | reply in "LSAT Tutoring" thread; template verbatim, no 7Sage line (she declined transcription, no notes) |
