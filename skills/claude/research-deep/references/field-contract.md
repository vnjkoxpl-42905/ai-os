# Recovered research field contract

The original validator was recovered verbatim from Git commit `9b1a3aa3`, path `skills/codex/research/validate_json.py`. The immutable recovery copy and SHA-256 are recorded in `audits/skills-2026-10-11-dependencies/`. No original fields.yaml dataset was found; each research task supplies its own field definitions in this recovered format.

```yaml
field_categories:
  - category: basic_info
    fields:
      - name: name
        required: true
        description: The product or subject name
      - name: description
        required: false
        description: A sourced description
```

The result can be flat (`name`, `description`, `uncertain`) or grouped under its schema category name (`basic_info`). The recovered historical category aliases (Basic Info, Technical Features, Performance Metrics and others) remain supported. Field names are unique and reserved metadata names `_source_file`/`uncertain` cannot be schema fields. An empty schema is invalid.

`--require-complete` requires every defined field, rejects unknown fields and checks the root uncertain array against [uncertain] markers within field values. Use `uncertain: []` when no fields are marked. Legacy default mode still requires only required fields and reports optional coverage; research-deep always uses strict mode. An explicitly missing input path, no JSON inputs, malformed schema/JSON, duplicate keys, or an array instead of a result object fails with nonzero status.

The validator does not certify factual accuracy, language, citation support, whether an empty value contains useful research, or current live-system truth. These require source review. Only schema categories and historical aliases are wrappers; arbitrary nested structures are field values. Do not reinterpret a different fields format without explicitly converting it and preserving the original.

Free isolated usage:

```text
uv run --no-project --with pyyaml==6.0.3 python "<installed-skill>/scripts/validate_json.py" --require-complete -f "<topic>/fields.yaml" -j "<topic>/results/item.json"
```
