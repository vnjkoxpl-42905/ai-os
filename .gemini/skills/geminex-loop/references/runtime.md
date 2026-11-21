# CLI & Antigravity Language Server Runtime (`geminex-loop`)

Use Python 3.10+ and the runner installed at `../scripts/runner.py` relative to this reference. Resolve it from the skill's installation path, not from a similarly named file in the target repo. Runtime has zero third-party pip dependencies. Commands below use `RUNNER` as a placeholder for that absolute path; quote paths containing spaces and launch with `python -X utf8` on Windows.

The runner orchestrates one cross-provider turn between **Gemini 4 Argon (Medium)** (`gemini-4-argon`, effort `medium`, Antigravity `MODEL_PLACEHOLDER_M418`) and **Codex CLI** (`codex`). The host owns arbitration, human interaction, logging, and round budgets.

## Roles and commands

```text
python -X utf8 RUNNER roles --host gemini
python -X utf8 RUNNER roles --host codex --builder gemini
python -X utf8 RUNNER review --host gemini --repo PROJECT --plan docs/implementation.md
python -X utf8 RUNNER review --host codex --repo PROJECT --plan docs/implementation.md --model gemini-4-argon --effort medium
```

- When `--host gemini` is used, **Gemini** coordinates and **Codex CLI** is the default independent reviewer (`codex exec -s read-only`).
- When `--host codex` is used, **Codex** coordinates and **Gemini 4 Argon (Medium)** (`--model gemini-4-argon --effort medium`, mapped to `MODEL_PLACEHOLDER_M418` on the local Antigravity Language Server) is the default independent reviewer.
- For an explicit Codex model choice, pass `--model gpt-6-astra --effort high`. For Gemini, `--model gemini-4-argon --effort medium` is the default and maps to `MODEL_PLACEHOLDER_M418` (`low` -> `M419`, `high` -> `M417`; `gemini-3.8-flash` maps to `M320`/`M319`/`M318`).

## Resume, check, and one-shot routing

```text
python -X utf8 RUNNER review --host codex --repo PROJECT --plan docs/implementation.md --resume PREVIOUS_RESULT --feedback DISPOSITIONS
python -X utf8 RUNNER check --host codex --repo PROJECT --plan docs/implementation.md --approval APPROVED_RESULT
python -X utf8 RUNNER route --host codex --repo PROJECT --route-mode read-only --prompt-file TASK.md
python -X utf8 RUNNER route --host gemini --repo PROJECT --route-mode read-only --prompt-file TASK.md
```

Each call prints its unique artifact directory immediately before launch (`prompt.txt`, `command.json`, `stdout.txt`, `stderr.txt`, and `result.json`). After completion, read `result.json`; an exit code of zero means a completed turn, **not APPROVED** (the verdict may be `REVISE` or `BLOCKED`).

## Review boundaries

- **Codex reviewer (`--host gemini`)**: runs `codex exec -s read-only` with `--disable apps --disable plugins -c notify=[]`, all enabled MCP servers switched off, and `--output-schema`.
- **Gemini 4 Argon (Medium) reviewer (`--host codex`)**: connects to the running local Antigravity `language_server.exe` over loopback HTTP/HTTPS using its CSRF token and starts or resumes a dedicated `cascadeId` pinned to `MODEL_PLACEHOLDER_M418` (`gemini-4-argon`, medium reasoning). After the turn finishes, it audits only the new trajectory steps and validates the returned structured JSON review against `REVIEW_SCHEMA`.

The Gemini audit is **post-run detection and result rejection, not preventive sandboxing**. A forbidden action may already have happened before the runner sees it. The audit rejects command/file mutation, subagent, message, scheduling, question, task-management and generic MCP-call records before accepting the reply. It normalizes camel/snake/kebab identifiers and reads concrete step types/payloads plus nested planner/tool/function-call records. Metadata, tool catalogues, configuration, arguments, result bodies and prose are not treated as invocations. Unknown future trajectory schemas require an audit update; this is not proof that every possible side effect is prevented. Non-read-only builds bypass this rejection. No live provider call is needed for the offline regression suite:

```text
python -X utf8 -m unittest discover -s .agents/skills/geminex-loop/scripts -p test_runner_audit.py -v
```
