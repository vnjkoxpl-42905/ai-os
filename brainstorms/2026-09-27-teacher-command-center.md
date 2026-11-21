# Teacher command center: Brainstorm / Discovery Notes
Date: 2026-09-27 · Goal: Define a distinct, functional teacher Home for Joshua that brings together student progress, requests, work, messages, schedule, and Stripe activity.
Status: 2026-10-28 full Home plan reopened for independent review; current post-session implementation is a local subset, not the complete dashboard
Context sources: `brainstorms/2026-09-27-stripe-admin-home.md`; `brainstorms/2026-09-23-classroom-home-PLAN.md`; live Teacher Workspace audit from 2026-09-27; six user-supplied dashboard reference images.

## Current plan and design contract, 2026-10-28

This section is the current plan. Dated sections below preserve discovery and history; conflicting historical rules do not apply. The 2026-10-27 post-session plan remains the detailed technical contract for that subsystem, with its documented deviations below. This full Home plan does not turn its earlier approval into approval of the complete dashboard.

### Authorization and review

Joshua requested Claudex Loop to perfect the plan and design. This pass may inspect, critique and revise the plan; it does not authorize a new full-dashboard build or a release. Preserve all existing uncommitted work, local originals and student behavior. No commit, push, merge, publish, live migration, function deployment, student assignment/access mutation or message sending. Any implementation decision follows presentation of the reviewed direction. Lovable backend deployment and credit use retain their separate confirmation requirements.

Codex hosts/plans; Claude CLI independently reviews using its configured default, with requested and observed models recorded separately. Mode review; maximum five completed plan rounds. A later authorized build defaults to Codex, with two fix rounds and two fresh Claude inspections. Old budgets/results remain historical; this is a new explicitly requested full-plan review. Diagnostics outside the app checkout; full responses appended to the review log.

### What success means

Home answers: **What needs my action, and which student am I preparing for next?** It is Joshua's teaching desk. The signature object is a session with its unfinished teaching work and context, rather than generic metrics. My list is equally real work; messages never substitute for either.

The full design includes: durable after-session work, private My list, payment activity and exceptions, access decisions, student/enquiry email, upcoming primary-calendar agenda, platform messages, and small recent-student/presence summaries. Each must have a real data contract, action, empty/loading/stale/error state and destination. A feature is not complete because a sample panel exists.

Observable acceptance:

- In a five-second desktop scan, identify unfinished session work, one next session, and any payment/access/email decision. On phone, first active session identity/action begins within the first 60% of the usable viewport; no oversized greeting or assignment promotion precedes it.
- With 12 queued sessions and 8 manual tasks, Home shows compact capped lists and truthful totals; expansion/detail is accessible without burying the other categories. No section grows indefinitely on Home.
- A known completed payment never produces another grant task. An unmatched payment never receives guessed student identity. Tier mutation updates only the selected account, and never acts on opening a row.
- A completed session produces one durable task without needing a transcript; saved checklist/manual match/transcript/handled state survives refresh, retry and rescheduling. Paused/stale/failed sync does not claim an empty healthy queue.
- A private task survives reload and is invisible to students and other admins. Its handling/blocker changes cannot alter a student assignment.
- Email shows only verified student correspondence or explicitly classified enquiries. Unknown mail is not silently included as student mail. Presence is labelled by what the implementation can actually prove.
- Every production control opens the right context or saves a verified change; no sample save behavior in the authenticated app. Student Home and its feature access remain intact.

### Decision map and assumptions ledger

| Decision | Resolved choice / evidence | Cost of a wrong assumption |
|---|---|---|
| Primary work | After-session tasks plus private My list; user answers recorded below | A polished messaging page still misses Joshua's work |
| Visual language | Retain selected warm-paper/charcoal material and Fraunces/Outfit; `design/principles.md`, preserved `raw/sources/design/2026-10-27-dashboard-material/dashboard.png` | Replacing the accepted identity with a generic dashboard |
| Source reuse | Existing normalized contracts/actions, with bounded Home-specific readers where old ones overfetch; source inventory below | Duplicate grants, contradictory states or wasted integration |
| Calendar | Primary Google Calendar, all upcoming event types visible; owner-only agenda action reads original attendee metadata and exact matcher, not names inferred from cached titles | Missing preparation or assigning work to the wrong person |
| Task clock | Scheduled end creates follow-up cue, not attendance proof; no historical flood | False attendance claim and task overload |
| Completion | Explicit teacher handling; link opening is not completion | Quiet loss of unfinished work |
| Email | Students and tutoring enquiries only; exact known email and explicit enquiry label/classification | Hidden student mail or personal mail leaking into the work list |
| Presence | Until live connection proof: “Active in the last 5 minutes”; true “Online now” requires verified presence behavior | Last visit presented as current online status |
| Recap | Track preparation and confirmed posting separately; no automatic drafting/sending/posting in this release | A checkbox misrepresented as delivery |
| Storage | Existing local originals plus verified private Drive initial copy; no continuous sync is active | Stale context presented as current |

Routine reversible composition choices are resolved here. Automatic AI draft generation and two-way Drive synchronization remain separate decisions, not hidden prerequisites. An explicit Gmail enquiry label is the conservative initial classification; unrelated “likely human” mail is excluded. Verify actual account/label availability read-only before integration and show setup-required if absent.

### Strongest visual direction: a compact teaching desk

Use the existing editorial-greeting direction, reduced to the needs of a daily work screen. Taste library comparison on 2026-10-28 offered editorial-greeting and achromatic-ledger; choose editorial-greeting for the personal teaching desk, retain palette/type, and take the ledger's aligned, quiet rows rather than a money-led composition. Saved sheet: app `.taste-skill/review-20261028/direction.json`, seed 2078823331. The library's example metric tiles and replacement shell are not mandatory: they conflict with the confirmed work-led brief and existing navigation. Keep the 12-column alignment and tonal hierarchy, not four invented metrics.

At 1440 x 900 with the actual signed-in classroom shell, use available content width, 20-24px gutters and 16-20px panel spacing. Header is one compact greeting/date/status line, 24-28px greeting, with a real Assign work button and Open email shortcut. Remove the large dark assignment promotion; reserve charcoal for one action, current selection and small today mark. No search box with a vague global scope; student search belongs with students.

Desktop layout target, based on available content width rather than window width:

1. Compact header, then a quiet attention summary row with payment/access/email counts and explicit category names. Counts belong to their panels; no repeated vanity KPI row. A summary count is also a jump link to its region, not another data total.
2. Main band: left 7 columns = After-session work followed by My list; right 5 columns = Next up agenda followed by Needs attention. Two compact session summaries plus two manual tasks and the first agenda/decision rows should fit on the first desktop screen. Lower rows continue naturally; no stretched equal-height blank cards.
3. Lower band: recent payment activity and separate email/platform-message groups, each capped at 2-3 rows with View all and total where reliable. A small recent-student/presence strip sits alongside or below these; no large roster directory on Home. Student search remains an accessible compact control opening full student details.
4. The week is optional secondary context, never a second contradictory schedule. If retained, derive from the same primary-calendar agenda data and use dates that match. Remove it if it only repeats the next few sessions while pushing actual work below the fold.

Keep every primary category discoverable in the first desktop screen through a header/first row or its honest attention summary. Do not claim all full lists can fit there. Test with 2, 12 and 0 sessions, long names, errors and absent providers before accepting the composition.

Session rows collapsed: student, absolute session date/time, unfinished steps in plain text, transcript state, and one Open follow-up disclosure/action. The selected row expands inline to notes, transcript, folder, checklist, explicit Mark handled and correction controls. Keep only one expanded row at once; collapse must not discard input. Keyboard disclosure uses aria-expanded and returns focus. Manual tasks show title, optional student/blocker, and a comfortable check target; Add task is visible beside My list. Preparation/posted/assigned labels reflect distinct persisted facts, never inferred from navigation.

