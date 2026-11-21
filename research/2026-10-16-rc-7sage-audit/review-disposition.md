# Review status and changes

Updated 2026-10-17. **Gemini Argon: COMPLETE.**

Independent hands-on visual UI/UX audit (via the dedicated Agent Browser on Port 9223) and full source inspection (`C:\Users\Joshu\dev\ai-os-projects\lsatu-rc-create`) were completed by Gemini Argon after fixing the Antigravity PreToolUse plugin hook blocker.

Scope clarification confirmed with Joshua during the live browser pass: **this audit and plan are strictly scoped to Reading Comprehension (RC) Practice & Drilling** (`/practice/drills?section=rc`, `/rc/search`, Global Question Finder, `/practice/exams` RC sections, the RC drill/section runners, and RC results/review). It has **nothing to do with the RC Bootcamp** (`/bootcamp/rc-engaging-with-the-passage`). Accordingly, `RC-13` and Packet `T08`'s bootcamp-cover changes are removed from the RC Practice plan.

---

## Part 1: Verification of Codex's Original Findings (`RC-01` through `RC-13`)

| Codex ID | Summary | Argon Verification | Disposition |
|---|---|---|---|
| `RC-01` (P1) | `/rc/search` opens a whole passage drill directly and drops the clicked question identity | **Confirmed in live browser & source** (`RcSearch.tsx:101, 291, 355`). Clicking `Open` on a question row starts a live ticking drill (`/rc/drill?passage=<id>`) at Question 1 with no preview step. | **Accept (P1)** -> `T03` |
| `RC-02` (P1) | Adaptive accuracy uses `everIncorrect` over the last 40 touched questions | **Confirmed & expanded** (`rcAdaptive.ts:71`). Plus two critical P1 data bugs in `getQuestionHistory()` (`A1`, `A2`, `A3` below) and zero UI visibility into what level "Adaptive" is targeting. | **Accept & Expand (P1)** -> `T01` / `T07` |
| `RC-03` (P1) | Full-content preview exposes fresh/reserved material; `/rc/search` defaults to PT 101-159 | **Confirmed in live browser** (`RcHubSurface.tsx` preview drawer and `/rc/search` PT range `101-159` vs builder `101-148`). | **Accept (P1)** -> `T01` / `T03` |
| `RC-04` (P1) | `RcResults.tsx` prints the full answer key (`EVERY QUESTION` table) right above `Review all`, spoiling blind review | **Confirmed in live browser** (`/rc/results/34ff285e-ab7c-4217-88d0-b5c2366a92cf`). Both chosen and credited letters (`A / B`, `A / C`) are visible above `Review all`. | **Accept (P1)** -> `T06` |
| `RC-05` (P2) | `Saved sets` tab on RC Drills is an LR-only dead end | **Confirmed in live browser** (`AcademyMainhub.tsx:408-413`). Shows "Saved LR sets" even when `Reading Comprehension` is selected. | **Accept (P2)** -> `T04` |
| `RC-06` (P2) | Search grammar, pool counts (`249` vs `1` match), and 200-row caps conflict across 3 surfaces | **Confirmed in live browser & source** (`RcHubSurface.tsx:583, 811`, `rcSearch.ts:159`). | **Accept (P2)** -> `T03` |
| `RC-07` (P2) | Normal drill launch displays previous-start recovery copy and internal passage IDs | **Confirmed in source** (`RcHubSurface.tsx:519, 674`). | **Accept (P2)** -> `T02` |
| `RC-08` (P2) | RC section start bounces through the drill builder before preflight, hides Status filter, and contradicts clock-start copy | **Confirmed & root-caused in source** (`SectionSelector.tsx:238, 359`, `rcSections.ts:131-150`, `RcHubSurface.tsx:497-509`). See `A4` below for exact file mapping. | **Accept & Expand (P1/P2)** -> `T02` / `T05` |
| `RC-09` (P2) | Protected standalone RC section runner lacks RC reader tools | **Confirmed & upgraded to P1** (`TimedStandaloneSectionRunner.tsx:154-160`). Standalone sections render LR's single-stimulus `OfficialQuestionPane` instead of `RcExamPane`. See `A4` below. | **Upgrade to P1** -> `T05` |
| `RC-10` (P2) | Question progress and ARIA labels say `Drill 1 of N` instead of `Question 1 of N` | **Confirmed in live browser & source** (`RcPlayer.tsx:1183`, `RcChrome.tsx:130`). | **Accept (P2)** -> `T02` |
| `RC-11` (P2) | Stacked panes at medium widths and comparative passage cross-referencing friction | **Confirmed & expanded in live browser** (`/rc/drill?passage=168`). See `A9` below for comparative passage A/B switcher design. | **Accept & Expand (P2)** -> `T05` |
| `RC-12` (P2) | Manual passage picker dumps all 248 passages (4,051 DOM nodes) with no pagination/sort/history facets | **Confirmed in live browser** (`RcHubSurface.tsx`). | **Accept (P2)** -> `T03` |
| `RC-13` | Bootcamp cover (`/bootcamp/rc-engaging-with-the-passage`) orientation | **Rejected / Out of Scope**. Joshua explicitly confirmed this audit is strictly for RC Drilling/Practice, not the RC Bootcamp. | **Remove from RC Drilling Plan** |

