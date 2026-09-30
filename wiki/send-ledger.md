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
| 2026-09-14 15:52 | zeina-borji | booking link update (Re: Meeting Cancellation) | sent 2026-09-14 | Sent updated link (https://lsatprep.study/book/session), noted no slots today but slots tomorrow; Msg 1a0a17a10df330dd |
| 2026-09-14 18:11 | celia-cutler | Rescheduling session today to Wednesday (emergency came up) | sent 2026-09-14 | to celiacutler@gmail.com; offered Wednesday afternoon or evening after 7:00 PM; Msg 1a0a1f9ce41a8a58 |
| 2026-09-23 01:13 | gianna-jean | Request for Accommodations (QP form attached) | sent 2026-09-23 | to giannajean005@gmail.com; skill accommodations-email; default 4 items; new "process moving" opener; no student folder yet; Msg 1a0ccaefd2b5f2d1 |
| 2026-09-23 01:14 | amanda | Request for Accommodations (QP form attached) | sent 2026-09-23 | to amhuynh@asu.edu; skill accommodations-email; default 4 items; new "process moving" opener; Msg 1a0ccaf7700409e9 |
| 2026-09-28 00:01 | gianna-jean | Your 10-session tutoring booking link | drafted | to giannajean005@gmail.com; existing 10-session pass, 0/10 used; Gmail draft r-6664624807132742590; not sent |
| 2026-09-28 00:16 | gianna-jean | Your 10-session tutoring booking link | revised draft | replaced long public URL with account-bound https://lsatprep.study/book/gianna; removed October-date line; Gmail draft r-6664624807132742590; not sent |
| 2026-09-28 00:28 | gianna-jean | Your 10-session tutoring booking link | revised draft | Corrected destination to original no-login prepaid calendar; visible HTML link text is Book your sessions; Gmail draft r-6664624807132742590; not sent |
| 2026-09-28 00:46 | gianna-jean | Your 10-session tutoring booking link | revised draft | Removed Wednesday/Sunday availability line; added schedule whenever ready and accommodations check-in; original no-login booking link retained; Gmail draft r-6664624807132742590; not sent |
| 2026-09-28 01:26 | gianna-jean | Your 10-session tutoring booking link | sent 2026-09-28 | Joshua explicitly approved send in chat; to giannajean005@gmail.com; exact approved HTML draft with original no-login booking link; Gmail message 1a0e67ab26ae8be6; one matching Sent message verified |
| 2026-09-28 01:41 | whit-wilson | Re: Updated Scheduling Link | revised draft | to whitwilson929@gmail.com; replaced prior unsent general-session draft with prepaid one-credit booking URL; draft r790915509299354042, message 1a0e688041b52df7; not sent |
| 2026-09-28 02:32 | whit-wilson | Re: Updated Scheduling Link | revised draft | to whitwilson929@gmail.com; added specific-time squeeze-in offer and https://lsatprep.study platform link; kept prepaid booking link; existing draft r790915509299354042, message 1a0e6b74b1c575ee; not sent |
| 2026-09-28 02:34 | whit-wilson | Re: Updated Scheduling Link | sent 2026-09-28 | Joshua explicitly approved send in chat; to whitwilson929@gmail.com; prepaid one-session booking link, LSAT U platform link, specific-time offer; Gmail message 1a0e6b88e935e2f8; one new Sent copy verified against draft |
| 2026-09-30 | yahunatan-zetvy / Yahunathan | Must Be True: Translate the rules, scheduled 2026-09-30 | platform notification sent | User requested assignment; assign-lsatu-work single-student authorization. Assignment c0ee2b74-178a-43da-ba7b-51e02e7c8ac3; inbox/bell/email returned OK; one unread bell verified. Email receipt not independently verified. |
| 2026-09-30 | yahunatan-zetvy / Yahunathan | Must Be True: Connect the rules, scheduled 2026-10-01 | platform notification sent | User requested assignment; assign-lsatu-work single-student authorization. Assignment 78756ac9-953b-4cab-9f1e-33b9b64b7950; inbox/bell/email returned OK; one unread bell verified. Email receipt not independently verified. |
| 2026-09-30 | yahunatan-zetvy / Yahunathan | Must Be True: Prove the inference, scheduled 2026-10-03 | platform notification sent | User requested assignment; assign-lsatu-work single-student authorization. Assignment 9fc8acc1-0f37-4745-a65e-f0b202cb5a36; inbox/bell/email returned OK; one unread bell verified. Email receipt not independently verified. |
| 2026-09-30 | yahunatan-zetvy / Yahunathan | PT101.S3 LR, scheduled 2026-10-04 | platform notification sent | User requested assignment; assign-lsatu-work single-student authorization. Assignment faba73d8-4c9e-4e5c-bcf5-65cf5c876d85; inbox/bell/email returned OK. Email receipt not independently verified. |
