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

## Open flags (pending input)
- Why PT154/156/159 did not load -> Claude (diagnose before loading)
