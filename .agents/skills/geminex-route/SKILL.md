---
name: geminex-route
description: "Fast routing and one-shot handoff between Gemini 4 Argon (Medium) and Codex. Recommend which model should handle a task, get a quick cross-provider second opinion, or delegate a scoped task in either direction (Gemini-to-Codex or Codex-to-Gemini Argon 4 Medium)."
---

# Geminex Route: Fast Gemini 4 Argon (Medium) <-> Codex Router

Evaluate the task, recommend the best provider/model, and optionally execute a single one-shot handoff via `../geminex-loop/scripts/runner.py`.

## Model Table

| Provider | Model & Effort | Best For |
| :--- | :--- | :--- |
| **Gemini (Antigravity)** | `gemini-4-argon` (`--effort medium`, enum `MODEL_PLACEHOLDER_M418`) | 1M-context synthesis, deep architectural reasoning, multimodal/UI analysis, product/pedagogy alignment, cross-checking Codex plans and diffs. |
| **Gemini (Fast)** | `gemini-3.8-flash` (`--effort medium`, enum `MODEL_PLACEHOLDER_M319`) | High-speed repo recon, quick verification, low-latency checks. |
| **Codex** | `gpt-6-astra` / `gpt-6-luna` / `gpt-6.1-sol` (`--effort medium|high`) | Multi-file implementation, surgical refactors, test writing, root-cause debugging, adversarial code review. |

## Executing a One-Shot Handoff (`route`)

Resolve `RUNNER` as `../geminex-loop/scripts/runner.py`:

- **From Codex -> Send task to Gemini 4 Argon (Medium)**:
  ```powershell
  python -X utf8 RUNNER route --host codex --repo <REPO_ROOT> --route-mode <read-only|write> --model gemini-4-argon --effort medium --prompt-file <TASK.md>
  ```
- **From Gemini -> Send task to Codex**:
  ```powershell
  python -X utf8 RUNNER route --host gemini --repo <REPO_ROOT> --route-mode <read-only|write> --prompt-file <TASK.md>
  ```

After completion, inspect `result.json` in the printed artifact directory and verify any changed files if `--route-mode write` was authorized.
