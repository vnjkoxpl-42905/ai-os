---
title: Guided Drill Verification Log
type: project
tags: [lsat-u, guided-drills, verification, assignments]
created: 2026-07-03
updated: 2026-09-30
status: active
subject: Guided Drill Verification Log
aliases: []
---

# Guided Drill Verification Log

Running log of guided drills that have already been verified in the live platform. Once a drill is listed here as `verified-working`, do not repeat full browser launch QA before assigning it again unless the drill, runner, guided-drill routing, or assignment wiring has changed.

## Rules

- Check this page before browser-verifying a guided drill.
- If `status` is `verified-working`, skip full launch QA and cite the prior verification.
- Still verify the target student's profile/access and the post-assignment rows/notification every time.
- Re-verify a drill only when there is a relevant code/data change, broken student report, or explicit request from Joshua.

## Verified Drills

| Date verified | Drill | Slug | Verification evidence | Status | Notes |
|---|---|---|---|---|---|
| 2026-07-03 | Necessary Assumption - First Taste | `w2-07-necessary-assumption-first-taste` | Live preview opened; runner loaded 10 real question ids and first LR question/answer choices; targeted tests passed 33/33. | verified-working | Assigned to [C. Alexander](../students/non-students/c-alexander/c-alexander.md) the same day. |
| 2026-07-03 | Missing Links: First Taste | `w2-06-missing-links-first-taste` | Live library card matched W2.6 metadata; runner loaded 6 real question ids and first LR question/answer choices; targeted tests passed 33/33. | verified-working | Assigned to [Bella Lorenzo](../students/non-students/bella-lorenzo/bella-lorenzo.md) the same day. |

## Needs Reverification

Add entries here if a verified drill later needs re-checking.

| Date flagged | Drill | Slug | Reason | Resolution |
|---|---|---|---|---|

## Headless assignment and content verification (2026-09-30)

These are `verified-headless`, not browser runner launch checks. Joshua explicitly requested headless guided assignments. The [student assignment log](../students/yahunatan-zetvy/assignment-log.md) records full IDs and exact content specifications.

| Date | Drill slug | Evidence | Status |
|---|---|---|---|
| 2026-09-30 | `yahunathan-mbt-conditionals-2026-09-30` | Four deployed conditional MBT questions, difficulty 1-2; complete stimulus and five choices; saved catalog matches specification; one assignment and visible Classroom item; correct local dates; one unread bell; inbox/bell/email returned OK | verified-headless |
| 2026-09-30 | `yahunathan-mbt-conditionals-2026-10-01` | Four deployed conditional MBT questions, difficulty 2-3; complete stimulus and five choices; saved catalog matches specification; one assignment and visible Classroom item; correct local dates; one unread bell; inbox/bell/email returned OK | verified-headless |
| 2026-09-30 | `yahunathan-mbt-conditionals-2026-10-03` | Four deployed conditional MBT questions, difficulty 3; complete stimulus and five choices; saved catalog matches specification; one assignment and visible Classroom item; correct local dates; one unread bell; inbox/bell/email returned OK | verified-headless |
| 2026-09-30 | `w5-02-conditional-logic-easier-set-4` | Existing published drill; deployed pool 56 questions difficulty 1-2, native count 9; level/count/source row and Classroom dates/visibility verified; one bell; inbox/bell/email OK; repeat returned same ID without notification | verified-headless |
| 2026-09-30 | `w3-12-conditional-logic-easier-set-2` | Existing published drill; deployed pool 87 questions difficulty 2-3, native count 7; level/count/source row and Classroom dates/visibility verified; one bell; inbox/bell/email OK; repeat returned same ID without notification | verified-headless |
| 2026-09-30 | `w7-08-conditional-logic-medium-set-4` | Existing published drill; native pool 3-4, beginner assignment selects 52 eligible difficulty-3 questions without fallback, native count 9; source row and Classroom dates/visibility verified; one bell; inbox/bell/email OK; repeat returned same ID without notification | verified-headless |


## 2026-10-25 | Amanda recap homework

- `w2-03-must-be-true-first-taste`: 6 questions, beginner, effective difficulty 1-3; assignment `047ab1ac-299c-4a9e-88c6-12cfb5c485c4`, Classroom `51b66ba4-1495-453e-9f58-62dc2954089a`.
- `w8-04-parallel-flaw-famous-flaws-set-2`: 5 questions, beginner, effective difficulty 2-3; assignment `c8de0383-5c77-4aa6-b294-567fcb48d1b1`, Classroom `ba73da4f-6d32-4ddb-a082-4ad7a5ac6cbd`.

Both published pools preflighted live; schedule 2026-10-25, due 2026-11-01 local. Source assignments, Classroom dates/visibility and exactly one bell per guided assignment verified. Inbox/bell/email accepted. Verified headlessly, not browser launch or receipt. Evidence: students/amanda/assignments/2026-10-25-recap-homework/.

- **2026-11-16 · Ore:** Verified Classroom assignment read-back for w10-famous-flaws-easier and w8-01-famous-flaws-medium-set-1. Five eligible questions per assignment at levels 1–2 and 3–4 respectively. Future unlocks verified. Runner launch and deferred notification delivery were not tested. Evidence: [[students/ore/assignment-log]].

- **2026-11-17 - Sara:** `w2-07-necessary-assumption-first-taste` assigned headlessly. Preview and assignment verified (10 questions, pool 109, difficulty 1 to 3, one bell, Classroom item 4db0406c-a6cb-4ce6-befc-3b7ffd34d155). Runner launch and email receipt not tested. Evidence: [[students/sara-altuwaijri/assignment-log]].
