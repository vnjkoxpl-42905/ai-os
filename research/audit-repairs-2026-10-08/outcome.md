# AI OS audit repairs and what remains

Repair pass: 2026-10-08. Current root: `C:/Users/Joshu/dev/ai-os`. Baseline: [full audit](../../audits/audit-2026-10-08-052114-f4a92b.md). The original report remains unchanged; this receipt records subsequent work. This is a repair outcome, not a new scored full audit or a claim that every document is factually verified.

## Repairs completed

- Shared Superwhisper glossary/corruption safeguards and configured-model tables agree across the scoped manuals. Shell-specific invocation differences remain intentional.
- HANDLING, protected-records and student conventions now agree with the current root credential/data policy. The old APFS bundle and private storage design are explicitly historical; no storage was recreated or moved.
- Current app/dashboard routes use the verified sibling repository. Missing old life-path/reform destinations are clearly historical/unavailable instead of being presented as working routes.
- Hot-cache empty-corpus and old deployment/test claims are dated appropriately. Connections was refreshed from actual reads, not from credential presence. A task-ledger freshness notice preserves recorded statuses without pretending all app tasks were reverified.
- Active/catalog GWS and Kling copies are reconciled without downgrading newer useful content. Pre-consultation scheduling is catalogued with its declared runtime exception. Validator and static smoke pass.
- Four legacy Codex review/build/interview names now route to the appropriate independent Claude workflow. Public triggers and compatibility behavior are documented in [PARITY](../../skills/PARITY.md).
- The declared Claudex upstream clone is restored, and useful Windows patches are explicit updater overlays. A successful update changed four global copies with zero conflicts; the subsequent offline dry-run reported zero changes/conflicts. This is manual repair evidence, not a future due-run receipt.
- Stripe financial access works through the existing API credential. The [safe account-read helper](../../system/scripts/stripe-account-read.py) verifies the live Aspiring Attorneys account without exposing secrets. The separate Codex Stripe connector still needs reauthentication if desired.
- Backup documentation points to verified complete scheduled generations and the matching cloud recovery guide.
- Wiki lint recognizes actual native memory/system targets and ignores inline examples. Seven surviving historical app documents were retained with hashes and a [human-readable recovery index](lint-cal-repair.md). Old wiki history was not rewritten, and deleted-worktree byte identity is not invented.
- Cal.com sweep distinguishes HTTP/API/JSON/schema/pagination failures from a truly empty complete result. It bounds requests/pages and deduplicates results. No cancellation or other live Cal.com write was performed.
- Sync runner retains atomic, bounded 200-event execution history with run IDs and explicit success/failure/deferred states. An independent review identified a child-lock false-success case; it was corrected so busy children skip Drive and record deferred. No active sync process was stopped.

## Verification

| Check | Result |
|---|---|
| Skill validator | PASS: 220 Claude / 205 Codex catalog entries, activations resolve, INDEX complete |
| Static discovery smoke | PASS: 19 Claude / 32 Codex project entries from root and student working directories |
| Wiki resolver regression fixtures | 4 passed |
| Cal.com read/error/pagination fixtures | 5 passed |
| GitHub/Drive/runner/runtime-export/discovery fixtures | 21 passed |
| Claudex permission/provider boundary fixtures | 7 passed |
| Claudex updater offline dry-run | 0 changes / 0 conflicts |
| Retained old-vault source hashes | 82/82 passed after repairs |
| Stripe API account read | Verified live Aspiring Attorneys, account `acct_1PJnXRIULVCj6rqq` |

**37 regression fixtures passed**, plus validator/static smoke and source-hash checks. Structural lint/index verification was repeated after final filing. These fixtures are isolated; no paid model review, booking cancellation, outbound message, task-status change or production deployment was launched to obtain a pass.

Current workflow samples have actual ingestion, recap and independent review outputs with correction/failure records. That is evidence of useful repeated work, not justification for deleting unused-looking skills. Global query/lint copies were updated, while contextual global ingest routing was preserved. Wider library equivalence and live duplicate-name resolution remain outside the proven scope.

## Cloud evidence and the comparison correction

An exact published snapshot comparison initially flagged eight of ten sampled files as different. Inspection established **newline normalization only**, not content drift: two matched byte-for-byte and eight matched after CRLF-to-LF normalization. All ten sampled files match the snapshot's text.

GitHub and the completed Drive receipt both referenced `095b87a5527b024061205c877dc9e4ce52286896`; live archive checksum/size matched that completed receipt. Machine-only [cloud evidence](../../setup/github-sync/state/audit-repairs/cloud-evidence.json) records the checks. Some later repair changes occurred after that snapshot; this receipt does not claim every final repair file is already included in a completed remote archive. Future completed receipts are the freshness authority.

