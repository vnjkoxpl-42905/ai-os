# Connect the working knowledge after preserving the remote generation

Verified 2026-10-08 through the installed Obsidian 1.14.4 CLI and the current app's Sync settings. This is a prepared plan, not a completed connection or a change to the remote vault.

## What is actually connected

- Current local root: `C:/Users/Joshu/dev/ai-os`. CLI `vault` reports this exact path and approximately 3.05 GB of supported local content.
- Current Sync state: disconnected; its remote vault ID/name are unset. Enabling the core Sync plugin alone has not connected it.
- The signed-in remote-vault chooser lists `Ai-os`, North America, **968.00 KB**, created a month before the current inspection. It reports the maximum number of remote vaults already created. This is the account's existing remote, not evidence that this laptop's current vault syncs to it.
- The older local root remains `C:/Users/Joshu/Documents/Ai-os`. No file or setting in that source root was changed by these repairs.
- The installed CLI matches vault names without distinguishing the case-only pair: both `vault=ai-os` and `vault=Ai-os` returned the current root. Always read and verify the absolute path before an operation; do not use the second command to claim inspection of the old root.
- Google Drive and GitHub are separate publication/backup paths. Their success does not connect the phone.

The earlier account screenshot showed Sync Standard. Official [current plan limits](https://obsidian.md/sync) are one remote vault, 1 GB storage and 5 MB per file for Standard. The app's existing remote list confirms the remote count boundary, but this inspection did not read a new billing receipt.

## A practical candidate fits without moving notes

Keep the current folder tree intact. Sync its working notes and selected small images/PDFs, while retaining raw archives, source libraries, runtime code/catalogs and heavy evidence in the local/GitHub/Drive paths that already own them.

The read-only candidate scan found **1,599 files, 83,002,610 bytes**, consisting of Markdown, Canvas, Bases, images and PDFs outside the excluded domains. Every candidate was under 5,000,000 bytes. This is a point-in-time content estimate, not remote billed usage; version history, remote-only files and future clips can increase usage. Text-only candidates were 1,183 files / 30,378,321 bytes.

Candidate excluded folders:

```text
agents
archive
distillates
graph-imports
projects
raw/assets
raw/data-about-me
raw/sources
scratch
setup
skill-audit
skills
system
temp
tmp
```

`raw/inbox/` remains included so incoming clips can be seen across devices. The proposal excludes `system/attachments/` with the runtime system tree; any needed image there requires a narrower reviewed exclusion configuration before joining. The 83 MB estimate includes small images/PDFs already in the other included domains. It does not promise all attachments or source archives on the phone.

Sync images/PDFs only after reviewing required attachments. Leave audio, video and unsupported file types off initially. Hidden credentials stay outside ordinary Sync; explicitly confirm configuration categories separately. [Obsidian's selective-sync instructions](https://obsidian.md/help/sync/settings) state that exclusions and sync settings are per device, hidden folders are excluded except the configuration folder, and exclusions do not remove previously uploaded remote content.

## The safe sequence

1. Preserve a read-only download of the existing remote generation in a fresh staging folder before joining the current vault. The earlier 100-file migration covers the old laptop generation, not verified remote-only or phone-only content.
2. Compare that generation with the local migration coverage and preserve any remote-only content, including images. Do not delete or recreate the existing remote merely to change its contents.
3. Configure exclusions, file types and conflict-file handling on the current vault **before** allowing its first upload. Confirm the absolute root and encryption access in the app; never paste its encryption password into chat.
4. Connect the current vault to the existing remote, retain conflicting generations for review, and verify both the uploaded file list and storage usage. This has not been done during the repairs.
5. On the phone, sign into the same account, connect the intended local vault to that remote, configure device-specific exclusions and verify one current note plus one newly clipped note. Physical phone state cannot be inferred from laptop status.

If a remote export or encryption access cannot be established through available tools, Joshua must supply access in the Obsidian app. Do not claim remote completeness from the chooser's size.

## Web Clipper is separately pending

Chrome and Edge both have Web Clipper 1.7.1 installed. Automatic opening of Chrome's extension settings was rejected by the browser tool's security policy because `chrome-extension:` pages are blocked. No alternate browser or raw storage workaround was attempted after that rejection. The selected template/save destination is not verified.

Joshua should inspect the template he actually uses and confirm `raw/inbox` plus the current root. Case-only vault names are ambiguous in the installed CLI, so a recent clip's actual on-disk destination is stronger evidence than the displayed name. Existing recent Markdown clips in the current `raw/inbox/` support that route, but do not prove every template uses it.
