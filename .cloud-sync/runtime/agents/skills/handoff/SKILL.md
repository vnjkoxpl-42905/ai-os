---
name: handoff
description: "Use only when the user explicitly selects handoff or its specific documented preset/reference. Does not trigger on generic current-vault, frontend, AI or everyday workflow requests."
argument-hint: "What will the next session be used for?"
disable-model-invocation: true
---


## Local execution contract (2026-10-10)

Legacy handoff is explicit reference only. Current project session-handoff owns runtime handoff behavior and handoffs destination. Preserve useful templates without automatic competing triggers or source mutation.

## Workflow

Write a handoff document summarising the current conversation so a fresh agent can continue the work. Save to the temporary directory of the user's OS (`$TMPDIR`, else `/tmp`; `%TEMP%` on Windows) - not the current workspace.

Include a "suggested skills" section in the document, naming which skills the next agent should call the Skill tool for.

Do not duplicate content already captured in other artifacts (specs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.

Redact any sensitive information, such as API keys, passwords, or personally identifiable information.

If the user passed arguments, treat them as a description of what the next session will focus on and tailor the doc accordingly.
