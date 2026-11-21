# Signed-in RC comparison observations

Date: 2026-10-16, America/Toronto. Inspector: Codex. Browser: Codex in-app browser, signed-in Joshua accounts. These are observations, not a claim that every combination or persistence failure was tested. No app code changed. No messages sent or existing work deleted.

## Reproduction ledger

| ID | Path and action | Observed result |
|---|---|---|
| E01 | 7Sage Dashboard > menu > Drills, sections, PTs | One hub separates drills, sections and PTs; in-process counts and saved templates are visible. RC Short (1 passage), Long (2 passages), Quick-start unlimited adaptive. Drill-by-tag priorities lead into filtered builders. |
| E02 | 7Sage RC Short drill > Customize questions | Automatic/manual selection; tags, passage difficulty, status. Automatic pool showed 379 of 404 passages for this account/configuration. This is NOT directly comparable to LSAT U's filtered count. |
| E03 | 7Sage Training modes | Immediate feedback after passage, Anticipation, Line-by-line. The latter two were enabled together and observed in a launched passage. |
| E04 | 7Sage manual picker | Search; Available for drills, Status, Tags, Difficulty, PrepTest, Bookmarked, Result, Takes; reset, sort, total matches, selected passage/question count, Load More. Rows use source address and abbreviated tags, with expandable passage. |
| E05 | 7Sage manual search | `P.D. James` returned zero; `James` returned nine passage matches. PT101.S4.P1 was identifiable and added. Punctuation handling is a concrete improvement opportunity; do not claim all text search is broken. |
| E06 | 7Sage timing menu for PT101.S4.P1 | Standard 8:45, Unlimited, Target 9:51; percent and absolute-time customization; accommodation settings link. |
| E07 | 7Sage live PT101.S4.P1 runner | Full matching passage exists; first sentence visible in Line-by-line mode. Separate passage-reading tracking initially masks question area. Stop reading tracking exposes anticipation choice: have something in mind / nothing in particular. Selecting the former reveals answers. No typed prediction was required in this observed step. |
| E08 | 7Sage runner tools/menu | Passage-only, find, hide timer, review, accessibility, flag, response masking, keyboard highlight; expandable text labels. Menu has submit, pause, save-exit, print, training toggles, timing accommodations, blind review, score prediction, appearance. Accessibility offers color schemes, font size, zoom, line height. Controls observed, not every setting changed. |
| E09 | 7Sage blind-review settings | Recommendation categories: incorrect, flagged, skipped, slow, inferred guesses, multiple answer changes, and 0-2 correct questions to obscure correctness. Reasons can be shown. This inspection did not validate recommendation accuracy. |
| E10 | 7Sage RC Section setup | Fresh-status filter; source section picker; 35-minute standard timing; practice-pool settings; Anticipation, Line-by-line, Test Day Disruption. Later actual section inspection recorded in E30. |
| E11 | 7Sage analytics > Questions & explanations | Filters for source, status, section, tags, difficulty, availability, bookmarks, analytics inclusion, notes, result, blind review, timing vs target, last format, practice timing, date, takes. RC question source `PT101.S4.P1.Q1` found one; shorter `PT101.S4.Q1` found zero in attempted scope. |
| E12 | 7Sage PT101.S4.P1.Q1 detail | Passage, question, hidden-answer switch, option-level explanation toggles, notes/bookmark/comments, AI and tutor entry points. Explanation has passage and question videos, alternative instructor versions, captions/speed controls. Videos not watched end-to-end; AI/tutor not invoked. |
| E13 | 7Sage same question Analytics | Question/passsage difficulty, tags, answer popularity, cohort score information, take history and timing, including prior LawHub-labelled attempt. Statistical validity and full explanation coverage not verified. |
| E14 | LSAT U Classroom > Practice > RC | Create/In progress/Completed/Saved sets. Builder: 1 passage, Untimed/Standard/Custom; After passage/At end/After question; automatic/manual. 249 filtered fresh passages initially. |
| E15 | LSAT U Filter passages | Topic, Standard/Comparative, framework, 1-5/adaptive difficulty, Any/Fresh/Incorrect before/Incorrect last try, PT range 101-148 default with newest-test protection copy. |
| E16 | LSAT U Choose passages > `P.D. James` | One correct title match; selected count 1 passage/8 questions. Header still says 249 passages match filters, failing to distinguish pool from search results. All manual rows initially appear in a very long list. |
| E17 | LSAT U Preview drill > expand PT101 P.D. James | Full passage and eight questions/options visible, correct answers/explanations hidden. Preview promise identifies exact launched content. Previewing full content before timed work can contaminate freshness, even without an answer key; track exposure separately. |
| E18 | LSAT U Start this drill | Transient recovery copy references previous Start and passage ID 1352 on a normal launch. Then correct full passage and all eight questions load. |
| E19 | LSAT U PT101.S4.P1 drill runner | Directions, passage-only, find, underline/three colors/eraser, text size/spacing, timer, bookmark/study marks, flags, cross-outs, question overview, pause, save-exit, complete, help, check passage. Find `James` reports 1 of 7 with next/previous/clear. Pause hides content and resumes. No answers submitted in this inspection. |
| E20 | LSAT U runner wording/layout | Official source label plus `Drill 1 of 8` for a question. At approximately 1000px-wide Codex panel, passage and question are stacked with separate scroll regions, outer scroll, and More below fade. 7Sage at comparable panel width retained side-by-side panes. This is one viewport observation, not a complete responsive audit. |
| E21 | LSAT U RC > Saved sets | Destination says Saved LR sets; reusable sets support LR only. RC directs users to histories instead. Confirmed feature gap. |
| E22 | LSAT U Practice Exams > Take a section > RC > PT102 S1 | PrepTest searchable picker, section dropdown, standard/1.5x/2x timing. RC status selector disappeared when switching from LR. Timing copy uses per-question average, despite passage reading overhead. Start copy says clock starts straight away. |
| E23 | Same section launch | Start Section briefly shows populated four-passage drill builder, then Prepare section screen, then separate Start section. Preflight explicitly says clock has not started. Actual start acknowledged and countdown runs. Full source passage and 26 questions present. This contradicts initial copy, rather than proving premature timing. |
| E24 | LSAT U protected RC runner | At inspected viewport, passage/question, flag, cross-outs, question pager, next/previous, pause, finish, notepad. No drill-style passage search, annotation toolbar, text size/spacing or passage-only controls visible. Account save acknowledged copy is prominent. Pause acknowledged; returned to exam hub, which lists PT102 S1 0/26 answered. |
| E25 | LSAT U global question finder | RC scope preselected, PT/section/question controls and address/text search. `PT101 S4 Q1` resolves source correctly; Open question leads to read-only preview with full passage and exact question. Explicit launch says all eight questions, untimed, after-passage feedback. This is a strength to preserve. |

