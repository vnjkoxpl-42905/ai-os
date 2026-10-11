---
name: research-deep
description: Research an explicitly selected outline.yaml into structured JSON using its fields.yaml schema, bounded batches and field-coverage validation. Use for structured research batches, not ordinary knowledge questions or transcript intake.
---

# Structured research with validated field coverage

## Select the topic and authorization

Use the user-selected topic directory containing `outline.yaml` and `fields.yaml`. If one unambiguous topic is explicitly implied, use it; if several candidates exist, ask which. Do not choose an arbitrary newest outline. Reuse the already authorized batch scope; ask before expanding it, not before each already approved batch. Research is read-only unless saving the requested local outputs. Do not make paid calls or publish results without corresponding authorization.

## Resolve the validator before dispatch

This package includes `scripts/validate_json.py`, recovered from Git commit `9b1a3aa3` (`skills/codex/research/validate_json.py`) and adapted to reject empty/missing inputs. Resolve `{validator_path}` from the actual installed skill directory, not a guessed home path. Its YAML contract is documented in `references/field-contract.md`.

Use an interpreter with PyYAML. On this Windows machine the tested isolated interpreter is `C:/Users/Joshu/dev/ai-os-projects/skill-dependency-tests/.venv/Scripts/python.exe`. Verify it before use. Portable fallback: `uv run --no-project --with pyyaml==6.0.3 python`. If neither exists, install PyYAML in a project environment outside the vault, not system Python. A package-manager operation does not prove the validator ran.

Validate one output before starting a large batch. Require `--require-complete`: all schema fields, no unknown fields, and an `uncertain` array exactly matching fields whose values contain `[uncertain]`. This checks structure and coverage, not truth, source quality, English prose or whether citations support claims.

## Workflow

1. Read the selected outline's topic, items and execution configuration (`output_dir`, `batch_size`, `items_per_agent`). Resolve paths against that selected topic directory.
2. Resume only after validating existing result files with the current fields schema and strict mode. File existence alone is not completion. Keep invalid prior evidence and repair its output explicitly.
3. Dispatch within the authorized scope using researcher roles actually available in the host. Parallel work requires available slots. Each worker receives the full item, schema, unique output path and validator command. If no researcher role is available, perform bounded research directly rather than inventing a tool.
4. Preserve each field's source evidence in the schema's source/citation fields or a companion evidence Markdown file; never manufacture a value just to fill coverage. Mark unresolved values `[uncertain]` and list those field names in `uncertain`.
5. Run the validator on every result and repair failures. Keep stdout/stderr and the actual exit status. Report passing, failed and uncertain items. Do not suppress failures or infer completeness from an empty directory.

## Worker prompt

Substitute only the selected task's values below. `{validator_command}` is the verified interpreter/uv command, quoted script path and `--require-complete -f "{fields_path}" -j "{output_path}"`.

```text
Research {item_related_info}, output structured JSON to {output_path}.
Read {fields_path} for every field definition.
Use primary sources and preserve citation evidence. All field values must be in English.
Mark unresolved field values [uncertain]. Add uncertain as an array of precisely those field names, or [] when none.
Keep every defined field. Do not invent values to satisfy coverage.
After saving, run:
{validator_command}
Complete only when the actual validator exits 0. Report failures and unresolved source limits.
```

Use plain-language `research-deep` requests or the runtime's supported explicit skill picker. Codex explicit syntax is `$research-deep`; slash-command spellings are not portable.
