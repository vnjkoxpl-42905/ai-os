# Full teacher Home plan and design review, 2026-10-28

Host/planner: Codex current conversation. Independent plan reviewer: Claude CLI configured default; no explicit model/effort requested, no silent fallback. Mode review, five completed plan rounds maximum. Later authorized build defaults Codex, two fix rounds/two fresh Claude inspections. No inspection opt-out. This is a user-requested full-plan review, separate from earlier bounded post-session rounds.

Plan: `C:/Users/Joshu/dev/ai-os/brainstorms/2026-09-27-teacher-command-center.md`.
App: `C:/Users/Joshu/dev/ai-os-projects/lsatu-home-polish-20261027`, existing uncommitted work preserved.
Diagnostics: `C:/Users/Joshu/.codex/verification/2026-10-28-teacher-home-plan/` outside target app/vault.

Authorization: inspect, critique and revise the plan/design direction. No full-dashboard build, commit/push/merge/publish, deployment, provider mutation or student-facing writes in this pass. Earlier live-release approval request remains unanswered.

Recon: current post-session view lacks My list, payments, access and student/enquiry email. Existing Today readers/actions can be reused with actor/role and provider-contract fixes. Current four-row student_sessions agenda is not the requested primary Calendar agenda; last_seen heartbeat is recent activity, not reliable current online connection. Explorer read source, not providers or render.

Visual evidence opened: selected material reference; final 2026-10-27 desktop fold/page and mobile fold/page. These are existing renders, not a new full-dashboard prototype. Current browser tab2 read confirms sample state. Loaded Taste v2 exact home path `C:/Users/Joshu/.agents/skills/design-taste-frontend/SKILL.md`, pinned upstream 12af471f627f866411b4bd785b19646d3672784c; compared app library editorial-greeting/achromatic-ledger, selected editorial-greeting keeping palette/type. Saved direction seed2078823331 in app `.taste-skill/review-20261028/`. No production source changed.

Host critique: (1) large assignment promotion competes with follow-up; shrink into action bar, (2) expanded session rows hide other primary jobs; compact selectable disclosure, (3) missing manual/business/email blocks are substantive gaps, not whitespace opportunities. Keep warmth, grounded surfaces and shared edges; no decorative charts/images or extra motion. New direction has not been rendered or visually approved.


## Round 1: claudex-pckp4w9s

Observed CLI 2.1.309 (Claude Code); observed model ['claude-sonnet-5-5'].

