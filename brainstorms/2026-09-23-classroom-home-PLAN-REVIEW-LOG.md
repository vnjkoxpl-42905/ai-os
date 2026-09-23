# Plan Review Log: Classroom Home redesign
Started 2026-09-23. MAX_ROUNDS=3. Reviewer: Codex gpt-6-astra, reasoning effort medium, read-only sandbox.

## Round 1 - Codex (thread 01a0cd63-8505-7c10-9a99-39e0cd4a974d)

## 1. FLAWS

The design direction is implementable, but the plan needs corrections to its data contracts, launch behavior, and inbox model. These findings are from repository code; deployed schema and student rendering were not verified. No files were modified.

1. **“Smart Drill filtered to a type” is not an existing launch contract.** Adaptive Smart Drill accepts no type/count parameters; filtered practice is a separate launch kind. Implementing the proposal literally either ignores the filter or changes Smart Drill, which is explicitly out of scope. See [drillLaunch.ts:94](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/lib/drillLaunch.ts:94).  
   **Fix:** Launch type/count selections through `kind: 'filter'`, optionally with the existing smart presentation; keep adaptive Smart Drill as its own action.

2. **The all-practice data gap is confirmed, not merely an open question.** `attempts` covers the LR runner; RC records separately, and bootcamp exercises have separate stores. An active RC student could otherwise receive an empty or misleading performance area. See [sectionFreshness.ts:16](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/lib/sectionFreshness.ts:16), [rcProgress.ts:151](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/features/rc/api/rcProgress.ts:151), and [supabase-progress.ts:78](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/topics/abstract/lib/supabase-progress.ts:78).  
   **Fix:** Add a source-to-lens matrix before implementation, with source-specific adapters and explicit coverage labels; do not present LR accuracy as all-practice accuracy.

3. **Several proposed inputs are not available in the named shape.** The assignment feed exposes status and display copy, not structured scores or completion timestamps; `trap_pattern` belongs to journal notes, not `wrong_answer_journal`; sections have legacy score/time fallbacks already handled by a reader. See [useAssignedTodoFeed.ts:16](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/hooks/useAssignedTodoFeed.ts:16), [wajNotesService.ts:29](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/lib/wajNotesService.ts:29), and [sectionHistory.ts:25](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/lib/sectionHistory.ts:25).  
   **Fix:** Name the actual readers and joins per lens; never parse subtitle text for scores or treat manual completion as demonstrated mastery.

4. **The rollup cannot produce the specified 30-day metric.** Its buckets are current seven days, previous seven days, and everything older; the last bucket cannot be trimmed to 30 days. It also counts attempt rows, not distinct questions. See [rollup migration:47](C:/Users/Joshu/dev/ai-os/projects/lsatu/supabase/migrations/20260710031524_bf477c7f-e3a5-4717-93b8-a4e2c72c69ca.sql:47).  
   **Fix:** Add a bounded Home-specific RPC with explicit repeat/review rules and distinct-question sample counts, preserving the existing Analytics contract.

5. **The selection rules rank activity volume, not usefulness.** Twenty question attempts and one completed section have incomparable units; the same section may drive several redundant cards. “Minimum eight” also leaves undefined what happens with fewer than three eligible lenses, an inactive student, or an unsupported pinned lens.  
   **Fix:** Define normalized per-lens scores, deterministic ties, redundancy suppression, sample rules, and a pinned-insight fallback; show fewer cards when evidence is insufficient.

6. **The inbox already duplicates events across its two sources.** Assignment and recap writers create both a chat message authored as Joshua and a notification. A simple merge displays the same event twice, and sender-based pinning elevates automated assignment notices as personal messages. See [classroomNotify.ts:87](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/lib/classroomNotify.ts:87) and [sessionBundleNotify.ts:48](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/lib/sessionBundleNotify.ts:48).  
   **Fix:** Introduce an event identity and explicit message origin for new writes, with a conservative legacy display policy; preserve the existing message records.

7. **“One hook, two queries, shared mark-read” substantially understates the work.** `useInbox` already exists with many consumers and multiple sequential reads. Messages use participant read timestamps, Home dismissal uses a separate watermark, and notifications use booleans. Independent hook instances do not provide shared optimistic state. See [useUnreadMessageCount.ts:9](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/hooks/useUnreadMessageCount.ts:9), [useInbox.ts:253](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/hooks/useInbox.ts:253), and [useInbox.ts:276](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/hooks/useInbox.ts:276).  
   **Fix:** Add a separately named unified-feed adapter backed by shared cache/provider state; define thread-versus-message rows, badge units, read behavior, and dismissal independently.