## Account effects and boundaries

E30: On the follow-up continuing into 2026-10-17, launched 7Sage PT102 S1, matching the LSAT U inspected section. Full opening passage about electronic mail, 26-question navigation and 35-minute countdown loaded directly. Passage-only, passage find, timer hiding, review, accessibility, flag, response masking and keyboard highlight controls remain available. Opened accessibility: color schemes, font, zoom, line height. Menu includes pause/save-exit and Anticipation/Line-by-line/Test Day Disruption switches, all off. Saved and exited to Dashboard without answers or submission. This verifies section entry and visible tools, not scored completion or all tool behavior. Practice ID `pra_034hERU64yoBO63XEhMYTN`, first item `itm_034hERU7LDFDDy1VBfV5SU`.

E29: Live `/bootcamp/rc-engaging-with-the-passage` cover shows Exit, RC BOOTCAMP, Engaging With The Passage, Resume and 55% complete for the existing account. No purpose, expected time or description of the task appears on this cover. Existing progress was not advanced. The internal lesson sequence was source-inspected, not completed live.

### Additional search and review inspection

- E26: Separate LSAT U `/rc/search` lists 320 passages and 2,150 questions, PT101-159, with question family/type/feature filters. Its title/stem search returned zero for `PT101 S4 Q1`, which the global finder resolves. These are different search contracts and pools, not evidence that content is missing. Source confirms capped result tables without pagination.
- E27: Completed RC history lists passage counts, first-answer counts and dates, with Results and Review actions. An existing one-passage attempt dated 2026-08-27 was opened read-only. Results show first-attempt score, conditions, total/average recorded question time, unanswered count, top three type focus areas, difficulty counts, passage rollup, each answer/correct answer/time, Review all, Drill your misses, New drill, and Exclude from analytics. No analytics setting was changed. This is substantive existing functionality, not a missing results page.
- E28: Review all for existing session `34ff285e-ab7c-4217-88d0-b5c2366a92cf` opens the full passage and first question with original answer hidden: 'Pick again, then see both.' Show my answer is available. Reader tools remain, cross-outs are disabled, existing flag is shown, and Question details displays source, difficulty, question type/features and passage topic/format/framework. No review answer was selected and no original result was changed. A global results page revealing correct answers before this hidden-answer review limits a truly blind sequence when entered via Results.

- Created LSAT U ordinary drill `b08b1675-ebed-43ce-ad4b-39a179709326`, PT101 S4 P1. Saved and exited without selecting answers.
- Created LSAT U protected section `6ecee5df-3e8c-4afa-b14d-ab5fb1e0ac8a`, PT102 S1. Started, paused at approximately 34:22, returned to hub; 0/26 answers confirmed.
- Created 7Sage drill `pra_034hDuyRDBgramkF4Ds48U`, PT101 S4 P1; saved and exited without answers. In-process count increased 38 to 39. Mode choices applied to this audit drill. No deletion performed.
- These audit sessions can affect exposure/history and must not be treated as learner performance. No scores were submitted. Existing student assignments and prior attempts were not altered.
- No physical phone, screen-reader speech, full zoom matrix, offline/failure injection, cross-device concurrency, scored completion or exhaustive content coverage was verified in this browser pass. Prior source receipts are separately identified in source-inventory.md.
- RC Recall/RC Training is a separate already-specified workstream. Do not overwrite its current build order.

## Authoritative links

- [LSAT U RC builder](https://lsatprep.study/practice/drills?section=rc)
- [LSAT U exams](https://lsatprep.study/practice/exams)
- [7Sage practice hub](https://7sage.com/u/usr_031j8RfMOF3zm8TC7Hg2iW/practice)
- [7Sage RC builder](https://7sage.com/drills/build/rc)
- [7Sage RC section setup](https://7sage.com/drills/section/rc)
- [7Sage inspected question](https://7sage.com/u/usr_031j8RfMOF3zm8TC7Hg2iW/question/PT101.S4.P1.Q1)

Screenshots of live runner layouts and accessibility trees are retained in this chat's tool evidence; this file summarizes observations without copying the licensed passage corpus.
