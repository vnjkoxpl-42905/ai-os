# Claude Code -> Google Drive live sync: Brainstorm / Discovery Notes
Date: 2026-09-11 · Goal: decide how every Claude Code chat, skill, config, and the ai-os vault gets mirrored to Google Drive continuously so the MacBook Pro opens identical.
Status: in progress
Context sources: ~/.claude survey (this session), global CLAUDE.md, vault CLAUDE.md

## Facts gathered before the interview (verified on disk, 2026-09-11)
- Google Drive for Desktop is installed and running (GoogleDriveFS.exe), mounted as `G:\My Drive` (streaming mode).
- `~/.claude`: projects/ 367 MB (254 .jsonl transcripts across 7 project dirs), skills/ 55 MB, plugins/ 329 MB, settings.json, CLAUDE.md, file-history/, backups/, sessions/, shell-snapshots/.
- `~/.claude.json` 54 KB (holds MCP config + OAuth state; contains secrets by design).
- `~/.codex/` exists (auth.json, config.toml, sqlite logs).
- Vault `dev/ai-os` has `.gitignore` and `.obsidian` but **no `.git`** (not a repo). `projects/` holds the lsatu code repo.
- No rclone installed.

## Summary / key decisions
(running)

## Q&A log

## Open flags (pending input)

### Round 1
#### Q1 - Backup vs live shared state
- Asked: one-way continuous backup + restore, or bidirectional live state across machines?
- Recommended: (a) one-way mirror for ~/.claude, git for vault/skills.
- Captured (user's words): "my whole Claude code setup should be transferrable to a different laptop." "fire up another laptop I've never used, upload and download Claude code on that laptop, and be able to move because I might change computers soon." "In the last laptop, I lost all of my updates since I was a month out, a month and a half out-of-date, and I don't want that to happen again." "Everything that I've done, all my projects, all the tasks I've worked on, needs to be saved."
- Decision: the goal is **continuous full backup + clean restore onto a brand-new machine** (migration), not two machines writing the same files at once. Zero data-loss window is the priority; the previous loss was ~1-1.5 months.
- Also settles Q2: scope is *everything* (transcripts, skills, config, plugins, vault, projects), not a subset.
- Tentative: pairing with the MacBook was mentioned in the skill args, not by the user; the user's concern is machine replacement.
- Q3-Q6: not yet answered.

- Fact (from finished survey): vault is 19.2 GB total; `projects/` is 17.8 GB (lsatu repo + node_modules); vault minus projects ≈ 1.4 GB; `skills/` 54 MB.

### Round 2
#### Q1 - Cadence/mechanism
- Asked: 10-min scheduled mirror vs hourly vs logon-only.
- Captured: user does not know what robocopy is; asked for the options explained plainly. Wants "instantly" / "automatically synced" — the mental model is "open Google Drive on a laptop and Claude Code works perfectly from there."
- Status: mechanism still open, pending plain-language options (Round 3).
#### Q3 - Secrets
- Captured (user's words): "I want everything; I don't want you to avoid anything with MCPs, I want everything, .env, all of that. This is my private drive, so it doesn't matter."
- Decision: include secrets, .env, MCP config, auth files. (Concern noted in chat; user overruled.)
#### Q5 - Plugins
- Captured: include plugins too ("everything I have set up should instantly be there").
#### New scope items
- Superwhisper settings must be included ("all my settings, everything I have set up").
- Code repos: "maybe live repos are saved there" (tentative; user unsure how).
- Restore experience wanted: "open a new laptop, it should direct exactly what it is" — i.e. paths/config fix themselves.
#### Q2 (vault git), Q4 (new laptop OS), Q6 (restore test): not answered yet.

### Round 3
#### Q1 - Option choice
- Captured (user's words): "Just do option two. It should add everything up to date, including my AIOS on a new folder with everything new, all the stuff I've done, every skill, and everything else I've done. Make sure it's all there."
- Decision: **Option 2** (scheduled mirror into Google Drive). Also interested in git for vault + skills; asked whether GitHub is preferable to Drive and would create a private repo if so.
#### Q2 (lsatu repo), Q3 (OS), Q4 (restore test): not answered; proceeding on recommendations (b: copy minus node_modules; both scripts; test tonight) unless overruled.

## Summary / key decisions (updated)
- Goal: continuous full backup to Google Drive + one-script restore on a new laptop. Never lose more than ~10 min again.
- Mechanism: Windows Scheduled Task, every 10 min + at logon, mirror to `G:\My Drive\claude-code-backup\`.
- Scope: ~/.claude (all), ~/.claude.json, ~/.codex, Superwhisper settings, full vault, lsatu minus node_modules. Secrets INCLUDED by explicit user decision.
- Git for vault+skills: pending user's read of the tradeoff (below).

### Round 4 - go
- Captured (user's words): "go and build it." Drive folder must be "easily identifiable ... like a README doc"; the old copy should say "don't download" and point to the new one. "Also, do the plus git for the vault + skills."
- Decision: GitHub AND Drive (different jobs: Drive = whole-machine restore, GitHub = history/merge). User accepted.
- Built 2026-09-11:
  - `setup/backup/backup.ps1`, `restore.ps1`, `restore.sh`, `install-task.ps1`, `README.md`, `README - START HERE.md`
  - Drive: `G:\My Drive\CLAUDE-CODE-BACKUP - START HERE\` + top-level pointer file; old `AI-OS` renamed `_OLD AI-OS (Aug 2026) - DO NOT USE` with marker file inside (nothing deleted).
  - GitHub: private `vnjkoxpl-42905/ai-os`, initial commit 9b1a3aa, 6,691 files; ignores projects/ raw/ tmp/ .firecrawl/ .env.
  - Scheduled task "Claude Code Backup": every 10 min + at logon.
Status: build in progress (first full run + restore proof pending)
