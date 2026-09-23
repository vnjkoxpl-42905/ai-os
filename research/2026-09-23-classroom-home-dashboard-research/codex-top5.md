# Five ways to make v3 a better learning dashboard

2026-09-23 · Independent research; no other researcher consulted.

**My view:** preserve v3’s visual character and make every prominent element connect evidence to a useful action. The reference images support hierarchy, atmosphere, and varied scale; they do not establish learning effectiveness. All five recommendations sharpen existing cards. Keep the warm palette, dark anchors, one inbox, fixed-rule insights, coach pinning, and the seven-day strip unchanged.

Evidence below supports principles or product precedents, not proven LSAT U outcomes. Paths are relative to `C:/Users/Joshu/dev/ai-os/projects/lsatu/`. Sizes, thresholds, and motion timings are proposed specifications. Effort includes missing integration work.

## 1. Prescribe the practice, not just the question type

**Student sees:** Within the existing 420px main insight, reserve a 64–88px action block: “Rebuild the assumption test” → “Open the lesson.” Show a short, fixed explanation tied to the saved finding. A fundamentals finding routes to a mapped bootcamp lesson; a process finding to a guided drill; a reading finding to Read, Recall, Colour; a test-taking finding to a section briefing. Keep the existing alternative practice/review links and top actions. The action block crossfades in 150ms; no automatic movement while reading. Without a supported mapping, show “Review the diagnosis.” Coach-pinned state names Joshua explicitly.

