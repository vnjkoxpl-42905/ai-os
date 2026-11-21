# Restore the saved data on another computer

Download the complete recovery folder from Google Drive first. Keep all numbered `.7z.001`, `.002`, and later volumes together with `CLOUD-VERIFIED-SHA256SUMS.txt`. Install 7-Zip yourself. The helpers do not install software or sign into accounts.

Both helpers check every file listed in the cloud-verified manifest, test each active archive, and extract into a new staging folder. Their default mode changes no application/profile files. Keep the cloud originals and extracted staging evidence.

## Windows: restore the core data after closing the apps

From an external PowerShell terminal:

```powershell
powershell -ExecutionPolicy Bypass -File .\restore-recovery-windows.ps1 -BackupFolder 'C:\Users\YOURNAME\Downloads\laptop-recovery-2026-10-04'
```

After reviewing the extracted files, close Codex and Claude, including terminal agents. Run again with `-Apply` to copy the core runtime folders, second brain, development folders, and personal files into your current Windows profile. A fresh staging folder is made each run.

```powershell
powershell -ExecutionPolicy Bypass -File .\restore-recovery-windows.ps1 -BackupFolder 'C:\Users\YOURNAME\Downloads\laptop-recovery-2026-10-04' -Apply
```

Existing conflicting files are preserved under a new `preexisting-before-restore-*` folder before being overwritten. Source files and directories are never deleted. Stale locks and SQLite sidecars are not copied. Existing SQLite sidecars are preserved away from replacement databases. The final Codex delta is applied last when present.

The helper stages `app-data`, `additional-profile`, and `sqlite-live-raw` but does not apply them. Additional profile data preserves VS Code/Antigravity extensions and Supabase configuration for manual review. Raw SQLite is forensic recovery evidence, not a replacement for consistent database snapshots. Windows AppData needs app-specific review, with the app closed. Restored credentials can be machine-bound; sign in again where required.

## Mac: restore portable data and keep Windows evidence intact

From Terminal:

```bash
bash ./restore-recovery-mac.sh "$HOME/Downloads/laptop-recovery-2026-10-04"
```

Close Codex and Claude before requesting portable-data application:

```bash
bash ./restore-recovery-mac.sh "$HOME/Downloads/laptop-recovery-2026-10-04" --apply
```

Mac application restores `~/dev/ai-os`, its sibling development folders, personal documents, activated skills, Claude history, and portable Codex sessions/assets. Existing conflicting files are preserved locally first.

Windows AppData, native binaries, Codex databases, runtime credentials, and Windows-specific configuration remain in staging. This preserves all backed-up evidence without automatically inserting Windows paths into a Mac database. Chat transcript files are restored; automatic appearance of old chats in the Mac app sidebar is unverified and requires application-specific migration.

## Reconnect the working environment

Install Codex, Claude, Obsidian, Git, Node/Python and the tools you use. Open the restored `dev/ai-os` folder in Obsidian and Codex. Keep application repositories outside the vault at `dev/ai-os-projects`.

Review references to `C:\Users\Joshu`, Windows executable paths, PowerShell commands, browser profiles and drive letters before enabling hooks or automations on either new computer. Mac paths start at your actual `$HOME`; do not globally replace text inside databases. Restore app dependencies from each project's lockfile, then reconnect Google Workspace, GitHub, browser sessions and other accounts.

A saved data backup is not an operating-system image. App installation, sign-ins, machine-bound credentials, path repair and Mac chat-sidebar migration remain necessary. The helpers have not been applied to the original laptop.
