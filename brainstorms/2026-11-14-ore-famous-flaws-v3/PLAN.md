# Plan: Famous Flaws note for Ore (rebuild v3)

Roles: Claude (host) plans and builds. Codex reviews this plan (max 2 rounds) and inspects the build in a fresh session. Output is a local preview only. Nothing is posted or assigned until Joshua approves.

## Why a rebuild

Joshua judged the posted "Famous Flaws" note (archived on Ore's account 2026-11-14) low quality: bland, weak information, poorly organised, hard to understand before the questions, big dark AI-looking surfaces. This build must read as a polished teaching note a student can learn from before she drills.

## Goal and acceptance criteria

One self-contained HTML note, `out/famous-flaws.html`, that teaches Joshua's 10 Famous Flaws so Ore can name each flaw on sight before her flaw drills unlock (2026-11-16).

1. **Content source:** Joshua's handout `src/famous-fallacies-handout.pdf` ("Famous Flaws - LSAT Logical Reasoning"). Exactly 10 flaws in his two tiers, in his order:
   - Five Most Common: Necessary vs. Sufficient, Causal, Part vs. Whole, Unproven vs. Proven False, Ad Hominem.
   - Not-So-Common: Sampling, Inappropriate Appeal, Circular Reasoning, Internal Contradiction, Equivocation.
   Names and definitions follow the handout (lightly voiced; meaning unchanged). Every handout example is kept word for word **except** two pandemic-era examples, replaced by neutral examples of the same flaw: Inappropriate Appeal's Fauci/hats example, and Ad Hominem's governor/masks example.
2. **Flaw breakdown** (term defined in `ai-os/CONTEXT.md`): every one of the 10 flaws gets all six parts, in this order:
   1. Name (handout name) plus tier tag.
   2. What it is: one plain sentence.
   3. Example(s): handout example(s), with the jump marked inline (evidence vs. conclusion visually distinguished; the overreaching move highlighted).
   4. Why it fails: the reasoning, said out loud, second person, short sentences, including the "what if" that breaks it.
   5. How the right answer words it: 2 to 4 real-style answer-choice phrasings for this flaw. Phrasings must be accurate LSAT descriptions; the real question's correct answer text may be quoted.
   6. The lookalike: one answer-choice-style description that sounds like this flaw but describes a different flaw or no flaw, and one sentence on how to tell them apart.
3. **One custom diagram per flaw** (10), inline SVG drawn for that flaw's logic, not a text card. Each has `<title>`/`<desc>`, uses the note's tokens, readable at 360px width:
   - Necessary vs. Sufficient: rule arrow A → B; the conclusion's arrow drawn reversed (B → A) and struck; a second panel shows the negation version (not A → not B) struck.
   - Causal: one observed correlation (two linked dots) with three competing explanations fanned out: A causes B, B causes A, C causes both.
   - Part vs. Whole: a row of tiles each tagged with a trait, an arrow to the assembled block with "?" on the trait; bidirectional.
   - Unproven vs. Proven False: two-state meter: "Not shown true" and "Shown false" with a gap between; the argument's arrow leaps the gap.
   - Ad Hominem: two targets (speaker vs. claim); the argument's arrow hits the speaker, the claim target is untouched.
   - Sampling: a population field of mixed dots; a small clustered circle of same-colour dots labelled "sample"; mismatch marker.
   - Inappropriate Appeal: a speech badge (feelings / unqualified authority / pick without reason) pointing at the conclusion through a broken connector.
   - Circular Reasoning: a loop where the premise card and conclusion card say the same thing.
   - Internal Contradiction: two statements from the same author joined by a "cannot both be true" bar.
   - Equivocation: one word that forks into two meanings, premise uses meaning 1, conclusion uses meaning 2.
4. **Joshua's three images** (he generated them; in `img/`): `hero-bridge.webp` at the top (the missing plank is the metaphor: an argument that steps over a gap), `divider-common.webp` before the Most Common tier, `divider-less-common.webp` before the Not-So-Common tier. Inlined as `data:image/webp` with meaningful `alt` text. Images sit on the paper ground, not in dark frames.
5. **One real LSAT U question per flaw** (10), from `src/questions.json` (pulled from the app's own question bank, `lsatu/public/data`): stimulus, stem, all five choices verbatim. Ore picks one choice; the note then marks it right or wrong, reveals the correct letter, and explains in Joshua's voice why the correct choice names this flaw and why her pick (if wrong) does not. She can retry. Choices:
   | Flaw | Question | Correct |
   |---|---|---|
   | Necessary vs. Sufficient | PT133.1.25 | A |
   | Causal | PT126.4.3 | D |
   | Part vs. Whole | PT121.1.2 | D |
   | Unproven vs. Proven False | PT138.2.7 | B |
   | Ad Hominem | PT118.3.6 | C |
   | Sampling | PT136.4.1 | A |
   | Inappropriate Appeal | PT131.2.6 | C |
   | Circular Reasoning | PT112.1.10 | C |
   | Internal Contradiction | PT146.1.22 | A |
   | Equivocation | PT102.4.17 | B |
   Each question has a short explanation for every wrong choice, not only the right one. PrepTest ids are not shown to the student.
6. **Navigation:** an index of the 10 flaws grouped by the two tiers. On wide screens it is the shell's rail, with tier labels; on narrow screens a compact index near the top. Each flaw is marked done once its question is answered correctly; state is remembered in `localStorage` with try/catch, keyed by the lesson id; the page works without storage.
7. **Look:** Lanae's model note via the shell (`shell/note-shell.html`): warm paper ground, plane sections, Fraunces + Outfit embedded, brass/green/red tokens. No big dark gradient hero, no glow, no generic AI cards. The shell's `.quote` dark block is not used. Visual hierarchy: tier heading > flaw name > the six parts with consistent small mono labels.
8. **Order of the page:** hero (bridge image, title "Famous Flaws", lede: what a flaw is and how to use the note) → "How to use this note" (3 steps: name the flaw in your own words before the choices; match it to the list; pick the choice that describes that move) → Tier 1 divider image + 5 flaws → Tier 2 divider image + 5 flaws → a one-screen recap table (flaw | the move | the answer usually says) → "What to do next" (`ol.steps todo`): her already-assigned drills, named as on the platform: "Flaw - First Taste" (unlocks 2026-11-16), "Famous Flaw (Easier) Set 1" (unlocks 2026-11-18), "Abstract + Flaw (set 1)" (unlocks 2026-11-20), plus "message me on the platform".

## Writing rules (student-visible text)

Joshua's teaching voice (`ai-os/wiki/teaching-voice.md`): plain, direct, second person, short sentences, teach the reasoning. The thing is a "note". No em-dashes or en-dashes in authored prose. **Exemption:** verbatim quotations (the real questions' stimuli, stems and choices, and the handout's example sentences) keep their original punctuation. None of: delve, dive deep, unlock, unleash, harness, seamless, robust, elevate, supercharge, game-changer, "it's not just X, it's Y", Moreover/Furthermore/Additionally to open a paragraph, "Great question", "Certainly". No keyboard-shortcut hints. No tool names, no mention of transcripts, Codex, Claude or platform internals.

## Technical approach

- Build script `build.py` (Python, stdlib only) reads `shell/note-shell.html`, `src/content.py` (all prose, authored by Claude) and `src/diagrams.py` (the ten SVGs), `src/questions.json`, `img/*.webp`, and writes `out/famous-flaws.html`.
- The shell's `<style>` and `<script>` blocks are copied byte-identical. Additive CSS goes in a second `<style>`; additive JS (question picker, done state, tier labels in rail, mobile index) in a second `<script>`. Shell template sections are replaced with the note's own sections; every top-level section keeps `main > section > .wrap > .sec-kicker` so the shell's rail and progress work.
- Meta `lsatu-interactive-lesson` content `ore-2026-11-14-famous-flaws-v3`; `<title>` "Famous Flaws · Note".
- Size: target under 500 KB (shell is 277 KB of which fonts are most; images are ~108 KB raw, ~144 KB base64).
- Must pass `node tools/validate-cli.mjs out/famous-flaws.html`, a wrapper that calls `validateInteractiveLesson` and exits non-zero on failure (no external resources).

## Non-goals

No posting or assignment. No changes to the LSAT U app repo. No new fonts or libraries. No flaws beyond the handout's 10. Not the 15-flaw catalog.

## Risks and assumptions

- Joshua's Internal Contradiction example (the LSAT is "incredibly challenging for anyone" vs. a protocol making it "feel" easy) can be read as two compatible statements. It is kept verbatim per his decision; the "why it fails" text explains the tension honestly, and the risk is reported to Joshua at handoff.
- Handout's Unproven vs. Proven False second example (Braves/Blackhawks) illustrates "a faulty argument for X does not make X false" only loosely; kept verbatim, and the why-it-fails text addresses the second form of the flaw in the definition.
- PT146.1.22's question type is labelled "Flawed Reasoning" in the bank; it is a flaw question.
- Explanations for real questions are written by Claude; each is checked against the stimulus during build.

## Verification

1. `node tools/validate-cli.mjs out/famous-flaws.html` prints VALID and exits 0 (checked: it exits 1 on a missing file and on the template's placeholder id).
2. A Node check script `verify.mjs` asserts: exactly 10 flaw sections in handout order with tier tags 5/5; each has all six breakdown parts (data attributes `data-part="name|what|example|why|wording|lookalike"`), one inline SVG with title+desc, one question with 5 choices whose correct letter equals `questions.json`; the stimulus and choices text are byte-equal to `questions.json`; the three images present as data URIs with alt text; no banned words or en/em-dashes in visible text outside `.qtext` (verbatim question) and `.passage` (verbatim example) elements; Fauci, mask, governor, coronavirus absent; file size printed.
3. Browser (built-in browser pane) at 1440, 1024, 768 and 375 widths: screenshot top, one flaw, one question after a wrong then right pick, the index, the end. Check no horizontal scroll, diagrams legible, images not cropped badly, index marks done and survives reload.
4. Keyboard: Tab reaches every choice; Enter/Space selects; feedback announced via `aria-live`.
5. Fresh Codex inspection of the final files against this plan.
