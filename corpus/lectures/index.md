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

## Choose a section

| Section | Archive |
|---|---|---|
| Logical Reasoning | [Topics, core lectures, and advanced lectures](logical-reasoning/index.md) |
| Reading Comprehension | [Topics and lecture levels](reading-comprehension/index.md) |

Concept tags: contrapositives, linking conditional rules, applying facts to rules, illegal reversal, illegal negation, AND/OR, quantifier scope, inference pivots, numerical boundaries, requirement language, and passive voice.

## Find a lecture by concept

| Search phrase | Tag | Lecture preparation |
|---|---|---|
| Applying facts to rules | `fact-triggers-rule` | [Before teaching: Core Must Be True](logical-reasoning/must-be-true/core/2026-08-27-33013/teaching-brief.md) |
| Linking rules | `conditional-linking` | [Before teaching: Core Must Be True](logical-reasoning/must-be-true/core/2026-08-27-33013/teaching-brief.md) |
| Inference family | `inference-family` | [Before teaching: Core Must Be True](logical-reasoning/must-be-true/core/2026-08-27-33013/teaching-brief.md) |
| Conditional logic | `conditional-logic` | [Before teaching: Core Must Be True](logical-reasoning/must-be-true/core/2026-08-27-33013/teaching-brief.md) |
| Contraposition | `contrapositive` | [Before teaching: Core Must Be True](logical-reasoning/must-be-true/core/2026-08-27-33013/teaching-brief.md) |

## Package layout

`<logical-reasoning-or-reading-comprehension>/<topic>/<core-or-advanced>/<lecture-date>-<video-id>/` holds:

- `transcript.md`: faithful timestamped source text, with raw evidence and hash references.
- `teleprompter.md` and `teleprompter.html`: read-aloud script with adjacent images and unspoken cues.
- `screenshots/`: initial teaching board, every worked question, and important annotated board states.
- `timeline.json`: source ranges, concepts, question identifiers when verified, script segments, and visual links.
- `coverage.md`: full-lecture concept/question coverage, intentional cuts, and unresolved gaps.

Original captures are preserved separately under `raw/sources/lsat-lab-lectures/<video-id>/` with provenance and hashes. Corrections do not overwrite source evidence. No lecture is marked complete until the full transcript and every worked question have been checked.

Each folder level has an `index.md`. Topics may be question types, question families, or reasoning skills. A lecture has one canonical home; overlapping topics use links and tags. Core/advanced describes its archive placement, not the difficulty of every question inside it. Platform and instructor remain lecture metadata rather than an extra routing layer.
