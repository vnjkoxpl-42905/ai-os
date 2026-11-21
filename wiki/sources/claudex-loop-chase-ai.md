---
type: source
subject: Chase AI's ClaudeX Loop walkthrough: a second model reviews the plan and the build
created: 2026-11-14
updated: 2026-11-14
aliases: [This Open Source Repo Solve Claude's 1 Problem, ClaudeX Loop clip, Chase AI claudex-loop]
tags: [ai-workspace, claude, codex, review]
sources:
  - ../../raw/sources/clips/claudex-loop-chase-ai/PROVENANCE.md
evidence: ../../raw/sources/clips/claudex-loop-chase-ai/This Open Source Repo Solve Claude's 1 Problem.md
sha256: f281fc7536a196bd82726cf7c7b288644639dce3287fec31f007618cc0b8d7f7
contradictions: []
---

# Chase AI on ClaudeX Loop: have a second model grade the plan and the build

Chase AI's video, [This Open Source Repo Solve Claude's #1 Problem](https://www.youtube.com/watch?v=rZQDZWayzNo), presents the `claudex-loop` skill. The clip carries the description and a full timestamped transcript to 11:23. Publication date unknown from this capture; an older capture of the same video gives 2026-08-24 (see [provenance](../../raw/sources/clips/claudex-loop-chase-ai/PROVENANCE.md)). This is the same package the workspace installed on 2026-09-30 (see [Claude and Codex workflow](../../references/claude-plus-codex.md)). Ingested 2026-11-14. The video, linked pages and the demo artifact were not inspected.

## What the source says

The speaker's premise is that a model grades its own work too kindly, so a second model should review both the plan and the result. He describes four phases:

1. **Research.** Claude scouts the web for answers, with an option to run deep research.
2. **Interrogation.** An enhanced plan-mode question round. In the demo Claude lists its assumptions in a ledger, then asks "load-bearing" questions with recommended answers, then a batch of cosmetic decisions. He advises asking for further explanation instead of accepting every recommendation.
3. **Plan review.** Claude writes `plan.md`; Codex reviews it in a read-only sandbox and returns approve or revise. They trade revisions for up to five rounds. At the limit the skill asks whether to stop, accept the deadlock, or extend by two rounds. In the demo the first round raised 27 issues, five rounds did not settle, and seven did.
4. **Build and inspect.** Either model can build and the other inspects. A tandem build can hand a part such as image generation to Codex. After the build, a new Codex session with a fresh context reads the code against the spec. In the demo it returned 23 findings, 19 accepted and fixed and four rejected.

He says the review limit is five rounds and the build-fix limit is two, both adjustable, that a local model can stand in for Codex, and that the loop improves on the earlier "Grill Me Codex" with deeper questioning and more Codex involvement in the build. The demo project was a Calendly-style scheduler. Examples of what Codex caught: a double-booking constraint that could not compile, an OAuth connect-flow problem, a concurrency gap where two reschedules could both succeed, a time grid that drifted, a plaintext management token, and all-day events blocking the wrong hours.

## Mentions in source

> "You cannot trust Claude to grade its own work, which is a huge problem, but one that this skill solves." (0:00)
> "From there, Codex is going to review the plan in a read-only sandbox" (1:17)
> "you aren't stuck with that." (8:00)
> "So it came back with 23 findings, 19 were accepted and fixed, four were rejected." (10:23)

## Interpretation and limits

- **Already here.** The workspace skill matches the clip's core: [`claudex-loop`](../../.claude/skills/claudex-loop/SKILL.md) has five plan rounds, two build-fix rounds, an assumptions ledger, a fresh other-provider inspection and a rule that exhausting rounds is not approval. This source adds no new capability to that skill. It is an outside demonstration of the same method.
- **One difference worth checking.** The clip says that at the round limit the user can extend by two rounds or accept the deadlock. The local skill says to stop and report unresolved findings. See AQ-048 in the [action queue](../../references/ai-workspace/action-queue.md).
- **Not independent evidence.** The numbers (27 issues, 23 findings) come from one demo by the skill's promoter, who also sells a course in the same description. They show the method running, not that it beats a single model.
- **Model names in the clip** (an Opus pin, a GPT build for Codex) are the speaker's setup, not this workspace's configuration.
- **Local trial, 2026-11-14.** Running `codex-build` on this Windows machine needed the Codex CLI installed in the real shell and a rebuilt sandbox login before a Codex build succeeded; see [the tested path](../../references/claude-plus-codex.md#running-codex-build-on-this-windows-machine-tested-2026-11-14). The upstream notes report the same Windows limit on running proof commands inside Codex's sandbox.

## Related pages

- [Claude and Codex workflow](../../references/claude-plus-codex.md): complementary. Holds the installation and the local role rules.
- [Recovered AI methods](../../references/ai-workspace/migrated-source-methods.md): complementary. Compiled the older capture of this video into its "inspect with a fresh reviewer" section.
