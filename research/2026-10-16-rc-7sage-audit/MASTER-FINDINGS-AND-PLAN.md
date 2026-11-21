# Master RC Practice & Drilling Audit: Combined Codex + Gemini Argon Findings & Execution Plan

**Date**: 2026-10-17
**Owner**: Joshua (Product, Pedagogy & Voice Authority)
**Contributors**:
1. **Codex**: Initial live browser observation (`E01`–`E30`), source inventory, and draft execution plan (`RC-01`–`RC-12`).
2. **Gemini Argon (Antigravity)**: Independent hands-on visual UI/UX audit in the dedicated Agent Browser (`Port 9223`) across LSAT U and 7Sage, plus full source code audit (`A1`–`A9`) in `C:\Users\Joshu\dev\ai-os-projects\lsatu-rc-create`.
**Next Reviewer**: Claude Code (Independent Architectural, UX & Plan Review before implementation).

---

## 1. Strict Scope & Non-Goals

- **In Scope**: LSAT U **Reading Comprehension (RC) Practice & Drilling** end-to-end:
  - Practice Hub (`/practice/drills?section=rc` — `Create`, `In progress`, `Completed`, `Saved sets`)
  - Automatic (`Choose for me`) & Manual (`Choose passages`) Drill Builder (`src/features/rc/components/RcHubSurface.tsx`)
  - Question & Passage Discovery (`/rc/search`, `/rc/preview`, and Global Question Finder `Ctrl+K` / `/`)
  - Section Launcher (`/practice/exams` -> `Take a section` -> `Reading Comprehension`, `src/components/drill/SectionSelector.tsx`)
  - Live RC Drill Player (`src/features/rc/pages/RcPlayer.tsx`) & Standalone Timed RC Section Runner (`src/components/timed/TimedStandaloneSectionRunner.tsx`)
  - Post-Drill Results (`src/features/rc/pages/RcResults.tsx`), Blind Review & Explanations (`src/features/rc/components/RcReviewLayer.tsx`)
  - History, Adaptive Selection & Persistence (`src/features/rc/api/rcProgress.ts`, `src/features/rc/lib/rcAdaptive.ts`, `src/lib/standaloneDrillHistory.ts`)
  - Shared LR/RC contracts where RC depends on shared primitives (`src/lib/drillLaunch.ts`, `src/components/drill/official/OfficialDrillToolbar.tsx`)
