# RC Training must work reliably before its demonstration is produced

Date: 2026-10-16. Status: audit and proposed plan only, not an approved implementation specification.

## Scope and conclusion

Joshua requested inspection before implementation. No application code, backend schema, media, tests, builds, commits or deployments were changed or run during this audit. Browser interaction exercised the existing local preview and its connected backend. This document supersedes earlier broad statements that the local change had no blockers. Prior passing checks covered a narrower change and do not establish product readiness.

RC Training is not ready for end-to-end acceptance. A real section cannot start and history cannot load because the connected API cannot find `public.rc_recall_attempts`. Navigation also demonstrably opens training pages at the wrong vertical position. Source inspection identifies additional save/recovery risks requiring controlled failure tests after the backend works.

Audit target: `C:/Users/Joshu/dev/ai-os-projects/lsatu-reading-center-rc-recall`, local preview at `http://127.0.0.1:8080/reading-center/rc-recall`. This is not a production audit. The working tree includes untracked feature files, which must be included in subsequent review and handoff.

## The educational contract

The authoritative Cappuccino notes specify this sequence:

1. Read and translate a whole paragraph, preserving details, relationships and qualifications. Brief reactions help engagement.
2. Hide the text and silently recall that newest paragraph in your own words.
3. Briefly confirm against all text read so far. Find what was omitted or changed rather than starting a fresh read.
4. Continue with the next paragraph. Hidden recall remains about that paragraph; confirmation includes earlier text.
5. Optionally recall the whole passage at the end. This is particularly useful when first learning and periodically afterward.

There is one current workout under RC Training. Sentence-level hidden recall and mandatory cumulative hidden retelling are not part of this contract. The separate 35-minute Cappuccino variant removes paragraph recaps and must not be mixed into these instructions. Untimed practice with an optional elapsed display is Joshua's chosen adaptation. The source's six-minute progression benchmark is not a countdown or forced cutoff. Recall is self-checked, not automatically graded.

Primary sources:

- `C:/Users/Joshu/dev/ai-os/Loophole Lecture/Day Six/How and Why to Do Cappuccino RC Translation/ellens-notes.txt`
- `C:/Users/Joshu/dev/ai-os/corpus/loophole-online/workouts/cappuccino-rc-translation-drill/README.md`
- Decaf comparison only: `corpus/loophole-online/workouts/decaf-rc-translation-drill/README.md`.

## Findings, with evidence strength

P1 means required before acceptance; P2 means substantial usability or reliability work; P3 means polish. Source-derived risks are not claimed as reproduced failures.

