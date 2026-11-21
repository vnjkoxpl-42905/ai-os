# Backup upload and local removal on 2026-10-23

## Completion verified, 2026-10-25

Approved cleanup worker state is `complete`, with no remaining offload failures and empty stderr. It finished at 2026-10-25 01:26 America/Toronto. Fresh core 20261024-211629 uploaded successfully as a complete restore point; its cloud chain was verified and a real downloaded sample checked before historical discard. All 39 generations in the latest core/personal dependency closure were protected and cloud-verified.

Nine failed historical payloads were discarded (335,922,457,339 bytes). The tenth reviewed payload, 20261014-200506, finished uploading and was instead removed through the verified preservation offloader. Additional verified offloads covered fresh core and its required baseline. Total removed by this approved worker: 423,140,639,218 bytes, approximately 394.08 GiB, including matching SQLite working copies. Current C: free space read 537.38 GiB. The job preserved manifests, cloud history and unrelated recovery originals. Evidence: `C:/Users/Joshu/LaptopBackups/2026-10-07/APPROVED-TEN-HISTORY-CLEANUP.json` and its recorded discard audit plus per-generation `OFFLOADED.json` files.

## Current continuation status, 2026-10-24

The background PID 21348 described below has exited unsuccessfully. It is historical launch evidence, not the current job. Current coordinator PID 2620 is preserving historical generation 20261014-200506 through uploader PID 27808; progress is in `C:/Users/Joshu/LaptopBackups/2026-10-07/run-20261024-192547.log`.

Fresh complete core 20261024-211629 exists locally but has no verified cloud receipt yet. Its required dependency 20261023-174504 had 198/374 matching Drive parts, leaving 21.95 GiB to upload, followed by the fresh core's 6.23 GiB. A separate direct uploader, PID 14252 at launch, now prioritizes that chain with per-generation locks and BelowNormal priority. Logs: `C:/Users/Joshu/LaptopBackups/fresh-core-priority-20261024.stdout.log` and the corresponding `.stderr.log`. Fresh personal 20261024-213612 already has a verified cloud receipt and its payload was offloaded. The fresh core chain remains pending until live verification completes.

Volume free space was 131.37 GiB at this continuation's first read. Remaining local payload archives totaled 439.27 GiB and SQLite working snapshots 27.97 GiB. These are observed values, not guaranteed final amounts.

Ten failed historical payloads outside the newest restore chains total 336.54 GiB. Joshua approved the pending conditional cleanup with "handle that" on 2026-10-24. No conditional deletion has executed yet. Exact review targets: `research/2026-10-24/backup-failed-history-discard-plan.json`. A separate bound plan and guarded cleanup CLI have been prepared; nine isolated checks and independent review passed. Applying it requires confirmed plan identity, idle coordinator/upload locks, full live cloud chain verification and actual payload hashes. Metadata and snapshots remain preserved. Coordinator parent 2620 was identity-checked and stopped to prevent additional historical uploads; both existing uploader children 27808 and 14252 were left running.

The uploader now reports sanitized structured failure categories and bounded transient retries with 2/8-second delays. Nineteen focused checks and live read-only account/error diagnostics passed. Old logs lack enough detail to prove the original HTTP failure cause; current account/quota checks succeed. Existing active upload children retain their loaded code; the priority fresh-core child uses the updated code.

Approved cleanup worker launched as PID 42644, BelowNormal, with the exact bound plan SHA `b0b0908f68c950c4d17e03d8048047de103a40907ab7b8363a7fcc65b39ad9c5`. Read-back state confirmed `waiting-original-uploaders` with both original uploader creation identities bound; stderr was empty. It waits for both uploads, retries only transient fresh-core failures, verifies the fresh cloud core, offloads that core through the existing real-download verifier and requires bound restore-sample evidence before historical discard. Then it rechecks all fresh core/personal dependencies and hashes all remaining exact approved targets under locks before removal. Receipt-bearing or already absent targets are skipped; receipt-bearing payloads and the three named fresh-chain generations use the existing verified offloader. Seven worker and ten guarded-discard checks pass; independent review covered the original worker and discard safeguards. Actual completion is not yet confirmed. Persistent state/log: `C:/Users/Joshu/LaptopBackups/2026-10-07/APPROVED-TEN-HISTORY-CLEANUP.json` and `.log`. Console errors: `C:/Users/Joshu/LaptopBackups/approved-cleanup-20261024.stderr.log`.

