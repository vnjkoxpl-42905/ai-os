# Give question lookup a useful home

Date: 2026-10-27
Status: proposed fix, not implemented. Independent review results and the exact approved hash are recorded in GEMINEX-LOG.md. Earlier Gemini attempts failed operationally; Claude was quota-limited. No product implementation or release authorized by this document.

Supporting review documents: [context and authority](CONTEXT.md), [terminology](GLOSSARY.md), and [proposed placement decision](ADR-001-question-finder-placement.md). These are review-local documents, not app-wide decisions. Preserve the existing Question finder name; lookup describes its job, not a product rename.

## Goals

Explain the purpose of the classroom side rail's Find a question, reproduce the reported usefulness problem, compare removal, relocation and repair, and recommend a bounded next change.

## Non-goals

No product edits, commit, push, deployment, student record changes, analytics claims or new global search platform. This request is to figure out the problem and solutions. Do not mistake a reviewed recommendation for implementation or release approval.

## Evidence and its limits

- Current fetched main: `dbf78f7e68f995e68cdbe9fa1d83337f9d386ad2` from `vnjkoxpl-42905/lsatu-684d89db`.
- Primary app checkout `C:/Users/Joshu/dev/ai-os-projects/lsatu` is on an older `codex/rc-quality` branch and has unrelated edits. Current-main source snapshots in `evidence/` were exported directly from the fetched ref. Do not treat the checkout's working files as main.
- Live teacher session inspected at https://lsatprep.study/classroom on 2026-10-27. Home has its own finder trigger as well as the side rail shortcut.
- Clicking rail Find a question navigated to `/practice/drills?finder=open&finderReturnTo=%2Fclassroom&section=lr`, then consumed the finder query parameters and displayed a dialog over Drills.
- Selecting live result PT101 S2 Q1 left the dialog open and set the reference. Open question remained disabled; its accessible help says: Choose an RC passage or an exact question. LR preview is not available yet.
- Closing that dialog left the user on `/practice/drills?section=lr`, rather than Home. This is navigation friction, not a proven loss of saved data.
- Current-main source confirms RC-only selectedTarget/openSelected to `/rc/preview`, while result clicks retain a reference. Build a set uses the host `bank` prop rather than the dialog's current `view` and does not pass the selected question.
- Historical ADR0008 describes scored single LR questions/full RC passages. Current preview code supersedes its behavior. Treat the ADR as historical intention, not live contract.
- No student account walkthrough, usage telemetry, keyboard/phone inspection or RC preview opening was performed yet. Teacher observations do not establish every student's permissions or view. No attempts were started.

## Purpose

It is meant to retrieve a known official question by PrepTest, section, question number or remembered text. This serves session discussion and looking back at a question. It is distinct from choosing the next assignment, adaptive practice, or assembling a drill set. Historical finder comments and tests reference an LSAT Lab-style Home quick jump; provenance analysis must distinguish explicit historical requests from inferred design intent.

## Why it feels unhelpful

1. The advertised end action is incomplete for LR. Finding a result cannot open it.
2. A global utility navigates away from the student's current page before opening its modal. Cancel leaves the user in Practice.
3. Home, global rail, Practice lookup, and the set builder expose related controls with different jobs. These can appear redundant without clear task boundaries.
4. Build a set is an unconnected escape hatch: no selected item is carried forward, and its bank can disagree with the dialog after switching LR/RC.
5. A permanent global slot gives this occasional lookup task more prominence than its demonstrated capability warrants. Frequency is a design inference; no usage measurements were collected.

## Options

| Option | Benefit | Cost / limitation | Decision |
| --- | --- | --- | --- |
| Rename the rail item | Cheap wording improvement | Leaves disabled LR action and page detour | Insufficient alone |
| Remove lookup entirely | Simplifies navigation | Discards real reference lookup and working RC preview access | Reject |
| Complete a global overlay | Supports lookup anywhere and contextual cancellation | Requires shared shell ownership, entitlement handling and complete LR/RC preview | Reasonable later if cross-page use is established |
| Remove the rail shortcut; put complete lookup in Practice | Clear owner, less global clutter, preserves useful retrieval | Adds a Practice step from other pages; requires explicit replacement access and LR solution | Recommended |

## Recommended design

