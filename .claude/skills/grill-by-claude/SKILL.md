---
name: grill-by-claude
description: Grill a plan with Codex, then get independent Claude Code review and revise against its findings. Use when the user asks to grill by Claude, grill with Claude, or reverse the Claude-to-Codex grilling workflow.
---

# Codex coordinates, Claude reviews

Read and follow `../claudex-loop/SKILL.md`, resolving that skill's references and runner paths from its own directory. Use the current shared workflow instead of duplicating its interview and review protocol.

This entry point explicitly selects Claude as the reviewer. In Codex, conduct the requirements interview, prepare the plan, and invoke the sibling runner's review command with `--host codex`. Claude Code independently reviews through its authenticated CLI; Codex evaluates the findings, revises the plan, and manages further rounds under the loop's limits. Preserve the user's model choice or use the CLI configuration when none is specified. Do not claim a completed Claude review until the runner returns a valid completed result.

For an existing plan or note, use review mode when the user asks only for review. Preserve its teaching or writing requirements in the review brief. A request to grill or review does not authorize implementation. If implementation is separately authorized, follow the shared loop's build and final inspection phases.

This entry point requires a Codex host. If invoked from Claude itself, explain that the shared runner rejects same-provider plan review and ask the user to invoke this entry point in Codex. Do not silently substitute Codex as the reviewer.

Keep this locally maintained entry point during upstream updates. Never restore upstream legacy grilling instructions.
