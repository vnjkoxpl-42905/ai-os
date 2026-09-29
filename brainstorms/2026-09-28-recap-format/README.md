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
| `05-concept-and-arrow-lesson.md` | Concept-only explanation of ranges, arrow directions, and the inference patterns that do and do not work | Earlier concept draft, before the source-informed reorganization. |
| `06-some-most-all-note.md` | Teaches some, then most, then all individually before comparison, chaining, and overlap | Earlier working draft based on Joshua's supplied PDFs and screenshots. |
| `07-quantity-statements-lesson.md` | Opens with the purpose of quantity statements, teaches each word with a new book example and visual, then adds inference checks and a cumulative drill | Current reviewed draft. Keeps the group-size comparison as a short extension. |
| `08-quantity-statements-visual-preview.html` | Interactive local LSAT U Classroom presentation of draft 07 | Book-count experiment, movable majority-overlap diagram, seven short-answer inference checks with worked feedback, figure captions, and a final worksheet. No student post. |

## 2026-09-28 wording and visual revision

Joshua rejected “starting group” as an unexplained term. The fourth draft asks “What are we counting?” and defines some, most, and all individually before using them in inferences. It distinguishes a permitted count from a guaranteed count, uses a 10-cookie range chart and concrete examples, and shows all → most → some as a one-way guarantee.

Joshua then clarified that the note should teach concepts, not revisit the banjo question. The fifth draft removes that question and the scheduling/conditional-indicator detours. It covers the quantity meanings, reversals, conditional interpretation of “all,” valid chaining, invalid chaining, and the two-majority overlap. Its diagrams show the arrow directions and why two majorities of the same group intersect.

Joshua rejected the fifth draft's abstract opening, “how much of a group fits a description,” and asked for his teaching voice throughout. The revised fifth draft opens with the ten cookies and direct definitions, removes repeated summary language, and explains each inference by asking what the statement actually proves. Keep future notes concrete and direct; do not lead with invented umbrella descriptions of the concept.

Joshua supplied `Quantifier Math Takeaways.pdf`, `Quantifiers_Diagram.pdf`, and three screenshots on 2026-09-28. The sixth draft uses their core models: some is reversible, most is directed and yields some in reverse, all is a conditional, a second all-rule carries the first quantifier forward, and two most claims about the same group force a some overlap. It also explains the rarer group-size comparison without revisiting the banjo question. The diagrams are teaching references, not student-note instructions. The supplied shared-start all + all diagram needs an existence premise before it can establish some; the draft does not copy that inference without the premise. Ambiguous synonyms such as “often” and “can be” are also omitted because their meaning depends on context.

Joshua's next design direction: introduce quantity statements generally before teaching Some, Most, and All individually. In each section, explain the idea and then use an example and visual. Only after the three sections should the note teach combined inferences and overlap. Students should answer questions as they go, not only at the end. The corpus index marks Quantifiers as an unfilled lesson; the relevant conditional-logic notes confirm the arrow language, while the Valid Conclusion homework models a pause-and-answer rhythm.

Joshua supplied a photographed Some & Most textbook page as a writing and structure reference. Its useful sequence is orientation and stakes → direct definition → one fixed-size example with all permitted counts → transition to diagramming → a question about why the arrows differ → explanation → worked application. Its connected prose explains why each visual appears, rather than placing diagrams as decoration. For Joshua's note, use that teaching sequence and sentence rhythm without copying its “rogue sufficients” metaphor, exclamations, or book-specific vocabulary. The page's 1%-to-100% and 51%-to-100% shortcuts are imprecise for its five-cookie example; write “at least one” and “more than half,” then calculate the actual whole-number counts. The current sixth draft opens with cookies before orienting the reader to quantity statements; that opening remains to be revised after the interview decisions settle.

Joshua supplied five more photos from the same chapter. The sequence now visible is: define and diagram each quantifier; explain the arrow with one worked sentence; draw out the less obvious reverse implication of Most; show valid inference patterns beside tempting invalid ones; compress the lesson into a short game plan; finish with a cumulative drill. The photographed drill asks for original diagrams and contrapositives where applicable, then combines statements into chains and asks which chain warrants an inference. The useful writing pattern is connected, conversational explanation interrupted by small headings, diagrams, callouts, and a question immediately before the reasoning that answers it. Use original examples and prose in Joshua's voice, rather than the textbook's jokes or exact wording. Joshua explicitly wants a short drill at the end in addition to questions during the lesson. The drill should test the same moves the note just taught and include an answer explanation.

Joshua approved a purpose-first introduction, asked for an example other than cookies, approved the cumulative drill, and accepted keeping the rarer group-size inference as a short extension. Draft 07 uses eight books for the basic quantity ranges, library books for all-rule chains, club members for shared-group overlap, and volunteers for the final five-statement drill. Inline answer reveals are provisional until the Classroom rendering is verified. The new SVGs in `assets/` are local draft visuals, not hosted student-page assets.

Joshua corrected the draft 07 opening: define quantity statements in the first sentence, give an intuitive example before the books, and do not mention combining statements before that concept has been taught. The revised opening uses a class assigned a case and compares “some,” “most,” and “all” about the same class before asking what each sentence requires or permits.

Joshua then asked to see the note in the LSAT U page frame and found the first rendered preview too uniform. Draft 07's source remains intact. The second local preview, generated by `build-preview-08.mjs`, uses the Classroom CSS, pairs an editorial serif reading face with LSAT U's Outfit headings, puts the three class claims on separate rows, makes the two guiding questions a distinct panel, adds jump links, gives the try/check prompts their own visual treatment, and sets the final drill apart as a worksheet. Checked in Chrome at desktop and 430px mobile width: all six visuals loaded, six native answer reveals were present, the first opened, and no horizontal overflow was observed. This is still a local visual study; hosted images and sanitized production rendering have not been tested.

On 2026-09-29 Joshua asked for the entire note to be more visually alive and for the seven-item pop quiz to accept short answers. The local preview now has a widened lesson canvas, an eight-book threshold slider, a ten-member overlap experiment, distinct concept colors, figure captions, and a seven-step typed-answer sequence. The quiz checks only the student's yes/no conclusion, then reveals the worked reason for self-comparison; it does not grade free-form reasoning. Motion accompanies state changes and stops under reduced-motion preference. The Markdown source remains the static fallback and carries the full seven-question answer key. Browser checks covered the slider thresholds, overlap rearrangements, all seven quiz answers, invalid input, incorrect verdict feedback, mobile layout, and image loading. The existence check was corrected to use abstract A/B/C because the earlier club example had already established members.

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
- How should the interactive lesson be implemented in LSAT U when Joshua approves publishing it? The current Classroom note renderer sanitizes HTML, so the prototype's script needs an app feature rather than a pasted note.
- How much of a session's secondary topic belongs in the note when one topic dominates?

These are reversible format choices, so no ADR is needed. Once Joshua chooses, update the existing `session-recap` skill and its quality reference instead of adding a parallel rule.
