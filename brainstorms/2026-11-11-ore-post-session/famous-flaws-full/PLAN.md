# Build plan: the Famous Flaws note

Status: standalone work order. **Not independently approved**: the Codex plan review returned BLOCKED (its shell could not start), and the owner chose to build anyway. Roles: Claude coordinates and inspects, Codex builds, a fresh Codex session inspects Claude's later edits.

You are building inside this folder only. Do not read or write outside it. No network access is needed or allowed. Never modify anything under `sources/`, `shell/` or `tools/`.

## Goal

One self-contained HTML note titled **Famous Flaws** that presents the full list of 15 famous LSAT flaws with nothing simplified, shortened or skipped, in the look of the owner's own Famous Flaws catalog design. Every flaw gets a full breakdown and its own visual. Output: `out/famous-flaws.html`.

## Inputs (all in this folder, read-only)

1. `sources/05_compiled_content_voiced.md`, section **Note 2 · Famous Flaws Catalog** (from the line `## Note 2 · Famous Flaws Catalog` up to `## Invented · Answer Choice Disguise Library`), plus the two sections after it: `## Invented · Answer Choice Disguise Library` and `## Invented · Flaw vs. Flaw Disambiguation Matrix`. Canonical content. Its own rule: render near-verbatim, do not edit for tone, do not flatten the voice.
2. `sources/03_design_artifact.html`: the canonical look. Open it and study sections 3 (Cake-on-Blocks), 6 (Filterable Catalog), 7 (Disambiguation Matrix) and 11 (Wall of Worked Examples), and its design tokens (`:root` variables).
3. `sources/flaws.ts`: the app's version of the list. Use only to fill a gap, never to override source 1.
4. `shell/note-shell.html`: the base page (embedded fonts, warm paper look, one example of every component).
5. `tools/lsatu-lesson-validate.mjs`: the validator the finished file must pass.

The list: **15 flaws in 3 groups.**
- Group 1, usually the real flaw (6): Necessary vs. Sufficient, Causal, Part vs. Whole, Unproven vs. Proven False, Ad Hominem, Sampling.
- Group 2, usually the trap (4): Circular Reasoning, Internal Contradiction, Equivocation, Inappropriate Appeal.
- Group 3, named by the author (5): Sleight of Hand, Sleazy Sales Pitch, Universal Desires Assumption, Value Assumptions, Secret Downsides.

Source 1 holds **68 answer-choice phrasings** (6, 6, 5, 5, 5, 6 | 4, 3, 4, 4 | 5, 4, 4, 4, 3), a **10-row Disambiguation Matrix** and **5 disguise mechanics**. The matrix and the mechanics are marked "Invented" in the source. Include them, and label each of those two sections in the page with a small, honest note ("Draft section: not yet checked by Joshua") as an HTML comment only, not visible text, so Claude can review it before posting.

Flaw ids to use everywhere (data keys, panel ids, slot names): `necessary-vs-sufficient`, `causal`, `part-vs-whole`, `unproven-vs-proven-false`, `ad-hominem`, `sampling`, `circular-reasoning`, `internal-contradiction`, `equivocation`, `inappropriate-appeal`, `sleight-of-hand`, `sleazy-sales-pitch`, `universal-desires`, `value-assumptions`, `secret-downsides`.

## Decisions already made (do not reopen)

1. **Look:** keep the shell as the base and add an **additive Famous Flaws layer** in a second `<style>` block placed after the shell's own `<style>`. Do not edit one byte of the shell's CSS or script. Fonts stay Outfit and Fraunces (already embedded). No new fonts, no downloads. Use the design artifact's group colours (Group 1 green, Group 2 gold, Group 3 purple, read the exact values from its `:root`), its card grid, filter chips, panel design, matrix table and pink margin questions.
2. **One page**, with all 15 panels collapsed by default and opening on click or keyboard. Nothing is removed to save space.
3. **Invented parts** (matrix, five mechanics): include both in full.
4. **Matrix check and per-flaw checks use short original stimuli** that you write, each labelled "New example" in visible text. Keep them correct: try a counterexample on every one.

## Per-flaw panel (every one of the 15)

Each panel carries every part the source gives for that entry, with its wording kept. What the source gives differs by entry, so the parts are defined per entry. **Do not invent a part the source lacks, and do not drop a part it has.**

