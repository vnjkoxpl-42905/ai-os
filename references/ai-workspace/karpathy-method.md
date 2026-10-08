---
type: reference
subject: Use the reviewed Karpathy teaching setup
created: 2026-10-08
updated: 2026-10-08
aliases: [Karpathy method]
tags: [karpathy, claude, codex]
sources: [../../wiki/karpathy/rules.md, ../../wiki/sources/i-built-another-andrej-karpathy-using-claude.md]
---

# Ask for a small explanation you can check

The project `karpathy-teach` skill uses [seven reviewed rules](../../wiki/karpathy/rules.md) and the [Karpathy wiki](../../wiki/karpathy/index.md). It teaches a mechanism with a small example, states a prediction, runs the code, explains an isolated failure and fix, and grades the result. It is a method derived from public evidence, not a person or an endorsed replica.

Example request:

```text
/karpathy-teach build me a tiny byte-pair tokenizer from scratch and teach me what it does
```

Claude activation: `.claude/skills/karpathy-teach/SKILL.md` and `.claude/agents/karpathy.md`. Codex activation: `.agents/skills/karpathy-teach/SKILL.md` and `.codex/agents/karpathy.toml`. Corresponding inert catalog copies remain in `skills/{claude,codex}/` and `agents/{claude,codex}/`. New runtime components may require a fresh session to be discovered.

The agent starts at the hot page, reads at most five wiki pages per task, cites source pages for statements about Karpathy and reports what ran, what came out and what changed. New links use the existing `ingest` skill, which updates the owning pages; no separate Karpathy intake pipeline was installed.

## Execution is checked within a defined scope

Claude has a project Stop hook in `.claude/settings.json`, with a Karpathy SubagentStop matcher for delegated tasks. It identifies actual skill/agent use in the current turn, successful code writes/edits and subsequent runtime commands. It returns exactly `Karpathy rule, run it before you say it works.` when execution is missing. Pre/PostToolUse snapshots also track shell-created code under the active project directory and the registered external example workspace, excluding immutable raw material, skill catalogs, dependencies and runtime directories. Writes outside monitored roots must use Write/Edit so the transcript records them. A failed execution still counts as execution and must be reported as failure, never success.

The earlier agent-only hook was an adaptation and has been replaced. Its optional Python helper `../ai-os-projects/karpathy-method-tools/run_gate.py` still produces stronger current-file execution receipts. The project hook also accepts ordinary runtime commands; command recognition is an audit aid, not proof of branch coverage or a malicious-process security boundary. There is no report-prefix escape from the literal run requirement.

Codex uses the same teaching workflow but has no native Claude Stop hook. [Official Claude hook documentation](https://code.claude.com/docs/en/hooks), checked 2026-10-08, distinguishes project Stop and SubagentStop events.

## Check the actual stage, not the source count

[Verbatim compliance](../../research/karpathy-video-2026-10-08/VERBATIM-COMPLIANCE.md) owns current sequence status. The [saved collection is compiled](../../research/karpathy-brain-2026-10-08/COMPILATION-AUDIT.md), with payload processing distinguished from semantic reading. Media fidelity and exhaustive X history remain unverified. The [native hook probe](../../research/karpathy-brain-2026-10-08/NATIVE-STOP-ACCEPTANCE.md) observed blocking and recovery. The original ordered Claude replay was blocked at Prompt 3 by the Pro subscription limit, reporting reset at 2026-10-08 12:40 America/Toronto; the literal tokenizer invocation is pending. Existing adapted tokenizer tests remain separate evidence. No change to Joshua's identity, teaching policy or vault structure is implied.
