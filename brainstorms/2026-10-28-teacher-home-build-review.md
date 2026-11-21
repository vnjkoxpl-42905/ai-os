# Full Home implementation review

Joshua authorized the full approved dashboard build and main/frontend release on 2026-10-28. Lovable backend credit confirmation remains separate. Baseline `d42e0ddf`; full pending Home release baseline `e4035d9c`. Approved plan SHA256 `2cc1f4f713b3918fbb426e4f38b6e498254bf91d4717e471b1f10223bebc3740` remains unchanged.

## Inspection 1 and fix round 1

Claude CLI default, observed `claude-sonnet-5-5`, returned REVISE. Result: `C:/Users/Joshu/.codex/verification/2026-10-28-teacher-home-build/claudex-o8_2rwqi/result.json`. Scope: complete pending Supabase changes, Home action helpers and two database harnesses. Snapshot `2635703667f8d9dfa17f964c42fa1b4a180111b65e08cd1ca6017cf88cac4566` is the diff hash, not final approval. Reviewer did not execute tests and explicitly did not read test bodies or UI; those limits remain explicit.

- F1 accepted: creating a link against an existing pass now rejects visibly and opens its current balance for an explicit additive action. No automatic second write.
- F2 accepted: attention means review, never grant authority. Return offer/live-mode context and explicit non-grantable status; the existing backend action owns final eligibility. Exclude test-mode activity from production Home.
- F3 accepted: replace isolate-memory agenda continuations with signed self-contained cursors and distinct error codes. Remove roster caching so identity/access/folder changes are re-read.
- F4 accepted: admin authority rather than historical pass creator; exact receipt replay before eligibility checks; serialized read-only pending-operation resolution. Unknown-outcome keys remain actor-scoped until verified. Corrupt pending data requires fresh balance readback and explicit quarantine before clearing; never silently lose an unknown operation.
- F5 accepted: owner-scoped operation UUID for manual create with payload-conflict detection. Retain the draft operation across retries.
- F6 accepted error mapping and database returned-tier assertion. Retain the short transaction's SHARE lock on user_roles: locking only the actor role row does not protect against a concurrent target admin-role insertion. This is a deliberate correctness tradeoff.
- F7 accepted: bounded paged email read with explicit lower-bound metadata; specific scope errors. Reject event relabeling while a durable task exists, preserving work rather than silently deleting it.
- F8 accepted: shared input matcher tests for agenda/worker. Root expands disposable DB checks to more than 100 tasks/history rows and thousands of payment rows, including stable page ties and private account boundaries.

No product contract is superseded by these corrections. Current source tier rules remain five configurable doors, Tier 3 Messages and Schedule, derived Review and retired flags off. Historical broader tier notes do not authorize widening access.

The first attempt at inspection 2 was deliberately terminated before a verdict when the UI worker reported two remaining contract defects: missing consultation source-change status and an inconsistent crowded fixture. Its Python process 43200 and children were stopped. That abandoned snapshot carries no approval or completed inspection result. The final inspection must start fresh after those corrections; this is recorded as an aborted attempt, not a passing review.

## Render review 1

Root opened all six Taste fold/page images at 1440, 768 and 390, plus the desktop expanded session state in the browser. Initial first phone action starts about 50% down the usable preview viewport after removing its lab toolbar. Top issues: count badges have insufficient contrast; action text needs a 14px floor; payment window and unconfigured enquiry empty-state wording need clarification. UI worker is correcting all three.

Taste measured zero FAIL and two WARN. Warm low-chroma paper is the selected approved material, so the palette warning is deliberate. Content-fit work/agenda columns intentionally differ in height; forcing equal-height blank panels conflicts with the approved app brief. Final rebuild/screenshots are still required. Sample navigation geometry is a preview, not signed-in production acceptance.

## Completed inspection 2 and final fix round

`claudex-q2v3daib/result.json` returned REVISE, observed Claude Sonnet 5.5. No high findings, one medium (expired pass recovery), five low findings. Its scope manifest was complete, but the reviewer explicitly did not read most UI components, CSS or tests. This is not independent UI approval. The two completed inspection budget is exhausted; final fixes receive host verification, not another independent approval claim.

