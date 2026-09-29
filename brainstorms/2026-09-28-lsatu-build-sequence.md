# LSAT U connected experience: build sequence

Date: 2026-09-28  
Status: Twelve verified slices published; full ticket coverage remains open  
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
| Final | [#178 Impeccable review and fixes](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/178) | All functional slices | Critique, audit, material fixes, recheck, and final task/data verification. |

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
