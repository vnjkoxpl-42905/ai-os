---
name: karpathy-teach
description: Teach an AI or programming topic using the evidence-supported Karpathy method. Use when Joshua asks for Karpathy-style teaching, a runnable explanation, or the saved Karpathy tokenizer demonstration.
---

# Teach with the reviewed Karpathy method

Hand the user's topic and success criterion to the project `karpathy` subagent. Give the minimum relevant context; do not include unrelated student or personal records. The agent reads wiki/karpathy/hot.md first, uses at most five wiki pages and applies wiki/karpathy/rules.md. The wiki is compiled public evidence, not a clone of a person; its full-corpus coverage remains incomplete.

Before showing the answer, grade it against all seven rules. Require concrete evidence for each pass: mechanism reconstruction, small baseline, prediction versus observed output, meaningful counterexample/fix where applicable, relevant execution, explicit assumptions, and justified simplicity. Reject invented outputs and rerun after edits. A non-code question can mark execution and broken-code demonstration not applicable. Preserve Joshua's instructions and voice.

End with the learner-facing explanation, sources for claims about Karpathy, what ran, what came out, what changed and the seven-rule grades. The agent's scoped Stop gate requires successful current-file Python execution receipts from the external helper. Other languages need an evidence adapter and must not be described as runtime-verified by this Python gate.

Use the existing `ingest` workflow for new sources; this skill does not create another intake system or collect sources automatically. Canonical topic and evidence paths remain under wiki/karpathy/ and raw/sources/karpathy-brain/.
