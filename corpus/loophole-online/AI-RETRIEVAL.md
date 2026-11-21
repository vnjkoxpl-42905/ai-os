---
type: synthesis
subject: Loophole knowledge retrieval for Claude, Codex and Gemini
created: 2026-10-15
updated: 2026-10-19
aliases: [Loophole AI search, Loophole knowledge retrieval]
contradictions: []
sources:
  - README.md
  - ROUTER.md
  - ../../system/schema/llm-wiki.md
---

# Find the relevant knowledge, then read its full source

This is the shared retrieval entry point for Claude, Codex and Gemini. Their workspace instructions route Loophole requests here automatically. It uses local Markdown, preserved captures and a rebuildable search index. It does not require a browser session, a signed media URL, an installed plugin or an activated skill. [README.md](README.md) is the human entry point; [ROUTER.md](ROUTER.md) owns filing decisions.

For **what we have, where it lives, and known gaps**, start with the [generated library map](library-map.generated.md). It describes retained generations and folder conventions, indexed record counts, content homes and evidence qualifications. Counts are indexed text records, not unique lectures or videos.

## Read a complete workout or routine directly

For how to perform a captured workout or routine, use `instructions` before manually extracting a large sourcebook. It returns exact captured authored instruction, advice, example, answer-key and footnote spans with their source paths and line ranges. It is a source reading view, not a rewritten summary or the entire sourcebook.

```powershell
python system/scripts/query-loophole.py instructions "The Conditional Rehab Routine" --kind routine
python system/scripts/query-loophole.py instructions "Unless Practice Routine" --kind workout
```

Use an exact title or returned identity; optional `--section LR|RC|shared` and `--kind routine|workout` narrow resolution. Ambiguous names return candidates to choose from. Other content types and unrecognized instructional headings return an explicit gap; use `open` and the full original source in those cases.

For routines, the result includes the captured classification, conditions, advice, schedule, repetitions, routine-specific steps and recognized instructional resources, plus full authored spans from uniquely matched workout routes. Each linked workout block identifies its `routine_step` and `workout_identity`. Read routine modifications and repetitions alongside the general workout instructions; the routine governs its application. Inspect `gaps` for any step without a unique captured workout route. Do not infer a complete routine from only one workout.

Read **every page** through `total_pages`. Outputs paginate at complete-block boundaries around 24,000 text characters; an oversized individual block remains intact and is marked. Run the returned `next_page_command` after the normal `python system/scripts/query-loophole.py` prefix, or repeat the command with `--page 2`, then subsequent pages. The blocks preserve original text rather than clipping an instruction. Follow source-relative image or resource links from their identified source directory and use `open` for media companions.

## Start with the smallest useful route

| Need | First route | Then read |
|---|---|---|
| RC method, Decaf/Cappuccino, passage or RC question strategy | [Reading Comprehension](reading-comprehension/README.md) | The relevant method, lecture transcript and written notes, keeping each version distinct. |
| LR translation, CLIR, question type or reasoning method | [Logical Reasoning](logical-reasoning/README.md) | The relevant topic and its original evidence. |
| Camo, vocabulary, retention or a method shared by sections | [Shared methods](shared/README.md) | The original procedure, not just the hub description. |
| A workout and its complete instructions | [Workouts](workouts/README.md) | Its local full-detail file, including exceptions and associated resources. |
| A routine and its ordered tasks | [Routines](routines/README.md) | The complete local routine sourcebook; preserve order, repeats and other tasks. |
| Bootcamp questions, choices, correct responses and instructor feedback | [Bootcamps](bootcamps/README.md) | The full drill, original captured JSON, formatted HTML and local instructional images. Only observed response branches are captured; inspect its coverage report. |
| A question citation, written Correct CLIR, MP3 or speech transcript | [Question database](question-database/README.md) | The question's local README and related transcript/audio files. |
| Exact source wording or capture completeness | [Source catalog](source-catalog.generated.md) | The identified notes, caption, transcript, HTML or provenance record. |

**The captured question database is LR only.** RC lectures and strategies are present, but an RC question database was not captured. A missing RC question match does not mean that the lecture library is missing. Course days 4 and 5 were not captured. For other limits, use the owning capture record rather than inferring absence from a search result.

