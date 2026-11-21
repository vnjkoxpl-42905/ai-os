---
title: Private source map · Oreoluwa · 2026-11-11
student: ore
internal: true
---

# Private source map · Oreoluwa · 2026-11-11

Internal. Not for the student. Source: `students/ore/transcript-downloads/2026-11-11-ore-notes-by-gemini.md` (full transcript read, 00:00:00 to 00:54:43).

## Tags (taxonomy.md)

| Kind | Tags |
|---|---|
| Question type | Flaw |
| Question feature | Famous Flaws; Abstract Answers (answer-choice language); Part vs. Whole |
| Reasoning type | Conditional Logic (sufficient versus necessary); Causation (correlation versus causation) |
| Practice mode | Reading Comprehension (one advice line only) |

Read before building: `wiki/homework-assigning/rules.md`, `note-formula.md`, `taxonomy.md`, and the Flaw, Famous Flaws, Part vs. Whole and Causation sections of `by-topic.md`.

## Source map

- **Governing concept:** four common flaws (sufficient versus necessary, correlation versus causation, part versus whole, unproven versus proven false) and name-the-flaw-first on flaw questions. Joshua taught causal first and longest (00:01 to 00:14), then part/whole (00:14 to 00:19), then unproven (00:19 to 00:26), then a conditional example (00:29 to 00:30).
- **Her actual sticking point:** on the assigned flaw question she named the flaw correctly (sufficient versus necessary), narrowed to A and E, and doubted A until Joshua walked it (00:37 to 00:44). She first read the word "cause" and guessed causation (00:43:26 to 00:44:27). She asked how to make the between-two-answers doubt go away (00:44:27 to 00:45:21).
- **Joshua's answer:** the answer choices are abstract, so de-abstractify them; fluency comes from exposure; review the wrong choices, not only the one you chose (00:45:21 to 00:49:02). Keep the fallacy list beside the questions.
- **Valid moves taught:** name the flaw before the choices; "a guaranteed way is not the only way"; a lack of evidence is not evidence of lacking.
- **Student words quoted in the note:** 00:43:26 to 00:44:27 ("why is it only harsh criticism... it could be gentle, it could be constructive... other things"), 00:15:46 block ("just because the team does well overall..."), 00:25:37 ("because I can't prove you're innocent, you're guilty"), 00:47:21 and 00:48:14 (the habit of just knowing a choice is wrong).

## Commitments

| Who | Work | Timestamp |
|---|---|---|
| Joshua | Send the list of fallacies | 00:26:28, 00:28:57, 00:49:02 |
| Joshua | Assign flaw practice with the list beside the questions | 00:49:02, 00:49:51 |
| Joshua | Send a complete note on the session with the study instructions | 00:50:51 |
| Ore | Memorize the fallacies by practicing with the list beside her | 00:49:02 |
| Ore | 1 or 2 Reading Comprehension passages every other day | 00:49:51, 00:50:51 |

## Reuse

- **Closest earlier note:** "The Famous Flaws: the most common ones" (2026-08-19, Yahunathan and Sofia; five copies in `notes-archive/`) plus the routine from "Reading Flaw Answer Choices" (Lexi A, 2026-08-05) and "Parallel Flaw: Name the Mistake First" (Charles, 2026-11-02).
- **What was reused:** the earlier note's tier-one table for the four flaws this session taught, with its tells, curated into the reference note. Its Sampling row and its six distractor flaws were dropped because the session did not teach them. The earlier note is a reference, not a teaching note, so the recap note is new, written in the shell's teaching shape.
- **Corpus query:** `query-brain.py` returned only conditional-logic pages for this topic. A grep found `corpus/Curriculum/Flaw and Famous Flaws/` (Notes, Homework). I read its `PRODUCT.md` head, `reference_flaw.md`, `notes_flaw.md` and `Homework/Fallacy Homework.md`. None defines the four flaws in Joshua's words, so the note's definitions come from the session itself.

## Corrections and cautions (things I decided or fixed)

1. **Gemini summary error.** It says flaw questions are "over 50% of LSAT logic sections". The transcript (00:26:28) says over half of flaw questions fall into these fallacies. The note uses the transcript's version.
2. **Not used: "flaw questions are the most common questions on the LSAT, period"** (00:49:02). I could not verify it and left it out.
3. **00:24:34.** Ore repeated Joshua's line as "lack of evidence is an evidence of it lacking", dropping the "not". Joshua said "exactly". It reads as a slip or a transcription error. The note states it correctly: a lack of evidence is not evidence of lacking.
4. **Transcript mishears:** answer choice E reads "takes the reputation of an argument". It is almost certainly "repudiation". The note avoids quoting the choice. "Logical for the trinity" is "Logical Reasoning".
5. **The recording starts mid-session.** At 00:00:00 Joshua is already closing the conditional-logic part ("requirements versus guarantees, subsets... then necessary versus sufficient fallacies. These are three ways they'll show up"). That earlier teaching is not on record, so the note covers sufficient versus necessary only as it appears in the recorded part.
6. **Which PrepTest question it was:** not stated in the recording (Joshua shared his screen; "logical for the trinity"). I did not identify it. The note uses fresh examples and the student's own words only, so it does not need the stimulus.
7. **Left out on purpose:** the race and crime-rate example, the religion discussion, the politics examples and her personal chat. The note uses neutral examples (team, campus, footbridge, doctor's note). Joshua's own neutral examples are kept.
8. **Check logic:** in the note's switch gate, the "Only the second" state says the evidence never said this route works. That is the case where the conclusion says "only" with no "enough" in the evidence. I wrote it as a bigger gap rather than a different named flaw, because the transcript does not teach that case.

## Not done in this job

- `students/ore/open-loops.md`, `transcripts.md` and `wiki/log.md` were not touched. The job was the recap, the proposal and the ledger row only.
- No dry run of `post-lesson` and no `assign_student_work`.

## Added after review (2026-11-14)

- Reviewer stand-in found the Reading Comprehension claim wrong (Read, Recall, Colour is LR). Fixed in the note and the proposal.
- The 2026-11-14 vault check found the real Famous Flaws list: 15 flaws in three groups (`raw/sources/lsat-curriculum/.../Flaw and Famous Flaws/_HANDOFF/05_compiled_content_voiced.md`, mirrored in `lsatu/src/bootcamps/fallacy-flaw-v2/data/flaws.ts`). The four taught in the session are four of the six Group 1 flaws. Whether Joshua covered Ad Hominem and Sampling before the recording starts is unknown.

## Famous Flaws build (2026-11-14)

- Plan `famous-flaws-full/PLAN.md`; review and build log in `PLAN-REVIEW-LOG-famous-flaws.md`. Neutral build `famous-flaws-full/famous-flaws.html` (no student content) and the filled version `famous-flaws-ore.html` (made by `finish-for-student.py`, Claude only, never sent to Codex).
- Her words quoted in the Famous Flaws panels: 00:43:26 to 00:44:27 (only harsh criticism), 00:43:26 to 00:44:27 (saw the word cause), 00:15:46 block (team does well), 00:25:37 (innocent, guilty).
- The Internal Contradiction canonical example is arguable (Codex FF-003). Kept verbatim. Owner to decide.