| ID | Priority and evidence | Finding | Required outcome |
|---|---|---|---|
| A01 | P1, live confirmed | History requests return HTTP 404 / PGRST205: `Could not find the table 'public.rc_recall_attempts' in the schema cache`. Starting PT102 Section 1 loads its passage JSON successfully, then the attempts endpoint returns 404 and launch fails. | Verify the deployed persistence contract, then create, complete and read back a real controlled attempt. Do not treat retry UI or mocked saves as proof. |
| A02 | P1, live confirmed | From RC setup at scrollY 806.4, LR opened at 717.6. Returning to RC left scrollY 698.4 and its heading at -609.2px. Focus was BODY. | New sidebar destinations open at a predictable visible heading with deliberate keyboard focus. Browser Back restores prior location/view. |
| A03 | P1, source risk | Run position and timestamps live in React state; sidebar navigation remains available. Audio backup does not preserve paragraph/stage/timing. | Durable attempt checkpoint/resume, with an explicit leave behavior and no silent abandonment. |
| A04 | P1, source risk | Failed finalization and its duration are retained only in runner state. Back exits and clears that state. | Persist pending finalization and retry exactly once with the original duration after exit/reload. |
| A05 | P1, source risk | IndexedDB failures are swallowed; recorder ignores backup initialization failure. UI promises failed audio stays on-device. Missing chunk runs can be assembled as if complete. | Report backup health honestly; validate chunk completeness; retain a safe recovery/download path when available. |
| A06 | P2, source risk | Silent Finish does not immediately lock concurrent actions. Duplicate finish or End racing insert can leave inconsistent local/persisted status. | Guard actions immediately and reconcile idempotently with server state. |
| A07 | P2, source risk | Create failure says nothing was saved even when a lost response could follow a committed insert; retry generates a new ID. | Retain/reconcile the same attempt ID before retry or definitive copy. |
| A08 | P2, source risk | Recovery ignores failed/empty outcomes; runs only on mount; young crash remnants are skipped without scheduled retry; no-Web-Locks behavior can strand unclean recordings. Failure-marker update errors are ignored. | Visible pending/failed recovery with manual and reconnect retry; bounded cross-tab ownership; preserve errors and original work. |
| A09 | P2, live and source | Reading Progress exposes only LR Recall and Speed Reading. Dashboard also omits RC. Local RC history is capped at 50 and offers counts rather than recap playback, retry or resumable detail. | Discoverable RC history, pagination, explicit attempt/save states, recap access, and resume. Do not invent grades. |
| A10 | P2, live confirmed | Tags removes all main sidebar destinations. Its Back button returned to Speed Reading after entry from Reading Progress. | Keep global navigation reachable and label or preserve the return destination. |
| A11 | P2, live confirmed | Instructions click expands full text, but reloading the same `#rc-recall-how` URL leaves it collapsed. | URL, expanded view, Back/Forward, scroll and focus describe the same view. |
| A12 | P2, source mechanism | LR uses a separate gate/shell branch from other activities; access loading may replace the workspace. Tabs are eagerly imported within the Reading Center bundle. | Stable shell geometry and content-local loading while retaining correct access controls. Do not assume per-tab code splitting is the cause. |
| A13 | P1 teaching, visible and source | Demo starts at paragraph 2, then supplies the model recall during the recall stage. | Teach paragraph 1 first; clearly separate instructor modelling from learner retrieval. |
| A14 | P1 teaching assessment | Instructions explain actions more than why hiding/checking helps. | Explain familiarity versus recall, then show how checking reveals missing meaning. |
| A15 | P2 teaching, source | Demo check shows no actual omission/correction and paragraph 2 of 2 ends with next-paragraph wording. | Demonstrate one realistic lost qualification and its repair; end at optional passage recall or next passage. |
| A16 | P2, source | Silent recall requires a second Start click after hiding; labels alternate translation/recall; current attempt mode can display RC Flow. | One obvious next action at each stage, consistent terminology, version-aware history names without rewriting legacy methods. |
| A17 | P1 media, source | Existing recordings show instructor rather than visible passage interaction. Old instruction film combines methods, retains old labels, and manifest is unverified. | New source-faithful teaching video and verified app walkthrough. Keep old mixed-method film disabled. |
| A18 | P3, source/design | LR/RC use different font/token systems; other tabs add a separate top bar. Sidebar transitions lack reduced-motion overrides. | Shared content origin, hierarchy, header spacing and motion policy; preserve useful activity differences. |

The setup also makes unconditional save promises while the actual backend is unavailable. The future spec must define truthful unavailable, pending, saved and recovery states rather than treating copy as a guarantee.

## What the browser audit established

Visited Dashboard, LR Training, RC Training, Speed Reading, Tags and Reading Progress through their visible controls. Reproduced RC/LR scroll inheritance in both directions, Tags return behavior, omitted RC central progress, instruction deep-link collapse, history failure and real launch failure. Speed Reading landed at scrollY 0 in this sequence; that does not prove a deliberate scroll policy because shorter content can clamp the inherited offset.

Screenshots: `C:/Users/Joshu/.codex/visualizations/2026/10/16/01a14720-885c-73a1-8050-32c0d2f14473/audit-rc-before-transition.png` and `audit-lr-after-transition.png`.

Real runner execution, successful saves, completed history, playback, crash recovery and cross-account isolation remain blocked or unverified. The previous turn's synthetic two-passage run and 79 passing checks are limited prior evidence, not substitutes for this acceptance. This audit did not measure animation frame timing or run a complete keyboard/screen-reader/mobile matrix.

## Proposed experience

At entry, present a short purpose statement, a watchable complete example, and one primary Start a section action. Keep Instructions and Your attempts easy to find. Suggested purpose copy: “A paragraph can feel familiar while you are looking at it. Hiding it shows what you can explain from memory. Checking afterward shows which details or connections you lost.”

Use the same navigation model for LR and RC: predictable entry view, explicit instructions/examples views, visible return path, consistent heading focus and URL behavior. Keep the sidebar stable while content changes. Smoothness means correct destination, stable geometry and continuity first; any brief animation comes afterward and respects reduced motion.

During practice, show passage and paragraph position, current step, one short instruction and one dominant next action. Recommended silent sequence: Read → Hide and recall → Check my recall → Next paragraph. Hiding begins silent recall immediately. Spoken optional recap retains explicit recording controls and visible recording/save status. This control simplification is proposed, not approved or implemented.

Recommend resumable checkpoints rather than merely warning before leaving. Persist current stage, paragraph, elapsed accounting and pending writes per account/attempt. The spec must define whether away time counts; recommended default is to pause when deliberately leaving practice and disclose it. Do not infer inactivity from slow silent thinking.

