# Validation and explicit limits

2026-10-24.

- Eleven new/revised canonical summaries: evidence paths and SHA-256 rechecked independently; all source-summary exact quotes checked against preserved bytes.
- Twelve newly preserved input generations: SHA256SUMS and retained inbox originals rechecked independently. No source edits, moves or deletes.
- Hub links and modified skill copies: see hub-check.json for exact results. Root AGENTS.md and CLAUDE.md both route to the hub. Project and existing home-loaded ingest/resource skill copies match their respective runtime catalogues.
- Master catalogue refreshed: 3951 wiki pages.
- Full wiki lint completes with six findings, all outside the newly ingested source pages: two thin older pages, three older links in archived/log text, and one unrelated MCAT source orphan. No new source hash, quote, alias or evidence-drift errors remain. Report: system/generated/wiki-lint.generated.tsv.
- Full skill-catalogue validation does **not** pass: 21 unrelated catalogue/activation/shadow-copy problems remain, including chrome-extensions/modern-web-guidance catalogue gaps, Gemini/Codex pairing gaps and older home skill divergence. This task did not alter or repair those unrelated skills. The two modified skills' exact-copy checks pass independently.
- All new actions are optional proposals AQ-018 through AQ-032; existing statuses were preserved. The stale Next ID pointer that already named existing AQ-017 was advanced using the actual maximum allocated ID.
- Readback caught repeated carriage-return translation in compiled Markdown during action-link insertion; normalized compiled outputs and corrected the writer. Immutable evidence was never normalized.
- No original video visuals, commercial product claims, paid services, repository internals or live design tools were newly verified by this ingestion. No dashboard modifications, installation, production deployment or background ingest watcher.

The design hub is a single navigable domain within the existing LLM wiki. Capture still goes to raw/inbox; an invoked design ingest now maintains the hub in both runtimes.


## Subsequent skill repair (2026-10-24)

The21blocking skill findings recorded above are now resolved. The full validator passes; unrelated home-version warnings remain explicitly documented. See [repair report](../2026-10-24-skill-repair/REPORT.md). Historical audit counts describe the earlier snapshot; current design registries include the repair refresh.
