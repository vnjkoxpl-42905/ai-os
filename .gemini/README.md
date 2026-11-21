---
type: router
subject: Gemini / Antigravity Workspace Router
updated: 2026-10-15
---

# Gemini / Antigravity Workspace (`.gemini/`)

This directory is the dedicated operating workspace for Gemini and Google Antigravity within `ai-os`. It isolates Gemini's runtime assets from Claude's workspace (`.claude/`) and Codex's workspace (`.codex/` and `.agents/`).

---

## Directory Map

| Path | Purpose | Format / Contents |
|---|---|---|
| `.gemini/skills/` | Active Gemini skills | Individual skill folders copied from `skills/gemini/` |
| `.gemini/agents/` | Subagent definitions | TOML configurations for specialized Gemini subagents (`karpathy.toml`, `browser-navigator.toml`, `web-researcher.toml`, etc.) |
| `.gemini/hooks.json` | Runtime protection & immutability hooks | Enforces `guard_protected_runtime_paths.py` and `guard_raw_sources.py` |
| `.gemini/scripts/` | Gemini workspace maintenance scripts | Helper scripts (`sync_gemini_skills.py`, `guard_protected_runtime_paths.py`, `guard_raw_sources.py`) |
| `.gemini/output/` | Deliverables | Generated reports, prompt designs, and teardowns |

---

## Knowledge & Skill Repositories

* **Central Operating Instructions:** Governed by [`GEMINI.md`](../GEMINI.md) at the repository root (delta over [`AGENTS.md`](../AGENTS.md)).
* **Unified Knowledge Vault:** All shared knowledge, sources, and ledgers live in the repository root (`wiki/`, `corpus/`, `students/`, `raw/sources/`, `raw/inbox/`) governed by [`system/schema/llm-wiki.md`](../system/schema/llm-wiki.md). Legacy `.gemini/wiki/` and `.gemini/raw/` folders are preserved historical artifacts; new knowledge ingests route through `second-brain-ingest` into the main vault.
* **Loophole Online AI Retrieval:** Route through [`corpus/loophole-online/AI-RETRIEVAL.md`](../corpus/loophole-online/AI-RETRIEVAL.md) and `python system/scripts/query-loophole.py`.
* **Skills Repository:** Canonical Gemini skills are kept in `skills/gemini/` and indexed in [`skills/INDEX.md`](../skills/INDEX.md). Active skills are copied into `.gemini/skills/`.
* **Push to Main Protocol:** Standard procedure for pushing directly to production lives in `PUSH_TO_MAIN_PROTOCOL.md`.
* **Firecrawl Web Intelligence:** Operational standards and schemas live in `references/firecrawl.md` and `references/firecrawl/`.
