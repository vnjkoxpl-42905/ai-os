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

### Integrate complete source banks through a progressive course, 2026-10-11
Status: explicit implementation authorization, not acceptance or publication.

Joshua wants the finished course, not another isolated prototype or plan. Create the conceptual contrapositive note first, compare the actual Intro to LR lesson/drill progression, then integrate every source question at the point its prerequisites have been taught. Preserve the existing 24 foundation questions; rewriting them is not required. Keep familiar statements when the learner performs a new operation. Preserve all original source text and record corrections separately. Improve interaction and visual design, not merely copy worksheets into cards. Show the complete sequence at the end.

Implementation direction: concept and example, learner decision, explanation; then indicator selection, complete-condition placement, forward diagrams, faithful if/then rewriting, formal contraposition, and full mixed practice. Keep prose self-review distinct from reliable automatic checks, local-device persistence distinct from account records, and source coverage distinct from mastery. Entire-bank availability does not require one long sitting. Provide short-session resume and review.

### 2026-10-11: source procedure matters as much as coverage

- Joshua rejected the legacy sufficient-practice drill after source-bank integration. Counting imported items does not prove that the source teaching procedure was implemented. Audit every existing drill route alongside new source sets.
- Preserve the notes' progression: indicators, complete conditions, learner-defined symbols, original arrow, contrapositive, English readbacks. Introduce each prerequisite before testing it.
- Fade assistance across the course. Guided recognition can supply choices; independent translation must begin with blank production and withhold models until the whole attempt is written.
- Keep one active operation, the source rule in view, readable stage progress and specific feedback. Correct objectively wrong answers before advancing; label written comparison honestly as self-review.
- Validate actual rendered contrast, responsive layout, stage gating and draft recovery. A source import, passing tests or a wrapper stylesheet alone is not a polished drill.

## Gold standard: the Contrapositive lesson page (approved 2026-10-12)

Joshua called the finished page "perfect". Treat it as the template for every other concept lecture: same order, same density, same rules. Do not copy its wording or its examples. Rework the structure for the new topic and pick fresh examples.

**Where it lives:** `ai-os-projects/lsatu-conditional-bootcamp/src/bootcamps/conditionals/components/` (`OpeningCourseContent.tsx` `ContrapositiveNote` and `FourRules`, `ContrapositiveVisuals.tsx`, `contrapositive-visuals.css`), commit `383747e9` plus the uncommitted follow-ups of 2026-10-12. Video project: `ai-os-projects/contrapositive-video/lecture` (`script.json`, `index.html`, `build_audio.py`). Full correction log: `wiki/COPY-CORRECTIONS.md`.

### Page shape (about 600 words of text, seven sections)

1. **What it is.** Plain definition first, in a navy panel, then one short example. No run-up.
2. **Why it matters or what it gives you.** Two or three sentences. The key term pulses, one exclamation at most.
3. **Watch the lesson.** A 60 to 90 second narrated video placed after the idea is introduced. Captions track, poster image, written fallback that only renders when opened or when the video fails.
4. **How to write it.** Two bold steps (Step 1 and Step 2), then an interactive demo with "Step 1. Click here to ..." and "Step 2. Click here to ..." buttons. A second demo uses a fresh, simple, intuitive example where one side already starts negated, so the rule that two nots cancel is shown, not stated. Each demo shows the rule as an if-then sentence above the diagram and the result as an if-then sentence below.
5. **What it is not.** One line, then slim cards: red "Wrong" for each look-alike, green "Right" for the answer. Badge, one-line change, diagram. Nothing else.
6. **A short habit paragraph.** One paragraph, no list.
7. **Pop Quiz.** Centered title with a letter-pop and light-sweep effect. Four items, one at a time. Ideas shown as short phrases, never letters. Right answer explanation is one sentence (the answer as a natural if-then). Wrong answer explanation is "Not that one." plus one specific reason about that choice. No intro paragraph, no category tag lines.

### What Joshua wanted (keep)

- One main example carried through the page, plus one fresh second example. Never the same example in more places than that, and never an example already used on another page.
- Natural if-then sentences for every rule and result. Diagrams support the sentence; they never replace it.
- Bold numbered steps. Controls say what to click. The student drives; nothing autoplays.
- Colour carries meaning and travels with the idea (amber sufficient, teal necessary). Wrong looks wrong (red, X); right looks right (green, check).
- Sleek, high-end visuals. A new effect for each new moment; never reuse the same trick. Every animation has a still equivalent and stops under reduced motion.
- Short. When a page feels like too much, cut sections, not words: remove whole parts that repeat what the video, a demo or the quiz already does.
- Ideas in quiz diagrams are condensed statements ("On the list", "Wristband"), not letter codes.
- Narrated video in his voice standard, AI voice acceptable, built from the same wording as the page.