- Accept F1: explicit expiry reactivation preserves the same private link and every existing credit, then a separate intentional Add operation.
- Accept F2: resolving a never-applied unknown operation must record a cancellation tombstone under the same operation lock. A delayed original request cannot apply after that resolution. Do not rely only on the absence of a receipt.
- Accept F3: preserve the original private manual-task operation and payload until a verified result. Editing a failed draft must not silently allocate a fresh operation UUID.
- Accept F4: 120-second provider focus freshness and 15-second explicit retry throttling, with tests.
- Reject F5's expanded mail-authentication requirement. The approved contract matches exact recorded sender addresses; it does not certify cryptographic identity. The UI does not claim such verification and no email classification authorizes a write. Naive SPF/DMARC filtering could hide legitimate forwarded mail; mail-authentication policy is separate scope. The lower-bound count visibility correction is accepted and implemented.
- Reject F6 table-lock removal for the same documented target-promotion insertion race. A lock on the actor's existing role row cannot lock a nonexistent target admin-role row.

Root verification before final-round edits: 171 Home/helper tests passed, 18 Deno tests passed, expanded desk SQL harness 48 checks passed, production build/postbuild passed. These results are snapshot-specific and require affected reruns after the final fixes.

## Render review 2

Root opened all 11 generated images at 1440, 980, 768, 390 and 320. Zero FAIL, two deliberate warnings as above. Count contrast and action-size corrections are visible. The Taste 320 viewport was only 200px high, so root separately inspected actual 320x844 through browser emulation and captured it. No horizontal overflow at 320 or 390. At 390x844 with reduced motion, the first action's measured usable ratio is 0.5795. All content remains visible under reduced motion.

Additional browser states exposed a preview-only empty-count inconsistency and native mobile select auto-zoom. Correct empty fixture totals and use 16px mobile form fields; then inspect the final build. Crowded fixture uses 12 real session records and eight manual records, capped on Home. Keep raw failed captures as evidence rather than silently replacing them.

## Main release checkpoint, 2026-10-28

Full approved Home landed on main at b6deac33bc82265f4949fa954bfbee2c3919eaf7. Concurrent Finder PR244 was merged with the role dispatcher and resolved actor permission gate preserved; read-only explorer integration review found no further changes. Combined tests passed 312/313; the sole RC expansion failure passed all 29 tests in an isolated rerun without code changes. Merged production build/postbuild and safe-push typecheck passed. Preview build passed. Final booking sheet light/dark screenshots were opened and legible. Access sheet DOM bounds were correct, but browser compositor captures were inconsistent, so those screenshots do not certify final access-sheet visual review.

Lovable latest_commit_sha matched main before free deploy_project call. Deployment 8ef40a3e-1994-4bca-b323-41af5b7da9f1 returned pending. Live custom domain currently still shows the older student-like Home with index-Ts4r9CBV.js; publication is not yet proven. Backend credit confirmation is pending; no migrations/functions/import/scheduler activation were executed. Final source fixes were host-tested, without another independent Claude approval.

## Frontend publication verified

After the pending deployment propagated, signed-in https://lsatprep.study/classroom?release=b6deac33 showed data-role-home=teacher and Teaching desk. Production entry changed to index-DO1jUJBR.js. Actual live Messages and recent student activity loaded. Backend-dependent sections honestly showed setup/errors; no automation acceptance is claimed. Screenshot saved at .taste-skill/full-home-browser/published-teacher-home.png. Backend credit confirmation remains pending.

## Authorized backend attempt, 2026-10-28

Joshua approved Lovable credit use for backend setup. Run umsg_01m61j8x5jfjss58azxvv7dsp5 completed stopped after the first exact migration, managed as 0040_teacher_post_session. Cost reported: 8.8 credits. Desk migration rolled back on text=uuid: production profiles.class_id and section_history.class_id are TEXT, whereas the local fixture modeled UUID. Host independently queried and confirmed these types. No functions deployed, secrets set, folder imports or scheduler activation. Five base tables remain empty/disabled. Calendar OAuth secret names exist; direct Gmail three names are absent. Follow-up local schema correction and production-type harness checks underway. This is a host validation defect; original local green checks did not certify real schema compatibility.