```json
{
  "verdict": "REVISE",
  "summary": "This is a narrow review. I read the plan, SignupQueue.tsx, presence.ts and the grants and RPCs in the post-session migration. I did not read the other adapters, PaymentsPanel, useGmailTodoSource, useInbox, the worker, or the lower half of the migration. The plan is mostly sound and states its limits honestly. It has four concrete gaps that should be fixed in the plan before a build is approved: unbounded RPC payloads, the one-click X in the reused signup queue, undefined consultation dedup for recurring events, and the \"reuse existing readers\" claim, which the signup read contradicts.",
  "findings": [
    {
      "id": "F1",
      "severity": "medium",
      "path": "supabase/migrations/20261027190000_teacher_post_session.sql:54-60",
      "evidence": "teacher_post_session_home() returns every unhandled task and every handled task through jsonb_agg, with no limit, cursor or total count. The plan requires \"No section grows indefinitely on Home\" and \"truthful totals\" with compact caps. After months of sessions, the handled history grows without bound, so each Home load and refresh ships all of it. Capping only in the UI would hide the true total.",
      "fix": "Have the RPC return a limited window (for example the oldest N open tasks and the most recent N handled) plus an exact open_count and handled_count. Add a paginated history RPC. Say in the plan that the Home payload is bounded and that the counts come from the server."
    },
    {
      "id": "F2",
      "severity": "medium",
      "path": "src/components/teacher/SignupQueue.tsx:20-55",
      "evidence": "The existing queue's X button sets Tier 3 in one click, and the checkmark opens a tier picker. The plan requires that access be explicit, with the resulting tier and features shown before save, and that \"opening a row never acts\". It also says to reuse these controls. Reusing as-is would keep the one-click Tier 3 decision, and a misclick would permanently take the account out of the undecided queue. The query key ['signup-queue'] has no actor scope, and the queryFn calls listManagedUsers() unscoped. The plan names the risk but does not say how it will be fixed.",
      "fix": "In the plan, require that the Home adapter replaces the X with an explicit Basic (Tier 3) confirmation showing the resulting features. Key the query by admin user id, clear it on actor change, and have the save return the account id and tier so the UI can check it targeted the selected account."
    },
    {
      "id": "F3",
      "severity": "medium",
      "path": "brainstorms/2026-09-27-teacher-command-center.md (Consultations section)",
      "evidence": "The plan says \"unique calendar/event/type\" for consultation tasks. It does not say how recurring or rescheduled events are keyed. Google recurring instances share a base id, and a rescheduled consultation keeps its event id. A key without the instance id and end time would either collapse separate instances into one task or create a second task after a reschedule. The post-session section requires state to survive rescheduling, but the consultation section has no matching rule. A cancelled or declined event also has no stated outcome.",
      "fix": "Specify the dedup key as calendar id + instance event id + type. Say what happens when the end time moves before the cue fires, and what happens on cancellation after the task exists. Cover these cases in the DB harness."
    },
    {
      "id": "F4",
      "severity": "low",
      "path": "brainstorms/2026-09-27-teacher-command-center.md (Data, actions and reuse contract: Payments and Access rows)",
      "evidence": "The plan says to reuse existing readers and actions through actor-scoped adapters, and that a known completed payment never produces another grant task. The plan itself says the original signup read must not cross-account cache, and that the historical manual-grant description conflicts with automatic grants. It does not name which readers and which tests establish that a completed credit is distinguished from an exception. The verification list names the case but gives no concrete fixture for it.",
      "fix": "List the exact reader functions and the grant_state values that separate completed, awaiting and unmatched payments. Require recorded-input fixtures for each of the three states before the Home panel is built."
    },
    {
      "id": "F5",
      "severity": "low",
      "path": "src/lib/presence.ts:3",
      "evidence": "ONLINE_WINDOW_MS is 5 minutes, and a name like \"online window\" invites reuse as \"Online now\". The plan correctly requires the label \"Active in the last 5 minutes\", but it does not say that the shared constant, helpers or existing student-facing strings must be audited so the old wording does not leak into the Home presence strip.",
      "fix": "Add a build step to grep every consumer of ONLINE_WINDOW_MS and the online helpers. Require Home to use the recent-activity wording until real presence ships."
    }
  ],
  "coverage": [
    "Read the full plan.",
    "Read src/components/teacher/SignupQueue.tsx.",
    "Grepped src/lib/presence.ts for the online window.",
    "Grepped the post-session migration for grants, RLS policies and the home and update RPCs, and read the home RPC (lines 54-60)."
  ],
  "limitations": [
    "I did not inspect PaymentsPanel, useGmailTodoSource, useInbox, scheduleEvents, the worker, the lower half of the migration, or the existing tests.",
    "I could not run tests or the DB harness.",
    "I did not verify the plan's file and command claims, such as whether model_test.ts exists.",
    "Absence of other findings is not an approval of the unread areas."
  ]
}
```


## Round 2: claudex-pmaeupq1

