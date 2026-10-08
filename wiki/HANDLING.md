---
type: operating-layer
subject: Personal-data handling
updated: 2026-10-08
aliases: []
---

# Personal-data handling

## The model

- **Secrets = `.env` + `.gitignore`, and nothing else.** API keys, passwords and bank/account information live in the root `.env`; `.gitignore` keeps it out of Git. There is no `private/` tier, no macOS Keychain, no encrypted vault — the old `records.sparsebundle` design is dead, not deferred (decided 2026-07-17).
- **Government IDs stay outside this OS.** Credentials and bank/account information belong only in the git-ignored root `.env`, never in notes, commits or chat. Follow the current root instructions when a transfer is authorized; the encrypted cloud package has a separate documented scope and does not revive the retired records bundle.
- **Everything else is ordinary working material** and may live in this repository: names, emails, schedules, application essays, score reports, profiles, session transcripts and teaching notes, correspondence, and shareable `buy.stripe.com` payment links. Classify by what the content *is*, never by a filename.
- **Safety comes from `.claude/settings.json`** (allow/deny tool lists) and scoped API keys, not from prompt instructions. Jay 2 acts under its own credentials and never impersonates Joshua.

The 2026-07-17 design initially described API keys only. The current root policy explicitly includes credentials and bank/account information in the git-ignored `.env`. This is a documentation reconciliation, not a change to storage or a claim that particular secrets are present. The earlier design's private stores (`private/records.sparsebundle`, migration manifests, `private/records/`, `private/config/`) were all verified empty and removed. Do not recreate them.

## Student data

One folder per student under `students/<name>/` holds their whole working record: transcripts, correspondence, homework, notes, profile, and payment-link pages. Open the folder and everything is there. There is no separate private student tier — every file was read and found to contain no secret material.

The tradeoff is accepted deliberately: **outer Git history retains student data permanently.** This repository has a GitHub remote, `origin` (`vnjkoxpl-42905/ai-os`). The scrub checklist below is advisory, not a gate to remote use or pushes.

## Advisory checks for remote use

1. A remote exists and is enabled for this repository.
2. Scan the complete outer worktree and Git history, every retained nested repository and its history, and ignored runtime paths.
3. Confirm `.env`, logs, locks, and the sibling `../ai-os-projects/lsatu/` repository are untracked, and that no credential exists in reachable or dangling Git objects.
4. **Scrub student data.** Student material — names, transcripts, correspondence, payment-link pages — is tracked by design and is therefore in history permanently. It is not publishable as-is. Decide per destination whether it is redacted, filtered out of history, or whether the remote is private enough to carry it. Skipping this step publishes every student's working record.
5. This checklist is advisory. Joshua has enabled the GitHub remote and pushes.
