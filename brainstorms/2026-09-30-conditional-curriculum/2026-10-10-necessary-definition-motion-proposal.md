# Necessary definition and motion proposal, revised

Planning and source review only. No page edits or generated video this turn. Codex proposes; Claude reviews with configured default. Two review rounds maximum. User explicitly rejected the abstract Required for what opening and standalone then indicator claim. Those user corrections override older source wording.

## Explain the relationship, then test it

Proposed student copy, distributed over teaching beats:

Calling a condition necessary means the other condition can't be true without it. It identifies a requirement. It doesn't tell you whether meeting that requirement is enough on its own.

Take our rule: If you're enrolled in law school, you're a student.

Could you be enrolled in law school and not be a student without breaking that rule? [Learner answers before reveal.]

No. The rule says everyone enrolled in law school is a student. Being enrolled and not being a student would contradict it. That's why being a student is necessary for being enrolled in law school.

Now suppose you're a student. Does that alone establish that you're enrolled in law school? [Learner answers before reveal.]

No. One case the rule allows is that you're a history student who isn't enrolled in law school. You meet the requirement, but enrollment still hasn't been established by knowing only that you're a student.

Connect the roles: being enrolled in law school is sufficient to establish that you're a student. Being a student is necessary for enrollment. One tells you what is enough to establish the other; the other tells you what is required.

Boundary: do not claim a necessary condition is never sufficient. Some rules work both ways. Do not classify the word 'then' as a standalone Group2 indicator. The law-school example is a stated rule, not evidence that anyone is actually enrolled. The first question tests a forbidden combination without introducing a new contrapositive procedure or notation.

## Reuse the existing lesson rather than add another explainer

Current NecessaryConditionExperience.tsx already has three selectable cases; SufficientConditionExperience.tsx has the nested-group visual. NecessaryConditionStatement.tsx currently only pulses a highlight. The gap is reasoning made visible, with a chance to predict before feedback.

Recommendation: adapt that existing necessary interaction to render the student-group diagram, keeping the current case data as the shared source of labels and facts. Preserve the existing Kling film. Do not add a second independent set of law/history/nonstudent data. If extracted, use one shared scene/case module for the HTML/SVG diagram and any later export. Keep the complete rule readable and all information available in reduced motion.

Storyboard for the in-page explanation:
1. Show Students and People enrolled in law school as a schematic of the rule. Label outer-only space: allowed by the rule, not asserted. Neither area nor group size is quantitative, and the rule alone does not assert any members or a strict subset.
2. Suppose you're enrolled. Highlight both memberships together, without moving a person between groups. Ask whether enrolled-but-not-student fits; reveal the contradiction after an answer.
3. Suppose only that you're a student. Ask whether enrollment follows. Reveal one allowed case, a history student explicitly not enrolled, inside Students and outside the law-school group. Do not present that hypothetical as an existence claim deduced from the rule.
4. Hold the two roles beside the same rule: enough to establish / required for.

No new standalone contrapositive lesson here. Existing nonstudent case can remain, but do not expand it into a procedure. Keep people's positions stable while attention changes; avoid implying causation or temporal sequence.

## Chase AI source and video route

Found wiki/sources/claude-now-does-video-free-javascript.md and read its archived transcript raw/sources/clips/claude-now-does-video-free-javascript/Claude Now Does Video (FOR FREE) Thanks To JavaScript 1.md in C:/Users/Joshu/dev/ai-os. Captured2026-10-10, publication date unknown. Original https://www.youtube.com/watch?v=rscb1DgJtNg.

Creator describes deterministic JavaScript time-to-frame rendering, browser capture, FFmpeg MP4 assembly, storyboard-first work and contact-sheet revision. The source does not demonstrate this workspace or Codex. Applying the coding method with Codex is our engineering proposal, not a source-verified result. No creator skill URL or verified licence in the archive. No claim to have installed that skill. Runtime readiness would be checked before production; saved source did not verify Playwright or faster-whisper.

Use the one shared diagram/scene definition for the interactive lesson first. An optional MP4 can later render the same scene states, so it does not drift from the lesson. No arbitrary duration fixed now: derive holds from actual text/narration and inspect playback for pacing. Contact sheets verify composition and transitions' sampled states, not reading time or audio synchronization. Playback must be reviewed separately. Start silent/captioned; no external TTS generation or paid tool calls in this scope. All necessary teaching stays in HTML.

## Source comparison already performed by host researcher

- 7Sage raw/sources/7sage-curriculum/conditional-overview-Tjdkaq4A-xM/source-transcript.txt:64-70 explains required via impossible outside-US/in-Texas combination.
- Lab raw/sources/lsat-lab-lectures/16784/source.en-US.vtt:164-261 contrasts required membership with a counterexample to reversal.
- wiki/sources/lsat-demon-mastering-conditional-statements.md:36-45 distinguishes A requires B from B required for A as same relationship.
- references/lsat-teaching-voice-standard.md:399-410 calls for multiple teachable moments, not one definition/answer;452 rejects temporal interpretation.
- corpus/Curriculum/Conditional Logic/Notes/_megadoc_notes_conditionals.md:158 advocates personalizing the rule and asking what it requires.

This is targeted comparison of major relevant sources, not an exhaustive audit of every corpus item. Please judge final explanation and recommendation; no code implementation or video claim.