**Why world-class:** The dashboard makes an instructional decision, rather than leaving the student to translate a chart. [Ericsson et al.](https://graphics8.nytimes.com/images/blogs/freakonomics/pdf/DeliberatePractice(PsychologicalReview).pdf) describe deliberate practice as structured work aimed at particular improvements. This extends the plan’s diagnosis-to-filter link to different learning activities.

**Existing foundation:** `src/lib/sectionAnalysis.ts` already contains categories, prescriptions, process families, and supporting questions; `src/lib/sectionHistorySave.ts` saves `analysis_json`. Launches: `src/lib/drillLaunch.ts`; recall activities: `src/features/activity-centre/api/types.ts`. **New:** a coach-reviewed diagnosis-to-resource registry; never infer a lesson from free text.

**Effort: M. Risk:** an inaccurate diagnosis can prescribe the wrong work. Expose the finding, preserve alternatives, and let Joshua’s pin win.

## 2. Turn “revisit” into a learning loop with an ending

**Student sees:** Expand v3’s amber wrong-answer strip to approximately 112px: “Revisit 3 questions” with three quiet stages: **Recall → Reattempt → Try a new question**. Launch the existing player; explanations stay concealed until the student attempts the question. After the due reviews, offer one fresh, matching question as a separate step. Return Home to “3 revisited · fresh check: 1/1,” never “mastered.” In-progress work resumes; no due items yields “Nothing scheduled for review.” A saved completion produces one 180ms check transition, no celebration.

**Why world-class:** It adds retrieval and transfer checking to the already-planned due queue. [Roediger and Karpicke](https://journals.sagepub.com/doi/10.1111/j.1467-9280.2006.01693.x) found better delayed recall after testing than restudying prose. [Khan Academy](https://support.khanacademy.org/hc/en-us/articles/360037127892-What-are-Mastery-Challenges-in-course-mastery) revisits previously practised skills according to elapsed time and mastery. The fresh-question check is my proposed LSAT adaptation, not a validated mastery test.

**Existing foundation:** `src/lib/wajNotesService.ts` supplies due dates, next actions, and lessons; `src/hooks/useJournalEntries.ts` supplies entries; `src/lib/drillLaunch.ts` supports question lists and filters. **New:** durable loop/outcome records and exposure-aware fresh selection. Journal status alone cannot prove delayed retention.

**Effort: L. Risk:** remembered answer letters masquerading as understanding; keep repeat and fresh results separate and never auto-promote journal mastery.

## 3. Show the gap between confidence and correctness

**Student sees:** An eligible 220px-high minor insight beneath the main card, using four labelled cells: **Sure/right, Sure/wrong, Unsure/right, Unsure/wrong**. Example: “You rated 3 missed questions 4–5/5. Revisit those decisions.” Tap a cell to open its evidence list, then the question. Counts appear immediately; selected-cell emphasis fades in 120ms. Use 1–2 as unsure, 4–5 as sure; show neutral/missing counts in a coverage line. Hide the lens below a provisional 12 distinct rated initial attempts.

**Why world-class:** Accuracy misses the distinction between uncertainty and a confident misconception. [Metcalfe and Finn](https://www.columbia.edu/cu/psychology/metcalfe/PDFs/MetcalfeFinn2011.pdf) studied correction of high-confidence errors after feedback. Their general-knowledge findings motivate investigation; they do not establish an LSAT benefit.

**Existing foundation:** `src/pages/Drill.tsx` writes correctness, confidence, mode, and time to `attempts`; `src/components/drill/ConfidenceSelector.tsx` uses 1–5. **New:** an aggregation adapter restricted to verified pre-feedback ratings; some write paths currently save null.

**Effort: M. Risk:** sparse or post-feedback ratings. Exclude unknown timing, disclose coverage, and avoid personality labels such as “overconfident.”

## 4. Make the next session a prepared conversation

**Student sees:** Inside the existing dark session card, add an 88px “Bring to Joshua” preview above its buttons: up to three student-selected question addresses and one short note. “Prepare session” opens a drawer with flagged questions, relevant evidence, and a link to the last published recap. States: empty invitation, private draft, explicitly shared, session rescheduled. Saving uses a quiet inline confirmation; the drawer opens in 180ms. Any message goes through the existing inbox with an explicit Send action.

**Why world-class:** It connects independent work to the service students actually buy. [Things](https://culturedcode.com/things/support/articles/4001304/) brings calendar context and actionable tasks together; [Linear’s inbox](https://linear.app/docs/inbox) lets people inspect the underlying work directly. The coaching benefit is a design hypothesis worth testing with Joshua and students.

**Existing foundation:** `src/lib/flaggedService.ts` supplies flags and notes; `src/pages/ClassroomRecaps.tsx` reads published recaps; `src/components/classroom/home/homeModel.ts` supplies session context; `src/hooks/useInbox.ts` supports messaging. **New:** agenda selection/draft storage keyed to booking, plus coach visibility.

**Effort: M. Risk:** another coach queue. Keep one brief per booking, accessible from session details; never treat every flag as an agenda item.

## 5. Make the beautiful bubbles explain themselves

**Student sees:** Preserve v3’s main bubble composition. Add a 32px “Missed questions” legend with two reference sizes. Bubble **area**, not diameter, encodes misses; every bubble names its denominator. Tap or keyboard-select one to highlight its existing type row below and update the action block. Use the existing rows for exact comparisons; on narrow containers, expose those values without overlapping labels. No eligible evidence means no bubbles. Selection gets a 150ms outline fade; resizing never animates statistical change.

**Why world-class:** [Datawrapper](https://www.datawrapper.de/blog/chart-types-guide) distinguishes expressive proportional-area graphics from easier-to-compare bars. V3 can have both. Change “costing you the most points” to “Most misses in your recent LR practice”: adaptive sampling does not establish lost exam points. Suppress trend arrows when modes or difficulty mix are materially different; name the mismatch.

**Existing foundation:** `src/pages/Drill.tsx` records question type, difficulty, mode, and correctness. The plan’s distinct-question RPC is **planned, not existing**. `src/lib/sectionAnalysis.ts` already models evidence-bearing breakdowns.

**Effort: M. Risk:** precision theatre. Counts describe sampled work; neither large bubbles nor tiny percentage changes establish ability.

## Blind spots

1. **Adaptive instability:** freeze insight order during a visit; offer an explicit refresh after new work. Background updates must not move a focused action. This adds to the plan’s fixed selection rules.
2. **Accommodation-aware interpretation:** pace findings must use the student’s actual timer allowance. Extend the plan’s timer preservation into every comparison, not just launches.
3. **Beyond keyboard testing:** check screen-reader chart alternatives, 200% text enlargement, contrast on orange gradients, and focus restoration from drawers. [WCAG 2.2](https://www.w3.org/TR/WCAG22/) covers these concerns; reduced motion alone is insufficient.
4. **Evidence lifecycle:** distinguish loading, failed, stale, and truly empty sources. Preserve the last successful result with its date; an RPC failure must not tell a returning student to “Start here.”
5. **Success criteria:** test time to appropriate practice, delayed-review completion, fresh-question performance, and coaching preparation. Dashboard engagement alone cannot validate learning.

## Considered and rejected

- **Readiness score:** [Strava’s fitness/freshness](https://stories.strava.com/articles/how-to-use-stravas-fitness-and-freshness-tool) is an appealing metaphor. LSAT U lacks a validated equivalent; a composite number would overclaim.
- **Persistent animated glows:** keep atmospheric styling, cut continuous attention-seeking motion. [NN/g](https://www.nngroup.com/articles/animation-usability/) explains its distraction cost.
- **Another command surface:** [Raycast Quicklinks](https://www.raycast.com/core-features/quicklinks) are useful precedent, but the planned Question Finder already owns this job.
- **An unrestricted widget builder:** [Notion’s task aggregation](https://www.notion.com/help/guides/give-your-to-dos-a-home-with-task-databases) is useful; requiring students to design Home adds configuration work and weakens coaching priorities.

Research used Firecrawl searches and primary-page scrapes; paid product flows were not tested. Stripe’s scrape was CAPTCHA-blocked and supplies no relied-on evidence. Source captures remain in `.firecrawl/`.
