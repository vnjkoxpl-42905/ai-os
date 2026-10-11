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
