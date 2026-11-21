# Obsidian, storage and backup verification on 2026-10-23

This records the initial diagnosis and repairs. After Joshua subsequently authorized
Drive upload followed by local backup removal, the first verified offload reclaimed
79.59 GiB. Current execution status and remaining work are in
[upload-offload-status.md](upload-offload-status.md). The initial no-deletion and
low-free-space observations below describe that earlier phase.

## Confirmed causes

Obsidian's renderer crashed with V8 JavaScript heap exhaustion during native indexing, before community plugins loaded. A temporary 4096 MiB heap test remained slow and named a 38,082,494-byte generated Codex transcript under `setup/github-sync/state/conversations/codex/`. Generated chat Markdown accounts for approximately 473 MiB of the vault's 640 MiB of Markdown. This directly supports removing the generated cache from native indexing. The source chat sessions must remain preserved.

C: had approximately 8.8 GiB free of 952.4 GiB during this audit. LaptopBackups measured 585.889 GiB. A bounded performance-counter sample during the audit showed approximately 1–1.3 GiB available RAM and substantial paging. The low free disk space compounds system pressure; the observed Obsidian exception specifically establishes a JavaScript heap limit failure.

The latest failed core manifest examined, `20261021-190002`, records errors for two Codex AF_UNIX socket endpoints. Windows reports these as regular files with reparse tag `0x80000023`, so a regular-file check alone is insufficient. Failed runs continue baselining the last complete generation, repeatedly archiving changed files. Nineteen failed core manifests account for 428.67 GiB of recorded archive sizes. The runner has no pruning implementation. Antigravity's claim that successful upload would have triggered pruning was incorrect.

## Repairs and verified results

- Sync source now targets hidden `state/.conversations`, preserving cloud `.cloud-sync/conversations/` paths. Four migration regression tests passed. The reversible migration requires both existing sync locks, a closed Obsidian process, and complete pre/post hashes.
- The active scheduled sync timed out a long secret scan and began another scan. Main disabled new launches, stopped the scheduled runner, then terminated its remaining observed child publisher during scanning to release the lock. Temporary files were preserved. Migration verified all 818 generated files, 499,606,496 bytes, using complete pre/post hashes. Receipt: `setup/github-sync/state/conversation-cache-migration-20261023T062329.340042Z.json`. Scheduled sync was re-enabled and its Enabled=True read back; a later scheduled run started normally. This does not establish that subsequent publication succeeds.
- Normal-memory Obsidian launch completed native indexing. A direct screenshot showed the open vault with no indexing notice. A subsequent restart returned layoutReady=true, no notices and zero generated conversation exports in the file inventory. Renderer working set was approximately 853 MiB after restart versus approximately 2.4 GiB before the reproduced OOM. Restricted Mode was already on and remains on; community plugins were inactive in both failure and successful tests. Plugin-enabled performance and a real browser Web Clipper save have not been tested. A broad CLI full-text search was attempted but its result was not yet confirmed; do not claim search performance acceptance.
- Backup capture now explicitly excludes AF_UNIX endpoints and other non-regular files, checks a default 20 GiB free-space reserve, and checks SQLite temporary-space headroom. Actual socket classification and isolated headroom rejection checks passed. Full capture/upload not run because adequate headroom is unavailable.
- A read-only retention planner protects incremental dependency chains and cannot delete. Keeping just two newest generations would be unsafe without dependency verification.
- Latest complete core cloud receipt found locally is `20261009-202545`. Read-only live Drive metadata verification matched all 269 files in its nine-generation dependency closure by receipt ID, MD5 and size. No downloaded restore acceptance or exhaustive newer-cloud discovery was performed. See `backup-findings.md` and `backup-cloud-readback.json`.
- Whole-drive metadata inventory completed in 871 seconds: 2,606,110 files, 383,784 directories, 180 reparse entries skipped and 134 access-denied errors, with zero long-path errors. See `storage-inventory.json`. Logical bytes count hardlinked paths separately and do not represent exact allocated disk space. AppData measured 63.249 GiB, materially above Antigravity's estimate. Measurements do not establish that staging, downloads, recordings or old backup generations are disposable.

## Other observed issues and limits

The broad CLI full-text search subsequently completed with results and exit code 0. The vault remained ready with no notices on direct readback. Search latency was not measured reliably, so no speed claim is made.

Windows reported shadow-copy deletion/growth failures and three dllhost hangs involving PowerToys Explorer extensions. The physical disk reports Healthy. No hardware-failure conclusion is supported by these checks. No reliable battery-wear or update-compliance finding is established. The pagefile's 44.78 GiB allocation does not establish that it will automatically shrink after cleanup.

No user data or backup generations have been deleted. Generated cache files were renamed with hash verification. The cleanup question received a request for explanation, not approval. Original edited scripts have timestamped backups. No manual commit, push, or outbound message was performed; the preexisting scheduled sync has been restored. C: remained critically low, approximately 7.35 GiB free on the final volume check. A fresh successful core capture/upload remains blocked on adequate storage headroom. Backup repair independently reviewed; persisted safety regressions passed, including actual Windows sockets and WAL-aware SQLite reserve behavior. Keeping only two backup directories is not a safe retention policy for these incremental chains.
