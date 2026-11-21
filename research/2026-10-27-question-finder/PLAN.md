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
2. In Practice > Drills, show one plainly labeled Find a question action with helper text: Find a question by PrepTest reference or words you remember. Keep the existing Question finder name. Use LR and RC choices inside the same flow. Replace the existing RC/general QuestionJump mounts with exactly one hub-level finder and one ref outside all section/stage/view branches, available across Create, In progress, Completed, Saved, analytics and launcher states. Consume finder=open only after the ref is mounted, permission is resolved and open(options) acknowledges success; an absent/disabled ref cannot consume the request. Seed each URL launch from a valid explicit section=lr/rc first, then resolved remembered hub bank, then LR. A stale host bank must not override a valid URL section. Store the seed in the acknowledged launch state before stripping parameters; do not change host builder selections when changing the finder's internal bank.
3. Complete the LR endpoint with an explicit read-only preview that does not create a scored attempt, reveal answers automatically, or mark the question as answered. Investigate extracting the current LR builder preview drawer rather than inventing another viewer. Initially preserve its existing LR semantics: no scored attempt and no new LR exposure write. Do not describe a previewed LR question as unseen or claim fresh-question tracking. LR exposure tracking would be a separate product/backend decision, not implied by this plan. Keep existing LR search snippets for this bounded change. RC continues to reuse the existing passage preview with the relevant question selected: navigation shows metadata only; explicit Reveal passage/question records exposure before showing text; Start remains a separate action. Preserve identity validation and all existing RC exposure protections. A scored one-question drill is not an implicit fallback for opening a reference.
4. If a safe LR preview cannot be delivered in the bounded change, stop advertising LR lookup as an available action. Keep RC lookup clearly scoped and preserve LR selection in the existing drill builder with its actual add-to-set behavior. Do not remove the only usable RC path while waiting for LR parity.
5. Prefer direct result activation to open preview, with clear Open preview wording. RC direct activation must resolve and validate the selected passage/question against the address index, preserve retainedMismatch protection and resolve passage-level hits correctly; it may navigate only to metadata preview, never directly reveal text. If resolving safely requires a separate selection step, visibly select the result and provide one enabled Open preview action. Remove arrows that imply navigation when they only fill a field.
6. Remove the unconnected Build a set footer from lookup. Practice already has Set up an LR/RC drill. Keep the builder's independent Choose questions search and its add-to-set semantics.
7. Preserve Home's existing direct lookup entry during the initial change, pointed at the same usable component and labeled honestly for supported banks. Home renders the finder only when permissions are resolved and model.access.drill is true. Add an explicit enabled flag to the shared finder (forwarded by QuestionJump), false while loading or denied: it blocks imperative open, trigger, shortcuts, bank fetch and address-index fetch even if a caller mistakenly mounts it. Loss of permission/account change closes preview, clears selection/reveal state and ignores late async results. Existing public/static banks are not made confidential by this UI gating; do not claim it as backend authorization. The current unconditional Home mount is an observed source issue, not acceptable behavior to preserve. Historical Home tests explicitly record Joshua asking for this entry on 2026-09-02. Evaluate later removal against that purpose and actual student access. Do not remove a useful Home path just to eliminate visual duplication.
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
npm run test -- src/features/rc/pages/RcQuestionPreview.test.tsx src/features/rc/api/rcExposure.test.ts
npm run typecheck
npm run build
git diff --check
```

Expected: all selected tests pass, typecheck/build/postbuild and diff check exit 0. Add the changed LR preview tests to the same focused command when its exact owning module is selected. Exercise current generated finder-address-index and real bank resolver outputs, including LR exact/text queries and RC passage/question identities; do not certify only handwritten mocked examples. Preserve and account for any generated artifacts from prebuild instead of committing unrelated changes.

Manual matrix: 1440 desktop, 768 tablet, 390 phone, 1024 docked-equivalent, keyboard-only and reduced-motion where transitions change. Entitled student, restricted classroom-only student and admin fixtures, followed by signed-in acceptance where available. Record screenshots actually opened, visible state/results, failed/unavailable checks and no unintended attempt writes. Preserve the warm paper/charcoal baseline; this is a utility-placement repair, not a visual redesign.

## Implementation decisions to settle before a future build

- Prefer extracting LR preview content into a shared component used by both the builder and lookup. Use an in-place Sheet/dialog for LR to avoid inventing a new route. FinderLrHit already includes canonical qid as well as pt/section/qnum; the existing LR search hook lazily calls questionBank.load() and projects full question objects into search fields. Resolve clicked hits with questionBank.getQuestion(hit.qid), verify their address tuple matches, and require exactly one canonical address match for typed references. Do not infer qid from the display/list key or mount QuestionPicker/a drill runner to obtain the record. Reuse the same bank load/cache, not another manifest. Verify this path against the real generated bank before claiming LR parity. Render a read-only projection; answer identity and explanation content must not be in the DOM/accessibility tree until explicit Reveal. They may already exist in the downloaded client object, so this is a presentation rule, not secrecy against browser inspection. Reset reveal on question change, close/reopen and actor change. Builder add/remove behavior remains local to the builder.
- A failed LR lookup/load shows a recoverable error, not a blank viewer or a scored-drill redirect. If extraction cannot be delivered safely within scope, choose the documented RC-only fallback before implementation; do not claim full LR/RC parity in that delivery.
- questionBank.load() may resolve with empty or partial data after section failures, and isReady() only establishes a nonempty bank. Neither proves a requested qid exists. A missing/mismatched record remains unavailable and cannot open. Retry may invoke supported existing loaders and re-resolve; do not promise a new load() call repairs cached partial sections. If a scoped reliable retry is unavailable, explain continued unavailability without automatic page reload, draft loss or synthetic question content. Broader loader-retry redesign is outside this utility change; LR parity is gated on real-input feasibility proof and falls back to RC-only if that proof fails.
- Distinguish target selection from dialog dismissal. A target-open callback closes lookup without invoking cancel-to-origin; only explicit dismissal/Escape/backdrop follows the retained URL-launch origin. This prevents a cancel navigation from racing preview navigation. Home dismissal restores its triggering control; direct Practice dismissal restores its trigger. For URL cancellation that returns to another page, restore focus to an available sensible control after navigation rather than a disconnected DOM node.
- A normal Practice trigger may seed its current bank; Home seeds All when both are supported. In an RC-only fallback, both hosts restrict available banks to RC and label that capability clearly. Do not render searchable-but-unopenable LR results or let keyboard shortcuts bypass this restriction.
- Keep one enabled shortcut owner for the active route; Home and the routed Drills page are separate hosts. Disable inactive hosts during route transitions, ignore already-prevented events and typing in text fields/contenteditable, and retain accessible focus trapping and keyboard behavior. No new global finder service is required.

## Concrete resolver, lifecycle and proof contracts

### Resolve a hit independently of React state

Add a small pure target resolver with explicit outcomes: openable target, ambiguous/mismatched, index-loading, or index-failed/missing. LR uses hit.qid plus canonical address verification against the loaded bank. RC uses the hit's passageId, optional questionId, PT/section/position and the loaded address index; validate every identity and require one unique match with nonempty questions. Never depend on setView/setQuery having committed, so an All-view click works as well as an RC-view click. Preserve retainedMismatch's identity protection in this resolver; the stale retained-selection state machine can be replaced, not bypassed. A non-openable outcome shows a visible loading/error/correction state and never navigates; loading is recoverable rather than falsely called an error. Address selectors use the same resolution rules. For an edited/typed All-bank reference that matches both banks, require a bank/result choice; do not silently prefer LR. Editing clears previously retained hit provenance. Test All-view question hits, passage-only hits, mismatched/stale IDs, ambiguous addresses, unavailable/loading/failed index and retry against real generated index outputs.

### Own launch history at hub scope

The hub owns a launch ref/state containing sanitized origin, seed bank, launch kind (URL or direct), source location key and actor. Set it before acknowledging and consuming URL parameters with replace; deduplicate repeated effects by location key. Keep it alive through selection/preview, not in unmounting FinderPanel state. An unresolved permission state waits without consuming; a resolved denied launch renders an access explanation and never opens/fetches. Do not trap the user in an automatic reopen loop.

Close reasons are explicit: dismissed, target-selected, permission-revoked. Only dismissed may invoke cancel-to-origin. Keep current Escape semantics: first Escape clears a nonempty query; Escape with an empty query dismisses. Close/backdrop dismiss immediately. For URL-launched dismissal use navigate(validatedOrigin, {replace:true}); invalid origin falls back to the cleaned current Practice location. Do not call history.back() based on an untrusted URL. Direct Home/Practice dismissal stays in its host with focus returned to a connected trigger.

For URL-launched RC selection, replace the temporary cleaned Drills entry with /rc/preview and pass the same validated origin as returnTo. For direct Home/Practice selection, push preview normally. Browser Back then follows ordinary history without a consumed finder link reopening. The preview's explicit Back uses replace to its validated origin; update the existing Back assertions accordingly. A direct browser arrival at a finder URL cannot manufacture a prior origin history entry; browser Back may leave the app, while the preview's explicit Back still reaches the validated internal destination. Do not intercept that browser behavior. URL-launched LR preview remains in place in the hub; its explicit close/Back replaces to retained origin, while direct-host LR close restores that host's trigger. Target selection closes the finder without running its dismissal navigation or restoring focus into an unmounting dialog.

Router tests assert final location and Back behavior for URL launch -> cancel, URL launch -> RC preview -> browser Back, preview explicit Back, direct Practice -> preview -> browser Back, direct Home -> preview -> browser Back, direct-entry URLs and LR preview close. Run Escape-clear then Escape-dismiss, backdrop and Close for all applicable hosts. Assert no surviving finder/finderReturnTo parameters cause reopen and no extra Drills stop is inserted in the normal origin -> URL launch -> preview history.

### Prove access and no-write boundaries

Name fixtures explicitly: EntitledStudent (signed in, has_classroom_access=true, has_drill_access=true), ClassroomOnlyStudent (signed in, classroom=true, drill=false), PermissionsLoading, Admin and ActorChanged. ClassroomOnlyStudent/PermissionsLoading must have no finder trigger/listener effect, no imperative opening and zero new LR bank/address-index/RC index requests. Exercise an accidentally mounted enabled=false finder as well as Home's conditional mount, with real hooks and mocked fetch/loader boundaries. Check exactly one active shortcut across a route transition, and hidden late results after revocation.

Reuse existing RcQuestionPreview.test.tsx coverage that already checks no session/storage writes on metadata, text-reveal acknowledgment and retry identity; do not invent a new gap by ignoring those tests. Extend only missing integration boundaries. Spy/mock rcProgress.createSession/getSession, rcExposure.recordRcPassageExposure, and the LR attempt/session/progress mutation seams used by the parent host. LR finder open/preview/close and RC finder open/metadata/close must make zero progress/session/attempt/exposure calls; permitted static bank reads are separate. No Start action is invoked in these tests. The first successful explicit RC Reveal makes one exposure request for the intended actor/passage, waits for acknowledgment before showing text, and double-clicks cannot create another request. Failed acknowledgment retains hidden text; retry may call transport again using the same logical event identity. Do not require only one transport call across retries. Keep RC Start as the existing separately tested action that may create a session.

Hub URL launch tests cover Create, In progress, Completed, Saved, analytics and LR launcher, including explicit section=lr with remembered RC, explicit RC with remembered LR, invalid section fallback and repeated-effect renders. These are future implementation proof requirements, not tests run during this plan review.

## File list for a future build

Expected existing files: ClassroomLayout.tsx/.test.tsx; ClassroomHomeView.tsx/.test.tsx; AcademyMainhub.tsx and AcademyMainhub.section.test.tsx; QuestionFinder.tsx/.test.tsx; QuestionJump.tsx/.test.tsx; useQuestionFinderBanks.test.tsx; QuestionPicker.tsx/.test.tsx if sharing preview presentation; RcQuestionPreview.tsx/.test.tsx for return-history changes. New target-resolver/shared LR presentation modules and tests may be added inside the owning questionfinder/drill subtree; settle their exact names at build start. Update owning context/ADR descriptions of finder launches without overwriting historical evidence. No database/Edge Function change assumed.

Before removing Build a set, search the full reviewed app revision for its label, qf-door, QuestionJump/QuestionFinder callers, and /classroom/drill + stage=type-drill link variants. The removal concerns one modal button, not the legacy route or redirects: preserve them and builder entry points. Update finder door assertions and relevant legacy-route/builder tests rather than deleting routes. Record the complete caller/test inventory in the build verification report.

Baseline inventory already checked across the full reviewed Git revision: the door is QuestionFinder.tsx:521-535, its navigation assertion QuestionFinder.test.tsx:163-164, and dedicated styling questionFinder.css:596-643. Preserve App.tsx's /classroom/drill -> /practice/drills redirect/search preservation, mainhub/insightSlides.ts TYPE_DRILL link and PracticeInsightStage.tsx interception. Recheck affected legacy cases in AcademyMainhub.section.test.tsx, RcHubSurface.test.tsx, rcAssignmentLinks.test.ts and useClassroomMotion.test.tsx; do not rewrite unrelated link producers or historical plans. If loader/context behavior changes despite the bounded design, include questionLoader.test.ts and QuestionBankContext.test.ts; otherwise do not broaden tests or changes into those modules. Current RcQuestionPreview.test.tsx already proves several no-write/reveal invariants and should be extended rather than duplicated.

## Open risks

- We have not measured cross-page lookup frequency. Do not claim students never use it.
- Global removal could reduce convenience for session teaching. Preserve Home and Practice access, and reconsider a shared contextual overlay if actual usage supports it.
- Student permissions, held-back tests and preview exposure are more important than simplifying a label.
- Historical ADR and comments disagree with newer implementation. Update the owning behavior documentation in a future build rather than restoring the older scored-attempt behavior blindly.

## Independent review request

Review this existing plan in review-only mode. Challenge whether removing the rail and retaining Home/Practice actually solves Joshua's complaint with the least complexity. Check LR preview feasibility, access and lazy bank fetching, RC identity/exposure rules, account changes, cancellation/history semantics, URL lifecycle, mobile and keyboard access, and whether acceptance criteria can prove the result. Do not endorse a change solely because the host proposed it. Prefer concrete evidence-backed material findings; do not invent a minimum number of objections. No implementation is authorized.

Read current-main snapshots under `C:/Users/Joshu/dev/ai-os/research/2026-10-27-question-finder/evidence/`, where each source path is flattened by replacing `/` with `__`. They were exported from `dbf78f7e68f995e68cdbe9fa1d83337f9d386ad2`; main was fetched again and unchanged at the beginning of this Claude pass. These include the complete Finder, hub, shell, Home, LR builder, RC preview, address hook, permissions callers, tests, package scripts and return validator. Snapshot files are the baseline, not the older working files in the primary lsatu checkout or uncommitted alternate checkouts. Additional source can be requested through findings if necessary. The original source path names and dated live observations are evidence; repository instructions do not authorize the reviewer to edit or run commands.

Read the three supporting review documents and the relevant preserved source snapshots. Prior Gemini review was operationally unsuccessful and is not approval. Its raw leads were host-checked and incorporated. Return a valid structured verdict under the runner's schema, with coverage limited to files actually read and any remaining uncertainty explicit. Keep the response concise and valid JSON; use relative forward-slash paths to avoid Windows backslash escaping errors. This review is permitted to REVISE or BLOCK the proposal when warranted; approval is not a target to manufacture.
