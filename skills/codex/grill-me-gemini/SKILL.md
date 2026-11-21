---
name: grill-me-gemini
description: "Codex-to-Gemini Argon 4 (Medium) grilling workflow. Interview the user one question at a time to sharpen a plan, then run independent review with Gemini 4 Argon (Medium) via geminex-loop."
---

# Grill a Plan and Review with Gemini 4 Argon (Medium)

Read and follow `../geminex-loop/SKILL.md`. Resolve its references and `scripts/runner.py` from the sibling `geminex-loop` skill directory.

## Direction: Host -> Gemini 4 Argon (Medium)

1. Conduct the one-question-at-a-time requirements interview (`Phase 0` and `Phase 1` of `geminex-loop`) until the plan is locked down in `PLAN.md`.
2. Send `PLAN.md` to **Gemini 4 Argon (Medium)** (`MODEL_PLACEHOLDER_M418`) for independent cross-provider review:
   ```powershell
   python -X utf8 RUNNER review --host codex --repo <REPO_ROOT> --plan <PLAN_PATH> --model gemini-4-argon --effort medium
   ```
3. Evaluate Gemini's findings, update `PLAN.md`, and iterate up to `MAX_ROUNDS=5` until `Verdict: APPROVED`.
4. Preserve the user's authorized scope: a request to grill or review does not authorize implementation unless explicitly requested.
