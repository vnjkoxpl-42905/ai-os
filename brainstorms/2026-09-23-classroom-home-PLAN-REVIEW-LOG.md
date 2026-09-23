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