On 768/980 and docked layouts, stack when either working column would be under 340px. At 390/320: compact title/actions, small urgent decision summary, session work, My list, agenda, then other areas. Use collapsed rows and progressive disclosure so the first session action is visible promptly. Keep actionable business items reachable before a long queue through summary jump links. No squeezed two-column forms or page-wide horizontal overflow. Touch targets at least 44px; body/action text 14-16px; metadata at least 12px. Preserve saved input and focus across refresh/layout changes.

Material: warm ground, lighter work plane, subtle row selection and local raised controls. One consistent contact shadow under a raised plane, crisp edges, no diffuse haze. Shared radii distinguish section, row and control. Preserve selected reference, not cool-gray/white replacement. Status hue is small and paired with words; never use a green dot alone as online proof. Fraunces only greeting; Outfit working text; tabular money/durations. No decorative images, charts, glows or atmospheric animation. This app's substance is its students, session work and trustworthy events.

Motion: purposeful 120-180ms press/disclosure feedback, at most one animated region; no page entrance, auto-scroll, repeated reveal or flash on refresh. Respect reduced motion with immediate state changes, retain feedback/focus, and no layout animation that moves the control being clicked. GSAP is optional implementation tooling, not a reason to animate every panel.

### Data, actions and reuse contract

| Home area | Existing source / implementation path | Required behavior and missing work |
|---|---|---|
| After-session | `src/components/classroom/home/teacher/PostSessionWork.tsx`, `usePostSessionHome.ts`, dedicated migration/worker; detailed `2026-10-27-post-session-home.plan.md` | Keep durable owner-private model, final matching/error/admin fixes, manual history and no-op source revision safety. Adapt compact UI; don't rebuild queue storage |
| My list | Not present; `useTeacherTodoQueue.ts` is derived, not manual storage | Add dedicated owner/admin RLS manual tasks with id, revision, title, optional student, blocker, created/handled timestamps and history. Owner-only mutation RPC; optimistic display only if rollback/error is explicit. Full tasks view/search/filter can be one Home sheet, not a new page unless needed |
| Payments | `src/components/teacher/PaymentsPanel.tsx`, mounted summary in `src/pages/teacher/shell/DeskTodaySurface.tsx` | Reuse normalized ledger/action contracts, not its unbounded all-history loader on Home. Bounded RPC below. Show recent paid/credited activity separately from unresolved/actionable states. Ignore obsolete manual-only comment; existing eligible automatic credit grant remains authoritative. Top-up shortcut requires additive-balance repair/proof below |
| Access | `src/components/teacher/SignupQueue.tsx`, existing dossier access controls | Compact unassigned-tier queue + named-student access sheet. Tier1/full and Tier3/basic reuse verified preset definitions through new CAS writer; Tier2 is Customize only, preserving draft flags until explicit Save. Show resulting tier/features before save, confirm returned account/state. Scope reads by actor; original unscoped signup query must not cross-account cache |
| Email | `useGmailTodoSource.ts` is broad human-mail heuristic, insufficient | Adapter must use unread exact roster-email mail plus explicitly labelled tutoring enquiries, paginated without a silent total cap. Separate email from platform messages. Open email available even if signal provider fails; use existing safe open-inbox route. No send or mark-read on Home list view |
| Platform messages | Current `useInbox` summary/read protections | Specific conversation open may mark its messages read using existing rules; viewing Home doesn't. Preserve partial snippet failure behavior and full unread count |
| Agenda | Existing Google token/Calendar helper and exact post-session matcher; cached `scheduleEvents.ts` lacks attendee metadata and current Home has only four student_sessions rows | Add owner-only agenda read action on the pinned handler, described below. Original primary Calendar metadata supplies identity; show all event types in a bounded 7-day window, 3 initial rows with View calendar. Never infer prep links from cached title/description. Independent freshness/error state |
| Recent/presence | `last_seen_at`, `usePresenceHeartbeat.ts`, `presence.ts` | Last few visits stay small. A 3-minute heartbeat / 5-minute threshold means recent activity, not reliable live connection. To label Online now, add actor-safe presence with disconnect expiry, reconnection, multitab dedup and tests; otherwise retain honest recent-active fallback |

All adapters are owner-keyed and role-gated; wait for resolved admin role, clear on sign-out/actor change and never reuse another admin's cached private data. Failures are per-area; no one provider failure blanks Home. Refresh existing data in place, with last good timestamp. Count only known data: unknown total is not zero. Narrow resource limits show a window and View all; an uncapped total requires actual paginated aggregation.

Bounded payloads are a backend contract, not just a visual cap. Replace the current unbounded `teacher_post_session_home()` response in the later full-Home build: exact owner-scoped open_count/handled_count, at most 20 open rows ordered oldest ends_at then id, and no history rows until requested. A separate keyset-paginated history RPC orders handled_at descending then id, with page size at most 20 and a cursor; active tasks beyond the first page also have a cursor. Home initially renders two session summaries; View all loads additional pages in the work sheet. Preserve id/revision mutation semantics. The current post-session plan's all-rows payload is superseded only by this explicit future full-Home contract, not represented as already fixed. Server counts and paginated records share the same owner/filter. Updates refetch counts/window; no UI assumption that loaded rows equal total. Tests use >100 handled/open records, tie timestamps, page boundaries and actor switches.

Access reuse means extracting safe contracts, not mounting SignupQueue or its client writer unchanged. Replace its one-click X-to-Tier3 path on Home with an explicit “Basic (Tier 3)” action that opens the named account and resulting enabled features for confirmation. Use query key ['teacher-home-signups', adminUserId], enabled only after resolved admin authorization; cancel/remove old-actor cache and reject stale callbacks. Existing setStudentTier returns void, is a blind overwrite and may fall back to direct profiles writes; Home must NOT call it or the existing set_tier action for its saves. Add Home-only authenticated admin-manage-users action set_home_tier backed by one transactional compare-and-set RPC: requested class_id, expected prior tier (null for undecided signup), expected preview flag map/revision, requested Tier1 or Tier3. Server verifies current actor admin authorization and target non-admin/non-archived eligibility, locks target row, checks expected state, applies shared verified preset rules, and returns written class_id/tier/all flags atomically. Any concurrent decision, eligibility change, mismatch or no row rejects with conflict/refresh, never overwrites a newly decided account. Do not allow eligibility checks only in the client filter. Existing backend's old/unknown-action response fails visibly; NO direct-profile fallback or speculative second write on Home. Refetch through authorized reader to confirm if needed. No mutation on list open, row select, close or cancel. Existing Today/dossier paths remain unchanged unless separately scoped.

Customize source reference is setStudentAccess(person,field,value), which also returns void and writes directly; do not use it directly on Home. Add authenticated admin-manage-users set_custom_access for one atomic Tier2/allowed-feature-map compare-and-set update with the same target eligibility, expected preview and row-lock checks as set_home_tier, sharing existing feature normalization and derived review rules. Reject unknown flags and stale/ineligible targets; return full verified class_id/tier/flags. Tier2 on Home is ONLY this Customize path: initialize draft from actual current switches, preserve unedited values, show the complete result, then apply once on explicit Save. Never call the existing set_tier(tier_2), whose implementation resets flags despite its preservation comment. That historical preservation claim is superseded for this current plan. No mixed per-toggle auto-save; cancel discards draft. Preset/custom success verify the same named target and returned fields. Existing toggle/apply_template partial responses are insufficient. Tests cover concurrently decided signup, concurrently modified preview, admin/archived target, Tier2 unedited flags and derived outcomes, mismatched/no-row responses, old endpoint, cancel, partial error and no client fallback.

