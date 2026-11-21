---
type: source
subject: Austin Marchese video on "Karpathy's method" for Claude, in three layers, spec, verifier and environment
created: 2026-10-14
updated: 2026-10-14
aliases: ["Stop Prompting Claude. Use Karpathy's Method Instead.", Austin Marchese Karpathy method video, spec verifier environment]
tags: [ai-workspace, second-brain, hooks, verification, claude-md]
evidence: "../../raw/sources/clips/stop-prompting-claude-karpathy-method/Stop Prompting Claude. Use Karpathy_s Method Instead..md"
sha256: 3778b15435110adb08f49f33d91471ab518bbafa9abc4c1ddab5609de7ffe61a
sources: [../../raw/sources/clips/stop-prompting-claude-karpathy-method/PROVENANCE.md]
contradictions: []
---

# Austin Marchese on Karpathy's method: ai-os has the spec, verifier and environment; the gap is rules enforced by hooks

"Stop Prompting Claude. Use Karpathy's Method Instead." is a YouTube video by Austin Marchese ([YouTube](https://www.youtube.com/watch?v=7zZy1QTvokM)), published 2026-06-09, clipped 2026-07-19 with the Obsidian Web Clipper, and archived 2026-09-08. The full description and auto-caption transcript (captions run to 13:08) were read on 2026-10-14. The provenance file marks the clip as processed, but no source summary for it existed in `wiki/sources/` on 2026-10-14; this page fills that gap. The Karpathy quotes in it are clips played inside the video, not his original recordings.

Evidence: [archived clip, provenance and hashes](../../raw/sources/clips/stop-prompting-claude-karpathy-method/PROVENANCE.md). SHA-256 `3778b15435110adb08f49f33d91471ab518bbafa9abc4c1ddab5609de7ffe61a`. The `SHA256SUMS` file there also hashes `PROVENANCE.md`.

## What he says

- **Layer 1, the spec (0:28 to 3:26).** He says Karpathy, at an event the captions call "AISN 2026", showed that models answer "walk" when asked whether to drive or walk to a car wash 50 m away; Austin says Claude, Gemini, Grok and ChatGPT all failed it for him. Models are strong on what can be measured and weak on unstated context. A spec delivers your understanding in a form the agent can use. In a played clip, Karpathy says he does not like plan mode as much as working with the agent on a very detailed spec. Three steps: uncover the real goal (ask Claude to interview you); work in small, agile specs with checkpoints instead of one waterfall task; be precise and make the AI ask you to verify key decisions.
- **Layer 2, the verifier (3:34 to 8:15).** He plays Karpathy's "animals versus ghosts" answer: models are statistical circuits, so yelling or pleading does not help. Austin's analogy is a robot librarian that cannot tell when a book is missing and may answer confidently anyway. The lever is verification. Set evaluation criteria up front ("three sections, each ends with a recommendation", not "make it look good"). Use a second model as critic; he suggests the Codex plugin for Claude Code. Pull external signal: check the deployment system itself, or compare against past reports. He attributes to Boris Cherny, the creator of Claude Code, a claim that a feedback loop gives two to three times better results.
- **Layer 3, the environment (8:46 to 12:28).** The workshop where spec and verifier live. Four steps. First, a good `CLAUDE.md`, injected into every prompt; for example, a line requiring a verification plan before any multi-step build. His has sections for how the repo works, the custom skills and their routing, the knowledge architecture, and key working rules. Second, an LLM knowledge base, because "your data is your moat". Third, a skill for anything you do repeatedly; skills improve with use ("the best way to find a leak in a hose is to run water through it"). Fourth, rules for what the AI may touch: a `CLAUDE.md` line is a request the model can ignore, so critical rules need a PreToolUse hook on Write and Edit that blocks the change at the tool level. Sort actions into always do, ask first, and never do.
- **The one thing to focus on (12:47).** A played clip: Karpathy says you can outsource your thinking but not your understanding.

## Mentions in source

> "that might get you 80% of the way there, but it's essentially a request, not a rule" (11:40)

> "it's enforced at the tool level, not the prompt level" (11:51)

> "The first is always do. This is things that AI should run on autopilot. The second is ask first." (12:14)

> "before building anything multi-step, include a verification plan" (9:31)

## How it compares with ai-os (interpretation)

Checked on disk 2026-10-14 against the root `CLAUDE.md`, `.claude/settings.json` and `system/scripts/wiki-maintenance.py`. Decisions are recorded in the [second-brain adoption ledger](../../references/ai-workspace/second-brain-adoptions.md).

| His idea | Here | Verdict |
|---|---|---|
| Rules that matter are enforced by hooks, not `CLAUDE.md` wording | No hook blocks edits to `raw/sources/`. The one PreToolUse hook runs the Karpathy-teach "run it before you say it works" check; its code snapshot skips `raw/`, and it is not a guard for that folder. `wiki-maintenance.py --evidence` re-hashes archived evidence against every `SHA256SUMS`, which catches a change after the fact but does not prevent it | Pending Joshua's decision on a PreToolUse hook protecting `raw/sources/` |
| Always, ask, never buckets | Guardrails in `CLAUDE.md` and the global safety rules (draft by default, send only on "send", never delete without confirmation) | Already |
| An LLM knowledge base | The [vault schema](../../system/schema/llm-wiki.md) and wiki | Already |
| Skills improve by running them | `CLAUDE.md`: "When a skill run exposes a gap, improve the skill before moving on." | Already |
| Spec by interview; precise goals; verify key decisions | `grill-me` and `grilling` skills; the 95% rule in `CLAUDE.md` ("Ask until you are") | Not yet evaluated |
| Small agile specs with checkpoints | No standing rule | Not yet evaluated |
| Evaluation criteria up front | The `verification-before-completion` skill | Not yet evaluated |
| A second model as critic | `codex-review` and `claudex-loop` skills; [Claude plus Codex](../../references/claude-plus-codex.md) | Not yet evaluated |
| External signal: check the real system | `CLAUDE.md` makes live systems the authority for operational state | Not yet evaluated |
| A `CLAUDE.md` line requiring a verification plan before multi-step builds | No such line in the root `CLAUDE.md`; verification lives in skills and memories | Not yet evaluated |
| `CLAUDE.md` sections: repo, skill routing, knowledge architecture, rules | The root `CLAUDE.md` has identity, a routing map, retrieval order, a skills table and guardrails | Not yet evaluated |

- **ai-os already states his principle in its own words.** The root `CLAUDE.md` says "Safety is the tool layer, not prompts", and the global instructions say "A prompt is not a permission layer." The gap is that the immutability of `raw/sources/` still rests on wording plus an after-the-fact hash check. A blocking hook would make it a rule in his sense. That choice is Joshua's, so it is recorded as pending.
- **His spec and verifier layers map onto existing skills.** Interviews (`grill-me`), the 95% rule, Codex review and verification-before-completion cover most of it. Whether to add his explicit `CLAUDE.md` line about verification plans has not been decided.
- **His environment layer is what ai-os is.** A router `CLAUDE.md`, a knowledge base, skills that improve with use, and guardrails.

Related: [7 Claude hacks video](7-claude-hacks-austin-marchese.md), [harness engineering video](harness-engineering-austin-marchese.md), [Karpathy sub-wiki](../karpathy/index.md), [six automation steps](automate-99-percent-work-claude-austin-marchese.md), [Matt Pocock's skill process](matt-pocock-system-claude-skills-austin-marchese.md), [AI workspace hub](../../references/ai-workspace/index.md).

## Limits

- Auto-captions. Likely mis-hearings: "Boris Cherney" (Boris Cherny), "next eight era" (probably "next AI era"). "AISN 2026" is a caption spelling of an event that was not identified.
- The Karpathy remarks are short clips chosen and framed by Austin; their full context was not checked. The car-wash test results are his.
- Unverified: the two-to-three-times quality figure attributed to Boris Cherny, and the behavior of the Codex plugin he links (github.com/openai/codex-plugin-cc).
- His on-screen prompts and his own `CLAUDE.md` were not visible in the clip text.


## Queue record

Done 2026-10-26: AQ-003. Identical verification-plan guardrail implemented in both runtime manuals and compared. Local implementation checked; next native-session behavior remains a future observation. [Implementation record](../../research/2026-10-26-source-implementation/REPORT.md).
