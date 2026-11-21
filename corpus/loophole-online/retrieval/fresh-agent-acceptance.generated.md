# Fresh-agent Loophole retrieval acceptance

Test date: 2026-10-18 (America/Toronto).

## Independent baseline

A new agent with no conversation history received nine realistic source requests. It received no library paths, commands or retrieval directions. It independently followed workspace instructions, opened local source bodies, and checked relevant media paths. No live website was used and no original source was changed.

**Result: 9/9 source-finding and opening tasks passed.** Workarounds exposed four usability gaps. File existence, sizes and selected MP4 header checks do not establish playback, listening or fresh checksum verification.

| Request | Actual evidence opened | Result |
|---|---|---|
| Decaf instruction lesson | Day One Decaf written notes and native captions; original video/audio exist | Pass; bare `Decaf` initially selected a mixed routine, so the agent used the exact title |
| Cappuccino comparative Passage B demo | Day Six Passage B full captions; ordered demo titles and original media | Pass |
| Caffeinated introduction, Passage A and failsafes | New RC activity-package captions and full written failsafe instructions; original media | Pass |
| Conditional homework | Conditional Rehab ordered tasks and full bounded procedural source sections | Pass; 8,271-line sourcebook required a manual heading scan |
| Unless lecture-attached quiz | Three questions, choices, observed responses and final feedback | Pass; historical Q2 mismatch remained qualified; final choices A/B/C separately verified in capture |
| Referential Phrasing Book Extras | Full five-question drill and retained earlier comments | Pass; explanation gaps and gated stimuli remained explicit |
| How to Camo generations | Native captions/notes/media plus older transcript-only README and transcript | Pass |
| PT101.S2.Q1 | Full question README, written Correct CLIR and speech transcript; MP3, SRT and title-card media exist | Pass; question `open` omitted useful companion paths, so the agent followed README links |
| Reverse Shuffle | Full written notes and native captions; original media | Pass |

The conditional homework request was explicitly interpreted as **The Conditional Rehab Routine**. Its ordered tasks are Unless Practice, Question Stem Training (3+ sections), Acronym LR Section and Unofficial Diagramming Marathon. Written CLIR and spoken examples remain separate sources. Missing substantive feedback is not reconstructed.

## Baseline friction

1. `search "Decaf Cappuccino Caffeinated" --kind lecture --section RC --limit 12 --excerpt 130` returned about 13,556 tokens / 998 lines, mostly repeated artifact inventories. The agent manually projected JSON fields.
2. Broad lexical OR results favored progression lessons. Bare `open "Decaf" --section RC` chose AC Primer + Decaf Routine, albeit labeled as fallback. The agent supplied a more specific title.
3. The complete Conditional Rehab sourcebook was too long for an unbounded read; complete instructions were recoverable through manual section scans.
4. Question records exposed fewer companion artifacts through `open` than lecture packages. README links provided the missing access route.

## Source routes

- [Agent retrieval guide](../AI-RETRIEVAL.md)
- [Generated library map](../library-map.generated.md)
- [RC activity demonstrations](../reading-comprehension/activity-demos.md)
- [Conditional sources and homework](../logical-reasoning/conditionals/README.md)
- [Question records](../question-database/README.md)

## Repairs and second blind test

The engine now emits compact search results by default, with `--details` retaining full inventories. The exact baseline query shrank from 54,218 characters / 998 lines to 19,789 characters / 362 lines (63.5% fewer characters), preserving all twelve result identities and qualifications. Ambiguous short-name opens return explicit candidates, sourcebooks expose heading ranges and ordered workout routes, and question records expose original audio, text, subtitles, word data and clearly labeled title-card video with fresh presence checks.

A second new agent, again without parent paths or command hints, retried four difficult requests. **4/4 passed.** It independently handled Decaf ambiguity, found the three demo families, read all four conditional homework procedures and footnotes, and opened the question README/transcript/subtitles with all companion files present. It checked 21 matching demo/method folders: video, audio, VTT and README were present in each.

The second agent still used manual heading extraction for large workout files. A direct source-preserving `instructions` view was added to eliminate that remaining workaround. It returns authored instructions, advice, examples, answer keys and footnotes, with exact source paths and line ranges. Routine-specific modifications stay attributed separately from canonical linked workout procedures. Pagination preserves complete blocks and explicitly identifies any continuation or gap.

## Final blind homework acceptance

A third agent with no conversation history received only the practical homework request and normal workspace instructions. It independently found the new command and opened **22 complete blocks, page 1 of 1, no gaps and no oversized block**. It read all four procedures, the Unless answer key, full Acronym LR process, routine-specific advice, prior/new-section conditions and both LawHub footnotes. **No manual extraction script, temporary file, browser or parent retrieval directions were needed.**

The agent found one imprecise shortened-title documentation example. The example now uses the exact source title:

```powershell
py system/scripts/query-loophole.py instructions "The Conditional Rehab Routine" --kind routine
```

The machine-readable JSON format suits agent retrieval; it is not a new human-facing reader. Templates and walkthrough videos remain separate companion resources, rather than being silently treated as part of the written procedure. Native captions, unavailable stimuli and feedback qualifications retain their original limits.

Independent read-only review checked each returned instruction block against its claimed source line range and found no mismatch. Final automated verification passed **33 grouped checks and seven negative safeguards** on **5,613 indexed records**. Final verified engine SHA-256: `888ffe6a973351da7bcb4ce1d8f6b96528720bfa729e7ac95c2f767d7d2cfe3d`.

**Outcome:** baseline 9/9 source tasks passed, four friction areas repaired, second blind retry 4/4 passed, and final blind homework acceptance passed without manual extraction. Original sources and Joshua's curriculum were unchanged.
