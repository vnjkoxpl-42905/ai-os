# Persona Agent Creator: source and setup verification

Verified 2026-10-09 in `C:/Users/Joshu/dev/ai-os`. Joshua requested a reusable skill for creating agents from other people's documented work, then selected a non-Karpathy name and required the actual Karpathy agent to create/refine it.

## Source method

The [original video](https://www.youtube.com/watch?v=bvGptCLDhyo) explicitly describes transfer to a sales teacher, author or coach at 02:15–02:24. The full [saved transcript](../karpathy-video-2026-10-08/transcript.md), [on-screen prompts](../karpathy-video-2026-10-08/prompts.md) and [untouched cards](../karpathy-video-2026-10-08/verbatim/) were reviewed. The source has five numbered cards and a sixth real test command, not a verified numbered sixth card.

A fresh browser export obtained during this task has SHA-256 `1E0D338FD0E8FD0317B15625C3B7051A665C96DC87786A55528EE0278DCD2620`, identical to the retained browser transcript in `research/karpathy-video-2026-10-08/verification-2026-10-09/browser-transcript.txt`. That earlier comparison established 393 matching caption segments. Captions are automatic, not an audio-verified transcript or biographical authority. No claim of watching every audiovisual frame in this turn is made. The saved prompt cards were previously checked visually.

The sequence is collect physical evidence without summaries, compile linked knowledge, derive seven corroborated rules, build the native agent and independently grading entry skill, add an applicable scoped verification gate, then test a real task. Continued updates use existing ingest. Generalizing person, domain and runtime is an adaptation, not identical verbatim execution of the Karpathy prompts.

## Current Karpathy configuration

Read-only source-fidelity reviewer inspected agent, activated/catalog skill, hook definitions and retained native acceptance events. Matching copies, hot-first retrieval, five-page cap, citations, parent grading and output endings are present. `.codex/config.toml` enables hooks. Prior native receipts prove main Stop blocking, real execution recovery and unrelated-turn acceptance; child SubagentStop remains configured/unit-tested, not separately live-blocked.

A fresh actual `agent_type=karpathy` probe explained mechanism reconstruction, consulted hot then rules then its study-advice source (three wiki pages), and correctly labeled author/sales examples as our adaptations. Parent compared the answer with the reviewed rule evidence. Independent grades: mechanism reconstruction pass, small baseline pass, explicit assumptions pass, simplicity pass; prediction/run/comparison, broken-code repair and code execution N/A for this non-code probe. This proves a current source-based handoff, not the entire native skill invocation or hook lifecycle again.

Fresh regression command in sibling `ai-os-projects/karpathy-method-tools`: `python -m unittest test_codex_stop test_project_stop test_run_gate`. Result: 82 tests, OK, 20.246 seconds. This is current regression evidence, not a fresh native child-hook blocking test.

Limits: saved-source compilation is not exhaustive acquisition of every public artifact/media; X browser acquisition was the authorized paid-provider exception; Codex `$karpathy-teach` differs from Claude slash syntax; arbitrary tool wrappers are not universally certified. Existing Karpathy adapter and event matchers hardcode its identity and do not guard newly named personas automatically.

## New skill and authorship

Final name: **persona-agent-creator**. Canonical [skill](../../skills/codex/persona-agent-creator/SKILL.md) and [procedure](../../skills/codex/persona-agent-creator/references/procedure.md); active Codex copy at `.agents/skills/persona-agent-creator/`. Mirrored Claude catalog/activation copies preserve the same host-aware procedure. Copies are project-scoped, not global.

Parent prepared a draft. The actual registered Karpathy agent then edited all three canonical files: SKILL.md, references/procedure.md and agents/openai.yaml. It renamed internal invocation/UI, refined triggers and exclusions, defined done, added a representative acceptance baseline and required predicted/observed comparison plus failure repair/rerun. Parent inspected final files before mirroring and validation.

Entry invocation: `$persona-agent-creator`. Triggers include creating a persona agent, building an agent based on a named author/teacher/coach/expert, and replicating the source-based process for another person. Ordinary generic coding-agent creation and use of an already built persona are excluded.

This creator is an instruction workflow; it is not itself a new person's agent. Each future requested persona still needs its own sources, attributable rules, configuration and actual native acceptance. It does not clone a person's private mind or imply their endorsement, automatic learning or watching for new sources.

## Independent checks

- Canonical and active skill passed bundled quick_validate.py using an external uv environment with PyYAML. Initial base Python lacked PyYAML; no dependency folder was added to the vault.
- Independent simulated scenario: four reposts of one interview plus two essays count as three originals; only three corroborated rules remain three, not invented seven. Non-code work gets domain checks, not a contrived execution gate. Missing/ambiguous identity requires clarification after local lookup. No material defect found.
- Review suggested explicit inclusion of hot/rules/source pages in the five-page cap and clear workflow-only non-code completion criteria; both were added before final mirroring.
- Final simulated trigger check matched author creation and coach replication, excluded generic code review and existing Karpathy tokenization teaching. This simulation does not establish new-agent runtime acceptance.
- Skill index regenerated. Whole-library check-skills.py still fails exactly one pre-existing unrelated session-handoff activation mismatch; no new creator or Karpathy defect was reported. Do not interpret this as a globally clean library.

Parent independently grades the final creator: mechanism reconstruction pass (six distinct stages); small baseline pass (one representative task before broad claims); prediction/comparison pass for tested validation and explicit future acceptance requirements, not completed future persona tests; counterexample/fix N/A for application code, while duplicate-corroboration and unsupported-attribution cases were simulated; relevant execution pass for validators and hook regression only; assumptions pass (coverage/runtime/gate limits); simplicity pass (existing ingest/schema/catalog infrastructure reused).

## Changes and remaining work

Created and activated the creator skill in both project runtimes, regenerated skill index, documented parity and appended the system change to wiki/log. No raw sources, existing agent/hook settings, unrelated handoff skill or external systems were changed. No new person was selected, so no new persona corpus or registered person-agent was created. Future invocations must verify actual runtime discovery and acceptance before calling that persona complete.
