# LSAT U connected experience: build sequence

Started: 2026-09-28
Last reconciled: 2026-09-29
Status: Eighteen slices published; every implementation ticket remains open until its full acceptance checks pass. The latest slice lacks a positive real-row live check.
Specification: [#165](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/165)  
Decision map: [#155](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/155)

## The end state we are building

Students have seven dependable destinations: Home, My Work, Practice, Review, Progress, Library, and Schedule. Tabs keep related tasks on one page; the rail stays short. Every assignment, practice sitting, review episode, and session note opens its own saved record and returns to the right place. Home recommends a real next action. Scores and Progress use disclosed, account-owned evidence. Joshua keeps full teacher controls in a clearly identified selected-student mode while his practice answers remain separate from student results. The design adapts useful patterns from LSAT Lab, 7Sage, LSAT Demon, and AdeptLR without copying features that do not fit one-to-one teaching. No new video catalog is required.

**Status rule:** published means code is on the live site; it does not close a ticket. A ticket closes only when its source data, permission checks, deep links, error states, responsive UI, and a live task walk satisfy its acceptance list. The [coverage matrix](https://github.com/vnjkoxpl-42905/lsatu-684d89db/blob/main/docs/specs/2026-09-28-competitor-audit-coverage.md) is the feature-by-feature checklist; the GitHub tickets hold the full checks. The local app copy is `C:\Users\Joshu\dev\lsatu-connected-experience\docs\specs\2026-09-28-competitor-audit-coverage.md`.

The opening status text in specification #165 predates implementation. Use its requirements, the current ticket checks, and this reconciled status section when deciding what has shipped.

## What is already on the live site

| Area | Verified work | Still required before its ticket closes |
|---|---|---|
| Navigation | Seven-destination student rail and URL tabs. | Legacy-link and phone/sidecar sweeps, access locks and preference migration checks. |
| My Work and Home | Combined work and notes, source-linked weekly status, actor-owned next action. | Investigate My Work refetch blanking; check every assignment source, duplicate assignments, saved-start and finish, and post-completion Home behavior with real rows. |
| Practice | LR and RC Inspect, canonical exam pages, distinct custom LR, RC, Smart Drill, and guided sittings with resume and results. | Complete feedback/mode behavior, assigned-run task walks, exam result details, timed failure and second-device cases. |
| Review | Exact items from LR, RC, Activities, completed tests and sections; the historical Intro to LR interactive adapter is published. | Native bootcamp labs, Hard Sentences, teacher-selected reasons, new review episodes, flag independence, first/blind/reveal workflow, and a positive live saved-row check for the latest slice. |
| Progress | First-answer panel, dated saved-answer History, filters and topic views. | Reconcile every numerator, denominator, source, timeframe, and student/teacher view; disclose missing coverage. |
| Library and Schedule | Main Conclusion written topic pilot and existing Activity, bootcamp, and booking surfaces. | Saved resume and finish across representative exercises; one session's prep, recap, and follow-up chain across both views. |
| Teacher and study tools | Selected-student Review and Progress entry points. | Full teacher actions with actor attribution; teacher answers isolated from students; bookmarks, reading tools, explanations, weekly settings. |

The chronological release notes below record what was checked when each slice shipped. Earlier notes that say a later-shipped feature was still open are historical, not the current state.

## Ticket map, not a completion claim

The tickets below have native parent and blocker links in GitHub. They remain open while the remaining acceptance checks are worked through.

| Order | Ticket | Blocked by | Shippable result |
|---|---|---|---|
| 0A | [#166 Shared student scope and source coverage](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/166) | None | Trusted actor/subject scope and typed source coverage for both views. |
| 0B | [#167 Timed exam save safety](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/167) | #166 | Account-acknowledged timed LR/RC and full-test save-failure pause; reuse full PT sync already on `main`. |
| 1 | [#168 Seven-destination shell](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/168) | None | Short rail, URL tabs, locks, direct links, redirects, saved preference migration. |
| 2 | [#169 My Work](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/169) | #166, #168 | One honest To do, Completed, Notes & recaps ledger shared with Home and dossier. |
| 3 | [#170 Review](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/170) | #166, #168 | Typed review reasons, question workflow, and stable flag/history lifecycle. |
| 4A | [#171 Drills and Inspect](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/171) | #166, #168 | Exact selection, pool preview, mode labels, and score-free Inspect. |
| 4B | [#172 Practice Exams](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/172) | #167, #168 | Overview, All Exams, Attempts, deliberate starts, safe resume. |
| 5 | [#173 Progress](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/173) | #166, #168 | Shared first-answer LR/RC metrics, History, Topics, transparent coverage. |
| 6 | [#174 Home v3 integration](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/174) | #169, #170, #172, #173 | Reasoned next action and accurate entry points into the new system. |
| 7A | [#175 Library and exercises](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/175) | #166, #168 | Text-first Activities/bootcamps resume and one topic hub. |
| 7B | [#176 Schedule chain](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/176) | #169, #175 | Session prep, recap, follow-up links in student and teacher views. |
| 7C | [#177 Selected-student Teacher mode](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/177) | #166, #168, #169, #170, #173, #175, #176 | Full teacher controls under Joshua's identity, teacher answers isolated from student results. |
| 8A | [#179 Question study tools](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/179) | #170, #171 | Bookmarks, reading tools, optional attributed explanations, distinct feedback controls. |
| 8B | [#180 Weekly plan and settings](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/180) | #169, #173, #174 | Scannable prescribed week and consequence-aware study settings. |
| Final | [#178 Impeccable review and fixes](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/178) | All functional slices | Deferred by Joshua on 2026-09-29 while functional work continues. |

## Build from here, in verified slices

The order below is the current priority, not a request to rebuild shipped screens. A step may yield more than one release. Keep student flows usable after each release, then finish the teacher view on the same underlying records.

| Step | Build and decision | Completion evidence |
|---|---|---|
| **0. Stabilize My Work** | Reproduce Lovable's report that weekly-plan refetch blanks the assigned list or flashes loading. If confirmed, make source refresh independent so one failing lookup cannot hide other loaded work. Preserve existing rows and statuses. | Tab switch and background refetch keep prior content visible; a weekly lookup failure shows a local error; live student and teacher task walk. If not reproducible, record the attempted cases instead of treating the monitoring report as proven. |
| **1. Close the data and save foundation** | Finish [#166](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/166): trace LR, RC, Activity, bootcamp, assignments, and teacher actor/subject scope. Then finish [#167](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/167): timed PT/LR/RC and break save failure, retry, second-device takeover, and revoked-access behavior. | Owner and cross-account checks, authorized teacher attribution, explicit missing-source disclosures; network-failure task walks pause clock/navigation and resume exactly once. Ownerless old browser copies stay outside account Attempts. |
| **2. Close navigation and access paths** | Finish [#168](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/168): sweep old links and redirects, locked direct URLs, student Admissions lock with Joshua/admin access, saved navigation preferences, persistent Inbox and Finder, keyboard use, and phone/laptop/sidecar navigation. | Every main destination, internal tab, deep link, and return route lands correctly under student, teacher, admin, and denied-access states. No locked tab opens a misleading page. |
| **3. Complete Review** | Finish [#170](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/170): adapt current native bootcamp labs and Hard Sentences, add a durable teacher-selected review record and reason, then finish review episodes, first/blind/reveal states, flag independence, return filters, and optional detailed table. Get a real owned historical Intro to LR miss fixture if one exists; do not fabricate one for a demo. | Four source types and teacher selection open exact content and return to filters. Marking reviewed leaves the flag and attempt intact; a later miss opens a new episode; positive live detail where a genuine row exists. Unsupported sources remain disclosed. |
| **4. Close the coached work loop** | Finish [#169](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/169), [#174](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/174), and the weekly-plan portion of [#180](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/180). Trace two instances of one assignment, saved start, submitted finish, notes, teacher-to-student weekly status, and Home's next action after completion. | My Work, Home, and the student dossier agree on each owned source record. Opening alone never claims progress; finishing is saved before Completed; the recommended next action changes for the right reason. |
| **5. Finish Practice and Progress** | Close remaining [#171](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/171), [#172](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/172), and [#173](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/173) checks: mode and feedback labels, exact inspected/started set, deliberate exam start, compact results and expanded question detail, first/blind answers, then one calculation contract across Progress, History, Topics, and teacher view. | Repeated sittings remain separate; Continue/Results/Review target the same run; no Inspect write; timed and exam errors are safe; every displayed percentage names its source, count, denominator, window, and missing coverage. |
| **6. Connect learning and sessions** | Finish [#175](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/175) with two text-first Activities, one bootcamp, assigned exact exercise links, resume/finish, and authored topic pages. Then finish [#176](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/176) with one session's prep, recap, and follow-up through Schedule, My Work, and teacher dossier. | Saved work resumes exactly; completion is source-backed; authored explanations remain Joshua's; session links refer to the same event with correct timezone and honest absent states. No video dependency. |
| **7. Complete Teacher mode** | Finish [#177](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/177) on the shared student records. Give Joshua/admins selected-student assignment, review, note, and exact inspection controls while keeping an explicit Teacher mode banner and actor attribution. | A teacher can act on a selected student's work without impersonating them. Teacher practice answers never change student attempts, score, completion, History, or Review. Verify with two accounts and denied cross-student access. |
| **8. Add the remaining useful study controls** | Finish [#179](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/179) and settings in [#180](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/180): separate bookmark from flag, supported passage find/highlight/elimination, optional attributed second explanation, and consequence-aware accommodations, feedback, text size, contrast, and analytics choices. | Tools preserve the first answer and saved attempt; settings record provenance and affect future work only where specified. Keyboard, laptop, phone, and sidecar checks pass. |
| **9. Final functional acceptance; design pass when resumed** | Recheck every functional ticket against its acceptance list, resolve material failures, and publish the integrated functional release. [#178](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/178) Impeccable review is deferred by Joshua; run it and its fixes only when he resumes it. | Functional release may proceed with #178 explicitly open. Full plan completion requires its review and material fixes, plus agreement among live student and teacher task walks, source coverage, permissions, responsive layouts, and ticket status. |

**Next build:** Step 0. First confirm or disprove the My Work refetch report on a real signed-in page. If confirmed, fix that failure before adding more sources to the same work loop. Step 1 follows with the shared data and timed-save checks.

## Release method for every remaining step

1. Read the ticket's current acceptance checks and the coverage-matrix row. Identify an existing owned live fixture before changing code, if one exists.
2. Trace the durable source record, actor and subject, exact route, return route, and save failure behavior. Add the smallest source adapter or state change that makes one usable slice.
3. Run focused tests for the meaningful failure and permission cases, then typecheck and production build. Review the diff and restore only known build-generated churn.
4. Check changed UI in a running browser, including the relevant phone/laptop/sidecar sizes for responsive work. Keep the source error and empty states honest.
5. Commit and push the app through its guarded `.claude/safe-push.sh`. Confirm Lovable imported that commit; publish through its free control when ready. Any action that may spend Lovable credits still needs Joshua's immediate approval.
6. Open the fresh production route and walk the actual task. Record GitHub, publication, backend, permissions, and live evidence separately. Update the coverage matrix and this plan; close only the acceptance checks actually proved.

## What remains deliberately open

- Old ownerless browser-only exam recovery is outside the first release. Copies remain untouched and do not enter any account's Attempts. No display or import design was attributed to Joshua.
- The exact list of Impeccable findings cannot be known before functional screens exist. #178 requires recording and resolving material findings when they appear.
- A current-student prototype test may inform later refinement, but Joshua chose not to wait for it before this spec or these tickets.
- Joshua later authorized building and deploying verified slices. Lovable credit spend still requires separate approval immediately before the action. No new video production is planned.

## Rollout execution notes

These are improvements drawn from the first eleven published slices, not claims that the remaining tickets are done.

1. Trace the saved, owner-scoped record and exact return route before designing a new queue item. Teacher-selected Review and bootcamp work need durable source contracts before they can be displayed honestly.
2. Freeze the exact question or passage selection before offering Inspect. Both LR and RC builders now use the inspected IDs at launch; future builders should follow the same contract.
3. Identify a live account fixture at the start of each slice. If none exists, verify the adapter, owner guard, and empty state locally, and state plainly which live interaction could not be checked. Do not create practice records just to make a demo look complete.
4. Run focused tests while changing code, then one integrated typecheck and production build when the slice stabilizes. Repeat a gate only after a relevant fix or because the guarded push requires it. This avoids the several-minute duplicate checks that slowed the earlier slices.
5. After a build, restore only its known generated-file churn (`public/data/_bank.generated.json`, `public/data/finder-address-index.json`, `supabase/functions/mcp/index.ts`) and inspect the diff before committing.
6. Treat `main` push, Lovable Publish, and fresh live task walk as three separate checkpoints. Publish once per verified slice and wait for Lovable's completion state; a pushed commit alone is not a live release.
7. Reuse read-only question views and narrow source adapters. They kept owner checks, labels, return links, and no-write behavior easier to verify than duplicated page logic.
8. Confirm Lovable's project preview is ready before Publish. The first RC Inspect publish attempt failed while its new GitHub commit still showed Previewing. That timing is an observation, not a proven cause; wait for preview readiness and check the explicit publish result.

## Thirteenth slice: connected practice and weekly work

Custom LR and standalone RC sittings now share the Drills In progress and Completed lists, with distinct repeated runs and exact Continue, Results, and Review routes. Practice Exams uses canonical Overview, All Exams, detail, and Attempts links; Attempts can filter Unfinished and Completed using the URL. Home and My Work read weekly-plan completion from the source task instead of relying on a stale classroom mirror. The combined focused suite passed 34 tests, and typecheck, production build, and diff check passed. Commit `70ba8a1` reached `main` on 2026-09-29. Lovable reported "Your website was updated." A fresh signed-in live page showed the Completed exam filter and the unified list with repeated LR and three RC sittings. The weekly-plan change has focused tests but no live teacher-to-student status transition was exercised. Smart Drill, guided drills, and assigned drills still have separate histories. The broader ticket set remains open. Joshua waived the final Impeccable pass for now.

## Fourteenth slice: saved Smart Drill and guided completion

Drills In progress now includes the student's single saved Smart Drill session after at least one answer, with a Continue route and an honest saved-answer count. It does not claim distinct completed Smart Drill sittings, because the existing adaptive resume key is reused and attempts have no run ID. Both natural finish and End Drill now update an assigned guided drill's source assignment and linked task under the student guard. Focused tests passed 27/27, typecheck and production build passed, and local UI inspection corrected a misleading full-pool denominator. Commit `f33a793` reached `main` on 2026-09-29. Lovable reported "Your website was updated," and a fresh signed-in live Drills page displayed the saved Smart Drill beside RC. A live guided assignment was not ended for verification. Distinct Smart Drill sittings, direct guided retake history, and the remaining source coverage still need implementation.

## Fifteenth slice: resilient first-answer Progress and dated History

The first-answer Progress panel now loads independently of the older attempt breakdown, so an error or delay in the latter does not hide the student's saved first-answer metrics. The older breakdown shows its own loading and error states. Saved-answer History now groups matching LR and RC answers under calendar dates while retaining the area, result, and first-versus-repeat filters. Four focused tests, typecheck, production build, and diff check passed. Commit `4434e2f` reached `main` through the guarded safe-push script on 2026-09-29. Lovable reported "Your website was updated." Fresh signed-in live pages showed date headings with ten matching answers and an Overview containing both first-answer accuracy and the broader attempt breakdown. The full four-platform audit ticket set remains open.

## Sixteenth slice: distinct Smart Drill sittings

Smart Drill now saves each account-owned sitting under a durable run ID, resumes the active sitting, and finishes into Results and Review. The adaptive eligible pool stays available for question selection, while the result and review count only answers from that sitting. A legacy shared resume row is adopted once and closed when the migrated sitting finishes. Local signed-in browser verification completed a two-answer legacy sitting, then a separate one-answer sitting; both appeared in Completed with distinct Results routes. An empty sitting returned to Drills without a completed record. A review found a second Next control that bypassed the save gate; both Next controls and answer-then-advance now wait for the account run save. Focused tests passed 10/10, typecheck and production build passed, and the diff check passed. Commit `55f3aec` reached GitHub `main` on 2026-09-29. Lovable missed that push notification, so an empty `a6deac2` commit was sent through the guarded safe-push script to trigger sync, following Lovable's documented recovery path. Lovable imported both commits and reported "Your website was updated." A fresh signed-in live Drills page showed two separate Smart Drill sittings; the newer Results showed one answered question and Review showed exactly that question. The local browser checks wrote two completed sittings under Joshua's teacher account. Guided drill retake history and the broader audit remain open.

## Seventeenth slice: distinct guided drill sittings

Guided assignments and direct guided drills now preserve each account-owned sitting under its own run ID. Students can resume a frozen question queue, inspect earlier Results and Review, and start a new sitting without overwriting history. Answer navigation waits for an account save. Finishing freezes the saved answers before writing analytics, and retries use stable attempt IDs to avoid duplicate or changed results. An early End counts only attempted questions. Local signed-in checks saved three sittings under Joshua's teacher account, resumed the same unfinished run, and showed a one-answer result of `0 / 1`. Focused tests passed 35/35, typecheck and production build passed, and a scoped review found no material regression. Commit `a33fcac` reached GitHub `main` on 2026-09-29. The first Lovable Publish attempt failed while the revision still showed Previewing; a retry updated the site. Fresh signed-in live pages showed all three completed guided sittings and the one-answer `0 / 1` Results. Teacher-selected review, broader Library and Schedule integration, study tools, settings, and other audit ticket details remain open.

## Eighteenth slice: saved Intro to LR interactive misses in Review

The student Review queue now includes owner-scoped, missed `intro_lr_attempts` from earlier authored interactive exercises 3.1 through 3.5, 3.7, and 3.9. Each saved attempt has its own read-only detail route with its recorded answer and current authored question and reasoning. Viewing it cannot launch the exercise runner or write another attempt. Unknown authored IDs remain out of the queue. A code review caught missing historical 3.7 pronoun-replacement questions; these and a regression test were added before release. Seven focused tests, typecheck, production build, and diff check passed. Commit `ac4456b` reached GitHub `main` on 2026-09-29. Lovable imported it, and fresh signed-in live Review showed the new source statement; the exact-detail route displayed an owner-safe unavailable state for a nonexistent ID. Joshua's teacher account had no matching historical missed attempt, so a positive live detail with a real row was not verified. Current native Intro to LR labs, Hard Sentences, other bootcamp sources, and teacher-selected Review remain open. Lovable project monitoring separately reported a My Work refetch/blank-state issue; this release did not address it.
