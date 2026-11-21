# Backup failures repeatedly captured the same changed files

Audit date: 2026-10-23. Read-only operational inspection; no capture, upload, deletion, or scheduled-task mutation.

## Verified cause

`setup/backup/new-machine-backup.py` selects the most recent **complete** matching-scope baseline. After core generation `20261009-202545`, socket errors left later core captures incomplete, so changed files kept being archived against that old baseline. SQLite databases are always snapshotted. `new-machine-run.py` skips incomplete captures for upload. Neither script implements pruning; the handoff claim that successful upload would trigger pruning is false.

Latest failed core `20261021-190002` has exactly two errors: Codex `app-server-control.sock` and `daemon-updater.sock`, both EINVAL. On this actual Windows filesystem, `Path.stat()` reports regular-file mode `0100666` but reparse tag `0x80000023` (AF_UNIX). A regular-file check alone would fail to fix the actual bug.

54 manifests record 462.43 GiB of archives. The 19 failed core captures account for 428.67 GiB. Repeated SHA256+size content across failed core captures totals 420.17 GiB of redundant **uncompressed** file bytes, not a recoverable/compressed-space estimate. Manifests do not account for all local disk occupation.

## Existing core cloud chain verified against live Drive metadata

Using gws only, paginated folder listings compared each receipt ID, MD5 and byte size. Core `20261009-202545` matched 43/43 files. Its nine-generation dependency closure matched all 269 files, with zero missing or mismatched entries. Detailed results: `backup-cloud-readback.json` beside this document. This does not establish a current restore test, actual downloaded byte verification, or exhaustive discovery of newer unreceipted cloud generations. Latest locally receipted personal capture is `20261021-203152`; its full chain was not remotely checked in this audit.

## Bounded repair

`new-machine-backup.py` now skips nonregular entries and Windows AF_UNIX-tagged files before opening them. Genuine read failures remain manifest errors. Default reserved free space is 20 GiB, checked before generation creation, during writes and before SQLite snapshot creation. A reserve breach aborts capture rather than continuing disk exhaustion. This is a reserve guard, not a complete upfront capacity estimate. SQLite may grow while snapshotting; failed partial archives remain preserved. No full capture acceptance test was run.

Original script preserved outside source at `C:/Users/Joshu/LaptopBackups/repair-source-copies/20261023-020930/new-machine-backup.py`.

`new-machine-retention-plan.py` has no deletion capability. It calculates the transitive manifest dependency closure for latest locally receipted complete scopes and lists other generations for review only. A passing planner is not cloud proof or deletion approval. Actual removal requires independent live chain proof, restore verification and approval of exact paths.

## Checks and commands

- `Path.stat()` on both exact live Codex socket paths: confirmed AF_UNIX tag and regular-file mode; repaired exclusion recognizes both.
- `compile(source, path, 'exec')`: repaired capture syntax passed.
- Isolated AST extraction of `require_headroom`, invoked with `minimum_free=10**20`: raised the intended RuntimeError.
- `python setup/backup/new-machine-retention-plan.py --stage C:/Users/Joshu/LaptopBackups/2026-10-07`: exit 0, 34 protected generations and 20 review-only generations.
- `gws schema drive.files.list` and `gws schema drive.files.get`: consulted before reads.
- Remote verification method: `gws drive files list --params` with `q=trashed=false and <receipt folder_id> in parents`, `fields=nextPageToken,files(id,name,size,md5Checksum)`, `pageSize=1000`; follow nextPageToken, compare all receipt IDs/size/MD5.

No permission-failure injection, full capture, archive download/restore, cloud write, deletion or scheduled-task mutation was performed. Repair is implemented with focused checks, not fully operationally accepted.

## Independent review follow-up

Review identified that SQLite WAL contents can exceed the source main-file size. Repair now checks pinned `PRAGMA page_count * page_size` before snapshot writes and checks reserved headroom in each SQLite backup progress callback. A real temporary WAL database regression produced 4,726,784 logical snapshot bytes while the source main file was only 4,096 bytes; assertion that logical bytes exceed twice main-file size passed. The temporary test used Python `sqlite3`, WAL mode, disabled autocheckpoint, and 1,024 committed 4 KiB rows.

