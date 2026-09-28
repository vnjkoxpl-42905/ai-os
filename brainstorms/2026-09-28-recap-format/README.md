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
| `04-visual-lesson.md` | Cookie examples, count ranges, and a one-way implication diagram before the later inferences | More intuitive entry point; the images need a usable URL when posted. |
| `05-concept-and-arrow-lesson.md` | Concept-only explanation of ranges, arrow directions, and the inference patterns that do and do not work | Best match for the latest direction; longer because it explains the boundaries of each rule. |

## 2026-09-28 wording and visual revision

Joshua rejected “starting group” as an unexplained term. The fourth draft asks “What are we counting?” and defines some, most, and all individually before using them in inferences. It distinguishes a permitted count from a guaranteed count, uses a 10-cookie range chart and concrete examples, and shows all → most → some as a one-way guarantee.

Joshua then clarified that the note should teach concepts, not revisit the banjo question. The fifth draft removes that question and the scheduling/conditional-indicator detours. It covers the quantity meanings, reversals, conditional interpretation of “all,” valid chaining, invalid chaining, and the two-majority overlap. Its diagrams show the arrow directions and why two majorities of the same group intersect.

Joshua rejected the fifth draft's abstract opening, “how much of a group fits a description,” and asked for his teaching voice throughout. The revised fifth draft opens with the ten cookies and direct definitions, removes repeated summary language, and explains each inference by asking what the statement actually proves. Keep future notes concrete and direct; do not lead with invented umbrella descriptions of the concept.

The student Classroom page renders `content_markdown` as plain text. Formatted posts use sanitized `content_html`; tables and HTTPS image URLs are supported there. Keep Markdown as the editable source, convert it to HTML for posting, and host the visual assets at usable HTTPS URLs. Relative image paths in this draft are for local review and will not by themselves display on the student page.

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