Always present (all 15 entries):
1. Group tag and frequency line (Group 2 shows its "Right-answer frequency").
2. Definition.
3. Stimulus tells (including any sub-list under it, for example the three things the Causal author ignores).
4. Answer-choice disguises: every phrasing as a list, none dropped.
5. Canonical worked example, with the explanation that follows it in the source (Sleight of Hand, Sleazy Sales Pitch and Value Assumptions give their example as a described case plus explanation; keep both).
6. One visual specific to this flaw.
7. One "say it first" check with an original example (decision 4).

Present only where the source entry has it:
8. **The "What if" counter**: **11 entries** have it in the source (Necessary vs. Sufficient, Causal, Part vs. Whole, Unproven vs. Proven False, Ad Hominem, Sampling, Sleight of Hand, Sleazy Sales Pitch, Universal Desires Assumption, Value Assumptions, Secret Downsides). The four Group 2 entries (Circular Reasoning, Internal Contradiction, Equivocation, Inappropriate Appeal) have none in source 1. For those four, use the app's `counterQuestion` from `sources/flaws.ts` in the same slot, and record each in `out/adaptations.json` with rule id `R6`. Never present them as source 1 text in any comment or report.
9. **Disambiguate from**: **9 entries** have it, 12 pairs in all (Necessary vs. Sufficient 2, Causal 1, Part vs. Whole 1, Unproven vs. Proven False 1, Ad Hominem 1, Sampling 2, Sleight of Hand 2, Sleazy Sales Pitch 1, Value Assumptions 1). Each pair keeps its question.
10. **When it IS the right answer**: the **4 Group 2 entries** only.
11. **Real LSAT phrase pairs the test exploits**: Sleight of Hand only (5 pairs).
12. The source's "Cross-link" line (Causal) is a permitted omission (rule `R7`).

## Visuals

Inline SVG or CSS only. No external files. Each SVG has a `<title>` and `<desc>` (alt text), uses the group colour, and any motion stops under `prefers-reduced-motion`.

| Flaw | Visual |
|---|---|
| necessary-vs-sufficient | Two nested sets, "enough" inside "required", with the backwards arrow struck out |
| causal | The three stories that fit one fact: A causes B, B causes A, a third factor drives both, plus coincidence |
| part-vs-whole | A team of stars and a team: pieces versus the thing they make, both directions |
| unproven-vs-proven-false | A two-state meter: "nothing shown" versus "shown false" |
| ad-hominem | An arrow aimed at the speaker (wrong target) versus at the claim (right target) |
| sampling | A population field with a small clustered sample and a mismatch marker |
| circular-reasoning | A loop: conclusion feeds the premise that feeds it |
| internal-contradiction | Two statements joined by a "cannot both hold" bar |
| equivocation | One word splitting into two meanings, one path per meaning |
| inappropriate-appeal | An authority badge that does not match the topic |
| sleight-of-hand | A premise term and a conclusion term with a ≠ between them |
| sleazy-sales-pitch | A one-sided scale: what is shown versus the two hidden pans |
| universal-desires | A crowd where most want the goal and a few visibly do not |
| value-assumptions | A fact stepping across a gap to a loaded word |
| secret-downsides | Visible benefit above a waterline, hidden cost below |

Page-level visuals from the design artifact: the **Cake-on-Blocks** validity model near the top (a button "Object: what if" separates the blocks and the cake falls; a Reset button restores it), the **15-card grid** with filter chips (All 15, Group 1, Group 2, Group 3 with counts), and the **Disambiguation Matrix** with each question set as a pink margin prompt.

## Page order

1. Hero: kicker slot, title "Famous Flaws", one paragraph saying what a flaw question asks and that there are 15 flaws in 3 groups (6, 4, 5).
2. How to use it: name the flaw before the choices, find it in the list, then read the choices for the one that says it.
3. Cake-on-Blocks.
4. The grid with filters. Each card opens its full panel.
5. The five disguise mechanics, each with its source examples.
6. The Disambiguation Matrix, all 10 rows, each with a forced-choice check (two labels, pick one, see the reason).
7. What to do next: a `<ol class="steps todo">` the owner fills later.

## Session slots (for the owner's later step; build them empty)

- `<div class="kicker"><!--SLOT:hero-kicker-->Famous Flaws</div>` in the hero: the kicker text is replaced later.
- In every panel's header: `<span class="session-slot" data-slot="session-<flaw-id>"></span>` (15 empty spans).
- In every panel: `<div class="session-quote" data-slot="quote-<flaw-id>" hidden></div>` (15 empty hidden blocks).
- In "What to do next": the `<ol class="steps todo">` with a single placeholder `<li>` whose text is exactly `SLOT:next-steps`.
- The page must work and look finished with all slots empty.

