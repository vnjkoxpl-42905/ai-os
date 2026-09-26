# LR explanation coverage: Brainstorm / Discovery Notes
Date: 2026-09-26 · Goal: decide what the coverage states are called, what counts as "explained", and how the 846 gaps get closed.
Status: in progress
Context sources: [[../wiki/lr-missing-explanations]], [[../wiki/lr-missing-explanations-by-category]], `projects/lsatu/src/components/drill/CONTEXT.md` (Question Explanation, Argument Breakdown, Choice Note, Question Type, Reasoning Type), `projects/lsatu/src/hooks/useLrExplanation.ts`

## Starting facts (looked up, not decisions)
- Live `lr_*` tables vs question bank, 2026-09-26: 354 no explanation, 298 Choice Notes with no Argument Breakdown, 194 in the bank but never loaded. Total 846 of 3,965 LR questions.
- Glossary says Question Explanation is authored for "0 of 3,964": stale.
- Glossary Reasoning Type examples (Conditional Logic, Comparisons) differ from bank values (Conditional Reasoning, Comparative Reasoning).
- Glossary wants ~25 canonical Question Types; the coverage report grouped into 16 families.
- PT154 (77/77 gaps), PT156 (36 never loaded), PT159 (37 never loaded) all have transcribed files in `projects/lsatu/Explanations/`.

## Summary / key decisions
- **Coverage states (Joshua, R1 Q1):** Complete (Argument Breakdown + Choice Notes), Notes-only (Choice Notes, no Argument Breakdown), Unexplained (neither), Unloaded (not in the lr_* tables). Only Complete counts as having a Question Explanation. Headline: 3,119 of 3,965.
- **Source for the gaps (R1 Q2):** Claude writes them, as an identical writer to the existing LSAT Lab explanations: same structure, language, style, quality and tone, matched to each question's type and reasoning. Built from a deep analysis of the whole existing corpus, using similar questions as examples. Clearer where possible, never AI-sounding.
- **First pass (R1 Q3):** load PT154, PT156, PT159 from the existing transcribed files before any new writing.
- **Scope (R1 Q4):** LR only. No RC.
- **Existing explanations are untouched (R2).** Work is only on questions that lack one. The existing corpus is reference material, never edited.
- **Method (R2):** pick a golden set of 10 to 30 of the best explained, best structured existing explanations as the standard. For each missing question, also use existing explanations with the same Question Type and the same Question Features as reference points. Output should match them in writing, style and structure, be more understandable and digestible for any student, and be consistent across the whole set.

- **Provenance (R3 Q5):** mark each explanation as LSAT Lab or LSAT U "for our purposes"; never shown to students.
- **Review (R3 Q6):** yes. Pilot of about 20 reviewed in full by Joshua, then spot checks; nothing live before the pilot is approved.
- **Styles (R3 Q7):** Standard only, plus Choice Notes.
- **Notes-only (R3 Q8):** they count as missing ("half explained"). Claude writes the Argument Breakdown; LSAT Lab's Choice Notes stay unchanged.
- **Golden set (R3 Q10):** Claude proposes it; Joshua approves before any writing.
- **Latitude (R3 Q11):** match the top-tier explanations and optimise them so students "can execute their goal better." Not one-size-fits-all: no fixed rules like short sentences or one idea per step. "Some fluidity," but "a strong framework."
- Order of work: open (R3 Q9).

## Q&A log
### Round 1
#### Q1 - What counts as "explained"
- Asked: does Notes-only count as having a Question Explanation?
- Recommended: no; four states Complete / Notes-only / Unexplained / Unloaded.
- Captured: "go with your recommendation."
#### Q2 - Where the missing explanations come from
- Asked: who produces explanations LSAT Lab never wrote (Joshua / Claude draft / AI tutor fallback / video transcription)?
- Recommended: Claude drafts in Joshua's voice for review, transcribe video where it exists.
- Captured: Claude writes them, but modelled on the existing explanations, not Joshua's voice: "should be identical ... as though an identical writer." Match "the language, the style, and the quality." Different questions need different reasoning, so pay attention to type. Requires "a deep analysis of all of the questions, all of the different scenarios." Use other questions of the same or similar type as examples. Goal is "top notch" and "top tier"; improve clarity where possible; no AI-sounding language.
- Tentative: video transcription not mentioned; treated as not chosen.
- Flags: review gate not stated -> Joshua (R2). Conflicts with the glossary line "transcribed LSAT Lab content and never generated" -> Joshua (R2).
#### Q3 - Load what's already transcribed first
- Captured: yes, load PT154, PT156, PT159 in the first pass.
- Fact (looked up): `scripts/knowledge/ingest-lr-explanations.mjs` already covers PT141-PT159 from `Explanations/`, and writes via SQL chunks pasted into the Supabase SQL editor (no direct DB connection). So these three gaps are a parse or load failure to diagnose, not a missing source.
#### Q4 - Scope
- Captured: LR only. "Don't worry about reading comp." (Recommended background RC count dropped.)

### Round 2
Asked Q5 (record who wrote each explanation), Q6 (review gate and pilot), Q7 (Standard only vs all three styles), Q8 (Notes-only: keep LSAT Lab notes, add Argument Breakdown), Q9 (order: assigned questions first, then by type).
#### Answer (covers method, not Q5-Q9 directly)
- Captured: "We're not changing the current ones we have." Use existing explanations from other questions "to help make explanations in the same way as the top ones." Make explanations "for all the ones that don't have explanations"; "the ones that already have them, we don't have to worry about for now." "Take like 10 to 20 or 30 questions that are the top best ones ... use them as golden standards." Also "pay attention to the other questions that have the exact same features and exact same question type ... as reference points." Aim: "top tier," "more understandable, more digestible for any student," "very consistent."
- Tentative: Q8 partly answered. Existing Choice Notes stay unchanged; whether Notes-only questions get an Argument Breakdown added is still open.
- Flags: Q5, Q6, Q7, Q9 unanswered -> Joshua (R3).

### Round 3
#### Q5 - Record who wrote it
- Captured: "you can mark it for our purposes. It shouldn't actually be showing ... when student facing."
#### Q6 - Review
- Captured: yes.
#### Q7 - Styles
- Captured: "Have standard only."
#### Q8 - Notes-only
- Captured: yes, "without it they're half explained."
- Captured (reminder): "only do the questions that don't currently have explanations."
#### Q9 - Order
- Captured: "not necessarily." Assigned-first rejected; no alternative given.
- Flags: order of work -> Joshua (R4).
#### Q10 - Golden set
- Captured: yes, Claude proposes, Joshua approves.
#### Q11 - Latitude to improve
- Recommended: keep structure, labels, tone; improve clarity with shorter sentences and one idea per step.
- Captured: improve clarity yes, but "it doesn't have to be shorter sentences or one idea per step ... not a one-size-fits-all approach." "They should match what's in the top tier explanations ... optimized so people can execute their goal better. You don't have to actually match identically. There's some fluidity there, but we should have a strong framework and get the best outcome possible."
- Superseded: my R3 recommendation of fixed sentence rules.

## Open flags (pending input)
- Why PT154/156/159 did not load -> Claude (diagnose before loading)