Exact source contract: `PaymentsPanel.tsx` exports `StripePayment`, `loadRecordedPayments()` and `needsAttention(p)`. The full-history reader pages stripe_payments 500 at a time ordered by paid_at/id descending; leave it for the history view, not Home. grant_state is none/awaiting/granted/dismissed; match_state is matched/unmatched/linked/ignored. Existing attention is awaiting OR (unmatched AND succeeded AND source webhook). Retain the important webhook/backfill distinction, but do not blindly preserve its dismissed-unmatched edge case: explicit ignored/dismissed is excluded from Home action counts; granted always wins as credited activity, never another grant. Failed/refunded/disputed rows can show as activity/review, never grantable. An awaiting row becomes grantable only after authoritative eligible package/student/offer, succeeded and unrefunded checks. A matched succeeded none-state row is ordinary activity unless a separate authoritative exception exists. Display money per currency, not a sum across currencies. `SignupQueue.tsx` exports `signupQueueRows(users)`; reuse its non-admin, non-archived, no-tier selection. Reader `listManagedUsers()` in `src/lib/accessTierClient.ts` invokes `admin-manage-users` and merges access-tier fallback from profiles. Tier/feature client writers return void and have direct-write paths; Home uses the explicitly extracted backend-only verified-row variants above. Stable student identity is class_id, not user_id.

Before constructing Home, derive private recorded-input fixtures through these real readers for: (1) succeeded matched/linked package with grant_state granted and actual credited amount, (2) grant_state awaiting package, (3) succeeded unmatched webhook payment, (4) historical unmatched source=backfill payment that is not actionable, and (5) ignored/dismissed and failed/refunded/disputed payments, including contradictory combinations. Capture sanitized source rows or produce them through the same real normalization/classification output; no provider writes to manufacture fixtures. Compare before/after classifications for identical rows; all differences must equal the explicit Home rule changes above, not an unexplained drift. If a live class has no row, use generated reader output and name the synthetic case separately, not as observed production evidence. Unknown/new state requires review, not an automatic grant. Preserve existing mutation idempotency and authoritative server result; UI disables duplicate submit but does not substitute that for server safety.

Bounded payment RPC: owner-admin-only `teacher_home_payments` returns at most 3 recent rows from the last 90 days, 3 newest attention rows with a keyset cursor for more, and exact attention_count computed server-side under the Home predicate above. Recent window is labelled; older unresolved attention remains eligible regardless of age. Select only id, paid_at, status, product, currency, amount_cents, amount_refunded_cents, student_id, payer display fallback, match_state, grant_state, granted_credits and source needed for this view; no whole-ledger SELECT*. Detail opens the existing authorized payment history/action. Query/mutation cache keys include admin actor; realtime events invalidate the bounded reader, not load all history. Tests seed thousands of rows and prove bounds, stable cursor/ties, exact count, per-currency display and last-window boundaries. No all-history payment read on Home mount or refresh.

Verified agenda action: add authenticated owner-only `agenda` read action to the existing pinned handler, reusing its Google token helper, primary-calendar identity check, exact roster/verified-alias matcher and strict Calendar link handling. Query original primary Calendar with singleEvents=true, orderBy=startTime, a frozen [now,now+7 calendar days] window, maxResults=20 and pageToken paging. No task/attempt/error status writes from this read action; only sync updates worker health. Return at most 20 events per request, opaque continuation bound to owner/calendar/frozen window, server fetched_at and calendar timezone; Home shows 3 rows and View calendar/load more. No global event total unless fetched/countable. Return instance id, title, starts/ends, status, Calendar link and nullable verified student id/name; raw guest emails and descriptions remain server-side. Multiple/archived/unmatched identities return no prep link, no guessed student. No titles used to establish identity. This action is an additional read path, not a claim that schedule_events already stores attendees. Keep cached agenda only as explicitly dated fallback without inferred student context. Tests cover no-attendee, two matches, archived/declined, recurring instances, pagination, primary-owner mismatch and failed provider with last-good data.

Agenda handler isolation: branch after authenticating the pinned admin but BEFORE recordSyncAttempt, lease or sync orchestration. Use its own try/catch and returned area error; an agenda identity/token/provider failure must not invoke worker finish/attempt RPCs. Tests spy on all settings writes and compare health fields before/after agenda success and failure. Home agenda refresh runs on mount and every 120 seconds only while visible, with focus refresh deduplicated inside that interval; explicit Retry is throttled at 15 seconds. Keep last-good data and separate area freshness, never alter sync success. Cache the selected-field roster/alias lookup server-side by owner/calendar for at most 60 seconds, invalidate after identity/access/folder-map changes, never share across owners. Do not reuse the worker's full SELECT* scan on every agenda request. Batch-check matched candidate profiles' current archived/non-admin eligibility before returning prep links; owner role authorization is fresh, never TTL-cached. Bound provider/cache cold-load work with errors/timeouts and truthful stale UI rather than a false empty agenda.

Verified organizer edge case: current model.ts excludes every attendee with organizer=true. For the full Home build, replace that blanket exclusion in the shared matching contract: exclude configured teacher/self/resource/declined entries, but a non-teacher organizer with an exact eligible student email remains a candidate. Organizer status alone must not erase a legitimate student-organized session or its prep link. This explicitly supersedes the earlier technical plan's blanket organizer exclusion. Apply the same normalized candidate filter to agenda and post-session matching; add same-input fixtures proving teacher-organized, student-organized, declined-organizer, resource-calendar and multi-match outcomes. No name guessing and no broader automatic identity permission.

All event display and calendar-day windows use the returned primary-calendar timezone (normally America/Toronto), never the current machine timezone. Store instants in UTC. Test daylight-saving transitions, midnight boundaries and two otherwise identical local times. Keep absolute date/time labels on task rows; a relative label can supplement, not replace them.

### Carry-forward scope for earlier approved needs

| Earlier need | Full Home release status | Acceptance/prerequisite |
|---|---|---|
| Private booking-pass link, status and revoke | In, behind a compact More actions sheet, not another header promotion | Before exposing top-up, inspect/fix booking-pass-admin replace-balance behavior. Add credits atomically and idempotently: 2 existing + 5 purchased/granted = 7, retry remains 7, concurrent increments preserved. Named student/session count preview, status/readback and explicit revoke confirmation. No payment request or student redemption step. If prerequisite fails, this blocks that shortcut's delivery rather than showing a broken action |
| Brief recent test results | In, small “Recent results” disclosure with at most 3 verified results | Reuse recorded test-result source identified in recon; score/test/date/type kept together, student detail for more. No homework-risk/missed-work alert or invented mastery. Missing source remains setup/unknown, not fabricated results |
| Per-student task progress/blockers and full Tasks view | In, “All tasks” Home sheet with student/type filters and keyset paging | Count open/handled/blocked task work per student server-side across task sources; label these teacher-task counts, not student performance. Manual blocker supported on session and manual task rows, preserved by worker refresh. Explicit source/type makes session/manual/consultation work distinct. Sheet supports reload, handling/reopen and matching student context without replacing assignments |
| Automated AI drafting / two-way Drive sync / arbitrary Drive transcript discovery | Deferred, outside this release | No hidden promise; attachment matching/manual fallback and private initial folder copy are explicit. Separate scope needed |

This scope table carries the earlier shortcut/results/task requirements forward. It does not authorize their implementation or live mutations before the build/release gates. Full Home is not called delivered while an in-scope item is missing.

