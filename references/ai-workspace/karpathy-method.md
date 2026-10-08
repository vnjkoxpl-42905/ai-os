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
Use karpathy-teach to explain byte-pair tokenization with a tiny runnable example. Tell me what you expect before running it, show a failure and its fix, and grade the lesson against the seven rules.
```

Claude activation: `.claude/skills/karpathy-teach/SKILL.md` and `.claude/agents/karpathy.md`. Codex activation: `.agents/skills/karpathy-teach/SKILL.md` and `.codex/agents/karpathy.toml`. Corresponding inert catalog copies remain in `skills/{claude,codex}/` and `agents/{claude,codex}/`. New runtime components may require a fresh session to be discovered.

The agent starts at the hot page, reads at most five wiki pages per task, cites source pages for statements about Karpathy and reports what ran, what came out and what changed. New links use the existing `ingest` skill, which updates the owning pages; no separate Karpathy intake pipeline was installed.

## Execution is checked within a defined scope

Claude's project agent has frontmatter `PreToolUse` and `Stop` hooks. The pre-tool snapshot detects changed code in the registered example workspace, including shell writes. Successful Write/Edit changes elsewhere are tracked through the agent transcript. Shell edits outside the registered workspace are not covered and are forbidden by the agent workflow. The Stop hook requires current-file, successful execution receipts. An unrelated command, failed run or stale file hash does not pass.

The external helper lives at `../ai-os-projects/karpathy-method-tools/run_gate.py` relative to the vault. It traces actual Python file execution, records hashes and exit status, and stores runtime evidence outside the vault. It is a correctness aid for a trusted assistant, not a security boundary against a malicious process. The current adapter covers Python; unsupported languages require another adapter or an explicit unverified blocker report. After one gate retry, a final report beginning `Execution blocked:` can exit honestly without claiming success.

Codex uses the same execution-receipt workflow. This setup does not install or claim a native Codex equivalent of Claude's Stop hook. [Official Claude hook documentation](https://code.claude.com/docs/en/hooks#hooks-in-skills-and-agents), checked 2026-10-08, describes the agent-specific lifecycle and conversion of an agent Stop hook to SubagentStop.

## Check the actual stage, not the source count

[Video execution record](../../research/karpathy-brain-2026-10-08/VIDEO-PROMPT-EXECUTION.md) records current results and gaps. Source inventory and physical storage are separate from semantic compilation. The full corpus is not yet completely read; media and exhaustive X history are also unresolved. No broad change to Joshua's identity, LSAT teaching policy or vault structure is implied.