Targeted non-backup inventory is saved under `research/computer-health/2026-10-24/targeted-storage-inventory.json`. Recovery staging is 54.06 GiB and includes conflict originals; the largest temp directory is an active 8.74 GiB GitHub sync workspace. Neither was deleted. One 217 MiB installer duplicate is hash-proven, but unrelated deletion remains unapproved.

Joshua explicitly authorized uploading backups to Google Drive, then removing their verified local copies.

## Completed

- Actual newest failed core archive membership and full integrity verified: 341,443 file records across ten archives passed SHA256, size and CRC checks. Original manifests remained unchanged.
- First real offload pilot passed full local/remote checks and a downloaded restore sample before deletion.
- The first full offload pass exited successfully: 79.59 GiB of local payloads and duplicate upload chunks removed across 36 previously uploaded generations. Every generation retained manifests, checksums, receipts and restore tools. Evidence is each generation's `OFFLOADED.json` and `C:/Users/Joshu/LaptopBackups/2026-10-07/run-20261023-025559.log`.
- C: had 87.05 GiB free after that pass, compared with approximately 8 GiB before it. Other running processes can change volume free space.
- A new, non-personal verification probe `20261023-025822` passed an actual new upload, remote download/hash verification and local removal. It has scope `verification` and cannot replace a core/personal baseline or restore index.
- Google Drive account was verified as contact@aspiringattorneys.com; its 5 TiB quota had adequate headroom. The backup root's permissions showed only that account as owner.

## Script changes

`new-machine-cloud.py` stages one 128 MiB part at a time, resumes matching cloud parts, verifies archive identity and live remote dependencies, checks quota and writes bound cloud receipts. It supports explicit preservation of incomplete and unindexed captures without claiming they are complete restore points. Fourteen focused uploader tests passed.

`new_machine_offload.py` verifies exact fixed stage paths, no reparse paths, local archive/part hashes, matching remote account/file identity/checksum/size/location and a downloaded sample. It writes evidence before and after deletion. Only proven backup payloads/parts and matching archived SQLite working copies are eligible. Twelve focused offloader tests passed. New snapshot-only eviction evidence binds the archive identity, metadata hashes and downloaded sample; legacy proof lacking this binding preserves snapshots as pending.

The coordinator reclaims existing verified copies before capture, uploads each scope before starting the next, publishes current complete restore points before the historical backlog, and preserves interrupted/unindexed bytes separately. Maintenance-only runs do not label an old backup as a fresh successful capture. The existing scheduled task uses the updated script; its description was updated without replacing its triggers or account.

## Background run in progress

PID at launch: **21348**, Python 3.12, BelowNormal process priority. Main read back that the process existed and was processing generations. This is an active run, not a claim that all uploads or a fresh complete capture have finished.

- Arguments: `new-machine-run.py --resume-core C:/Users/Joshu/LaptopBackups/2026-10-07/20261021-190002`
- Progress: `C:/Users/Joshu/LaptopBackups/2026-10-07/run-20261023-032345.log`
- Console: `C:/Users/Joshu/LaptopBackups/drive-offload-20261023-032345.stdout.log`
- Errors: `C:/Users/Joshu/LaptopBackups/drive-offload-20261023-032345.stderr.log`

It reuses the validated historical core data as a partial baseline while rescanning current source files. The capture rechecks the base ZIP before reuse. It uploads required dependencies before declaring a complete current cloud capture. Historical failed captures remain incomplete in their original manifests.

At launch, unreceipted failed-core payloads totaled 422.63 GiB. Two no-manifest payloads add 53,463,537,291 bytes. The 2026-10-22 payload is not a usable ZIP: the matching log proves Errno 28 during finalization. Explicit opaque preservation sends its original bytes without representing them as a valid restore point. Unrecorded snapshot files and unknown files remain local pending proof; they are not blindly removed.

Closing the laptop or network interruption can interrupt a request. No local archive is eligible for eviction without a verified cloud receipt; matching cloud chunks are reusable on rerun. The scheduled coordinator retains its lock while active, preventing concurrent backup runs. No unrelated downloads, recordings, migration staging, source files, or Google Drive files were deleted.