History should distinguish in progress, completed, ended early, pending save and recovery needed. Open an attempt to resume or inspect its saved recaps. Central Reading Progress should link into the same records, with duration and completion rather than fabricated recall scores.

## Video design, not production

Produce a short conceptual lesson, approximately 2–3 minutes subject to an approved timed script, and a separate concise walkthrough of the verified app. Use an original two-paragraph passage. Keep watching separate from creating an attempt.

| Scene | Teaching point | Visual evidence |
|---|---|---|
| 1 | Why hide the text? | Show paragraph, hide it, expose the difference between recognizing and explaining. |
| 2 | Read paragraph 1 for meaning | Entire paragraph visible; connect claim, evidence and qualification with restrained highlights. Model one brief reaction. |
| 3 | Recall paragraph 1 | Hide text; label narration as an instructor example, not a learner answer to copy. |
| 4 | Check and repair | Reveal original; identify a plausible missing qualification, explain its effect, repair the account. |
| 5 | Read and recall paragraph 2 | Show that hidden recall concerns paragraph 2 alone. |
| 6 | Confirm both paragraphs | Reveal paragraphs 1 and 2; check details and their connection without restarting a full read. |
| 7 | Optional final recall | Clearly offer whole-passage recall or continue. No second workout. |
| 8 | Use the app | Capture real verified controls for section choice, elapsed display, starting, completing and finding saved work. |

Production order later: source map → original example and script → storyboard → visual design → narration/captions → frame and teaching review → approved render → playback/accessibility verification. The faceless-explainer skill fits conceptual graphics. Actual UI instruction must capture the actual verified app rather than invent its controls. Review captions at edit boundaries and text legibility at narrow player sizes. Provide transcript, keyboard playback and a playback-failure fallback. Preserve source media and derivative provenance. No media was generated, rendered, uploaded or paid for in this audit.

## Plan in dependency order

1. Resolve the audit into a testable specification. Lock learning outcomes, resume/time semantics, navigation model, history detail and the two-video boundary. Keep facts separate from design proposals.
2. Establish the backend contract in an approved environment. Verify schema, policies, storage, ownership and failed-response reconciliation before polishing save claims. Deployment routing and any Lovable credit spending require their separate explicit authorization.
3. Deliver a minimal complete real attempt: create → paragraph cycle → optional recap → finalize → history readback. Prove both silent and spoken paths where supported.
4. Add durable checkpoints, recovery and idempotency. Exercise failures before integrating global navigation so tab switching cannot silently discard work.
5. Unify sidebar transitions and view navigation across activities. Add RC to central progress. Preserve access boundaries and existing account scoping.
6. Refine the teaching UI and original interactive example against the source contract. Verify novice comprehension, not merely button operation.
7. Produce videos only after script and actual UI behavior are stable. Review teaching accuracy, captions and playback.
8. Run independent standards and specification reviews, fix findings, then complete signed-in acceptance. Production release remains a separate decision.

## Acceptance matrix for the future spec

| Area | Required checks | Current evidence |
|---|---|---|
| Setup | valid sections, loading/empty/error/retry, timer choice, no duplicate attempts | UI inspected; real launch blocked |
| Read/recall/check | whole paragraphs; correct visibility; newest paragraph recall; cumulative check; single next action | source reviewed; prior synthetic flow only |
| Passage pair | A then B; headings excluded; selected confirmation scope accurate | source reviewed, real run unverified |
| Passage end | skip optional recall; silent/spoken recap; next passage; final completion | real run blocked |
| Timing | elapsed only; passage reset; section total; hide display; away/resume semantics | prior synthetic evidence; persistence unverified |
| Save | success readback; double-click; lost response after commit; offline; failed finalization | live failure confirmed; other cases unverified |
| Recording | permission denied; interruption; zero bytes; quota/IndexedDB failure; missing chunks; playback | source risks; live cases unverified |
| Recovery | reload, tab change, browser crash, reconnect, cross-tab lock, no Web Locks | source risks; controlled tests required |
| History | completed/unfinished/pending/failed; pagination beyond 50; recap access; resume; legacy naming | history unavailable; central omission confirmed |
| Privacy | account-scoped queries, storage ownership, sign-out/account switch, isolation | protective source patterns present; acceptance unverified |
| Navigation | all sidebar pairs; scroll/focus; Back/Forward; direct URLs; loading; drawer | desktop sample confirmed defects; full matrix pending |
| Accessibility | keyboard sequence, focus visibility, announcements, contrast, reduced motion, zoom, 320/768/1024/1440 widths | not certified by this audit |
| Learning/media | novice explains purpose/sequence; preserves details; identifies omission; captions/playback failure | teaching defects and storyboard documented |

