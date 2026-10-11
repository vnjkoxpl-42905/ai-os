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

1. Resolve the vault and app roots as above before opening project-state files.
2. Read `wiki/tasks.md`. This is the living ledger of what is in progress (`## Now`), queued (`## Next`), and finished (`## Done`, struck through). The open items here are the spine of the briefing.
3. Read `wiki/hot.md` (last-session handoff cache).
4. Read `wiki/dashboard.md` (product ground-truth).
5. Skim `wiki/index.md` to learn what pages exist. Do NOT crawl individual pages.
6. Read only the most recent entry in `wiki/log.md`.

Do not read deeper synthesis/concept/plan pages yet. Pull those lazily only when Joshua points at a specific task. The goal is orientation per token, not loading everything.

## Output: a briefing, then stop

Emit 6 to 8 lines, then wait for Joshua unless his current request explicitly includes continuing the work.

```
Where we left off: <1 line from hot.md / tasks.md "Now">
Now (in progress): <the open ## Now items from tasks.md, terse>
Next (queued): <top 1-3 ## Next items>
Open threads: <anything blocking or unresolved>
Hot right now: <the single most recent thing>
Suggested next: <one concrete action>
```

If `wiki/tasks.md` does not exist yet, say so and offer to seed it from hot.md, then fall back to the old 4-line briefing (hot.md, dashboard.md, index.md, log.md).

## Rules

- No em dashes. Terse. Opinionated.
- `raw/` is immutable; never read it for knowledge (read `wiki/`).
- This is scoped to LSAT U work only.
- End by waiting unless Joshua has already asked you to continue. `/wrapup` is the mirror skill for session end.
