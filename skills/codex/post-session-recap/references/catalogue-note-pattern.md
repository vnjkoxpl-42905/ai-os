# Catalogue note pattern

Use this when the session taught a **set of named things** the student has to recognize: famous flaws, question types, conditional patterns, method-of-reasoning moves. A note on one idea uses the progression in the [quality bar](lesson-quality-bar.md) instead. A session can need both: a short concept note, then a catalogue as the reference beside it.

## The model

Ore's **Famous Flaws** guide, posted 2026-11-16. File: `students/ore/assignments/2026-11-16-famous-flaws.html`, Classroom item `c14d048e-eff2-46b8-88ae-bc22246f3ad2`. Marker `ore-2026-11-11-famous-flaws`, 455 KB, ten lessons, 30 practice cards.

How this was judged (2026-11-17): the text of the saved HTML was read in full against the transcript-grounded source map. The rendered page was **not** re-inspected in that pass, so the visual claims below come from the build log (verifier 34/34 at 1280 px and 375 px), not from a fresh look. Re-inspect the render before copying any visual decision.

## What makes it good

1. **One panel layout, repeated for every item, in the same order.** The reader learns the layout once, then spends all their attention on the content. The order is:
   Example → Evidence and conclusion → Why the reasoning fails → What follows (the visual) → How it appears on the LSAT → What would strengthen or weaken it.
2. **Everyday examples, not the test stimulus.** Mina and the doctor's note, the marbles from the top of the jar, the riverbank and the bank. The test's abstract answer wording is kept apart under a label ("Illustrative answer-choice wording"), so the student sees the idea first and the disguise second.
3. **The evidence is split from the conclusion.** Each panel names the premises and the conclusion separately, then says what is missing between them. The student sees the gap before they see the label.
4. **Every explanation names the story that defeats it.** Not "this is flawed" but "Mina might have been excused for a family emergency", "if the jar was filled in layers, the top could be entirely red". A specific counterexample is the lesson.
5. **Valid and invalid moves side by side.** The necessary versus sufficient panel shows the given conditional, the invalid reversal, the invalid negation and the valid contrapositive, each with one sentence of why.
6. **It says where the flaw stops.** "Shared vocabulary alone does not make an argument circular." "A survey can still be good evidence." "Two speakers disagreeing is different from one speaker committing to incompatible claims." These boundaries are what keep a student from over-naming flaws.
7. **It ties each flaw to the question types.** The closing lines say what evidence would strengthen, what would weaken, and what the argument must assume. This is what turns a vocabulary list into a method.
8. **Contrasts between neighbours.** Sampling versus composition. Discrediting an argument versus proving a claim false. These are where students actually confuse the items.
9. **Practice sits in the page.** Name-the-flaw cards with a shown answer and explanation, mark for review, and shuffle. The page also opens with a two-tier map ("five foundations", "five more") so ten items do not read as a flat list.
10. **It stays one file.** Under 500 KB, inline fonts and script, a stable `lsatu-interactive-lesson` marker. It posted and verified without a workaround.

## The process that produced it

The note was good because the work before the HTML was done, not because of the HTML.

- **A private source map first** (`brainstorms/2026-11-11-ore-post-session/PRIVATE-source-map.md`). Headings: Tags (from `wiki/homework-assigning/taxonomy.md`), Source map (governing concept, the student's actual sticking point, Joshua's answer, valid moves, her words with timestamps), Commitments (who, what, timestamp), Reuse (closest earlier notes and what was kept or dropped), Corrections and cautions, Not done.
- **Transcript errors were caught, not copied.** The Gemini summary said "over 50% of LSAT logic sections"; the transcript said over half of *flaw questions*. The note used the transcript. An unverifiable claim from Joshua ("the most common questions on the LSAT, period") was left out and logged.
- **A plan with acceptance criteria** (`PLAN-famous-flaws.md`): panel parts per item, a coverage check against the source list, size, banned words, no em dashes, desktop and 375 px, keyboard use. A second reviewer round found real defects (only 11 of 15 entries had a "what if" counter in the source).
- **A closed list of permitted changes** from the source wording. Everything else stayed verbatim.
- **A read-through for logic**: each example and explanation was tested with a counterexample.

## Use it for the next catalogue note

1. Write the private source map first. Stop and resolve any claim you cannot ground in the transcript or corpus.
2. Decide the scope out loud: which items this note covers and which it leaves out, and why. Say that on the cover (the Ore note says "ten" and links the rest). A student should never wonder whether an item was forgotten.
3. Group the items into two or three tiers, the ones the session actually taught first.
4. Write one panel per item in the fixed order above. Use a fresh everyday example for each. Keep the test's wording in its own labelled block.
5. For each item, write the counterexample sentence, the boundary sentence, and the question-type sentence. If one is missing, the item is not finished.
6. Add a contrast line wherever two items get confused.
7. Add name-it practice cards, three per item, with answer-specific explanations.
8. Run the [quality gate](lesson-quality-bar.md#before-handoff) plus the checks below.
9. Plan the homework from [notes and homework package](notes-and-homework-package.md): the catalogue is the reference note, and the guided drills practise the same items.

## Checks specific to a catalogue note

- Every item has all six panel parts. Count them; do not trust a skim.
- Every example is independent of the original test question and passes a counterexample attempt.
- Each item's answer-choice wording is labelled as illustrative, not quoted as a real question.
- The scope line names what is out.
- Any item the transcript never taught is marked as extra, not presented as something the session covered.
- Outside material is credited accurately. The Ore guide includes a conditional logic walkthrough credited to an outside teacher. Confirm the credit and permission before reusing that block, and never present outside prose as Joshua's.
- Arguable examples are flagged to Joshua. The Internal Contradiction example in the 15-flaw build was kept verbatim but a reviewer called it arguable (Codex FF-003). Say so in the handoff instead of choosing silently.
- Rule-of-thumb figures from Joshua (such as "99.9%") are kept as his words and marked as unverified.
