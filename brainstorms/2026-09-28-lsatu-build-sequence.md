# LSAT U connected experience: build sequence

Date: 2026-09-28  
Status: Sixteen verified slices published; full ticket coverage remains open  
Specification: [#165](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/165)  
Decision map: [#155](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/155)

The tickets below have native parent and blocker links in GitHub. They describe usable vertical slices, with student flows first and the existing teacher desk retained. A slice is complete only after its live route, relevant backend state, permission checks, and task walk agree. Current `main` must be reconciled before coding from the older dirty feature checkout.

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

## How to run the work

1. Start #166 and #168 as independent early slices. #167 follows the shared scope contract; verify current production behavior and migrations before changing exam code.
2. Release #169 and #170 as working student pages. Keep direct old links and locked tab behavior intact on each release.
3. Build #171, #172, and #173 in parallel where teams do not edit the same files. Do not publish Review or Progress totals without their source coverage checks.
4. Connect #174, then finish #175 and #176. #177 can prototype its selected-student shell earlier, but its completion depends on the shared facts and coaching actions.
5. Complete #179 and #180 for the remaining viable audit details, then run #178. Its fixes and recheck are part of the core release, not a report handed off for later.

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
