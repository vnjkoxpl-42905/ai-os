# AI-setup and second-brain organization: one vault or several: Brainstorm / Discovery Notes
Date: 2026-11-20 · Goal: decide how to organize Joshua's AI-setup material (clips, sources, references) and what to fix first, so Obsidian is fast and clips have one clear home.
Status: in progress
Context sources: [wiki/second-brain-one-vault-vs-many.md](../wiki/second-brain-one-vault-vs-many.md), [system/schema/llm-wiki.md](../system/schema/llm-wiki.md), [references/second-brain-levels.md](../references/second-brain-levels.md), [decisions/log.md](../decisions/log.md), [wiki/log.md](../wiki/log.md) (2026-11-20 ingest entry)

## Summary / key decisions
Confirmed by Joshua: AI-setup material is mostly for agents, occasionally read by him (Q1). The 2026-10-14 separate-vaults decline is open.

Agent recommendation (NOT confirmed; awaiting Joshua's yes), 2026-11-20:
1. Keep ONE vault (`dev\ai-os`) as the system of record. Split inside it, not apart: a small AI-setup hub (promote `references/ai-workspace/index.md`) with its own short index, and a separate inbox subfolder for AI-setup clips. No bulk moves.
2. Backups first (Drive sign-in; a backup commit of own work only).
3. Shrink `wiki/index.md`: keep the 237 non-Karpathy lines (about 13,200 tokens), move the 3,842 Karpathy rows into a folder-level index, fix the generator. Measured: about 290,000 tokens now vs about 13,200.
4. Hide `wiki/sources/karpathy/` from Obsidian (ignore filter; nothing deleted). Split `skills/INDEX.md` (about 85,000 tokens, too big to read whole).
5. Rule: every router and index must be small enough to read whole. Retrieval without RAG: router, then folder index, then page; scripts for counting and freshness questions; plain keyword search if needed.
6. Revisit a second vault only if Obsidian is still slow after 1 to 4, or Joshua wants a separate reading space.
Karpathy-teach demo (read-only, chars divided by 4 as token estimate, quality of answers not tested): see this session's 2026-11-20 transcript.

Standing input from Joshua, 2026-11-20 (user-confirmed): the 2026-10-14 decline of "separate vaults per data type" was not a definitive rule; he was still learning and wants the best setup. The setup is open.

Facts checked on disk 2026-11-20 (not decisions):
- Committed `wiki/index.md` is 13,203 bytes. The working copy is 1,159,899 bytes (regenerated 07:26 today, uncommitted): about 3,842 rows for `wiki/sources/karpathy/` plus 167 hand-curated lines that are not in the commit.
- After the current Obsidian ignore filters, about 17,000 markdown files remain visible: corpus 5,460, skills 4,213, wiki 4,007 (3,841 Karpathy), setup 1,093, students 772, Loophole Lecture 432, brainstorms 394.
- Google Drive mirror not running (no G: drive); 6,262 changed or untracked paths in git.
- Cause of the current Obsidian slowness: not measured. The 2026-10-23 stall was a different cause (473 MiB of chat markdown, since moved out).

## Q&A log
### Round 1
Re-asked in plainer words after Joshua (2026-11-20) said he did not know what "cross-links", "Karpathy mirrors" and "the index" meant. Definitions given: cross-link = a link inside a note to another note (works only inside one vault); Karpathy mirrors = `wiki/sources/karpathy/`, 4,258 machine-made note copies of Karpathy's public GitHub files; index = `wiki/index.md`, the master table of contents. Questions unchanged in substance; still unanswered.
#### Q1 - Who reads the AI-setup material
- Asked: do you read these clips and notes yourself in Obsidian, or is it mostly there for agents to learn from?
- Recommended: none (fact about how Joshua works).
- Captured (Joshua, 2026-11-20): "mostly it's for agents to learn from, but also I might read it once in a while."
- Joshua also asked, instead of answering Q2 to Q7 himself: what do the sources recommend, and what would I recommend. His stated aim: the smartest, most organized, most supercharged setup; one CLAUDE.md that knows which vault it points to; no RAG; draw on all the sources (including Every Level and Tina Huang's video) and on the Karpathy teaching skill; give a best default layout for his actual tasks. Q2 to Q7 therefore remain unanswered, answered by recommendation below pending his yes.
#### Q2 - Cross-links
- Asked: do AI-setup notes need to link to LSAT, student or business pages (links do not work between two vaults)?
- Recommended: none (fact).
- Captured: pending
#### Q3 - Slowness symptom
- Asked: when is Obsidian slow: opening the vault, search, graph view, or typing in a note?
- Recommended: none (fact).
- Captured: pending
#### Q4 - Karpathy mirror pages
- Asked: do you ever open anything under `wiki/sources/karpathy/` (about 4,250 generated copies of Karpathy's GitHub files)?
- Recommended: none (fact).
- Captured: pending
#### Q5 - Safety before changes
- Asked: sort out the backups (Drive sign-in, a backup commit) before moving or hiding anything?
- Recommended: yes, backups first; no one else's uncommitted work gets committed without his word.
- Captured: pending
#### Q6 - The 1.16 MB index
- Asked: treat it as a bug: keep the 167 curated lines, replace the 3,842 Karpathy rows with one hub link, and change the script so it stops regenerating them?
- Recommended: yes.
- Captured: pending
#### Q7 - Where clips land
- Asked: keep agents compiling clips into wiki pages, and give AI-setup clips their own inbox folder so they stop mixing with LSAT clips?
- Recommended: yes; it works under any vault outcome.
- Captured: pending

## Open flags (pending input)
- Catalog regeneration and the `wiki-maintenance.py --index` behaviour: no owner yet; blocked on Q6.
