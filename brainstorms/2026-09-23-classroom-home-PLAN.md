# Plan: Redesign the LSAT U Classroom Home (student view first)
_Round 3 revision by Claude, 2026-09-23, after Codex rounds 1-3 (see PLAN-REVIEW-LOG). The two round-3 fixes were applied after the final round and were not re-reviewed by Codex._

Decisions come from Joshua's grill-me interview: `brainstorms/2026-09-23-classroom-home-visual-upgrade.md`. Visual reference: https://claude.ai/artifact/6zF3FgewiMA7pCZSk766Xt (v1; its PT trend, goal dial, streak, month calendar and week curve are REJECTED).

## Situation
- App: `projects/lsatu` (React + Vite + TS + Tailwind, TanStack Query present, Supabase via Lovable Cloud). Home = `/classroom` in the Classroom frame (`src/components/classroom/CONTEXT.md`).
- Home code: `src/components/classroom/home/` — `useClassroomHome.ts`, `homeModel.ts` (pure, tested), `ClassroomHomeView.tsx`, `home.css`.
- ~25 one-to-one students plus Joshua. Student copy follows `wiki/teaching-voice.md`; no em dashes.
- Hard rules: completed student work never lost or modified (additive migrations only). Branch per session, PR to main. Lovable Cloud: Edge Functions deploy through Lovable, confirm with Joshua first. Frontend reaches lsatprep.study only via Lovable deploy. A teacher is never the student.
- Done separately: PR #132 (sideways scrollbar).

## Goal
A sleek, high-end Home that (1) gets a student into practice in one click, (2) shows the performance insight that matters most for THIS student's recent work, and (3) puts every message and notification in one place.

## Approach

### 0. Feature-preservation checklist (applies to every phase)
The redesign must keep, until a named replacement ships:
- Assigned work rows and their actions (`ClassroomHomeView.tsx:168`).
- Timed-section link interception that shows the Section briefing (`ClassroomHomeView.tsx:197`, `SectionBriefing.tsx`).
- Report-card seen tracking (`ClassroomHomeView.tsx:362`, `reportCardSeen.ts`).
- Home message preview dismissal watermark.
- Access gates in `HomeAccess` (messages, schedule, activities, drill): a hidden feature stays hidden.
- Next seven days strip: markup, classes and behavior unchanged.
Existing `ClassroomHomeView.test.tsx` cases stay green; new cases added per phase.

### 1. Layout
Top to bottom; two columns decided by the Home container's available width (CSS container query), not the viewport, so a docked side panel collapses it to one column.
1. **Practice launcher** (the existing `QuestionFinder`, extended; one instance, one Ctrl/Cmd+K owner, lazy bank loading and focus trap kept) + inbox bell + greeting.
2. **Three one-click actions**:
   - Continue assigned work: the earliest-due eligible assigned row (not overdue-dismissed, not teacher-addressed); hidden when none. Timed sections still route through the briefing.
   - Smart Drill: `kind: 'smart-drill'` (adaptive, unchanged).
   - Start a timed section: opens the launcher on its Section tab.
3. **Performance area**: one main insight + up to three minor ones (fewer when evidence is thin).
4. **Inbox panel** (right column): unified feed, Joshua's human-written messages pinned.
5. **Next session** card (dark).
6. **Next seven days**: unchanged.
- Look: light and warm, dark cards for emphasis. Motion: count-up, settle-in, gentle pulse; off under `prefers-reduced-motion`.
- Empty states: one line + one action.
- Verification matrix: student account at narrow (390), mid (900), wide (1440), and side-panel-docked widths; keyboard-only pass; reduced motion; dark class (`html.dark`).

### 2. Practice launcher (Joshua's "specific question / dropdown" idea)
One panel, three tabs, all through the existing launch codec (`src/lib/drillLaunch.ts`):
- **Question**: PrepTest → Section → Question dropdowns plus free text (exists). Contextual action changes with depth: PT+Section selected → "Start section"; +Question → "Open question". LR/RC routing stays the finder's.
- **Section**: bank-aware dispatch: an LR section launches `kind: 'section'` (LR bank, `Drill.tsx:540`); an RC section does NOT reuse the finder's single-passage link (`passage=<id>` opens one passage with `DEFAULT_CONFIG`, `RcPlayer.tsx:130`). New RC section launch: resolve every passage of that PT section in order, create an RC session with those passage ids and the chosen timer config (the player already accepts multiple ids and explicit config, `RcPlayer.tsx:141`), then navigate by session id. PrepTest + Section, annotated with freshness ("24 of 25 unanswered", `sectionFreshness.ts:46`), fresh-only toggle, and the student's timer setting (standard / 52.5 / 70 / custom / untimed) carried into `kind: 'section'` `timerMode`. RC freshness shown as unknown until RC history is connected.
- **By type**: question-type multi-select + count + optional difficulty → `kind: 'filter'` (`drillLaunch.ts:163`). Adaptive Smart Drill is never repurposed for this. "Fresh only" needs an exposure-aware path: add an optional `excludeAnswered?: boolean` to the filter body (additive, old links unaffected), resolved when the queue is built (`drillRunSpec.ts:146`) against the student's answered qids; the built queue is stored in the Run Record so resume replays the same questions. If fewer fresh questions exist than `count`, say "Only N new Flaw questions left" before start, with an option to include answered ones.
- Shelves (search-matched in the same panel): Flagged (`flaggedService.ts`) and Needs review (journal review status). Decided: yes (Joshua, 2026-09-23).

