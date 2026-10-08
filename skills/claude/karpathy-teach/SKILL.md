---
name: karpathy-teach
description: Teach an AI or programming topic using the evidence-supported Karpathy method. Use when Joshua asks for Karpathy-style teaching, a runnable explanation, or the saved Karpathy tokenizer demonstration.
---

# Teach with the reviewed Karpathy method

Hand the user's topic and success criterion to the project `karpathy` subagent. Give the minimum relevant context; do not include unrelated student or personal records. The agent reads wiki/karpathy/hot.md first, uses at most five wiki pages and applies wiki/karpathy/rules.md. The wiki is compiled public evidence, not a clone of a person; its collected-source coverage and media limits are documented.

Before showing the answer, grade it against all seven rules. Require concrete evidence for each pass: mechanism reconstruction, small baseline, prediction versus observed output, meaningful counterexample/fix where applicable, relevant execution, explicit assumptions, and justified simplicity. Reject invented outputs and rerun after edits. A non-code question can mark execution and broken-code demonstration not applicable. Preserve Joshua's instructions and voice.

Show the learner-facing explanation and source citations after grading. Put assumptions and the seven-rule grades before the final three sections: What I ran, What came out, What I changed. The project Stop hook returns the exact video message when changed code has no subsequent execution. A failed run must be reported as failure. The Python receipt helper is additional evidence, not a requirement that every task use Python.

Use the existing `ingest` workflow for new sources; this skill does not create another intake system or collect sources automatically. Canonical topic and evidence paths remain under wiki/karpathy/ and raw/sources/karpathy-brain/.
