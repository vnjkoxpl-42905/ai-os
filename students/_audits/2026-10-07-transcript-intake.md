---
title: Transcript intake · 2026-09-29 to 2026-10-07
type: audit
record_kind: primary
as_of: 2026-10-07T16:47:32-04:00
status: intake-complete-with-evidence-gaps
---

# Five transcript sources across the eight-day window

The scan covered 2026-09-29 00:00 through 2026-10-07 16:47:32 in America/Toronto. Google primary Calendar and a complete Drive listing of 299 native Google Docs named `Notes by Gemini` or `Meeting started` were reconciled. The Drive listing had no continuation token. Source session dates were checked independently of creation dates. Uploaded Markdown copies were excluded.

Calendar returned 18 bookings: 16 past confirmed events, one explicit cancellation, and one future event. Five past bookings have attached native Gemini Docs. The other 11 past bookings have no matching Gemini Doc anywhere in the checked Drive listing. Missing notes establish neither attendance nor cancellation. No unattached transcript in this date window was found. All five exports were absent locally at the start of this pass and were exported as `text/plain` for intake.

## The five sources and their record homes

| Local date | Person and local record | Calendar event ID | Native Doc |
|---|---|---|---|
| 2026-09-29 | [Sofia Minassian](../sofia/transcripts.md) | `680eb8f3b6db4a70a9a8d299f14495ae` | [Source](https://docs.google.com/document/d/16BfIKhEGj9g-TZLdbjzvLln9U6V3w9t6jg9WEZN59z4/edit) |
| 2026-10-02 | [Charles Moore](../charles-moore/transcripts.md) | `116976dfb26941b29421b4f870b6184d` | [Source](https://docs.google.com/document/d/1vceAbqsIwbXRSPVv2n476z_O4Y7ojRQqAooGBO7bBLA/edit) |
| 2026-10-02 | [Zeina Borji](../zeina-borji/transcripts.md) | `ssd14f6241fef84effaff07f2147526cfe` | [Source](https://docs.google.com/document/d/1LxUMqKPEX73dEbNiDO6Yxe4Sg9RUwBGJoeTqM664qaI/edit) |
| 2026-10-03 | [Ivory Johnson](../ivory-johnson/transcripts.md) | `46cdd5v18dnqtd5e3q02k6u3u0` | [Source](https://docs.google.com/document/d/1hWpVEme70s5yPRA7e8A3m1rsieE23vB0ZRkA112zh6A/edit) |
| 2026-10-06 | [Yahunatan Zetvy](../yahunatan-zetvy/transcripts.md) | `9a4f72d217ad47a39d102a93c616c279` | [Source](https://docs.google.com/document/d/19vWxelDXapKNDA0vKl8fbu_WIDIVDhbZ1eIrwwE8d5M/edit) |

The source-to-person mapping uses the Calendar attachment ID and guest email, checked against local records and `students/_aliases.md`. Sofia, Charles, and Zeina also have matching student speaker labels. Ivory and Yahunatan have recordings dominated by Joshua's speaker labels; the event guest and attached source establish their mapping.

## Eleven past bookings have no matching source

| Local date | Time | Booked person | Guest address |
|---|---|---|---|
| 2026-09-29 | 15:40 | Yahunatan | ynproemail@gmail.com |
| 2026-09-30 | 13:00 | Gianna | giannajean005@gmail.com |
| 2026-09-30 | 14:20 | Whitney | whitwilson929@gmail.com |
| 2026-09-30 | 15:40 | Sandra | koohsandra@gmail.com |
| 2026-09-30 | 17:00 | Yahunatan | ynproemail@gmail.com |
| 2026-10-01 | 15:00 | Ivory | ivoryj.johnson3@gmail.com |
| 2026-10-01 | 17:20 | Venusa | laveaux.law@gmail.com |
| 2026-10-02 | 15:40 | Sofia | sofiaminassian@gmail.com |
| 2026-10-05 | 15:20 | Sofia | sofiaminassian@gmail.com |
| 2026-10-06 | 15:00 | Ivory | ivoryj.johnson3@gmail.com |
| 2026-10-07 | 15:00 | Whitney | whitwilson929@gmail.com |

Every row remains attendance-uncertain. Whitney's 2026-10-07 scheduled event ended at 16:10, shortly before the cutoff, so a later-created Doc remains possible. Venusa's existing private record says her only verified official session was 2026-09-24, based on Joshua's 2026-09-28 confirmation; that evidence does not establish attendance for the 2026-10-01 booking.

## The cancelled and future bookings

- Gianna, 2026-10-06 17:00: Calendar explicitly marks event `fh9tf3duat762fnqiov3o0e22o` cancelled. It is excluded from the missing-transcript count.
- Sofia, 2026-10-07 17:00: event `5e479aadb54d497ea98f508735c2b57c` starts after the cutoff. It is excluded from intake and the missing-transcript count.

## Preserve source timing disagreements

- Sofia's attached Calendar event starts 2026-09-29 21:00 EDT, and the Drive title names the same local date and time. The raw Doc header says 2026-09-30. The session is filed under verified local date 2026-09-29; the header is preserved. A UTC date rollover is a plausible explanation because 21:00 EDT is 01:00 UTC on 2026-09-30, but Gemini's header timezone was not independently verified.
- Yahunatan's 2026-10-06 event is booked 18:20 to 19:30 EDT, while the attached Doc title starts 19:42 EDT. The matching guest and attached source ID identify the student and local date, but the actual start-time disagreement remains explicit.

Discovery evidence and SHA-256 hashes are in `system/logs/transcript-intake-2026-10-07/reconciliation.generated.json`, alongside the raw Calendar and Drive JSON responses and unchanged text/plain exports. This report records discovery; completed record preparation and checks belong in the intake log.


## Record preparation completed · 2026-10-07

All five native sources are now preserved in the matching student's transcript-downloads folder with exact byte/hash matches and a complete session package. Teaching notes and open loops were appended; newest-first inventories and profile routers link the new records. Source summary errors remain preserved with explicit transcript-grounded qualifications. No recap, assignment, publication or send was performed.

- [Sofia package](../sofia/sessions/2026-09-29-lr-review-pacing-and-accommodations/summary.md).
- [Charles record](../charles-moore/transcripts.md).
- [Zeina record](../zeina-borji/transcripts.md).
- [Ivory package](../ivory-johnson/sessions/2026-10-03-sufficient-assumption-pathways/summary.md).
- [Yahunatan package](../yahunatan-zetvy/sessions/2026-10-06-quantifiers-and-must-be-true/summary.md).

Final check: 23 student folders, 119 Markdown files under transcript-downloads (117 source exports plus two new provenance files), 47 complete session packages. All internal record links resolve. All five new exports and package transcripts match the staged source SHA-256. Eleven no-source bookings remain attendance-uncertain; these are unresolved evidence gaps, not cancelled-session findings.

Discovery artifacts were filed intact from the temporary staging directory into [system/logs/transcript-intake-2026-10-07](../../system/logs/transcript-intake-2026-10-07/reconciliation.generated.json). Embedded exportPath fields retain the original capture location for provenance; filenames now live beside the reconciliation. [Final verification](../../system/logs/transcript-intake-2026-10-07/verification.generated.json).