8. **The existing notification hook cannot support “every notification” reliably.** It fetches only 30 rows, computes unread count from those rows, but marks *all* unread rows read. Filtering hidden types after that limit can leave visible events inaccessible. New event types also require a database constraint change, not just TypeScript additions. See [useNotifications.ts:55](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/hooks/useNotifications.ts:55), [useNotifications.ts:130](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/hooks/useNotifications.ts:130), and [notification constraint:1](C:/Users/Joshu/dev/ai-os/projects/lsatu/supabase/migrations/20260506163026_3253f980-7520-4671-a14e-1a1795ba5985.sql:1).  
   **Fix:** Filter before pagination, fetch a matching unread total, scope bulk-read consistently, and specify each event’s writer, type, destination, and retry/idempotency behavior.

9. **The proposed inventory misses existing student Home functionality.** The current view renders work rows, intercepts timed-section links for briefings, and records report-card viewing. Phase one could remove graded-work visibility before phase three supplies its replacement. See [ClassroomHomeView.tsx:168](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/components/classroom/home/ClassroomHomeView.tsx:168), [ClassroomHomeView.tsx:197](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/components/classroom/home/ClassroomHomeView.tsx:197), and [ClassroomHomeView.tsx:362](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/components/classroom/home/ClassroomHomeView.tsx:362).  
   **Fix:** Add a feature-preservation checklist and retain those paths until their replacements ship; choose “Continue” from eligible work, not an arbitrary hero/feed row.

10. **Pinning has an incomplete authorization and lifecycle contract.** “Admin write, student read own row” omits admin reads for Hub hydration, identity mapping, invalid lens/params handling, and unpinning. This is an implementation gap, not evidence of an existing exploit.  
    **Fix:** Specify admin SELECT/write policies, authenticated student ownership checks, validated lens parameters, server-controlled attribution, unpin behavior, and cross-student RLS tests.

11. **A viewport breakpoint and another shortcut listener are insufficient integration plans.** The finder already registers Ctrl/Cmd+K, lazy-loads banks, and restores/traps focus. A second launcher instance risks opening two dialogs. Two columns must also fit the available Classroom stage when other panels occupy space. See [QuestionFinder.tsx:64](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/components/questionfinder/QuestionFinder.tsx:64) and [QuestionFinder.tsx:148](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/components/questionfinder/QuestionFinder.tsx:148).  
    **Fix:** Use one launcher owner, preserve permission gates and lazy loading, base columns on available width, and require student-view checks at narrow/mid/wide and sidecar-docked sizes, including keyboard focus and reduced motion.

## 2. IDEAS

Ranked by value relative to effort:

1. **Make the launcher an address bar with contextual actions. — Very high value / medium effort**  
   Keep `PrepTest → Section → Question` visible when opened. Once a section is selected, offer **Start section**; once a question is selected, offer **Open question**. Put type/count practice in a separate tab within the same panel. Preserve LR/RC routing through the existing finder and launch codec. This turns dropdown selections into useful actions without another configuration screen.

2. **Add “Flagged” and “Needs review” shelves inside the launcher. — High value / low–medium effort**  
   A student often remembers *why* they need a question, not its address. Show compact address rows with their flag note or review status, searchable alongside PT/section/question. Existing sources: [flaggedService.ts:31](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/lib/flaggedService.ts:31) and [wajNotesService.ts:29](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/lib/wajNotesService.ts:29). Keep this inside the launcher rather than adding a recent-drills card.

3. **Show section freshness and timer choice before launch. — High value / low–medium effort**  
   Annotate LR section options with “24 of 25 questions unanswered” and offer fresh-only filtering. Carry the existing standard, accommodated, custom, or untimed setting into the launch. The machinery exists in [sectionFreshness.ts:46](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/lib/sectionFreshness.ts:46) and [drillLaunch.ts:100](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/lib/drillLaunch.ts:100). For RC, show unknown freshness until its own history is connected.

4. **Give every insight an evidence drawer. — High value / low–medium effort**  
   Beneath “Strengthen questions need attention,” offer **See the questions behind this**. Show source, dates, sample size, and exact question addresses before the practice action. Existing section detail includes question records, breakdowns, and saved analysis: [sectionHistory.ts:25](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/lib/sectionHistory.ts:25). This makes the dashboard a reasoning tool and exposes bad aggregation early.

5. **Offer “Review these” alongside “Try new ones.” — High value / medium effort**  
   A weak-type insight should distinguish understanding the mistakes already made from testing the skill on fresh questions. Use journal review status and saved section question records for the first action; use a filtered launch with explicit exposure filtering for the second. Label repeated work so it cannot masquerade as fresh performance.

