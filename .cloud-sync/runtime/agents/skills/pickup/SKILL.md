---
name: pickup
description: Load LSAT U project state from the Obsidian vault only when Joshua explicitly asks for pickup. Never run automatically at session start. Reports open tasks. Trigger with /pickup or an explicit request to run pickup.
---


## Local execution contract (2026-10-10)

Run only on explicit pickup request. Resolve current checkout/handoff/remote and current native memory, never assumed ~/.Codex/plans or projects/lsatu. An explicit continue request authorizes unfinished scoped work; do not force a second permission pause.

## Workflow

Load the current LSAT U / Aspiring Attorneys project state from the Obsidian vault so this session can continue immediately, with no re-explaining from Joshua. Be fast and terse. Do NOT start doing work after this; brief, then wait.

Vault root: `~/ai-os/`.

## Steps (in order)

1. Read `wiki/tasks.md` first. This is the living ledger of what is in progress (`## Now`), queued (`## Next`), and finished (`## Done`, struck through). The open items here are the spine of the briefing.
2. Read `wiki/hot.md` (last-session handoff cache).
3. Read `wiki/dashboard.md` (product ground-truth).
4. Skim `wiki/index.md` to learn what pages exist. Do NOT crawl individual pages.
5. Read only the most recent entry in `wiki/log.md`.
6. **Resume pointer.** Check `wiki/hot.md` (its `## Resume here` block, if present) and the `## Now` items in `wiki/tasks.md` for a reference to an active plan or handoff file (a path under `~/.Codex/plans/`, the repo `docs/implementation-plans/`, or a handoff doc). If one is named, read THAT file and pull its Context + the immediate next step/stage. This is the one exception to "read lazily" — an active plan is exactly where we left off, so open it. If the file is missing or stale, say so and fall back to the ledger.

Do not read deeper synthesis/concept pages yet. Pull those lazily only when Joshua points at a specific task. The goal is orientation per token, not loading everything.

## Output: a briefing, then stop

Emit 6 to 8 lines, then wait for Joshua. Do not begin work.

```
Where we left off: <1 line from hot.md / tasks.md "Now">
Now (in progress): <the open ## Now items from tasks.md, terse>
Next (queued): <top 1-3 ## Next items>
Open threads: <anything blocking or unresolved>
Hot right now: <the single most recent thing>
Resume at: <active plan/handoff file path + the exact next step, or "none" if no active plan>
Unresolved: <open questions carried in from the last handoff that still need Joshua, or "none">
Suggested next: <one concrete action>
```

The `Resume at:` line is what makes a fresh chat land exactly where the last one stopped: it names the plan file and its next stage so Joshua does not re-explain. Omit it only when there is genuinely no active plan.

If `wiki/tasks.md` does not exist yet, say so and offer to seed it from hot.md, then fall back to the old 4-line briefing (hot.md, dashboard.md, index.md, log.md).

## Rules

- No em dashes. Terse. Opinionated.
- **Carry open questions forward.** If the handoff or `hot.md` you are resuming from lists open questions, they go on the `Unresolved:` line and get re-asked before any new work starts. They do not silently roll forward, and they are never assumed resolved just because time passed.
- **Do not restate stale state as current.** A handoff's "verified state as of HH:MM" was true then. If a claim about a live system (deploy, DB, what was sent) is load-bearing for the next action, re-check it and say you did; otherwise mark it unverified in the briefing.
- `raw/` is immutable; never read it for knowledge (read `wiki/`).
- This is scoped to LSAT U work only.
- End by waiting. `/wrapup` is the mirror skill for session end.