## Production schema repair released

Independent live schema audit confirmed all referenced existing columns, UUID-only has_role signature, booking wrapper parameters/composite return type, profile/tier trigger behavior. Fixed profile comparisons with UUID-to-text casting and safely joined auth.users for results to avoid casting arbitrary legacy text IDs. Added 20261028090000_teacher_home_profile_identity_repair.sql for the already-applied base; the desk/access migrations remain unapplied and corrected in place. Historical managed0040 preserved. Corrected fixture types: profiles.class_id/section_history.class_id/stripe_payments.offer_id TEXT. Host reran 57 partial-deployment repair checks, 56 fresh-install checks, 30 access/booking checks: all pass. Production build/postbuild and safe-push typecheck pass. Main 2d6c74b90ba304a3cb1cc505ad41fdee73be2cf1. Auth broker/bun changes preceding managed0040 were inspected separately; no critical regression found, production remains on localStorage. No final independent Claude approval is claimed. New bounded backend retry awaits fresh immediate credit confirmation after the8.8credit stopped run.

## Backend activation and display boundary fix

Authorized retry umsg_01m61m5vz7ejgre55dsj7jjaw8 completed at 12.5 credits; cumulative two-run cost21.3 credits. Managed migrations0041/0042/0043 independently compared to corrected source after line-ending/trailing-whitespace normalization: exact. All six checked private tables have RLS. Anonymous access to all checked functions denied; authenticated direct access to imports/ticket/access/credit helpers denied. Host unsigned worker POST returned401. Exact17folder mapping independently compared equal. Single active job382 uses pinned endpoint and single-use ticket auth, schedule */5 * * * *. Settings enabled with cutoff2026-10-28T16:15:30Z. Host verified five scheduled successes and worker last_success2026-10-28T16:40:03.380655Z/no error/zero tasks. Actual owner-authenticated agenda HTTP200 verified Calendar readiness, stronger than deployment agent's ticket inference. Student email returned truthful setup_required because direct Gmail credentials remain missing.

Live check exposed frontend crash on that exact HTTP200 email setup envelope with no threads. Host captured actual response metadata through browser CDP, with no credential/message-content output. Hotfix48acb651 separates setup envelopes, validates ready provider shapes and guards arrays.23 focused tests passed including actual payload. Updated local preview setup state rendered successfully. Preserved concurrent My Work release; focused integration audit found no role/refresh regressions. Merged production build/postbuild and typecheck passed. Main b0ceb239d184a8beb96d389fe0a1da9707baca1c; Lovable exact SHA verified before free publish6f3e10d2-1374-4f49-9931-d5f2f5f5a785, pending propagation at this checkpoint. Gmail secure configuration, six unmatched folder identities, actual post-cutoff ended-session creation and actual laptop-off acceptance remain incomplete. No real student content/access/credit writes or emails occurred.

## Final live verification

Free deployment6f3e10d2 propagated. Actual signed-in lsatprep.study/classroom?release=b0ceb239 now serves index-B31VFlty.js. Browser response body independently contains the new Invalid primary calendar response and Invalid student email response guards. Teacher marker and connected agenda/payment/results/task data render. Gmail setup envelope no longer crashes Home. Actual 1440x1000 desktop and390x844 phone screenshots were saved/opened: published-final-desktop.png and published-final-phone.png under .taste-skill/full-home-browser. Both viewport metrics match and no horizontal overflow. Task-history panel read returned0 active tasks; title/close color/bounds/hit testing and keyboard close verified. Portal screenshot compositor remained inconsistent, so no final screenshot certification of modal visuals. Restored browser metrics/media/page scale and retained live tab. No further source changes after successful build/typecheck. Remaining acceptance limits unchanged: Gmail secrets, six excluded account identities, actual new ended-session, laptop-off, signed-in student and production multi-connection contention. Final source fixes were host-tested, not independently Claude-approved.


