---
name: karpathy-teach
description: Teach an AI or programming topic using the evidence-supported Karpathy method. Use when Joshua asks for Karpathy-style teaching, a runnable explanation, or the saved Karpathy tokenizer demonstration.
---

## Current AI OS execution contract

Verify hook activation separately from configuration or old receipts. Current-file execution receipts are required for edited code; never claim new native trust based solely on a historical acceptance report.

# Teach with the reviewed Karpathy method

In Codex, invoke this skill with `$karpathy-teach`; the video's `/karpathy-teach` spelling belongs to Claude and is not a registered Codex command. Read wiki/karpathy/hot.md first, then wiki/karpathy/rules.md. Hand the user's task to the registered project agent with `agent_type="karpathy"`. Do not substitute a generic worker or perform the lesson yourself. If registration fails, report the exact discovery error and repair registration before continuing. Read no more than five wiki pages per task, including hot and rules. Cite the source pages for claims about Karpathy. The collected sources are compiled with explicit text, payload, attribution and media limits.

For a code lesson: define done, show the smallest useful mechanism, predict the result before execution, run it, explain the observed result, demonstrate a meaningful isolated failure, fix and rerun, then ask the learner to reconstruct one step. Application files and dependencies belong in sibling ai-os-projects/.

Wait for the agent's answer, inspect its execution evidence, then independently grade all seven rules before presenting it: mechanism reconstruction, small baseline, prediction/run/comparison, counterexample/fix, relevant execution, explicit assumptions, justified simplicity. Use concrete pass/needs-improvement/not-applicable evidence rather than copying its self-grades. Send any failed applicable rule back to the same agent for correction and recheck before showing the answer. A non-code question may mark execution and broken-code demonstration not applicable.

Use ../ai-os-projects/karpathy-method-tools/run_gate.py --run with --file for edited Python files to preserve execution receipts. This helper traces executed Python files and hashes; an unrelated command does not prove the edited code ran. Rerun after edits. Codex project hooks are configured in .codex/hooks.json using codex_stop.py. New hook definitions must be reviewed and trusted through Codex /hooks before they run. Until activation is verified, enforce execution through this workflow and reviewed receipts; do not claim native blocking. Never bypass or fabricate hook trust. Preserve Joshua's instructions and voice.

Present the explanation, source links, assumptions/limits and seven-rule grades, then end with What I ran, What came out, What I changed. New source intake uses the existing `ingest` skill; do not build a competing pipeline.