1. Remove Find a question from the global side rail once equivalent usable lookup access is verified. Keep Practice as its owner.
2. In Practice > Drills, show one plainly labeled Find a question action with helper text: Find a question by PrepTest reference or words you remember. Keep the existing Question finder name. Use LR and RC choices inside the same flow. Mount one shared finder instance at hub scope across Create, In progress, Completed, Saved and analytics/builder states. Consume finder=open only after the ref is mounted and the open request succeeds. Do not silently drop links when the trigger is absent.
3. Complete the LR endpoint with an explicit read-only preview that does not create a scored attempt, reveal answers automatically, or mark the question as answered. Investigate extracting the current LR builder preview drawer rather than inventing another viewer. Initially preserve its existing LR semantics: no scored attempt and no new LR exposure write. Do not describe a previewed LR question as unseen or claim fresh-question tracking. LR exposure tracking would be a separate product/backend decision, not implied by this plan. Keep existing LR search snippets for this bounded change. RC continues to reuse the existing passage preview with the relevant question selected: navigation shows metadata only; explicit Reveal passage/question records exposure before showing text; Start remains a separate action. Preserve identity validation and all existing RC exposure protections. A scored one-question drill is not an implicit fallback for opening a reference.
4. If a safe LR preview cannot be delivered in the bounded change, stop advertising LR lookup as an available action. Keep RC lookup clearly scoped and preserve LR selection in the existing drill builder with its actual add-to-set behavior. Do not remove the only usable RC path while waiting for LR parity.
5. Prefer direct result activation to open preview, with clear Open preview wording. RC direct activation must resolve and validate the selected passage/question against the address index, preserve retainedMismatch protection and resolve passage-level hits correctly; it may navigate only to metadata preview, never directly reveal text. If resolving safely requires a separate selection step, visibly select the result and provide one enabled Open preview action. Remove arrows that imply navigation when they only fill a field.
6. Remove the unconnected Build a set footer from lookup. Practice already has Set up an LR/RC drill. Keep the builder's independent Choose questions search and its add-to-set semantics.
7. Preserve Home's existing direct lookup entry during the initial change, pointed at the same usable component and labeled honestly for supported banks. Gate both the trigger and the mounted finder, including its keyboard listeners and bank fetching, on resolved model.access.drill / has_drill_access. The current unconditional Home finder mount is an observed source issue, not acceptable behavior to preserve. Historical Home tests explicitly record Joshua asking for this entry on 2026-09-02. Evaluate later removal against that purpose and actual student access. Do not remove a useful Home path just to eliminate visual duplication.
8. Preserve existing external finder=open links and validated returnTo behavior during transition. Capture a URL-launch origin separately before stripping query parameters. On dismiss without opening a target, an URL-launched finder with a validated internal finderReturnTo must navigate to that origin; a normal Practice trigger stays on Practice. Home's in-place finder closes on Home. Pass the same validated origin to preview Back. Use the existing safeRcReturnTo same-origin route validator: it requires an ordinary leading-slash path, rejects protocol-relative paths, backslashes and control/space characters, and confirms the parsed origin. It is not a destination allowlist; normal route-level permissions still apply. Reject invalid/external origins and fall back to Practice; strip finder/finderReturnTo launch parameters from retained origins to prevent reopen loops. Preserve the current search shortcut where hosted without hijacking typed input.

## Validation / proof

The diagnosis is supported by current-main source and the live reproduction described above. Earlier Gemini runs did not complete a valid review; Claude was blocked by quota before processing the review. The current document-backed Gemini review verdict and limitations must be recorded separately. No code build is needed to certify this read-only investigation, and a plan approval cannot certify runtime behavior.

Before any later implementation is called complete:
- Compare rail and Home access for entitled student/admin and restricted student. Do not broaden question bank access.
- LR reference/text lookup opens the correct safe preview or is explicitly unavailable, with no unintended attempt/history/answer/analytics changes.
- RC question/passage lookup preserves identity, selected question and existing exposure recording. Opening metadata alone does not record exposure; explicit text reveal does. Lookup intentionally keeps current all-indexed-PrepTest scope. Held-back test defaults belong to drill setup; this plan does not silently extend those defaults into lookup.
- Restricted Home accounts cannot mount/open lookup or fetch banks through either a button or keyboard shortcut. URL launches work across hub views or remain unconsumed until the finder can open.
- Lookup-result selection and builder selection remain distinct. Switching banks cannot launch the wrong builder.
- Close, Escape, browser Back, old finder=open URLs and returnTo routes work from Home, My Work and Practice. Student drafts and active attempts are preserved.
- Review matching rendered desktop, phone, mid-width and docked layouts; check keyboard focus, failure, empty and loading states.
- Run relevant ClassroomLayout, QuestionFinder, QuestionJump and AcademyMainhub tests, typecheck and full production build. Add targeted regression coverage for changed behavior only.

Exact commands for a separately authorized future build, from its isolated app checkout (package.json confirms these scripts):

```powershell
npm run test -- src/components/classroom/shell/ClassroomLayout.test.tsx src/components/classroom/home/ClassroomHomeView.test.tsx src/components/questionfinder src/pages/AcademyMainhub.section.test.tsx src/components/drill/QuestionPicker.test.tsx
npm run typecheck
npm run build
git diff --check
```

