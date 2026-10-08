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

Joshua selected **Codex** for this method on 2026-10-08. The original video prompts remain preserved; [the Codex variant](../../research/karpathy-video-2026-10-08/CODEX-PROMPTS.md) records the runtime substitution.

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

Codex uses its own event-based adapter, `../ai-os-projects/karpathy-method-tools/codex_stop.py`, configured in `.codex/hooks.json`. It is separate from the Claude transcript parser. [Codex hook acceptance](../../research/karpathy-brain-2026-10-08/CODEX-STOP-ACCEPTANCE.md) owns test scope and activation state. New hook definitions must be reviewed and trusted in the Codex CLI using `/hooks` before they run; project-directory trust alone is insufficient. [Official Codex hooks documentation](https://learn.chatgpt.com/docs/hooks), checked 2026-10-08. No trust bypass or fabricated trust is used. Until activated, the skill requires relevant execution and reviewed receipts.

Start Codex in this AI OS directory, open `/hooks`, inspect the definitions from `.codex/hooks.json` and trust those project entries. A fresh session also discovers the new project agent. The current delegated teaching test applied its instructions through a generic worker because the active chat did not expose a newly registered `karpathy` role; that fallback is explicitly recorded.

## Check the actual stage, not the source count

[Verbatim compliance](../../research/karpathy-video-2026-10-08/VERBATIM-COMPLIANCE.md) preserves the original video sequence and historical Claude runs. [Current execution record](../../research/karpathy-brain-2026-10-08/VIDEO-PROMPT-EXECUTION.md) owns the authorized Codex stage status. The [saved collection is compiled](../../research/karpathy-brain-2026-10-08/COMPILATION-AUDIT.md), with payload processing distinguished from semantic reading. Media fidelity and exhaustive X history remain unverified. The historical Claude quota no longer blocks this Codex task. [Fresh Codex tokenizer acceptance](../../research/karpathy-brain-2026-10-08/CODEX-TOKENIZER-ACCEPTANCE.md) records actual execution and the chronological failure/fix. Hook tests are distinct from trusted native-hook acceptance. No change to Joshua's identity, teaching policy or vault structure is implied.
