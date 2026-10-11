# Bootcamp teaching preferences

Captured 2026-10-11 from Joshua's conditional-bootcamp conversation. These are requirements for future builds where applicable, not proof that any implementation has passed acceptance.

## General standards confirmed by repeated corrections

- Compare the topic against internal corpus sources before drafting. Preserve source provenance and distinguish a source claim from Joshua's decision. Ingest new clips through the ingest skill before relying on them. Never infer a video transcript from its title.
- Explain the concept in plain language, then develop it through a concrete familiar example. Introduce notation after meaning. A short definition alone is not a lesson. Avoid recursive definitions and tongue twisters.
- Break explanations into readable sections with clear visual hierarchy, larger text, generous spacing, and short paragraphs. Inspect the actual rendered page, including the docked browser width and mobile, rather than treating JSX inspection as visual approval.
- Bring meaningful interaction early, after enough teaching to attempt it. Feedback explains the reasoning and distinguishes given facts from conclusions of a rule. Do not merely cycle reveal buttons and call that practice.
- Use color, emphasis, and motion to direct attention to the entire relevant idea. Preserve complete conditions, restrictions, timing, modality, and the difference between a rule and a fact.
- Preserve existing teaching media while revising. Check that videos still exist and play in their intended lesson. New media must earn its place in the teaching flow.
- Review content against the corpus, review the rendered UI, and use independent Claude Code review when requested. Record the actual model from the run, review artifact, findings, disposition, and limitations. Code/screenshot review is not live browser testing. Tests, local build, deployment, and signed-in acceptance are separate claims.

## Necessary-condition lesson: explicitly approved wording

Joshua supplied and approved this copy on 2026-10-11:

> **A necessary condition is a requirement. It has to be met, but meeting it might not be enough.**
> For example, you have to be a student to be enrolled in law school. That makes being a student **necessary for law-school enrollment**.
> But being a student doesn’t mean you’re enrolled in law school. You could be studying history instead.
> **Being a student is required. It doesn’t establish enrollment on its own.**

Keep “might not”: a condition may be both necessary and sufficient. Do not replace this with “something another condition can’t be true without.”

Explicit page corrections:
- Emphasize the complete consequent, “then you are a student,” and identify “you are a student” as the condition. Do not teach isolated “then” as a standalone necessary-condition indicator.
- Law student / history student / not a student should be vertical case tabs. Keep keyboard navigation, visible selected state, and mobile stacking. This is a decision for this case comparison, not a mandate for every interaction.
- Remove “Replay emphasis”; use a gentle continuous pulse for this page, with a static reduced-motion equivalent. This does not authorize constant pulsing on every page.
- Make clear which facts are given and which follow. If a history case says not enrolled, make it explicitly given rather than inferring it from studying history.

Content preservation checks for the conditional sequence:
- Necessary examples retain only, only if, only when, only where, always, requires, must; explain their meaning in the complete sentence and preserve modality/scope. This is the existing lesson coverage, not a context-free replacement dictionary.
- Sufficient Group 1 stays on-page: if; when/whenever; any/anytime; all; every/every time; in order to; people who; each.
- Keep the reference-letter qualifiers, including current and accepted for review. A distractor should reveal a reasoning error, not reward guessing.

## Must arrow: correction and open work

- Confirmed title: **Must arrow**, not “Read the must arrow.”
- Teach the direction explicitly with a familiar relationship: in this convention sufficient on the left, necessary on the right, arrow pointing right. The left condition guarantees the right **if the left condition is true**. The arrow alone asserts neither condition as a fact, neither causation nor chronological order, and no reverse inference.
- The lead “A must arrow shows what has to be true if another condition is true” was rejected as too abstract on 2026-10-11. Do not preserve it as approved wording. Joshua wants the direction shown and explained directly.
- Current provisional implementation: “The must arrow points from left to right. If the left side is true, the right side must be true.” The new LSAT Lab clip (jeDnykOrswY) supports certainty at 0:31 and left requiring right at 8:19, per the source review in this session. This wording is not yet user-approved.
- Source comparison completed; final wording remains provisional pending Joshua’s review. Earlier assistant summaries saying tests passed or an opening was updated are implementation reports, not user approval.
- Source finding, not a user wording approval: original HTML `raw/sources/conditional-reasoning-voice-standard/conditional_reasoning_transcription.html`, lines 322-356, supports sufficient-to-necessary placement. The parent source comparison is recorded in `brainstorms/2026-09-30-conditional-curriculum/2026-10-11-must-arrow-review.md`.
- Source pointers, relative to the vault resolved through its AGENTS.md: `wiki/sources/lsat-lab-conditional-logic-clip.md` and `corpus/Curriculum/Conditional Logic/Notes/_megadoc_reference_conditionals.md#the-must-arrow-shows-a-direction-of-guarantee`.

