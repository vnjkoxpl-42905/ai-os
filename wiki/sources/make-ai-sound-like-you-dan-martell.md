---
type: source
subject: Dan Martell video on making AI write in your voice with a "brain system" interview and a per-medium voice style guide
created: 2026-10-14
updated: 2026-10-14
aliases: [How to Make AI Sound EXACTLY Like you, Dan Martell voice style guide, Dan Martell brain system, AI voice cloning]
tags: [ai-workspace, voice, writing, prompts]
evidence: "../../raw/sources/clips/make-ai-sound-like-you-dan-martell/How to Make AI Sound EXACTLY Like you.md"
sha256: 877ad5657c44d990438eb9703e88b9de4288c2b5d24cac733a6deaaaab85f49b
sources: [../../raw/sources/clips/make-ai-sound-like-you-dan-martell/PROVENANCE.md]
contradictions: []
---

# Dan Martell's voice method: separate guides per medium, built from real samples, and the human stays at the start

"How to Make AI Sound EXACTLY Like you" is a YouTube video by Dan Martell ([YouTube](https://www.youtube.com/watch?v=wtaRjOFqdyU)), inferred from the go.danmartell.com link and his Instagram handle. The publication date is unknown; the inbox file was last modified 2026-10-09. The description, which carries his three prompts, and the auto-caption transcript (to 17:50) were read in full on 2026-10-14.

Evidence: [archived clip, provenance and hashes](../../raw/sources/clips/make-ai-sound-like-you-dan-martell/PROVENANCE.md). SHA-256 `877ad5657c44d990438eb9703e88b9de4288c2b5d24cac733a6deaaaab85f49b`.

## What he says

- **Build the brain (0:43 to 4:16).** AI needs your material first: past writing, playbooks, and from now on recordings of meetings, calls, decisions, voice notes and AI chats, all dropped in one home (Obsidian, Notion or Drive). He names Granola, Pocket and Wispr Flow as capture tools.
- **Teach it to think like you (4:27 to 7:58).** Connect email, Drive, Notion, Slack and meeting notes so it sees your beliefs and the stories behind them. Then run his "brain system" prompt: gather from connected tools, interview you in at least four rounds for points of view, contrarian takes and the stories behind decisions, and output one document every chat starts with.
- **Make it sound like you (7:58 to 12:27).** Feed real writing separately per medium, because email, Slack, texts and on-camera speech differ. Have the AI find patterns: sentence length, punctuation, favorite words, capitalization, openings, closings, sign-offs. Add a list of words you never use ("delve", "leverage", "robust", "quietly"). His voice-style-guide prompt pulls the 20 most recent emails, Slack messages and documents, analyzes each medium separately, asks instead of guessing, and outputs a guide to paste into any chat. He still reviews everything. He cites survey figures on AI distrust (20% to 40%, 54% for Gen Z), unsourced.
- **Keep the human part (12:36 to 17:50).** The better it sounds, the bigger the risk of a mistake that costs trust. He cites an MIT essay study on weaker engagement in the AI group. His rule: use AI to pull ideas from you, not push them onto you; be at the inception of every idea. His newsletter prompt: name the topic, let it gather context, have it interview you, then write with the brain system and voice guide.

## Mentions in source

> "Keep each medium separate so my email voice and my Slack voice don't blend together." (description, Voice Style Guide prompt)

> "If something isn't in the samples, ask me instead of guessing." (description, Voice Style Guide prompt)

> "I would never let something go out that was written by AI that makes no sense to me." (11:55)

> "we have to use the AI to pull from you, not push onto you." (15:38)

## How it compares with ai-os (interpretation)

Checked on disk 2026-10-14. The voice files were read, not edited.

| His idea | Here | Verdict |
|---|---|---|
| Voice guide built from real samples | [Teaching voice](../teaching-voice.md) was tested against 944 messages Joshua authored (mid-2025 to mid-2026, analyzed 2026-07-18), with quoted evidence | Already here, and on a larger sample than his 20 per medium |
| Separate guides per medium | Teaching voice has three registers (coaching for email, teaching content, brand); [Reddit chat voice](../reddit-chat-voice.md) covers DMs; the [LSAT teaching voice standard](../../references/lsat-teaching-voice-standard.md) covers lesson and teleprompter writing | Already here |
| Banned-words list | `CLAUDE.md` Voice section and the global never-use list, plus [copy corrections](../COPY-CORRECTIONS.md) | Already here |
| "Brain system" interview | [About Joshua](../../context/about-me.md) and the `grill-me` skill, which can run exactly this kind of interview | Already here |
| Ask instead of guessing | Root rules: look before asking, the 95% rule | Already here |
| Review before anything goes out | Draft by default; send only on "send" | Already here, stricter |

- **Nothing to queue.** Every step of his method already exists here, most of it with more evidence. The one difference is freshness: his prompt re-samples the 20 most recent messages, while the teaching-voice corpus analysis is dated 2026-07-18. That is a maintenance question for the voice files, not something this source proposes as new, so it was not queued.
- **His "pull, not push" rule** is the same stance as Joshua being the content authority.

Related: [Dan Martell's AI brain](ai-system-so-smart-dan-martell.md), [Austin Marchese on Matt Pocock's skills](matt-pocock-system-claude-skills-austin-marchese.md), [Greg Isenberg's five repos](greg-isenberg-5-github-repos-ai-slop.md) (the no-ai-slop editor, AQ-005), [AI workspace hub](../../references/ai-workspace/index.md).

## Limits

- Auto-captions; "WhisperFlow" is presumably Wispr Flow. The survey and MIT study figures are unsourced in the clip and were not checked.
- His full banned-words list is offered by Instagram DM and was not obtained.