```json
{
  "verdict": "REVISE",
  "summary": "F1\u2013F5 from round 1 are resolved in the plan text: bounded RPC contract, safe access adapter, consultation identity, named payment readers, presence audit. Your accepted rebuttal on F3 is right. An end time must not be in the dedup key. I found no new defect in those areas, and the payment enums and attention predicate in the plan match PaymentsPanel.tsx. Four new gaps remain. The agenda's attendee-based student identity has no stored source. The approved shortcuts and per-student tracking are neither scoped in nor out. The payments reader loads the whole history on every Home load. The consultation classifier is undefined. The visual and phone acceptance gates are also untested against the proposed layout, because the only screenshots are the old sample-data baseline.",
  "findings": [
    {
      "id": "G1",
      "severity": "medium",
      "path": "supabase/functions/_shared/googleCalendar.ts; supabase/functions/gcal-sync-pull/index.ts; plan Agenda row and Calendar decision-map row",
      "evidence": "The plan says agenda session identity \"uses verified attendees\" and gives \"Calendar event link + verified student prep context\", reading from \"Cached scheduleEvents.ts, primary sync\". A grep for attendees, recurringEventId and singleEvents in _shared/googleCalendar.ts returned nothing. The plan's own historical note says gcal-sync-pull stores title, description, time, status and link, and drops attachments. The cached schedule_events agenda therefore has no attendee evidence. A Home agenda built only on it will either leave every session row without student context, or infer the student from the title or description, which the plan forbids elsewhere. The post-session worker model.ts does mention attendees, but it is a separate subsystem with owner-private storage and is not the agenda source.",
      "fix": "Add a plan step to decide where verified attendee and instance identity for agenda rows comes from. The options are extending the sync schema and pull, or reusing the worker's verified student match through a read RPC. State that rows without verified identity show no student and no prep link. Add a fixture test for that case."
    },
    {
      "id": "G2",
      "severity": "medium",
      "path": "plan Current section (Data, actions and reuse contract; Build sequence); historical Q31-Q32, Q36",
      "evidence": "Earlier approved decisions are neither carried into the current contract nor excluded. They are: the additive private booking-pass link with status and revoke (Q31\u2013Q32), brief recent test results (Q36), and per-student task progress counts and blockers with a full Tasks view (Q23). The current section says only that the full tasks view can be \"one Home sheet\". Home header actions are listed as Assign work and Open email only. The plan says conflicting historical rules do not apply, so an implementer cannot tell whether these are dropped, deferred, or still required. The booking-pass shortcut also depends on fixing the replace-balance bug in booking-pass-admin, which the current section never mentions.",
      "fix": "Add an explicit scope table for the full Home release, marking each of these as in or deferred. Name the booking-pass top-up fix as a prerequisite for the link shortcut, and record that Joshua has been told what is deferred."
    },
    {
      "id": "G3",
      "severity": "medium",
      "path": "src/components/teacher/PaymentsPanel.tsx:36-51; plan Payments row and bounded-payload paragraph",
      "evidence": "The plan tells Home to reuse loadRecordedPayments(). That function loops over stripe_payments in 500-row batches with select('*') until the table is exhausted, with no limit and no time window. The plan elsewhere requires that no Home section grows without bound and that payload bounds are a backend contract, but it applies that contract only to the task RPC. A Home mount would read all payment history, including payer emails, even though Home shows only 2\u20133 recent rows plus a count of rows needing attention. The result is a slow Home and over-fetching of personal data. The plan's \"historical unmatched sync payment\" is also a wording mismatch, because the enum value in the source is 'backfill', not 'sync'.",
      "fix": "Require a bounded Home payment reader: a recent-window query with a limit, a separate server-side count or capped fetch of needsAttention rows, and selected columns only. Leave the full reader for the history view. Use the real enum value 'backfill' in the plan and the fixtures."
    },
    {
      "id": "G4",
      "severity": "medium",
      "path": "plan Consultations paragraph; historical Live Calendar fact check",
      "evidence": "The consultation paragraph requires a \"positively identified ended consultation\". It never says how a consultation is identified. The only evidence in the plan is that 12 September events had \"Consultation\" in the title and Cal.com details in the description, and the plan itself says other and manual naming has not been checked. A title or description match is the kind of guessing the plan prohibits for students. The current section does not say whether a manual label by Joshua is persisted or how it is stored. The DB tests listed cover instances, reschedule, cancellation and declined guests, but not a misclassified title.",
      "fix": "State the classifier rule, for example a Cal.com booking marker or the manual label only. Say where a manual label is stored and that it applies only from the label time forward. Add negative fixtures for lookalike titles."
    },
    {
      "id": "G5",
      "severity": "low",
      "path": ".taste-skill/post-session-final/desktop-fold.jpg, mobile-fold.jpg",
      "evidence": "I read both images. They are the old sample-data preview: a dark Assign work promotion above the after-session list, a Students search panel, and a \"Sample data\" toolbar. This is a baseline, not the proposed design, so no visual review of the new layout is possible. As a baseline check, on the 390px mobile fold the first session's Mark handled button sits at about y=735 of 844, roughly 87% of the viewport. That would fail the plan's 60% phone criterion. The baseline also shows Mark handled on the collapsed row, while the plan says it belongs only in the expanded row, so that behavior changes.",
      "fix": "Keep the render loop as a mandatory gate. Treat the old screenshots as the failing baseline and record the 87% number as a regression target. Do not count this plan approval as visual evidence."
    },
    {
      "id": "G6",
      "severity": "low",
      "path": "src/pages/teacher/students/StudentDossier.tsx:106; src/pages/teacher/TeacherStudentDetail.tsx:120; src/components/hub/StudentOverview.tsx:220; src/pages/teacher/desk/DeskPeopleSurface.tsx:589",
      "evidence": "The presence audit you scoped is confirmed. Four surfaces call isUserOnline() and show 'Online on LSAT U' or 'Online now', and ThreadList uses isParticipantOnline. The only evidence is the 3-minute visible-tab heartbeat in usePresenceHeartbeat.ts. The plan correctly keeps these out of scope, but the Home strip may be placed next to the same teacher-side wording, which would give Joshua two different labels for the same data.",
      "fix": "Record these consumers in the plan as a known inconsistency. Either schedule a separate wording follow-up or accept the mismatch explicitly. Keep the Home test for the absence of 'Online now'."
    }
  ],
  "coverage": [
    "Read the full revised plan.",
    "Read PaymentsPanel.tsx lines 15-75 and checked the StripePayment enums, loadRecordedPayments and needsAttention against the plan.",
    "Grepped the consumers of presence.ts and the heartbeat hook.",
    "Grepped _shared/googleCalendar.ts and gcal-sync-pull for attendee and recurring fields.",
    "Checked the post-session migration for dedup keys and the home RPC call sites.",
    "Viewed the post-session-final desktop-fold and mobile-fold images."
  ],
  "limitations": [
    "I did not read the adapters, the worker, or the tests beyond grep hits: useGmailTodoSource, useInbox, scheduleEvents.ts, teacher-post-session-sync model.ts and index.ts, gcal-sync-pull in full, accessTierClient and booking-pass-admin.",
    "I did not verify the claim about label availability for Gmail enquiry classification.",
    "I could not run anything, and no tests passed or failed here.",
    "The screenshots are the old baseline, so the new design is not visually reviewed."
  ]
}
```