### Must-arrow visual readback correction, 2026-10-11

Status: explicit newest user direction, relayed in this chat; resulting markup is provisional until reviewed by Joshua.

- Label the diagram's **Left side** and **Right side** clearly.
- Teach how to follow/read this arrow from left to right, and explain **must** as what must be true if the left condition is true.
- Simplify or remove the repeated closing student conclusion. Prefer one intuitive readback of the diagram over restating the same inference in several paragraphs.
- Scope: the original sufficient-to-necessary arrow in this introduction. This does not ban a later contrapositive or other valid inference that has been separately taught.

Acceptance: inspect the rendered diagram for visible side labels; read its explanation aloud in order to check that direction and certainty are clear without repeated student conclusions. Preserve the condition that the left side is true. Do not call new markup user-approved merely because it implements this request.

### Must-arrow layout and practice corrections, 2026-10-11

Status: six explicit browser corrections relayed in this chat. These record requested outcomes; resulting implementation remains provisional.

- Give the two diagram sides balanced, breathable space, especially the right side. Use spatial presentation and meaningful motion to teach the relationship. GIF or Kling video is an option, not a requirement; native motion may serve the same purpose. Preserve reduced-motion access and existing spending authorization boundaries.
- Shorten the explanation of why reversing the arrow is invalid, and visually separate its ideas so the learner can follow them.
- Replace the practice presentation labelled “Recall card” and its counter. Do not keep card-count machinery merely because it already exists.
- Remove the confusing “Think before you turn” framing and the corner “Explain in own words” / “Turn explanation” controls from this practice presentation.
- Resolve the ambiguous “Revisit card” action. Labels should make the next action and its learning purpose obvious.
- Add a clear progress bar and a polished sequence through the practice. Preserve the learning function: these presentation corrections do not authorize deleting all practice or eliminating the learner's reasoning step.

Acceptance: inspect both diagram sides at docked and narrow widths; verify the direction remains intelligible with motion disabled. Walk the practice from start through response, feedback, progress and completion. Confirm rejected labels are absent, actions are clear, and a substantive learning check remains. Do not treat a progress bar alone as proof of mastery, or mark new implementation approved without Joshua's review.

## Coverage audit of the earlier conversation, 2026-10-11

Scope: the visible conversation from the pasted handoff through the request to save a reusable bootcamp skill, the original attachment below, and the named local checkpoints. This is not an assertion that inaccessible conversations or every historical checkpoint were reviewed. User statements are authoritative; handoff summaries report earlier decisions, while reviewer suggestions and assistant implementation reports remain a separate evidence class.

| Scope and status | Direction to retain | Acceptance check |
|---|---|---|
| General teaching, explicit repeated request | Inspect the original HTML and corpus for depth, not just a definition match. Develop what the concept means, use a concrete example, then flow into interaction. Make its connection to the preceding concept obvious. | Source coverage records what the page teaches and deliberately defers; the example explains the definition before practice. |
| Necessary page, explicit correction | Use a very brief, bold, relevant subtitle. Do not restore “What can't be missing” or the confusing “Required for what” framing. Larger type and hierarchy must make the reasoning easy to follow. | Inspect title/subtitle and first screen at the actual docked width; no tiny helper-copy substitute for the central explanation. Exact replacement subtitle still requires context, not a universal formula. |
| Definition pages, earlier locked decision reported in handoff | Reuse law-school/student across sufficient and necessary pages. Do not substitute breathing, raffle, or square/rectangle on these definition pages. | Both definition pages share the anchor; this exclusion does not ban the later raffle arrow walkthrough. |
| Conditional sequence, earlier locked decision reported in handoff | Define an indicator as a word or phrase, separate it from the complete condition. Keep formal contrapositive procedures, notation, and detailed indicator lessons in their later destinations. | Definition pages explain the relationship without prematurely adding later procedural teaching; list coverage remains on-page as specified above. |
| Wording, historical preference with explicit later exception | Handoff records preference for “you are” instead of “you're” on the necessary page, not a ban on all contractions. The later exact approved paragraph above includes “you’re” and takes precedence for that paragraph. | Preserve approved copy verbatim; use “you are” elsewhere unless Joshua directs otherwise. Do not mechanically rewrite his newer wording. |
| Media, explicit request | Check the existing Kling films made for sufficiency are still present and properly placed. Joshua asked for a similar style for necessity. | Verify asset, route and playback rather than assuming preservation from filenames. New creation is a task request, not blanket permission for paid generations. |
| Motion research, explicit request | Search the second brain for the recently clipped ChaseAI material about AI motion design/video creation, even if framed around Claude. Explain how the approach might apply through Codex and use meaningful motion to teach. | Cite the actual source and distinguish demonstrated source workflow from an unverified Codex adaptation. Do not claim research itself created a video. |
| Review process, explicit request | Have Claude Code review both wording and the actual visual result after changes; answer which model actually ran. Joshua also asked for a full-page and Impeccable-style scan, including rewording, spacing and hierarchy. | Give the reviewer current screenshots or browser evidence as supported, record model/result, and run host browser checks separately. Do not claim that screenshot review operated the live UI. |
| Collaborative scope, explicit next-page reply | When Joshua says “Review the page together first,” show the page and discuss findings before implementation. | No implementation during review-only scope; later explicit fix requests supersede that pause. |
| Ongoing skill, explicit request | Save corrections throughout the build in the existing bootcamp skill so future topics do not repeat the same mistakes. | This reference is reread and updated at each authorized revision; topic-specific treatments are not blindly applied to every topic. |

