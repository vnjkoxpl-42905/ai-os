---
name: session-handoff
description: Use when Joshua says "session handoff", "hand off", "handoff summary", "summarize before I clear", or is about to /clear mid-work (especially near the ~250k dumb-zone). Produces a chat-only handoff — decisions, shipped changes, key files, running state, verification, deferrals, open questions — so a fresh agent (Claude or Codex) continues seamlessly. Distinct from `wrapup`, which updates the wiki ledgers; this writes nothing.
---

# Session Handoff

Produce a repeatable end-of-session summary so Joshua can `/clear` and start a fresh agent without losing continuity. The next agent should pick up by reading this summary alone.

This is a **context-handoff artifact**, not a status report. The audience is a future instance of you, not a stakeholder.

**Handoff vs. wrapup:** run `session-handoff` when the *context window* is the problem — nearing ~250k tokens (the dumb zone), or passing work between Claude and Codex. It is chat-only and writes nothing. Run `wrapup` when the *work day* is done — it strikes tasks, refreshes `wiki/hot.md`, and appends `wiki/log.md`. They can be run back to back (wrapup to persist, then handoff to reset).

## When to invoke

Joshua says: "session handoff", "hand off", "handoff summary", "summarize before I clear", or any near-equivalent. Note "let's wrap up" belongs to `wrapup`, not here — if he says that and the context window is also deep, run `wrapup` first, then offer this. Also invoke proactively if he says he's about to `/clear` without having run it, or if the session is clearly deep into the dumb zone.

## How to produce the summary

1. **Review the full conversation**, not just the last few turns. Handoffs miss things when they only summarize recent context.
2. **Pull state from these sources (in order):**
   - Plan files referenced this session; resolve the actual recorded path rather than assuming a runtime directory.
   - TodoWrite state — any in-progress or pending tasks.
   - Background processes started with `run_in_background` — shell IDs are load-bearing for the next agent.
   - Files created or modified this session — you know what you touched; don't grep to re-discover.
   - Memory files actually used this session. Codex guidance is under `~/.codex/memories/`; Claude native project memory is under `~/.claude/projects/C--Users-Joshu-dev-ai-os/memory/`. Do not invent a Codex project-memory path or update either store merely to produce a handoff.
   - Unresolved questions — things you asked Joshua that never got a clear answer, or things he asked that got deflected.
3. **Do NOT audit the filesystem.** This is synthesis of what happened in THIS session. No `git log`, no broad `Glob` sweeps. If you didn't touch it this session, it doesn't belong here.
4. **Produce the output in chat.** Do not write a file. Do not update memory. Chat-only.

## Output template — use exactly this structure, every time

```
# Session Handoff — <one-line title of what this session was about>

## Where it started
<2-3 sentences: what Joshua asked for, key framing or constraints that emerged>

## Decisions locked + what shipped
- <decision or change> — <why, and where it lives (absolute path if a file)>
- ...

## Key files for next session
- `<absolute path>` — <why the next agent should read this first>
- Plan file: `<path>` (if a plan drove the session)
- Memory files touched: `<paths>` (if any)

## Running state
- Background processes: <shell IDs + what they are + how to kill> — or "none"
- Dev servers / ports: <url + port> — or "none"
- Open worktrees / branches: <paths> — or "none"

## Verified state as of <HH:MM>
- <claim about live/system state> — <how it was checked, and when>
- <claim> — NOT re-verified this session; last confirmed <when>
- ...

## Verification — how to confirm things still work
- `<command>` — <expected outcome>
- ...

## Deferred + open questions
- Deferred: <item> — <why pushed to later>
- OPEN (must be resolved or re-asked before new work): <question needing Joshua's input> — <context>

## Pick up here
<1-2 sentences: the single most likely next action for a fresh agent>
```

## Hard rules

1. **Chat output only.** Never write the handoff to a file. Never update memory from this skill. (That is `wrapup`'s job, not this one.)
2. **Never invent state.** If a section has nothing to report, write "none" — do not omit the section. Structure stability is the whole point.
3. **Absolute paths always.** The next agent may have a different working directory, or be Codex.
4. **If a plan file drove the session, name it first** in "Key files" so the next agent reads it before anything else.
5. **No emojis, no hype, no "great job" summaries.** Terse and concrete — paths, commands, shell IDs, decisions. Tone of a seasoned engineer handing off at end-of-shift.
6. **Background process IDs are critical.** If you started any `run_in_background` shells, their IDs must appear in "Running state" with the kill command — the next agent cannot find them otherwise.
7. **Stamp verified state, and separate it from assumed state.** Read the current clock in the user's timezone and use the real time; on Windows use `Get-Date` with the applicable timezone conversion. Every claim about live systems (deploy status, DB contents, what was sent, what is published) is either something you actually checked this session — say how — or explicitly marked NOT re-verified. A handoff that presents stale belief as current state makes the next session re-derive everything, which is the exact cost this skill exists to remove.
8. **Open questions are obligations, not notes.** Anything under OPEN must be resolved by the next session or re-asked to Joshua before it starts new work. Requirements have been silently re-typed across sessions, and a promised artifact once never arrived because nobody re-asked. If a question was open in the handoff you are picking up from, it is the first thing you raise.

## Anti-patterns — do not do these

- Summarizing the last 3 turns and calling it a handoff.
- Listing files by relative path.
- Skipping "Running state" because "nothing is running" — write "none" instead.
- Writing the summary to any file. This is chat-only by design.
- Adding a "what went well / what went poorly" retrospective. This isn't a retro.
- Recommending next steps beyond the single "Pick up here" line. The next agent decides; you just hand off.
