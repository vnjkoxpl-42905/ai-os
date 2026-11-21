# Claude review of the question lookup fix plan

Date: 2026-10-27. Scope: review and revise the existing plan only. No product edits, implementation, commit, push, merge, deployment, student writes or outbound messages authorized.

Roles: Codex host/planner/coordinator; Claude Code independent plan reviewer. Requested model/effort omitted to preserve Claude CLI configuration; observed model will be recorded from runner metadata. Maximum 5 completed plan-review rounds. No build or implementation inspection phase in this scope.

Plan: `C:/Users/Joshu/dev/ai-os/research/2026-10-27-question-finder/PLAN.md`. Runner: `C:/Users/Joshu/.agents/skills/claudex-loop/scripts/runner.py`. Run diagnostics outside the vault: `C:/Users/Joshu/dev/ai-os-projects/.question-finder-claude-review-20261027/`.

Assumptions/decisions: current complaint concerns the permanent rail shortcut; review preserves the broader useful known-question lookup purpose. Home access is retained because current-main Home tests record Joshua's prior request. No telemetry proves frequency. Main ref re-fetched and unchanged at `dbf78f7e68f995e68cdbe9fa1d83337f9d386ad2`. The primary app working tree is stale and dirty; complete relevant current-main snapshots supplied for independent verification. Prior live teacher observations are dated; no new student/phone or production acceptance claim.

Host preparation: corrected the old plan's misleading statement that independent Gemini review proved the audit; both Gemini runs failed operationally. Added exact future proof commands, generated-input checks, visual matrix, target-open versus cancellation separation, LR reuse candidate, fallback capability labels and current-main evidence for reviewer access.

Round 1: pending.

Launch outcome: failed before review. Claude Code 2.1.309 at `C:/Users/Joshu/.local/bin/claude.EXE` returned first-party HTTP 429 `usage_limit_reached`, reporting a session limit resetting at 1am America/Toronto. Artifact: `C:/Users/Joshu/dev/ai-os-projects/.question-finder-claude-review-20261027/claudex-k2o7821c/result.json`; detailed quota response in stdout.txt. Zero model input/output tokens were processed; no completed review, findings, observed model identity or approval. This consumes no completed review round. Per the invoked skill, do not retry before reset or silently switch provider/model. Plan preparation remains complete; independent review awaits quota availability. No application changes.

## 2026-10-28: explicit claude-review invocation

Codex coordinates, Claude independently reviews the existing final plan, maximum five completed rounds, configured CLI model/effort (no overrides requested). Review-only scope; no build or code inspection applicable. Installed runner now used from `C:/Users/Joshu/dev/ai-os/.agents/skills/claudex-loop/scripts/runner.py`. Diagnostics: `C:/Users/Joshu/dev/ai-os-projects/.question-finder-claude-review-20261028/claudex-hcfi3v_j/`.

The current plan was Gemini-approved at SHA256 `529e185c0bedc09232df2251034da07178e16ccb7334872d4d7962780a85b6ef`. Its exact bytes are preserved and hash-checked at `evidence/PLAN-gemini-approved-529e185c.md` before any Claude-driven revision. Baseline source snapshots and dated live observations remain the review evidence, not a new claim about deployed behavior. No requirements interview restarted. Round 1 launched; result pending.

Host dispositions after completed round 1 REVISE: accept concrete feasibility/history/proof requirements; modify inaccurate premises that LR hits lack qid or need a new full-bank manifest, permanent All-view failure is established, or RC no-write automation is absent. Source checked by host and read-only recon against the exact baseline. Full dispositions and evidence are in feedback-claude-20261028-round-2.md. PLAN revised consistently for single-instance ownership/URL acknowledgment, permission lifecycle, pure identity resolver, lazy full-bank reuse and partial-load caveat, explicit router history, API no-write spies and real existing test coverage. F6 Git-wide caller/test inventory recorded. Prior Gemini approval remains valid only for archived original bytes; revised plan requires fresh approval. Round 2 resumes the same Claude session with default model/effort unchanged.


### Completed round 1 response