Historical continuity, not new user mandates: the handoff reports interview/email practice replacing repetitive medical-school practice on sufficiency, with invited-applicant restrictions and what remains open without an invitation; necessary practice preserves a current reference letter and acceptance for review. Retain those qualifiers when revising those exercises. The old handoff describes a two-state requirement interaction and says narrated films were in a later application lesson. Those are historical implementation locations, superseded where later authorized work changed the UI or placement. Verify current code and page before reporting them as current.

Provenance:
- Original supplied handoff: `C:/Users/Joshu/.codex/attachments/34cfb64c-e3ca-4b84-a538-4fdab5f268ea/Pasted text.txt`, headed “Session Handoff — Conditional Bootcamp definitions, source review and teaching voice,” recorded 2026-10-10. Its older then-indicator wording is superseded by Joshua's later explicit correction above.
- Visible user requests in this chat: corpus/HTML depth; natural definition; brief bold subtitle; larger type and earlier interaction; whole-clause emphasis; vertical cases; pulse without Replay emphasis; Kling preservation/similar necessity media; ChaseAI research; Claude Code UI/text review; Must arrow title and direction; review-together scope; accumulated skill capture. Dictation noise is not a requirement and “Tay” does not establish another person's preference profile.
- Vault checkpoints inspected: `brainstorms/2026-09-30-conditional-curriculum/2026-10-10-necessary-definition-motion-dispositions.md`, `2026-10-10-necessary-flow-feedback.md`, `2026-10-10-necessary-motion-feedback.md`, and `2026-10-11-must-arrow-review.md` in that same directory. They distinguish reviewer findings and provisional changes from user approval.
- ChaseAI source route recorded in the conversation: `wiki/sources/claude-now-does-video-free-javascript.md`. Retrieve it before relying on its technical method; this preference audit did not revalidate the video pipeline.

## Continue the same record

For each new correction, add a dated entry here with topic/page scope, exact wording when approved, status, evidence, and a concrete acceptance check. Keep rejected wording visible only as a regression warning. Do not turn ambiguous dictation into a named person or a universal rule. Reconcile conflicts with Joshua's newest explicit direction. At completion, report what was verified and what remains provisional. Reuse the existing bootcamp-builder skill as the master workflow.

### Must-arrow review follow-through, 2026-10-11
Joshua authorized fixing the review findings and explicitly requested Claude Opus at normal (slow) speed for the next review. This run used Opus5.5, high effort, standard speed. Preserve a learner answer before feedback, specific reasoning for each wrong choice, answered-question progress, complete conditions and keyboard focus. Narrow layouts must preserve this lesson's left-to-right direction without breaking words mid-word. These are scoped corrections, not an assertion of user approval of all resulting copy. Review evidence: brainstorms/2026-09-30-conditional-curriculum/2026-10-11-must-arrow-review.md.


### Distinguish position from completion, 2026-10-11
Joshua flagged the conflicting-looking 1 of 4 answered above Question 2 of 4. Keep the question-position heading, but express progress as answered and remaining (for example, 1 answered / 3 remaining), avoiding two adjacent fractions with different meanings. Implemented label remains provisional pending his review.