### What Joshua rejected (never repeat)

- A squiggle (~) for negation anywhere. Use the word "not" or a diagonal strike from the idea's top left to bottom right.
- The raffle, coat, coffee, breathing, elevator, door and any example already used elsewhere. "Door", "patterns" and "move" as student words.
- Sophistry and obligation metaphors ("promise", "depends on", "nothing to stand on"). Stock encouragement and run-ups ("Here's the good news", "Every time:").
- Content repeated on the page, a legend that restates what a pill already says, a paragraph before the quiz explaining the quiz, tag lines that add nothing.
- Complicated interactives: the first light-bulb stage (wires, chips, extra buttons) and the "four worlds" picker were both cut as too busy. One idea, one control, one sentence.
- Long answer explanations. Explanations that talk about the diagram ("both ideas get a not") instead of saying the answer in plain English.
- Letters standing in for ideas.

### Process that produced it (work backwards from this)

1. Write the section list above for the new topic before any copy. Cut anything the video, a demo or the quiz already covers.
2. Draft prose in Joshua's voice, then run the `humanizer` skill over it and the corrections log. No em dashes.
3. Build the visuals one at a time, check each on the live preview (not only in tests), and ask what is new about each effect.
4. Pin the page order and the key phrases in the content test; update the test when a section is deliberately cut.
5. Video: one script file, narration synthesized per sentence, word timings for sync, scenes built in the page's own palette, rendered and checked frame by frame. Voice: Kokoro af_heart (author grade A) when no paid voice key exists.
6. Log every new correction in `wiki/COPY-CORRECTIONS.md` and here before moving on.

### Necessary definition and careful door metaphor, 2026-10-13
Explicit direction: Joshua's wording "The necessary condition is what you can guarantee will occur if the sufficient condition happens." leads the "Where the certainty is" section of the Necessary page. The door metaphor from his source may be used carefully (sufficient opens the door; necessary is guaranteed on the other side). This narrows the earlier blanket rejection of "door" as a student word; "door" as a unit of content stays banned. Avoid copy that sounds AI-written. Acceptance: read the section aloud; the metaphor must not suggest cause, timing, or that the necessary condition is only true behind the door.

### Drill review corrections and future authoring contract, 2026-10-14

Status: explicit user corrections in this conversation, including the seven sufficient-drill browser annotations. These are requirements, not acceptance of resulting implementation. Prior assistant reports of fixes, tests, assignments or publication are not verification evidence in this capture.

Scope and continuity: applies to future bootcamps, drills and quizzes where the interaction fits. Preserve earlier approved wording, source provenance and topic-specific exceptions in this same ledger. The existing historical sections are the retained earlier record; this entry does not claim every historical conversation was reviewed. Continue the conditional topic through `brainstorms/2026-09-30-conditional-curriculum/`, especially `2026-10-11-staged-drill-repair.md`, `2026-10-12-sufficient-source-notes.md` and the current topic checkpoint. Earlier self-review-only writing requirements remain historical; the newest semantic-grading request below supersedes them for the current sufficient rewrite step once reliable grading exists.

**Entry and active practice**
- Keep full drill instructions on the entry page. Once practice starts, focus on the current operation, the given rule, the learner response and useful feedback. Do not repeat the entry instructions on every question.
- Remove the broken three-step entry demonstration from Spot the condition; do not keep a redundant preview solely because a component exists. This does not forbid a useful, task-specific demonstration elsewhere.
- Remove the redundant `Select one answer.` helper. Do not fill active practice with unnecessary labels or definition legends; remove the sufficient/necessary legend from this sufficient-practice scene.
- Keep the rule visible and stable. Submitting an answer must not automatically expand the same sufficient/necessary diagram and generic read-left-to-right lesson after every question. Any expansion must teach the particular operation and be deliberately useful.

