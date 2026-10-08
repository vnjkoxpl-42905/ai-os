---
name: karpathy-teach
description: Teach an AI or programming topic using the evidence-supported Karpathy method. Use when Joshua asks for Karpathy-style teaching, a runnable explanation, or the saved Karpathy tokenizer demonstration.
---

# Teach with the reviewed Karpathy method

Read wiki/karpathy/hot.md first, then wiki/karpathy/rules.md. Use the project `karpathy` agent if available; otherwise follow its instructions directly and state that delegation was unavailable. Read no more than five wiki pages per task, including hot and rules. Cite the source pages for claims about Karpathy. Full-corpus semantic compilation remains incomplete.

For a code lesson: define done, show the smallest useful mechanism, predict the result before execution, run it, explain the observed result, demonstrate a meaningful isolated failure, fix and rerun, then ask the learner to reconstruct one step. Application files and dependencies belong in sibling ai-os-projects/.

Before presenting the answer, grade all seven rules with concrete pass/needs-improvement/not-applicable evidence: mechanism reconstruction, small baseline, prediction/run/comparison, counterexample/fix, relevant execution, explicit assumptions, justified simplicity. A non-code question may mark execution and broken-code demonstration not applicable.

Use ../ai-os-projects/karpathy-method-tools/run_gate.py --run with --file for edited Python files to preserve execution receipts. This helper traces executed Python files and hashes; an unrelated command does not prove the edited code ran. Rerun after edits. Codex has no Claude Stop hook installed by this skill: execution is enforced by this workflow and reviewed receipts, not a claimed native blocking mechanism. Preserve Joshua's instructions and voice.

End with the explanation, source links, what ran, actual output, what changed, assumptions/limits and seven-rule grades. New source intake uses the existing `ingest` skill; do not build a competing pipeline.
