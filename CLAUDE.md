# ai-os — second brain

This directory IS the Obsidian vault. It is the decision layer; code repos under `projects/` are the implementation layer.

**Vault root (this machine, Windows):** `C:\Users\Joshu\dev\ai-os`
**Code repo:** `C:\Users\Joshu\dev\ai-os\projects\lsatu`

Older notes may say `/Users/joshuaf/ai-os` (the previous Mac), `~/Documents/Obsidian Vault/...`, or `~/Documents/Claude/02_PROJECTS/LSATU`. All three are stale. Use the paths above.

## Layout

| Path | What it holds | Editable |
|---|---|---|
| `wiki/` | Live knowledge. Read from here. | Yes |
| `wiki/tasks.md` | Living ledger: Now / Next / Done | Yes |
| `wiki/hot.md` | What is warm right now | Yes |
| `wiki/log.md` | Dated session log, append-only | Append |
| `wiki/dashboard.md` | Status at a glance | Yes |
| `wiki/index.md` | Map of the vault | Yes |
| `wiki/teaching-voice.md` | Route ALL student-facing copy through this | Yes |
| `wiki/entities/aspiring-attorneys.md` | The tutoring business: offers, channels, priorities | Yes |
| `students/<name>/` | A student's whole record — transcripts, notes, homework | Yes |
| `corpus/` | LSAT teaching knowledge, fills by ingest | Via ingest |
| `raw/` | Immutable input. **Never edit.** | No |
| `raw/inbox/` | The one intake queue. Web Clipper writes here. Empty = nothing pending. | Drains via `ingest` |
| `raw/sources/` | Processed evidence, each with `PROVENANCE.md` + `SHA256SUMS`. Clips land in `raw/sources/clips/`. | No |
| `archive/` | Read-only pre-rebuild reference (2026-07-16). May be stale. | No |
| `projects/` | Code repos | Yes |
| `setup/` | Machine setup files for this box | Yes |

## Session protocol

**Session start — "brief me" / `/pickup`**
Read in order: `wiki/tasks.md` → `wiki/hot.md` → `wiki/dashboard.md` → `wiki/index.md` → latest `wiki/log.md` entry. Then give a 6–8 line briefing (Now / Next / open threads / suggested next) and wait.

**Session end — "done for today" / `/wrapup`**
Propose which tasks are done and confirm first. Then strike them through in `wiki/tasks.md` with a date, refresh `wiki/hot.md`, append a dated `wiki/log.md` entry, update the task anchor, and give a 4-line confirmation.

Finished work is struck through with a date so a new session never re-runs it.

## Rules

- Read knowledge from `wiki/`, never from `raw/`.
- `raw/` is immutable input. If an archived page becomes load-bearing again, re-ingest it through `raw/` rather than editing it in place.
- When saving deliverables to the vault use `[[wiki-link]]` syntax and `UPPERCASE-HYPHENATED.md` filenames.
- The `obsidian` CLI (`search`, `backlinks`, `read`) needs the Obsidian app open. Flat file reads work without it.
- Skip the vault entirely for trivial code edits.
