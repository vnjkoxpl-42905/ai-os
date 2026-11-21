# The six-entry Karpathy workflow already exists

Reconciled against current disk files on 2026-10-26. **AQ-039 can close as an evidence reconciliation and overlap decision.** Do not reinstall the teaching agent, introduce another ingest pipeline or repeat source acquisition merely because the extraction-stage prompt file still says subsequent work is pending.

The source sequence is five verified numbered cards plus a visible tokenizer test command, not six verified prompt cards. [Original extraction](../karpathy-video-2026-10-08/prompts.md) preserves that distinction. [CODEX-PROMPTS](../karpathy-video-2026-10-08/CODEX-PROMPTS.md) records Joshua's authorized runtime substitution and the `$karpathy-teach` invocation. Its headings called Prompt 6 do not establish a sixth on-screen card.

## Each source entry has an implementation home

| Source entry | Disposition on 2026-10-26 | Current mapped files and evidence | Remaining boundary |
|---|---|---|---|
| 1. Collect public sources | Already implemented for the saved collection; no new crawl | `raw/sources/karpathy-brain/raw/` exists. [Handoff verification](../karpathy-brain-2026-10-08/HANDOFF-VERIFICATION.md) separates physical files from logical posts and preserves failed/incomplete acquisition. [Compilation audit](../karpathy-brain-2026-10-08/COMPILATION-AUDIT.md) covers saved sources and separate supplements. | Not everything public was acquired; no new raw-source integrity or whole-history acquisition audit performed. Existing X acquisition was Joshua's authorized alternative to TwitterAPI.io. |
| 2. Compile a wiki | Already implemented | [Karpathy index](../../wiki/karpathy/index.md), [log](../../wiki/karpathy/log.md), [hot](../../wiki/karpathy/hot.md), source pages and generated GitHub audit exist. The compilation audit records 79 writings, 17 transcript texts, 1,215 GitHub files and separately accounted X text. | Counts and full semantic-coverage conclusions are historical audit evidence, not newly re-derived. Machine payload processing is distinguished from authored-text review; audio/media fidelity remains outside that proof. |
| 3. Derive seven recurring rules | Already implemented | [Seven rules](../../wiki/karpathy/rules.md) exists with quotation pairs, distinct raw-source links and separate evidence/application sections; [execution record](../karpathy-brain-2026-10-08/VIDEO-PROMPT-EXECUTION.md) records fourteen raw-matching quotes. | This reconciliation verifies presence and readable support structure, not a fresh audit of all fourteen quotations or a claim Karpathy always follows these rules. |
| 4. Agent plus teaching skill | Already implemented; copies currently match | `.codex/agents/karpathy.toml`, `.agents/skills/karpathy-teach/SKILL.md` and `skills/codex/karpathy-teach/SKILL.md` exist. Current instructions require hot first, five-page limit, real registered-agent handoff, independent parent seven-rule review and the three required ending sections. [Native lesson acceptance](../karpathy-brain-2026-10-08/NATIVE-CODEX-LESSON-ACCEPTANCE.md) preserves the 2026-10-09 registered-agent discovery and handoff. | Current skill bytes differ from the 2026-10-09 acceptance hash because the explicit current-execution contract was added later. Native behavior of every current instruction was not rerun in a fresh session. |
| 5. Scoped Stop gate | Already implemented; current local suite passes | `.codex/config.toml` enables hooks; `.codex/hooks.json` still defines UserPromptSubmit, SubagentStart, PreToolUse, PostToolUse, Stop and SubagentStop pointing to sibling `codex_stop.py`. `run_gate.py` and `project_stop.py` also exist. [Stop acceptance](../karpathy-brain-2026-10-08/CODEX-STOP-ACCEPTANCE.md) and retained native event file document historical blocking/recovery/unrelated-turn acceptance. | Config presence and current unit tests do not verify current native trust, native main Stop interception in this session or child SubagentStop enforcement. No trust UI, hooks, config or registrations were changed. |
| 6. Visible tokenizer test | Already implemented; current behavioral check passes | Sibling `../ai-os-projects/karpathy-method-tools/examples/native-codex-tokenizer-20261009/tokenizer.py` exists, with matching historical SHA-256 and lesson README. Fresh `--check` passes exact merges, unseen bytes, overlap, nine round trips, byte preservation and boundary checks. | The 2026-10-09 native lesson/independent grading remains historical evidence. This run did not repeat a full learner lesson, deliberately broken run or registered-agent handoff. |

## Fresh tests are separate from historical native acceptance

From `C:/Users/Joshu/dev/ai-os-projects/karpathy-method-tools`, executed with installed Python 3.12:

```text
py -3.12 -B -m unittest test_run_gate test_project_stop test_codex_stop
Ran 82 tests in 1.061s
OK
```

The tests were inspected for scope before running. They use temporary fixtures and mocked snapshots; the receipt helper's subprocess test can create an ordinary local runtime receipt. No live service or new hook registration was exercised. This is current local regression evidence, not native trust/enforcement proof.

From its existing example directory:

```text
py -3.12 -B tokenizer.py --check
PASS: baseline, exact merges, unseen bytes, overlap, 9 round trips,
      byte preservation, empty/single/zero-merge training, negative count
```

Current tokenizer SHA-256: `d05867d01afafae8cc3a46baa7d3f6a363bd05a82966ca86af7fd8b170099c7e`, matching the historical native acceptance record.

Current activated and catalog Codex skill SHA-256, both equal: `f2e8da3e885bb96cf4d4677c2362add97e1126437a67138cef598d383ede0363`. This differs from the old acceptance record's skill hash. The existing current-execution contract explicitly requires fresh activation verification before claiming new native enforcement; that boundary must survive any canonical summary update.

## What to adopt from the source now

Use the existing [Karpathy teaching route](../../references/ai-workspace/karpathy-method.md) for an actual teaching task. It already captures the useful mechanisms: tiny baseline, explicit prediction, relevant run, meaningful failure/fix and independent grading. Keep new source intake in the existing second-brain-ingest route.

No second teaching-agent installation, competing ingestion skill, new hook, trust change, paid API or complete-public-history claim is warranted. The original extraction file is historical evidence and should stay unchanged. Current-state readers should follow the later execution and acceptance records with their dates and explicit limits.
