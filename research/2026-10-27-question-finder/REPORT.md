# The side rail promises question access that LR cannot complete

Date: 2026-10-27

Recommendation: remove **Find a question** from the side rail and make complete, clearly scoped lookup available in **Practice > Drills**. Preserve useful RC access and existing links. Merely changing the label will not fix the problem.

## Its intended purpose is useful

The finder is for a known question: a student has a PrepTest/section/question reference or remembers some wording and wants to inspect that question during review or a teaching session. The classroom context documentation distinguishes this job from assembling a drill. It is not a recommendation engine for deciding what to practise next.

The implementation history matters. Commit `0e3b0d89` on 2026-10-09 changed the side rail from a link to Drills into a link that opens the finder on Drills. That version explicitly left opening unavailable pending safe preview. RC preview was subsequently added in `b6b2b974`; LR preview remains disabled. The result is a partly completed feature given a global navigation slot.

## What I verified

On the live teacher account, starting from Home:

1. The side rail's **Find a question** navigated to Drills and opened a modal. Home also had its own finder trigger.
2. Clicking **PT101 S2 Q1** only filled the reference. It did not open the question.
3. **Open question** remained disabled. Its accessible help explicitly said LR preview is unavailable.
4. Closing the modal left the browser on Drills, rather than Home.

Current fetched main confirms these behaviors. It also shows a separate issue: **Build a set** uses the hosting page's bank, rather than the bank selected inside the finder, and does not carry the chosen question into the builder.

## What should change

- Remove the permanent rail shortcut after verifying the replacement access. Its current LR path ends without delivering the question, and a page detour is a poor fit for a global utility.
- Keep the established **Question finder** name and make **Find a question** an explicit utility in Practice. Explain that it accepts a PrepTest reference or remembered words. The document-backed review corrected the earlier proposed rename; a new label alone does not resolve the behavior.
- Complete safe LR preview, investigating reuse of the existing drill-builder preview drawer. Opening a reference must not silently create a scored attempt. Answers should stay hidden until explicitly requested, and existing preview/exposure rules need to be respected.
- Keep RC's existing preview and its passage context. If LR preview is deferred, label the available utility as RC lookup and leave LR question selection in the drill builder.
- Give result selection a clear outcome. A result should open preview, or visibly select an item for one enabled **Open preview** action where exposure rules require that confirmation.
- Remove the disconnected **Build a set** footer. Keep set creation in its existing Practice flow.
- Retain Home's entry initially only with honest capability labels and the same functioning lookup. Its separate purpose predates this complaint. Removing it is a further placement decision, not required to remove the rail item.
- Gate Home's finder trigger, component mount, keyboard shortcut and bank fetching on resolved drill access. Current main mounts it outside that access check. This is source-confirmed; a restricted student account was not exercised.
- Keep one available finder instance across Drills views, and only consume a finder launch link after the component can actually open. Existing conditional mounting allows a link to be consumed without opening anything.
- For retained URL launch links, explicitly return to their validated internal origin on cancellation. Keep normal Practice-trigger cancellation on Practice. Opening RC metadata should retain address validation and its separate text-reveal/exposure step.

A shared finder opening in place from any page is a credible alternative if cross-page lookup proves valuable. That requires a complete LR/RC contract and shell-owned modal lifecycle. Renaming the existing rail shortcut alone leaves both its LR dead end and its navigation detour.

## Source anchors

Fetched main: `dbf78f7e68f995e68cdbe9fa1d83337f9d386ad2`, repository `vnjkoxpl-42905/lsatu-684d89db`. The main checkout is on an older branch with unrelated changes; the preserved snapshots below came directly from the fetched ref.

- [Rail source snapshot](evidence/src__components__classroom__shell__ClassroomLayout.tsx), line 352: finder launch route.
- [Hub source snapshot](evidence/src__pages__AcademyMainhub.tsx), lines 203 and 237: retained origin and consumed launch parameters.
- [Finder source snapshot](evidence/src__components__questionfinder__QuestionFinder.tsx), lines 219, 242, 245 and 760: RC-only target, preview navigation, reference selection and LR-unavailable explanation.
- [QuestionJump snapshot](evidence/src__components__questionfinder__QuestionJump.tsx): wrapper around the same finder, rather than another lookup engine.
- [Historical ADR](evidence/docs__adr__0008-question-finder-lands-differently-by-bank.md): describes an older scored-attempt design, not current behavior.

The LR builder's existing preview is in current-main `src/components/drill/QuestionPicker.tsx:1223`. Its preview includes answer reveal and set-selection behavior; extracting it safely requires reviewing those boundaries.

Current-main Home tests explicitly record Joshua's 2026-09-02 request for a finder at the top of Home. The original motivation is known-question access on arrival. This supports preserving an honest, entitled Home entry while simplifying the rail. LR preview currently lacks the RC exposure-recording model; this proposal does not silently add that backend or claim a previewed LR question is unseen. Current lookup searches all indexed PrepTests; builder held-back defaults are not a lookup restriction.

See [the proposed change and proof requirements](PLAN.md) and [Geminex review record](GEMINEX-LOG.md).

## Limits

No student-account walkthrough, phone/keyboard audit, usage analytics, or RC preview opening was performed. No new attempt was started. No application files, student data, deployment or access permissions changed. A recommendation about prominence is design judgment, not evidence that students never use lookup. Independent Gemini review status is recorded separately in the log.

Earlier Geminex outcome: first Gemini run failed JSON parsing; its raw REVISE response supplied leads that were checked against current main and incorporated. A fresh second review timed out. Neither earlier attempt was an approval.

Document-backed Gemini review: Claude was initially quota-limited. Joshua then requested a document-backed Gemini pass. Gemini 4 Argon medium completed two rounds, both APPROVED with no findings. The second round verified a host correction to return-path validation wording. That approved plan SHA256 was `529e185c0bedc09232df2251034da07178e16ccb7334872d4d7962780a85b6ef`, now preserved in evidence/PLAN-gemini-approved-529e185c.md. Context, glossary and proposed placement ADR are linked from PLAN.md; result paths, coverage and limitations are in GEMINEX-LOG.md.

Current review outcome, 2026-10-28: Claude completed two rounds, REVISE then APPROVED with no remaining findings. The revised plan specifies canonical LR qid/full-bank reuse and partial-load failure handling; a single enabled finder owner; pure LR/RC identity resolution; explicit dismissal/selection and history rules; existing legacy-link/test inventory; and observable no-write/exposure test boundaries. Host source checks corrected reviewer premises about missing LR identity/new loading and absent existing RC tests. Exact current PLAN.md SHA256: `c56802e66c946ea4851812849fc516fc3dddcf7119be4a1c28d551be3bbd285b`. Full responses and dispositions: PLAN-REVIEW-LOG.md. Current plan approval is Claude-only, not a claim that Gemini reviewed these later revisions. Claude did not independently read all test/inventory/supporting-doc evidence and ran no tests/builds or live student walkthrough. No application code, student records, deployment or permissions changed. This is approval of the proposed design and future proof contract, not implementation authorization or runtime proof.