Concrete result source: `src/lib/sectionHistory.ts` exports teacher-safe `fetchSectionHistoryByClass(classId)` reading section_history by class_id and completed_at descending. Add a bounded multi-student Home reader for the last 3 recorded section results with id, student identity, pt/section/mode, initialScore/initialTotal, optional separately labelled blind-review score and completedAt; query only eligible managed students, avoid an N+1 call for the whole roster, and open `/teacher/students/:studentId/progress`. Do not reuse `listSavedAccountPracticeTestRuns(userId)` across students: it is account-asserted, not a teacher reader. Label section results as sections, never whole-test scores; no extra mastery inference.

Concrete booking prerequisite: `StudentBookingPanel.setRemaining()` currently sends booking-pass-admin action:update with total_credits = used_credits + DEFAULT_CREDITS; the handler invokes manage_booking_pass set_terms_and_remaining. That sets remaining, not an additive top-up. Full Home shortcut must use a dedicated server-authorized atomic/idempotent add operation; don't reinterpret the existing edit action as add, and retain explicit set-remaining elsewhere with its existing semantics. Regression targets include StudentBookingPanel.test.tsx, bookingRemediationContract.test.ts and bookingPhase1Contract.test.ts, plus same-input before/after SET behavior and new ADD retry/concurrency proof. Status/revoke remain existing-contract actions with explicit selected-student context and readback.

Top-up retry identity: opening a confirmed named-student/pass/amount preview generates a cryptographic UUID operation key once. Persist the pending key, actor id, pass/student id and amount in actor-scoped session storage so reload/network retry reuses it; clear on sign-out without transferring it to another account. Editing target or amount cannot reuse that key. Keep an unknown-outcome operation pending until exact server receipt/readback; do not silently create another key after a timeout. A dedicated append-only add ledger is unique(owner_id,pass_id,operation_key), stores request payload hash/delta and original receipt. In one server transaction authenticate/validate target, lock current pass, insert unique receipt and increment credits atomically; replay with same payload returns original receipt without another increment, mismatched payload fails. A new intentional add gets a new key even if amount is identical. Do not revoke/replace the existing active pass via grant_booking_access to implement a top-up. Return/read back current balance separately from the original operation receipt so later distinct adds are visible. Tests: 2+5=7, same-key retry/reload remains7, two distinct +5 operations yield12, concurrent distinct increments both persist, same-key changed amount/target rejects, unauthorized actor cannot replay or read receipt.

Presence audit before build: find every consumer of ONLINE_WINDOW_MS and online helpers, including imported roster labels. Home must render “Active in the last 5 minutes” for heartbeat-only evidence even when an imported helper is named online. Keep any unrelated wording change separately scoped; do not rewrite student-facing surfaces under this Home plan. Tests assert the Home label and the absence of a false Online now claim.

Consultations: the older full brief includes a single durable follow-up after a positively identified ended consultation. This remains distinct from student after-session work and is not implemented by the current student worker. Initial positive classifier is an explicit owner-applied Consultation label in an owner-private teacher_calendar_labels table keyed owner/calendar/instance event id, with labelled_at and revision/history; NOT a title/description substring or an unverified Cal.com-looking link. Owner can label from agenda; no automatic retrospective task: cue requires end >= max(activation_cutoff,labelled_at), ended and eligible guest. General/ambiguous events stay visible without tasks. Verified provider booking metadata could automate classification in a separate evidenced extension, not silently assumed here. Add separate task source/type with unique owner/calendar/recurring instance event id/type, never series base id or mutable end time. A reschedule before creation delays the cue; a moved existing task retains id/manual work and shows changed time/source state. Cancelled, all-day or declined-only guest events cannot create. Cancellation after creation preserves task/history with cancelled label; no automatic handle/delete. No guessed student or automatic email. Reuse existing derived queue as evidence only, not durable completion. DB/model tests cover lookalike “Consultation” titles without label (no task), solo planning, two recurring instances, label/cutoff timing, reschedules, repeated sync, cancellation and declined guests.

Known presence wording inconsistency outside Home: StudentDossier.tsx, TeacherStudentDetail.tsx, StudentOverview.tsx and DeskPeopleSurface.tsx currently use isUserOnline with heartbeat-only evidence, and ThreadList uses isParticipantOnline. Do not import their false-live label into Home. Record a separate wording follow-up; Home can ship honest “Active in the last 5 minutes” without claiming those other surfaces were repaired.

Transcript linking: the full Home release uses the existing local unique native Docs Calendar attachment matching and explicit manual link fallback. A task appears even when neither is available; the UI says Waiting for transcript or Needs review. Ingestion-ledger matching described in the earlier technical plan is deferred, not an implemented promise or a prerequisite hidden in this plan. Local Drive copy is not a watched transcript inbox. Never guess by filename/name similarity; manual provenance wins. Unmatched native Docs and conflicting automatic links show needs review. This bounded support is stated in the release notes and preview so the design cannot imply automatic discovery of arbitrary Drive uploads.

Recap delivery state: preserve private draft preparation and confirmed posting as separate fields if both are shown. A workspace agent may update them only through the same authenticated revisioned task API with explicit success evidence; otherwise Joshua updates them manually. Do not infer completion from transcript arrival, generated files, link opening or assignment-list access. Workspace transcript/recap skills remain available.

### Build sequence after approval

1. Read scoped app instructions, teacher glossary/context and existing source contracts. Reconcile older exclusive Reply/Review/Assign and instrument-panel rules with this reopened brief explicitly; do not silently enforce conflicting scopes. Capture HEAD and preserve uncommitted/unrelated changes. Extract actor-scoped adapters before new UI.
2. Add durable manual/consultation task model, RLS, history and revisioned mutations. Retain tested post-session schema/API. Verify permissions and identity on actual generated/source output with disposable PostgreSQL and provider read-only fixtures; don't rely only on handwritten happy paths.
3. Implement compact Home composition with real reusable payment/access actions, separately scoped email and primary agenda. Leave missing-provider setup visible. Keep business mutations explicit, backend-authoritative and duplicate-safe.
4. Build preview from real view components plus labelled derived fixtures, and a signed-in real-shell staging run when available. Use the same source objects to compare prior/current task and payment classifications; expected differences documented, existing grants unchanged.
5. Complete proof/review/render loop; obtain separate release/deployment approval only after concrete diff and known limits are ready. Run one student/session pilot before broad activation. No live mutation is implied by plan approval.

### Verification and stopping rules

Exact app commands already used by this repo: `npx vitest run src/components/classroom/home src/hooks/useInbox.read.test.tsx src/hooks/useInbox.summary.test.tsx src/hooks/useUserPermissions.resolved.test.tsx src/hooks/useUnreadCounters.test.tsx src/hooks/useSharedRailQueries.test.tsx`; `node --max-old-space-size=4096 node_modules/typescript/bin/tsc --noEmit -p tsconfig.app.json`; `npm run build`; scoped `git diff --check`. New adapter/manual-task tests must cover actor switches, stale/failed providers, exact email scope, pagination, completed credit vs exception, target-account access save, consultation dedup and manual task reload/handled/reopen.

Backend: `deno check supabase/functions/teacher-post-session-sync/index.ts`; `deno test --allow-net supabase/functions/teacher-post-session-sync/model_test.ts`; `node docs/verification/post-session-db-check.mjs C:/Users/Joshu/.codex/verification/tools/pglite/node_modules/@electric-sql/pglite/dist/index.js`; vault `python -m unittest discover -s setup/student-context-drive -p test_*.py`. Extend disposable DB harness for new tables/RPCs. Expect no student/other-admin access, stale-write rejection, source refresh preserving teacher work and no duplicate task/grant. Test old/new on the same recorded source inputs; strip secrets and use private fixtures ignored by Git. Local checks do not certify deployed RLS or provider delivery.