Question records provide citations, classifications, written Correct CLIR and available recordings/transcripts. Question stimuli, answer choices and correct-answer reveals were outside this capture. Do not reconstruct missing official question text or claim an answer-key check from an instructor recording. Exact current citations take priority over old-citation aliases; when both match different records, inspect both citation fields before choosing the intended source.

## Use bounded full-text search when the hub is not enough

Run from the repository root. Search is local and read-only. Python's standard library supplies SQLite full-text search; no model call or embedding upload is involved.

```powershell
python system/scripts/query-loophole.py search "Cappuccino" --section RC --limit 5 --excerpt 500
python system/scripts/query-loophole.py search "Accuracy Failsafe" --kind workout --limit 3
python system/scripts/query-loophole.py search "Translation Decaf" --kind routine --limit 3
python system/scripts/query-loophole.py search "PT101.S2.Q1" --kind question --limit 1
python system/scripts/query-loophole.py search "How to Camo" --kind lecture --limit 3
python system/scripts/query-loophole.py search "Referential Phrasing" --kind bootcamp --limit 3
```

Filters: `--section LR|RC|shared`; `--kind question|lecture|notes|workout|routine|prep-map|reference|bootcamp`. LR and RC each include material shared by both; `shared` selects material tagged for both sections. Omit the section filter for all material. Start with five hits and increase only when the task needs more. Query words are literal full-text terms combined with OR, with title matches weighted, not a semantic model: if there is no useful match, try aliases such as `Camo`, `review`, `Decaf`, `CLIR` or the displayed title. Exact question citations are ranked ahead of broad lexical matches.

CLI search results are compact JSON with a source path, stable identity, status, aliases, bounded excerpt, line references, `artifact_count` and an `open_hint`. Titles and aliases are weighted lexical matches, not semantic understanding. Use `search "terms" --details` for the full result inventories (`related_files` and lecture `package_artifacts`), or use `open` for the selected package. `package_media` summarizes recorded media availability. Open `source_path` at the returned lines, then read the complete relevant instruction or transcript section. An excerpt locates evidence; it is not a complete drill or routine. The index is a derived locator, not a new authoritative knowledge source.

Per-query verification covers the returned text sources. Audio availability and companion paths are captured metadata, not a fresh MP3 byte audit on every lookup. Use the publication verification record, or rehash the selected MP3 against its recorded audio hash, when current binary integrity matters.

For a missing or stale index, use the reported rebuild instruction:

```powershell
python system/scripts/query-loophole.py build
python system/scripts/query-loophole.py verify
```

The generated database is `retrieval/knowledge.sqlite3`. Build also refreshes [library-map.generated.md](library-map.generated.md); do not hand-edit that map. Build refreshes derived retrieval artifacts; it does not rewrite course sources. Search checks indexed catalog/publication freshness and selected source identity. Freshness errors require a rebuild; do not quote a stale snippet as current. Full archive integrity remains a separate hash audit. The database and local question library are deliberately Git-ignored; a GitHub checkout alone does not contain their data. Rebuild works when the captured files are present locally.

If Python or the generated database is unavailable, use the same hubs and source catalog with bounded `rg` searches; navigation remains usable. Ordinary `rg` skips the ignored question library. For that library only, search the known subtree with `--no-ignore`, then open the matching question file. Do not scan the entire vault with `--no-ignore`.

```powershell
rg -l -F -w --no-ignore -g README.md "PT101.S2.Q1" corpus/loophole-online/question-database/library
```

Run `verify` after rebuilding or changing retrieval behavior. It checks representative retrievals and source-limit safeguards; ordinary lookups do not require rerunning the suite. The receipt and query-proof files in `retrieval/` record indexed coverage, timings and observed checks.

## Resolve a source and its companion artifacts

Use `open` when you need the complete package rather than a search excerpt. It prints a JSON locator and artifact inventory; it does not launch a media player or read every artifact for you.

```powershell
python system/scripts/query-loophole.py open "Reverse Shuffle" --section RC
python system/scripts/query-loophole.py open "How to Camo" --kind lecture
python system/scripts/query-loophole.py open "How to Diagram Unless" --section LR
python system/scripts/query-loophole.py open "PT101.S2.Q1"
```

