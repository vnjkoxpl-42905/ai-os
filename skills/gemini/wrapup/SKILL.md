---
name: wrapup
description: Close an LSAT U session by updating the Obsidian vault so the next chat picks up cleanly. Marks finished tasks done (struck through) in the task ledger, refreshes the handoff cache, and appends to the log. Trigger with /wrapup.
---

Close the current LSAT U / Aspiring Attorneys session. Leave the next session a clean, accurate handoff and mark completed work as done so it is never re-run. Resolve the vault root from the current workspace and its nearest instruction files; never assume a saved `~/ai-os/`, Windows, or Mac path. In this vault, read `system/schema/llm-wiki.md` and obey its index/log conventions.

## Step 0: read the anchor

Before writing anything, re-read `wiki/tasks.md` and `wiki/hot.md` so the handoff reflects the real goal, not just the last thing touched. If a `plans/` file or README framed this session, skim it too.

## Step 1: confirm task status changes only when needed

From verified session work, determine whether task status changes are needed. If no task status changes are needed, leave `wiki/tasks.md` alone and continue with the authorized handoff and log updates without a confirmation step. If task status changes are proposed, show Joshua the concrete proposal before editing `wiki/tasks.md`:

```
Proposing for wiki/tasks.md:
  -> Done (strike through): <items you believe are finished this session>
  -> Stays in Now: <still in progress>
  -> New Next: <anything surfaced that should be queued>
```

Wait for Joshua to approve or correct proposed task status changes, unless those exact changes were already approved in this session. Completion MUST be correct: a wrong "Done" is the exact failure this prevents. Do not mark something done on a guess; if unsure, leave its status unchanged and say so. This gate applies to task status changes, not to routine authorized handoff/log filing. If requesting approval, explain that this skill requires confirmation before changing task status.

## Step 2: write the authorized handoff and log

1. **`wiki/tasks.md`** - move approved finished items into `## Done`, wrapping each in `~~...~~` with a date, e.g. `~~Wire AI tutor into official drill surface~~ (2026-06-12)`. Update `## Now` and `## Next` only as approved. Preserve older task records; do not prune or delete them without explicit authorization. Skip this file when no task changes were approved or needed.
2. **`wiki/hot.md`** - rewrite the `## Most recent (YYYY-MM-DD): <title>` block with 4 to 8 bullets of what changed. Refresh `## Active priorities` and `## Open threads` so they are true now.
3. **`wiki/log.md`** - append a new entry at the BOTTOM of the log using `## [YYYY-MM-DD] system | Session wrapup`. Include source/output links, meaningful changed pages, verified results, unresolved work, and any skipped steps. Use Joshua's client date/time context. Preserve old entries exactly, including their legacy formats; never rewrite or reorder them. Multiple sessions per day are normal, so add a distinct title suffix when useful. If this session's authorized handoff and log entry already contain the same verified work, report them rather than duplicating the entry.
4. **Task anchor** - if a README, plan, or wiki page advanced, make a surgical status update. Touch only what changed.

## Step 3: confirm, then stop

```
Handed off: <1 line headline of this session>
Tasks: <N marked done, M still in Now>
Logged: <the wiki/log.md entry label you added>
Next session starts at: <the top open item in tasks.md / hot.md>
```

## Rules

- No em dashes. Terse. Surgical changes only (Karpathy: touch only what changed).
- `raw/` is immutable; never write there.
- `pickup` is the mirror skill for session start; run it only when explicitly requested.
- Read current target contents before writing. Preserve unrelated changes. Unattended automation writes only generated files or fenced generated sections and uses compare-and-swap.
- Do not re-log unchanged events, invent completed work, or claim a commit/push occurred without verification.