## Round 3: claudex-vo2ywpnl

```json
{
  "verdict": "REVISE",
  "summary": "The G1\u2013G6 dispositions are reflected in the plan, and the claims I could check against source hold. In StudentBookingPanel.tsx, `setRemaining` sends `total_credits = used_credits + DEFAULT_CREDITS`. `fetchSectionHistoryByClass` exists in `src/lib/sectionHistory.ts:92`. The `progress` route exists under the student dossier in `src/App.tsx:809`. Three small defects remain in the new text, and none needs an implementation to fix. First, the additive top-up requires retry safety but defines no idempotency key. Second, the access save contract assumes a return value that `setStudentTier` does not provide. Third, the agenda action must be isolated from the handler's worker-health writes and its full-roster scan. These are plan-text clarifications, not design reversals. I could not review the new full design visually, because it has not been rendered.",
  "findings": [
    {
      "id": "H1",
      "severity": "medium",
      "path": "plan Carry-forward scope table (booking-pass row) and 'Concrete booking prerequisite'; supabase/functions/booking-pass-admin/index.ts:145-153",
      "evidence": "The plan requires the top-up to be atomic and idempotent, and says \"retry remains 7, concurrent increments preserved\". It defines no retry identity. Without a client-generated operation key, the server cannot tell a network retry of 'add 5' from a deliberate second 'add 5'. A timeout then retry would give 12 instead of 7, or a dedup rule based on amount and time would drop a real second top-up. Today `grant_booking_access` revokes the prior active pass (line 145-153), and the existing edit path sets remaining, so neither can supply the add semantics. The key and where it is stored are an unresolved design decision.",
      "fix": "Specify a per-submit idempotency key. It should be generated when the confirm preview opens and stored with the add in a ledger row unique on (pass or student, key). The server returns the original result on replay. Add a negative test for two distinct intentional adds, and require the key to survive a page reload during retry."
    },
    {
      "id": "H2",
      "severity": "medium",
      "path": "src/lib/accessTierClient.ts:43-63; plan Access paragraph ('compare returned account id and tier/features', 'reuse its authorization and result contract')",
      "evidence": "`setStudentTier(classId, tier)` returns `Promise<void>`. It verifies preset flags internally, but it never returns the account id or the written row, so the plan's save-mismatch check has nothing to compare. If the edge function's answer does not match, the function silently falls back to a direct client `profiles` update by class_id (lines 54-61) and then verifies that row. That is a second write path, whose success depends on table policy rather than on the admin-manage-users authorization the plan says to reuse. Home would inherit it unless the plan says otherwise. The plan's 'Customize (Tier 2)' feature save also has no named mutation here. The tier writer sets presets, and the per-feature writer starts at line 65, which the plan does not name.",
      "fix": "Say Home uses an extracted variant that returns the verified written row (class_id, access_tier and flags), compares it with the selected account, and treats a mismatch as an error. State explicitly whether the direct-profile fallback is allowed on Home (recommend not). Name the per-feature mutation for Customize."
    },
    {
      "id": "H3",
      "severity": "low",
      "path": "supabase/functions/teacher-post-session-sync/index.ts:62-124,150-166,306-329; plan Verified agenda action",
      "evidence": "The existing handler records a sync attempt right after auth and before the Calendar identity check (lines 93-100). Its catch block writes an error attempt and a finish error (lines 306-329). Authenticated non-sync actions pass through the same path, gated by `recordSyncAttempt(requestAction, \u2026)`, whose body I did not read. The plan requires the agenda read to make no status writes, which needs an explicit early branch before line 93 and a separate catch. Also, the roster step lists every auth user across pages and every profile row with `select *` (lines 150-166), on every call. An agenda action that reuses it would repeat that full-roster scan on each Home refresh, and the plan sets no refresh cadence. This is a build prerequisite, not a design gap.",
      "fix": "Add to the plan that the agenda action branches before `recordSyncAttempt` and has its own error handling. Cap its refresh cadence and cache the roster and alias lookup server-side with a short TTL. Add a test that an agenda failure leaves `teacher_post_session_settings` health fields unchanged."
    }
  ],
  "coverage": [
    "Read the full revised plan.",
    "Read the handler `index.ts` lines 20-130, 148-168 and 304-333.",
    "Grepped booking-pass-admin and StudentBookingPanel for the credit paths.",
    "Read `accessTierClient.ts` lines 36-63.",
    "Grepped `sectionHistory.ts` exports and the `App.tsx` dossier route list.",
    "Re-checked earlier items: PaymentsPanel enums and attention predicate, presence consumers, the home RPC's unbounded return, and the old fold screenshots."
  ],
  "limitations": [
    "I did not read: the body of `recordSyncAttempt`; the matcher in `model.ts`; `booking-pass-admin` beyond grep hits; `manage_booking_pass`; the `StudentBookingPanel` and booking contract tests; `useGmailTodoSource`; `useInbox`; or the teacher-home RPC migrations, which do not exist yet.",
    "I did not verify the section_history RLS for admin reads across students.",
    "I ran no tests. No rendering exists for the new design, so the composition, density and phone-first claims are not visually reviewed.",
    "Approval of this plan binds only to its text, not to any implementation."
  ]
}
```