Visual: build production preview, run Taste `inspect.mjs --app` at 1440/768/390, add 320/980 and actual docked shell. Open all fold/full-page screenshots. Compare selected material reference and old/new matched data. Baseline mobile Mark handled was roughly y735/844 (87%); the new collapsed-row Open follow-up must start within 60%, with Mark handled deliberately inside expanded content. This is an intentional action-model change, not a claim the baseline already passes. Critique top three visible defects and iterate up to three render rounds; no automatic “perfect” score. Zero FAIL, each WARN defended specifically. Include full, empty, >10 tasks, long student/task names, loading, offline, stale, partial-error, save-error, missing-link, conflicting-doc, expanded history/access sheet and reduced motion. No clipping, readable contrast, visible keyboard focus, logical tab order and saved input preservation. Representative real press/disclosure timing must be watched; settled screenshots are not motion proof.

Independent review: fresh Claude source inspection after an authorized build, exact pre-build base and all task paths. Preserve complete response, actual coverage and exclusions. Final code changes require fresh other-provider inspection if budget remains; report unreviewed fixes if exhausted. Approval is never a whole-product guarantee.

Live acceptance after separate release permission: correct owner/primary Calendar, exact folder import/readback, student/other-admin denial, real ended session produces exactly one task, laptop-off cron run, manual and workspace completion readback, payment/event duplication safeguards, explicit access mutation target, exact email classification and presence disconnect test if enabled. No “automatic and live” claim until those pass.

Known current limits: only local post-session slice exists; Drive copy complete but initial-only; 17 exact folder-account mappings with six unresolved; no live backend import/worker/cron/deploy; broad Home payment/access/email/manual-task areas absent; the preview lacks the full authenticated navigation shell. Earlier final corrections passed local tests but have not received clean independent final implementation approval. This plan review must not hide those limits.

Design approval means the direction is concrete enough to build and test. It does not mean a screenshot, sampled motion or one reviewer proved every state flawless.

## Reopened teacher Home brief, 2026-10-27

Joshua clarified that the local role-Home preview is too focused on student messages. Teacher Home must support his actual teaching and business work. This current request reopens the Calendar, Stripe, email and private-task scope excluded by the narrower 2026-10-22 build order. The student Home remains a separate surface. No revised app implementation is approved by this discovery note alone.

Confirmed needs from the current request and earlier accepted decisions:

- Automatic payment updates, including successful credit grants and exceptions requiring a decision. The September manual-grant-only description below is historical: current source supports automatic credits for eligible matched package payments, with unmatched payments requiring review. Fresh live operation is not verified in this interview.
- Access decisions and direct student access controls on Home.
- Recent student access and meaningful progress, with a route to the student's details. A visit is not evidence of learning or assignment completion.
- Student email signals and a quick route to email, alongside platform messages.
- A durable after-session work list linked to each student and session: obtain the Gemini transcript, prepare the recap/notes, review the draft, post approved material, and assign the next work. This explicitly supersedes the old exclusion of transcripts from the dashboard's scope.
- Preserve private My list for manual tasks, student-linked tasks, handled history/reopen, and manually recorded blockers. Do not replace the task list with messages or a roster.
- Keep upcoming primary Google Calendar events visible and distinct from unfinished follow-up work. Existing decisions excluded a historical session-task flood at launch.
- Keep Joshua's existing workspace-based transcript and post-session workflow available. Home should expose and track the work; it must not silently require him to use the app ingest page instead.

Current source checks: `src/components/teacher/PaymentsPanel.tsx` has payment updates; `booking-commerce-webhook` calls the automatic grant flow. `CONTEXT-MAP.md` routes teacher language to `src/pages/teacher/CONTEXT.md`; its Session Transcript, Recap, Task and approval definitions already describe the transcript-to-draft workflow. These are source facts, not new live acceptance evidence.

Reuse before building: the current `src/pages/teacher/shell/DeskTodaySurface.tsx` already assembles a task queue, payment summary, task rail and signup queue. `useTeacherTodoQueue.ts` and `useDeskTaskQueue.ts` already join email, Calendar, unread platform messages and other teacher inputs. The next Home proposal must compare these existing controls and their persistence with the narrower role-Home preview before introducing parallel queues or integrations.

Original interview questions (answers and remaining gaps below):

1. On a confidently matched Gemini transcript's arrival, automatically prepare the recap draft, or add a task that Joshua starts? Recommendation: automatically prepare a draft; posting and sending still require Joshua's approval. The location/execution of preparation must fit the existing workspace workflow.
2. Flag only student emails and tutoring enquiries on Home, or all unread email? Recommendation: student emails and tutoring enquiries, plus an Open email shortcut.

### Interview answers, 2026-10-27

- After every student session, add a Home task for post-session work. Do not wait for the transcript to arrive. Ideally pair the Gemini transcript to the correct student/session and expose it from that task. Missing or ambiguous transcripts do not remove the task.
- Joshua can point to Google Drive student folders for context. Inspect existing saved mappings first; otherwise obtain the intended folder link. Automatic drafting timing is not yet settled by this answer.
- Email scope confirmed: students and tutoring enquiries.
- Recent activity should be a small area showing only the last few entries, with details opened on demand. Joshua also requests a small Online now area showing students currently online while he uses Home. Keep the teacher task list and after-session work primary. Recent visits and current online presence must remain distinct; the existing last-seen heartbeat alone is not verified live connection status.
- Current implementation gap: the Calendar queue excludes ended events, so it cannot supply the required durable after-session queue. No general teacher-created My list was found. Do not silently reuse student-owned task storage. Existing transcript ingestion and recap review are building blocks, not proof of a complete automatic Home workflow.

Next discovery must resolve reliable live student presence and the available evidence of recent student access; the session-to-transcript matching path; and the durable connection between Home tasks and workspace completion. No implied approval to send, post, grant access or deploy follows from this note.

### Student storage discovery, 2026-10-27

Verified local root: `C:/Users/Joshu/dev/ai-os/students`. There are 23 student-named folders outside system/former-student areas, containing 553 files and 16,342,239 bytes. This is a folder count, not verified active enrolment. Existing records include profiles, teaching notes, open loops, assignment logs, transcript exports and session packages. The owning structure is `students/README.md`.

Read-only Google Drive access was verified for Joshua's business account. No canonical live Home folder mapping was established. Existing workspace archive sync does not establish an active per-student context connection.

Recommended connection: preserve local primary records; maintain a private Drive copy of relevant student context and transcript documents; store durable after-session tasks and their status in LSAT U. Match documents by verified student identity and session date, retaining stable document IDs and refresh timestamps. Keep ambiguous matches for review. Start with one student/session before expanding. This is a recommendation, not an implemented sync: no records moved, deleted or uploaded and no automatic Home connection deployed in this discovery.