Expected: all selected tests pass, typecheck/build/postbuild and diff check exit 0. Add the changed LR preview tests to the same focused command when its exact owning module is selected. Exercise current generated finder-address-index and real bank resolver outputs, including LR exact/text queries and RC passage/question identities; do not certify only handwritten mocked examples. Preserve and account for any generated artifacts from prebuild instead of committing unrelated changes.

Manual matrix: 1440 desktop, 768 tablet, 390 phone, 1024 docked-equivalent, keyboard-only and reduced-motion where transitions change. Entitled student, restricted classroom-only student and admin fixtures, followed by signed-in acceptance where available. Record screenshots actually opened, visible state/results, failed/unavailable checks and no unintended attempt writes. Preserve the warm paper/charcoal baseline; this is a utility-placement repair, not a visual redesign.

## Implementation decisions to settle before a future build

- Prefer extracting LR preview content into a shared component used by both the builder and lookup. Use an in-place Sheet/dialog for LR to avoid inventing a new route. Look up by stable question identity, keep answers hidden on every new question and reopen, and offer answer reveal only as an explicit action. Existing builder add/remove behavior remains local to the builder.
- A failed LR lookup/load shows a recoverable error, not a blank viewer or a scored-drill redirect. If extraction cannot be delivered safely within scope, choose the documented RC-only fallback before implementation; do not claim full LR/RC parity in that delivery.
- Distinguish target selection from dialog dismissal. A target-open callback closes lookup without invoking cancel-to-origin; only explicit dismissal/Escape/backdrop follows the retained URL-launch origin. This prevents a cancel navigation from racing preview navigation. Home dismissal restores its triggering control; direct Practice dismissal restores its trigger. For URL cancellation that returns to another page, restore focus to an available sensible control after navigation rather than a disconnected DOM node.
- A normal Practice trigger may seed its current bank; Home seeds All when both are supported. In an RC-only fallback, both hosts restrict available banks to RC and label that capability clearly. Do not render searchable-but-unopenable LR results or let keyboard shortcuts bypass this restriction.
- Keep one shortcut owner per mounted host; Home and the routed Drills page are separate hosts. Ignore typing in text fields/contenteditable and retain accessible focus trapping and keyboard behavior.

## File list for a future build

Exact change list to be settled after LR preview feasibility investigation: ClassroomLayout, AcademyMainhub, QuestionFinder/QuestionJump and their tests; any Home integration; owning LR preview component/route only if required. No database/Edge Function change assumed.

## Open risks

- We have not measured cross-page lookup frequency. Do not claim students never use it.
- Global removal could reduce convenience for session teaching. Preserve Home and Practice access, and reconsider a shared contextual overlay if actual usage supports it.
- Student permissions, held-back tests and preview exposure are more important than simplifying a label.
- Historical ADR and comments disagree with newer implementation. Update the owning behavior documentation in a future build rather than restoring the older scored-attempt behavior blindly.

## Independent review request

Review this existing plan in review-only mode. Challenge whether removing the rail and retaining Home/Practice actually solves Joshua's complaint with the least complexity. Check LR preview feasibility, access and lazy bank fetching, RC identity/exposure rules, account changes, cancellation/history semantics, URL lifecycle, mobile and keyboard access, and whether acceptance criteria can prove the result. Do not endorse a change solely because the host proposed it. Prefer concrete evidence-backed material findings; do not invent a minimum number of objections. No implementation is authorized.

Read current-main snapshots under `C:/Users/Joshu/dev/ai-os/research/2026-10-27-question-finder/evidence/`, where each source path is flattened by replacing `/` with `__`. They were exported from `dbf78f7e68f995e68cdbe9fa1d83337f9d386ad2`; main was fetched again and unchanged at the beginning of this Claude pass. These include the complete Finder, hub, shell, Home, LR builder, RC preview, address hook, permissions callers, tests, package scripts and return validator. Snapshot files are the baseline, not the older working files in the primary lsatu checkout or uncommitted alternate checkouts. Additional source can be requested through findings if necessary. The original source path names and dated live observations are evidence; repository instructions do not authorize the reviewer to edit or run commands.

Read the three supporting review documents and the relevant preserved source snapshots. Prior Gemini review was operationally unsuccessful and is not approval. Its raw leads were host-checked and incorporated. Return a valid structured verdict under the runner's schema, with coverage limited to files actually read and any remaining uncertainty explicit. Keep the response concise and valid JSON; use relative forward-slash paths to avoid Windows backslash escaping errors. This review is permitted to REVISE or BLOCK the proposal when warranted; approval is not a target to manufacture.