**Question-specific feedback**
- Explain why this answer follows from this particular rule and given facts. Address the learner's actual selected error or written response; do not repeat one explanation for every answer path.
- Keep explanations concise, clear and complete in Joshua's teaching voice. Name the relevant condition and the actual inference or missing information. Preserve scope, negation, modality and complete conditions. Do not equate a rule with an asserted fact.
- Wrong-answer feedback gives a targeted hint before revealing; repeated misses can offer `Show me`. Correct feedback should explain the reason rather than merely announcing `Correct.` A success label can remain when the explanation earns its space.
- Do not show `Revise my answer` after an objectively correct choice. Offer the useful next action. Revision belongs where correction or a learner writing revision actually serves the task.
- Give explanations a polished inline visual home with clear status, icon, hierarchy and readable spacing. The current direction is a restrained green success card and amber hint card, with depth and a short reveal where appropriate. Respect reduced motion and accessible status announcements. Do not replace persistent teaching feedback with a transient toast. The exact gradient, border, component vendor and animation are implementation candidates, not universal approved tokens.

**Progress and layout**
- Put question position in a compact, intentional progress area, not an isolated `Question 3 of 24` line crowding the question. Distinguish current position from completion; progress must reflect real answered/mastered state and the real item count.
- Joshua requested better components through the 21st.dev MCP connector for progress and feedback, and rejected the first plain alert as too basic. Research a suitable component when this scope calls for it, then inspect the actual integrated result. A library name or a successful import does not establish visual quality or approval.
- Verify the rendered docked desktop and narrow layouts, answer and hint states, keyboard access, reduced motion, progress, resume and completion. Build, tests, local preview, deployed asset and signed-in acceptance are separate evidence claims.

**Build the sufficient side: seven annotations**
1. Indicator prompt: use the intended plain question `Which word indicates a conditional relationship?` Support `word or phrase` where the actual answer includes a phrase; keep indicator and complete condition distinct. Do not ask which indicator introduces the sufficient condition at this step.
2. Remove `Revise my answer` after correct choices.
3. Remove the constant sufficient/necessary definition legend in the statement panel.
4. Replace `Which direction keeps the original rule?` with a task question about which rule or diagram represents the original statement. Candidate: `Which diagram represents this rule?` Exact new copy is provisional until reviewed; do not turn the rejected word direction into a global ban on explaining arrows.
5. Rephrase the final task as rewriting the conditional naturally. Do not call the original sentence a diagram. Candidate: `Rewrite this conditional in your own words.`
6. Do not label the textarea `Your if/then sentence` or mechanically require literal if/then syntax. Use a natural response label such as `Your rewrite` and accept equivalent language that preserves the conditional meaning. The newest annotation supersedes the earlier suggestion to say natural if/then sentence.
7. Replace generic model-answer comparison and the self-attestation `I compared the direction and complete conditions` with feedback particular to what the learner wrote. A checkbox is not grading.

**Semantic rewrite grading**
- User requested an AI grader using the cheapest eligible model Lovable offers. Verify current eligible models, capabilities and pricing when implementing; do not freeze a named model or an unverified price into this teaching standard. Model choice is backend configuration.
- Compare the learner's rewrite with the authored meaning, accepting faithful paraphrases and natural conditional expressions. Identify the actual error in the submitted response: reversal, lost restriction, negation, modality, missing condition or unrelated content. Do not merely echo the reference answer or claim a comparison that did not run.
- On unavailable service, timeout or malformed grading, show an honest retry/unavailable state. Never award correctness, mark the step complete or silently fall back to self-attestation as successful AI grading.
- Before enabling a grade-driven advancement rule, check equivalent paraphrases, a reversed conditional, missing qualifiers, changed modal strength, empty/unrelated text and service failure. Preserve draft recovery. Lovable credit-spend and deployment approval boundaries still apply.

Regression review: inspect entry and active states separately; submit correct and each meaningful incorrect choice; submit faithful and flawed rewrites; verify question-specific explanation, no automatic generic rule expansion, no success-state revise button, compact truthful progress, responsive feedback and honest grading failures. Record what passed and what remains provisional. Review drills with Joshua one by one; do not claim a complete bootcamp audit from this bounded pass.
### Check grading judgments and teaching feedback separately, 2026-10-14

Status: current-chat live-check evidence reported by the parent task; five grading calls returned correct correctness booleans, but the feedback prose failed teaching requirements. Observed failures included revealing the full answer, treating a conditional relationship as causation, and saying a rewrite matches before marking it incorrect. The implementation fix is pending, not approved.