6. **Reuse section diagnoses rather than inventing a second diagnostic engine. — High value / medium effort**  
   The app already saves section analysis and has rules for timing, blind review, and confidence errors. Let Home select and summarize an eligible existing finding, then link to its report. See [sectionAnalysis.ts:568](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/lib/sectionAnalysis.ts:568) and [sectionHistory.ts:44](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/lib/sectionHistory.ts:44). That produces more specific guidance and keeps Home consistent with the results page.

VERDICT: REVISE

### Claude's response
Accepted all 11 flaws (verified drillLaunch kind filter exists at drillLaunch.ts:163). Changes: preservation checklist; launcher uses kind filter for types, Smart Drill untouched; source-to-lens matrix with adapters and coverage labels; new additive RPC with distinct-question 30-day window; normalized scoring, floors, redundancy, pinned fallback; separate useHomeFeed on shared TanStack Query; dedup via additive event_key/origin + legacy heuristic; notification query fixes and CHECK constraint extension with named writers; full pin RLS; container-query layout and verification matrix.
Ideas adopted: 1 (contextual address bar), 3 (freshness + timer), 4 (evidence drawer), 6 (reuse section diagnoses). Ideas 2 (shelves) and 5 (review vs new) put to Joshua as product decisions, not argued.

## Round 2 - Codex

## FLAWS

Most earlier issues are addressed. These material gaps remain:

1. **The launcher still promises capabilities the launch contract lacks.** `kind: 'section'` feeds the LR question bank; RC uses a separate route. `kind: 'filter'` has no fresh-only option, so “Try new ones” can repeat answered questions. See [Drill.tsx:540](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/pages/Drill.tsx:540), [drillRunSpec.ts:146](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/lib/drillRunSpec.ts:146), and [questionFinderSearch.ts:413](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/components/questionfinder/questionFinderSearch.ts:413).  
   **Fix:** Specify bank-aware section dispatch and an exposure-aware selection path, including insufficient-fresh-question behavior and preservation of the selected queue on resume.

2. **The proposed deduplication fields cannot reliably connect messages to notifications.** `event_key` exists only on notifications; `origin` distinguishes authorship but cannot identify matching events. Thread-level origin is also inadequate because one thread contains both human and automated messages. Notification uniqueness does not prevent duplicate chat inserts on retries. Existing writers perform separate inserts: [classroomNotify.ts:87](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/lib/classroomNotify.ts:87).  
   **Fix:** Store a shared event identity on each generated message and notification, make both writes retry-safe, and place origin on individual messages.

3. **Deduplication, unread counts, and read actions still disagree.** A separate notification count includes events hidden during client-side deduplication. Reading the visible thread does not necessarily clear its hidden notification. Furthermore, one “latest message” row can show a student reply or automated notice while burying Joshua’s unread human message; the current inbox checks only the latest message when calculating unread state. See [useInbox.ts:189](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/hooks/useInbox.ts:189).  
   **Fix:** Define one canonical visible-event model for counts and read actions, and explicitly select the human-message preview independently of the thread’s latest message.

4. **The new notification columns need protection in the existing write guard.** Students can update their notification rows to mark them read; the immutability trigger protects an enumerated list of columns. Merely adding `event_key` and `origin` leaves those new fields outside that protection. See [notification guard:120](C:/Users/Joshu/dev/ai-os/projects/lsatu/supabase/migrations/20260506124235_9378ad65-24e0-49bb-8d59-0a8fc28211f2.sql:120).  
   **Fix:** Extend the database guard or restrict column update privileges, with tests proving students cannot alter event identity or origin.

5. **The section reader does not provide the claimed legacy fallbacks.** I overstated this in my previous review. It defaults missing `initial_total`, `initial_percent`, and `total_time_ms` to zero instead of deriving them from legacy fields; missing dates become the current time. It also does not restrict results to timed sections. Reusing it unchanged can manufacture zero scores, apparent recent activity, and a false “Timed sections” label. See [sectionHistory.ts:113](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/lib/sectionHistory.ts:113); untimed section analysis is explicitly supported in [sectionHistorySave.ts:237](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/lib/sectionHistorySave.ts:237).  
   **Fix:** Correct the adapter’s legacy normalization, preserve unknown dates, and use “Sections” unless timing is verifiable.

6. **The LR RPC cannot supply the engine’s promised evidence or recency.** It returns only type, question count, and correct count, while selection needs the latest activity date and the drawer needs exact supporting attempts. A separate unconstrained attempt query could disagree with the RPC’s latest-per-question exclusions. The universal question-address drawer also does not fit assignment-status or bootcamp-progress lenses.  
   **Fix:** Define source-specific evidence payloads; return recency from the RPC and provide an evidence query using exactly the same window and attempt-selection rules.

