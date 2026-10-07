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
|---|---|
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

## Call up a lecture during preparation

Ask: "Open the Core Must Be True lecture," "Use the lecture on applying facts to rules," or "Find the lecture on linking rules." Follow the concept links above for preparation, then open the lecture's `teleprompter.html`. The files are saved in this second brain; the localhost URL is a viewing convenience and may need its local server restarted after a reboot.

The teleprompter is a private teacher guide. Read SAY and ASK aloud. WAIT tells you when to pause; EXPECTED RESPONSE gives private answer guidance and likely wrong turns. BOARD and QUESTION copy only the material you need for the whiteboard. Next up previews the following moment, and Read ahead lets you inspect the upcoming sequence. Advance manually when the student is ready. The continuous script remains available when you want to read the whole lesson before teaching.

## Files kept with each lecture

`<logical-reasoning-or-reading-comprehension>/<topic>/<core-or-advanced>/<lecture-date>-<video-id>/` holds:

- `transcript.md`: faithful timestamped source text, with raw evidence and hash references.
- teleprompter.html: private teacher view with short spoken passages, Socratic guidance, previews, and copy controls.
- lesson-steps.json: ordered teacher cues, questions, expected reasoning, likely mistakes, and follow-up prompts.
- teleprompter.md and full-script.html: continuous reading script with images and unspoken cues.
- `screenshots/`: initial teaching board, every worked question, and important annotated board states.
- `timeline.json`: source ranges, concepts, question identifiers when verified, script segments, and visual links.
- `coverage.md`: full-lecture concept/question coverage, intentional cuts, and unresolved gaps.

Original captures are preserved separately under `raw/sources/lsat-lab-lectures/<video-id>/` with provenance and hashes. Corrections do not overwrite source evidence. No lecture is marked complete until the full transcript and every worked question have been checked.

Each folder level has an `index.md`. Topics may be question types, question families, or reasoning skills. A lecture has one canonical home; overlapping topics use links and tags. Core/advanced describes its archive placement, not the difficulty of every question inside it. Platform and instructor remain lecture metadata rather than an extra routing layer.
