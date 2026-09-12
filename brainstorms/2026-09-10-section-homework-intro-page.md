# Section homework intro page: Brainstorm / Discovery Notes
Date: 2026-09-10 · Goal: decide how a single-PT-section homework assignment opens for the student, replacing the classroom "assignment detail" page with a LawHub-style section intro (PT title, section pill, question count, Begin, directions) that launches the timed section.
Status: paused (2026-09-11, at Q13)
Context sources: PR #113 (`fix/homework-timed-section-launch`), `src/components/classroom/ClassroomRouteViews.tsx` (ClassroomAssignmentView), `src/pages/TestingCentre.tsx` + `src/pages/PracticeTestRun.tsx` (existing practice-test lobby + between-section screen), screen recording 20260911-0150-03 (current flow), LawHub PT101 screenshot (target).

## Summary / key decisions
- Current flow (verified from recording): Home "Open the set" → `/classroom/:assignmentId` detail page (title, callout, "25 questions | about 35 minutes | assigned", Start) → Start → timed section. Joshua calls the middle page "the notes page" and wants it gone for section homework.
- SUPERSEDED by Q1: first target screenshot (breadcrumb `Library / The Official LSAT PrepTest 101`; left: PT title, "Sections" row of pills with status under each ("Not started"); right teal panel: "Section 1", "Questions 27", **Begin**, official Directions paragraph. Begin starts the section.) Actual target is the LawHub section-directions card; see Q1.

## Q&A log