- **Explicitly Out of Scope**:
  - **RC Bootcamp (`/bootcamp/rc-engaging-with-the-passage`)**: Confirmed by Joshua as completely separate from RC Drilling. (Codex's earlier `RC-13` bootcamp cover note has been removed).
  - **RC Recall / Reading Center Training (`/reading-center/rc-recall`)**: Separate parallel workstream in `lsatu-reading-center-rc-recall`. Coordinate shared links only; do not overwrite its build spec.

---

## 2. Executive Summary: Where LSAT U Stands vs. 7Sage

### What LSAT U Already Does Better Than 7Sage (Preserve & Elevate)
1. **Passage-First Builder with Honest Defaults**: Clear separation of `Choose for me` vs. `Choose passages`, explicit reveal choices (`After each passage`, `At the end`, `After each question`), readable framework/topic filters (no cryptic tag abbreviations like 7Sage), and automatic protection of newest PrepTests (`PT 149-159` held back by default in the builder).
2. **Punctuation-Tolerant Title Search in the Builder**: Searching `P.D. James` in LSAT U's manual builder finds `PT101 S4 P1` immediately, whereas 7Sage's manual search returns `0` matches for `P.D. James` (`E05` vs `E16`).
3. **Pedagogically Superior Written Passage Summaries**: LSAT U's structured `Passage summary` in Review (`Topic`, `Framework`, `Main Point` with quoted Most Valuable Sentence, and paragraph-by-paragraph `P1–P4` breakdowns) is much faster and clearer to study from than 7Sage's video-only explanations.
4. **Built-in Accessibility Color Schemes & Paragraph Focus**: Source and live inspection revealed that LSAT U's player **already has** `Paragraph focus` (hover paragraph highlighting) and 6 accessibility color themes (`Black on white`, `Grey on light grey`, `Purple on light green`, `Black on violet`, `Yellow on navy`, `White on black`) inside `RcPlayer.tsx:1213-1251` — they are just hidden behind an unlabelled `Aa` (`Text size`) icon.

### Where 7Sage Currently Beats LSAT U (And Why LSAT U Feels Fragmented)
1. **Broken History & Adaptive Signals (`A1`, `A2`, `A3`, `RC-02`)**: LSAT U's RC history query (`getQuestionHistory`) ignores excluded sessions, treats skipped questions as 100% correct, silently truncates after 1,000 rows, and uses permanent `everIncorrect` sticky flags.
2. **Accidental Live-Drill Launches & Broken Finder Dropdowns (`RC-01`, `A5`)**: Clicking a passage or question in `/rc/search` or the Global Finder (`Ctrl+K`) immediately starts a live ticking drill instead of opening a read-only preview, and the `TEST` dropdown in `Ctrl+K` is stuck on `Loading…`.
3. **Standalone Timed RC Sections Use the Wrong Player (`RC-08`, `RC-09`, `A4`)**: Starting a standalone RC section on `/practice/exams` hides the `Fresh` status filter, flashes the 4-passage drill builder during redirect, and mounts LR's single-stimulus `OfficialQuestionPane` with no RC toolbar, no highlights, no search, and no comparative layout.
4. **Spoiled Blind Review (`RC-04`)**: `RcResults.tsx` prints both the student's answer and the credited answer key for every question right above the `Review all` button, spoiling the hidden-answer blind review flow (`"Pick again, then see both"`).
5. **Missing Reusable RC Sets & Anonymous History Cards (`RC-05`, `A6`)**: Clicking `Saved sets` in RC shows `"Saved LR sets"`, and `In progress` / `Completed` cards all say `"RC drill · 1 passage"` with no PrepTest, Section, Passage Title, Score, or `Discard` button.

---

## 3. Complete Master Ledger of All 21 Findings (Codex `RC-01`..`RC-12` + Argon `A1`..`A9`)

### Tier 1: P1 Critical Bugs (Data Integrity, Wrong Player, Premature Launch & Spoilers)

#### 1. `[A1]` (P1 — Found by Argon): "Exclude from analytics" on `RcResults` is completely ignored by `getQuestionHistory()`
- **Exact Code**: [`src/features/rc/api/rcProgress.ts:377-411`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/features/rc/api/rcProgress.ts#L377-L411) vs. [`src/features/rc/pages/RcResults.tsx:177-187`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/features/rc/pages/RcResults.tsx#L177-L187).
- **Evidence**: Toggling `Exclude from analytics` on `RcResults` updates `rc_sessions.excluded_from_analytics = true`. However, `getQuestionHistory()` queries `rc_attempts` directly by `user_id` without joining `rc_sessions` or filtering out excluded sessions.
- **Impact**: Excluded sessions still count toward `Fresh` / `Incorrect before` / `Incorrect on last try` filters in the RC Drill Builder and still feed `rollingAccuracy()` adaptive difficulty.
- **Required Fix (`T01`)**: Filter `getQuestionHistory()` so attempts belonging to sessions with `excluded_from_analytics = true` are excluded.

#### 2. `[A2]` (P1 — Found by Argon): Skipped/Unanswered RC questions are counted as 100% Correct in `rollingAccuracy()` and mark passages `"Completed"`
- **Exact Code**: [`src/features/rc/pages/RcPlayer.tsx:650`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/features/rc/pages/RcPlayer.tsx#L650), [`src/features/rc/api/rcProgress.ts:399-407`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/features/rc/api/rcProgress.ts#L399-L407), [`src/features/rc/lib/rcAdaptive.ts:71-82`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/features/rc/lib/rcAdaptive.ts#L71-L82), [`src/features/rc/components/RcHubSurface.tsx:937-949`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/features/rc/components/RcHubSurface.tsx#L937-L949).
- **Evidence**: When a learner submits an RC drill with unanswered questions, `RcPlayer.tsx:650` writes `selected: null, isCorrect: null` to `rc_attempts`. In `getQuestionHistory()` (`rcProgress.ts:399`), `const wrong = row.is_correct === false;` evaluates to `false` for `null`.
- **Impact**:
  1. `rollingAccuracy()` (`rcAdaptive.ts:77`) computes `correct = recent.filter((e) => !e.everIncorrect).length`. Every skipped question is counted as **answered correctly**, inflating rolling accuracy toward 100% and pushing adaptive passage difficulty to Level 4.
  2. `passageStatus()` (`RcHubSurface.tsx:945`) labels a passage where all questions were skipped as `"Completed"` with 0 missed, and excludes it from `Fresh`, `Incorrect before`, and `Incorrect on last try`.
- **Required Fix (`T01`, `T07`)**: Track `answeredAttempts`, `everCorrect`, and `unansweredOnLastTake` explicitly in `RcQuestionHistoryEntry`. Do not count unanswered rows as correct in `rollingAccuracy()`, and surface `"Incomplete / Skipped"` distinctly from `"Completed"` in `passageStatus()`.

#### 3. `[A3]` (P1 — Found by Argon): Silent 1,000-row truncation in `getQuestionHistory()`
- **Exact Code**: [`src/features/rc/api/rcProgress.ts:379-384`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/features/rc/api/rcProgress.ts#L379-L384).
- **Evidence**: `getQuestionHistory()` queries `rc_attempts` ordered by `created_at ASC` with no `.range()` or pagination loop. Supabase PostgREST caps unpaginated selects at 1,000 rows (~37 RC sections or ~140 passages including reattempts).
- **Impact**: Once a student exceeds 1,000 attempt rows, all newest attempts are silently truncated. Recently completed passages revert to `Fresh`, and `rollingAccuracy()` freezes on stale early attempts.
- **Required Fix (`T01`)**: Paginate `getQuestionHistory()` in 1,000-row pages (matching `fetchAnsweredQids` in `src/lib/sectionFreshness.ts`).

#### 4. `[RC-02]` (P1 — Found by Codex, Expanded by Argon): Adaptive `everIncorrect` never clears after mastery and hides target level
- **Exact Code**: [`src/features/rc/lib/rcAdaptive.ts:71-90`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/features/rc/lib/rcAdaptive.ts#L71-L90), [`src/features/rc/components/RcHubSurface.tsx`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/features/rc/components/RcHubSurface.tsx).
- **Evidence**: `rollingAccuracy()` checks `!e.everIncorrect` across the 40 most recently touched questions. If a student missed a question once and later got it right on a fresh retry, `everIncorrect` remains `true` forever, penalizing their rolling accuracy. Furthermore, the UI says `"Adaptive: fresh passages near your level"` without telling the student what difficulty level (1–5) is currently targeted or why.
- **Required Fix (`T07`)**: Separate first-attempt diagnostic accuracy from recent performance (`incorrectOnLastTake`) and review mastery, and display the active target difficulty badge and sample basis in the builder.

#### 5. `[A4 / RC-09]` (P1 — Observed by Codex `E24`, Root-Caused in Code by Argon): Standalone Timed RC Section Runner mounts LR's single-stimulus `OfficialQuestionPane` with no RC tools
- **Exact Code**: [`src/components/timed/TimedStandaloneSectionRunner.tsx:154-160`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/components/timed/TimedStandaloneSectionRunner.tsx#L154-L160) and [`src/lib/timedSectionController.ts:67-70`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/lib/timedSectionController.ts#L67-L70) vs. [`src/components/testing/TimedOfficialChildRunner.tsx:211-221`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/components/testing/TimedOfficialChildRunner.tsx#L211-L221).
- **Evidence**: Full practice tests (`TimedOfficialChildRunner.tsx`) properly mount `RcExamPane` + `RcPassagePane` + `RcQuestionPane` for RC sections. Standalone timed sections (`/testing/sections/:sittingId` in `TimedStandaloneSectionRunner.tsx`) flatten each RC passage into `question.stimulus` (`timedSectionController.ts:68`) and render LR's `OfficialQuestionPane` with hardcoded `highlights={[]}`, `highlightMode="none"`, `searchTerm=""`, `fontScale={1}`, and `onTextSelection={() => false}`.
- **Impact**: Students taking a standalone timed RC section have no split RC reader, no passage search, no highlighters/underline/eraser, no text-size/spacing controls, no `Passage only` view, and broken comparative passage formatting.
- **Required Fix (`T05`)**: Mount `RcExamPane`, `RcPassagePane`, `RcQuestionPane`, and policy-scoped `OfficialDrillToolbar` inside `TimedStandaloneSectionRunner.tsx` when `state.snapshot.sitting.kind === 'rc'`, matching `TimedOfficialChildRunner.tsx`.

#### 6. `[RC-01 / A5]` (P1 — Found by Codex & Expanded Live by Argon): Clicking a passage or question in `/rc/search` or Global Question Finder (`Ctrl+K`) immediately launches a live ticking drill, and the `Ctrl+K` `TEST` dropdown is stuck on `Loading…`
- **Exact Code**: [`src/features/rc/pages/RcSearch.tsx:101, 291, 355`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/features/rc/pages/RcSearch.tsx#L101), [`src/components/questionfinder/QuestionJump.tsx`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/components/questionfinder/QuestionJump.tsx), [`src/components/questionfinder/QuestionFinder.tsx`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/components/questionfinder/QuestionFinder.tsx), [`src/components/questionfinder/useFinderAddressIndex.ts`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/components/questionfinder/useFinderAddressIndex.ts).
- **Live Browser Evidence**:
  1. In `/rc/search`, clicking `Open` on a question row drops the clicked question ID and immediately creates and starts a full-passage drill (`/rc/drill?passage=<id>`).
  2. In the live `Open a question (Ctrl+K)` modal on `/practice/drills?section=rc` (`steps/164/media_0.jpg`), the `TEST` dropdown is permanently stuck on `Loading…` (disabled), cascading to keep `SECTION`, `Question`, and `Open question` disabled unless the user types a text address.
  3. Clicking any of the passage pills/cards inside the live Question Finder (`steps/201/media_0.jpg`) navigates directly to `/rc/drill?passage=<id>`, starting a ticking clock (`Time Elapsed: 00:01`) and creating an in-progress drill session with no `Discard` button.
- **Required Fix (`T03`)**: Fix the `QuestionFinder` / `QuestionJump` address index loading state, and route all discovery clicks in `/rc/search` and `Ctrl+K` to read-only `/rc/preview?passage=<id>&q=<questionId>` before creating any sitting.

#### 7. `[RC-03]` (P1 — Found by Codex `E17, E26` & Confirmed Live by Argon): Unprotected full-text preview & inconsistent reserved PrepTest range (`101-148` vs `101-159`)
- **Exact Code**: [`src/features/rc/components/RcHubSurface.tsx`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/features/rc/components/RcHubSurface.tsx), [`src/features/rc/lib/rcSearch.ts:38-39`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/features/rc/lib/rcSearch.ts#L38-L39).
- **Evidence**: Expanding `Preview drill` or opening `/rc/search` (which defaults to `PT 101-159` instead of the builder's `101-148` reserved-PT boundary) exposes full passage and question text without recording exposure, while `Status: Fresh` only checks answered attempts.
- **Required Fix (`T01`, `T03`)**: Default previews to spoiler-safe metadata first (`PT · S · P`, title, topic, format, difficulty, question count) with explicit text reveal, align `/rc/search` default PT range with the builder's reserved-test protection (or badge reserved PTs `149-159` clearly), and track full-text exposure separately from answered attempts.

#### 8. `[RC-04]` (P1 — Found by Codex `E27-E28` & Confirmed Live by Argon): `RcResults` prints the full answer key right above `Review all`, spoiling Blind Review
- **Exact Code**: [`src/features/rc/pages/RcResults.tsx:480-550`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/features/rc/pages/RcResults.tsx#L480-L550), [`src/features/rc/components/RcReviewLayer.tsx`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/features/rc/components/RcReviewLayer.tsx).
- **Live Browser Evidence**: On `/rc/results/34ff285e-ab7c-4217-88d0-b5c2366a92cf` (`steps/129/media_0.jpg`), the `EVERY QUESTION` table displays both the student's pick and the credited answer (`A / B`, `A / C`) right above `Review all`. When the student then clicks `Review all`, the player says `"Your answer is hidden. Pick again, then see both"` (`steps/134/media_0.jpg`) — after the student has already seen the answer key!
- **Required Fix (`T06`)**: Offer a review-first finish step (`Start blind review` vs `Reveal score & answers`) and conceal credited answers on `RcResults` until the learner explicitly reveals them or completes blind review.

---

### Tier 2: P2 High-Impact UX, Workflow & Reader Gaps

#### 9. `[A4 / RC-08]` (P2 — Observed by Codex `E22-E23`, Root-Caused by Argon): RC Section Launcher hides the `Status` (`Fresh`) filter, bounces through `/rc` drill builder, and contradicts clock-start copy
- **Exact Code**: [`src/components/drill/SectionSelector.tsx:236-240, 359, 520-528`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/components/drill/SectionSelector.tsx#L236-L240), [`src/features/rc/lib/rcSections.ts:131-150`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/features/rc/lib/rcSections.ts#L131-L150), [`src/features/rc/components/RcHubSurface.tsx:497-509`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/features/rc/components/RcHubSurface.tsx#L497-L509).
- **Evidence**:
  1. `SectionSelector.tsx:359` hides the `Status` (`Fresh · never attempted`) dropdown when `kind === 'rc'` because of an outdated comment claiming RC writes no attempts.
  2. `SectionSelector.tsx:238` navigates to `rcSectionHref()`, which opens `/rc?passages=...&start=1&timedSection=manual-canonical`, mounting `RcHubSurface` (flashing the 4-passage drill builder) before a `useEffect` (`RcHubSurface.tsx:497-509`) redirects to `newManualSectionHref()` (`/testing/sections/:uuid`).
  3. `SectionSelector.tsx:525` says `"The clock starts straight away"`, whereas the `/testing/sections/:uuid` preflight screen says `"The clock has not started"`.
- **Required Fix (`T02`)**: Wire RC section freshness in `SectionSelector.tsx` using `rc_attempts`, navigate directly to `newManualSectionHref()` from `SectionSelector.handleStart`, and align the start copy with the preflight screen.

#### 10. `[RC-05]` (P2 — Found by Codex `E21` & Confirmed Live by Argon): `Saved sets` tab on RC Drills is an LR-only dead end
- **Exact Code**: [`src/pages/AcademyMainhub.tsx:408-413`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/pages/AcademyMainhub.tsx#L408-L413).
- **Live Browser Evidence**: Clicking `Saved sets` while `Reading Comprehension` is active displays `"Saved LR sets — Reusable saved sets support Logical Reasoning"` (`steps/121/media_0.jpg`).
- **Required Fix (`T04`)**: Support both **Fixed RC Sets** (saved ordered passage IDs) and **RC Selection Recipes** (saved filter/count/timing/reveal templates) under `Saved sets` when `section === 'rc'`.

#### 11. `[A6]` (P2 — Found by Argon): `In progress` and `Completed` RC History cards are completely anonymous (`"RC drill · 1 passage"`) and lack a `Discard` action
- **Exact Code**: [`src/lib/standaloneDrillHistory.ts:50-67`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/lib/standaloneDrillHistory.ts#L50-L67), [`src/pages/AcademyMainhub.tsx:424-432`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/pages/AcademyMainhub.tsx#L424-L432).
- **Live Browser Evidence**: Every row in `In progress` (`steps/112/media_0.jpg`) and `Completed` (`steps/117/media_0.jpg`) says `"RC drill · 1 passage"` or `"RC drill · 4 passages"` with `"7 first answers saved · 8/27/2026"`.
  - None of the cards show the **PrepTest, Section, Passage #, Title (e.g., `PT 139 · S3 · P1 · Improving Farm Economics`), Topic, or Score (`2/7 · 29%`)**.
  - `In progress` cards only have a `Continue` button, with no `Discard` button to remove accidental or abandoned drills.
- **Required Fix (`T04`)**: Resolve passage metadata from `loadRcIndex()` in `buildStandaloneDrillHistory()` to display `PT · S · P · Title` (or passage summary for multi-passage sets) and first-attempt score on `Completed` cards, and add a `Discard` action for `In progress` RC sessions.

#### 12. `[A8]` (P2 — Found by Argon): Question-level filters (`Question Family`, `Question Type`, `Question Feature`) are hidden on `/rc/search` with zero link from the RC Drill Builder, and `Cancel` on Create jumps to `In progress`
- **Exact Code**: [`src/features/rc/components/RcHubSurface.tsx`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/features/rc/components/RcHubSurface.tsx), [`src/pages/AcademyMainhub.tsx:441`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/pages/AcademyMainhub.tsx#L441).
- **Live Browser Evidence**:
  1. `Filter passages` on `/practice/drills?section=rc` (`steps/26/media_0.png`) only shows passage-level filters (`Topic`, `Format`, `Framework`, `Passage difficulty`, `Status`, `PrepTests`). Question Family, Question Type, and Question Features only exist on `/rc/search` (`steps/44/media_0.png`), and there is **no link or button on `/practice/drills?section=rc` to reach `/rc/search`**.
  2. Clicking `Cancel` in the header of the default `Create` view (`AcademyMainhub.tsx:441`) unexpectedly switches the user to the `In progress` tab instead of resetting the builder.
- **Required Fix (`T02`, `T03`)**: Expose Question Family/Type/Feature filtering (or a clear question-filter tab/link) directly in the RC Drill Builder, and replace the misleading `Cancel` button on the default `Create` view with `Reset filters`.

#### 13. `[A8]` (P2 — Found by Argon): LSAT U's existing `Paragraph focus` and 6 Accessibility Color Schemes are hidden inside the `Aa` (`Text size`) button
- **Exact Code**: [`src/features/rc/pages/RcPlayer.tsx:1213-1251`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/features/rc/pages/RcPlayer.tsx#L1213-L1251), [`src/components/drill/official/OfficialDrillToolbar.tsx:295-351`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/components/drill/official/OfficialDrillToolbar.tsx#L295-L351).
- **Live Browser Evidence**: Clicking `Aa` (`aria-label="Text size"`) opens a popover (`steps/212/media_0.jpg`) containing `Text size`, `Paragraph focus` ("Highlight the paragraph under your mouse"), and 6 `COLOR SCHEME` themes (`Black on white`, `Grey on light grey`, `Purple on light green`, `Black on violet`, `Yellow on navy`, `White on black`), while `Change line spacing` sits as a separate adjacent icon. Because the trigger only says `Aa` / `Text size`, students (and Codex's audit!) miss that LSAT U already has `Paragraph focus` and color themes.
- **Required Fix (`T05`)**: Consolidate `Text size`, `Line spacing`, `Paragraph focus`, and `Color scheme` under a clearly labelled `Display` / `Aa Display` toolbar control and surface `Paragraph focus` as a discoverable toggle.

#### 14. `[A9 / RC-11]` (P2 — Expanded Live by Argon): Comparative Reading (`Passage A` & `Passage B`) renders as a single stacked wall of text, and expanding `Passage summary` in Review pushes questions off-screen
- **Exact Code**: [`src/features/rc/components/RcPassagePane.tsx`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/features/rc/components/RcPassagePane.tsx), [`src/features/rc/components/RcReviewLayer.tsx`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/features/rc/components/RcReviewLayer.tsx), [`src/features/rc/pages/RcResults.tsx:201-212, 395-450`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/features/rc/pages/RcResults.tsx#L201-L212).
- **Live Browser Evidence**:
  1. **Comparative Reading (`steps/201/media_0.jpg`, `/rc/drill?passage=168`)**: `Passage A` and `Passage B` are rendered sequentially in one single scroll container. Cross-referencing between Passage A and Passage B on synthesis questions requires constant vertical scrolling up and down.
  2. **`Passage summary` Placement in Review (`steps/151/media_0.jpg`)**: Expanding `Show passage summary` inside `RcReviewLayer` renders the multi-paragraph summary inside the **right-hand question column** above the question stem, pushing the question and choices A–E completely below the fold (`More below`).
  3. **Missing Source Badge on `RcResults` & Unprotected `drillMisses()` (`steps/129/media_0.jpg`)**: Under `BY PASSAGE`, cards show the title (`"Improving Farm Economics"`) and topic/framework badges but omit `PrepTest 139 · Section 3 · Passage 1`. And `drillMisses()` (`RcResults.tsx:209`) calls `createSession` with no `busy` state or `try/catch`, so double-clicking creates duplicate sessions.
- **Required Fix (`T05`, `T06`)**:
  - Add a sticky `[Both | Passage A | Passage B]` segmented view bar at the top of Comparative passages in `RcPassagePane.tsx`.
  - Move/dock `Passage summary` as a tab (`Passage Text | Passage Map`) on the **left passage pane** during Review so the student can read the P1–P4 map right next to the question and choices on the right.
  - Add `PT · S · P` source badges to `BY PASSAGE` cards on `RcResults.tsx` and guard `drillMisses()` with a `busy` state + optional skipped-question toggle.

#### 15. `[A7]` (P2 — Found by Argon): `\u00ad` soft hyphens & `****` markdown in RC JSON files break `Find Text` and comparative headers, and 0-match search hides the counter
- **Exact Code**: `public/data/rc/RC-PT119.json`, `RC-PT140.json`, `RC-PT148.json`, `RC-PT125.json`; [`src/features/rc/components/RcPassagePane.tsx:103`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/features/rc/components/RcPassagePane.tsx#L103), [`src/features/rc/pages/RcPlayer.tsx:1255`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/features/rc/pages/RcPlayer.tsx#L1255), [`src/features/rc/player.css:58`](file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-create/src/features/rc/player.css#L58).
- **Evidence**:
  - Invisible `\u00ad` soft hyphens inside words in `RC-PT119/140/148.json` prevent `findMatches()` from matching those words.
  - `****Passage A****` (4 asterisks) in `RC-PT125.json` renders literal `*` characters in `RcMarkdown`.
  - When a user types a word in `Find Text` with 0 matches, `RcPlayer.tsx:1255` (`findCount > 0 && ...`) hides the counter completely instead of showing `0/0`.
- **Required Fix (`T03`, `T05`)**: Strip `\u00ad` and normalize `****` in the RC bank/loader, and display `0/0` when `findQuery.trim().length >= 2 && findCount === 0`.

#### 16–21. Additional Confirmed Codex Findings (`RC-06`, `RC-07`, `RC-10`, `RC-12` + Review Save Risks)
- **`[RC-06]` (`T03`)**: Builder header shows `248 passages match your filters` (`preview.poolSize`) even when manual search (`handPickRows`) narrows the list to `1` passage (`RcHubSurface.tsx:583, 811`), and `/rc/search` caps tables at 200 rows without pagination (`rcSearch.ts:159`).
- **`[RC-07]` (`T02`)**: Normal in-flight drill start shares `pendingStartRef` with unresolved prior starts, flashing recovery copy and raw passage IDs (`RcHubSurface.tsx:519, 674`).
- **`[RC-10]` (`T02`)**: Player breadcrumb and pager ARIA labels call each question `Drill 1 of N` instead of `Question 1 of N` (`RcPlayer.tsx:1183`, `RcChrome.tsx:130`).
- **`[RC-12]` (`T03`)**: Manual passage picker in `RcHubSurface.tsx` renders all 248 passages (4,051 DOM nodes) at once without pagination/virtualization, sorting, or take-history facets.
- **Review Save & Tutor Context (`T06`)**: `RcPlayer.tsx:969-987` reveals a review reanswer locally before awaiting `recordAttempt` acknowledgement, `RcReviewLayer.tsx:58` navigates to `/inbox` without passing the passage/question address, and `rcHydration.ts:46` resets blind review choices on revisit rather than showing prior review history alongside the option to reattempt again.

---

## 4. Ordered Implementation Packets (`T01`–`T10`)

| Packet | Scope & Primary Files | Key Deliverables & Acceptance Criteria |
|---|---|---|
| **T01: History, Analytics & Contract Integrity** | `src/features/rc/api/rcProgress.ts`<br>`src/features/rc/lib/rcAdaptive.ts`<br>`src/features/rc/lib/rcTypes.ts` | 1. Filter out `excluded_from_analytics = true` sessions in `getQuestionHistory()` (`A1`).<br>2. Distinguish `is_correct: null` (skipped/unanswered) from `true`/`false` in `RcQuestionHistoryEntry`, `rollingAccuracy()`, and `passageStatus()` (`A2`).<br>3. Paginate `getQuestionHistory()` in 1,000-row pages (`A3`).<br>4. Define shared types for RC Exposure, Fixed Sets, Selection Recipes, and Question-Level Filter scope. |
| **T02: Launch Polish, Section Preflight & Terminology** | `src/features/rc/components/RcHubSurface.tsx`<br>`src/components/drill/SectionSelector.tsx`<br>`src/features/rc/pages/RcPlayer.tsx`<br>`src/features/rc/components/RcChrome.tsx`<br>`src/pages/AcademyMainhub.tsx` | 1. Separate normal `Starting…` UI from unresolved prior-start recovery copy (`RC-07`).<br>2. Enable `Status` (`Fresh · never attempted` / `Any`) filter for RC sections in `SectionSelector.tsx` using `rc_attempts`, navigate directly to `newManualSectionHref()` without bouncing through `/rc`, and align clock-start copy (`RC-08`, `A4`).<br>3. Change `Drill X of N` to `Question X of N` across header and ARIA labels (`RC-10`).<br>4. Replace misleading `Cancel` on default `Create` view with `Reset filters` (`A8`). |
| **T03: Unified Search, Global Finder Fix & Paginated Selection** | `src/components/questionfinder/QuestionFinder.tsx`<br>`src/components/questionfinder/QuestionJump.tsx`<br>`src/components/questionfinder/useFinderAddressIndex.ts`<br>`src/features/rc/pages/RcSearch.tsx`<br>`src/features/rc/lib/rcSearch.ts`<br>`src/features/rc/components/RcHubSurface.tsx`<br>`src/features/rc/lib/rcBank.ts` | 1. Fix `QuestionFinder` (`Ctrl+K`) `TEST` dropdown `Loading…` state (`A5`).<br>2. Route all `/rc/search` and `QuestionFinder` passage/question clicks to read-only `/rc/preview?passage=<id>&q=<qid>` instead of launching a live ticking drill (`RC-01`, `A5`).<br>3. Expose Question Family/Type/Feature filtering (or direct `/rc/search` integration) inside the RC Drill Builder (`A8`).<br>4. Align reserved PT defaults (`101-148`), display eligible pool vs. search matches separately (`RC-06`), paginate/window the 248-passage manual picker (`RC-12`) and `/rc/search` (>200 rows), and strip `\u00ad` soft hyphens + normalize `****` markdown (`A7`). |
| **T04: Saved RC Sets, Recipes & Rich History Cards** | `src/pages/AcademyMainhub.tsx`<br>`src/lib/standaloneDrillHistory.ts`<br>`src/pages/SavedSets.tsx` (or RC set store) | 1. Implement reusable Fixed RC Sets and RC Selection Recipes on `/practice/drills?section=rc&view=saved` (`RC-05`).<br>2. Enrich `buildStandaloneDrillHistory()` with official `PT · S · P · Title`, Topic, and completed first-attempt score (`A6`).<br>3. Add a safe `Discard` action for `In progress` RC drills (`A6`). |
| **T05: Shared Reader, Comparative Switcher & Standalone Section Parity** | `src/components/timed/TimedStandaloneSectionRunner.tsx`<br>`src/lib/timedSectionController.ts`<br>`src/features/rc/components/RcPassagePane.tsx`<br>`src/features/rc/pages/RcPlayer.tsx`<br>`src/components/drill/official/OfficialDrillToolbar.tsx` | 1. Mount `RcExamPane`, `RcPassagePane`, `RcQuestionPane`, and policy-scoped `OfficialDrillToolbar` in `TimedStandaloneSectionRunner.tsx` for RC sittings (`RC-09`, `A4`).<br>2. Add sticky `[Both \| Passage A \| Passage B]` view switcher for Comparative passages (`A9`).<br>3. Show `0/0` when `Find Text` has 0 matches (`A7`).<br>4. Consolidate `Aa` (`Text size`), `Line spacing`, `Paragraph focus`, and the 6 color schemes into a clearly labelled `Display` toolbar control (`A8`).<br>5. Improve responsive side-by-side split breakpoint (`RC-11`). |
| **T06: Spoiler-Safe Results, Left-Pane Passage Map & Review Reliability** | `src/features/rc/pages/RcResults.tsx`<br>`src/features/rc/components/RcReviewLayer.tsx`<br>`src/features/rc/pages/RcPlayer.tsx`<br>`src/features/rc/lib/rcHydration.ts` | 1. Offer review-first finish and conceal answer keys on `RcResults` until explicit reveal or blind review completion (`RC-04`).<br>2. Add `PrepTest · Section · Passage` badges to `BY PASSAGE` cards on `RcResults` (`A9`).<br>3. Add `busy`/`try-catch` guard and optional skipped-question toggle to `drillMisses()` (`A9`).<br>4. Dock/tab `Passage summary` (`Topic`, `Framework`, `Main Point`, `P1-P4` map) on the **left passage pane** during Review so expanding it never pushes the question and choices off-screen (`A9`).<br>5. Await save acknowledgement with retry on review reanswers (`RcPlayer.tsx:969-987`) and pass passage/question context to `/inbox` in `RcReviewLayer.tsx:58`. |
| **T07: Transparent Adaptive Recommendations** | `src/features/rc/lib/rcAdaptive.ts`<br>`src/features/rc/components/RcHubSurface.tsx` | 1. Separate first-attempt diagnostic accuracy from recent performance (`incorrectOnLastTake`) and review mastery (`RC-02`).<br>2. Display active target difficulty (`Level 1–5`) and sample basis on `Choose for me` (`Adaptive`). |
| **T08: Optional Active Training Overlays** | `src/features/rc/` training overlay components | Optional `Anticipation` (prediction before choices) and `Line-by-line` segmented reading in flexible RC drills, strictly isolated from protected timed sections and coordinated with `/reading-center/rc-recall`. |
| **T09: Explanation Coverage Inventory** | `public/data/rc/` & explanation components | Audit corpus-wide explanation coverage and missing states; preserve structured summaries and per-choice explanations. |
| **T10: End-to-End Acceptance & Release** | Test suites & live Agent Browser (`Port 9223`) | Full unit/integration/E2E verification + signed-in Agent Browser visual verification across all acceptance cases. |

---

## 5. Claude Code independent review (2026-10-17): verdict and corrections

Verified by reading source in `C:\Users\Joshu\dev\ai-os-projects\lsatu-rc-create` and by a read-only pass on the live signed-in site (lsatprep.study). No application code touched, no drill started. RC Bootcamp and Reading Center RC Recall untouched. The 7Sage side of each comparison rests on the recorded Codex and Argon observations; I only confirmed that a signed-in 7Sage dashboard is open, I did not re-drive 7Sage drills.

**Verdict: GREENLIT for T01 with the revisions below. NOT yet greenlit: T03 (A5 premise not reproduced), T05 (reference implementation misdescribed), and the T02 section-launch item (flag fallback missing).** The rest stands as written.

### 5.0 Checkout facts to settle before T01
- The worktree is on branch `codex/rc-create-flow`, not `codex/rc-create`, and is 55 commits behind `origin/main`. A `HEAD...origin/main` diff over the RC, SectionSelector, timed, questionfinder, AcademyMainhub and standaloneDrillHistory paths showed no changes, so the findings are not stale in those files. Re-run after a confirmed fetch.
- `supabase/functions/mcp/index.ts` is modified here (known Vite rebundle artifact). Restore it, never commit it.
- Start T01 on its own branch off current `origin/main`.

### 5.1 Findings verification

| Finding | Result |
|---|---|
| A1 excluded sessions ignored | **Confirmed in source.** `rcProgress.ts:377-411` selects only `question_id, is_correct, created_at`. The sessions table is `rc_drill_sessions`, not `rc_sessions`. |
| A2 skipped counted correct | **Confirmed in source.** `RcPlayer.tsx:650` writes null `isCorrect` for unanswered; `wrong = is_correct === false` is false for null, so `!everIncorrect` counts it right. The `Completed` label in the manual picker has the same flaw. |
| A3 1,000-row cap | **Confirmed.** The plan misses that `order('created_at')` alone is not a stable pagination key. |
| RC-02 sticky `everIncorrect` | **Confirmed, but misdiagnosed.** The bigger defect is that `getQuestionHistory` ignores `is_first_attempt`. Blind-review re-answers are inserted as `is_first_attempt:false` rows (`RcPlayer.tsx:982`) and flow into `attempts`, `everIncorrect` and `incorrectOnLastTake`. The docstring of `rollingAccuracy` says "first attempts" but it does not read first attempts. A miss fixed in review turns "Incorrect on last try" into "incorrect on last review". |
| A4 / RC-09 wrong player | **Confirmed in source.** `timedSectionController.ts:68` flattens the passage into `stimulus`; the runner hardcodes LR pane props (`:154-160`). The proposed fix is wrong, see T05. |
| RC-08 section bounce | **Confirmed in source**, but the redirect is conditional, see T02. |
| RC-05 Saved sets dead end | **Confirmed live.** `/practice/drills?section=rc&view=saved` shows "Saved LR sets ... Reusable saved sets support Logical Reasoning" with an "Open saved LR sets" button. |
| RC-03 search range | **Confirmed live.** `/rc/search` says "PrepTests 101-159". |
| A5 Finder `TEST` stuck on `Loading…` | **Not reproduced live.** On lsatprep.study the finder opened with the TEST select enabled and 60 options; `/data/finder-address-index.json` returns 200. Source shows the label is `disabled ? "Loading…"` where `disabled = loading \|\| failed` (`QuestionFinder.tsx:343, 647`), so a failed or slow fetch looks like "Loading…" forever. Treat as an intermittent first-paint or failure-state bug, and capture the network request when it recurs. Do not rebuild the index loader on this evidence. |
| A5 Finder rows launch a live drill | **Not supported by source.** `openHit` (`QuestionFinder.tsx:222`) only sets view and query; the address picker routes to `/rc/preview` (`:217-219`). The live launch is real in `/rc/search` (`RcSearch.tsx:101`, `open()` goes to `/rc/drill?passage=` and drops the question id). Re-attribute the step-201 screenshot before changing the Finder. |
| RC-04 answer-key spoiler | **Plausible, not re-read in full.** Verify the markup in T06 prep. `toggleExcluded` (`RcResults.tsx:214`) sets state before the await and never rolls back on failure. |
| A9 `drillMisses()` unguarded | **Confirmed in source** (`RcResults.tsx:209`). |

Not re-checked live: the Section launcher `Status` filter, standalone timed RC reader, results page and History cards. These need an account with RC history and would create sessions; leave for T10.

### 5.2 Packet corrections

**T01 (revised, greenlit).**
1. Select `id, session_id, question_id, passage_id, selected, is_correct, is_first_attempt, created_at`. Join the session with `rc_drill_sessions!inner(status, excluded_from_analytics)` and drop excluded. Confirm the embed works against the live schema cache; fallback is a second paged query for excluded session ids.
2. Order by `created_at asc, id asc`; page with `.range()` in 1,000-row pages until a short page.
3. Extend `RcQuestionHistoryEntry`: `answered`, `firstTakeCorrect`, `unansweredOnFirstTake`, `everCorrect`, `lastFirstTakeIncorrect`, `reviewCorrected`. Compute "last try" and `rollingAccuracy` from `is_first_attempt = true` rows only.
4. Session status rule, explicit and tested: rows from `completed` and `in_progress` sessions count as exposure (keeps today's Fresh semantics); only a `completed` session with every question answered yields `Completed`; `abandoned` is exposure, never accuracy; excluded counts as neither. Align with `src/lib/firstAnswerProgress.ts` (`adaptRcAttempts`) so there is not a third definition of what counts.
5. Add passage states `not_attempted`, `partial`, `skipped_only`, `completed`; update the picker label and the `status` filter predicates (`RcHubSurface.tsx:600-601`) inside T01, since the type change breaks them otherwise.
6. Tests: excluded session; null `is_correct`; 2,500 rows with identical `created_at`; miss then review fix; partial in-progress; abandoned; cross-account isolation.
7. Defer the Exposure, Fixed Set and Recipe types to T03/T04. They have no consumer in T01.
8. No backfill. Old rows cannot distinguish "skipped on submit" from "left blank at abandon"; reclassify on read only.

**T02 (revised).**
- The `/rc` bounce is gated: `RcHubSurface` calls `newManualSectionHref` only when `manualSectionsEnabled()` is true, the pace maps to a protected pace, `reveal === 'end_of_set'`, and no assignment or practice-test params exist. `SectionSelector.handleStart` must keep `rcSectionHref` as the fallback for flag-off accounts and unmapped paces, or RC sections break for them.
- RC section freshness cannot reuse `fetchAnsweredQids` (LR-only). It needs a section-level helper over `rc_drill_sessions` and `rc_attempts` using the T01 exposure rule, including timed-sitting sessions.

**T03 (hold).**
- Split A5 into (a) an honest failed state with retry in the Finder, (b) `/rc/search` `open()` to `/rc/preview?passage=<id>&q=<qid>` using the question id the row already carries. Drop other Finder routing changes unless a real launch path is found.
- Reserved PT range is a policy choice. Show 149-159 with a badge and a default-off toggle; do not hide exact-address matches.
- Window the 248-passage picker so selections persist across scroll; confirm the DOM cost is real first.
- Soft-hyphen cleanup can corrupt saved highlights: `rc_annotations` stores character offsets into passage text, so stripping `\u00ad` from PT119/140/148 (and `****` in PT125) shifts offsets for students who already highlighted. Normalize at match time for Find; fix `****` only after an offset audit; do it in the bank build script, not the runtime loader.

**T04.** `Discard` must set the session to `abandoned`, never delete rows (student work must be preserved).

**T05 (hold, corrected).**
- `TimedOfficialChildRunner.tsx` does not use `OfficialDrillToolbar`. It has a bespoke bar (text size select, marker select, find input, passage-only button). `OfficialDrillToolbar` lives in `RcPlayer`, `Drill` and review. "Mount `OfficialDrillToolbar` to match the child runner" contradicts itself. Extract the child runner's RC branch into one shared `RcTimedReader` used by both runners; do the toolbar and Display consolidation separately.
- Persistence: the child runner keeps highlights in a localStorage marker and attaches `rcHighlights` to close telemetry. The standalone sitting store has no annotation field. Reuse that pattern. Do not extend the sitting command schema: that is edge-function work, deployable only through Lovable, and needs Joshua's credit confirmation.
- `hydrate()` flattens the passage into an `LRQuestion` with `difficulty: 3, qtype: 'RC'`. Retain the real passage and question items on `TimedSectionState` instead of re-deriving them.
- Sealed policy must hold: no answers or explanations, and confirm each Display option is allowed in sealed mode.

**T06 (adds).** Persist a reveal timestamp separately so refresh, back and direct links neither re-hide nor re-spoil. Roll back `toggleExcluded` on failure. `drillMisses()`: refuse protected sessions and make creation idempotent with a client key, not only a `busy` flag. Confirm the left-pane Passage Summary with Joshua before building.

**T07.** Depends on T01's first-take and `reviewCorrected` fields.

**T08/T09/T10.** Unchanged. T10 must test the flag-off RC section path, sealed mode, and the live-only checks listed above.

### 5.3 Revised dependency order
T01, then T02 (needs the T01 exposure helper), then T03, then T04 and the shared reader extraction in parallel (disjoint files), then T05, T06, T07. T02 and T03 both touch `RcHubSurface.tsx` and `rcSearch.ts`; run them sequentially.

### 5.4 Decisions needed from Joshua
1. "Incorrect on last try": first take only, or include blind-review re-answers? Recommended: first take only, plus a separate "Fixed in review" label.
2. Do partial answers in an in-progress drill remove a passage from `Fresh`? Recommended: yes, as today.
3. Reserved PT 149-159 in `/rc/search`: badge plus default-off toggle (recommended) or hidden.
4. May bank passage text change when saved highlights exist? Recommended: no; normalize at match time.

### 5.5 Decision log (2026-10-17)
- Decision 1 resolved by Joshua: **A**. "Incorrect on last try" uses the first answer of the latest drill only. Blind-review re-answers do not change it. Add a separate "Fixed in review" label (T01 stores `reviewCorrected`; T07 shows it). Decisions 2 to 4 in 5.4 are still open; T01 uses the recommended answers as defaults.