## Summary / key decisions (2026-09-27 historical baseline)
- **Teacher Home:** Distinct from the student Home, led by clear action queues and a useful upcoming agenda. Joshua wants a visually easy, utility-first command center using the strongest ideas from all six reference images, without copying one.
- **Needs your attention:** Unread student messages, paid packages awaiting teacher enrollment/pass grant, new accounts awaiting access-tier choice, and post-event teaching tasks. No tutoring-request queue, student homework review queue, missed-homework queue, or routine test-result task.
- **Calendar:** Use only Joshua's primary Google Calendar; show every upcoming event and open its Google Calendar event. A clearly identified tutoring session produces “Assign work or add notes” after it ends; a consultation produces one follow-up task. Ambiguous events remain visible and can be manually labelled. No historical task flood at launch. Importing transcripts is outside this dashboard scope; Friday 2026-09-25 events were verified to have attached “Notes by Gemini” Docs in Google Calendar.
- **Tasks:** Session/consultation tasks remain active until Joshua marks them handled. Handled tasks move to history and can be reopened. Separate Home area “My list” supports private manual tasks and check-off. A full Tasks page filters by student/type and shows per-student task progress counts and manually set blockers.
- **Messages:** Opening the specific student message clears its unread alert; opening the notification list alone does not.
- **Payments:** Show new Stripe activity and searchable roughly three-month history on teacher Home. A recognized paid package creates an “Enroll and grant passes” task; unmatched payer needs review. Only session/package payments can drive access actions, and a package pass grant remains Joshua's one-click decision.
- **Student access:** A new non-admin account without a tier needs a grant decision. Quick controls are Tier 1 full, Tier 3 basic, and Customize for Tier 2. Individual feature switches remain available.
- **Students and analytics:** Show only brief recent test results on Home. Opening any student should show detailed performance and all work, including the individual questions attempted in homework. Upcoming session rows should link to useful student preparation context.
- **Quick booking-pass link:** This is not a payment request. Joshua selects a named student and session count; creating the private `/book/{slug}` link makes the sessions usable immediately without login. Adding sessions preserves the current balance (2 + 5 = 7). The link has status and revoke controls. Current code's pass replacement must be fixed before surfacing this top-up shortcut.
- **Excluded:** The “course through the district checklist” phrase was accidental dictation. There is no student redemption step and no transcript import requirement for this dashboard.
- **Observed state:** Live `/teacher/today` already had a searchable 90-day Payments panel with 37 charges on 2026-09-27; `/classroom` still showed the student-style Home to the signed-in teacher. This does not prove every Stripe event reconciles or the new dashboard behavior exists.
- **Visual interpretation for proposal:** Image 2 provides a clear hierarchy, image 3 a compact schedule, and image 6 warm task cards. Charts should have real teaching meaning and not become decoration. Joshua has not approved a specific mockup yet.

## Code fact check (2026-09-27, read-only)
- `/teacher/today` already renders signup, payment, calendar, and task areas. Its calendar query is roughly a 24-hour window and includes general Google events, so it does not yet provide a reliable upcoming student-session preview (`src/pages/teacher/shell/DeskTodaySurface.tsx`, `src/pages/teacher/desk/scheduleEvents.ts`).
- The active student dossier has overview, work, notes, messages, and schedule routes, but no dedicated analytics route. Its work view does not expose individual homework questions and answers even though assignment records can include question ids (`src/App.tsx`, `src/pages/teacher/students/DossierWork.tsx`, `src/components/hub/HubAssignments.tsx`).
- Session transcripts are ingested through Gemini Notes email/Doc workflows with manual scan/match steps. The dossier Notes area lists stored sessions and transcripts. Calendar metadata supports matching; there is no code path found that automatically imports a transcript from an event note or creates a post-session assignment task (`src/pages/teacher/TeacherSessionIngest.tsx`, `supabase/functions/scan-session-notes/index.ts`, `src/pages/teacher/students/DossierNotes.tsx`).
- These are code findings from `projects/lsatu-stripe`, not confirmation of live behavior. Claude's uncommitted `supabase/functions/mcp/index.ts` was not edited.
- Tier access code: null `access_tier` on a non-admin, non-archived account defines the current signup queue. Tier 1 enables all 12 feature switches; Tier 3 enables Classroom, Messages, and Schedule (assigned work remains visible); Tier 2 preserves customized switches. The active dossier has per-feature toggles. Payment package pass grants use a separate `grant_state='awaiting'` and must remain a distinct queue (`src/lib/adminUsers.ts`, `src/components/teacher/SignupQueue.tsx`, `src/pages/teacher/students/DossierOverview.tsx`, `src/components/teacher/PaymentsPanel.tsx`). Code finding only.

## Live Calendar fact check (2026-09-27, read-only)
- Google Calendar CLI on Joshua's primary calendar returned three confirmed tutoring sessions on Friday 2026-09-25. All three have one attached Google Doc titled “Notes by Gemini.” This confirms Joshua's observation that Friday event records have a notes attachment. The event descriptions themselves are booking metadata, not the transcript text.
- A primary-calendar query for 2026-09-27 through 2026-10-05 returned the first upcoming tutoring session on 2026-09-28 at 15:20 Eastern and additional sessions later that week. The 2026-10-02 primary-calendar query returned no events at inspection time. The CLI also lists several secondary calendars; Joshua later chose the primary calendar only (Round 4).
- These are live Calendar observations, not evidence that LSAT U currently displays or syncs all those events.
- A search of the primary calendar's 2026-09-01 to 2026-09-27 events returned 12 confirmed events with “Consultation” in the title and Cal.com details in the description. This gives a reliable-looking current pattern for consultation classification, but other/manual event naming has not been exhaustively checked. Tutoring examples on 2026-09-25 used “<student> session” titles and “Booked via LSAT U” descriptions. All events should remain visible even if their task type cannot be classified.

## Calendar implementation finding (2026-09-27, code only)
- `gcal-sync-pull` syncs one configured calendar (default `primary`) into `schedule_events`, from 14 days behind through 90 days ahead on a full pull, then incrementally. It stores title, description, time, status, Calendar link, and related fields, but drops attachments. Friday's Gemini Notes attachments therefore exist in Google Calendar but are not mirrored into LSAT U (`supabase/functions/gcal-sync-pull/index.ts`, `supabase/functions/_shared/googleCalendar.ts`).
- Teacher Today triggers a Calendar pull on mount and every 120 seconds while visible; its event list refetches every 60 seconds. A production cron is mentioned in migration comments, but its actual active status was not verified. The Today query is limited to roughly 24 hours and the surface narrows further to the current day, which explains why the 2026-09-28 upcoming session is not shown on Sunday 2026-09-27 (`src/pages/teacher/desk/scheduleEvents.ts`, `src/pages/teacher/shell/DeskTodaySurface.tsx`).
- Best proposed path, subject to Joshua's remaining decisions: show a longer upcoming agenda from the already synced schedule; use each event's stored Google Calendar link to open the event and its attached note there; create a per-session, manually handled assignment-or-notes task after the event ends. Keep upcoming events and outstanding tasks distinct. No transcript ingestion is required for this scope.
- An event's scheduled end is not proof the lesson occurred. The follow-up should be worded as a review/assignment reminder, with a way to dismiss if no action is needed.

## Link generation implementation finding (2026-09-27, code only)
- The active teacher UI has no Stripe payment-link generator for a named student and custom session quantity. Existing 5- and 10-hour package links are fixed offers shown to students. An older booking-pass creator can make a private 1/5/10/custom-session pass immediately, without a Stripe charge, and its former route now redirects; it must not be presented as a paid-link action (`src/pages/teacher/BookingPasses.tsx`, `src/App.tsx`, `src/components/booking/BookingOfferHub.tsx`).
- Current package recognition relies on a registered Stripe Payment Link ID, validated paid amount/currency, and email matching. A paid recognized package can reach `grant_state=awaiting`; teacher grants passes with one click. A new custom student-specific Checkout flow would need its own verified mapping from local quote/student to Stripe Checkout Session and ledger, then the existing teacher grant pattern. It cannot safely assume that any custom Stripe link automatically creates credits (`supabase/functions/booking-commerce-webhook/index.ts`, `supabase/functions/_shared/stripeLedger.ts`, `src/components/teacher/PaymentsPanel.tsx`).
- Superseded recommendation (Round 6 correction): a “Create payment request” action using Stripe Checkout was proposed before Joshua clarified that his requested link is **not for payment**. Do not build that proposal for this shortcut. Stripe's Checkout docs were consulted for that discarded branch: https://docs.stripe.com/api/checkout/sessions/create .
- The dormant `BookingPasses` screen already defaults to five credits, 70-minute sessions, and no expiry; it supports 1/5/10/custom credits up to 50 and accepts a name or email. Creating the pass calls `booking-pass-admin`, which immediately returns a private public `/book/{slug}` URL. Anyone holding the private URL can book without LSAT U sign-in. The screen's former route redirects to Students, so this creation control is not currently exposed there (`src/pages/teacher/BookingPasses.tsx`, `supabase/functions/booking-pass-admin/index.ts`, `src/pages/PublicBooking.tsx`).
- Critical behavior: when the provided email matches an existing student, the admin endpoint's `grant_booking_access` path revokes the prior active pass and creates a new one. A “five more sessions” top-up shortcut would therefore erase remaining credits unless the flow is changed to preserve/top up the existing balance. This must be resolved before surfacing the shortcut. Code finding, not live tested (`supabase/functions/booking-pass-admin/index.ts`).

