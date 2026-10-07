# Skills repaired on 2026-09-30

Resolved the confirmed defects from [the skills audit](audit-2026-09-30-224230-85d44c.md) in the inspected scope.

- Validation now recognizes four documented runtime name pairs and requires both catalog counterparts. If either runtime activates a pair, the other counterpart must also be present. It distinguishes the verified GitHub remote identity from a local path. Relocated Markdown references are accepted only when changed destinations resolve to the same existing file, while changed instructions and missing/different resources still fail.
- A portable smoke check verifies copied project SKILL.md entry points and metadata from root and nested paths. It is explicitly a static check, not proof of live browser/CLI invocation or resource portability.
- The generated catalog separates 15 preserved support-only project folders from invokable skills. It no longer emits missing-description warnings for those folders. Copy-based activation wording replaces the old symlink instruction. README no longer points to the nonexistent Mac PLAN.
- Audit's five existing mirrors now contain the complete rubric-v2 package, references and templates, with accurate Claude/Codex names.
- Four lint mirrors use actual runtime roots and local diagnostics by default. Assumed external destinations and automatic reporting instructions were removed.
- Four doctor mirrors have truthful cloud-processing boundaries, correct provider identities and script paths, and Windows guidance. Codex frontmatter validates; Claude keeps its supported argument-hint field.
- Written-explanation transcription in both catalogs and three existing global copies now uses current browser entry points. Codex follows CUA documentation returned by its actual tool. It no longer depends on retired control-in-app-browser or a nonexistent memory file. The set log now resolves to the existing LSAT U repository location. Claude checks its own browser tool availability.

Verification: main skills validator PASS (Claude 220, Codex 202 catalog entries); generated catalog no weak-entry warnings; three regression tests pass; smoke check covers 19 Claude and 27 Codex project activations; offline Claudex dry run reports zero changes and zero conflicts. Workers checked local Markdown references in repaired packages and metadata. Doctor scripts --help worked without reading any conversation history. No live transcription, model review/build, external report or scheduler run was launched for testing.

Preserved useful support files and unrelated edits. Original audit report remains unchanged. No entire skill or support folder was deleted. Supporting backups for the instruction repair are outside activation roots at C:/Users/Joshu/AppData/Local/Temp/skill-doc-repair-backup-zgwifaxp.

Remaining verification gaps are not established defects: the broader global/catalog content differences have not all been adjudicated; actual usage/outcome history and plugin-cache completeness were not audited. The overlapping grill shortcut remains functional. It was not removed merely for having a similar trigger. No unverified skill was declared useless or safe to delete.