You can also pass an exact `identity` copied from a result. Identities distinguish kind and retained generation; question identities use the current citation. Preserve the full returned identity instead of constructing one from a title. A title can resolve to multiple formulations: inspect `source_generation`, `package_folder`, `indexed_records` and `parallel_versions`. Exact identity, current citation or title resolves first. If lexical search produces multiple candidate packages, `open` returns `resolved: false`, `ambiguous: true` and up to eight candidates, with instructional titles prioritized. Run `open` again using the intended exact title or returned identity. A broad activity name such as `Decaf` must not silently select a routine. With only one candidate, the command uses the top search hit and labels that fallback; confirm its title before relying on it. Parallel-version matches are title-based suggestions, not an exhaustive version history.

`artifacts` lists retained source, video, instructor audio, native captions, transcripts, written notes, excerpt, observed quiz, frames and verification/provenance files when present. Each item has a fresh `present` existence check, including ignored local files. `open` validates fingerprints for selected indexed text records and their retained text evidence. Artifact presence does not replace a binary checksum audit or establish listening verification. Missing roles do not prove a source never had that material: read its capture status and the library map's qualifications.

`open` validates indexed text members and their recorded text-evidence fingerprints. This does not read back every binary media hash. Question packages label original MP3, machine transcript, SRT, native word data and optional static title-card MP4 separately. The MP4 is a title card carrying original question audio, not an instructor lecture video; use each artifact's `present` flag and source qualifications.

For large sourcebooks, `reading_guide` supplies source-derived heading line ranges and total lines. Recognized original `Step N:` headings appear in `ordered_steps`, with exact-title workout identities under `drill_routes` when available. Use these to open the complete ordered procedure and its companion drills. The bounded outline can be marked `truncated`; it does not replace full instructions or prove every routine uses that heading convention.

Original course-day folders, dated conditional/RC batches and the older Camo transcript folder remain in place. Use notes for exact displayed wording, captions for captured spoken wording and the workout for its full procedure. Select the formulation the user requested and report material differences. A newer capture does not silently replace an older source, and a transcript-only record does not imply its parallel native package lacks media.

## Answer from the correct evidence

1. Identify RC, LR or a shared process, and whether the user needs a method, workout, routine, lecture or question.
2. Read the owning hub or obtain a few filtered search hits. Resolve ambiguous titles through the returned identity and local source path.
3. Read the full relevant source before explaining the drill. For workouts and routines, `instructions` provides exact authored procedural spans and explicit route gaps; follow every output page and required companion. A routine is an ordered sequence; one workout's instructions do not stand in for its whole routine.
4. Distinguish **captured written wording**, **native automatic captions**, **machine speech transcription**, and **compiled interpretation**. Automatic transcripts are unreviewed; a full extraction is not word-level accuracy verification.
5. Cite the local artifact and useful section, paragraph, line or timestamp. For a question include the current citation; preserve the old citation separately when supplied. MP3 and transcript files are companions to that question, not evidence of an independent answer-key audit.
6. Keep source errors, the silent recording, missing audio and subtitle-timing exceptions visible. Do not invent missing instructions or captions. A provenance URL never substitutes for the locally captured body.

Sources can disagree: the Decaf video notes, full workout and spoken transcript remain separate formulations. Use the formulation the user requested and report material differences. Vendor prescriptions remain attributed to Ellen Cassidy; they are not approved LSAT U curriculum merely because they are filed here.

## Keep one knowledge home as the library grows

Use the existing [LLM Wiki schema](../../system/schema/llm-wiki.md) and second-brain intake/query/lint workflows. Search before creating; update the existing subject rather than making a second summary. Preserve raw bytes, hashes and original paths, add reciprocal subject routes, refresh the source catalog through its owner, and rebuild the retrieval index after source/catalog changes. Do not edit generated files by hand. Log durable changes in the vault ledger. Retrieval itself does not authorize publishing, assigning a student, sending a message or changing a live service.

All three runtimes enter through their own root instructions and then this same page. Mirrored domain instructions are [AGENTS.md](AGENTS.md) and [CLAUDE.md](CLAUDE.md); the [Gemini adapter](GEMINI.md) delegates to that shared contract. Vendor configurations stay separate. The commands work from the vault root with local sources present; another checkout needs those source bytes and a rebuilt index. Existing sessions may need their normal instruction reload. Documented routes and passing local checks do not establish that a native Claude or Gemini session has actually run; report runtime-specific testing separately.