### 3. Insight engine (fixed rules, no AI text)
Pure `pickInsights(signals, pin?)` in `src/components/classroom/home/insights.ts`, fixture-tested. Adapters feed it, one per source; the engine never reads Supabase.

Source-to-lens matrix:
| Lens | Source / reader | Coverage label |
|---|---|---|
| LR question types | NEW additive RPC `home_lr_type_accuracy(p_class_id, p_days int default 30)`: latest attempt per distinct question in window, excluding review/blind-review replays; returns qtype, questions, correct, last_attempt_at. Companion RPC `home_lr_type_evidence(p_class_id, p_qtype, p_days)` shares the SAME selection function, returning the qids behind the number | "LR practice, last 30 days" |
| Sections | Home adapter over `section_history`, NOT the unchanged `sectionHistory.ts` reader (it zero-fills missing `initial_total`/`initial_percent`/`total_time_ms` and stamps missing dates as now, `sectionHistory.ts:113`). Adapter derives totals from `total_questions`/`initial_score`, leaves unknown dates unknown (excluded from recency), never infers timing | "Sections" ("Timed" only when `mode` proves it) |
| Section diagnosis | saved `analysis_json` via `sectionAnalysis.ts` categories (reading / fundamentals / process / test-taking); Home summarizes the top existing finding and links to its report | "From your last section" |
| RC | `src/features/rc/api/rcProgress.ts` | "Reading Comprehension" |
| Bootcamp | per-topic progress stores (e.g. `topics/*/lib/supabase-progress.ts`) | "Bootcamp: <name>" |
| Assigned work | `useAssignedTodoFeed` status only: done / due / overdue counts. No scores inferred from copy | "Work Joshua assigned" |
| Repeat mistakes | `wrong_answer_journal` by qtype; trap wording from `wajNotesService` notes where present | "Wrong Answer Journal" |
| Pace / confidence | `attempts.time_ms`, `attempts.confidence` (LR only) | "LR practice" |

Selection rules:
- Each lens returns `null` (ineligible) or `{ score 0..1, evidence }`. Eligibility floors per lens (e.g. qtype: ≥8 distinct questions; sections: ≥1 completed in 21 days; RC: ≥2 passages in 21 days).
- Score = 0.5 × recency (days since last activity in that source, decays over 14 days) + 0.5 × actionability (size of the gap the lens found, normalized per lens). Volume never compared across units.
- Ties broken by a fixed lens order. Redundancy: at most one card per source; a section cannot feed both Sections and Section diagnosis unless the diagnosis names something the score card does not.
- 0 eligible → a single "Start here" card (Smart Drill). 1–3 eligible → show only those.
- Pinned lens becomes main if eligible; if ineligible, show it as main with its empty state + the engine's picks as minors, and flag it in Joshua's Hub as "pinned view has no data".
- Every insight has: coverage label, sample size, date range, an **evidence drawer**, and actions. Evidence is source-specific: question addresses for LR types (evidence RPC) and sections (`questions_json`); module list for bootcamp; the assignment rows for assigned work; passage list for RC.
- From a section diagnosis, "Practice this exact skill": when the finding's type/feature ids match launch filters (`sectionAnalysis.ts:160` to `kind: 'filter'` `qtypes`/`qfeatures`), prefill and show the filters before launch. For a weak LR type: "Try new ones" (`kind: 'filter'`, fresh only) and, when journal entries exist, "Review these" (journal). Pairing decided: yes (Joshua, 2026-09-23).

### 4. Pinning
Additive table `home_insight_pins`: `class_id text primary key references profiles(class_id)`, `lens text not null check (lens in (<enum>))`, `params jsonb not null default '{}'`, `pinned_by uuid not null default auth.uid()`, `updated_at timestamptz default now()`.
RLS: admin SELECT/INSERT/UPDATE/DELETE (via existing admin role check); student SELECT where `class_id` = their own profile's class_id. Params validated per lens in the client and by a CHECK on known keys. Unpin = delete row. Hub control on the student's page. RLS tests: student cannot read another student's pin or write their own.

