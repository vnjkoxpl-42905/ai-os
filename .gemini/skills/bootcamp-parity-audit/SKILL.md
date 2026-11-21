---
name: bootcamp-parity-audit
description: Compare a named LSAT U bootcamp with current Intro to LR source, product and visual benchmarks. Use for explicit bootcamp parity or shipped-quality audits, not general second-brain audits. Diagnose without implementation unless requested.
---

# Compare a bootcamp against current evidence

Use the specified bootcamp name/slug. Ask once only if absent. Resolve the actual AI OS root and target application's working tree; read its applicable instructions. The local default is the sibling `ai-os-projects/lsatu`, not code inside the vault. Different worktrees can hold newer task-specific state.

## Benchmarks to read first

Resolve these paths from the AI OS root:

1. `references/bootcamp-quality-bar.md`: source coverage, teaching, actual interactions, persistence/access, accessibility and validation boundaries.
2. `references/intro-to-lr-product.md`: observed current comparison surfaces and historical intent limits.
3. `references/intro-to-lr-design.md`: imported scoped style evidence and the cream-versus-legacy-dark conflict.
4. `references/lsat-teaching-voice-standard.md`: Joshua's current selected instructional voice.

These three benchmark replacements were reconstructed on 2026-10-11 from identified existing documents/code. They are usable current references, not recovered historical originals or proof of live acceptance. Check their owning source paths and current imports before relying on numeric values. If a source is absent, disclose that limited comparison rather than inventing a standard. If a relevant entity/product page exists, read it; absence is a documentation gap, not proof of a missing feature.

## Inspect a focused comparison

1. Locate the target source in the actual app checkout. Compare meaningful equivalents against `src/bootcamps/main-conclusion/`: overview/learning flow, drill/review, source/data layer and saved progress. Do not infer a feature is absent only because folders differ.
2. Identify the current route mount and imported styles. Historical `/bootcamp/structure`, standalone no-auth plans and dark `tokens.css` cannot override current `/bootcamp/intro-to-lr` routes or imported cream `scoped.css`.
3. Sample relevant components and tests, then use a signed-in browser when authorized and available. Preserve live/backend authority. Code, old audit results, deployed rendering and real account persistence are different evidence levels.
4. Diagnose only. If asked to fix, follow the owning app's workflow and authorization. Do not change design/product decisions merely to obtain visual sameness.

## Report five deltas

```text
1. Feature parity: useful analogous capabilities missing from the target.
2. Visual parity: accidental deviations from current imported styles versus deliberate differences.
3. Content/pedagogy parity: reasoning, feedback, source coverage and teaching-standard gaps.
4. Data/quality gaps: dead interactions, fabricated state, persistence/access/error handling.
5. Verdict: shipped-quality / in-progress / needs-work, evidence limits and the highest-value next fix.
```

State checkout/commit, inspected surfaces and checks actually run. Qualify source-only review and unverified live acceptance. Keep findings short; use no em dashes. An undocumented target is a documentation gap to report, not a reason to silently skip it. Activate through the host's skill picker or a plain-language request; `$bootcamp-parity-audit` is Codex syntax, not a universal slash command.
