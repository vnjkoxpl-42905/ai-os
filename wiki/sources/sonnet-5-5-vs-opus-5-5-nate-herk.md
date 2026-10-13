---
type: source
subject: Nate Herk video, Sonnet 5.5 vs Opus 5.5 on seven workflows
created: 2026-10-12
updated: 2026-10-12
aliases: [I Tested Sonnet 5.5 vs Opus 5.5, Sonnet vs Opus clip]
tags: [ai-workspace, claude, models, cost]
sources: [../../raw/sources/clips/sonnet-5-5-vs-opus-5-5/PROVENANCE.md]
---

# Sonnet for a clear spec, Opus for a vague goal: Nate Herk's seven-task comparison

"I Tested Sonnet 5.5 vs Opus 5.5. What You Need to Know" is a YouTube video by Nate Herk ([YouTube](https://www.youtube.com/watch?v=7eo-11K2e3c), publication date unknown, clipped 2026-10-08). The full description and transcript (about 25:45) were read on 2026-10-12.

Evidence: [archived clip, provenance and hashes](../../raw/sources/clips/sonnet-5-5-vs-opus-5-5/PROVENANCE.md). SHA-256 `4568056ffab12dda803c3ffe3e079162a2a6c001a395b97911ede43f6e431b6f`.

Everything below is his account. Costs are his API-billing figures, not subscription usage, and were not checked here. The judging is his own taste and he says so.

## What he claims

- **Price (0:41).** Sonnet 5.5 is $2 / $10 per million input / output tokens; Opus 5.5 is $4 / $20. He says Sonnet 5.5 is about 30% faster and cheaper than Sonnet 5.
- **His rule (1:13 to 2:07).** Paraphrasing Anthropic's own guide: Sonnet fits a task with a clear spec and a way to check the result; Opus fits judgment-heavy, long-horizon or creative work. His reading: objective definition of done, try Sonnet first; subjective, thought-partner work, use Opus. Then record per skill which model does better.
- **Seven head-to-heads, both on high effort, same prompt:**

| Task | Better single output | His winner | Why |
|---|---|---|---|
| Scroll landing page | Opus (Sonnet's hero invented a fake can) | Sonnet | Opus took 52 vs 28 min and about 2x cost; a Sonnet re-prompt would close the gap |
| Motion show reel | Opus | Opus | Better taste in motion, copy and sound; Sonnet $14.37 vs Opus about $20.55 |
| Vague 90-day plan | Opus | Opus | Vague prompt rewards Opus; about $5 vs $9 |
| Spreadsheet + investor deck | Tie | Opus | Opus was cheaper and faster here. Both used formulas in cells |
| HTML explainer (with a skill) | Opus | Sonnet | Half the cost; one more Sonnet prompt would beat it |
| Live AI news dashboard from X | Opus | Sonnet | Sonnet was much cheaper; nothing it could not build with a clearer goal |
| YouTube resource guide (with a skill) | Tie | Sonnet | A skill defines "good," so the cheaper model follows it |

- **Totals (24:58).** Four to three for Sonnet. Opus ran about 46 minutes longer and cost about $16 more across all seven, less than double.

## What is useful here (interpretation)

- **The rule matches how we already route work.** Writing the spec and a check first is what lets a cheaper model do the job. That fits the plan-then-build split in [Claude plus Codex](../../references/claude-plus-codex.md).
- **Skills narrow the gap.** In both tasks where a skill defined the output, he found the models close. Our catalog is large; the cheaper model may be enough for well-specified skill runs. Not tested here.
- **Single-sample and self-judged.** One run per model per task, his taste as the judge. Treat the winners as anecdotes.
- **No tools or repos to install.** The only tools named are his private "HTML explainer" skill, Glaido (a sponsor dictation app; Joshua uses [Superwhisper](../../superwhisper/)) and his [scroll-craft](fable-5-1-kills-ai-website-slop.md) skill, already installed.

## Status

Captured only. No model comparison was run on our own work.

Related: [Claude plus Codex](../../references/claude-plus-codex.md), [Nate Herk repos clip](100-github-repos-for-claude-nate-herk.md), [AI workspace hub](../../references/ai-workspace/index.md).
