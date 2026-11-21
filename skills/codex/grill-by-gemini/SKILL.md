---
name: grill-by-gemini
description: "Grill a plan with Codex, then get independent Gemini 4 Argon (Medium) review and revise against its findings. Use when the user asks to grill by Gemini, grill with Gemini, or reverse the Gemini-to-Codex grilling workflow."
---

# Codex coordinates, Gemini 4 Argon (Medium) reviews

Read and follow `../geminex-loop/SKILL.md`, resolving that skill's references and `scripts/runner.py` from its own directory.

This entry point explicitly selects **Gemini 4 Argon (Medium)** (`--model gemini-4-argon --effort medium`, Antigravity `MODEL_PLACEHOLDER_M418`) as the independent reviewer:
1. Conduct the requirements interview and prepare `PLAN.md`.
2. Invoke the sibling runner's review command with `--host codex --model gemini-4-argon --effort medium`:
   ```powershell
   python -X utf8 RUNNER review --host codex --repo <REPO_ROOT> --plan <PLAN_PATH> --model gemini-4-argon --effort medium
   ```
3. Evaluate Gemini's findings, revise `PLAN.md`, and manage further rounds (`--resume` + `--feedback`) under the loop's limits. Do not claim a completed Gemini review until `result.json` returns `status == "completed"`.
