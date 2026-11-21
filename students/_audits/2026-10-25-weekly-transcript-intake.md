---
title: Weekly transcript intake 2026-10-19 through 2026-10-25
type: operational-audit
status: completed-with-source-gaps
updated: 2026-10-25
---

# Weekly transcript reconciliation

Scope: 2026-10-19 00:00 through 2026-10-26 00:00 America/Toronto. Live searches completed 2026-10-25 about 03:14 America/Toronto. The Sunday evening booking is future at that cutoff.

Primary Calendar was queried with expanded recurrence, showDeleted=true, maxResults=250. Twelve events returned, all confirmed, no nextPageToken. Guest emails establish student matches; a confirmed booking alone does not establish attendance.

Three completed native Google Docs searches checked (1) Gemini/Meeting-started names created in the window, (2) all native Docs created in the window, and (3) native Docs with requested dates in their names irrespective of creation time. All returned incompleteSearch=false and no nextPageToken. The name search also returned fuzzy out-of-window matches, excluded by actual title/date. All seven weekly native Doc IDs matched Calendar attachments; no unattached weekly source was found. Uploaded copies are not additional sessions. Google Workspace was accessed through gws CLI only. Evidence: [[2026-10-25-weekly-intake-evidence/calendar.json|Calendar JSON]], [[2026-10-25-weekly-intake-evidence/drive.json|Gemini created-window search]], [[2026-10-25-weekly-intake-evidence/drive-all-native.json|All-native created-window search]], [[2026-10-25-weekly-intake-evidence/drive-date-names.json|Date-name search]].

## Session-by-session result

| Date | Person | Result | Local record |
|---|---|---|---|
| 2026-10-19 | Whit Wilson (Whitney) | Already complete; existing export and package byte-identical to fresh live export, SHA-256 af35e5c3700c8f480c49d998f8e56cb3d785b3cb50e99023d14ebd0ba7933b0c. Existing observations, follow-ups, preferences and routers retained. | [[../whit-wilson/sessions/2026-10-19-claim-precision-and-rephrasing/summary]] |
| 2026-10-20 | Yahunatan Zetvy | Completed: full export, package, private distillation, commitments/preferences and routers. | [[../yahunatan-zetvy/sessions/2026-10-20-negation-and-necessary-assumptions/summary]] |
| 2026-10-21 | Sofia Minassian | Completed: full export, package, private distillation, commitments/preferences and routers. | [[../sofia/sessions/2026-10-21-necessary-assumptions-and-warm-up/summary]] |
| 2026-10-21 | Amanda Huynh | Completed: full export, package, private distillation, commitments/preferences and routers. | [[../amanda/sessions/2026-10-21-conditional-rules-facts-and-parallel-flaws/summary]] |
| 2026-10-21 | Celia Cutler | Completed: full export, package, private distillation, commitments/preferences and routers. | [[../celia-cutler/sessions/2026-10-21-generalization-flaws-and-reading-warm-up/summary]] |
| 2026-10-22 | Venusa Laveaux | Source not found in completed searches; attendance unconfirmed. Existing record documents objection to transcription; no source recreated. | [[../venusa-laveaux/transcripts]] |
| 2026-10-22 | Ana consultation, nastiyahaydash@icloud.com | Source not found in completed searches; attendance unconfirmed. No student folder created; consultation remains in this intake inventory under the existing other-sessions routing policy. | Calendar event _etd5ig9k6pa76q1oegqjij9naoq5auig9p8k0gr1dgn66rrd |
| 2026-10-22 | Zeina Borji | Completed: full export, package, private distillation, commitments/preferences and routers. Calendar booked 15:30; native Doc title says 18:33 EDT. Preserve timing discrepancy. | [[../zeina-borji/sessions/2026-10-22-conditional-foundations-and-study-plan/summary]] |
| 2026-10-22 | Gianna Jean | Source not found in completed searches; attendance unconfirmed. | [[../gianna/transcripts]] |
| 2026-10-23 | Oreoluwa James | Completed: full export, package, private distillation, commitments/preferences and routers. | [[../ore/sessions/2026-10-23-argument-refresher-and-causal-scope/summary]] |
| 2026-10-24 | Sandra Kooh | Source not found in completed searches; attendance unconfirmed. | [[../sandra/transcripts]] |
| 2026-10-25 | Gianna Jean, 17:00 | Future at cutoff; no attendance or missing-transcript conclusion. | [[../gianna/transcripts]] |

No lesson, recap, posting, assignment, email, source deletion, or unknown student-folder creation is authorized by this intake. Sources were preserved without overwriting previous generations. The seven original full-export hashes and byte counts are recorded in [[2026-10-25-weekly-intake-evidence/export-hashes.json|export hash manifest]]. A fresh verification export of Whit's Doc is preserved in the evidence directory and matches her existing source bytes.

## Validation

Completed 2026-10-25: py system/scripts/check-student-records.py passed, checking 23 student folders, 130 full local Markdown exports and 58 packages. All internal routers and local session links resolve; no unrelated failures. Independently recomputed all seven export hashes and verified every package transcript is byte-identical. All six newly ingested sources were read in full and distilled; Whit was already complete and fresh live-source bytes match. Final source coverage: six newly completed, one already complete, four past bookings without a source in completed searches, one future booking. No failed search remains hidden as a missing-source conclusion.