Midcapture low-space failure now records the real error and breaks capture, closes ZIP, runs existing CRC/SHA validation, and writes an incomplete manifest. Initial preflight still fails before making a generation. The planner separately lists directories lacking manifests as review-only. Interrupted processes, hardware failure and an already exhausted disk can still prevent finalization. Full injected capture regression has not been run.

Persisted focused test command: `py -3.12 setup/backup/new-machine-safety-checks.py`. Exit 0: reserve rejection, committed-WAL divergence and both actual Windows AF_UNIX tags passed. This tests safety primitives and observed file types, not a complete capture.

Parent agent additionally invoked the actual core capture CLI with the existing stage and default 20 GiB reserve using Python 3.12. It refused at initial reserve preflight without creating a generation. This verifies fail-fast on the current low-space machine; it does not establish successful backup acceptance.

## Actual archive inspection and historical preservation

`20261021-190002/payload.zip`: 48,240,161,191 bytes. ZIP membership matches all 262,581 own-generation manifest records, no missing/unrecorded entries or size mismatches. Full `ZipFile.testzip()` completed with no CRC error; details `newest-failed-archive-check.json`.

Earlier failed generations contain historical revisions not represented by the latest snapshot. For example, Oct20 has 655 own key/SHA256/size records differing from the newest manifest. Every earlier failed core has some such history. Therefore uploading only newest failed core cannot justify deleting all older failed archives. Preserve those archives remotely first, or explicitly adjudicate historical-version loss. Metadata-only comparison is recorded in `failed-core-historical-coverage.json`.

Pending failed-core archives lacking local cloud receipts total 453,797,488,002 bytes (422.6318 GiB). Existing receipted archive/part duplicates are separate potential headroom and require matching live checksums before offload.

Optional `new-machine-salvage.py` was implemented but no derivative created. It defaults to validating source and dependencies, with explicit `--create` required for a new complete historical derivative. It validates exact runtime errors and actual AF_UNIX tag, whole archive SHA256, per-file SHA256/size and ZIP CRC through reads, and leaves original manifest unchanged. The chosen preservation workflow can keep incomplete archives as-is instead. Validation command started: `py -3.12 setup/backup/new-machine-salvage.py --generation C:/Users/Joshu/LaptopBackups/2026-10-07/20261021-190002 --report research/computer-health/2026-10-23/newest-failed-sha-validation.json`. SHA validation result is pending until that report exists. Syntax and refusal of unexpected/empty error lists passed.

SHA validation completed successfully, exit 0: **341,443 required file records across ten archives** (262,581 newest-own plus 78,862 inherited) matched per-file SHA256, size and ZIP CRC. Every archive whole SHA256 matched its original manifest. Source manifest bytes were checked unchanged afterward. Detailed report: `newest-failed-sha-validation.json`. No derivative was created.

Metadata-only inventory `receipted-local-payloads.json` totals 85,459,250,968 local payload/cloud-part bytes across 36 already-receipted generations. These are potential headroom only after independent live proof. Sorted smallest-first records support bounded offload sequencing. This inventory does not authorize deleting non-payload files or source roots.

## Interrupted 2026-10-22 archive

`20261022-190004` has no manifest; `payload.zip` is 46,988,392,284 bytes. Opening its ZIP central directory fails with `BadZipFile: File is not a zip file`. Matching `run-20261022-190003.log` records 346,000 captured files followed by Errno 28 (disk full) while `zipfile.close()` tries to finalize its central directory. The next personal capture also failed writing machine-info with Errno 28. No full CRC was attempted because the ZIP directory is unreadable. Preserve these opaque original bytes and snapshots before local removal; this is not a valid conventional restore point. Specialist ZIP recovery may salvage contents later.

Independent uploader test rerun: `python -m unittest discover -s tests -p test_new_machine_cloud.py -v`: 13 tests passed, including interrupted opaque preservation without original-byte mutation. Independent snapshot-offloader review identified prior-eviction proof binding and coordinator snapshot-only skip issues, sent to coordinator owner before actual cleanup; follow-up fix status belongs to owner.