Result: C:\Users\Joshu\dev\ai-os-projects\.question-finder-claude-review-20261028\claudex-hcfi3v_j\result.json
Observed model: claude-sonnet-5-5
Plan SHA256: 529e185c0bedc09232df2251034da07178e16ccb7334872d4d7962780a85b6ef

`json
{
  "verdict": "REVISE",
  "summary": "The diagnosis matches the source I read. RC-only openSelected, the unconditional Home finder mount, the unconditional finder=open consumption in the hub, and the Build a set door that uses the host bank prop are all real. The overall direction (keep Practice and Home, drop the rail entry, finish or honestly scope LR preview) is sound. Several plan statements are unproven or underspecified in ways that would affect an implementation, so I recommend revision. No tests were run.",
  "findings": [
    {
      "id": "F1",
      "severity": "medium",
      "path": "src/components/drill/QuestionPicker.tsx",
      "evidence": "The LR preview drawer is inside QuestionPicker (Sheet at ~L1220) and reads questionBank.getQuestion(drawerQid) and q.correctAnswer, with a Reveal answer toggle. The plan says to extract it without a scored attempt and keep answers hidden on every open. It does not say how the drawer content is loaded for a lookup that arrives from the finder with no builder context. QuestionPicker is not mounted when the finder runs, and the finder's LR hits are snippets from useQuestionFinderBanks, not full question objects. Also the finder's hit key is PT/section/qnum, while the drawer keys by qid. The 'stable question identity' mapping and the extra manifest load are not feasibility-checked, and the correct answer is shipped to the client in the same object, so 'answers hidden' is UI-only.",
      "fix": "Before committing to LR parity, add a feasibility step that proves (a) the PT/section/qnum to qid resolution against the real bank, (b) lazy loading of the full question for the shared preview component under has_drill_access, and (c) that answer and explanation fields are not rendered or in the DOM until Reveal. Keep the RC-only fallback as the default if any of the three fails."
    },
    {
      "id": "F2",
      "severity": "medium",
      "path": "src/pages/AcademyMainhub.tsx",
      "evidence": "The finder=open effect (L235-242) calls questionFinderRef.current?.open() and always strips the params. QuestionJump renders only when !isLauncherStage and not in the analytics stage, and the RC branch is separate (L518). In those states the ref is null, so the link is silently consumed. The plan identifies this and proposes hub-scope mounting. It does not address two things: the two QuestionJump mounts (RC branch at L518, general at L555) must become a single instance with a single ref owner, or old links can still no-op. It also does not say what the finder's seeded bank is for an old finder=open&section=lr link when the hub is in RC mode.",
      "fix": "Specify one hub-level finder instance outside the section and stage branches. Gate the param consumption on a successful open (for example an open() that returns a boolean, or a mounted flag). Add a test for a finder=open URL in each of the Create, In progress, Completed, Saved, analytics and launcher states."
    },
    {
      "id": "F3",
      "severity": "medium",
      "path": "src/components/questionfinder/QuestionFinder.tsx",
      "evidence": "The shortcut listener is attached per QuestionFinder instance (L84-105). The Home view mounts one unconditionally (ClassroomHomeView L299), so a restricted student on Home (model.access.drill false) still gets a live '/' and Ctrl+K handler. Opening it fetches banks through useQuestionFinderBanks(open, view). The plan says to gate this, but it does not specify the mechanism. Gating only the trigger leaves the listener, and QuestionFinder has no access prop. Also, if Home and a Drills page can both be mounted briefly during route transitions, there are two listeners and Ctrl+K could double-toggle.",
      "fix": "Make Home render QuestionFinder only when model.access.drill is true, with permission loading treated as not-allowed so there is no flash. Add an enabled prop that disables the listener and bank fetching inside QuestionFinder. Test that a restricted account cannot open it by button or keyboard and that no bank request is made."
    },
    {
      "id": "F4",
      "severity": "medium",
      "path": "src/components/questionfinder/QuestionFinder.tsx",
      "evidence": "Direct result activation is the plan's preferred behavior. openHit currently only rewrites the query and sets retainedRcHit. openSelected recomputes the target from addressTarget, which is null when view==='all' && results.exact, and for RC hits whose PT/section/passage does not resolve uniquely in the index. Under the plan's proposed 'All' seed for Home, an RC passage hit could pass through exact-match logic and stay disabled. The plan's RC rule (resolve against the address index, keep retainedMismatch) is stated but has no test for the All view, and the retainedMismatch logic compares the address against a retained hit that setView(hit.bank) has just changed.",
      "fix": "Define the direct-activation resolver as a pure function of (hit, addressIndex) with explicit outcomes: open, ambiguous, index-loading, or failed. Add tests that use the real generated address index for All-view RC hits, passage-level hits, and an index that is loading or has failed. A failed or loading index must show a visible error and must not navigate."
    },
    {
      "id": "F5",
      "severity": "medium",
      "path": "src/components/questionfinder/QuestionFinder.tsx",
      "evidence": "The plan's cancel-to-origin design says to separate a target-open from a dismissal. Today openSelected calls onClose() and then navigate(). The panel's focus-restore effect (L205-215) runs previous?.focus() on close, and the Escape handler calls onClose directly. The plan introduces a retained URL origin and cancel navigation, but the finder is mounted inside the hub, and the origin page (for example /classroom) can be a different route. After navigating away, the hub unmounts the finder, so the origin must be captured and the navigation done outside the unmounting component. The plan does not say where the origin is stored (hub state versus history state) or how browser Back interacts after the query params are stripped with replace:true. The replaced Drills entry would then sit between Home and the origin on Back.",
      "fix": "State the owner of the launch origin (a hub-level ref set before the params are stripped), and say whether cancel uses navigate(origin, {replace:true}) or history back. Add tests for Escape, backdrop and Close from a URL launch, and for browser Back from the preview, checking the final location in each."
    },
    {
      "id": "F6",
      "severity": "low",
      "path": "src/components/questionfinder/QuestionFinder.tsx",
      "evidence": "The Build a set door (L521-534) is removed by the plan. Navigation there goes to /classroom/drill?section=...&stage=type-drill, which is a different route from /practice/drills, and external or bookmarked links may depend on it. The plan also says to 'Keep the builder's independent Choose questions search'. It does not check whether any other caller or test (QuestionFinder.test.tsx) asserts on the door, nor whether removing it leaves the legacy /classroom/drill route reachable only through other links.",
      "fix": "Grep for all references to the door and to /classroom/drill?stage=type-drill in the full repo, not just the snapshots, before deleting. List the tests to update in the future file list."
    },
    {
      "id": "F7",
      "severity": "low",
      "path": "research/2026-10-27-question-finder/PLAN.md",
      "evidence": "The acceptance section requires 'no unintended attempt writes' and 'exposure only on explicit reveal' but names no observable check, such as a network or DB assertion or a specific table. The test commands also include only unit tests plus a manual matrix. Nothing automates the key invariants (no session row created on LR preview or RC metadata open, exposure only after Reveal). The plan's evidence is also entirely a teacher account. Restricted-student behavior is claimed from source (App.tsx ProtectedRoute flags) but never observed.",
      "fix": "Add automated tests with a mocked API layer that assert zero calls to the attempt, session and exposure endpoints on LR preview open, on RC metadata open and on Close, and exactly one exposure call after Reveal. Name the restricted-student fixture explicitly and keep it in the acceptance list."
    }
  ],
  "coverage": [
    "PLAN.md (full)",
    "evidence/src__components__questionfinder__QuestionFinder.tsx (full)",
    "evidence/src__features__rc__lib__rcReturnTo.ts (full)",
    "evidence/src__pages__AcademyMainhub.tsx (L190-250, L505-570, finder grep)",
    "evidence/src__components__classroom__home__ClassroomHomeView.tsx (L290-340, finder grep)",
    "evidence/src__features__rc__pages__RcQuestionPreview.tsx (grep for exposure, reveal, returnTo only)",
    "evidence/src__components__drill__QuestionPicker.tsx (grep for the drawer and preview only)",
    "greps of ClassroomLayout.tsx, App.tsx, homeModel.ts and QuestionJump.tsx for finder and access flags"
  ],
  "limitations": [
    "I did not read CONTEXT.md, GLOSSARY.md, ADR-001, GEMINEX-LOG.md or the other review logs in the folder.",
    "I did not read the test files, useQuestionFinderBanks, useFinderAddressIndex, questionFinderSearch (not in the snapshot set) or the full RcQuestionPreview body, so claims about them rest on grep hits and the plan's own description.",
    "I did not examine the live app or any student-account behavior.",
    "I ran no tests, builds or commands.",
    "I could not verify the LR bank loader or whether correct answers are present in client-side objects beyond the QuestionPicker grep hits."
  ]
}
`