## Proposed teacher Home composition (awaiting confirmation)
- Teacher account's Home opens the teacher command center, not the student `/classroom` content. Student Home remains student-specific. Reuse the existing Teacher Today feeds where appropriate.
- **Top:** date, concise greeting, student search, and quick actions for Add task, Create session link, and Assign work.
- **Primary row:** Needs your attention with distinct counts/queues for unread messages, package grants, access-tier grants, and post-session or consultation tasks. Each row opens its actual action. Group by type; within a group, overdue/due work precedes recent items.
- **Alongside:** upcoming agenda from the primary Google Calendar, initially the next seven days; all event types visible; event click opens Google Calendar. A recognized past teaching session or consultation creates its durable follow-up only from launch forward. Unknown event types can be manually labelled.
- **Next row:** My list quick add/check-off, linked to full Tasks page. Payments panel shows recent account activity and opens the searchable roughly 90-day history. A paid package creates a separate grant task; a free session link never appears as payment.
- **Student area:** compact recent test results and a searchable student list. Student detail needs real analytics, all work, and per-question homework evidence. Session rows link to student prep context when identity is known.
- **Full Tasks page:** combined view with source/type/student filters, handled history and reopen, private manual tasks, per-student progress counts, and manual blocker status.
- **Create session link:** named student, 1/5/10/custom count, adjustable duration and expiry, explicit additive top-up, then Copy private `/book/{slug}` URL. No payment or redemption step. Show status and revoke action. Fix current pass replacement before release.
- Visual proposal: clear light grid from reference image 2; compact schedule rhythm from image 3; warm task-card treatment from image 6. Use dark emphasis sparingly, with no ornamental analytics.

## Q&A log

### Round 1
#### Q1 - First thing you see
- Asked: whether action items, today's schedule, or student progress should lead.
- Recommended: action queue first, then sessions, progress, and recent activity.
- Captured: “Yeah, I need your attention.” Joshua wants queues for different student-related matters, with upcoming sessions and payments visible.
- Flags: exact queue categories and priority rules -> Joshua.

#### Q2 - Student work
- Asked: whether student assignments, Joshua's follow-ups, or both belong on Home.
- Recommended: separate student obligations from teacher follow-ups.
- Captured: Joshua wants “homework to do” on the dashboard, but did not distinguish student outstanding homework from his own follow-up work.
- Flags: precise meaning of “homework to do” and actions from the queue -> Joshua.

#### Q3 - Performance at a glance
- Asked: which performance changes and level of detail belong on Home.
- Recommended: brief attention list with reasons; detailed analytics on student page.
- Captured: recent test results should be “very brief.” Clicking any student should reveal all work and data, including questions attempted in homework and how the student is performing.
- Tentative: student detail could include session transcripts, pending verification of source and desired placement.
- Flags: whether to show student risk signals or simply latest activity on Home -> Joshua.

#### Q4 - New activity
- Asked: which events persist as actionable alerts versus appear as routine feed activity.
- Recommended: actionable requests, unread messages, payment exceptions, and work requiring response in a queue; routine completions and payments in activity.
- Captured: Joshua reiterated that payments and student messages belong on the dashboard. He mentioned a screenshot and a private student message, but no screenshot/message was attached in this reply. No alert persistence rules were confirmed.
- Flags: alert categories, resolution/read behavior, and any referenced screenshot -> Joshua.

#### Q5 - Visual direction
- Asked: which of six references should guide the page.
- Recommended: image 2 layout with image 6 warmth.
- Captured: take the best features from all six images and other suitable sources; prioritize utility and visual clarity. Joshua did not choose one reference.
- Flags: exact visual composition can be resolved during design review -> Joshua.

#### New topic raised - Completed session context
- Captured: Joshua wants a way to incorporate a transcript or completed-session record, potentially via a note attached to the Google Calendar event.
- Tentative: the Calendar note may be the source; this is not verified.
- Flags: inspect existing session/transcript data path -> Codex; decide where it appears and whether any automation is desired -> Joshua.

### Round 2
#### Q6 - Attention queues
- Asked: which events should wait for Joshua.
- Recommended: separate queues by type and put time-sensitive items first.
- Captured: unread messages; package payments requiring a grant; students requiring an access grant; Joshua's post-session work assignment. Joshua explicitly excluded tutoring requests, student homework needing review, missed homework, and generic session follow-ups.
- Flags: how to determine when a grant is actually pending and whether any other teacher tasks join this queue -> Joshua after code fact check.

#### Q7 - Homework
- Asked: student work owed, work needing Joshua's review, and work Joshua needs to assign.
- Recommended: include all three with distinct labels.
- Captured: only homework Joshua needs to assign matters on this dashboard. Student homework completion or missed homework is not a problem to surface here.
- Flags: post-session assignment task generation and completion rules -> Joshua.

#### Q8 - Messages
- Asked: whether opening a message clears the alert or whether it persists until reply/handling.
- Recommended: separate unread from needs-reply.
- Captured: opening a student's message should clear its alert. Joshua also said opening notifications might clear it; the exact trigger is ambiguous.
- Flags: whether viewing the notification list alone marks each item read, versus opening the specific message -> Joshua.

#### Q9 - Upcoming sessions
- Asked: whether a session should open latest homework, recent result, prior note, agenda, or all behind one click.
- Recommended: time, student, and short prep cue on Home; full context one click away.
- Captured: yes, upcoming sessions should provide this preparation help. No narrower field selection was given.
- Flags: inspect available source data -> Codex; choose concise Home fields after seeing a proposed design -> Joshua.

#### Q10 - Student attention
- Asked: flag meaningful changes versus show every student's latest activity.
- Recommended: flag only changes needing teaching action; full activity on student view.
- Captured: Joshua emphasized an organized place for his tasks. He did not choose a student-performance alert rule.
- Flags: whether any academic-performance item belongs in the Home action queue -> Joshua.

#### New topic raised - Tier and feature access
- Captured: Joshua wants a visible queue of students who need access, a quick grant for tier 1/2/3 or full access, and a more detailed feature-permission path, using or connecting to the existing Teacher Workspace controls.
- Flags: inspect existing tier/feature model and grant paths -> Codex; define safe quick-grant defaults and trigger -> Joshua.

### Round 3 (partial answers)
#### Q11 - When to create an assignment task
- Asked: task creation on tutoring-session end, transcript timing, and exclusion of consultations/cancellations.
- Recommended: create on completed tutoring session; attach transcript later; exclude consultations/cancellations.
- Captured: all Google Calendar events should be visible on Home, including sessions and consultations. After a completed session, a task should say Joshua needs to assign work or notes. Transcript ingestion is unnecessary.
- Flags: whether consultation and non-teaching events create any handled task, and how the system distinguishes tutoring from other Calendar events -> Joshua plus code check.

#### Q12 - Figuring out what to assign
- Asked: open a student-context workspace and optionally draft suggestions for Joshua to approve.
- Recommended: context and drafts; no automatic assignment.
- Captured: Joshua narrowed the Home requirement to a reminder/task to assign work or notes after the session. He did not request automated assignment suggestions in this answer.
- Flags: whether a separate assignment-planning workspace is in scope -> Joshua, can be deferred beyond the Home build.

