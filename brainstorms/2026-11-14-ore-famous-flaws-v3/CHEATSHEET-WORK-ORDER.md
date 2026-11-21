# Work order: turn Ore's Famous Flaws note into a cheat sheet, in Joshua's voice

Builder: Codex. Standalone work order requested by Joshua (not plan-reviewed). Claude inspects the result. Files you may edit: `src/content.py`, `build.py`, `src/layer.css`, `src/layer.js`, `verify.mjs`. Do not edit `shell/`, `src/diagrams.py`, `src/questions.json`, `tools/`, `img/`, `refs/`.

## What Joshua said (2026-11-15)

- The writing still doesn't sound like him. Emulate his writing style. Figure out what it is from his own words (below).
- Do not use the "gap" image or the word gap anywhere ("steps over a gap", "name the gap" are out).
- He wants a **categorizing cheat sheet of the 10 flaws**, Most Common and Not-So-Common, organized and quick to scan. Ideally **an image for each flaw** (he will make the images later; build a slot for them now).
- The kicker "Before you start · Flaw" is wrong. This note is about the famous flaws (fallacies) themselves, which show up across question types, not one flaw question set. The kicker is `Famous Flaws`, and the title should say what it is (for example "The Famous Flaws" or "Famous Flaws: the ten to know"; your call, in his voice).

## His voice: where to get it

1. **His handout is his own writing.** `refs/famous-fallacies-handout.txt`. Its definitions are the voice to match: plain, direct, a little conversational ("Presenting a conditional rule and then using it in an illegal backwards or opposite fashion", "Acting like X must be false", "Overconfidently concluding one possible causal interpretation of a curious fact", "Almost always wrong answers"). **Use his handout definition for each flaw's definition**, near verbatim. You may only: replace dashes, fix an obvious typo, and drop "Example:" labels. Do not paraphrase them into something smoother.
2. His spoken lines from Ore's session (`refs/ore-2026-11-11-transcript.md`, `refs/PRIVATE-source-map.md`): "a guaranteed way is not the only way", "a lack of evidence is not evidence of lacking", de-abstractify the answer choices, review the wrong choices too, keep the list beside the questions, over half of flaw questions fall into these fallacies.
3. His posted notes: `refs/sofia-*.txt`, `refs/celia-parallel-reasoning.txt`. Short sentences. Questions the student asks herself. No promises, no build-up, no decorative metaphor.
4. `refs/WRITING-SKILL-REVIEW.md` explains how earlier drafts drifted from him; `refs/teaching-voice.md`.

Everything you write that isn't his should sound like it sits next to his handout without a seam. When in doubt, shorter.

## Page structure (replace the current one)

1. **Hero:** kicker `Famous Flaws`, title, the bridge image stays (it's Joshua's), and at most two plain sentences under it: what this sheet is and how to use it (keep it beside you while you practice; name the flaw before you read the choices). No metaphor talk about the bridge.
2. **The sheet (overview), right after the hero.** Two labeled groups, "Most common" (5) and "Not-so-common" (5), in the handout's order. Each flaw is a card: number, name, its one-line handout definition (short form allowed only by cutting, not rewording), an **image slot**, and a link to its full entry. The cards show done state (replace the current `.findex` index; keep the done/progress behavior working, and keep a progress count). Two columns on desktop, one on phones.
   - **Image slot:** in `build.py`, if `img/flaw-<id>.webp` exists, embed it as a data URI in the card (and in the entry header, small); if not, render a quiet placeholder tile that shows the flaw's number, so the page looks finished without images. Use `alt` text from a new `"img_alt"` field per flaw in `content.py` (write it now, describing the planned image in one line).
3. **How to use it**, short: three questions she asks herself on a flaw question (what's the conclusion; what did the evidence actually show; which flaw is that, then which choice says it in plain words). Keep `HOW["said"]` (her stuck-between-two moment). Keep the legend for the colour marks.
4. **One entry per flaw**, compact and identical in shape (the flaw breakdown, `ai-os` term): name and tier; **What it is** (his handout definition); the diagram (keep, unchanged); **Example** (handout, verbatim, marked); **Why it's wrong** (two to four short sentences, his voice); **Spot it** (one line: what to look for in the argument); **The right answer says** (keep the existing `wording` list exactly); **Don't confuse it with** (keep `lookalike` name/text exactly; rewrite `tell` short); **From our session** where it exists (keep the existing `said` lines exactly); **Try a real one** (unchanged behavior and text). Drop the separate "What if" callout; fold anything essential into "Why it's wrong".
5. **Tier dividers** with Joshua's two drawings stay, between the groups of entries, each with one or two plain sentences (tier 1 must say over half of flaw questions fall into these; tier 2 that these show up less as the flaw and some, like the appeals, mostly as wrong answers, which is the handout's own note).
6. Recap table: cut it (the sheet at the top replaces it). Keep "What to do next" (`NEXT`), plain, dates as "November 16" etc.

## Locked (do not change)

Handout `examples` strings (verbatim with `<ev>/<con>/<j>`), `wording` lists, `lookalike` name/text, existing `said` lines, all `EXPLAIN` logic, the 10 real questions, the diagrams, flaw order and tiers, the logic settled in review (Internal Contradiction: the handout example can be read as consistent because of "feeling"; a true contradiction is two claims that cannot both hold, like the PCB question. Circular: "would you already have to accept the conclusion to accept the premise", and a weak or off-topic premise is a different problem. Inappropriate Appeal: authority whose credibility is never established). The two pandemic examples stay replaced. Drill names and dates.

## Rules for any text you write

No em dash or en dash. No "gap". None of: delve, dive deep, unlock, unleash, harness, seamless, robust, elevate, supercharge, game-changer, "it's not just X, it's Y", "Great question", "Certainly", "The good news", "Your job is to", "Before you start". No paragraph opening with Moreover/Furthermore/Additionally. Never "manual" or "recognition drill". No mention of transcripts, recordings, Gemini, Claude, Codex, a handout, or platform internals. American spelling. Dates as "November 16".

## verify.mjs

Update it to the new structure, never weaker: still check 10 entries in order with tiers 5/5, all breakdown parts present (`data-part` for name, what, example, why, spot, wording, lookalike), one diagram each, question text byte-equal, explanations, images-with-alt for the three drawings, banned words (add `gap` and `Before you start` to the banned list for authored text), no dashes outside verbatim blocks, pandemic remnants absent. Add: the sheet has 10 cards in two groups of 5; each flaw's definition text equals its handout definition after only the allowed edits (store the handout definitions in `content.py` as `HANDOUT_DEF` and compare).

## Proof (run; all must pass)

```
python build.py && node tools/validate-cli.mjs out/famous-flaws.html && node verify.mjs
```

Report: the new hero text, the kicker and title, every definition you changed from the handout and why (should be none or only allowed edits), and anything you could not do.
