# Execute the saved video sequence

Authority: Joshua's 2026-10-08 request to run the prompts from [the saved video](../karpathy-video-2026-10-08/prompts.md). Original sources remain immutable. This is the existing current ai-os vault, not the retired Ai-os vault.

| Prompt | Current verified state |
|---|---|
| 1. Collect | Physical blogs, repository snapshots, lecture captions and X ledgers exist. Collection is useful but not exhaustive; latest X run stopped on HTTP 429. |
| 2. Compile | In progress. Three delegated domain passes are reading sources and writing source pages plus explicit semantic coverage. Existing five-source starter is preserved. Inventory and automated keyword scans do not count as semantic reading. |
| 3. Derive rules | Pending reviewed synthesis and two independent source locations per retained rule. Do not force seven unsupported rules. |
| 4. Agent and teaching skill | Pending rule evidence. Scope to Karpathy teaching, preserve Joshua's identity, use native runtime configurations and project activation/catalog copies. |
| 5. Scoped execution gate | Pending implementation and behavioral tests. Current official Claude documentation checked on 2026-10-08; Claude Stop/SubagentStop mechanisms must not be represented as a Codex hook. |
| 6. Tokenizer lesson | Pending prior stages. Run a small example, predict output, expose and fix a broken case, and grade against each supported rule. |

## Source and implementation references

- [Video source page](../../wiki/sources/i-built-another-andrej-karpathy-using-claude.md).
- [Karpathy index](../../wiki/karpathy/index.md).
- [Source coverage audit](HANDOFF-VERIFICATION.md) and [latest X rerun](X-RERUN-RESULT.md).
- [Official Claude hooks reference](https://code.claude.com/docs/en/hooks) and [subagent reference](https://code.claude.com/docs/en/sub-agents), verified for implementation design on 2026-10-08.

Subagent frontmatter hooks can scope enforcement to that agent. Skill hooks can remain registered for later turns, so any implementation must explicitly protect unrelated sessions. A command that merely ran is not proof that edited code passed; execution evidence must refer to the relevant version and outcome.
