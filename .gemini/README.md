---
type: router
subject: Gemini / Antigravity Workspace Router
updated: 2026-09-19
---

# Gemini / Antigravity Workspace (`.gemini/`)

This directory is the dedicated operating workspace for Gemini and Google Antigravity within `ai-os`. It isolates Gemini's runtime assets from Claude's workspace (`.claude/`) and Codex's workspace (`.codex/` and `.agents/`).

---

## Directory Map

| Path | Purpose | Format / Contents |
|---|---|---|
| `.gemini/skills/` | Active Gemini skills | Individual skill folders containing `SKILL.md` and assets |
| `.gemini/agents/` | Subagent definitions | TOML configurations for specialized Gemini subagents |
| `.gemini/wiki/` | Gemini knowledge layer | Distilled concepts and source notes (`index.md`, `concepts/`, `sources/`) |
| `.gemini/raw/` | Source intake | Immutable raw text, video transcripts, and research dumps |
| `.gemini/output/` | Deliverables | Generated reports, prompt designs, and teardowns |

---

## Knowledge & Skill Repositories

* **Skills Repository:** Canonical Gemini skills are kept in `skills/gemini/`. Active skills are copied into `.gemini/skills/`.
* **Central Operating Instructions:** Governed by `GEMINI.md` at the repository root.
* **Push to Main Protocol:** Standard procedure for pushing directly to production lives in `PUSH_TO_MAIN_PROTOCOL.md`.
* **Firecrawl Web Intelligence:** Operational standards and schemas live in `references/firecrawl.md` and `references/firecrawl/`.
