---
name: skill-lint
description: Diagnose broken skill paths, missing dependencies, stale commands, conflicting runtime copies, or wasteful instructions; list skills and propose scoped local repairs.
---

## Gemini host boundary

Use the current shared runner/CLI contract. Claude-native browser, task and hook tools named in the reference are available only when actually exposed; otherwise use the supported host route and report unavailable operations. Keep project paths relative to this registered root.


# Skill lint

Audit or repair the skills the user names. Resolve the repository root and the loaded skill directory first. Codex project activations use `.agents/skills`; Claude uses `.claude/skills`. Also inspect `.codex/skills`, user-level runtime roots, and `skills/{codex,claude}` when they exist or the user asks for the catalog/global setup. Do not invent a `.Codex` directory or assume every runtime searches every root.

Read [reference.md](reference.md) relative to this skill directory for procedures. This skill diagnoses package structure and instructions. `skill-doctor` is a separate optional history-based evaluation, not a prerequisite.

## Modes

- `list` or `info <skill>`: report actual names, descriptions, source locations, and required resources.
- `<skill>` or an audit request: identify confirmed defects, verification gaps, and intentional runtime differences.
- `--optimize <skill>`: improve trigger clarity, duplicated instructions, and useful detail. Length alone is not a defect.
- `--manage`, `clone`, `diff`, `sync`, or `revert`: compare actual origins and copies; preserve local changes and explain the proposed operation.
- `feedback`, `report`, `gist`, `pr`, or `resolve`: prepare a local draft. Publish or send only when the user explicitly authorizes that external action and identifies the destination.

## Repair boundaries

Use read-only checks first. Reproduce only with safe commands, help output, synthetic fixtures, or existing evidence. Do not run a substantive skill, paid generation, sends, or builds merely to lint it. Resolve supporting paths from the containing skill, commands from the documented working directory, and repository references from the repository root.

When the user asks for repairs, apply confirmed scoped fixes and update the canonical/runtime copies that belong to that skill. Preserve supporting resources and declared differences. Do not replace independent local policies blindly, remove history, or delete packages without explicit authorization. Compare files before and after, verify links and metadata, and summarize what remains unverified.

External reporting is optional. No default Discussion, Slack channel, repository, connector, or feedback service is assumed. Ordinary local diagnostics require no GitHub authentication or network calls.