## The workflow Joshua was asking for

The local `/ask-matt` router supports specification-driven development with a separate implementer and reviewer. Use the stronger reasoning model for audit, decisions, specification and final review. Use a cheaper model for small, bounded implementation tickets once acceptance criteria are settled.

Route: `/ask-matt` → audit and decision resolution (`/grill-with-docs` where useful) → `/to-spec` → review specification → `/to-tickets` → fresh-context implementation per ticket → `/code-review` on two axes, standards and specification → acceptance and retrospective.

This turn completes the audit and proposed plan. It does not approve a specification, publish issues, authorize implementation or dispatch another model. The next model should produce the specification from this evidence, not jump directly to coding. Ticket boundaries should be vertical, independently verifiable slices, with backend and recovery dependencies explicit. Review must include untracked files and final working-tree state, not only committed diffs.

Relevant local workflow instructions: `C:/Users/Joshu/.agents/skills/ask-matt/SKILL.md`, its `PHASE-BOUNDARIES.md`, sibling `to-spec/SKILL.md`, `to-tickets/SKILL.md`, and `code-review/SKILL.md`. Video planning reference: `C:/Users/Joshu/dev/ai-os/.agents/skills/faceless-explainer/SKILL.md`.

### Handoff for the specification stage

```text
Develop a reviewable RC Training specification from:
C:/Users/Joshu/dev/ai-os/brainstorms/2026-10-16-rc-training-audit-and-plan.md

This is specification work only. Do not implement, deploy, publish tickets, spend credits or produce videos. Read the applicable repository instructions and inspect current state before relying on the audit. Preserve unrelated work and include untracked feature files in your inspection.

Use the original Cappuccino sources to preserve the single paragraph-recall procedure. Respect untimed practice with an optional elapsed display. Resolve the proposed navigation, checkpoint/resume, elapsed-time and history contracts. Explain any unresolved decision clearly rather than silently choosing a different teaching method.

Produce problem and outcome statements, user journeys, state transitions, failure/recovery contracts, accessibility and motion requirements, source-mapped teaching copy, video briefs/storyboards, acceptance criteria linked to audit IDs, and test seams. Separate verified facts, proposed choices and blocked validation. Include a dependency-ordered ticket proposal and an implementation handoff template, but do not dispatch it.

Require real signed-in create/complete/history readback and controlled failure tests before acceptance. Prior unit/build/synthetic evidence does not prove deployed persistence. Review the specification before a cheaper implementation model begins. The later reviewer must independently assess both specification compliance and engineering/teaching quality.
```

## Source inspection pointers

Paths below are relative to the app checkout and are evidence pointers, not a frozen implementation design.

- `src/features/reading-center/rc-recall/RcRecallPage.tsx`: 39–42 run/view state; 63–66 recovery handling; 80–91 creation/exit; 100–156 instructions; 168–175 history.
- `src/features/reading-center/rc-recall/RcRecallRunner.tsx`: 41–53 timing/position; 145–157 concurrent silent finish; 178 pending finalization; 225–257 control wording; 292–296 backup promise/exit.
- `src/features/reading-center/rc-recall/lib/attempts.ts`: 68–79 creation; 109–119 failure updates; 160 finalization; 178–187 history limits/order.
- `src/features/reading-center/rc-recall/lib/backup.ts`: 62–95 durability/chunks; 122–135 recovery branches. `useRecapRecorder.ts`: 54–68 cleanup and 88 backup initialization.
- `src/features/reading-center/rc-recall/RcTrainingDemo.tsx`: 17, 26–38 demo sequence, answer and ending.
- `src/features/reading-center/index.tsx`: 31–43 shell branches. `components/AppShell.tsx`: 58–74 outlet/focus; 109–112 Tags replacement; 134 navigation; 185 return destination; 329 top bar.
- `src/features/reading-center/pages/ProfilePage.tsx`: 90–114 activity coverage. `ReadingCenterHome.tsx`: central RC omission. Confirm exact file locations in the current checkout before editing.
- `supabase/migrations/20261016120000_rc_recall_attempts.sql`: local schema, uniqueness and policies. A file on disk is not proof of deployment.
- `scripts/rc-recall-media/README.md`: 36–46 old film and visible-text limitations. `.local-media/rc-recall/manifest.json`: unverified status. Configuration flags alone do not establish media quality.
