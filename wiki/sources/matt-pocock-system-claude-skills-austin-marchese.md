---
type: source
subject: Austin Marchese video distilling Matt Pocock's five-step process for writing Claude skills
created: 2026-10-14
updated: 2026-10-14
aliases: [Matt Pocock's EXACT System To 10x Your Claude Skills, Matt Pocock skill process, send it back test, skill no-ops, leading words]
tags: [ai-workspace, skills, matt-pocock]
evidence: "../../raw/sources/clips/matt-pocock-system-claude-skills-austin-marchese/Matt Pocock's EXACT System To 10x Your Claude Skills.md"
sha256: 0749f94e925d2fb7c36bfffc5815206875b2a85b5c00b3fe8ebdf5f1fe4177c1
sources: [../../raw/sources/clips/matt-pocock-system-claude-skills-austin-marchese/PROVENANCE.md]
contradictions: []
---

# Matt Pocock's skill process, via Austin Marchese: write a skill for what you keep sending back, keep it short, cut what does nothing

"Matt Pocock's EXACT System To 10x Your Claude Skills" is a YouTube video by Austin Marchese ([YouTube](https://www.youtube.com/watch?v=QsU0f-547rQ)) about Matt Pocock's skills ([mattpocock/skills](https://github.com/mattpocock/skills)). Sponsor: AIQORA (captioned "AI Core"). The publication date is unknown; the inbox file was last modified 2026-10-02. The description and the auto-caption transcript (to 15:14) were read in full on 2026-10-14. Pocock's words reach this page secondhand, through Austin's clips and paraphrase; the on-screen changelog and prompts are not in the clip text.

Evidence: [archived clip, provenance and hashes](../../raw/sources/clips/matt-pocock-system-claude-skills-austin-marchese/PROVENANCE.md). SHA-256 `0749f94e925d2fb7c36bfffc5815206875b2a85b5c00b3fe8ebdf5f1fe4177c1`.

## What it says

- **Step 1, notice what you keep sending back (0:42).** Pocock's definition: a skill is a correction you got tired of making. If the model already gets a task right, a skill for it is bloat that costs tokens. Models rush to produce an output ("premature completion"), so skills should focus on one step. Austin suggests scanning 30 days of conversation history for send-backs.
- **Step 2, leading words (3:03).** Use a term the model already knows deeply ("refactor", "relentlessly", "decision tree", "steelman", "premortem") instead of defining your own. Before writing a skill, ask whether an established term exists.
- **Step 3, smaller and harder to use (7:06).** Pocock's `grill-me` skill is seven lines and 22 words. He turns off model invocation on most skills: descriptions loaded on every message cost tokens forever, and a user-invoked skill removes a class of "why did that fire" errors.
- **Step 4, iterate with the send-it-back test (9:57).** He judges by vibes, not evals: use the skill on real work; if you stop sending results back, it works. Each line of his changelog fixed something observed (give a recommended answer; one question at a time; do not act until confirmed; separate facts from decisions). Add nothing you have not watched fail.
- **Step 5, cut the no-ops (12:15).** Lines like "be thorough" change nothing; remove a suspected line and see if output changes, or have Claude flag no-op language. Delete whole sentences. Say what you want rather than what you do not, since naming the banned thing puts it in context. Do not create a skill whose behavior existing skills can compose.
- **Ownership (14:24).** Do not blindly copy others' skills; write your own and own the process.

## Mentions in source

> "A skill is a correction you got tired of making." (0:51)

> "A made-up word recruits no priors." (3:40)

> "Don't add anything you haven't personally watched fail." (11:45)

> "If you can compose the behavior from existing skills, then don't create a new skill." (13:43)

## How it compares with ai-os (interpretation)

Checked on disk 2026-10-14.

| Idea | Here | Verdict |
|---|---|---|
| Pocock's skills themselves | `grill-me`, `grilling` and his engineering set are cataloged ([skill catalog](../../skills/INDEX.md)); the [Matt Pocock skills field guide](../../references/matt-pocock-skills-field-guide.html) tracks 39 of them | Already here |
| User-invoked only, to save context | The vault `.claude/settings.json` sets 69 vendor skills `user-invocable-only` and 183 unused skills `name-only` (2026-10-12, per the skill-listing-budget memory) | Already here |
| Scan history for send-backs | `level-up` reads 30 days of sessions for requests repeated three or more times, not for corrections; `skill-doctor` grades sessions; [copy corrections](../COPY-CORRECTIONS.md) logs copy fixes by hand | Partial: queued as AQ-012 |
| Cut no-ops; say what you want | No audit of the active vault skills for no-op lines has been recorded | Gap: queued as AQ-013 |
| Fix only what you watched fail | Matches "when a skill run exposes a gap, improve the skill" in the root rules | Already here |
| Compose before creating | Matches "search before creating" and the catalog check in the [AI workspace hub](../../references/ai-workspace/index.md) | Already here |
| Do not copy skills blindly | Consistent with AQ-002 (scan third-party skills before activation) | Already queued |

- **Tension with safety rules, not a contradiction.** "Say what you want, not what you don't" is advice about output quality. The vault's "never send", "never delete" and "never spend Lovable credits" lines are guardrails, and AQ-013 keeps them as written.

Related: [Austin Marchese's automation steps](automate-99-percent-work-claude-austin-marchese.md), [Austin Marchese's Claude hacks](7-claude-hacks-austin-marchese.md), [Karpathy's method](stop-prompting-claude-karpathy-method-austin-marchese.md), [Dan Martell's voice method](make-ai-sound-like-you-dan-martell.md), [declared runtime differences](../../skills/PARITY.md).

## Limits

- Secondhand: Pocock's positions come through Austin's selection and paraphrase. Only the short quoted clips are Pocock's own words, and they are auto-captions ("Mattacott" is Matt Pocock; "asset rush" is probably a mis-hearing).
- The 22 million users and 1.1 million installs figures are Austin's claims and were not checked.
- The "creator of Claude Code told people to delete all their skills" claim is referenced, not shown.


## Related source

Matt Pocock's own [v1.2.0 release video](matt-pocock-skills-v1-2.md) covers wait-what, rounds in grill-me, writing-for-agents, wizard and to-questionnaire.

## Queue record

Partial 2026-10-26: AQ-013. One clearly redundant 50-byte sentence removed; guardrails retained. Remaining: complete five-skill audit and real-run behavior checks. [Implementation record](../../research/2026-10-26-source-implementation/REPORT.md).

Partial 2026-10-26: AQ-012. Three source-grounded teaching/interview corrections implemented and installed copies synced. Remaining: refreshed 30-day correction scan and remaining groups; no blanket adoption of every old suggestion. [Implementation record](../../research/2026-10-26-source-implementation/REPORT.md).