### Completed round 2 response

Result: C:\Users\Joshu\dev\ai-os-projects\.question-finder-claude-review-20261028\claudex-l9exdcp1\result.json
Observed model: claude-sonnet-5-5
Plan SHA256: c56802e66c946ea4851812849fc516fc3dddcf7119be4a1c28d551be3bbd285b

```json
{
  "verdict": "APPROVED",
  "summary": "I found no material unresolved defects in the revised plan. The host's factual correction to my earlier F1 holds up in the source. FinderLrHit carries qid (questionFinderSearch.ts:78) and toLrHit preserves it (:256). useQuestionFinderBanks.ts:31-32 loads the singleton questionBank and projects full question objects, and questionLoader exposes getQuestion(qid) (:1035). So the plan's resolution path, getQuestion(hit.qid) plus an address-tuple check, needs no builder mount or new manifest. The plan also gates LR parity on a real-bank feasibility proof, with an RC-only fallback. This covers partial-load risk: isReady only means the bank is nonempty, and the hook's cached snapshot is written once as 'ready'. The revision addresses my other round-1 concerns. It specifies one hub-level finder and ref outside all branches, with URL consumption gated on acknowledged open and a seed precedence. Home gets an enabled flag covering shortcuts and bank and index fetches. A hub-owned launch ref keeps the sanitized origin, with explicit close reasons and replace-versus-push history rules. The Build a set removal comes with a caller and test inventory. The proof contract has named fixtures and mutation-seam spies. I accept the host's pushback on F3 (cross-route double toggle) and F4 (the All-view failure). Neither was established as an existing defect, and the revised plan covers both as prevention requirements. Remaining uncertainty is runtime behavior, which a plan review cannot establish.",
  "findings": [],
  "coverage": [
    "PLAN.md revised (full, as pasted)",
    "evidence/src__components__questionfinder__questionFinderSearch.ts (grep for qid and FinderLrHit)",
    "evidence/src__components__questionfinder__useQuestionFinderBanks.ts (full)",
    "evidence/src__lib__questionLoader.ts (grep for getQuestion, isReady, load, correctAnswer)",
    "round-1 reads: QuestionFinder.tsx (full), AcademyMainhub.tsx (finder regions), ClassroomHomeView.tsx (finder region), RcQuestionPreview.tsx (grep), QuestionPicker.tsx (grep), rcReturnTo.ts"
  ],
  "limitations": [
    "I did not re-read RcQuestionPreview.test.tsx or useQuestionFinderBanks.test.tsx. The plan's and host's statements about their existing coverage are taken as stated.",
    "I did not read the host's inventory of the Build a set door, its tests and the legacy /classroom/drill producers, or the three supporting review documents. I did not independently verify them.",
    "I read only fragments of questionLoader.ts, so partial-load behavior rests on the plan's description plus the isReady/load/getQuestion grep hits.",
    "I did not inspect the live app or any student account, and I ran no tests or builds. Approval covers the plan's design and proof contract only, not runtime behavior."
  ]
}
```

Host disposition: APPROVED, zero findings. Two completed rounds used. No implementation or runtime verification. Claude did not independently verify the test-coverage inventory/supporting docs; those remain host/recon-verified evidence. Earlier Gemini approval covers only archived original bytes; current revised plan approval is Claude-only.