7. **Session reminders still have no identified writer or implementation phase.** “Existing reminder writer, confirm” does not establish that reminders are emitted. Phase five names graded work and booking changes only. A notification type and schedule link do not create a reminder.  
   **Fix:** Identify the existing producer or explicitly schedule its implementation, including delivery timing, cancellation/rescheduling handling, and idempotency.

## IDEAS

Only new additions, ranked by value/effort:

1. **Prioritize “Needs review” by the student’s actual review date. — High value / low effort**  
   The journal already stores `reattempt_due_at` and `next_action`. Within the accepted shelf, surface due reviews first and show the student’s own next step beside the question address. This makes the shelf a useful practice queue rather than another collection. Source: [wajNotesService.ts:31](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/lib/wajNotesService.ts:31).

2. **Offer “Practice this exact skill” from a section diagnosis. — High value / medium effort**  
   Some findings concern a feature or reasoning pattern within a question type. Section analysis already breaks results down by type, family, feature, reasoning, and difficulty; the launch codec supports question-feature filters. Where the identifiers match, prefill a focused practice selection and display its filters before launch. Sources: [sectionAnalysis.ts:160](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/lib/sectionAnalysis.ts:160), [drillLaunch.ts:163](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/lib/drillLaunch.ts:163).

VERDICT: REVISE

### Claude's response
Accepted all 7. Verified no reminder producer exists (reminder type appears only in the hook, the list component and migrations). Changes: bank-aware section dispatch; additive excludeAnswered on filter launches with shortfall message and queue stored for resume; shared event_key on messages and notifications with partial unique indexes; per-message origin; trigger protection; server-side home_feed RPC as the one visible-event model for list, counts and reads; human-message preview; new Sections adapter instead of the zero-filling reader, labelled Sections unless timing is proven; LR RPC returns last_attempt_at plus an evidence RPC on the same selection; source-specific evidence; session reminder producer specified as a new scheduled job. Ideas adopted: Practice this exact skill; Needs review ordering added to Joshua's product question.

## Round 3 - Codex (final, MAX_ROUNDS reached)

## FLAWS

Two material problems remain in the revised fixes. The other addressed findings can stay closed.

1. **The proposed RC dispatch opens one passage, not a section.** The finder’s RC link supplies `passage=<id>`. The player then creates a session with exactly that passage and `DEFAULT_CONFIG`, so this route does not preserve the selected full section or timer. This is confirmed by [RcPlayer.tsx:130](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/features/rc/pages/RcPlayer.tsx:130). The player separately supports multiple passage IDs and explicit configuration at [RcPlayer.tsx:141](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/features/rc/pages/RcPlayer.tsx:141).  
   **Fix:** Specify an RC section launch that resolves all passages in section order, creates a session with the intended timing configuration, and navigates using its session ID.

2. **Event-specific reads cannot safely use a conversation-wide read timestamp.** Suppose Joshua sends an unread human message, then an assignment event arrives. Opening the assignment and advancing `last_read_at` also marks the earlier human message read, even though the student only opened the assignment. That contradicts the revised promise to mark only the selected event’s rows read. The existing mechanism is explicitly conversation-wide: [useInbox.ts:247](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/hooks/useInbox.ts:247).  
   **Fix:** Keep generated-event read state separate from the conversation watermark; advance that watermark only when the conversation is read, and use event acknowledgements—including a fallback for message-only delivery—to synchronize generated duplicates.

## IDEAS

No additional ideas this round. The plan already contains enough useful additions; resolving these two behavioral contracts is more valuable than expanding scope.

VERDICT: REVISE

### Claude's response
Accepted both. RC section launch now resolves all passages of the section and creates a session with the chosen timer config, navigating by session id. Read state split: conversation watermark moves only when a conversation is opened; generated events use a new event_acks table. These two fixes were applied after the final round and were NOT re-reviewed by Codex.

## Outcome
No APPROVED verdict within 3 rounds. No open disagreement: every Codex finding was accepted. Remaining product decisions for Joshua: Flagged/Needs review shelves; Review these vs Try new ones; whether session reminders are wanted.

