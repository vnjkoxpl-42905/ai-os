---
name: resume
description: Continue from the most recent chat export or handoff doc without Joshua having to hand-type a path. Finds the newest file in C:/Users/Joshu/dev/ai-os/handoffs/ and, if in the LSATU repo, the newest file in docs/agent/handoffs/ and docs/implementation-plans/, reads it, and picks up from the last open thread. Trigger with /resume.
---

Continue exactly where the last session left off, without Joshua re-explaining or hand-typing a path.

## Steps (in order)

1. Find the newest file (by mtime) in `C:/Users/Joshu/dev/ai-os/handoffs/`.
2. If the current working directory is inside `C:/Users/Joshu/dev/ai-os-projects/lsatu/`, also find the newest file in `docs/agent/handoffs/` and the newest file in `docs/implementation-plans/**` (recursive, any depth) within that repo.
3. Compare mtimes across whatever set you found in steps 1-2. Read the single newest file in full.
4. If that file references a more specific active plan/spec (a path it names as "next" or "continue from"), open that file too — same exception as `/pickup`'s resume pointer: an explicitly named active plan is exactly where we left off.
5. If LSAT U work and `wiki/tasks.md` / `wiki/hot.md` exist in the vault (`~/ai-os/`), also check those for a `## Now` item or `## Resume here` pointer that corroborates or updates what the file says. Don't do the full `/pickup` ritual, just this cross-check.

## Output: a briefing, then stop

Emit this, then wait for Joshua. Do not start work.

```
Resuming from: <file path + date>
Where it left off: <1-2 lines, the last decision or state>
Open thread: <what was unresolved or the immediate next step named in the file>
Suggested next: <one concrete action>
```

If nothing was found in either location, say so plainly and ask what to resume, don't guess.

## Rules

- No em dashes. Terse.
- Never edit the source file being read; it's a record, not a scratchpad.
- If multiple files in `handoffs/` were written within minutes of the newest one (same session, chunked), skim the second-newest too and mention if it looks like a continuation set, but only fully read the newest.
- Don't crawl the whole vault or the whole `docs/agent/` tree, just the newest-file lookup above. This is a fast pointer skill, not a full audit.
