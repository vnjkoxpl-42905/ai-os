---
type: teaching-notes
subject: Read-aloud lecture archive
created: 2026-09-30
updated: 2026-09-30
aliases: []
tags: [lsat, lectures, teleprompter]
---

# Lectures ready to teach

Each lecture package keeps the source transcript, read-aloud script, visual timeline, and board/question captures together. The script retains the source's instructional sequence and teaching detail while removing names, attendance chatter, and class logistics. Spoken words and unspoken display cues are separate.

## LSAT Lab

| Topic | Source | Package status |
|---|---|---|
| Must Be True | [Patrick Tyrrell, 2026-08-27, video 33013](https://app.lsatlab.com/video-library/?videoid=33013) | [Read the lecture](lsat-lab/must-be-true/2026-08-27-33013/teleprompter.html). Full automated captions, opening boards, five worked questions, cleaned script, and [coverage/corrections](lsat-lab/must-be-true/2026-08-27-33013/coverage.md). |

Concept tags: contrapositives, linking conditional rules, applying facts to rules, illegal reversal, illegal negation, AND/OR, quantifier scope, inference pivots, numerical boundaries, requirement language, and passive voice.

## Package layout

`lsat-lab/<topic>/<lecture-date>-<video-id>/` holds:

- `transcript.md`: faithful timestamped source text, with raw evidence and hash references.
- `teleprompter.md` and `teleprompter.html`: read-aloud script with adjacent images and unspoken cues.
- `screenshots/`: initial teaching board, every worked question, and important annotated board states.
- `timeline.json`: source ranges, concepts, question identifiers when verified, script segments, and visual links.
- `coverage.md`: full-lecture concept/question coverage, intentional cuts, and unresolved gaps.

Original captures are preserved separately under `raw/sources/lsat-lab-lectures/<video-id>/` with provenance and hashes. Corrections do not overwrite source evidence. No lecture is marked complete until the full transcript and every worked question have been checked.

Detailed categorization follows Joshua's instructions. The initial classification uses the platform and lecture topic only.