#### Q13 - Finishing that task
- Asked: automatic completion on saved assignment, manual completion, or either.
- Recommended: automatic on assignment save plus “No assignment needed.”
- Captured: task should stay in the queue until Joshua presses a check mark or similar “handled” control. He may leave it there if unfinished. This supersedes the automatic-completion recommendation.
- Flags: whether “handled” is reversible and whether a note is optional -> Joshua.

#### Q15 - Transcript home
- Asked: LSAT U transcript storage versus Calendar event note as source.
- Recommended: LSAT U session record with Calendar link.
- Captured: transcript ingestion is not needed for this teacher dashboard. Joshua believes Friday Calendar events already have attached notes/transcripts and requested inspection. Calendar event should open in Calendar.
- Flags: inspect Friday Calendar events and avoid moving transcript data without a later request -> Codex.

#### New question - Calendar scope
- Captured: Joshua wants all Calendar events, future events visible on Home, click through to Calendar, and a synchronized schedule. He asked whether this is possible and for the best implementation route.
- Flags: inspect current Calendar sync, event fields, Friday examples, and upcoming schedule -> Codex.

### Round 4
#### Q17 - Which calendars
- Asked: primary calendar versus all visible calendars.
- Recommended: primary calendar initially.
- Captured: “Stick with my Google Calendar. Just stick with one calendar.” Use the primary calendar already connected to LSAT U.

#### Q18 - Which events create a task
- Asked: tutoring sessions only versus consultations and other events.
- Recommended: tutoring sessions create work/notes tasks; other events visible without task.
- Captured: sessions for existing students should create homework-and-notes work. Consultations should create a follow-up or check-in task. Joshua's phrase “And three consultations, check-in” needs clarification before defining timing or a sequence.
- Flags: exact consultation action/timing and detection of consultation versus existing student -> Joshua and implementation audit.

#### Q19 - Existing sessions
- Asked: create a backlog from sessions before launch or start after launch.
- Recommended: start after launch.
- Captured: “No, it shouldn't fill sessions.” No historical session-task flood at launch.

#### Q20 - Marking handled
- Asked: move checked tasks into searchable Handled history with reopen.
- Recommended: yes, with history and reopen.
- Captured: “As long as I clear it, it should be…” Joshua wants a clear action that removes a handled task from the active list. He did not explicitly confirm searchable handled history or reopening.
- Flags: desired handled history and reopen behavior -> Joshua, can be resolved with a mockup.

#### New topic - Two to-do areas and student task tracking
- Captured: a second to-do list supports manual add and crossing off. Automatic items may include enrollment after package payment. Joshua wants quick visual task widgets that open a fuller page, with tasks grouped by student or task and a progress/blocker measure such as percentage or count completed.
- Tentative: there may be a course or district checklist; dictation was unclear, so no product definition is assumed.
- Flags: task-list ownership and separation, package enrollment exact action, student versus teacher task visibility, progress denominator, and meaning of the named checklist -> Joshua.

### Round 5
#### Q21 - Two task areas
- Asked: separate auto-generated Needs your attention and manually editable My list on Home, each linking to full Tasks page.
- Recommended: yes, with student/type filters in full page.
- Captured: Joshua explicitly wants a quick to-do list on Home and a link to an expansive platform page; he then accepted the recommendation for all Q21-Q25.

#### Q22 - Consultations
- Asked: whether consultations create a follow-up when they end, and what “three consultations” meant.
- Recommended: one follow-up at consultation end, manual handled.
- Captured: Joshua accepted the recommendation. The phrase “three consultations” remains unparsed and is not treated as a three-day reminder.

#### Q23 - Student task tracker
- Asked: progress count for Joshua's tasks per student and manually set blocked state.
- Recommended: yes.
- Captured: accepted.

#### Q24 - Student visibility
- Asked: manually added student-linked item private to Joshua versus visible to student.
- Recommended: private; student assignment separate.
- Captured: accepted.

#### Q25 - Package payment
- Asked: paid package creates “Enroll and grant passes” for Joshua rather than automatically granting.
- Recommended: yes, preserving prior one-click teacher grant decision.
- Captured: accepted.

#### New idea - Quick link generator
- Captured: Joshua wants an easy shortcut to create an individual-student link for a chosen session quantity, such as five, and possibly add a credit when the link is used. He asked for a judgment on whether this is a good feature.
- Superseded by Round 6: the link is not for requesting payment.
- Flags: inspect existing booking-pass flow -> Codex; determine redemption/grant behavior and why a link is needed versus direct admin grant -> Joshua.

### Round 6 (correction)
#### Q26-Q29 - Link type
- Asked about paid Checkout link, price, payment follow-up, and copy/send behavior.
- Captured: “not requesting payment.” Joshua corrected the premise. Treat this as a credit/access link with no charge; do not infer Stripe Checkout, a price, or an enrollment/payment task from this shortcut.
- Flags: does opening/redeeming the link create credits, or is it a shortcut to an admin grant screen; is it single use and bound to one student; should generated links be copied only -> Joshua.

### Round 7 (correction)
#### Q30 - What using the link means
- Asked: whether the student redeems a single-use credit link or the link opens a teacher grant screen.
- Captured: “I don't know what you mean by redeem it, but they should be able to use it as soon as possible. And that link should be there. If I send them a link, they should be able to use it no problem.” No student redemption ceremony is wanted.
- Superseded recommendation: provide a signed-in `/booking` link. Existing code actually provides a public private `/book/{slug}` link, which fits Joshua's no-friction requirement better.
- Flags: confirm that this existing private booking-pass link is the intended shortcut; decide whether adding sessions to an existing student must preserve unused credits -> Joshua.

### Round 8
#### Q31 - Additional sessions
- Asked: if a student has 2 sessions left and Joshua creates a 5-session link, should the student have 7.
- Recommended: yes, preserve existing sessions.
- Captured: “yes to both.” The grant is additive, not replacement. This supersedes the current `grant_booking_access` replacement behavior for this shortcut.

#### Q32 - Private no-login link
- Asked: whether an easy private link that can be forwarded is acceptable, with status and revocation controls.
- Recommended: yes.
- Captured: “yes to both.” Private `/book/{slug}` remains usable without login; Joshua needs visibility into its status and an option to revoke it.

### Round 9
#### Q33 - Unclassified Calendar events
- Asked: leave uncertain events visible and let Joshua label them Session or Consultation; auto-create tasks only for clearly classified events.
- Recommended: yes.
- Captured: Joshua approved the recommendation.

#### Q34 - Quick access grants
- Asked: Tier 1 full, Tier 3 basic, and Customize for Tier 2.
- Recommended: yes; Tier 2 opens feature picker.
- Captured: approved.

#### Q35 - Message alerts
- Asked: specific message open clears its unread alert; opening notification list alone does not.
- Recommended: yes.
- Captured: approved.

#### Q36 - Test results
- Asked: brief Home result linking to full analytics, not a task to clear.
- Recommended: yes.
- Captured: approved.

#### Q37 - Handled tasks
- Asked: checked task leaves active queue but remains in Handled history with reopen.
- Recommended: yes.
- Captured: approved.

#### Checklist phrase
- Asked: meaning of “course through the district checklist.”
- Captured: Joshua said it was accidental dictation. No such checklist is part of this dashboard brief.

## Open flags (pending input)
- Final shared-understanding confirmation of the consolidated teacher dashboard brief -> Joshua.
- The current tier, pass, and Calendar findings are code-level. Live behavior of newly proposed flows is untested because no implementation has begun.
- Queue ordering and visual composition can be settled in the mockup if Joshua approves the brief. Proposed defaults: due/urgent work before recent activity; compact light layout with warm accents and limited charting.
