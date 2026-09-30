---
name: grill-me-codex
description: Interview the user about a plan, then use the current Claudex loop for independent review and optional implementation. Compatibility entry point for the former grill-me-codex workflow.
---

# Grill a plan with the current Claudex loop

Read and follow `../claudex-loop/SKILL.md` before proceeding. That sibling skill is the authoritative workflow, including its references and CLI runners. Resolve its supporting paths from the sibling skill directory.

Treat the user's request and arguments as inputs to that workflow. Start with its requirements interview when requirements are unresolved. If the user requests review of an existing plan, use its review mode. Preserve the user's authorized scope; a request to interview or review does not authorize implementation.

Use the actual host runtime to select roles. In Codex, Codex coordinates and Claude reviews. In Claude, Claude coordinates and Codex reviews. Follow the current loop's model selection, validation, and inspection rules.

This name is maintained locally as a compatibility alias. Do not load or restore the upstream legacy implementation.
