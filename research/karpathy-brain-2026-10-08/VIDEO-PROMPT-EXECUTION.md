# Execute the saved video sequence

**2026-10-08 correction:** the table below records a preliminary adaptation, not completion of the literal ordered prompts. The [verbatim video compliance review](../karpathy-video-2026-10-08/VERBATIM-COMPLIANCE.md) is authoritative for the exact-sequence request. Joshua explicitly accepted the existing collected X posts instead of TwitterAPI.io; compilation continues, final rule/agent/test execution awaits those stages.

Authority: Joshua's 2026-10-08 request to run the prompts from [the saved video](../karpathy-video-2026-10-08/prompts.md). Original sources remain immutable. This is the existing current ai-os vault, not the retired Ai-os vault.

| Prompt | Current verified state |
|---|---|
| 1. Collect | Physical blogs, repository snapshots, lecture captions and X ledgers exist. Collection is useful but not exhaustive; latest X run stopped on HTTP 429. |
| 2. Compile | In progress. Three delegated domain passes are reading sources and writing source pages plus explicit semantic coverage. All 2,072 captured own-author X primary texts reviewed; 16 GitHub files reviewed and 1,199 physical GitHub files unread. Eight of seventeen lecture/interview/animation files fully reviewed, nine bounded. All 79 writing Markdown inventory items accounted for: 78 new full reads/source pages plus the retained Animals page. Writing qualifications remain in blog-synthesis.md. Inventory and keyword scans do not count as semantic reading. |
| 3. Derive rules | Seven provisional rules implemented, each with quotes from two distinct supporting locations. Strongest reviewed evidence, not whole-corpus final ranking. |
| 4. Agent and teaching skill | Installed project/catalog copies for Claude and Codex. Claude skill and subagent actually invoked in the tokenizer demonstration; Codex configuration validated but not live-invoked here. |
| 5. Scoped execution gate | Twenty tests pass. Native Claude agent hook accepted the actual executed lesson. Python execution receipts and current hashes; registered example workspace; advisory trust boundary. No Codex native hook claim. |
| 6. Tokenizer lesson | Actually executed: corrected decoder 8/8 passes; broken decoder 5/8 failures. Windows helper encoding failure fixed and rerun verified. See TOKENIZER-ACCEPTANCE.md. |

## Source and implementation references

- [Video source page](../../wiki/sources/i-built-another-andrej-karpathy-using-claude.md).
- [Karpathy index](../../wiki/karpathy/index.md).
- [Source coverage audit](HANDOFF-VERIFICATION.md) and [latest X rerun](X-RERUN-RESULT.md).
- [Official Claude hooks reference](https://code.claude.com/docs/en/hooks) and [subagent reference](https://code.claude.com/docs/en/sub-agents), verified for implementation design on 2026-10-08.

Subagent frontmatter hooks can scope enforcement to that agent. Skill hooks can remain registered for later turns, so any implementation must explicitly protect unrelated sessions. A command that merely ran is not proof that edited code passed; execution evidence must refer to the relevant version and outcome.