### Keep the arrow lesson focused, 2026-10-11
Joshua approved the audit sequence: see the two sides, understand why, place conditions, read the arrow, try a new example. Foreground Left: sufficient condition and Right: necessary condition; align a prominent arrow between the actual conditions at every width. Immediate answer-first placement practice replaces answer-labelled click-through construction. Condense indicator/abbreviation detours. Practice must primarily test left, right, reading and sentence-order transfer. Keep law-school anchor, brief no-reversal boundary and sentence-order comparison. A visible recap must not give away a fresh transfer question. This approval authorizes direction, not blanket approval of final copy.


### Natural comparison headings, 2026-10-11
Joshua rejected "Sentence order can change. The arrow stays the same" as awkward and authorized the remaining review polish. The implemented replacement is "Two ways to say the same thing". In the arrow lesson, name the left side and right side explicitly. Teach the condition-versus-indicator distinction before practice. Keep one practice sequence and logical heading levels. Replacement wording remains open to his review.

### Name the learner task, 2026-10-11
Explicit correction: Joshua rejected the drill title "Enough, required, or still open?" because it does not make sense without missing context. Enough and required need a referent; still open is vague. It mixes condition roles with uncertainty about a conclusion, so it does not tell a learner what to do. Prefer a concrete, standalone task title and explain the actual activity in its subtitle. Check a title without surrounding lesson text: can a learner tell what they will practice? Match landing, navigation and in-drill titles. Implemented candidate: "What follows from the rule?" with a subtitle naming sufficient and necessary conditions. This wording is provisional, not quoted user approval.

### Drill names and specific instructions, 2026-10-11
Joshua explicitly named the foundation practice "Drill 1" and rejected "What follows from the rule?" as generic and unclear. Instructions must be specific to the actual drill: name its examples, what the learner does, and the sequence. Do not substitute broad labels such as Conditional logic practice for useful guidance. Keep instructions accurate to current questions; narrowing the question set is a separate curriculum change. Prior proposed title is superseded.

### Inspect questions before writing instructions, 2026-10-11
Joshua explicitly requested question-by-question review before drafting drill instructions. Drill 1 has seven questions: raffle rule alone; market rule alone; market with rain fact; museum sufficient/necessary relationship; cafe absent sufficient condition; delivery sufficient condition; raffle counterexample to reversal. Instructions should describe these actual operations, not merely list examples or generic study steps. Never reveal a correct answer in the introduction: the prior bicycle-without-winning instruction gave away the final response and was corrected to describe testing a claim.

### Describe actions, not question scenarios, 2026-10-11
Explicit correction supersedes the earlier scenario-naming guidance: Joshua does NOT want example names or question subjects in drill instructions. Personalize to the reasoning task, not the story. Inspect the questions first, then describe the learner actions, decision and feedback interaction without naming scenarios or exposing answers. Compared live Intro to LR Main Conclusion Lab landing and first active item: concise objective, select conclusion sentence, analyze selection. Drill 1 now explains identifying condition roles, deciding what is established from facts, testing a proposed conclusion, and reading feedback after selection. Live comparison also found broader content scope and an enabled Next task before answering; these are observed follow-up issues, not fixed by the copy edit.

### ASTRA showcase design authorization, 2026-10-11
Joshua explicitly requested ASTRA to redesign Drill 1 with exceptional visual taste, dimensional/3D techniques, refined typography/color and advanced motion, working autonomously through at least three meticulous iteration passes. This scoped creative freedom supersedes exact Intro LR visual-template parity for Drill 1. Preserve learner clarity, logical accuracy, task-specific scenario-free instructions, responsive access and reduced motion. Intended eventual audience is 10,000+; this is not evidence of deployment or approval to publish. Record concrete critique and changes for each pass. No need to use generated media if procedural visuals better communicate the reasoning.

### Intensive foundational practice, 2026-10-11
Explicit correction: Drill 1 needs more than seven application questions. Joshua requests definitions and identification of necessary and sufficient conditions, left/right arrow placement in varied sentences, trigger and required outcome, and conditional indicator recognition. Build depth through varied operations and explanations, aligned with preceding teaching and the next lessons. Keep indicators separate from complete conditions; trigger/outcome must not imply cause or time. Earlier seven-question descriptions above are historical, not a fixed limit. Also preserve his explicit removal of the entry storage note and the subtitle Read the rule. Use the facts. Acceptance: inspect the actual expanded sequence, test each answer path, and ensure progress/results reflect its real count. New wording remains provisional for his review.