### Q1 - What "Open the set" lands on
- Asked: right-half-only intro vs LawHub two-halves vs whole-PT with clickable siblings.
- Captured: none of the three. Joshua supplied a second screenshot, the LawHub **section directions card**, and wants that template "ideally exactly", replacing the green panel idea:
  - full-width light blue-grey background (#c5d3e0-ish)
  - one white rounded card, centred text: `Section 2` / `Total Section Time - 35 minutes` / `25 Questions`
  - inside the card, left-aligned: **Directions:** followed by the official LR directions paragraph ("Each question in this section is based on the reasoning presented in a brief passage. In answering the questions, you should not make assumptions that are by commonsense standards implausible, superfluous, or incompatible with the passage. For some questions, more than one of the choices could conceivably answer the question. However, you are to choose the best answer; that is, choose the response that most accurately and completely answers the question.")
  - below the card, centred, an orange/brown pill button `GO TO QUESTIONS` (all caps)
  - no PT title, no section pills, no breadcrumb on this screen
- Tentative / suggested: the Section number shown is the real section number from the PT (Section 1 for PT143.S1), and "35 minutes" reads from the student's timing setting rather than a literal 35.
- Flags: none

### Q2 - Shell or takeover
- Asked: card inside the Classroom shell vs full-screen takeover.
- Captured: **"take over the screen."** Opening the set leaves the Classroom entirely; the card sits alone on the blue-grey background, like the timed section itself. No sidebar, no Assigned-work column.
- Flags: none

### Q3 - When the clock starts
- Asked: clock starts on GO TO QUESTIONS vs when the card appears; and what a return to the card after closing the tab looks like.
- Captured: **A.** Clock starts on GO TO QUESTIONS. The directions card is untimed, like LawHub and the real test.
- Tentative / suggested: because nothing is started until GO TO QUESTIONS, leaving on the card and returning shows the card again with no time lost, and the assignment stays "assigned" (not "in progress") until she presses the button. Not confirmed; Joshua answered only the clock question.
- Flags: return-to-card behaviour -> Joshua, if the suggestion above is wrong

### Q4 - Time line for an accommodated student
- Asked: read the student's timing setting vs always "35 minutes" vs no accommodations on homework.
- Captured: **A. It should adjust.** The card's "Total Section Time" shows the student's accommodated time, and the section runs on that clock. Joshua will give the specific accommodation per student "unless it's already there"; ideally each student's accommodation lives in their student file (`students/<name>/`), and he will likely tell the agent what it is (or the agent can ask) at assign time.
- Tentative / suggested: the source of truth in the app is the existing timing setting the Testing Centre already reads (`useUserSettings`); assigning a section does not need its own accommodation field. At assign time the script could print the student's current setting so a mismatch with the student file is caught before she opens it.
- Flags: which students have accommodations and what multiplier -> Joshua, per student, at assign time; record in `students/<name>/<name>.md`
- Found in code (not asked): the setting is `settings.defaultTimingMode` in `src/contexts/UserSettingsContext.tsx`, values `'35' | '52.5' | '70' | 'unlimited'` (standard, 1.5x, 2x, untimed). `SectionSelector` and the Testing Centre already derive `baseMinutes` from it. The PR #113 full-section launch hard-codes `timer.mode: '35'` at `drillRunSpec.ts:212`, so today an accommodated student assigned a section would get 35:00; the build must read the setting instead.
- Found in code (important): `defaultTimingMode` lives **only in the browser's localStorage** (`userSettings` key). It is not in Supabase, so Joshua cannot set it for a student from admin, it does not follow her between devices, and nothing at assign time can read it. Any "the card adjusts to her accommodation" promise needs a server-side field.

### Q5 - Where the accommodation lives in the app
- Asked: profile column set by admin vs per-assignment flag vs both.
- Captured: **A.** A column on the student's profile, set by Joshua. The assign script prints it, the directions card and the section clock read it. The browser `defaultTimingMode` becomes at most a per-session override.
- Tentative / suggested: `profiles.timing_multiplier` numeric (1.0 / 1.5 / 2.0), nullable = standard; the Testing Centre and SectionSelector should read the same column so one setting names one clock everywhere. Assign script warns when the student file and the profile disagree.
- Flags: none

### Q6 - After the last question
- Asked: auto-complete with results vs self-mark-done vs no results until session.
- Captured: **Blind review.** When the section is completed, the blind review should pop up so she does it right then, after the section. (Results/score come after blind review, as the existing blind-review flow does; assignment completion not separately stated.)
- Also captured (unprompted): **the timer must count down**, starting from the top (35:00 or her accommodated time) and going backwards, not up. Note: the fix-branch build already shows "Section Time Remaining: 34:59" counting down; the recording was of a build where it counted up, or Joshua saw the untimed stopwatch on the live site. Either way, countdown is the requirement.
- Tentative / suggested: assignment flips to completed once blind review is submitted, so "Mark done" is never needed for a section.
- Flags: confirm where "completed" is stamped (after section submit or after blind review) -> Joshua
- Found in code: blind review already exists (`BlindReviewSelection` → `BlindReviewFlow` in `src/pages/Drill.tsx`) and is enabled for `full-section` mode, but the selection screen appears **only if she flagged at least one question for BR during the section** (`brMarked.size > 0`, Drill.tsx:3187). With no flags she goes straight to results. So "the blind review should pop up" means: for an assigned section, always enter blind review after the last question, flags or not.

### Q7 - Blind review with nothing flagged
- Asked: always open with every question available vs flagged-only vs today's rule.
- Captured: **A.** For an assigned section, blind review always opens after the last question with every question available; flags made during the section pre-tick those.
- Flags: none

### Q8 - Pausing mid-section
- Asked: no pause vs pause allowed vs leaving forfeits.
- Captured: **B, with a first-time caution.** Pause is allowed, and she can pause and resume as many times as she wants. But the **first time** she presses Pause in a sitting, an "Are you sure?" confirmation appears that says, in Joshua's voice, that pausing is not allowed on a real test unless she has an accommodation that permits it. After she confirms once, later pauses in that section do not re-ask. Joshua also wants to **see that she paused** (visible to him: pause count / paused time on the attempt).
- Tentative / suggested: record pause events (count, total paused ms) on the section attempt and surface them on the teacher's view of the assignment, e.g. "Paused twice, 4 min total". Whether "first time" means per section or once ever per student was not stated; per section is assumed.
- Flags: exact wording of the caution -> Joshua (route through wiki/teaching-voice.md); first-time = per section vs per student -> Joshua

### Q9 - Classroom cards
- Asked: keep cards and change destination vs retitle vs leave as is.
- Captured: **A** ("Yes. You can do that."). Home "Open the set" and the Assigned-work "Open" both go straight to the directions card; "Mark done" is removed for section assignments because blind review completes them.
- Flags: none

### Q10 - Which section types
- Asked: LR only vs directions that swap by section type.
- Captured: **RC and LR, both.** "For RC and LR I should be able to do this." The directions card swaps its text by section type (LR directions vs RC directions). Logic Games is not on the current LSAT and must never be mentioned or asked about again.
- Flags: RC section data source. `public/data/*-LR.json` covers LR only; RC sections in the app live in the Read, Recall, Colour seed (12 sections) and `scripts/rc-source/recovered/`. Whether a timed RC section can be assigned today depends on whether the section runner can load an RC section by PT+section -> agent to check in the plan, then Joshua if content is missing.
- Found in code: RC timed sections already exist as a runner (`/rc/drill`, `src/features/rc/lib/rcSections.ts`: sections built from the passage index, 4 passages, 35:00 clock, own pace ids, and the Testing Centre's practice test runs RC legs through it). RC questions are keyed by passage id, not `PT-S-Q` qids, so an RC assignment cannot be a `homework_sets.question_qids` row the way LR is. The plan needs a second shape for an RC section assignment (PT + section → the RC runner) behind the same directions card.

### Q11 - Naming an RC section at assign time
- Asked: script infers type from PT.S vs explicit --rc flag.
- Captured: Joshua will say it in words: "a specific RC section", "a passage", or "take an RC section from this PT". The agent turns that into the command. So the script takes an explicit type (`--section PT143.S3 --rc`, or a `--passage` form for a single passage) and the skill maps his phrasing to it. He does not want to remember a flag; the agent does.
- Tentative / suggested: `--rc-section PT143.S3` for a full timed RC section; `--passage <id|PT.S.P>` for one passage (untimed or short clock, separate decision); "an RC section from PT143" = agent lists the loaded RC sections for that PT and picks/asks.
- Flags: single-passage assignment (timing, whether it uses the directions card) -> Joshua, only if he asks for one

### Q12 - Reopening a completed section
- Asked: read-only results vs free retake vs first-attempt-counts.
- Captured: once completed, the section leaves the homepage. It is saved to her **Analytics** and her **History**, and that is where she (and Joshua) find it afterwards. No retake path from the assignment itself was asked for.
- Tentative / suggested: reads as A (read-only record). If Joshua wants her to sit it again, he assigns it again; the unique index already allows re-issue once the prior copy is completed.
- Flags: none

### Q13 - Sequence and shipping (paused here)
- Asked: merge #113 now then one follow-up PR vs hold vs three small PRs.
- Captured: not answered directly. Joshua pivoted: erase the test assignments on joshua.fisseha01@gmail.com, assign a PT156 LR section of the agent's choice, and show him what it looks like as built right now; merging #113 first is allowed if needed to execute. That implies "merge #113 now" (A or C); the follow-up PR shape is still open.
- Flags: A vs C for the follow-up work -> Joshua, on resume

Status: paused 2026-09-11. Resume point: Q13 (shipping shape), then the completeness backstop.

## Open flags (pending input)
- Return-to-card behaviour if closed before GO TO QUESTIONS -> Joshua (assumed: card shows again, no time lost)
- Where "completed" is stamped: after section submit or after blind review -> Joshua (assumed: after blind review)
- Pause caution wording; "first time" per section or per student -> Joshua
- Each student's accommodation (1.0 / 1.5 / 2.0) -> Joshua, per student; record in students/<name>/
- RC section content coverage per PT -> agent to check in the plan
- Follow-up PR shape (one PR vs three) -> Joshua

### Q14 - Why the hero shows three buttons (asked by Joshua after seeing PT156.S4 live)
- Captured: Joshua wants "Open the set" / "Open assigned work" reconciled ("it should just make sense") and **Mark done gone**: an assigned section is marked done only when she completes it, and then it leaves the page.
- Found in code: "Open assigned work" is unconditional on the hero (ClassroomHomeView.tsx:290) and only switches to the Assigned-work list. Mark done is hidden when the classroom item's `metadata_json.kind === 'timed_section'` (useAssignedTodoFeed.ts selfCompleting), and such items self-close via `closeOutAssignedSection` when the full-section run finishes (Drill.tsx:2633). The `--section` script path writes a plain `homework` item (via `homework_sets`), so neither rule applies. Nothing in the codebase currently writes a `timed_section` item; that path also has its own in-place "briefing" overlay (SectionBriefing.tsx), which the LawHub card supersedes.
- Decision (agent proposal, pending Joshua): converge the two paths. A single-section homework assignment carries `timed_section` metadata (pt, section, section_kind, minutes) so it inherits no-Mark-done and self-close; the directions card replaces the briefing overlay as a full-screen page; drop "Open assigned work" from the hero when it duplicates the primary action.

### Q15 - First look at the built section (2026-09-11, Joshua on the dev build, PT156.S4)
- Captured, in his words where it matters:
  1. "Section Time Remaining" did not appear to be running down. Must count down visibly.
  2. When time is up the section **stops**, says **"Time's up"**, and points to blind review.
  3. An assigned section never offers **Show Answer** or **Explanation** during the sitting, unless Joshua explicitly says otherwise at assign time. (Sealed by default.)
  4. The runner's **Directions** button "doesn't make sense of how it's set up" - review what it opens and make it the same directions as the card.
  5. **Pause notice, LawHub-style, for every section and practice test a student sits** (not only assigned ones): title "Notice", body "Navigating to this page will pause the test. Note that pause functionality will not be available during the real exam.", buttons Cancel / Ok, checkbox "Don't show me this message again". If ticked, no more prompts for the rest of that section. If not ticked, it prompts on every Pause. Supersedes Q8's "first time only" rule.
- Joshua typed "/grillwithdocs"; no skill by that exact name is installed (nearest: grill-with-docs-codex, a Codex plan-review loop). Requirements above are concrete enough to build; noted here rather than blocking on it.