## Round 4: claudex-_tevyeom

```json
{
  "verdict": "REVISE",
  "summary": "H1\u2013H3 are resolved at plan level. The retry-key design and the agenda isolation contract are concrete, and I found no new defect in them. The H2 fix reads the admin-manage-users `set_tier` handler less closely than it needs to. The handler is a blind overwrite with no target eligibility check and no stale-baseline check, and its Tier 2 behavior contradicts the plan's 'current semantics' wording. One medium defect remains, and it is a text fix to the plan.",
  "findings": [
    {
      "id": "J1",
      "severity": "medium",
      "path": "supabase/functions/admin-manage-users/index.ts:311-336; plan Access paragraph ('Home-specific backend-only writer that invokes authenticated admin-manage-users set_tier')",
      "evidence": "The plan has the Home preset writer invoke the existing `set_tier` and compare the returned row with the expected preset. In the handler, `set_tier` validates only that class_id is present and tier is in TIERS. It then runs `.update(...).eq('class_id', class_id)` with no check that the target is a non-admin, non-archived student, and no check that the account is still undecided. Scenario 1: Joshua opens the Home access sheet for a new signup. Meanwhile the same account is decided on the Today signup queue, or in another tab, and set to Tier 1. His later Home Save overwrites that tier with Tier 3 and switches off nine feature flags, and the readback check passes because the returned row matches what Home wrote. The plan adds a stale-baseline check only for `set_custom_access`, not for the preset path. Scenario 2: a class_id belonging to an admin or archived account gets a tier and flag write, since eligibility is enforced only in the client list filter. Separately, the handler comment says Tier 2 'keeps whatever switches are there', but the code resets every flag and then sets the preset flags. The plan's 'Tier2 preserves customized switches' and 'current semantics' therefore describe behavior the code does not have.",
      "fix": "Require the Home preset writer to be compare-and-set. Send an expected prior access_tier (null for the signup queue) and refuse the write on mismatch, or add this as a new Home-only action instead of `set_tier`. Enforce server-side that the target is a non-admin, non-archived student. Resolve the Tier 2 contradiction in the plan: either Customize via `set_custom_access` is the only Tier 2 path, or state that `set_tier` with tier_2 overwrites flags. Add tests for a concurrently decided account, an admin or archived target, and the Tier 2 flag outcome."
    }
  ],
  "coverage": [
    "Read the full revised plan.",
    "Read admin-manage-users `set_tier` (lines 308-336) and grepped its other actions.",
    "Grepped the exported functions of accessTierClient.ts.",
    "Prior-round checks carried forward: agenda handler flow, booking panel and pass admin hits, section history exports, the dossier progress route, and the PaymentsPanel enums.",
    "I did not repeat the old screenshot review."
  ],
  "limitations": [
    "I did not read the manage_booking_pass SQL or booking-pass-admin beyond grep hits, nor any ledger design, since the table does not exist yet.",
    "I did not read `recordSyncAttempt`, `model.ts` or the roster cache implementation. I did not read useGmailTodoSource, useInbox or the tests.",
    "I ran no tests. No render of the new design exists.",
    "Approval would bind only to this plan text, not to code or visual quality."
  ]
}
```


