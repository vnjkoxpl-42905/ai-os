---
name: chat-export
description: "Export a conversation to a local Markdown file when explicitly asked to save or export the chat. Retrieve original session logs for a verbatim export; disclose missing ranges. Chat-only continuation uses session-handoff."
---


## Local execution contract (2026-10-10)

Save operational exports to the current project handoffs directory. A full verbatim export requires original session logs. If those are unavailable, export only visible context, label it partial and list missing/compacted ranges. Never reconstruct absent turns as verbatim.

## Workflow

# Chat Export Skill

Saves the current conversation as a structured markdown file to
`<current-project-root>/handoffs/` with a full transcript,
summary, and a paste-ready handoff prompt.

## Output path

```
<current-project-root>/handoffs/YYYY-MM-DD_short-title.md
```

Use today's date. Make the short title 3-5 words, kebab-case,
describing what the chat was about.

Example: `2026-04-28_claude-folder-cleanup-notebooklm.md`

## Steps

1. **Retrieve original session logs** for the requested conversation. Verify which turns are available and write retrieved user/assistant messages verbatim. If original logs are unavailable or incomplete, export visible turns only, label the transcript partial, and list missing or compacted ranges. Never reconstruct absent messages as verbatim.

2. **Write the structured summary** (see template below).

3. **Write the handoff prompt** — a single paste-ready block the user
   can drop into a new chat to resume instantly. It should:
   - Point to the file: `Read <current-project-root>/handoffs/<filename>.md`
   - State what was done
   - State what to do next (ask the user if unclear)

4. **Save the file** using an available host file-writing tool, then read it back and verify its coverage label and output path.

5. **Tell the user**:
   - The filename
   - The handoff prompt (show it in a code block so it's easy to copy)

## File template

```markdown
# <Chat title>

**Date:** YYYY-MM-DD
**Topic:** one-line description
**Tags:** (pick relevant: lsat-u | lsat-content | applications | tooling | drive-organizer | theology | general)
**File:** <current-project-root>/handoffs/<filename>.md

---

## Summary

One paragraph. What was this chat about, what was the goal, what was accomplished.

## What was decided / built

- bullet list of concrete outcomes, decisions, files created, commands run

## Open threads

- things not finished
- questions still unresolved
- next steps

## Handoff prompt

> Paste this into a new chat to continue:
>
> ```
> Read <current-project-root>/handoffs/<filename>.md and continue
> from where we left off. [Specific next thing to do goes here.]
> ```

---

## Transcript (complete or partial, with coverage)

### User
[message]

### Codex
[reply]

[Repeat for every retrieved message; list unavailable ranges above.]
```

## Notes

- Preserve all retrieved turns. A partial source must remain explicitly partial; report unavailable ranges.
- The "Open threads" section is the most important part for handoffs —
  be precise about what is unfinished.
- If the user specifies a subfolder (e.g. "save this under lsat-u"),
  save to `<current-project-root>/handoffs/lsat-u/<filename>.md`
  and create the folder if it doesn't exist.
- After saving, always show the handoff prompt in a fenced code block
  so the user can copy it in one click.