### Progress presentation, 2026-10-11
Joshua explicitly rejected Drill 1's small answered/remaining counter and requested a more refined visual progress bar. This supersedes the earlier specific answered/remaining display preference for this drill. Implemented candidate: continuous completion rail, prominent percentage, brief start/in-progress/completed state. Keep question position separate and only advance completion after checked answers. Verify narrow widths and reduced-motion support. Visual treatment remains open to his review.

### Necessary-condition rule and indicator presentation, 2026-10-11
Status: explicit browser corrections in the current conversation; directions to implement, not accepted implementation.

- In the case-comparison panel, state the actual rule: **If you are enrolled in law school, then you are a student.** Replace the generic instruction "Keep the same rule. Choose a person and see what their situation tells you." The rule must remain visible and intelligible while comparing cases.
- State explicitly that the indicator words help identify the **necessary condition**. Do not substitute the vague label "find a requirement" for the concept being taught. Keep the indicator distinct from the complete necessary condition.
- Match the indicator-box order and the worked-example order, so learners can move through one consistent sequence. Retain the existing coverage of only, only if, only when, only where, always, requires and must; read each in its full sentence rather than treating it as a context-free substitution rule.
- Give the indicator box a clear ordered hierarchy, readable spacing and an engaging visual response on hover. Provide equivalent keyboard-focus and touch access; essential explanations cannot depend on hover alone.

Acceptance: compare the visible list and examples item by item for identical order; inspect the actual rule in every case state; verify pointer, keyboard and touch interactions and readable narrow layouts. Resulting copy and visual treatment remain provisional until Joshua reviews them.

### Extend ASTRA visual direction to the lesson pages, 2026-10-11
Status: explicit extension of creative scope to the necessary-condition and Must arrow pages, not approval of a finished design or publication.

Joshua requested ASTRA-level artistic treatment for these pages, including refined color, typography, dimensional depth and advanced motion where useful. Inspect the entire Must arrow page for awkward alignment, insufficient breathing room and weak section grouping. Keep the left sufficient condition, the connecting arrow and the right necessary condition spatially unambiguous. Artistic effects must strengthen the instructional relationship and preserve complete conditions, readability, responsive access and reduced-motion alternatives.

Complete at least **three genuine iteration passes**: inspect the rendered result closely, record concrete weaknesses, and improve them before inspecting again. Record the actual changes and verification for each pass rather than calling three screenshots three iterations. Generated imagery, GIFs and Kling media are optional means, not required deliverables; procedural visuals may better serve the explanation. Preserve existing authorization boundaries for paid tools. The intended audience of 10,000+ students raises the quality bar but does not authorize deployment or establish acceptance.

### Group 1 visibility and direct flashcard practice, 2026-10-11
Status: newest explicit user direction, relayed in this conversation; not approval of the resulting implementation.

- Make the Group 1 list easy to find on the sufficient-condition page. Do not bury it below the videos. The current implementation is reported as placing it after the law-school example; this placement report is not user acceptance or a fresh visual verification.
- Newest clarification: provide a clearly labelled **Go to flashcards** button that opens the dedicated indicator set for the page: **Group 1 conditional indicator words** on the sufficient page and the corresponding **Group 2 conditional indicator words** set on the necessary page. Keep the general concepts/terms flashcard deck separate from these dedicated indicator sets.
- Support practice of individual indicator words and phrases and clear movement among them. Direct links from individual indicators to matching cards may supplement the button; they are optional, not a replacement for the requested primary button. Preserve the existing group coverage and the distinction between an indicator and the complete condition it identifies.

Acceptance: inspect the list's position on the sufficient page, then activate each page's Go to flashcards button and confirm it opens the correct dedicated group set. Confirm the general concepts/terms deck remains separate. Verify moving among individual words/phrases with keyboard and touch, accurate naming, preservation of all group items, and correct targets for any supplementary individual links. Record implementation and verification separately from Joshua's approval.

### Each lesson must advance the course, 2026-10-11
Status: explicit review and revision direction for the sufficient-words destination.

Joshua questions the need for a separate indicator-word page after the preceding lessons and Drill 1. Inspect preceding content, the curriculum skeleton/source intent, and the next drill before revising. Cut repeated definitions, recaps and UI that add no useful reasoning task. Do not organize this lesson as word-selector tabs. Keep indicator reference and dedicated flashcard practice in their existing homes. The proposed applied lesson on selecting the complete sufficient condition is an implementation direction, not acceptance of finished wording.

Acceptance: explain the distinct skill this lesson adds, show how it prepares the next drill, and check overlap with later Keep the whole meaning. Inspect the actual rendered lesson and its interaction. Preserve useful source-backed restrictions and distinctions while removing repetition; do not equate shorter copy with complete teaching.
