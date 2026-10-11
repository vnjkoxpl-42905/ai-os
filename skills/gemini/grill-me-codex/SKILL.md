---
name: grill-me-codex
description: "Claude-host entry point: Codex handles independent review or scoped delegation. Interview the user about a plan, then use the current Claudex loop for independent review and optional implementation. Compatibility entry point for the former grill-me-codex workflow."
---

## Gemini host boundary

Use the current shared runner/CLI contract. Claude-native browser, task and hook tools named in the reference are available only when actually exposed; otherwise use the supported host route and report unavailable operations. Keep project paths relative to this registered root.


## Installed direction: Claude to Codex

This copy is for the Claude host. The current Claude conversation coordinates. Use `host=claude` in the shared runner. The default independent reviewer and cross-provider handoff target is Codex. Preserve explicit user provider/model choices and authorized scope. For the loop, the host builds by default and the other provider inspects; the build compatibility entry point separately selects the other provider as builder.

# Grill a plan with the current Claudex loop

Read and follow `../claudex-loop/SKILL.md` before proceeding. That sibling skill is the authoritative workflow, including its references and CLI runners. Resolve its supporting paths from the sibling skill directory.

Treat the user's request and arguments as inputs to that workflow. Start with its requirements interview when requirements are unresolved. If the user requests review of an existing plan, use its review mode. Preserve the user's authorized scope; a request to interview or review does not authorize implementation.

Use the actual host runtime to select roles. In Codex, Codex coordinates and Claude reviews. In Claude, Claude coordinates and Codex reviews. Follow the current loop's model selection, validation, and inspection rules.

This name is maintained locally as a compatibility alias. Do not load or restore the upstream legacy implementation.
