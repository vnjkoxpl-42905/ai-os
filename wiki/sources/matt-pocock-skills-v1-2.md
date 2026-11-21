---
type: source
subject: Matt Pocock's skills v1.2.0 release video
created: 2026-11-20
updated: 2026-11-20
aliases: [New Skills v1.2, Matt Pocock skills v1.2.0, wait-what release video]
tags: [ai-workspace, skills]
sources:
  - ../../raw/sources/clips/matt-pocock-skills-v1-2/New Skills v1.2 wait-what writing-for-agents grill-me.md
evidence: ../../raw/sources/clips/matt-pocock-skills-v1-2/New Skills v1.2 wait-what writing-for-agents grill-me.md
sha256: 4c8d9657e8638756f758512bdeebdf55b5c1c38ea354da6f33b39608976468b8
contradictions: []
---

# Matt Pocock's skills v1.2.0: what changed and what we already have

Matt Pocock's [release video](https://www.youtube.com/watch?v=gaDdrDdczO4) was published 2026-08-05 (11:37), the same day as the `mattpocock/skills` tag `v1.2.0` (commit `e903586b`, checked with `gh`). Full auto-caption transcript; the docs site and terminal he shows were not seen. [Provenance](../../raw/sources/clips/matt-pocock-skills-v1-2/PROVENANCE.md).

## What the source says

- **Docs site** at aihero.dev/skills with skill groupings, a main flow (grill-with-docs, to-spec, to-tickets, implement, code-review), common questions and an AI coding dictionary.
- **Claude Code plugin marketplace:** the skills install as a read-only bundle that auto-updates.
- **Codex:** every skill now ships an `agents/openai.yaml` sidecar so `allow_implicit_invocation: false` hides user-invoked skills from Codex's context, as `disable-model-invocation` already did for Claude Code. Confirmed in the v1.2.0 tree.
- **wait-what (new):** a one-line re-pitch when the agent's reply does not land. It asks for ASD-STE100 Simplified Technical English and grounding in the project's own vocabulary. His point: the real fix for verbose output is using your terms, not just simpler words.
- **grill-me:** questions now come in rounds. Decisions form a graph; each round asks every question whose prerequisites are settled, each with a recommended answer, so easy questions get batch answers.
- **writing-for-agents:** the renamed skill-writing skill, for anything an agent reads (AGENTS.md, CLAUDE.md, skills), including moving front-loaded instructions out into skills. Model-invocable.
- **wizard (new):** generates a deterministic interactive bash script that walks a human through steps only they can do, such as provisioning and pasting keys, with no agent seeing the secrets.
- **to-questionnaire (new):** turns a grilling session's open decisions into a document another person can answer, then the answers go back to the agent.

## Already here

Every skill in the video is installed in both runtimes (`.claude/skills/` and `.agents/skills/`) and the catalog: `wait-what`, `grill-me`, `grilling`, `grill-with-docs`, `writing-for-agents`, `wizard`, `to-questionnaire`, plus `asd-ste100`. A scheduled "AI OS - Matt Pocock Skills Sync" task refreshes them every 10 days and skips locally edited copies ([log](../log.md)). Checked 2026-11-20: none of the five `SKILL.md` files matches v1.2.0 byte-for-byte, because the vault copies track a later upstream and carry local edits. Our `grill-me` already works in rounds and adds capture to a brainstorm file; our `wait-what` points to `GLOSSARY.md` rather than `context.md`. Runtime differences are recorded in [PARITY](../../skills/PARITY.md).

Nothing queued: the marketplace install would duplicate the existing sync, and every skill is already active.

## Useful for Joshua now

- When a reply reads as jargon, type `/wait-what`. It matches his standing complaint about AI phrasing.
- `to-questionnaire` fits decisions that need someone else, such as a student's parent or a collaborator, after a grill-me session.
- `wizard` fits setup work that needs his own logins or keys, so keys go into `.env` without passing through chat.

## Mentions in source

> "The real cure for verbosity is not to tell it to use simple language" (3:36)
> "these questions are really like a graph" (4:53)
> "generates an interactive bash wizard that walks the human through steps only they can perform" (7:44)

## Related

- [Matt Pocock's system for Claude skills (Austin Marchese)](matt-pocock-system-claude-skills-austin-marchese.md)
- [Matt Pocock skills field guide](../../references/matt-pocock-skills-field-guide.html)
- [AI workspace hub](../../references/ai-workspace/index.md) · [skill catalog](../../skills/INDEX.md)
