---
name: pickup
description: Load LSAT U project state from the Obsidian vault only when Joshua explicitly asks for pickup. Never run automatically at session start. Reports open tasks. Trigger with /pickup or an explicit request to run pickup.
---

Load the current LSAT U / Aspiring Attorneys project state from the Obsidian vault so this session can continue immediately, with no re-explaining from Joshua. Be fast and terse. Brief, then wait unless Joshua has explicitly asked you to continue the work.

## Resolve the current roots

Resolve the vault from the current session's root `AGENTS.md` / `CLAUDE.md`, not a saved home-directory path. Confirm the candidate with `git -C <candidate> rev-parse --show-toplevel` and the vault's `wiki/` directory. Resolve every vault-relative path below against that root.

If `projects/lsatu/LOCATOR.md` exists in that vault (historically `Projects/lsatu/LOCATOR.md`), read it and verify its app path. A missing locator is expected after relocation and does not block pickup. If the locator is missing or its app path cannot be verified, prefer the active LSAT U checkout named in the current session: verify its Git root, repository instructions, and remote identity (`vnjkoxpl-42905/lsatu-684d89db`). If no active checkout is supplied, use the application-code routing in the current vault instructions and verify that candidate the same way. Do not substitute an old Mac path or invent a checkout. If no app root can be verified, disclose that and continue the vault briefing.

Resolve app-relative plan/handoff pointers against the verified app root and vault-relative pointers against the vault root. Use an explicit absolute pointer only if it exists; a stale pointer remains unresolved rather than being silently rewritten.

## Steps (in order)

1. Resolve the vault and app roots as above, then read `wiki/tasks.md` first. This is the living ledger of what is in progress (`## Now`), queued (`## Next`), and finished (`## Done`, struck through). The open items here are the spine of the briefing.
2. Read `wiki/hot.md` (last-session handoff cache).
3. Read `wiki/dashboard.md` (product ground-truth).
4. Skim `wiki/index.md` to learn what pages exist. Do NOT crawl individual pages.
5. Read only the most recent entry in `wiki/log.md`.
6. **Resume pointer.** Check `wiki/hot.md` (its `## Resume here` block, if present) and the `## Now` items in `wiki/tasks.md` for a reference to an active plan or handoff file (a path under `~/.claude/plans/`, the repo `docs/implementation-plans/`, or a handoff doc). If one is named, read THAT file and pull its Context + the immediate next step/stage. This is the one exception to "read lazily" — an active plan is exactly where we left off, so open it. If the file is missing or stale, say so and fall back to the ledger.

Do not read deeper synthesis/concept pages yet. Pull those lazily only when Joshua points at a specific task. The goal is orientation per token, not loading everything.

## Output: a briefing, then stop

Emit 6 to 8 lines, then wait for Joshua unless his current request explicitly includes continuing the work.

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
- End by waiting unless Joshua has already asked you to continue. `/wrapup` is the mirror skill for session end.
