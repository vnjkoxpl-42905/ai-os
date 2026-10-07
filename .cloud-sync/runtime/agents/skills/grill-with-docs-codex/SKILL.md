---
name: grill-with-docs-codex
description: "Codex-host entry point: Codex handles independent review or scoped delegation. Interview and review a plan with persistent context, a glossary, and architecture decisions using the current Claudex loop. Compatibility entry point for the former document-backed grilling workflow."
---

## Installed direction: Codex to Codex

This copy is for the Codex host. The current Codex conversation coordinates. Use `host=Codex` in the shared runner. The default independent reviewer and cross-provider handoff target is Codex. Preserve explicit user provider/model choices and authorized scope. For the loop, the host builds by default and the other provider inspects; the build compatibility entry point separately selects the other provider as builder.

# Grill a plan and preserve its decisions

Read and follow `../claudex-loop/SKILL.md` before proceeding. That sibling skill is the authoritative workflow, including its references and CLI runners. Resolve its supporting paths from the sibling skill directory.

Treat the user's request and arguments as inputs to that workflow. Use its document-backed context support: read existing CONTEXT.md or CONTEXT-MAP.md where relevant, retain a clear glossary, and record material architecture decisions using its context and ADR formats. Update existing documents rather than creating competing versions. Keep context proportional to the task.

Start with its requirements interview when requirements are unresolved. If the user requests review of an existing plan, use its review mode. Preserve the user's authorized scope; a request to interview or review does not authorize implementation.

Use the actual host runtime to select roles. In Codex, Codex coordinates and Codex reviews. In Codex, Codex coordinates and Codex reviews. Follow the current loop's model selection, validation, and inspection rules.

This name is maintained locally as a compatibility alias. Do not load or restore the upstream legacy implementation.