## Adaptation rules (the only permitted changes from source text)

Each applied change is logged in `out/adaptations.json` as `{"rule":"R1".."R7","flaw":"…","from":"…","to":"…"}` and must fit one rule:

- `R1`: "Joshua-Named" becomes "Named by me": the page speaks in the owner's first person.
- `R2`: internal references leave the visible text and are rewritten into plain student language: the five spans listed under verification item 4.
- `R3`: PrepTest cites in examples are removed ("PT 16.2.19", "PT 16.2.10", "June 2007.3.21").
- `R4`: real public figures in examples become roles ("Dr. Fauci" becomes "the expert").
- `R5`: every em-dash and en-dash becomes a period, colon, comma or the middle dot.
- `R6`: the four Group 2 "What if" slots are filled from `sources/flaws.ts`.
- `R7`: the permitted omissions listed under verification.

Everything else is kept word for word. **Correctness exception:** the Internal Contradiction worked example in the source (the LSAT is "incredibly challenging for anyone", yet a prepared student will "feel like" it is easy) can be read as two compatible statements. It is the owner's canonical example, so keep it verbatim and do not silently change it. The panel's own "New example" check must use a clean contradiction about the same subject, time and sense. Report this example to the host so the owner can decide.

## Rules for any text a student reads

No em-dashes or en-dashes. None of these words: delve, unlock, seamless, robust, game-changer, supercharge, elevate, Moreover, Furthermore, Additionally, "Great question", "Certainly". The thing is called a "note", never a "manual", "recognition drill" or "conceptual note". No tool names, no mention of a transcript or a platform's internals. Second person, short sentences where the source allows them.

## Technical constraints

- One file `out/famous-flaws.html`, complete HTML document, **under 500 KB**, everything inlined.
- It keeps the shell's `<meta name="lsatu-interactive-lesson" content="…">`; set the id to `famous-flaws-full`. The visible h1 is `Famous Flaws`; the browser `<title>` is `Famous Flaws · Note`.
- Must pass `tools/lsatu-lesson-validate.mjs` (no external file, font, link, `@import`, or non-data `url()`). `url(#id)` fragment references inside SVG are allowed.
- The shell's `<style>` block and its `<script>` block must be **byte-identical** to the shell's. Your additive layer goes in its own `<style>` after the shell style. Any new script goes in its own `<script>` block after the shell script; the shell script must keep working (it builds the section rail from `main > section > .sec-kicker` and the reading progress bar; keep that structure for every top-level section).
- Mobile: at 375 px width there is no horizontal page scroll (tables may scroll inside their own wrapper). Controls are keyboard operable with a visible focus ring. Contrast stays readable.
- No `localStorage` requirement. If used, wrap in try/catch.

## Work packages (do them in order, in this one session)

| # | Package | Output |
|---|---|---|
| WP1 | Data layer: parse source 1 into structured data for all 15 flaws, 68 disguises, 10 matrix rows, 5 mechanics, applying the adaptation rules | `out/flaws.data.json`, `out/adaptations.json` |
| WP2 | Visual system: additive CSS layer, 15 SVGs, Cake-on-Blocks, accessibility and reduced motion | `out/famous-flaws.layer.css`, `out/svg/*.svg` |
| WP3 | Page assembly from the shell plus data, with the empty session slots | `build-famous-flaws-full.py` (Python 3, standard library only, run as `py -I build-famous-flaws-full.py`), `out/famous-flaws.html` |
| WP4 | Interactions: filters, panel open and close, matrix forced-choice check, per-flaw checks | inside the build script's output |
| WP5 | Verification scripts, see below | `verify-all.mjs`, `verify-browser.mjs` |

## Verification (you write both scripts; do not claim a pass you did not run)

**`verify-all.mjs`**: Node, no browser, no dependencies. Run as `node verify-all.mjs`. It must **parse `sources/05_compiled_content_voiced.md` itself** (not your `flaws.data.json`), so it checks the page against the source and not against your own intermediate data. It prints a table and exits non-zero on any failure:

