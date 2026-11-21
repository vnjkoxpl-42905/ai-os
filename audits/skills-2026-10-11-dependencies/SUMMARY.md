# Remaining skill dependencies repaired on 2026-10-11

Both named dependency gaps now have physical local support. No historical benchmark content was fabricated. Native runtime loading/trigger acceptance is being checked separately by the parent task and is not established by this report.

The hash ledger contains 29 changed/new package/reference files: 12 existing entrypoints, 7 restored validator copies, 7 field-contract copies and 3 reference anchors. Read-after-write hashes all matched. `check-skills.py` passed against the concurrent final catalog state (Claude 224 / Codex 211 / Gemini 222); this is structural catalog validation, not native model triggering.

## Research validator recovered and repaired

Git history contained the original `skills/codex/research/validate_json.py` at commit `9b1a3aa3`. The untouched [recovered original](recovered-original-validate_json.py) and SHA-256 are in [dependency receipts](dependency-receipts.json). Its actual `field_categories` YAML format was recovered; no original research dataset/schema file was found.

The adapted validator lives inside every existing `research-deep` package at `scripts/validate_json.py`. It retains required/optional fields, flat/category-grouped values and historical category aliases. Strict `--require-complete` mode requires all defined fields and a matching `uncertain` array. It rejects missing/empty inputs, malformed/empty schemas, duplicate keys, unknown fields and missing required fields. These are structural checks, not truth or English/citation quality checks.

An isolated free PyYAML 6.0.3 environment is installed at `C:/Users/Joshu/dev/ai-os-projects/skill-dependency-tests/.venv`. Skill instructions identify that interpreter and a portable `uv run --no-project --with pyyaml==6.0.3 python` fallback. No global Python package or vault environment was created.

The entrypoint now validates existing resume files rather than treating existence as completion; bounds work to the selected topic and authorized batch; uses available host researcher roles; and preserves uncertainty/evidence. No extra runtime skill activation was created.

## Three benchmark references reconstructed from actual evidence

- [Quality bar](../../references/bootcamp-quality-bar.md): current evidence-based audit checks, source completeness, teaching, persistence/access and acceptance boundaries.
- [Product comparison](../../references/intro-to-lr-product.md): actual current Main Conclusion route/components and explicit historical plan limits.
- [Design comparison](../../references/intro-to-lr-design.md): the currently imported cream scoped styles, role tokens and component override caveats.

The original three benchmark filenames were absent from the searched current roots and Git history. These replacements explicitly say reconstructed 2026-10-11. They link to existing handoff, canonical parity documents, historical Gate 5 audit, current routes/imported CSS and Joshua's selected teaching standard. None of those source files was edited.

The important recovered difference: current `src/index.css` imports cream `styles/scoped.css`; legacy `tokens.css` declares dark navy. The skill now prevents an old dark-only plan from becoming a false parity failure or silently reverting the imported design. The source route `/bootcamp/intro-to-lr` also takes precedence over the historical `/bootcamp/structure` report. No live deployment acceptance was inferred.

## Relevant executed checks

`test_dependencies.py`: **16 tests passed**, including valid flat/nested/custom-category results, strict missing-optional failure and repair, uncertainty mismatch, duplicate/schema/JSON keys, missing files, empty schema, non-object JSON, and actual benchmark source/import checks.

The untouched original returned success when its JSON input directory was missing. That counterexample was reproduced. The adapted validator returned failure for the same missing-input situation, then passed a real complete fixture.

Karpathy execution receipts:

- `0783f1fc5bed48529fb8b4ee0aed3257`: installed validator and test file actually executed, exit 0, 16 tests.
- `d435dbb045154f2faaa722a95292e82d`: compare-and-swap repair tool actually executed, exit 0, second run changed zero entrypoint/support files.
- `f6f03a0501914133afa9a6937a8a8988`: predicted complete fixture pass; actual direct CLI exit 0, 100% coverage, 1/1 passed.
- `7846d7fb783d4350b4330b98ede1a267`: predicted incomplete fixture failure; actual direct CLI exit 1, missing description, 50% coverage. This intentional rejection is correct behavior, not an unresolved validator failure.

Receipts live under `C:/Users/Joshu/dev/ai-os-projects/karpathy-method-tools/runtime/receipt-<id>.json`. The parent task owns native Codex/Claude loading and realistic trigger acceptance, plus final catalog/index validation.

## Limits and seven-rule grades

The standard follows [reviewed Karpathy rules](../../wiki/karpathy/rules.md); it is our operational method, not Karpathy's endorsement.

| Rule | Grade and evidence |
|---|---|
| Mechanism reconstruction | Pass: recovered YAML field definitions become field sets; strict comparison plus uncertainty markers determine success. |
| Small baseline | Pass: one two-field fixture passes before broader malformed/missing-input cases. |
| Prediction/run/comparison | Pass for follow-up CLI check: complete fixture predicted pass, missing optional description predicted failure; actual statuses saved separately. Initial 16-test run had no separate user-facing prediction and is not used as sole evidence of this grade. |
| Counterexample/fix | Pass: original missing-input directory exited 0; adapted validator fails the same case. Missing optional field fails strict mode and passes after completing/marking it. |
| Relevant execution | Pass: installed validator functions and benchmarks exercised; edited-file hashes recorded. Native triggers are outside this report's proof. |
| Explicit assumptions | Pass: reconstructed historical standards and source-only app evidence labeled; language/factual/citation quality remain human/source-review obligations. |
| Justified simplicity | Pass: recovered schema plus one free project dependency; no parallel ingestion pipeline, paid services, app redesign or unnecessary activations. |
