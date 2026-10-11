---
name: chat-export
description: "Export a conversation to a local Markdown file when explicitly asked to save or export the chat. Retrieve original session logs for a verbatim export; disclose missing ranges. Chat-only continuation uses session-handoff."
---

# Chat Export Skill

Saves the current conversation as a structured markdown file to
`C:/Users/Joshu/dev/ai-os/handoffs/` with a provenance-labeled transcript,
summary, and a paste-ready handoff prompt.

## Output path

```
C:/Users/Joshu/dev/ai-os/handoffs/YYYY-MM-DD_short-title.md
```

Use today's date. Make the short title 3-5 words, kebab-case,
describing what the chat was about.

Example: `2026-04-28_claude-folder-cleanup-notebooklm.md`

## Steps

1. **Retrieve transcript evidence.** Prefer the host's original conversation export/log for this exact session. Record source path, session identifier, available range and exclusions (tools/attachments). If unavailable, export only messages actually visible in context and label it `Visible-context export, incomplete history`. After compaction, a summary is not verbatim evidence: list unknown/missing ranges and never invent them. Use `### User` and `### Assistant` headings; preserve available message text exactly.

2. **Write the structured summary** (see template below).

3. **Write the handoff prompt** — a single paste-ready block the user
   can drop into a new chat to resume instantly. It should:
   - Point to the file: `Read C:/Users/Joshu/dev/ai-os/handoffs/<filename>.md`
   - State what was done
   - State what to do next (ask the user if unclear)

4. **Save the file** using an available local file-writing tool to the
   output path above.

5. **Tell the user**:
   - The filename
   - The handoff prompt (show it in a code block so it's easy to copy)

## File template

```markdown
# <Chat title>

**Date:** YYYY-MM-DD
**Topic:** one-line description
**Tags:** (pick relevant: lsat-u | lsat-content | applications | tooling | drive-organizer | theology | general)
**File:** C:/Users/Joshu/dev/ai-os/handoffs/<filename>.md

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
> Read C:/Users/Joshu/dev/ai-os/handoffs/<filename>.md and continue
> from where we left off. [Specific next thing to do goes here.]
> ```

---

## Transcript coverage

Source: <verified log/export or visible context>
Available range: <known range>
Missing sections: <none proven / explicit gaps / unknown earlier history>

## Available transcript

### User
[message]

### Assistant
[reply]

[Repeat for every retrieved message; list unavailable ranges above.]
```

## Notes

- Preserve all available verified messages, chunking file writes when needed. Do not call the export complete without original-history coverage evidence.
- The "Open threads" section is the most important part for handoffs —
  be precise about what is unfinished.
- If the user specifies a subfolder (e.g. "save this under lsat-u"),
  save to `C:/Users/Joshu/dev/ai-os/handoffs/lsat-u/<filename>.md`
  and create the folder if it doesn't exist.
- After saving, always show the handoff prompt in a fenced code block
  so the user can copy it in one click.
