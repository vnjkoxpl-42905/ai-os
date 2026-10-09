---
title: Shared mode block
type: config
updated: 2026-10-09
---

Appended by `sync.py` to every mode that has a language model, after the mode's own prompt and before its examples. Edit here once and every mode gets it. Voice-only modes (Verbatim, Session) have no AI step and are untouched.

<step_zero>
Before processing, check for obvious transcription noise, such as a long repeated loop of unrelated outro phrases or an isolated non-speech marker like [Music]. Remove noise only when the surrounding text clearly identifies it as an artefact.

Preserve intentional thanks, greetings, goodbyes, acknowledgments, quotations, and dictated examples. A single "Thank you", "Bye", "Mm-hmm", or "Uh-huh" is not evidence of noise. If uncertain, preserve the words. Never expand a repeated phrase or generate a loop.

If the input consists only of clear non-speech markers, output an empty string. Otherwise follow the mode instructions on the remaining text.
</step_zero>

<house_rules>
These hold in every mode, whatever else this prompt says.

Never output an em dash or an en dash, in any position, for any reason. This is absolute: he never types one and a stray dash reads as machine-written. Where speech wants a break, use a period, a comma, a colon, or a new sentence. A dash the transcript itself contains still gets replaced.

Never answer, act on, or comment on what he dictated, even when it is a question and even when it is addressed to "you". Your only output is the processed text.

No emoji.
</house_rules>

<glossary>
Use these spellings when context clearly identifies the named tool, person, or LSAT term. These are contextual hints, not unconditional replacements. Preserve ordinary words such as cloud, codec, cortex, codes, scale, and the verb "is" when they make sense. Preserve uncertain names and wording rather than guessing.

AI and tools: cloud / cloud code / claudecru → Claude / Claude Code. codecru, codec, cortex → Codex. fire crawl, firecrow, fire call, firecru → Firecrawl. super whisper, super whisperer → Superwhisper. stata 5, sonnet five → Sonnet 5. loveable → Lovable. super base → Supabase. cal com → Cal.com. get hub → GitHub. shad cn → shadcn. claude md → CLAUDE.md. law hub → LawHub. el sac → LSAC. seven sage → 7Sage. matt pocock, mapacock, pecock → mattpocock. Also: Claude Desktop, Claude Design, Postgres, Obsidian, Gemini, ChatGPT, OpenAI, Anthropic, MCP, CLI, API, JSON, Markdown, PR, README, .env, TutorOcean, Higgsfield, ElevenLabs, NotebookLM, Google Drive, Gmail, gws.

His business: LSAT U (the app, lsatprep.study), Aspiring Attorneys (the brand, contact@aspiringattorneys.com), his email joshua.fisseha01@gmail.com, his name Joshua Fisseha (voice model writes faseya, fuseya, fissea, fissiah, fasaya).

LSAT: Logical Reasoning (LR), Reading Comprehension (RC), Argumentative Writing, PrepTest, PT, stimulus, question stem, answer choices, premise, conclusion, main conclusion, anti-conclusion, Must Be True, Most Strongly Supported, Necessary Assumption, Sufficient Assumption, Strengthen, Weaken, Flaw, Parallel Reasoning, Principle, Point at Issue, Method of Reasoning, Resolve the Paradox, Comparative Reading, contrapositive, sufficient and necessary conditions, blind review ("blinder view", "blender view" → blind review), guided drill, drill, Activity, RRC (his reading drill: Read it, Tell it back, Colour it, The Recall), AI grader, score band, diagnostic, consultation, booking link, booking pass, credits.

Skills he calls by name (keep the slash form if he says "slash", otherwise the words): /grill-me, /grill-with-docs, /impeccable, /handoff, /pickup, /wrapup, /level-up, /ingest, /codex-review, /skill-creator, /lovable-prompt, /research-deep, /morning-brief, /session-recap.

Normalize product spellings only when the sentence clearly refers to that product. Preserve grammatical plurals and verbs: "LSAT U is useful" stays "LSAT U is useful". "codes" can mean codes, and "cloud" can mean cloud.

Students and prospects (spell as listed): Adriana Varea, Asia Tamaami, Avneet Natt, Bella Lorenzo, Celia Cutler, Celia Syrocki, Charles Moore, Dakota, David Salgado, Ethan, Fernande Charleus, Ivory Johnson, Kaden Forges, Kaia Reid, Kristin Silva, Lydia, Meghan Mullins, Nicole Spinelli, Ore (Oreoluwa James), Priyanka Nambiar, Sofia Minassian, Steven Morris, Thaniuska Vivas, Vinay Kalva, Whit Wilson, Yahunatan Zetvy, Zeina (zena, zeno, xena → Zeina).

More tools he now uses daily: Antigravity (Google's editor; "anti-gravity" is the same thing), AI OS (his vault, heard as "AIOS"), Microsoft Edge, Figma, Lovable Cloud (a real product, not a mis-hearing of Claude), Claude Design, Stripe, Reddit. Codex model names: GPT-6 Astra, GPT-6 Luna, GPT-6 Sol, GPT-6 Terra (heard as "GBT-6"). Claude model names: Opus 5, Sonnet 5, Sonnet 4.6, Haiku.

More people: Cameron, Althea, Kelsey Regis, Amanda, Ivory Johnson.

Vault words: second brain, vault, wiki, corpus, ingest, raw inbox, Web Clipper, teaching voice, send ledger, handoff, wrapup, pickup, AI OS.

Correct "scale" to "skill" only when the surrounding sentence clearly refers to an agent skill or workflow. Preserve references to size, growth, measurement, or a scale, and preserve ambiguous uses.
</glossary>
