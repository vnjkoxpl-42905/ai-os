---
title: Student record audit, 2026-09-25
type: audit
record_kind: primary
as_of: 2026-09-25
status: snapshot
---

# Student record audit, 2026-09-25

This is a dated snapshot, not an operational source of truth. Calendar, Gmail, Cal.com, LSAT U, and payment systems remain authoritative for their live state. No missing file below should be filled with an empty placeholder or inferred status.

## What was corrected

- Ingested the four native Gemini Docs attached to completed Calendar bookings from 2026-09-21 through 2026-09-24: Celia, Amanda, Sofia, and Sandra. Their existing session packages were retained. Full source exports, teaching notes, inventories, and follow-ups were filed.
- Added Gianna and Sandra to `students/README.md`; clarified the intended layout, the current LSAT U-only scope of `live-status.generated.md`, and the distinction between raw exports and session packages.
- Removed the contradictory `generated: true` marker from the primary session-summary template and seven existing primary summaries.
- Added frontmatter to Amanda and Charles assignment logs and Amanda open loops. Created evidence-backed teaching notes and open loops where this week's transcripts warranted them.

## Folder coverage

The standard files named here are `email-context.md` (EC), `email-correspondence.md` (EM), `payment-links.md` (PL), `teaching-notes.md` (TN), `open-loops.md` (OL), `live-status.generated.md` (LS), and `assignment-log.md` (AL). All 22 folders have a profile and transcript inventory. “Missing” means no file, not that the underlying event or information is absent. The table reflects the structure after the corrections above.

| Folder | Missing standard files | Session packages / source concern |
|---|---|---|
| adriana-varea | EC, EM, PL, AL | Review source coverage |
| amanda | EC, EM, PL, LS | 2026-09-22 source ingested |
| asia | EC, EM, PL, TN, OL, LS, AL | No 2026-09-21 Doc found |
| avneet-natt | EC, EM, PL, TN, OL, LS, AL | Review source coverage |
| celia-cutler | EC, EM, PL, LS, AL | 2026-09-21 source ingested; identity label needs confirmation |
| charles-moore | EC, EM, PL, TN, OL, LS | No 2026-09-22 Doc found |
| dakota | None | Ten raw exports; no session packages |
| david-salgado | EM | Twelve raw exports; no session packages |
| ethan | None | Six raw exports; no session packages |
| favour | EC, EM, PL | Raw export without a session package |
| fernande-charleus | EC, EM, PL, TN, OL, LS, AL | Review source coverage |
| gianna | EC, EM, PL, TN, OL, LS, AL | One session package |
| ivory-johnson | EC, EM, PL, TN, OL, LS, AL | No 2026-09-17 or 2026-09-24 Doc found |
| nicole | None | Two raw exports; no session packages |
| ore | EC, EM, PL, TN, OL, LS, AL | No 2026-09-18 or 2026-09-22 Doc found |
| sandra | EC, EM, PL, LS, AL | 2026-09-23 source ingested; no 2026-09-17, 2026-09-21, or 2026-09-24 Doc found |
| sofia | None | 2026-09-23 source includes a later unrelated conversation |
| steven-morris | EC, EM, PL, TN, OL, LS, AL | 2026-09-03 package transcript is only 756 bytes |
| vinay-kalva | EC, EM, PL, TN, OL, LS, AL | Review source coverage |
| whit-wilson | EC, EM, PL, TN, OL, LS, AL | Review source coverage |
| yahunatan-zetvy | EC, EM, PL | No 2026-09-23 Doc found |
| zeina-borji | EM, PL, LS, AL | Review source coverage |

Every one of the 35 existing session-package directories has `transcript.md`, `summary.md`, and `topic-map.md`. Content completeness still needs a source check; Steven's short transcript demonstrates why filenames alone are insufficient.

## Calendar reconciliation

For 2026-09-21 through 2026-09-24, 14 confirmed bookings had ended. Four had attached Gemini Docs and were ingested. Ten had no attached Doc and no matching native Google Doc created in the window: Asia, Sofia, Sandra on 2026-09-21; Charles and Ore on 2026-09-22; Yahunathan on 2026-09-23; Angie Pasquel (consultation), Ivory, Venusa, and Sandra on 2026-09-24. Confirmed booking status does not establish attendance. Four further sessions were scheduled for 2026-09-25 and 2026-09-26 at audit time.

For 2026-09-14 through 2026-09-20, 14 teaching/consultation bookings were confirmed. Nine had attached Gemini Docs and matching local session packages. Five had no attached Doc and no matching native Google Doc created that week: Celia on 2026-09-14; Ivory and Sandra on 2026-09-17; Ore and Ritaj Abbasi (consultation) on 2026-09-18. The two other confirmed Calendar blocks were personal or ambiguous (`Liturgy`, `Online`), so they were not classified as missing teaching notes. Twelve cancelled entries were excluded.

## Next structural improvements

1. Verify which no-Doc bookings actually took place. Search alternate source types only for attended meetings; record a true missing transcript separately from a meeting that did not occur.
2. Populate EC, EM, PL, and LS only from verified Gmail, payment, booking, and LSAT U sources. Keep mirror files marked as generated and primary judgments append-only. The large count of absent files makes this a data backfill, not a formatting edit.
3. Review Steven's 2026-09-03 source and the Sofia 2026-09-23 mixed conversation. Intake should check guest identity, source length, duration, timestamp, speaker changes, and Calendar match before declaring a package complete.
4. Decide whether to package historical raw-only exports. Preserve them regardless of that decision; packaging them all is a separate historical backfill.
5. Keep `students/_other-sessions/` separate as the reference corpus for one-off consultations and people without a student record. Do not create new student folders from a Calendar title alone.