### 5. Unified inbox
- New, separately named hook `useHomeFeed()` (existing `useInbox` untouched), on TanStack Query keys shared by Home panel and bell.
- **Event identity**: additive nullable `event_key text` on BOTH `notifications` and individual `messages`, plus `origin text check in ('human','system')` on individual messages (not threads). Generated writers (`classroomNotify.ts:87`, `sessionBundleNotify.ts:48`, new writers) compute one deterministic key per event (e.g. `assignment:<id>:assigned`) and insert both rows with it; partial unique indexes `(recipient, event_key) where event_key is not null` on each table make retries no-ops. Human-typed messages get `origin='human'`, no key.
- **Protection**: extend the notifications immutability trigger (`20260506124235_...sql:120`) to cover `event_key`/`origin`, and the same on messages; tests prove a student cannot change either.
- **One canonical visible-event model**, computed server-side in one RPC `home_feed(p_limit, p_before)`: an event with a key appears once (message wins, notification suppressed); legacy rows without keys use the 5-minute same-link heuristic inside the same RPC. The badge count comes from the same RPC, so counts never include hidden rows.
- **Read**: two separate read states, never mixed. (a) Conversation read = the existing participant `last_read_at` watermark (`useInbox.ts:247`), advanced ONLY when the student opens the conversation itself. (b) Generated events = a new additive `event_acks (user_id, event_key, acked_at)` table; opening an assignment/recap/grade/reminder event acks its key, which hides its notification duplicate and marks the generated message as read for the feed, without moving the conversation watermark. A generated message with no notification twin is acked the same way. Unread for a thread row = unread human messages after the watermark; generated messages count as unread until acked. Mark-all-read acks visible events and advances watermarks only for threads shown. RLS: student reads/writes own acks only.
- **Thread rows**: preview is Joshua's latest unread human message when one exists, else the latest message; unread = any unread human message from Joshua in the thread, not only the latest (the latest-only check in `useInbox.ts:189` is not reused).
- Hidden types (`streak`, `signup`) filtered in SQL before paging; page size 30 with load more.
- New notification types need the DB CHECK constraint extended (additive). Writers:
  | Event | Writer | Status |
  |---|---|---|
  | New assignment | `classroomNotify.ts` | exists, add key/origin |
  | Notes / recaps | `sessionBundleNotify.ts` | exists, add key/origin |
  | Graded work | grading completion (`activity_section_grades` flow) | new |
  | Session reminder | none today (type defined, no producer, verified). New scheduled job: 24h and 1h before `start_at`; key `session:<booking_id>:<offset>`; skipped when cancelled or moved, re-keyed on reschedule | new; needs a scheduler (Edge Function cron via Lovable, confirm with Joshua) |
  | Booking change | booking Edge Function | new, Lovable deploy |

### 6. Build order (each its own PR, each passes the preservation checklist)
1. Layout + restyle, existing data only; launcher tabs Question + Section; actions; inbox panel showing today's message preview; Next seven days untouched.
2. Insight engine: LR types (new RPC), Sections, Section diagnosis; evidence drawer.
3. Unified feed + bell + dedup columns + notification query fixes.
4. RC, bootcamp, assigned, mistakes, pace/confidence lenses; By-type launcher tab; pinning.
5. New notification writers: graded work; session reminders (scheduled job); booking changes. Reminders and booking need Lovable Edge Function deploys, confirmed with Joshua first.
6. Teacher view adopts the design.

## Key decisions & tradeoffs
- Rules, not AI text: predictable, never states a false thing.
- Source adapters + coverage labels instead of one "all practice" number: honest, more code.
- Separate `useHomeFeed` instead of rewriting `useInbox`: zero risk to current consumers, some duplication.
- Dedup via additive `event_key`/`origin` + a legacy heuristic, instead of back-filling old rows: no data changes.
- Container-query layout instead of viewport breakpoints.
- Next seven days frozen.

## Risks / open questions
- Performance: Home adds RPC + section history + feed. Plan: parallel queries, skeletons, no waterfall; measure first contentful paint before/after on a student account.
- Legacy dedup heuristic may miss or over-hide; accept for legacy only.
- Exact decay and floor values need tuning on real student data (fixtures from 3 anonymized students).
- Product decisions (Joshua, 2026-09-23: yes to all three): Flagged and Needs review shelves in the launcher, Needs review ordered by the student's reattempt_due_at with next_action shown; Review these next to Try new ones on weak-area insights; session reminders 24h and 1h before, via a scheduled job (Lovable deploy, confirm the route before deploying).

## Out of scope
- Public landing page. Goal score, streaks, latest PT, recent drills list, month calendar. AI insight text. Changes to how Smart Drill or assignments run.