1. **Source counts, from the source:** 15 entries; 68 disguise phrasings; 15 worked examples; **11** "What if" counters; 12 "Disambiguate from" pairs across 9 entries; 4 "When it IS the right answer" blocks; 5 phrase pairs; 10 matrix rows; 5 mechanics. It also checks that `sources/flaws.ts` has a `counterQuestion` for each of the four Group 2 entries.
2. **Block coverage, not just counted strings.** Split the in-scope source into blocks: the Group intro paragraphs, the "How to read this catalog" quote, and for each entry its frequency line, Definition, Stimulus tells (with any sub-bullets), every disguise bullet, the worked example and its explanation, the What-if counter, each Disambiguate bullet, When-it-IS, phrase pairs; the mechanics intro and each mechanic with its bullets; the matrix intro and, for each of the 10 rows, all three cells. Every block must appear in the visible text of `out/famous-flaws.html`, inside the panel or section for its entry, after applying `out/adaptations.json`. Normalise whitespace, quotes and markdown. Report each miss by entry and block. A shortened definition fails.
3. **Permitted omissions (the only ones):** the "Procedural-reference mode..." line (internal build note), slug text, the Causal "Cross-link" line, the "Stage 3 implementation note" quote, the "How to drill the matrix" section, and the last sentence of the "How to read this catalog" quote.
4. **Adaptation manifest validation, rule by rule.** The verifier owns the allowed transformations: it contains its own closed table of the permitted (rule, source span, replacement) triples, and `out/adaptations.json` must match that table exactly. It rejects an unknown rule id, a `from` that is not verbatim in the source, a `to` that does not fit its rule, and any manifest entry not in the table, even when the rule id is valid. Per rule: `R1` the only change is "Joshua-Named" to "Named by me" in the Group 3 heading; `R2` only the exact source spans that name internal references (Trap Pattern 4, the five spans "Trap Pattern 4 (Wrong Flaw)" (inside the sentence "it's probably Trap Pattern 4 (Wrong Flaw)."), "(Trap 4 Wrong Flaw, Trap 5 Contradicted from § 5)", "Wrong Flaw (Trap 4 from § 5) is the trap pattern that costs", "The Master Guide teaches you the flaws.", "The per-flaw disguise lists are embedded in each catalog entry above." (the section sign is the literal character U+00A7, so match it as written in the source)) may change, and each replacement is listed in the verifier's table; `R3` the `to` is the `from` with only the PrepTest cite parenthetical removed; `R4` the `to` is the `from` with only the named person replaced by a role; `R5` the `to` equals the `from` with only dash characters replaced; `R6` the `to` equals the `counterQuestion` string parsed from `sources/flaws.ts` for that flaw; `R7` the `from` is one of the enumerated omitted blocks, verbatim. Block coverage is then computed against the source with exactly these transformations applied, so a shortened definition cannot be introduced through the manifest.
5. Exactly 15 panels, each with all the parts that exist for that entry (per the lists above); 15 distinct SVGs plus the Cake-on-Blocks SVG, each with `<title>` and `<desc>`.
6. The shell `<style>` and `<script>` blocks are identical to `shell/note-shell.html` (compare after normalising CRLF to LF on both sides).
7. The validator passes. File size under 500 KB.
8. Zero em-dashes or en-dashes in visible text and attributes; none of the banned words.
9. Every "New example" is labelled as such.

**`verify-browser.mjs`**: Playwright test the owner runs, not you. It uses `createRequire('C:/Users/Joshu/dev/lsatu/package.json')` to load `playwright-core` and `chromium.launch()`. Do not run it. It checks at 1280 px and 375 px: no horizontal page overflow, Outfit and both Fraunces faces loaded, no console errors, the filter chips change the visible cards, a card opens and closes by mouse and by keyboard, Cake-on-Blocks Object and Reset work, the matrix check reveals reasons, and it writes full-page screenshots to `out/previews/`.

## Proof command (what the host runs independently)

`py -I build-famous-flaws-full.py && node verify-all.mjs`

## Non-goals

No posting or assigning. No edits to `sources/`, `shell/` or `tools/`. No paste-an-answer-choice tool. No new fonts. No content for any named student.

## Risks to report, not hide

- The Causal entry says the inference is wrong "99.9% of the time". Keep it as written; it is the owner's rule of thumb.
- Total content is about 6,000 words. Collapsed panels are the mitigation.
- The Internal Contradiction canonical example is arguable (see the correctness exception). Flag it, do not change it.
- If a command cannot run in your sandbox, say which one and stop. Do not fake output.
