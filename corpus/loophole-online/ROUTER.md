---
type: synthesis
subject: Loophole filing and retrieval router
created: 2026-10-14
updated: 2026-10-18
aliases: [Loophole router, Where Loophole files belong]
contradictions: []
sources:
  - README.md
  - ../../system/schema/llm-wiki.md
---

# Route by section, then by the job of the material

[Start here](README.md). This file is the routing contract for the entire Loophole reference. The vault's [LLM Wiki schema](../../system/schema/llm-wiki.md) and existing ingest/query/lint skills remain authoritative. This is a domain router, not a second pipeline.

The [generated library map](library-map.generated.md) answers what is indexed, where each retained generation lives, and what is missing or qualified. Use it for a whole-library inventory; use the subject homes below for the full source. Its counts describe indexed text records, not unique videos.

For **how to perform a workout or routine**, run `python system/scripts/query-loophole.py instructions "exact title or identity"` from the repository root. It returns exact authored procedure, advice, examples, answer keys and footnotes with source paths and line ranges. Routine output includes ordered tasks, modifications and uniquely linked full workout spans; inspect `gaps` and read every page through `total_pages`. Use `--page` or the returned next-page suffix after the normal script prefix. This is a selected source-span view, not the entire sourcebook. See the [procedure reading guide](AI-RETRIEVAL.md#read-a-complete-workout-or-routine-directly).

## Choose the subject home

| Material | Owning route | Filing decision |
|---|---|---|
| Passage translation, Decaf, Cappuccino, comparisons, RC stems/answers | [RC](reading-comprehension/README.md) | Link the exact method/lecture/example and its notes. |
| Stimulus reasoning, CLIR, conditionals, assumptions and LR types | [LR](logical-reasoning/README.md) | Group by reasoning topic; distinguish explanation from worked example. |
| RTQ mechanics, vocabulary, memory checks, routines and review used in both | [Shared](shared/README.md) | One shared explanation; link section-specific applications rather than copying it twice. |
| A mixed anthology | [Source catalog](source-catalog.generated.md) | Preserve the anthology and link relevant sections from both hubs. Do not pretend the full file belongs exclusively to one section. |
| A screenshot/checkpoint | [Source catalog](source-catalog.generated.md) | Preserve image and separate transcription; record unknown day or URL explicitly. |
| Workout cards, complete workout-detail instructions and associated prep-map points | [Workout library](workouts/README.md) | One record per observed workout URL; use the [catalog](workouts/catalog.html) to filter LR/RC and prep stage. Keep broken source links, related successful captures and coverage limits explicit. |
| Ordered workout sequences and full embedded sourcebooks | [58 routines](routines/README.md) | Preserve schedule order, repeats, other tasks, routine modifications and the one authored blank. |
| LR question metadata, Correct CLIR, MP3 and transcript | [Question database](question-database/README.md) | The portable reading home is `question-database/library/`. Desktop remains the preserved processing archive. |
| Book Extras Bootcamps and interactive question feedback | [Bootcamps](bootcamps/README.md) | Preserve chapter/drill/question order, exact wording, choices, observed responses and feedback. Evidence lives in `raw/sources/loophole-bootcamps-2026-10-18/`; `system/scripts/package-loophole-bootcamps.py` owns derived pages and catalogs. Capture completion is separate from adopting these drills as LSAT U curriculum. |
| RC activity demonstrations, including Decaf, Cappuccino, Caffeinated, Party Tricks, Camo and Reverse Shuffle | [Activity demonstrations](reading-comprehension/activity-demos.md) | Routes original course-day media and dated native packages together without relocating them. Instructions, demonstrations and captured companion status remain separate. |
| How to Camo across retained generations | [Activity demonstrations](reading-comprehension/activity-demos.md), [older transcript](<../../Loophole Lecture/Camo/how-to-camo-transcript.md>) and [capture record](<../../Loophole Lecture/Camo/README.md>) | Keep the older transcript-only capture, newer native demo package, older notes and Camo Review workout distinct. Use `open "How to Camo"` to inspect package artifacts and suggested parallel versions. |
| Prep-map instructions or capture errors | [Prep-map index](workouts/prep-map-points/README.md) | Working text/HTML is local; source errors remain explicit rather than invented. |

[Conditional reasoning](logical-reasoning/conditionals/README.md) owns the conditional source comparison and routes native lecture artifacts, observed in-video questions, separate Book Extras practice and full homework. Original captures remain in `Loophole Lecture/Conditional Reasoning 2026-10-18/`; its processor owns derived package files.

## Keep four kinds of material clear within each subject

1. **Methods and drills:** procedures, timing targets and progression criteria. Attribute vendor targets, preserve versions and link exact written instructions.
2. **Lectures:** retain the plan's day and sidebar order. Titles are original displayed titles; filenames may remove Windows-invalid characters.
3. **Question strategies:** link the stated task, lecture and notes; avoid silently substituting a general rule for the source's actual claim.
4. **Worked examples:** identify PT/section/passage/question and pace. A captioned instructor answer is not independent answer-key verification.

Do not create empty category folders. The subject README provides these routes until enough distinct compiled content earns a separate page.

## Preserve one source identity and multiple useful routes

- Existing source/media paths stay valid. Navigation lives here; original captures stay under `Loophole Lecture/` and recovered evidence under `raw/sources/`.
- New lecture evidence is copied byte for byte into `raw/sources/loophole-rc-2026-10-14/`, with hashes and provenance. Media stay in their original folders. No second recording copy is required to make a topic route.
- Notes, native captions, rendered transcript, screenshots and editorial comparisons are different artifacts. Keep the original notes HTML as well as readable text.
- One source may have links from several subject hubs; that is cross-reference, not a second source or a second transcript.
- The [generated catalog](source-catalog.generated.md) and [JSON identities](source-catalog.generated.json) map every retained source to its home. Rebuild using `system/scripts/organize-loophole.py`; its current batch list is explicit. Use `python system/scripts/organize-loophole.py --catalog-only` to refresh navigation from existing captures without writing raw evidence. Review changes to that list before future batch imports.
- Never hand-edit the four `*.generated.md` instructor collections. Preserve existing citations and use their owning generator for content changes.

## Fast retrieval for Claude, Codex and Gemini

The [AI retrieval guide](AI-RETRIEVAL.md) is the compact operating entry. Directory-scoped [Codex instructions](AGENTS.md) and [Claude instructions](CLAUDE.md) share the same retrieval contract; the [Gemini adapter](GEMINI.md) delegates to it. All three routes use the same generated local full-text index and authoritative source files. No runtime needs to scan the whole library or open the website to answer a captured-content question. Keep runtime configuration separate and maintain this one shared retrieval procedure.

Use `python system/scripts/query-loophole.py open "title or citation"` from the repository root to resolve an exact title, current question citation or returned stable identity. Optional `--section` and `--kind` filters match search. The JSON result lists package members, companion artifact paths with current existence flags, retained generation and suggested parallel versions. It does not launch the files. Broad names may return `ambiguous: true` with candidate packages instead of silently selecting a routine. Choose an exact title or identity and run `open` again. Confirm the title when resolution falls back to one search hit; open the selected full artifact afterward. See the [retrieval guide](AI-RETRIEVAL.md#resolve-a-source-and-its-companion-artifacts) for examples and limits.

Choose RC, LR or shared material deliberately. A question citation uses the database lookup route; a workout or routine uses its complete sourcebook; exact written lecture instructions use the notes artifact, while spoken wording uses the transcript. The current question database is LR-only. An RC question citation may have a lecture example without having a database record.

CLI `search` returns compact discovery results with `open_hint` and artifact counts; `--details` includes full inventories. `open` adds source-derived `reading_guide` heading ranges and recognized ordered steps for navigating long sourcebooks. Preserve the complete sequence and read the original step body; the outline is a locator, not a rewritten routine. Question companions explicitly distinguish MP3, machine transcript, SRT, word data and static title-card MP4. A title-card MP4 is not a lecture.

`python system/scripts/query-loophole.py build` owns the retrieval index and generated library map. Stable identities distinguish indexed kinds and generations; copy the returned identity rather than guessing it. A companion existence check does not verify its bytes or establish that every possible artifact was captured. Preserve source-specific verification status.

The search index is a disposable cache, not the source of truth. Preserve returned source paths, capture type, timestamps and availability flags. Open the relevant complete file for the answer, report a genuine source gap or mismatch, and rebuild a stale index through its owning command. Source errors, silent recordings and unavailable subtitles are distinct from missing search results. Never fill a source gap by inventing a lecture, question or answer.

## When adding or answering

For retrieval, start at [README](README.md), choose RC/LR/shared, then the exact source. For new source intake use second-brain-ingest: preserve/hash, read, compile into the existing subject, update the relevant hub and catalog, add source summary, refresh the wiki catalog and log. Do not infer adoption or assign work to a student from filing alone.

For material that contradicts an existing source, link both formulations and leave the conflict explicit. The full Decaf workout, nine-step video notes and spoken-caption version remain separate; the full Cappuccino and 35-minute versions remain separate. Preserve reviewed pages and all original source bytes.

## Files stay usable without the website

Workout and routine documents include their captured instruction bodies. Question READMEs include full written Correct CLIR and available speech transcripts; the MP3 and optional subtitle files live beside them. A source URL is provenance, never a substitute for those bodies. No recording was exposed for 4,302 question rows; PT2.S4.Q19 is a separately proven silent source. Automatic caption/ASR wording is unreviewed. Two complete speech transcripts have unusable native subtitle timing, explicitly labeled.

## Retrieval checks that must keep working

- Exact Cappuccino instructions: README → RC → Cappuccino → full notes text/HTML and original video.
- Sufficient Assumption example: README → LR → assumptions → existing package and provenance caveat.
- Day 7 order: README → RC → Day Seven → all twelve title folders.
- Automatic versus exact wording: the source record identifies notes text, captions and listening-verification limits.
- Old method reference: README → method library or complete catalog; historical links still resolve.


## Ordered routines and complete sourcebooks

[All 58 routines](routines/README.md) contain every captured schedule step in order, including repeated workouts and other tasks, plus full embedded workout instructions and resources. Use the searchable catalog linked there to filter by section impact, prep stage, challenge index, routine progression and useful filters. One confirmed source blank remains explicitly marked.