---

## Part 2: New Material Findings Discovered by Gemini Argon (Missed or Underspecified by Codex)

### A1 (P1 - Analytics & Adaptive Integrity): "Exclude from analytics" on `RcResults` Is Ignored by `getQuestionHistory()`
- **Evidence**: [`src/features/rc/api/rcProgress.ts:377-411`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/features/rc/api/rcProgress.ts#L377-L411) vs. [`src/features/rc/pages/RcResults.tsx:177-187`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/features/rc/pages/RcResults.tsx#L177-L187).
- **What Codex Missed**: Codex noted that `RcResults` has an "Exclude from analytics" toggle (`E27`), but never checked whether excluding a session actually excludes its attempts. `getQuestionHistory()` queries `rc_attempts` directly by `user_id` without joining `rc_sessions` or filtering out rows whose session has `excluded_from_analytics = true`.
- **Impact**: Toggling "Exclude from analytics" on a spoiled or diagnostic RC session has zero effect on the RC Drill Builder's `Fresh` / `Incorrect before` / `Incorrect on last try` status filters or on `rollingAccuracy()` adaptive difficulty.
- **Disposition**: **Accept (P1)**. Include in **Packet T01 / T07**: filter `getQuestionHistory()` against non-excluded sessions (or join `rc_sessions!inner(excluded_from_analytics)` where `excluded_from_analytics = false`).

### A2 (P1 - Adaptive & Status Corruption): Skipped/Unanswered Questions Are Counted as 100% Correct in `getQuestionHistory()`, `rollingAccuracy()`, and `passageStatus()`
- **Evidence**: [`src/features/rc/pages/RcPlayer.tsx:650`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/features/rc/pages/RcPlayer.tsx#L650), [`src/features/rc/api/rcProgress.ts:399-407`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/features/rc/api/rcProgress.ts#L399-L407), [`src/features/rc/lib/rcAdaptive.ts:71-82`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/features/rc/lib/rcAdaptive.ts#L71-L82), and [`src/features/rc/components/RcHubSurface.tsx:937-949`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/features/rc/components/RcHubSurface.tsx#L937-L949).
- **What Codex Missed**: When a drill is completed with unanswered questions, `RcPlayer.tsx` records each unanswered question with `selected: null, isCorrect: null`. In `getQuestionHistory()`, `const wrong = row.is_correct === false;` evaluates to `false` when `is_correct` is `null`.
- **Impact**:
  1. `rollingAccuracy()` (`rcAdaptive.ts:77`) counts `!e.everIncorrect` as a correct answer. Every skipped question is treated as answered **correctly**, inflating rolling accuracy and pushing adaptive target difficulty up to Level 4.
  2. `passageStatus()` (`RcHubSurface.tsx:945`) labels a passage where the learner skipped every question as `"Completed"` with 0 errors, and excludes it from `Fresh`, `Incorrect before`, and `Incorrect on last try`.
- **Disposition**: **Accept (P1)**. Include in **Packet T01 / T07**: track `answeredAttempts`, `unansweredOnLastTake`, and `everCorrect` explicitly in `RcQuestionHistoryEntry`; exclude unanswered items from the numerator of `rollingAccuracy` (or treat timed-out/skipped per explicit policy) and surface `"Incomplete / Skipped"` distinctly from `"Completed"`.

### A3 (P1 - Silent History Truncation): `getQuestionHistory()` Hits Supabase's Default 1,000-Row Limit Without Pagination
- **Evidence**: [`src/features/rc/api/rcProgress.ts:379-384`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/features/rc/api/rcProgress.ts#L379-L384).
- **What Codex Missed**: `getQuestionHistory()` selects from `rc_attempts` ordered by `created_at ASC` with no `.range()` or pagination loop. PostgREST caps unpaginated responses at 1,000 rows (~37 RC sections or ~140 passages including reattempts).
- **Impact**: Once a student records more than 1,000 attempt rows, all newest attempts are silently truncated from the response. Recently completed passages revert to `Fresh` in the builder, and `rollingAccuracy()` freezes on stale early attempts.
- **Disposition**: **Accept (P1)**. Include in **Packet T01**: paginate `getQuestionHistory()` in 1,000-row pages (matching `fetchAnsweredQids` in `src/lib/sectionFreshness.ts`) or compute per-question rollup via an indexed query/RPC.

### A4 (P1 - Standalone RC Section Runner & Launch Architecture): Exact Code Root Cause for `E22-E24` and `RC-08/RC-09`
- **Evidence**:
  1. [`src/components/timed/TimedStandaloneSectionRunner.tsx:154-160`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/components/timed/TimedStandaloneSectionRunner.tsx#L154-L160) vs. [`src/components/testing/TimedOfficialChildRunner.tsx:211-221`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/components/testing/TimedOfficialChildRunner.tsx#L211-L221).
  2. [`src/lib/timedSectionController.ts:67-70`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/lib/timedSectionController.ts#L67-L70).
  3. [`src/components/drill/SectionSelector.tsx:236-240, 359, 489-501`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/components/drill/SectionSelector.tsx#L236-L240), [`src/features/rc/lib/rcSections.ts:131-150`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/features/rc/lib/rcSections.ts#L131-L150), and [`src/features/rc/components/RcHubSurface.tsx:497-509`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/features/rc/components/RcHubSurface.tsx#L497-L509).
- **What Codex Missed**: Codex stated in `PLAN.md:108` that `source-inventory.md` did not establish the owning filenames for `/testing` and section launch. Argon traced the entire chain:
  - **Why standalone RC sections lack RC reader tools (`E24`)**: Full practice tests (`TimedOfficialChildRunner.tsx`) already render `RcExamPane` + `RcPassagePane` + `RcQuestionPane` for RC legs. However, standalone timed sections (`TimedStandaloneSectionRunner.tsx:154-160`) hardcode LR's `OfficialQuestionPane` for both LR and RC, passing `stimulus: item.passage.text`, `highlights={[]}`, `highlightMode="none"`, `searchTerm=""`, `fontScale={1}`, and `onTextSelection={() => false}`!
  - **Why starting an RC section flashes the RC Drill Builder (`E23`)**: `SectionSelector.tsx:238` calls `rcSectionHref()`, which builds `/rc?passages=...&start=1&timedSection=manual-canonical`. That URL mounts `RcHubSurface.tsx`, which renders the populated 4-passage drill builder while a `useEffect` (`RcHubSurface.tsx:497-509`) redirects to `newManualSectionHref(...)` (`/testing/sections/:uuid?kind=rc&pt=...`). `SectionSelector.tsx` should navigate directly to `newManualSectionHref()` without bouncing through `/rc`.
  - **Why the `Status` (`Fresh`) filter disappears on RC sections (`E22`)**: `SectionSelector.tsx:359` wraps the Status filter in `{kind === 'lr' && (...)}` with a stale comment claiming `"Only the LR runner writes attempts, so this is LR-only"`. In reality, RC attempts are stored in `rc_attempts` (`getQuestionHistory()`), so RC section freshness can and should be computed from `rc_attempts`.
- **Disposition**: **Accept (P1)**. Update `PLAN.md` `Likely code impact`, **Packet T02** (direct `newManualSectionHref` launch + RC section freshness in `SectionSelector.tsx`), and **Packet T05** (mount `RcExamPane` / `RcPassagePane` / `RcQuestionPane` and `OfficialDrillToolbar` inside `TimedStandaloneSectionRunner.tsx`).

### A5 (P1 - Global Question Finder Broken Dropdowns & Premature Live Drill Launch):
- **Evidence**: Live Agent Browser inspection (`steps/164/media_0.jpg`, `steps/201/media_0.jpg`), [`src/components/questionfinder/QuestionJump.tsx`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/components/questionfinder/QuestionJump.tsx), and [`src/components/questionfinder/QuestionFinder.tsx`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/components/questionfinder/QuestionFinder.tsx).
- **What Codex Missed**:
  1. In the live `Open a question (Ctrl+K)` modal on `/practice/drills?section=rc`, the `TEST` dropdown is permanently disabled on `Loading…`, keeping `SECTION`, `Question`, and `Open question` disabled unless the user types a text query into the input box. (Codex only typed `PT101 S4 Q1` into the text input in `E25` and never clicked the `TEST` dropdown).
  2. Clicking any of the passage pills/cards inside the live Question Finder (or clicking `Open` in `/rc/search`) immediately creates and starts a **live ticking drill** (`/rc/drill?passage=<id>` with `Time Elapsed: 00:01`) rather than opening the safe read-only preview (`/rc/preview`).
- **Disposition**: **Accept (P1)**. Include in **Packet T03**: fix the `QuestionJump` / `QuestionFinder` address index loading state on deployed/live routes and ensure all passage/question discovery clicks route to read-only `/rc/preview` before creating a sitting.

### A6 (P2 - Anonymous RC History Cards & Missing Discard Action):
- **Evidence**: Live Agent Browser (`steps/112/media_0.jpg`, `steps/117/media_0.jpg`) and [`src/lib/standaloneDrillHistory.ts:50-67`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/lib/standaloneDrillHistory.ts#L50-L67).
- **What Codex Missed**: `standaloneDrillHistory.ts:57` hardcodes every RC history row title to `` `RC drill · ${session.passageIds.length} passage(s)` `` with detail `"7 first answers saved · 8/27/2026"`.
  - Neither `In progress` nor `Completed` cards show **which PrepTest, Section, Passage number, Passage Title (e.g., `PT 139 · S3 · P1 · Improving Farm Economics`), Topic, or Score (`2/7 · 29%`)** the drill was!
  - Furthermore, `In progress` RC drills have no `Discard` / `Delete` button (unlike `/practice/exams`, which lets learners discard accidental/abandoned sittings).
- **Disposition**: **Accept (P2)**. Include in **Packet T04 / T06**: enrich `buildStandaloneDrillHistory()` with passage titles/addresses from the cached RC index and first-attempt score for completed sittings, and add a safe `Discard` action for in-progress sittings.

### A7 (P2 - Passage Text Hygiene, Comparative Markdown Headers & "Find in Passage" Zero-Match Feedback):
- **Evidence**:
  1. `public/data/rc/RC-PT119.json`, `RC-PT140.json`, `RC-PT148.json` (contain `\u00ad` soft hyphens inside words).
  2. `public/data/rc/RC-PT125.json` (`summaries.standard` uses `****Passage A****` 4-asterisk markdown).
  3. [`src/features/rc/components/RcPassagePane.tsx:103`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/features/rc/components/RcPassagePane.tsx#L103) and [`src/features/rc/pages/RcPlayer.tsx:1255`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/features/rc/pages/RcPlayer.tsx#L1255).
- **What Codex Missed**:
  - Soft hyphens (`\u00ad`) in the passage JSON break substring matching in `findMatches()` and `/rc/search`.
  - Four-asterisk `****Passage A****` in comparative summaries renders literal `*` characters in `RcMarkdown`.
  - When a student types a query in `Find Text` that has 0 matches in the passage (or 1 character), `RcPlayer.tsx:1255` (`findCount > 0 && ...`) hides the match counter completely instead of displaying `0/0` (`No matches`), leaving the student with zero feedback on whether search ran.
- **Disposition**: **Accept (P2)**. Include in **Packet T03 / T05**: strip `\u00ad` soft hyphens and normalize `****` markdown in bank/loader, and display `0/0` when `findQuery.trim().length >= 2 && findCount === 0`.

### A8 (P2 - Hidden Accessibility & Reading Focus Tools + Disconnected Question-Type Filters):
- **Evidence**: Live Agent Browser (`steps/212/media_0.jpg`, `steps/26/media_0.png`, `steps/44/media_0.png`) and [`src/features/rc/pages/RcPlayer.tsx:1213-1251`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/features/rc/pages/RcPlayer.tsx#L1213-L1251).
- **What Codex Missed**:
  1. **Hidden Reader Strengths**: Codex wrote in `AUDIT.md` (`E08` vs `E19`) that 7Sage had color schemes while LSAT U only had "text size/spacing". In reality, LSAT U's `Aa` popover (`RcPlayer.tsx:1213-1251`) **already implements `Paragraph focus` (hover paragraph highlighting) and 6 accessibility color schemes** (`Black on white`, `Grey on light grey`, `Purple on light green`, `Black on violet`, `Yellow on navy`, `White on black`), alongside `Line spacing` on a separate adjacent icon. Because the trigger is only labelled `Text size`, even Codex missed that these features exist!
  2. **One-Way Street to `/rc/search`**: Question-level filters (`Question Family`, `Question Type`, `Question Feature`, `Question Difficulty`) exist on `/rc/search`, not in the RC Drill Builder (`RcHubSurface.tsx`), and there is **no link from `/practice/drills?section=rc` to `/rc/search`** (only a `Back to drills` button on `/rc/search`).
- **Disposition**: **Accept (P2)**. Include in **Packet T03** (unify or link question-level filtering directly from the RC Drill Builder) and **Packet T05** (consolidate `Aa` + `Line spacing` into a discoverable `Display` toolbar control and surface `Paragraph focus`).

### A9 (P2 - Comparative Passage Ergonomics, Review Summary Placement & Results Source Identity):
- **Evidence**: Live Agent Browser (`steps/201/media_0.jpg`, `steps/151/media_0.jpg`, `steps/129/media_0.jpg`) and [`src/features/rc/pages/RcResults.tsx`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/features/rc/pages/RcResults.tsx).
- **What Codex Missed**:
  1. **Comparative Passages (`Passage A` / `Passage B`)**: Render as one long stacked scroll column without sticky headers or an `[A | B | Both]` switcher, forcing constant vertical scrolling when answering comparative relationship questions.
  2. **`Show passage summary` Placement in Review**: Expanding LSAT U's excellent structured Passage Summary (`Topic`, `Framework`, `Main Point`, `P1-P4` map) inside `RcReviewLayer` renders it above the question stem in the right-hand pane, pushing the question and choices A-E completely off-screen (`More below`). Putting the Passage Summary in a tab/drawer on the left passage pane keeps the question and choices visible while reviewing the passage map.
  3. **Missing Source Address on `RcResults` & Unprotected `drillMisses`**: On `RcResults.tsx`, the `BY PASSAGE` cards show the passage title (`"Improving Farm Economics"`) and topic/framework badges, but **omit `PrepTest 139 · Section 3 · Passage 1`**. In addition, `drillMisses()` (`RcResults.tsx:209-212`) calls `createSession` with no `busy` state or `try/catch`, so double-clicking creates duplicate sessions.
- **Disposition**: **Accept (P2)**. Include in **Packet T05** (comparative passage `[Both | Passage A | Passage B]` sticky header/switcher) and **Packet T06** (left-pane or side-by-side Passage Summary in Review, official `PT · S · P` badge on `RcResults` passage cards, and idempotent `busy`/`try-catch` guard on `drillMisses`).

---

## Final Review Status

- **Independent Evidence & Visual Audit**: Complete (`review-disposition.md`, `AUDIT.md`, `source-inventory.md`, and `PLAN.md` updated and reconciled).
- **Plan Review Verdict**: **APPROVED WITH ACCEPTED REVISIONS (`A1`-`A9` integrated; unrelated RC Bootcamp `RC-13` removed).**
- **Next Gate**: Ready for Joshua's green light to execute the implementation packets (`T01` through `T10`, excluding out-of-scope bootcamp changes) in `C:\Users\Joshu\dev\ai-os-projects\lsatu-rc-create`.
