---
name: grill-with-docs-gemini
description: "Codex-to-Gemini Argon 4 (Medium) document-backed grilling workflow. Interview and review a plan with persistent CONTEXT.md, GLOSSARY.md, and ADR files using geminex-loop and Gemini 4 Argon (Medium)."
---

# Grill a Plan with Persistent Docs and Review with Gemini 4 Argon (Medium)

Read and follow `../geminex-loop/SKILL.md`. Resolve its references and `scripts/runner.py` from the sibling `geminex-loop` skill directory.

1. Read existing `CONTEXT.md`, `CONTEXT-MAP.md`, `GLOSSARY.md`, and `DECISIONS.md` / ADR files where relevant.
2. Interview the user one question at a time to settle requirements and domain terminology. Update `CONTEXT.md`, `GLOSSARY.md`, and ADR records as material decisions are locked in, and write `PLAN.md`.
3. Run independent cross-provider review against **Gemini 4 Argon (Medium)** (`MODEL_PLACEHOLDER_M418`):
   ```powershell
   python -X utf8 RUNNER review --host codex --repo <REPO_ROOT> --plan <PLAN_PATH> --model gemini-4-argon --effort medium
   ```
4. Evaluate findings, update `PLAN.md` and supporting docs, and resume until `Verdict: APPROVED`. Do not implement unless separately authorized.