The subsequent automatic runner ended at **2026-10-08T05:57:50.779875Z with overall failure**, GitHub child exit 1. Discovery blocked the newly restored third-party `claudex-loop` updater clone as `Unapproved remote`. AI OS publication nevertheless completed partially: its local Drive upload receipt records commit `c51f74f4efb1447074fac028ac04b2105e6c313b` at 05:57:43.933498Z, 718280590 bytes and MD5 `1a3745fc89ed13dcfa9d9103a64b2d20`. This later upload was not independently downloaded or asserted to contain every final repair.

Discovery now skips the known tooling clone before initialization or publishing and reports it explicitly as skipped. Its upstream remote was not approved or changed. Other unapproved remotes remain blocked; owned project discovery remains intact. Two new isolated discovery fixtures pass, bringing sync tests to 21 and the combined regression total to 37. No next cloud job was triggered or awaited, so a successful automatic run after this fix is still unverified. See the [machine-only repair receipt](../../setup/github-sync/state/audit-repairs/tooling-discovery-repair.md).

Encrypted original-context metadata was checked without displaying secrets or writing decrypted plaintext. Ordinary workspace snapshots still exclude raw archives. The separate old-vault source package and laptop backup have their own preservation contracts.

## Findings carried forward individually

| ID | Repair state | Remaining boundary |
|---|---|---|
| F01 | Original validator defect remains resolved | New divergence repaired under F15 |
| F02 | Previously resolved, maintained | Copy activation wording preserved |
| F03 | Support-only classification preserved | Full archived support-folder semantic audit not claimed |
| F04 | Repaired lint rules preserved | All global mirrors/live executions not exhaustively retested |
| F05 | Current browser dependency preserved | Live bulk transcription not run |
| F06 | Audit package naming remains correct | No change required |
| F07 | Bounded reconciliation completed | Wider global/catalog equivalence and fresh runtime precedence remain unverified; intentional differences documented |
| F08 | Useful selected workflow evidence retained | Whole-library usage adjudication not completed; nothing deleted from lack of evidence |
| F09 | Public triggers/compatibility aliases clarified | Generic interview and independent-review jobs intentionally remain distinct |
| F10 | Correct processing boundary preserved | No new conversation-history scan |
| F11 | Repaired | Shared scoped safeguards/table verified |
| F12 | Repaired | Current root policy authoritative; retired policy explicit |
| F13 | Repaired or explicitly unavailable historical route | Missing old personal/reform source was not fabricated |
| F14 | Repaired in sampled current pages | App backlog completion and all historical numeric claims were not individually revalidated |
| F15 | Repaired | Validator and smoke pass |
| F16 | Repaired, including two additional legacy aliases | Actual new paid reviewer execution not launched |
| F17 | Financial read access restored through API | Connected-app OAuth still requires user sign-in |
| F18 | Missing-source/updater defect repaired | Future scheduled due success still needs observation |
| F19 | Repaired | Dated full-scope backup receipt used |
| F20 | Structural navigation repair completed | Human recovery index required for retired direct worktree links; exact deleted-generation identity unverified |
| F21 | Pending desired monitoring state | Existing operations monitor remains deliberately PAUSED; Joshua's choice was requested, not assumed |
| F22 | Current disconnection established; selective plan prepared | Remote-only/phone content, remote preservation and actual phone connection remain pending |
| F23 | History/false-success repair completed; sampled cloud content verified | All final repair-file publication, two due successes under new history, and actual alert/recovery delivery not yet established |
| F24 | Hardened and fixture-verified | No live cancellation or write-side API migration |

## Three external decisions or checks remain

1. **Read-only operations monitor:** resume its existing monitoring or keep it paused. The current user's broad repair request did not silently override the earlier pause; a specific choice was requested.
2. **Obsidian phone sync:** the current 3 GB local vault is disconnected. The signed-in chooser lists the existing remote `Ai-os` at 968 KB. [Prepared selective-sync plan](obsidian-sync-plan.md) measures 83 MB of candidate working notes/images/PDFs and preserves the current structure. Remote preservation/comparison must precede joining; no remote contents were changed or old vault deleted. Joshua previously deferred Sync, so proceeding was explicitly offered rather than assumed.
3. **Web Clipper selected template:** installed Chrome/Edge versions are verified, but the browser security policy rejected extension-page access. Joshua was asked to confirm the actual template's current vault and `raw/inbox` destination. No alternate extension-page or raw storage workaround was attempted.

Stripe connector reconnection is optional for restoring that interface because the API route already works. Physical phone access and an encryption password must be provided in the Obsidian app when needed, not in chat.

No new folder architecture was imposed. Useful notes, sources and original migration records were preserved; historical decisions stay historical. The repaired local system is ready for the remaining checks, but this receipt does not claim that everything everywhere is synchronized or validated.
