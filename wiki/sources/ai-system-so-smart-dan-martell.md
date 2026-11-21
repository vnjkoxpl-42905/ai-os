---
type: source
subject: Dan Martell video on an Obsidian "AI brain" with identity files, seven folders, meeting extraction and a nightly consolidation job
created: 2026-10-14
updated: 2026-10-14
aliases: ["This AI System Will Make You So Smart It's Almost Unfair", Dan Martell second brain video, Dan Martell AI brain]
tags: [ai-workspace, second-brain, obsidian, meetings, consolidation]
evidence: "../../raw/sources/clips/ai-system-so-smart-dan-martell/This AI System Will Make You So Smart It's Almost Unfair.md"
sha256: 67c3b63f0a0a90c7d4b5ea2a3711a20f0e294be741583ebacbff97cdc7a16ae2
sources: [../../raw/sources/clips/ai-system-so-smart-dan-martell/PROVENANCE.md]
contradictions: []
---

# Dan Martell's AI brain: ai-os has his structure; his nightly cleanup can only run here as a read-only report

"This AI System Will Make You So Smart It's Almost Unfair" is a YouTube video by Dan Martell ([YouTube](https://www.youtube.com/watch?v=b4d32pBa3UY)). The channel is inferred from the go.danmartell.com links. The publication date is unknown; the inbox file was last modified 2026-10-14. The full description, which includes his three prompts, and the auto-caption transcript (captions run to 11:36) were read on 2026-10-14.

Evidence: [archived clip, provenance and hashes](../../raw/sources/clips/ai-system-so-smart-dan-martell/PROVENANCE.md). SHA-256 `67c3b63f0a0a90c7d4b5ea2a3711a20f0e294be741583ebacbff97cdc7a16ae2`.

## What he says

- **Go pro (0:20).** Pay for an AI plan; he says free tiers give older, slower models. His percentages of paying users are unsourced.
- **Install the brain (0:44 to 2:15).** Chat memory is weak, so give the AI a permanent place to read from: your own files in your own structure. Three options: Google Drive (limited), Notion (he calls it AI native), Obsidian (Markdown, free, readable, with a graph view). He uses Obsidian.
- **Give it an identity (2:21 to 4:12).** Three files. `user.md` is who you are: role, communication style, frameworks, values. `soul.md` is how the AI should act: voice, tone, values; his says be direct, no hedging words, try to solve a problem before asking. `identity.md` is who the AI is; he let his assistant name itself after two weeks. Do not write these yourself: have an AI interview you, then draft them. The prompt is in the description. A playbook pitch follows (4:38).
- **Wire the brain before feeding it (5:02 to 6:58).** He says setting up folders took his answer accuracy from 60% to 85%. Seven folders: people, projects, decisions (what, how, alternatives), companies, meetings, daily (three to five lines a day), knowledge (insights, frameworks, quotes). An eighth, maps of content (MOCs), holds summary files that link work spread across folders; build one when a topic gets messy, not on day one.
- **Feed the brain (7:25 to 8:38).** Connect your systems and have the AI extract only what matters into the folders, the way a real brain filters noise. His meeting app auto-transcribes and applies a custom template: decisions (what, by whom, why), commitments (who promised what, by when), preferences (how people work and communicate), key insights. Output is Markdown in the meetings folder, named by date and meeting.
- **Compound the brain overnight (9:14 to 10:36).** Like sleep, the brain should organize, consolidate, connect and prune. The manual version is a prompt: read what was added today, find orphan mentions (people, projects, companies with no file), create those files, consolidate duplicates, update the MOCs, flag strategic items for tomorrow. He automates it as a Claude scheduled task at 11 pm and says the graph visibly grows each night. His claim: more links give a stronger context signal.
- **Payoff (11:19).** With enough context, "send the invite to John" works because John is the most-linked John in the vault.

## Mentions in source

> "I need you to find orphan notes, mentions of people, projects, companies that don't have their own files" (9:44)

> "you have to consolidate duplicates, you have to update the relevant map of contents with new links" (9:44)

> "you build them when a topic seems to get messy" (6:28)

> "Two, commitments, who promised what, by when?" (8:19)

## How it compares with ai-os (interpretation)

Checked on disk 2026-10-14. Decisions are recorded in the [second-brain adoption ledger](../../references/ai-workspace/second-brain-adoptions.md).

| His idea | Here | Verdict |
|---|---|---|
| `user.md`, `soul.md`, `identity.md` | [About Joshua](../../context/about-me.md), the identity and voice sections of `CLAUDE.md`, [teaching voice](../teaching-voice.md) | Already |
| Seven folders plus MOCs | Domain homes (`students/`, `decisions/`, `wiki/`, `corpus/`, `context/`) and hub indexes (`wiki/index.md`, `corpus/index.md`, `students/README.md`, the [AI workspace hub](../../references/ai-workspace/index.md)) | Already |
| Meeting template: decisions, commitments, preferences, insights | `transcript-intake` distillation gains commitments and preferences fields | Adopted |
| Nightly job that creates pages, merges duplicates and prunes | Conflicts with "automation writes only generated files", with never-delete, and with keeping conflicts explicit. The read-only part, a lint report that lists entity candidates, is kept | Conflicts; read-only part adapted |
| Orphan mentions become entity candidates | Lint lists candidates; a human approves each one | Adapted |
| Have the AI interview you to draft the identity files | `grill-me` runs this kind of interview; how `context/about-me.md` was first drafted was not checked | Not yet evaluated |
| A daily folder of three to five lines a day | `wiki/log.md` and `wiki/hot.md` record system work, not Joshua's day | Not yet evaluated |
| A general people folder | Only students have folders; there is no root `people/` | Not yet evaluated |

- **His structure is already here under other names.** People map to `students/` (students only), decisions to `decisions/log.md`, meetings to student transcript folders, knowledge to `wiki/` and `corpus/`, MOCs to the hub indexes.
- **The nightly job is the part that cannot run as written.** It creates, merges and prunes without review. Here, unattended automation writes only generated files, nothing is deleted without Joshua's word, and conflicting notes stay side by side until he decides. What survives is the useful half: a report of orphan mentions and duplicate candidates for a human to act on.
- **Commitments and preferences are the real gain.** Session transcripts already capture what happened; asking for who promised what, and how each student likes to work, gives follow-ups a concrete source.

Related: [Nate Herk's LLM wiki demo](fable-5-karpathy-llm-wiki-nate-herk.md), [GD4AI wiki plugin](gd4ai-obsidian-llm-wiki.md), [second-brain levels](../../references/second-brain-levels.md), [his voice-guide video](make-ai-sound-like-you-dan-martell.md), [Tina Huang's Obsidian levels](obsidian-in-24-minutes-tina-huang.md).

## Limits

- Auto-captions. "Grainola" is almost certainly Granola, the meeting-notes app; the product was not checked. "Talk like Dick" (3:33) is probably a mis-hearing, perhaps of "Dan". The assistant's name "Kai" is a caption spelling.
- His figures are unverified: 60% to 85% accuracy after adding folders, the share of paying AI users, and "60 seconds" for the nightly prompt.
- Whether Claude scheduled tasks can run his nightly prompt as described was not checked.
- The on-screen vault and graph were not visible in the clip text.