## Act 3 - Build (phase 1)
### Round 1 - Codex build (thread 01a0cd7c-b895-7c82-8b52-ed5405c2fb6e, gpt-6-astra medium, worktree feat/home-v2-phase1)
Codex report: new layout (finder bar + bell, three action cards, hero + assigned rows in the performance slot, inbox, next session, Read Recall Colour card kept below it, week strip untouched), pickContinueWork in homeModel, QuestionFinder open() handle, 8 new tests; typecheck + 51 Home tests passed. Added two unrequested dev preview files in src/dev.
### Claude's verdict
Read the full diff. Fixed directly (under 20 lines, no fix round spent): QuestionFinder had been gated on access.drill, a regression from the unconditional original; restored it and corrected the new test that asserted the gate. Deleted the src/dev preview files (out of scope, unreferenced). CSS diff is additive only; week strip JSX and rules unchanged. Verified: npm run typecheck clean; vitest home + questionfinder 107/107 pass; eslint 1 pre-existing warning. supabase/functions/mcp/index.ts is regenerated by the dev server; it stays unstaged. Visual check blocked: local dev server needs a signed-in account. Not committed.
### Visual check and ship (2026-09-23)
Checked on localhost:8091 signed in as Joshua (teacher): 1440 / 900 / 375 widths, dark mode, no horizontal overflow. Found and fixed an empty main column when there is no hero or assigned work (side cards now spread across) and two action cards leaving a blank third slot (actions now share the row). Six 400 console errors seen; not attributable to phase 1, which adds no requests. Student view verified by tests only. Committed and opened PR #133 (not merged, not deployed).

## Act 4 - v3 design critique (gpt-6-astra medium, read-only, thread 01a0cd9a-e74c-7320-bf98-d043eb7fe866)
Verdict: not yet at reference level; oversized greeting, competing numbers, crowded bubbles overlapping the text.
Taken: fixed bubble/text overlap; hero numbers cut to two at 44px, reviews removed from hero; continuous bars with question counts and "pts vs previous 30"; last section as two labelled bars; "Inbox · 3" labelled control; "Practice Necessary Assumption"; "Continue"; "Session details"; removed "Chosen for you" and dot halo; plainer headline copy.
Rejected: removing glows and warm gradient, shrinking the hero to a 96px header, replacing bubbles with bars. Reason: Joshua rejected v2 as too uniform and his references use exactly these (Homies tinted hero, Be.run bubbles, WeatherWise glow). Precision lives in the bar list below the bubbles.
Empty-state rules from the critique carried into the build spec.

## Act 5 - v3 build plan review (MAX_ROUNDS=3, gpt-6-astra medium, read-only)
Plan rewritten as the v3 first build from the capture (rounds 1-10, converged Q2-Q7) and the dual research.