## Approved visual restoration published, 2026-10-28

Joshua rejected the expanded Home's visual regression and explicitly approved restoring the earlier visual treatment while keeping the new teacher functions connected. Verified Taste v2 at C:/Users/Joshu/.agents/skills/design-taste-frontend/SKILL.md, upstream12af471f627f866411b4bd785b19646d3672784c. Kept Editorial greeting seed985551232 and the selected immutable dashboard material screenshot. Source comparison identified deliberate flattening in d67609a2, not loss from the My Work merge. Recovered presentation selectively rather than reverting functional work.

Restored light Fraunces greeting/italic personal name, charcoal Assign work launcher, warm paper contact/ambient depth,44px quick actions and hierarchy. Work plus correspondence use the main column; Calendar, decisions and payments use the rail. Student overview keeps the shared full-width edge. The greeting uses existing postSessionLede status logic, including paused/stale/catching-up/error states. Restored reduced-motion-aware press feedback. Preview now loads production font families. Actor keys, setup-envelope guards, forms, action callbacks, access/booking safeguards and all backend contracts retained.

Three host screenshot rounds,64 targeted tests on the merged checkout, typecheck, production build and postbuild all passed. Final full/empty Taste checks0FAIL0WARN with explicitly named approved material/type allowances; setup/error0FAIL1WARN for independent content-fit column heights. Opened all final fold/page sheets at1440/980/768/390 and state sheets.390px dark long-name render inspected; the inspector's320px viewport was only200px high, so a separate320x844 DOM check verified no page overflow and30px two-line title. Its sticky-toolbar compositor pixels were unreliable. Host critique7.8/10 is not independent jury or Claude approval. Read-only source reviewer verified fixes for truthful masthead status and the Messages touch target; no blocker remained.

Source2b81d9bd, merged upstream7eeb2e28 without Home conflicts, PR246 merged at29cf18a8d0fb0ef0c1106f8b976f26db13b9a3c4. Latest Lovable SHA matched exactly before free frontend publish5f675a4d-d421-4b22-9736-77cd92f46780. Signed-in custom-domain entry changed from index-CQImAh7y.js to index-CHsLAXVg.js; actual new bundle independently includes data-home-treatment, home-desk-launcher and retained student-email validation guard. Actual1440x1000 and390x844 production screenshots opened; no horizontal overflow. Masthead/main/student panel edges agree at1097px width. Actual glyph report confirms custom Fraunces regular/italic. All-task history read completed with0active session tasks; keyboard close and More menu targets verified. No assignment, email, recap, access or credit submission performed. Production images: .taste-skill/full-home-browser/restored-live-desktop.png, restored-live-phone.png and restored-live-full-desktop.png. Detailed critique: .taste-skill/paper-restoration-critique.md.

One user-owned live tab had moved to Inbox during work. Root reloaded it before noticing, disclosed the mistake immediately, restored its normal metrics and switched to a separate verification tab. No message was composed or sent. Verification tab metrics/media restored after inspection.

Existing backend limits unchanged: Gmail credentials still missing; six excluded student folder identities, actual future ended-session creation, laptop-off execution, signed-in student and production multi-connection contention remain unverified. No new paid Lovable action or backend change. Final runtime log review saw notification/homework/TA assignment background errors; the network recorded a canceled notifications request and no HTTP400+ response in the captured batch. Narrow baseline trace pending at this checkpoint; do not claim a clean console. Task ledger statuses unchanged.


### Background read follow-up

Narrow source review confirms the notification, homework-assignment and TA-assignment reads/loggers already exist unchanged in b0ceb239 and7eeb2e28; restoration adds no relevant reads or query invalidations. This establishes unchanged call sites, not proof that runtime failures occurred before release. Subsequent captured responses for notifications, homework_assignments and ta_assignments all returned HTTP200. The network history was truncated, so it cannot establish a full failure timeline or root cause. Do not claim a clean console. Current Home has no rendered alert, and private task-history read completed. No further source changes were needed for the visual restoration.
