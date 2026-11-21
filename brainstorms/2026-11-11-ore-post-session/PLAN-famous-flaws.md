# Plan: the Famous Flaws note, built properly

Status: draft plan. Nothing is built. Roles: Claude plans and coordinates, Codex (GPT-6 Astra) builds, Claude inspects, then a fresh Codex session inspects Claude's edits.

## Goal

One self-contained LSAT U note titled **Famous Flaws** that presents Joshua's full list of 15 famous flaws with nothing simplified, shortened or skipped, in a look that matches his own Famous Flaws catalog design. Every flaw gets a full breakdown and its own visual. The note is a draft for one student; nothing is posted or assigned.

The three earlier variations (`famous-flaws-v1..v3`) are rejected as too thin. They stay on disk untouched.

## What "my Famous Flaws list" is (sources, in priority order)

1. `raw/sources/lsat-curriculum/_stragglers/recovered-ai-gather/Claude 2/02_PROJECTS/Curriculum/Curriculum/Flaw and Famous Flaws/_HANDOFF/05_compiled_content_voiced.md`, **Note 2 Famous Flaws Catalog**, lines 372 to 785. The canonical content. Its own rule: render near-verbatim, do not edit for tone, do not flatten the voice.
2. Same folder, `03_design_artifact.html`, sections 3, 6, 7 and 11 (Cake-on-Blocks, Filterable Catalog, Disambiguation Matrix, Wall of Worked Examples). The canonical look.
3. `lsatu/src/bootcamps/fallacy-flaw-v2/data/flaws.ts`: the app's version of the same list (14 entries, slightly different wording, adds `everydayWording` and `abstractWording`). Use only to fill a gap, never to override source 1.

The list: **15 flaws in 3 groups.**
- Group 1, usually the real flaw (6): Necessary vs. Sufficient, Causal, Part vs. Whole, Unproven vs. Proven False, Ad Hominem, Sampling.
- Group 2, usually the trap (4): Circular Reasoning, Internal Contradiction, Equivocation, Inappropriate Appeal.
- Group 3, named by Joshua (5): Sleight of Hand, Sleazy Sales Pitch, Universal Desires Assumption, Value Assumptions, Secret Downsides.

Source 1 carries **68 answer-choice phrasings** (6, 6, 5, 5, 5, 6 | 4, 3, 4, 4 | 5, 4, 4, 4, 3) and a **10-row Disambiguation Matrix**, plus **5 disguise mechanics**. The matrix and the mechanics are marked "Invented" in the source file: written in the earlier build, not Joshua's own words.

## Per-flaw breakdown (every one of the 15, no exceptions)

Each flaw gets one panel with these parts, all taken from source 1 with its wording kept:

1. Group tag and frequency line (for Group 2 the "right-answer frequency").
2. Definition.
3. Stimulus tells.
4. Answer-choice disguises: every phrasing, as a list, none dropped.
5. Canonical worked example, with the explanation that follows it in the source.
6. The "What if" counter.
7. Disambiguate from: each confusion pair, with its question.
8. "When it IS the right answer" where the source gives it (Groups 2 and the entries that have it).
9. One visual, specific to that flaw (list below).

## Visuals

All inline SVG or CSS, no external files, each with alt text and a reduced-motion fallback.

| Flaw | Visual idea |
|---|---|
| Necessary vs. Sufficient | Two nested sets, "enough" inside "required", with the backwards arrow struck out |
| Causal | The three stories fit one fact: A causes B, B causes A, a third factor C drives both, plus coincidence |
| Part vs. Whole | A team of stars and a team: pieces versus the thing they make, both directions |
| Unproven vs. Proven False | A two-state meter: "nothing shown" versus "shown false" |
| Ad Hominem | An arrow aimed at the speaker (wrong target) versus at the claim (right target) |
| Sampling | A population field with a small clustered sample and a mismatch marker |
| Circular Reasoning | A loop: conclusion feeds the premise that feeds it |
| Internal Contradiction | Two statements joined by a "cannot both hold" bar |
| Equivocation | One word splitting into two meanings, one path per meaning |
| Inappropriate Appeal | An authority badge that does not match the topic |
| Sleight of Hand | Premise term and conclusion term with a ≠ between them (Joshua: "put a ≠ between them") |
| Sleazy Sales Pitch | A one-sided scale: what is shown versus the two hidden pans |
| Universal Desires Assumption | A crowd where most want the goal and a few visibly do not |
| Value Assumptions | A fact stepping across a gap to a loaded word |
| Secret Downsides | Visible benefit above the waterline, hidden cost below |

Page-level visuals, from his design artifact: the Cake-on-Blocks validity model near the top (click "Object: what if" and the blocks separate), the 15-card group-coloured grid with filter chips (All, Group 1, Group 2, Group 3), and the Disambiguation Matrix with each question set as a pink margin prompt.

## Look

Recommended: keep the approved Lanae shell as the base (embedded Outfit and Fraunces, warm paper ground, numbered sections), and add an **additive Famous Flaws layer** in a second `<style>` block appended after the shell's own. The shell's CSS and script stay untouched. The layer carries his catalog design: group colours (Group 1 green, Group 2 gold, Group 3 purple, as in the design artifact), the card grid, expandable panels, the matrix table and the pink margin questions. Fonts stay Outfit and Fraunces so the file stays under 500 KB without new font downloads.