- Check correctness judgments and pedagogical feedback separately. Accurate booleans alone do not justify saying the live grader passed.
- On a wrong answer, give a question-specific hint before revealing. Do not supply the model answer in the first corrective response.
- Do not infer causation from a conditional rule. Explain what the stated condition guarantees without adding a causal claim.
- Address the learner directly in the second person. Ensure feedback agrees with its verdict: do not praise a rewrite as matching the rule and then mark it incorrect.

Acceptance: inspect both the verdict and the complete visible feedback for faithful rewrites and meaningful errors. Verify hint-first behavior, no premature model answer, no causal overclaim and no contradiction between assessment and explanation. Report judgment accuracy and feedback quality as separate results; preserve existing model-choice requirements without adding a new model mandate.

### Keep capturing direction in the owning files, 2026-10-14

Status: explicit ongoing user direction, reaffirmed in the 2026-10-14 ledger-reconciliation request. Applies during authorized bootcamp, quiz, drill and activity edits. Capturing a direction does not approve resulting copy, implementation, publication or a broader design change.

- Update the appropriate owning files as edits happen, rather than waiting for a separate capture request. Record date, scope, evidence, explicit user direction versus provisional implementation, superseded guidance and a concrete regression check.
- Record wording corrections, rejected copy and removals in the vault's `wiki/COPY-CORRECTIONS.md`. Keep reusable teaching, feedback and interaction decisions in this ledger. Keep topic-only implementation state and acceptance evidence in the existing topic record.
- Visual standards and tokens belong to the app's `DESIGN.md` and the token sources it designates, only when the authorized scope changes those shared standards. A single activity's palette, effect or layout does not become a universal teaching requirement.
- Reconcile shared ledger updates deliberately across the owning Codex and Claude catalog and activation copies, including existing matching global copies. Preserve all unique sections, approval status, provenance and scoped exceptions; compare differences before writing and verify shared-ledger hashes afterward. This direction does not authorize unrelated file changes.

Latest Spot the Relationship entry corrections: see `wiki/COPY-CORRECTIONS.md`, section **2026-10-14: Activity entry pages must make the task visible** (`#2026-10-14-activity-entry-pages-must-make-the-task-visible`). That section owns the detailed wording corrections: visible task instructions before Start, ordinary answer language, a clearly connected example/response/reason, a usable primary Start action and truthful saving/preview behavior. Exact replacement copy and visual treatment remain provisional; the repair's colors and layout are not universal tokens.

Regression check: read that section before revising an activity entry; inspect entry and active states at docked desktop and mobile widths, confirm instructions are visibly readable and activate Start with keyboard access. Check any saving claim against the actual mode. Verify ongoing corrections reach their owning files within authorized scope and that all shared-ledger copies agree. This reconciliation updates only this ledger's six specified copies; it does not claim the Spot repair or any app implementation passed acceptance.


### Spot entry: remove attempt-policy narration, 2026-10-14

Explicit user correction: remove the entry paragraph announcing two attempts, retry hints and subsequent answer review. Keep entry instructions focused on the reasoning task and response format; give retry guidance when needed in practice. Preserve grading behavior and the separate mode/status notice. See wiki/COPY-CORRECTIONS.md, "2026-10-14: Remove attempt-policy narration from Spot entry". Regression: confirm the rejected paragraph is absent from the rendered entry and Start still works.


### Spot instruction video, 2026-10-15

Explicit user direction: use the JavaScript video-generation method captured in the second brain to make a creative Spot the Relationship instruction video and embed it inline on the page. Scope: this activity; it does not require videos on every quiz or drill. Demonstrate the reasoning task and response format, including multiple relationship types. Do not restore the rejected attempt-limit narration. Preserve user-initiated playback, captions, a faithful transcript, written instructions and a usable fallback. Exact script, voice, palette and animation are implementation candidates for review. Regression: inspect frames, then play the actual encoded media; check captions/transcript consistency and mobile inline playback. A poster or passing component test alone does not prove the video works.

### Keep optional feedback metadata separate from verdict validity, 2026-10-15

Status: current-task evidence reported by the parent: a gateway response returned HTTP 200 with `correct: true`, but reference-derived condition text in optional feedback metadata caused a downstream 503. The local fix is provisional, not user-approved.

Do not reject an otherwise verified semantic verdict solely because optional presentation fields such as condition/result use a paraphrase. Display learner quotations only when validated against the actual submission; otherwise use safe feedback based on verified evidence. This does not relax verdict correctness or validity checks: invalid verdicts, semantic-grader failures and genuine service errors remain ungraded. Regression: test correct semantic judgments with paraphrased optional metadata, ensure no invented learner quotation appears, and verify invalid judgments still cannot advance or complete the step.
### Ground the explanation as well as the verdict, 2026-10-15

