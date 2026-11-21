# Work order: rewrite the student-facing prose of Ore's Famous Flaws note

Builder: Codex. You edit **only `src/content.py`**. Do not touch any other file. Status: standalone work order requested by Joshua; not plan-reviewed. Claude inspects the result.

## Why

Joshua read the current note and said the writing is terrible and reads as AI. Example he flagged, the hero lede:

> "A flaw question hands you an argument that steps over a gap, like walking onto a bridge with a plank missing. Your job is to point at the gap. The good news: the LSAT reuses the same ten gaps again and again. Learn them here, one at a time, and you will start naming the flaw before you ever read the answer choices."

What is wrong with it, and with the note generally: it is written from a template, not from Ore's session. It promises ("The good news", "you will start naming"), stacks a decorative metaphor, and never says what students actually do wrong. None of Joshua's own lines from the session appear, and Ore is never quoted, though Joshua's posted notes always do both.

## Read these first (all in this repo)

1. `refs/ore-2026-11-11-transcript.md`: the full session. **Primary source.** Joshua teaches causal (00:01 to 00:14), part/whole (00:14 to 00:19), unproven (00:19 to 00:26), conditional (00:29 to 00:30), then works the harsh-criticism question with Ore (00:37 to 00:44) and answers her "how do I stop doubting between two answers" (00:44 to 00:49).
2. `refs/PRIVATE-source-map.md`: what the session covered, Ore's quotable lines with timestamps, the transcript errors to avoid (cautions 1 to 4), and topics to leave out (caution 7: no race, crime, religion or politics).
3. Joshua's real posted notes, the style to match: `refs/sofia-weakening-a-causal-argument.txt`, `refs/sofia-weaken-go-after-the-story.txt`, `refs/celia-parallel-reasoning.txt`.
4. `refs/WRITING-SKILL-REVIEW.md`: why earlier drafts missed Joshua's voice (findings F1, F3, F4, F5 especially), and `refs/teaching-voice.md`, `refs/lsat-teaching-voice-standard.md`, `refs/COPY-CORRECTIONS.md`.

## What Joshua's notes do (match this)

- **Open on the real problem.** Say what students do and why it fails, then the move that works. Sofia's note: "Students stall when they judge an answer by how strong its words sound instead of what it does to the author's cause." No promises, no "the good news", no "your job is to point at the gap".
- **Use Joshua's own lines and images from the session**, said plainly, as working tools. From this session, at least: "a guaranteed way is not the only way"; "a lack of evidence is not evidence of lacking"; the answer choices are abstract, so de-abstractify them (put them in plain words); review the wrong choices, not only the one you picked; keep the fallacy list beside the questions while you practice; over half of flaw questions fall into these fallacies (the transcript's version, not Gemini's). Find his own examples in the transcript and prefer them over invented ones (respect caution 7).
- **Steps are questions she asks herself.** "Start from the top. What is the conclusion?" "Name the suspects."
- **Credit lines quote Ore.** Each is one or two sentences: what she said in the session, and what was right about it. Sofia's: "You asked yourself whether that answer was leaning too hard on the author's cause. It was, and you were right to ask." Put them in the optional `"said"` field (see below). Only quote what the transcript supports; use the source map's timestamps; fix the 00:24:34 slip (state the line correctly, do not quote her slip).
- **Short, plain, spoken sentences with contractions.** Each caveat once. No stacked hedges.
- **Concrete over abstract.** When explaining why a flaw fails, use the example's own nouns, not "the author's claim".

## Exact scope in `src/content.py`

Rewrite for voice and teaching, keeping meaning accurate:
- `HERO["lede"]` (keep `kicker` and `title`).
- `HOW`: `h2`, `intro`, `steps`, `legend`. Add `HOW["said"]`: a credit line from her "how do I stop doubting between two answers" moment (00:44 to 00:49) with Joshua's answer.
- `TIERS`: `h2`, `p` (keep `id`, `img`, `alt`, `kicker`). Tier 1 must reflect what the session said about how often these come up.
- Each of the 10 `FLAWS`: `what`, `why`, `whatif`, `lookalike["tell"]`. Add `"said"` to the flaws the session covered where the transcript supports a quote: necessary-vs-sufficient (her "why is it only harsh criticism" reasoning, and that she first saw the word "cause"), part-vs-whole (team), unproven-vs-proven-false (innocent/guilty), causal (if supported). Do **not** add `said` to flaws the session did not cover (ad hominem, sampling, appeal, circular, contradiction, equivocation).
- `EXPLAIN` (the answer explanations for the 10 real questions): rewrite for voice only; keep every logical point. For `nec`, it is the question she worked in session; the explanation may tie back to that.
- `RECAP["p"]` and the middle column of `RECAP["rows"]`. `NEXT["steps"]`: plain, with the reason Joshua gave for practicing with the list beside her.

Do **not** change:
- Any `examples` string (Joshua's handout text, word for word, including `<ev>`, `<con>`, `<j>` markup), `name`, `id`, `q`, `tier`, `diagram`, `LESSON_ID`.
- `wording` lists and `lookalike["name"]`/`["text"]` (accuracy-checked: none may equal or contain its own question's correct answer).
- The logic settled in review: Internal Contradiction must say the handout example can be read as consistent because of "feeling", and that a true contradiction is two claims that cannot both hold (the PCB question). Circular must test "would you already have to accept the conclusion to accept the premise", and say a weak or off-topic premise is a different problem. Inappropriate Appeal's definition is an authority whose **credibility is never established** (not "no expertise"), and the neighbor example has no credential.
- Any fact about Ore's drills: "Flaw - First Taste" opens November 16, "Famous Flaw (Easier) Set 1" November 18, "Abstract + Flaw (set 1)" November 20.

## Hard rules for every string you write

No em dash or en dash. None of: delve, dive deep, unlock, unleash, harness, seamless, robust, elevate, supercharge, game-changer, "it's not just X, it's Y", "Great question", "Certainly", "The good news", "Your job is to". No paragraph opening with Moreover, Furthermore or Additionally. The thing is a "note"; never "manual" or "recognition drill". No mention of transcripts, recordings, Gemini, Claude, Codex or the platform's internals. Use American spelling. Keep it valid Python (escape quotes; the file uses `“` style escapes for curly quotes, which you may keep or use literal characters).

## Proof (run it; all must pass)

```
python build.py && node tools/validate-cli.mjs out/famous-flaws.html && node verify.mjs
```

Then report: every `said` line with its transcript timestamp, and any place you could not follow the brief.