### Round 1 - Codex (thread 01a0cf1d-8c21-7e01-ba34-e4b621c1ca13)
NOTE: reviewed the superseded plan file (Claude's rewrite had failed to save). Findings 2-6 concern the unified-notifications design, which v3 defers whole to build two; kept for that plan.

The plan needs revision before implementation. It still specifies the superseded release sequence, and several database and interaction contracts are incomplete.

1. **P1 — The build order contradicts the settled decisions.** [PLAN.md:96](C:/Users/Joshu/dev/ai-os/brainstorms/2026-09-23-classroom-home-PLAN.md:96) ships layout separately from insights. The [capture:135](C:/Users/Joshu/dev/ai-os/brainstorms/2026-09-23-classroom-home-visual-upgrade.md:135) explicitly supersedes PR #133 and combines them; [capture:154](C:/Users/Joshu/dev/ai-os/brainstorms/2026-09-23-classroom-home-visual-upgrade.md:154) also requires the finding-to-resource registry and evidence-attached Ask draft, neither of which appears in the plan.
   **Fix:** Replace the release sequence with the settled v3 split and explicitly enumerate the registry, Ask draft, and subsequent session-brief/review/Today work.

2. **P1 — The proposed message uniqueness constraint cannot be created as specified.** [PLAN.md:80](C:/Users/Joshu/dev/ai-os/brainstorms/2026-09-23-classroom-home-PLAN.md:80) requires `(recipient, event_key)` on both tables, but messages contain `conversation_id` and `sender_id`, with recipients represented through participants ([schema:24](C:/Users/Joshu/dev/ai-os/projects/lsatu/supabase/migrations/20260416234013_49bfd508-03f2-4942-a636-2763f1f3af5b.sql:24)). Also, a unique index makes duplicate inserts fail; it does not make retries successful no-ops.
   **Fix:** Define actual per-table identity columns and explicit conflict handling, including recovery when only one of the two writes succeeds.

3. **P1 — Update immutability does not protect event identity at insertion.** [PLAN.md:81](C:/Users/Joshu/dev/ai-os/brainstorms/2026-09-23-classroom-home-PLAN.md:81) protects changes to `origin` and `event_key`, but the existing message INSERT policy permits participant-authored messages without restricting those new fields ([schema:110](C:/Users/Joshu/dev/ai-os/projects/lsatu/supabase/migrations/20260416234013_49bfd508-03f2-4942-a636-2763f1f3af5b.sql:110)). A student could supply a system origin and colliding event key.
   **Fix:** Enforce ordinary-user inserts as `origin='human' AND event_key IS NULL`, reserve generated identities for authorized writers, and test forged inserts.

4. **P1 — Legacy generated events have no defined read transition.** [PLAN.md:82](C:/Users/Joshu/dev/ai-os/brainstorms/2026-09-23-classroom-home-PLAN.md:82) includes legacy rows with null keys, while the following paragraph acknowledges generated events exclusively by key. Those events cannot follow the specified acknowledgement path; legacy messages also lack a defined human/system classification.
   **Fix:** Give legacy feed events stable synthetic identities and explicit classification/read rules without rewriting historical rows.

5. **P1 — The two unread systems will disagree.** [PLAN.md:79](C:/Users/Joshu/dev/ai-os/brainstorms/2026-09-23-classroom-home-PLAN.md:79) leaves `useInbox` untouched, but its unread calculation ignores acknowledgements and uses the latest message ([useInbox.ts:192](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/hooks/useInbox.ts:192)). Opening a generated event can clear the Home bell while leaving the existing inbox unread; opening its conversation updates only the watermark, leaving the new event acknowledgement absent.
   **Fix:** Specify consistent read semantics across Home, the bell, and conversations, and adapt existing unread consumers through a shared selector.

6. **P1 — Rescheduled reminders reuse their old identity.** [PLAN.md:92](C:/Users/Joshu/dev/ai-os/brainstorms/2026-09-23-classroom-home-PLAN.md:92) promises re-keying on reschedule but defines the key only from booking ID and offset. Rescheduling the same booking after its first reminder makes the replacement collide with the old event or inherit its acknowledgement.
   **Fix:** Include a booking revision or scheduled-start timestamp in the key and revalidate that revision immediately before delivery.

7. **P1 — Fresh-practice actions ship before their dependency, and the named queue-building location is wrong.** [PLAN.md:72](C:/Users/Joshu/dev/ai-os/brainstorms/2026-09-23-classroom-home-PLAN.md:72) requires “Try new ones” for phase-two insights, while the filter extension sits with the later By-type work. [drillRunSpec.ts:146](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/lib/drillRunSpec.ts:146) merely constructs configuration; actual bank filtering occurs in [Drill.tsx:565](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/pages/Drill.tsx:565).
   **Fix:** Ship exposure exclusion and persisted-queue resolution before the insight CTA, applying exclusion before sampling and preserving that queue on resume.

8. **P1 — The new RPCs lack an authorization contract.** [PLAN.md:56](C:/Users/Joshu/dev/ai-os/brainstorms/2026-09-23-classroom-home-PLAN.md:56) accepts caller-supplied class IDs and returns question-level evidence, but specifies neither execution security nor cross-student tests; the feed RPC is similarly unspecified. Existing aggregate RPCs deliberately use `SECURITY INVOKER` ([migration:89](C:/Users/Joshu/dev/ai-os/projects/lsatu/supabase/migrations/20260709235900_phase6_query_rpcs.sql:89)).
   **Fix:** Require invoker/RLS enforcement or explicit owner/admin authorization, pinned search paths, bounded inputs, and anonymous/cross-student denial tests for every new RPC.

9. **P2 — The design’s comparative statistics cannot come from the proposed response.** [Home3.dc.html:108](C:/Users/Joshu/AppData/Local/Temp/claude/C--Users-Joshu-dev-ai-os/fe553725-d881-4068-8809-1fb7b342eee9/scratchpad/artifact-files/307bbd6c-86e0-43cd-a5df-8735d306b8fb/project/Home3.dc.html:108) shows change against the previous 30 days; [PLAN.md:56](C:/Users/Joshu/dev/ai-os/brainstorms/2026-09-23-classroom-home-PLAN.md:56) returns one window. Requesting 60 days does not produce two comparable windows because latest-attempt deduplication can select different attempts.
   **Fix:** Return separately defined current/prior buckets with a shared cutoff and sample floors, and hide comparisons lacking sufficient evidence.

10. **P2 — The visual contract omits truthful bubble sizing and accessible labels.** [Home3.dc.html:73](C:/Users/Joshu/AppData/Local/Temp/claude/C--Users-Joshu-dev-ai-os/fe553725-d881-4068-8809-1fb7b342eee9/scratchpad/artifact-files/307bbd6c-86e0-43cd-a5df-8735d306b8fb/project/Home3.dc.html:73) claims circles encode missed questions, but their diameters are hardcoded. The primary bubble also uses white labels over orange; white against `#ff8906` is approximately **2.38:1**. Keyboard testing alone will not catch that.
    **Fix:** Specify area-proportional sizing, readable text independent of bubble size, a textual equivalent, and contrast checks across gradients and themes.

11. **P2 — Empty, failed, and unavailable data remain conflated.** [PLAN.md:66](C:/Users/Joshu/dev/ai-os/brainstorms/2026-09-23-classroom-home-PLAN.md:66) offers only eligible evidence or `null`, then converts zero eligible lenses into “Start here.” A failed reader can therefore masquerade as no practice, and a failed pinned source can become “pinned view has no data,” contradicting [capture:153](C:/Users/Joshu/dev/ai-os/brainstorms/2026-09-23-classroom-home-visual-upgrade.md:153).
    **Fix:** Define loading/error/empty/insufficient/ready adapter states and prohibit failure or pending data from producing empty-state claims.

12. **P2 — RC history reuse risks truncated results and unnecessary downloads.** [PLAN.md:59](C:/Users/Joshu/dev/ai-os/brainstorms/2026-09-23-classroom-home-PLAN.md:59) points to `rcProgress.ts`, whose `getQuestionHistory()` requests all attempts without pagination and whose `listSessions()` requests all sessions. Parallelizing these reads does not make them bounded or guarantee complete results.
    **Fix:** Add a bounded Home aggregate that explicitly handles first attempts, excluded sessions, completion, and recency; fetch detailed evidence only when opened.

13. **P2 — The RC launcher duplicates an existing section launch path.** [PLAN.md:46](C:/Users/Joshu/dev/ai-os/brainstorms/2026-09-23-classroom-home-PLAN.md:46) proposes new session creation, but [rcSections.ts:131](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/features/rc/lib/rcSections.ts:131) already launches complete sections with accommodations, untimed mode, and end-of-set reveal. PR #133 also does not supply the promised Section tab: at branch commit `8b4c406`, `ClassroomHomeView.tsx:287` only opens the existing finder.
    **Fix:** Reuse the existing RC section contract, extend custom timing where necessary, and explicitly build/test Section-tab selection rather than treating PR #133 as that dependency.

Read-only review; no files modified. Findings are based on the supplied documents and source inspection, not runtime or deployed-database verification.

VERDICT: REVISE

### Claude's response
Saved the v3 plan properly. Applied to v3: #7 excludeAnswered applied before sampling at Drill.tsx:565 with persisted queue, same PR as the button; #8 security invoker + pinned search_path + bounded p_days + cross-student tests; #9 current/prior buckets with shared cutoff and floors; #10 computed area sizing, no white-on-orange, list as text equivalent; #11 adapter states loading/error/empty/insufficient/ready; #12 RC lens deferred; #13 Section tab deferred, will reuse rcSectionHref. #1 build order rewritten. #2-#6 carried to build two (notifications deferred whole).

### Round 2 - Codex

Reviewed the saved **“Act 5, Round 1 revision”**. Unified notifications remain excluded. These issues still need correction:

1. **P1 — The section adapter trusts a known bad legacy denominator.** [PLAN.md:35](C:/Users/Joshu/dev/ai-os/brainstorms/2026-09-23-classroom-home-PLAN.md:35) derives totals from `total_questions`, but [sectionHistorySave.ts:324](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/lib/sectionHistorySave.ts:324) documents historical rows carrying zero there while `initial_total` contains the real total. Valid work can become `19/0` or disappear as insufficient.
   **Fix:** Prefer valid `initial_total`, fall back to positive `total_questions`, preserve unknown denominators, and require `br_used` before showing blind-review results.

2. **P1 — Shared SQL logic does not guarantee matching evidence snapshots.** [PLAN.md:32](C:/Users/Joshu/dev/ai-os/brainstorms/2026-09-23-classroom-home-PLAN.md:32) uses `now()` for each RPC, while [line 42](C:/Users/Joshu/dev/ai-os/brainstorms/2026-09-23-classroom-home-PLAN.md:42) freezes the insight for the visit. Opening evidence later can include a new attempt, replace the selected attempt for a question, or exclude one crossing the window boundary.
   **Fix:** Return a snapshot cutoff with the aggregate and pass it to evidence queries, retaining selected attempt IDs where necessary.

3. **P1 — Fresh-only launches can resume an unrestricted queue.** [PLAN.md:47](C:/Users/Joshu/dev/ai-os/brainstorms/2026-09-23-classroom-home-PLAN.md:47) adds `excludeAnswered`, but the existing resume fingerprint includes only the current filter fields ([drillResumeSession.ts:93](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/lib/drillResumeSession.ts:93)). Identical filters with different freshness settings therefore share a resume record unless explicitly changed.
   **Fix:** Include freshness policy in the resume identity, preserve existing identities for unrestricted links, and test launching fresh-only after an unfinished unrestricted run.

4. **P1 — “Timed section” still cannot start a timed section.** [PLAN.md:22](C:/Users/Joshu/dev/ai-os/brainstorms/2026-09-23-classroom-home-PLAN.md:22) deliberately retains #133’s finder action while deferring section launching to build two. On `feat/home-v2-phase1`, `ClassroomHomeView.tsx:287` only calls `open()`; the finder returns individual questions/passages. This leaves a promised primary action without its advertised destination.
   **Fix:** Route the button to an existing working section-selection surface now; defer the new launcher tab independently.

5. **P1 — Keyboard-selectable bubbles cannot also be hidden from assistive technology.** [PLAN.md:51](C:/Users/Joshu/dev/ai-os/brainstorms/2026-09-23-classroom-home-PLAN.md:51) makes bubbles interactive, while [line 53](C:/Users/Joshu/dev/ai-os/brainstorms/2026-09-23-classroom-home-PLAN.md:53) applies `aria-hidden`. A summary label does not restore hidden controls, leaving keyboard focus on elements screen readers cannot identify.
   **Fix:** Either expose labelled bubble controls with selection state, or make bubbles entirely noninteractive and provide selection through accessible list controls.

6. **P2 — Perfect accuracy produces invisible bubbles.** [PLAN.md:51](C:/Users/Joshu/dev/ai-os/brainstorms/2026-09-23-classroom-home-PLAN.md:51) specifies `radius = k * sqrt(missed)` but only falls back when fewer than three types qualify. Three sufficiently practised types with zero misses qualify yet produce zero-radius circles; mixed results also lose labels for perfect types.
   **Fix:** Define an all-zero-misses result state and represent zero-miss types in the list without inventing a minimum bubble area.

7. **P2 — Confidence level 3 falls outside the promised matrix.** [PLAN.md:61](C:/Users/Joshu/dev/ai-os/brainstorms/2026-09-23-classroom-home-PLAN.md:61) counts non-null confidence for coverage and requires 12 rated attempts, but its matrix includes only ratings 1–2 and 4–5. Twelve neutral ratings can satisfy the floor while populating no cells, and displayed totals can disagree with the coverage line.
   **Fix:** Explicitly exclude and disclose neutral ratings, calculating the matrix’s eligibility floor from attempts actually represented in its cells.

No files modified; findings are based on source inspection, not deployed-data verification.

VERDICT: REVISE

### Claude's response
Accepted all 7 (technical). Denominator precedence initial_total > total_questions > unknown, br_used gate; aggregate returns cutoff passed to evidence; freshness in resume identity with test; Timed section now routes to /testing (verified: TestingCentre starts LR and RC sections, App.tsx:546); bubbles non-interactive, list rows are the controls; zero-miss types list-only plus all-zero result state; neutral ratings excluded and disclosed, floor counts only in-cell attempts.

### Round 3 - Codex (final, MAX_ROUNDS reached)

One material issue remains:

**P1 — The headline practice count has no active writer in the inspected code.** [PLAN.md:22](C:/Users/Joshu/dev/ai-os/brainstorms/2026-09-23-classroom-home-PLAN.md:22) uses `daily_stats.questions_answered`, but both the current checkout and `feat/home-v2-phase1` only read that counter. `increment_daily_stats` exists as a migration-defined RPC with no application caller; the drill persistence path writes `attempts` and returns ([Drill.tsx:1482](C:/Users/Joshu/dev/ai-os/projects/lsatu/src/pages/Drill.tsx:1482)). Consequently, completed practice can leave the prominent weekly number stale or zero. No deployed-only writer was verified.

**Fix:** Derive the count from persisted attempts using explicit local-day boundaries, replay exclusions, and an LR coverage label; verify that completing practice increments it.

The seven previous fixes are reflected in the revision. No files modified.

VERDICT: REVISE

### Claude's response
Verified: daily_stats is only read (gamification.ts, streakSystem.ts, useStudentAnalytics.ts, StudentWorkPanel.tsx); no client or function writer. Accepted: weekly count now comes from attempts via a new security-invoker RPC with local-day boundaries and replay exclusions, labelled LR, with an increment test. Applied after the final round; not re-reviewed.

## Act 5 outcome
No APPROVED within 3 rounds; no open disagreement (every finding accepted, 21 total incl. round 1 on the superseded file). Nothing for Joshua to referee. Joshua-owned items in the plan: one review of the action registry before PR 3.