## Round 5: claudex-aqlje99t

```json
{
  "verdict": "APPROVED",
  "summary": "I found no unresolved material defect in this plan text. The round 4 finding J1 is addressed. The plan now specifies a Home-only `set_home_tier` and `set_custom_access` with a row lock, compare-and-set on the expected prior tier and flags, server-side target eligibility, a verified full-row return, no direct-profile fallback, and Customize as the only Tier 2 path. Those answer the blind overwrite I verified in admin-manage-users `set_tier` at lines 311-336. The organizer edge case is real: `model.ts:109` excludes any attendee with `organizer`, and the plan's replacement rule is consistent with the agenda and matcher contracts. The rest of the plan is consistent with the earlier fixes. The remaining items are build prerequisites with named tests, not open design decisions. This approval binds only to the plan text and hash. It is not evidence about code, rendering, deployment, or live behavior.",
  "findings": [],
  "coverage": [
    "Read the full current plan, including the revised Access, Agenda, organizer, booking top-up and Consultations sections.",
    "Re-checked source facts across rounds: admin-manage-users `set_tier` (lines 311-336), accessTierClient writers, the post-session handler `index.ts` (auth, attempt, finish and catch flow), `model.ts` attendee filter (lines 18-21 and 109-110), the migration RPC and grant structure, and the PaymentsPanel enums and attention predicate.",
    "Also checked the presence helper consumers, StudentBookingPanel `setRemaining`, `sectionHistory` exports, and the dossier progress route.",
    "I viewed the old post-session-final desktop and mobile fold screenshots, which are the baseline only."
  ],
  "limitations": [
    "I did not read the manage_booking_pass SQL or the booking-pass-admin body beyond grep hits, the `recordSyncAttempt` body, the rest of model.ts, useGmailTodoSource, useInbox, scheduleEvents.ts, or any test file.",
    "I did not verify that the profiles table can support the 'expected flags/revision' compare-and-set, or that section_history policies allow the multi-student read.",
    "I ran no tests and checked no deployed behavior.",
    "No render of the new design exists, so composition, density and the phone 60% criterion are not visually reviewed.",
    "Approval of the plan is not a guarantee of the finished product."
  ]
}
```

Final approved plan SHA256: 2cc1f4f713b3918fbb426e4f38b6e498254bf91d4717e471b1f10223bebc3740. Five completed rounds used. No code build/inspection or new full-design render in this pass.

Runner approval check passed: Approval matches the current plan. Source/test paths cited in the proof command were checked for existence; scoped plan whitespace check passed. Host feedback files: `2026-10-28-teacher-home.feedback-1.md` through `feedback-4.md`. No post-approval plan edits. Requested reviewer model: configured CLI default; observed Claude Sonnet5.5, CLI2.1.309. Current app sample preview remains unchanged; approval covers plan text only. New render, implementation, RLS/provider and laptop-off acceptance remain mandatory future gates.