## Page order

1. Hero: title, the one-paragraph explanation of what a flaw question asks, the 15 / 3 / 6-4-5 counts.
2. How to use it: name the flaw before the choices, find it, then read the choices.
3. Cake-on-Blocks visual.
4. The 15-card grid with filters. Each card opens its full panel (collapsed by default so the page stays readable; nothing is removed).
5. The five disguise mechanics (from the source's Disguise Library), each with its examples.
6. The Disambiguation Matrix, 10 rows, with a forced-choice check for each row.
7. A short "say it first" check per flaw with an original example, labelled as new.
8. "What to do next".

The session-specific part (the recap kicker, "in our session" markers on the four flaws that were taught, the student's own words, the study tasks) is added by Claude afterwards, not by Codex. Codex builds a student-neutral note with named slots for it.

## Work packages (one Codex build session, in order)

| # | Package | Output |
|---|---|---|
| WP1 | Data layer: parse source 1 into structured data for all 15 flaws, 68 disguises, 10 matrix rows, 5 mechanics, applying the adaptation rules below | `flaws.data.json` and `verify-coverage.mjs` |
| WP2 | Visual system: additive CSS layer, 15 SVGs, Cake-on-Blocks, accessibility and reduced motion | `famous-flaws.layer.css`, `svg/` |
| WP3 | Page assembly from the Lanae shell plus data, with session slots | `build-famous-flaws-full.py`, `famous-flaws.html` |
| WP4 | Interactions: filters, panel open/close, the matrix forced-choice check, per-flaw checks with original examples | inside the build script |
| WP5 | Verification harness: validator, size, dashes, banned words, coverage, Playwright desktop and 375 px, interaction tests, screenshots | `verify-all.mjs`, `previews/` |
| WP6 | Claude only: session slots, voice read-through, claim audit, review fixes | final `famous-flaws.html` |

Codex works in an isolated folder holding only the shell, the compiled catalog, the design artifact and the app's `flaws.ts`. It gets no student records. Its output is copied to `brainstorms/2026-11-11-ore-post-session/`.

## Adaptation rules (what may change from the source, and nothing else)

- "Joshua-Named" becomes "Named by me": the note is in his first person.
- Internal references leave the student copy: "Trap Pattern 4", "Trap 5 from section 5", "Cross-link: the Causation module", slugs, and PrepTest cites in the examples. Where a cite carried meaning, replace it with a plain description.
- Real public figures in examples become roles (for example "the government's leading infectious-disease expert"). The reasoning in the example is unchanged.
- No em-dashes (the source uses them; replace with a period, colon or the middle dot).
- Banned words and the "note" naming rule from `note-formula.md` apply.
- Everything else (definitions, tells, all 68 disguise phrasings, worked examples, counters, the matrix questions) is kept word for word.

## Acceptance criteria

1. Exactly 15 flaw panels, each with all nine parts listed above present.
2. Coverage check passes: all 15 definitions, 68 disguise phrasings, 15 worked examples, 15 "What if" counters and 10 matrix rows from the source appear in the output after the permitted adaptations. The script reports counts and any mismatch.
3. 15 distinct SVGs, each with alt text. No two panels share a visual.
4. The shell's CSS and script are byte-identical to `note-shell.html`; the layer is a separate appended block.
5. `lsatu-lesson-validate.mjs` passes. No external file or font link. Total size under 500 KB.
6. Zero em-dashes or en-dashes in student-visible text, and none of the banned words.
7. Playwright at 1280 px and 375 px: no horizontal page overflow, all three fonts loaded, no console errors, filters and panels and the matrix check work with the keyboard.
8. Claude's read-through finds no claim in the examples or explanations that fails a counterexample test.

## Verification commands

- `node C:/Users/Joshu/dev/ai-os/brainstorms/2026-11-11-ore-post-session/verify-all.mjs` runs everything above and prints a table.
- Independently, Claude runs the validator and its own Playwright pass and reads the screenshots.

## Non-goals

- No posting, assigning or messaging.
- No edits to the shell, the earlier variations, the corpus or the app.
- No paste-an-answer-choice tool (the source's Stage 3 idea). Out of scope for a note.
- No new font downloads.

## Open decisions (each has a recommendation)

1. **Look.** Recommend: Lanae shell plus the additive Famous Flaws layer above. Alternative: rebuild in his design artifact's own fonts (Newsreader, Spectral, JetBrains Mono). That needs three font downloads and probably breaks the 500 KB limit.
2. **One page or three.** Recommend one page with collapsed panels. Alternative: three notes by group, which fits the usual package of three.
3. **The "Invented" parts.** The matrix and the five mechanics were written in the earlier build, not by Joshua. Recommend including both, and Joshua reads them before anything is posted.
4. **Matrix drill stimuli.** The source says to draw them from his Fallacy Homework, which lists only PrepTest cites, not the text. Recommend original short stimuli, labelled as new, until real question text is supplied.

## Risks

- The Causal entry says the inference is wrong "99.9% of the time". That is his rule of thumb. It is kept as written and cannot be verified.
- Total content is about 6,000 words, three times the 2,100-word upper bound in `note-formula.md`. Collapsed panels are the mitigation. If he wants it shorter, the split in decision 2 is the way.
- The worked examples come from the source and their original questions cannot be checked here.
