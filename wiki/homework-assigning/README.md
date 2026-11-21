---
title: Homework assigning
type: hub
status: first pass, 2026-11-14
---

# Homework assigning

Everything Joshua has assigned, to every student, in one place, so a new session transcript can be turned into a proposed package (notes, drills, activities) from what worked before.

| File | What it is | How it is made |
|---|---|---|
| [note-formula.md](note-formula.md) | How a note is built and how it reads: shapes, section order, Joshua's voice, font gaps. Derived from the Lanae note and the last two weeks of notes. | by hand |
| [model-note/](model-note/) | The Lanae note, and `note-shell.html`, the same page with `{{slots}}`. Rebuild the shell with `py -I system/scripts/build-note-shell.py`. | by hand + script |
| [rules.md](rules.md) | What Joshua has actually said about what to assign, plus the observed shapes. Hand-written. | by hand |
| [playbook.md](playbook.md) | In this situation, assign this. Draft, inferred from the record, not yet confirmed by Joshua. | generated |
| [by-topic.md](by-topic.md) | For each tag: earlier notes, activities, and catalog drills. Start here for "find me the causation note". | generated |
| [assignment-log.md](assignment-log.md) | Running log: each session, then what followed it. | generated |
| [taxonomy.md](taxonomy.md) | The tags and the keyword rules that apply them. Fix a rule here, then re-run. | generated |
| `notes-archive/<student>/` | The HTML of every live note ever posted, for reuse as a model. | export |
| `students/<slug>/assigned-work/` | Per-student package: every assigned note as HTML, a dated index of all assigned items, and per-note `CLAUDE.md` with session transcript links. Built 2026-11-14 for [Sofia](../../students/sofia/assigned-work/README.md) and [Celia](../../students/celia-cutler/assigned-work/README.md). | built from the export |
| `data/*.generated.json` | Raw and tagged rows, drill catalog. | export / build |

## Refresh

```bash
node system/scripts/lsatu-assignment-export.mjs
py -I system/scripts/build-homework-assigning.py
```

The export is read-only. It uses the saved admin login and posts nothing.

## Tags

Question type, question feature and reasoning type are the platform's own fields. Drills carry them in the catalog (exact). Notes and activities carry none, so they are tagged by keyword on title and headings (approximate).

## Using it on a new transcript

1. Tag the session. 2. Read each tag's section in `by-topic.md`: the closest earlier note, drills, any activity. 3. Check what the student already holds in `students/<slug>/homework/already-assigned/index.md`. 4. Propose. Nothing posts or assigns until Joshua approves. 5. No prior on the topic: run `second-brain-query` on `corpus/`, then build from scratch.

## Limits

- Only 131 of 342 items link to a session. Many accounts have no session folder or transcript, and some work was assigned between sessions.
- Session topics come from the opening summary of the Gemini export, so they are approximate.
- Test accounts (josh, lsatmaster, tester, Joshua Fisseha) are excluded. Twelve real students have no vault folder; they appear as `no-folder-<name>`.
- A stale `notes-archive/_unmapped/` folder from the first export run can be deleted; it duplicates the `no-folder-*` and `yahunatan-zetvy` folders.
