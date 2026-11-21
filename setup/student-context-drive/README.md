# Private student context copies

This tool copies the 23 named current student folders from `students/` into a private business-account Google Drive folder named **LSAT U - Student Context**. It does not move, delete, share, edit or convert the original files. Former students and system folders are excluded.

Run from the AI OS root:

```powershell
python setup/student-context-drive/copy_students.py
python setup/student-context-drive/copy_students.py --apply
python setup/student-context-drive/copy_students.py --verify-existing
python -m unittest discover -s setup/student-context-drive -p 'test_*.py'
```

The first command scans every candidate file for common credential markers and writes `inventory.generated.json`, with SHA256/MD5 hashes and sizes. `--apply` verifies the signed-in Drive account, searches for the exact managed root in My Drive, verifies private permissions and copies each file. No dependency install is needed; Python standard library and the authenticated `gws` CLI are used.

`copy-state.generated.json` saves stable Google folder and file IDs after each verified operation. Re-running checks existing content and skips identical copies. A same-name unmanaged folder, ambiguous file, changed remote content, changed source or public/shared permissions stop the run. Conflicts remain preserved for a human decision. The tool never replaces a remote version. A lost response can be recovered through the next exact-parent/name search and checksum verification.

Every uploaded file must match the remote MD5 and byte count. At completion, one file is downloaded into a temporary restore folder and its SHA256 must match the source. Local originals remain in place. These generated manifests contain internal paths and Drive IDs, not credentials; treat them as internal records.

Operations use at most four concurrent workers. Folder permissions are checked once per folder during each run, before uploading files. Atomic progress writes use a shared lock. Read-only requests retry transient failures twice; create requests are never automatically retried after an unknown outcome. Resume instead, so exact-parent lookup can recover an already-created item without making a duplicate. `student-folders.generated.json` supplies the stable student slug to private Drive folder mapping for Home integration.

`--verify-existing` validates a saved managed root and a `running` or `complete` status before any provider call. It finishes verification from an already complete per-file verified manifest: it requires matching local SHA256/MD5/size for every source file, checks the root and restored sample file permissions through Drive, downloads that sample and checks SHA256, and rechecks root privacy. It does not upload files or re-query every remote file. A full `--apply` run rechecks remote file MD5/size and folder permissions. Drive's CLI requires both upload and download paths to be relative to their process directory; this tool sets that directory explicitly.

All `*.generated.json` manifests in this directory are ignored by Git. They remain private local working records and are not part of a code commit. Do not manually add them to a commit.

This is an initial copy and safe repeatable reconciliation tool, **not continuous synchronization**. It does not create a timer, publish Home, change student access, import Calendar events or automatically produce recaps. Home automation is a separately verified integration. The root's private permission status is checked at each run; never share this root with students.

## Connect the verified folders to Home

Copy safety checks reject linked source roots, student folders, nested symlinks/junctions and resolved paths outside the student root. Windows requires the native `gws.exe`; `.cmd` shims are rejected so filenames stay subprocess arguments rather than shell commands. Credential checks include common JWT, OpenAI/Anthropic, AWS, Google OAuth refresh-token and Slack token shapes. Binary files are byte-scanned only; compressed PDF or archive contents are not decoded by this tool.

File-transfer regression tests cover lost-response adoption, changed remote content, moved IDs, unmanaged and duplicate names, checksum failure, no-create second runs, and unchanged source bytes. Windows junction rejection is tested with a temporary real junction. Actual symlink cases can skip when Windows does not grant symlink creation; deterministic guard tests still cover source, student and file levels.

`connect_home.py --app <absolute-LSAT-U-checkout>` authenticates using the existing ignored environment files, reads the live admin roster, and writes a dry-run `home-import.generated.json`. It uses each student's authored primary email, requires one eligible app account, and leaves unmatched, archived or duplicate identities unresolved. It does not change access or create student accounts.

The initial copy must be complete, its root and folder IDs must match the copy manifest, and a restore sample must have passed. After the new backend is deployed, `--apply` rechecks the Drive account, private folder permissions and managed folder ancestry, then imports only folder identifiers and verified identity metadata. It reads the saved links back and compares every student ID, local slug and folder ID exactly. Any failure exits nonzero; importing links does not activate the background schedule.

Generated manifests are ignored by Git. Keep them locally for safe resumption; they contain private paths, student emails and provider IDs. The scripts never print credentials or save access tokens. Backend activation instructions live in the app's `docs/ops/teacher-post-session-setup.md`.
