---
type: source
subject: Loophole complete workout-page capture
created: 2026-10-15
updated: 2026-10-15
aliases: [Loophole workouts, Loophole workout details, Loophole prep map points, Workout dropdown catalog]
evidence: ../../raw/sources/loophole-workouts-2026-10-14-complete/overviews.json
sha256: 5321d515e1c8efbeb3bcaa259ca346680f122ba78828f7da67d8018808432be9
contradictions: []
sources:
  - ../../raw/sources/loophole-workouts-2026-10-14-complete/PROVENANCE.md
  - ../../raw/sources/loophole-workouts-2026-10-14-complete/SHA256SUMS
  - ../../raw/sources/loophole-workout-filters-2026-10-15/PROVENANCE.md
  - ../../raw/sources/loophole-workout-filters-2026-10-15/facets.json
  - ../../raw/sources/loophole-workout-filters-2026-10-15/options.json
tags: [llm-wiki, lsat, loophole, teacher-research]
---

# Every observed workout has its own full source record

Ellen Cassidy / Loophole Online. Publication dates unknown. Captured from Joshua's authenticated Codex browser beginning 2026-10-14 and completed 2026-10-15. This preserves the four-page rendered workout inventory as private teacher research. Filing source instructions does not approve their pedagogy, assign student work or publish vendor content.

## Find the instructions by section or prep stage

The [workout library](../../corpus/loophole-online/workouts/README.md) and [searchable expandable catalog](../../corpus/loophole-online/workouts/catalog.html) contain 84 observed workouts. Each has its overview, section types, prep stages, challenge index, full rendered detail text and original HTML. The catalog provides separate exact-text views and 71 captured inline instruction footnotes across 70 workout pages. [RC](../../corpus/loophole-online/reading-comprehension/README.md), [LR](../../corpus/loophole-online/logical-reasoning/README.md) and [shared methods](../../corpus/loophole-online/shared/README.md) route to this single source collection.

The 62 referenced prep-map URLs yielded 29 working rendered pages and 33 source error pages. All 33 errors have an actually observed, successfully captured same-topic URL under another prep stage. The catalog preserves both URLs and labels related working captures; it does not claim the broken URLs' unseen content was recovered or that all stage variants are identical. Consequently `complete_within_captured_inventory` remains false, while workout-detail and footnote coverage are true. [Verification report](../../corpus/loophole-online/workouts/verification.generated.json).

Eight linked instructional Google documents are saved through read-only `gws` exports: seven XLSX templates and the Thunderdome PT7.S1 document as both text and PDF, nine files total. Their URLs, formats, byte counts and SHA-256 values appear in the [attachment manifest](../../raw/sources/loophole-workouts-2026-10-14-complete/attachments.json). Image URLs and alt text remain metadata; image/video/audio bytes and every related lecture were not downloaded by this capture.

## Mentions in source

> "Break all the rules to prove you've mastered them" (Anti-PT overview)

> "This will help you if:" (expanded workout overviews)

> "Prep Map Points" (expanded workout overviews)

## Capture repair and verification remain explicit

The initial immutable [source generation](../../raw/sources/loophole-workouts-2026-10-14/PROVENANCE.md) is retained. Review found 19 HTML fields truncated by tool-output limits despite intact text. Those 19 complete HTML captures and two affected nested section fields were recovered, then archived as the separate `-complete` generation linked above. Originals were not overwritten. The safe viewer balances retained tags, removes executable markup and preserves semantic lists; original HTML is separate evidence.

Independent checks confirmed all 21 files in the corrected archive's SHA256SUMS match, all 84 detail records and 71 footnotes are present, no intake JSON contains `[Truncated]`, all nine attachment hashes match, and all seven XLSX containers pass CRC checks. Coverage `issues` is empty; the 33 broken source references remain explicitly recorded rather than silently resolved.

The local browser check confirmed 84 workout cards and 62 prep-map cards, RC + Translation filtering to 15 workouts, Cappuccino search filtering that subset to six, and Decaf's tenth step plus its goal footnote. Collapsed summaries contain no leaked source-content links. [Browser evidence](../../corpus/loophole-online/workouts/evidence/catalog-browser.png).

The [browser capture recipe](../../system/scripts/loophole-workout-browser-capture.md), [UI capture helper](../../system/scripts/loophole-workout-browser-capture.mjs), [Google export helper](../../system/scripts/capture-loophole-workout-attachments.py), and [catalog compiler](../../system/scripts/build-loophole-workout-catalog.py) make this repeatable. They use observed UI links and approved read-only exports, not guessed backend endpoints. These are written-page captures, not audio transcriptions or independent verification of instructor claims.

## Filter mapping correction (2026-10-15)

The earlier local viewer exposed Section Type and Prep Stage; the other three top-level source controls were not fully mapped. This correction adds all five: **Section Type**, **Prep Stage**, **Challenge Index**, **Workout Pack**, and **Useful Filters**. The shared-only **LR & RC** section choice is distinct from the broader LR and RC choices.

The [separate immutable filter capture](../../raw/sources/loophole-workout-filters-2026-10-15/PROVENANCE.md) records actual option labels and rendered membership sets. Challenge Index has Pretty Chill, Buckle Up and Ellen Whyyy; all 17 Workout Pack labels come from observed detail-page query links matched to the captured choices. Useful Filters exposes six dimensions: Level, Sections to Use, Timing Compatible, How to Time, Volume and Intensity. The first four use each workout's captured quick facts matched to observed option labels; Volume and Intensity use the captured live membership sets. No prose-based intensity/volume guesses are used.

All 84 workouts have each of these classifications. Twelve observed membership checks cover the three section choices and the three options in each of Challenge Index, Volume and Intensity; [the generated verification report](../../corpus/loophole-online/workouts/verification.generated.json) records coverage and any unknown mappings. Each primary workout document includes its classification table alongside the complete workout, footnotes, related prep content and readable templates. Original source captures and prior immutable archives remain unchanged.
