# Student account controls, 2026-10-28

Local implementation in C:/Users/Joshu/dev/ai-os-projects/lsatu-my-work-20261026. Base18fc8af7; concurrent main29cf18 has separate published Home styling. Do not publish this local candidate wholesale over concurrent changes. No commit, push, merge, publish or real account mutations.

## Where

Teacher Home > Students at a glance > Student accounts:
- Add session credits: named student, exact current/after balance, default1, whole1..50 sessions, explicit confirmation.
- Account access: name/email, Full/Basic/Customize, five feature switches, explicit confirmation and verified saved baseline.
- Individual booking links: existing private link reuse/copy/open/revoke; first link requires explicit initial1..50 sessions. Creating/opening a panel never itself grants credits or permissions. Anyone with private booking URL can book; fictional demo URLs were never opened/shared.

Credits are bookable sessions, not Stripe/payment ledger entries or feature grants. Existing safe backend writers reused; no migrations/edge edits. Additive credit receipt+operation key protections and CAS access save retained. Exact pending operations recover independently of roster eligibility; unreadable protection can only be cleared after named eligible account load+balance review+checkbox. Archived/admin accounts cannot receive fresh grants through picker. New openings clear prior account/amount, while pending recovery restores its exact intent. Link-mode race loads existing link with no added credits.

Assistant can perform a specifically authorized named-account change through the authenticated safe UI and verify readback. Legacy lsatu-admin.mjs supports read/dryrun/access, but its credit command is a one-session absolute-total update without operation-key retries; do not use blind retries or claim arbitraryN safe grants there.

## Evidence and limits

Actual browser evidence in BROWSER-CHECKS.md, with readable desktop1440, phone390/320 and dark screenshots. Actual synthetic add4→5, initialnewlink1, consecutiveaccessedits, no mutation onopen/select/cancel, searchfiltering, directrowblankselection and exactfocusreturn verified. Production Supabase client replaced beforemoduleevaluation by throwing Viteplugin in start-teacher-home-preview.mjs; actions in memory only. No real auth/student/RLS/all-student end-to-end or production credit/access writes exercised.

Independent Claude source reviews: initialREVISE defects addressed; final3 and signoff APPROVED with no material defects, observed claude-sonnet-5-5 (CLI default), not Opus. Final3 lowretry/validationcopy corrected and re-reviewed by signoff. The signoff low-severity post-success rearm advisory was corrected afterward with an explicit Add more sessions guard. Only TeacherAccessBooking.tsx and its test changed after the approved snapshot (post-review-delta.json). Codex read the guard and verified it in the rendered browser. This last guard was not sent through another Claude loop. Do not imply the reviewer executed tests or the backend.

Final check results recorded below when complete. Earlier superseded checks retained in logs; they do not prove the final snapshot. Existing largechunk/Tailwindduration/noise.png warnings remain. Unrelated supabase/functions/mcp/index.ts hash preserved5359c2de7a28b626a3d2523d83b6fbd3e1777a0d5a60bb9757ed4bb2ee446f26.

Final focused tests: 51/51 across TeachingDesk and TeacherHomeView, worker-guard-tests.txt. Exact final source hashes: source-final.json. Typecheck/build still running; results must be read before completion claims.

Final guard typecheck passed: guard-typecheck.txt EXIT_CODE=0. One full npm build is running sequentially afterward in guard-build.txt. Superseded incomplete check processes were explicitly stopped only by their recorded own PIDs; they are not failures attributed to application code.

## Final completion

Final source frozen and hashes rechecked unchanged. 51/51 focused component tests pass. guard-typecheck.txt explicit EXIT_CODE=0. Full npm build (prebuild + Vite + postbuild) passed, Vite1m57s; guard-build.txt postbuild scanned784files with no canonical guide content. No new tracked generated build assets. Remaining warnings are pre-existing Tailwind ambiguous utilities, unresolved noise.png runtime asset and chunk size. Final repeated-add guard source-read and actually exercised in browser after Claude signoff; no further application edits. No real student tests or production mutation/deploy.
