---
type: source
subject: Austin Marchese video on a six-step framework for Claude automations (spike, skill-driven routines, scheduling, enhancement, scale, choice)
created: 2026-10-14
updated: 2026-10-14
aliases: [6 EASY Steps to Automate 99% of Your Work With Claude, Austin Marchese automation framework, skill-driven automations, green light drift]
tags: [ai-workspace, automation, skills, claude-routines]
evidence: "../../raw/sources/clips/automate-99-percent-work-claude-austin-marchese/6 EASY Steps to Automate 99% of Your Work With Claude.md"
sha256: fbea7ddd311391bd7e8e8b2ba66b0fcb2326a9604169f3253f55520f14efbdb5
sources: [../../raw/sources/clips/automate-99-percent-work-claude-austin-marchese/PROVENANCE.md]
contradictions: []
---

# Austin Marchese's six automation steps: a skill holds the logic, and every run says what it actually checked

"6 EASY Steps to Automate 99% of Your Work With Claude" is a YouTube video by Austin Marchese ([YouTube](https://www.youtube.com/watch?v=ktY1b2-OKRA)). Sponsor: CodeRabbit. The publication date is unknown; the inbox file was last modified 2026-10-14. The description and the auto-caption transcript (to 22:18) were read in full on 2026-10-14. The prompts he shows on screen are not in the clip text.

Evidence: [archived clip, provenance and hashes](../../raw/sources/clips/automate-99-percent-work-claude-austin-marchese/PROVENANCE.md). SHA-256 `fbea7ddd311391bd7e8e8b2ba66b0fcb2326a9604169f3253f55520f14efbdb5`.

## What he says

- **Minimum stack (0:29).** Every automation is a trigger, logic and monitoring. His: Claude routines for the trigger, skills for the logic, the Claude desktop app for monitoring. He rejects heavier agent setups as hard to maintain.
- **Step 1, spike (1:42).** Build the ugliest end-to-end version first to prove nothing blocks it. His example, a daily brief from email and Slack that emails him, only became possible when Claude could send email; do not take Claude's word that something is possible, run it.
- **Step 2, transferable (4:24).** Pasting the prompt into a routine rediscovers the work each time; a reusable prompt is hard to maintain. Make a skill and have the routine call it, so editing the skill updates the routine. He calls this "skill-driven automations" and non-negotiable.
- **Step 3, when, how often, where (8:37).** Run when the output gives the most value, not when it seems obvious; at the lowest frequency possible; locally unless missing a run is costly, then in the cloud.
- **Step 4, enhance (11:41).** Calibrate by iterating locally and adding a gotchas section; add features (plugins and connectors); change output format (text, HTML, artifacts); improve system design with self-correcting loops that have an explicit maximum loop count, and self-breaking runs that check every connection first and stop with a fix message.
- **Step 5, scale (16:49).** Shared utility skills instead of repeating logic (one Slack-message skill used by many automations); one place for all notifications; explicit run reports ("analyzed 41 of 41 emails, 200 Slack messages, 10 calendar events") so a wrong count shows a broken run. He names the failure mode "green light drift": the AI reports success it did not achieve.
- **Step 6, what to automate (20:30).** Only constraint-driven automations (remove a bottleneck) or enhancement automations (raise the value delivered); prune ones that stop helping. His examples: a weekly HTML digest of important tweets, and a weekly sync that ingests his data sources into a Claude project.

## Mentions in source

> "we can create a skill that is directly referenced in the routine." (5:22)

> "the lowest frequency possible. Less is more." (9:28)

> "make sure there is a maximum amount of loops explicitly stated so there's a way for it to break." (14:31)

> "I call it green light drift." (19:27)

## How it compares with ai-os (interpretation)

Checked on disk 2026-10-14.

| His idea | Here | Verdict |
|---|---|---|
| Skill holds the logic; the trigger calls the skill | All recurring work here is a skill (`morning-brief`, `consultation-inquiry-drafts`, `consultation-followup-drafts`). No Claude scheduled tasks exist (the scheduled-tasks list was empty on 2026-10-14); Windows Task Scheduler runs only the laptop backup | Logic already here; triggers mostly manual |
| Constraint versus enhancement filter | "Find the Constraint" in the [Three Ms framework](../../references/3ms-framework.md), walked by `level-up` | Already here |
| Self-breaking preflight and explicit run counts | None of the three draft skills checks its connections before starting or reports how many items it read | Gap: queued as AQ-011 |
| One notification home | Drafts and alerts land in Gmail drafts, the [send ledger](../send-ledger.md) and `wiki/hot.md` | Already close; not queued |
| Weekly sync that copies data sources into the project | Declined earlier: live systems stay authoritative and are read live ([adoption ledger](../../references/ai-workspace/second-brain-adoptions.md)) | Declined, unchanged |
| Lowest frequency, local before cloud | Consistent with the vault's preference for on-demand skills | Already here |

- **Green light drift is the useful name.** It describes the risk the vault's verification rules already guard against for builds; the draft sweeps are where it can still hide, because "no new inquiries" and "Gmail auth failed silently" look the same without a count.
- **His loop cap matches existing practice.** The [harness engineering summary](harness-engineering-austin-marchese.md) and the `claudex-loop` skill already bound review loops.

Related: [Austin Marchese's Claude hacks](7-claude-hacks-austin-marchese.md), [harness engineering](harness-engineering-austin-marchese.md), [Karpathy's method](stop-prompting-claude-karpathy-method-austin-marchese.md), [Matt Pocock's skill process](matt-pocock-system-claude-skills-austin-marchese.md), [managing agents](manage-ai-agents-five-steps-austin-marchese.md), [automation backlog](../../references/automation-backlog.md).

## Limits

- Auto-captions: "Claw", "Clawed" and "Clade" are Claude; "whack-a-ole" is whack-a-mole. "Claude routines" and "Claude can send emails since August 18th" are his product claims and were not checked against official documentation.
- His career and revenue figures are self-reported.
- The on-screen prompts are not in the clip.

## Queue record

- Done 2026-10-14: AQ-011 Add a connection preflight and a "checked N of N" line to the draft sweeps. `gws` preflight and closing `Checked:` line added to `morning-brief`, `consultation-inquiry-drafts` and `consultation-followup-drafts` in every catalog, `.gemini` and home copy. Check: preflight reads exit 0 with auth and exit 2 with an empty config dir; read-only sweeps showed morning-brief reads 40 of about 201 per query. Stale `~/.agents/skills/morning-brief` left for Joshua.
