---
name: gemini-build
description: "Codex-to-Gemini Argon 4 (Medium) build workflow. Delegate a concrete work order to Gemini 4 Argon (Medium), then independently inspect and verify the changes with Codex."
---

# Gemini 4 Argon (Medium) builds, Codex coordinates and inspects

Invoke this skill as `gemini-build`. The builder is explicitly **Gemini 4 Argon (Medium)** (`--model gemini-4-argon --effort medium`, Antigravity `MODEL_PLACEHOLDER_M418`).

Read `../geminex-loop/references/build.md` and `../geminex-loop/references/runtime.md`. Resolve `RUNNER` from `../geminex-loop/scripts/runner.py`. Preserve `SPEC_FILE` as `--plan`, `PROOF_CMD` as `--proof`, and `--model gemini-4-argon --effort medium`.

1. **Delegate Build to Gemini 4 Argon (Medium)**:
   ```powershell
   python -X utf8 RUNNER build --host codex --builder gemini --repo <REPO_ROOT> --plan <SPEC_PATH> --approval <APPROVED_RESULT_JSON> --proof "<PROOF_CMD>" --model gemini-4-argon --effort medium
   ```
   *(For an explicitly requested standalone work order without prior plan review, pass `--unreviewed-spec` instead of `--approval`.)*
2. **Independent Host Verification & Inspection**:
   - Inspect all changed, staged, and untracked files relative to the pre-build commit (`base` in `result.json`).
   - Run the agreed proof commands independently.
   - Run fresh cross-provider inspection (`python -X utf8 RUNNER inspect --host codex --builder gemini --repo <REPO_ROOT> --plan <SPEC_PATH> --base <BASE_COMMIT>`). Never ask Gemini to certify its own build as independent inspection.