Status: live QA reported in this task found a correct correctness boolean paired with an incorrect diagnosis: a missing time qualifier was described as a reversal. This is evidence of a feedback defect, not successful end-to-end grading or an approved fix.

Check semantic verdict accuracy and explanation accuracy separately. A model-provided error label is not proven merely because the verdict is correct. Ground the diagnosis in the actual learner wording and the original rule. If the claimed error cannot be verified, give a safe, specific comparison or hint based on that evidence; do not invent a diagnosis or reveal the full answer. Regression: a rewrite missing a time restriction must not receive reversal feedback unless it actually reverses the conditional relationship. Preserve hint-first feedback and existing validity/error handling.

### Spot entry: remove the video transcript, 2026-10-15

Explicit browser correction: remove the Read the video transcript disclosure and its expanded text beneath the Spot the Relationship video. This supersedes the earlier implementation direction to show a transcript on this entry page. Preserve the video, captions, written instructions and Start. Update playback-error wording so it does not point to a removed transcript. Scope: this activity, not a universal ban on transcripts. Regression: inspect the rendered entry for no transcript control or duplicate narration text, and check the video and written fallback remain usable.

### Give the drill a plain task name, 2026-10-15

Status: newest explicit user correction, relayed in the current task. Joshua rejected `Build the sufficient side` as vague and unnatural and requested simpler, more human wording. The UI worker's replacement title is a candidate pending review, not approved literal wording.

Name what the learner actually does in ordinary language. A drill title should make sense without surrounding lesson context; avoid abstract side-building labels and do not substitute a feature name for the task. Keep the entry title, active drill heading and navigation label consistent. This correction authorizes the scoped title/copy repair, not a broad shared design change. Acceptance: read the candidate title aloud, compare it with the actual operations, and inspect the matching labels in the entry, run and navigation. Preserve the newest approved/provisional status.

## 2026-10-15: RC Create must set up a new drill

Status and provenance: explicit Joshua direction relayed in the current RC Create audit task. Joshua reports that RC Create showing previous drills is broken and requests an audit/fix informed by LSAC and 7Sage. This entry records direction and pending regression checks; it is not independent reproduction, approval of literal copy or implementation, or evidence of publication or a complete RC repair. The parent owns app code and the audit report.

- Explicit direction: RC Create must create or set up a new drill. Do not list previous drills there. Existing work belongs in In progress or Completed, according to its actual status. Make starting new work clearly distinct from resuming existing work.
- Continue the standing direction to update owning design/principle files during authorized edits. Keep wording corrections in wiki/COPY-CORRECTIONS.md and reusable scoped interaction direction in teaching-preferences.md. Update app-owned design/principle files only within the parent's authorized app scope. Preserve prior decisions, unique sections and concurrent changes; do not promote this RC repair into a universal layout rule.
- Scoped implementation candidates, not approved literal wording or final design: an inline RC builder, history filtered by section and status, and truthful LR-only labeling/availability for saved sets where support is LR-only. Do not imply that an LR saved-set flow supports RC. These candidates serve the requested outcome and remain subject to actual implementation and review.
- Research boundary: use LSAC and 7Sage as audit inspiration with source attribution and clear evidence limits. Inspiration does not authorize copying their content or interface, or claiming that current authenticated competitor flows were inspected. This direction capture does not itself verify competitor behavior.

Pending regression checks for the parent audit/fix:

1. Open the exact `?section=rc&view=create` query directly, refresh it, return with browser Back, and exercise the legacy builder entry route. Each route must reach RC new-drill setup without showing existing drill rows; navigation must preserve the intended section and view.
2. Check In progress and Completed with RC and LR records in each meaningful status. History must respect both section and status, and new-drill and resume actions must remain unambiguous. Check empty histories and any LR-only saved-set labels/availability.
3. Inspect light and dark themes, narrow layouts, keyboard navigation and visible focus through setup and launch. Record rendered evidence separately from source or test results.
4. Preview must not create an attempt or write attempt progress. Freeze the selected passage/question IDs so preview and Start use the same selection rather than silently drawing another drill; verify the IDs and attempt-write behavior.

Verification boundary: these checks are requirements, not results. Report local implementation, tests, signed-in acceptance and publication separately. Do not claim this capture publishes a fix or establishes that all RC is fixed.
