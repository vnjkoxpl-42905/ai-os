---
type: generated
subject: Loophole library map (inventory, locations, gaps)
generated_by: system/scripts/query-loophole.py build
built_at: 2026-11-20T00:39:21.051873+00:00
---

# Loophole library map

Generated on every `build`; do not hand-edit. Start at [AI-RETRIEVAL.md](AI-RETRIEVAL.md). This page answers **what do we have, where is it, how do I open it and what is missing**. Counts are indexed text records, not media files.

## What we have (indexed records by kind and section)

| Kind | Sections | Records |
|---|---|---:|
| bootcamp | LR | 83 |
| lecture | LR | 26 |
| lecture | LR+RC | 4 |
| lecture | RC | 81 |
| notes | LR | 20 |
| notes | LR+RC | 2 |
| notes | RC | 46 |
| prep-map | LR+RC | 67 |
| question | LR | 5015 |
| reference | LR | 45 |
| reference | LR+RC | 58 |
| reference | RC | 24 |
| routine | LR | 4 |
| routine | LR+RC | 49 |
| routine | RC | 5 |
| workout | LR | 23 |
| workout | LR+RC | 41 |
| workout | RC | 20 |

Total indexed records: **5613**.

## Lecture packages by source generation

Each lecture package is one folder. Different generations use different folder conventions; the identity `loophole:<kind>:<generation>:<folder-slug>` is stable across them.

| Generation | Folder convention | Packages | Video | Audio | Captions | Written notes | Lecture quiz |
|---|---|---:|---:|---:|---:|---:|---:|
| RC course-day capture (Days 1-3, 6, 7) (`rc_course_day_2026-10-14`) | folder = Loophole Lecture/Day <N>/<title> | 59 | 59 | 59 | 59 | 28 | 0 |
| Conditional native lecture batch (`conditional_native_2026-10-18`) | folder = Loophole Lecture/Conditional Reasoning 2026-10-18/<title> | 26 | 26 | 26 | 26 | 20 | 26 |
| RC activity/demo native batch (`rc_activity_native_2026-10-18`) | folder = Loophole Lecture/RC Activity Demos 2026-10-18/<title> | 25 | 25 | 25 | 25 | 20 | 0 |
| How to Camo transcript-only capture (no media) (`camo_transcript_only_2026-10-15`) | folder = Loophole Lecture/Camo | 1 | 0 | 0 | 0 | 0 | 0 |

## Where each content type lives

| Content | Navigation hub | Original files |
|---|---|---|
| RC lectures (course days) | [reading-comprehension](reading-comprehension/README.md) | `Loophole Lecture/Day <N>/<title>/` |
| RC activities and demos (Caffeinated, Party Tricks, Reverse Shuffle, Camo, Mission Matching, Jail, failsafes) | [activity-demos](reading-comprehension/activity-demos.md) | `Loophole Lecture/RC Activity Demos 2026-10-18/<title>/` |
| Conditional reasoning lectures and attached quizzes | [conditionals](logical-reasoning/conditionals/README.md) | `Loophole Lecture/Conditional Reasoning 2026-10-18/<title>/` |
| Other LR topics | [logical-reasoning](logical-reasoning/README.md) | recovered references under `raw/sources/old-obsidian-vault-2026-10-07/Clippings/loophole-online/` |
| Shared methods (Camo, RTQ, vocabulary, review) | [shared](shared/README.md) | linked per method |
| Workouts (84) | [workouts](workouts/README.md) | `corpus/loophole-online/workouts/<slug>/` |
| Routines (58) | [routines](routines/README.md) | `corpus/loophole-online/routines/<slug>/` |
| Book Extras Bootcamps | [bootcamps](bootcamps/README.md) | `corpus/loophole-online/bootcamps/<chapter>/<slug>/`; evidence in `raw/sources/loophole-bootcamps-2026-10-18/` |
| LR question records, MP3s, transcripts | [question-database](question-database/README.md) | `corpus/loophole-online/question-database/library/PT<n>/S<n>/Q<n>/` (Git-ignored) |
| Every retained source with hashes | [source catalog](source-catalog.generated.md) | per row |

## How to open a complete source

```powershell
python system/scripts/query-loophole.py search "<words>" --section LR|RC|shared --kind <kind> --limit 5
python system/scripts/query-loophole.py open "<title, identity or citation>"
```

`open` lists every companion artifact in the package with its role (video, audio, captions, rendered transcript, written notes, book excerpt, attached quiz, frames, provenance, hashes) and the evidence status. Presence is checked by exact path, never inferred from `rg --files`, which skips ignored media.

## What is missing or qualified

| Item | Status | Meaning |
|---|---|---|
| RC question database | not captured | The question database is LR only. RC questions appear only inside lectures and demos. |
| Course Days 4 and 5 | not captured | No RC course-day folders exist for Days 4 and 5. |
| Day One written notes (10 of 11 lectures) | not checked | Only the Decaf notes were recovered; the rest are labeled not checked, not absent. |
| How to Camo (2026-10-15 generation) | transcript only | Loophole Lecture/Camo has no media. The 2026-10-18 RC activity package holds video, audio and notes. |
| RC activity demo inline quizzes | uncaptured | Attached quiz attempts were not captured; status is uncaptured, not absent. |
| Bootcamp feedback branches | observed only | Only response branches that were actually clicked are captured. |
| Gated external LSAT stimuli | gated | Some Bootcamp and book-excerpt stimuli were behind access gates and are recorded as unavailable. |
| LR question stimuli and answer choices | outside capture | Question records hold citations, Correct CLIR and recordings, not official question text. |
| Conditional quiz with stale feedback | unverified original | One historical attempt shows feedback attributed to the wrong selection; the final correct answer was verified separately. |
| Automatic captions and machine transcripts | unreviewed | Fully extracted but not checked word by word against audio. |
| Prep-map source errors | source error | 33 of 67 prep-map URLs returned errors on the source site; they are recorded, not reconstructed. |

Lecture packages without a local video file: How to Camo (`camo_transcript_only_2026-10-15`).
