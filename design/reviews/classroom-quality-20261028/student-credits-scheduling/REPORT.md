# Student credits and teacher scheduling

2026-10-28. Local candidate in C:/Users/Joshu/dev/ai-os-projects/lsatu-my-work-20261026, base 18fc8af7. No commit, push, publication, production credit/booking/upload/email operations.

## Where to use it
Teacher Home > Students at a glance > Student accounts. Add session credits: choose student from an alphabetical deduplicated dropdown, quantity defaults to one, click Add sessions. Accounts without a pass use the same single explicit Add action. Success shows the verified balance and requires explicit new intent before adding more. Account access and Individual booking links remain adjacent.

Schedule a session: choose student, available day, offered time, then named confirmation. Uses the same shared booking components and server protections as student booking. No arbitrary time entry, hidden grant or teacher JWT impersonation. Confirmation states exact student, date/year/timezone, one-credit use and ordinary confirmations. Teacher quick booking excludes notes/attachments; student booking retains them. Successful booking refreshes agenda/access/booking queries.

## Verification
Host: 166 focused tests across15 files passed before final low fixes; then167 across15 passed after source fixes, plus6 scheduling UI tests including the added API-instance race regression. Counts overlap. Final typecheck/build result recorded separately in release-checks.txt.

Actual isolated browser: one credit added to fictional Celia and immediately available in Schedule; Lydia booking balance4 to3, taken time removed, upcoming session added. Cancel/open/select create no mutations. Lost response recovered with one simulated debit and one request. Unknown response retained student/time, neutral copy, picker lock, close/reopen restoration, read-only check and explicit checkbox/discard with zero mutations. Desktop1440, phone390/320, midwidth768; no horizontal overflow at phone widths. Light/dark screenshots opened. Reduced-motion preference exercised with controls operable. No real notification delivery or student RLS acceptance performed. Preview plugin blocks both production Supabase and public-booking adapter; fake APIs only.

## Claude review
Four plan reviews ended APPROVED. First final inspection REVISE, corrected accepted findings. Second final inspection APPROVED with four low observations, observed model claude-sonnet-5-5. Inspector source-only, did not execute checks or review screenshots. Scope and exact snapshot in inspect-round2/claudex-r55r69sg/result.json.

Two subsequent narrow corrections are host-tested and not independently re-inspected: reset discard readiness when recovery API changes, and preserve public student committed-replay behavior when backend omits the existing redemption row. Inspection budget2 exhausted. No assertion of zero remaining issues or whole-repository approval. Conservative unknown-create readback also applies to definitive refusals because the writer lacks a trustworthy refusal discriminator; this costs one explicit Add more action but prevents duplicate grants. Prior calendar/Home polish is intentional carry-over, not newly reviewed whole-feature acceptance.

## Release boundaries
Both admin-manage-users full-pagination source and booking-pass-admin identity-bound historical recovery source need separately authorized Lovable Cloud backend deployment. Production roster completeness and historical recovery are not accepted by local proof. Existing default response shapes and legacy history path retained. No new endpoint/migration. SessionStorage pending state is per tab, not a cross-window lock; server atomic debit/collision remains canonical. Future public booking info may exclude old rows, so changed bindings recover through exact student/pass/operation history, read-only.

Unrelated supabase/functions/mcp/index.ts preserved SHA256 5359c2de7a28b626a3d2523d83b6fbd3e1777a0d5a60bb9757ed4bb2ee446f26. Final source manifest FINAL-SHA256.json. Prior dirty branch contains other work; do not publish wholesale.

## Images
- [Finished schedule](schedule-finished.png)
- [Direct credits](credits-one-step.png)
- [Phone390](schedule-phone.png)
- [Phone320](schedule-320.png)
- [Dark](schedule-dark.png)

Detailed plan, recon, dispositions, tests and runner artifacts are adjacent.

## Final build receipt
Final application typecheck exit0. Full npm prebuild/build/postbuild exit0; postbuild scanned784dist files with no canonical guide content. Build emitted utility ambiguity, unresolved /noise.png and large-chunk warnings; no build failure. Scoped source manifest unchanged after build; unrelated MCP hash unchanged. Final git diff --check produced no output.

## Authorized main release, 2026-10-28
User authorized push to main. Candidate was ported surgically into current-main isolated release checkout, preserving PR246 paper masthead/launcher/quiet-work and all current sections. No older local calendar/layout replacement or unrelated MCP edit was included. PR248 merged as9b1eec11bde0746f899c34ec9b5d42630395bfe8; release160tests/15files, typecheck and full build/postbuild passed. Responsive320/390/600/768/1024/1440 checked. Free frontend deployment457150a6-9b17-4915-b567-bd97933fe9d7 requested only after exact Lovable SHA parity. Live acceptance pending in release/live-assets.json. Backend function deployment requires explicit Lovable-credit approval, requested separately.

Production frontend verified: custom domain changed from index-CHsLAXVg.js to index-CR2y-3ue.js with exact student-credits-scheduling-20261028 marker, Schedule a session and Add session credits strings. Initial Lovable UI Build unsuccessful warning conflicted with successful eventual publication; no duplicate deployment issued. Backend updates still await credit-spend approval.

Live read-only credit form: Celia existing balance1 active,70minutes,noexpiry; default Add1 preview1→2 rendered. No Add click occurred. Live student picker29entries, alphabetically ordered, read from existing deployed endpoint; full future-roster pagination still requires new backend deployment.

## Backend deployment completed, 2026-10-28
User explicitly approved minimal Lovable credits for the two-function deployment. One standard (max_mode=false) agent request umsg_01m62fqcadfjxrxmz6z3trq93x completed, reported cost2.5credits. Both admin-manage-users and booking-pass-admin deployed from exact9b1eec11 source; four pinned fileSHA256s matched. Deployment upload bundlehashes are host-reported, not independent deployedsource retrieval. Agent exceeded requested deployment-only scope by reinstalling missing preview packages and running preview/typecheck checks; no further paid requests sent. No source/settings/record changes reported; remote main independently remains9b1eec11 and live index-CR2y-3ue.js unchanged.

Independent read-only audit: current40rosteridentities unchanged and cover all40currentprofiles;34passes balances/status byte-equal;103redemptions byte-equal. Snapshot was taken while the deployment request was running, not a guaranteed pre-deployment transaction snapshot. Existing history operation read returns expected row and exactstudent/pass/keymetadata; wrong-student request rejects withoutredemptions. Both anonymous calls401. Wrong-student rejection currently usesHTTP500 rather than4xx (existing outer error classification); it failsclosed, recorded as minor API-status limitation, no additional paid fix. Future >200-account pagination is source/multi-page-test evidence; no syntheticproductionaccounts created. No real student write/notification test. Full receipts backend-lovable-receipt.json,backend-live-audit.json,backend-roster-coverage.json.
