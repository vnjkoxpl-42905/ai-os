# Post-session note format comparison

Status: prototypes for Joshua's review. Nothing in this folder has been posted or adopted as the recurring format.

## Source and settled choices

- Working session: Charles Moore, 2026-09-25. Joshua accepted using the recommended real-session example.
- Source: `students/charles-moore/sessions/2026-09-25-quantity-logic/transcript.md`.
- Compare a concise reference, a full lesson, and a lesson with self-checks.
- Keep the existing primary recap at `students/charles-moore/recaps/2026-09-25-recap.md` intact while choosing a format.
- All three versions are student-facing drafts. They omit private teaching and scheduling follow-ups except the student action to text about a Friday time.

## What each version tests

| File | Design choice | Main tradeoff |
|---|---|---|
| `01-concise-reference.md` | Quick reference with compressed explanations | Easiest to scan; leaves fewer worked reasons to revisit later. |
| `02-full-lesson.md` | Standalone lecture note with worked reasons and cases | Strongest as a durable teaching resource; longest to read. |
| `03-guided-self-checks.md` | Short explanations followed by try/check prompts | Encourages active recall; repeated prompts may interrupt reference reading. |

## Accuracy checks

- The spoken session includes a reversed verbal description of the quantity hierarchy. The drafts use the valid entailment: all → most → some, assuming the starting group exists.
- The spoken session also suggests carrying a `some` group through a `most` claim. That inference is not guaranteed, so the drafts teach the boundary explicitly.
- “Most” means more than half, with the whole-number threshold depending on group size.
- The banjo/guitar total-size conclusion follows from comparing the same overlap against the two starting groups.
- The assigned work is limited to finishing conditional drills. Quantity drills and a visual aid were Joshua's promised follow-ups, not completed student assignments in this transcript.

## Decisions still open

- Which version, or combination, should define the recurring student-facing format?
- Should self-checks show answers immediately, use a separate answer key, or be omitted?
- Does “interactive” mean prompts within a static page note or clickable platform behavior?
- How much of a session's secondary topic belongs in the note when one topic dominates?

These are reversible format choices, so no ADR is needed. Once Joshua chooses, update the existing `session-recap` skill and its quality reference instead of adding a parallel rule.
