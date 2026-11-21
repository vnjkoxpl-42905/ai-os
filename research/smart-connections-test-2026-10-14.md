---
type: research
subject: Five-question retrieval test, index route versus Smart Connections (AQ-010)
created: 2026-10-14
queue_item: AQ-010
status: index column done; Smart Connections column waits on a full embedding run
---

# Smart Connections test: the index found all five pages, Smart Connections could not be tested yet

Queue item AQ-010 asks for five real lookups answered two ways: through the index route (catalog, aliases, one hop) and through Smart Connections. The index route is done below. The Smart Connections column is left for Joshua, because its index is nowhere near built (see "Why the Smart Connections column is blank").

## The logged miss did not exist

The queue item says `wiki/log.md` holds one `Miss:` line. It does not. The only match is line 3225, which describes the `Miss:` line format added to `second-brain-query`. No retrieval miss has been logged yet. All five questions below are new ones, worded the way Joshua talks rather than the way the pages are titled.

## The five-question table

| # | Question (Joshua's wording) | Right page | Index route (catalog, aliases, one hop) | Smart Connections in Obsidian |
|---|---|---|---|---|
| 1 | What did we decide about apology emails? | `wiki/teaching-voice.md`, section "The apology / accountability move" | **Found on the hop.** "apolog" in `wiki/index.md` hits only the `automation-backlog` line (the 19% apology tax). Its Related line links `[[teaching-voice]]`, one hop. `decisions/log.md` has no apology entry. | Joshua to fill |
| 2 | Why does a student see a slot as "just taken" when nothing is booked? | `wiki/LSATU-BOOKING-POLICY.md`, section "When a student reports 'That time was just taken'" | **Found on the hop.** "slot" hits the Cal.com stuck-bookings line first (the wrong page). That page links `[[LSATU-BOOKING-POLICY]]` at line 12. The booking-policy catalog line itself carries no "slot" or "taken" wording. | Joshua to fill |
| 3 | A student tried to pay but the time is still blocked. | `wiki/CALCOM-STUCK-BOOKINGS.md` | **Found directly.** The catalog line says "unpaid bookings hold slots invisibly". | Joshua to fill |
| 4 | How much of my email time goes to saying sorry? | `wiki/automation-backlog.md` (the 19% "apology tax") | **Found directly.** | Joshua to fill |
| 5 | Which LR questions still have no written solution? | `wiki/lr-missing-explanations.md` | **Found directly.** "the 772 LR questions with no, partial, or never-loaded explanations". | Joshua to fill |

Index route score: 3 of 5 found directly from the catalog, 2 of 5 on the one allowed hop, 0 missed. Neither of the two right pages has aliases (`aliases: []`), and adding one alias would turn each hop into a direct hit: `apology emails` on `teaching-voice.md`, and `just taken` on `LSATU-BOOKING-POLICY.md`.

## Why the Smart Connections column is blank

Checked 2026-10-14, read-only:

- **Obsidian was closed.** I launched it on the ai-os vault so the `obsidian` CLI could reach the plugin. It is still running. Smart Connections reported `state: loading` throughout, with 15,329 sources known and 6 vectors loaded in memory.
- **The saved index is almost empty.** `.smart-env/` holds vectors for **69 of about 15,329 sources**: mostly files edited on 2026-10-14 (root rules, skills, `wiki/log.md`, the action queue, synced conversation exports). **None of the five right pages has a vector.** Settings: model `TaylorAI/bge-micro-v2` (384 dimensions), blocks over 200 characters.
- **What a partial run returned.** I embedded the five questions with the plugin's own model and ranked them against the 69 saved vectors. The top results were `wiki/CONSULTATION-FOLLOW-UP-TEMPLATE.md`, `skills/claude/morning-brief/SKILL.md`, `decisions/log.md`, `context/priorities.md` and `wiki/log.md`, with scores from 0.50 to 0.66. That reflects which files are embedded, not retrieval quality. It is not evidence for or against Smart Connections.
- **Exclusions do not seem to be applied.** `smart_env.json` lists `raw/` and `setup/github-sync/state/` under `gitignore_exclusions`. But `raw/inbox/README.md` and eight `setup/github-sync/state/conversations/` exports are among the embedded files. If agents ever use this index, chat exports and raw captures would compete with compiled pages.

To fill the column: leave Obsidian open until Smart Connections finishes embedding (its status bar shows progress). Then, for each question, open a blank note, type the question, and check whether the right page appears in the Connections pane's top five. Or ask an agent to rerun the read-only ranking script, which uses the plugin's own model through `obsidian eval`.

## The decision Joshua makes

1. Fill the Smart Connections column, or accept the index result as enough.
2. Choose the role: **an Obsidian-only aid for you** (my recommendation: the index route went five for five, and the embedded set currently includes raw captures and chat exports), or **a retrieval step for agents**, and if so where it goes in the retrieval order.
3. Optional: add the two aliases above. Each costs one line and removes a hop.

Whichever role he picks still has to be recorded in `decisions/log.md` and then applied to `references/second-brain-levels.md` (level 3 row) and the embeddings row of `references/ai-workspace/second-brain-adoptions.md`. This run did not edit any of those files.
