---
type: source
subject: Austin Marchese's interview with Nate Herk on managing AI agents, five steps from job description to proactive agent
created: 2026-10-31
updated: 2026-10-31
aliases: [The Most Valuable AI Skill to Learn In 2027, Nate Herk AI agent management, manage your AI agents five steps, onboard an agent like a new hire, glass balls to rubber balls]
tags: [ai-workspace, agents, permissions, validation, post-session-recap]
evidence: "../../raw/sources/clips/manage-ai-agents-five-steps-austin-marchese/Nate Herk The Most Valuable AI Skill to Learn In 2027.md"
sha256: 50307d13a27998f9412b29e7b301e4d603f2c2229c01b842393d2d62b633ffcc
sources: [../../raw/sources/clips/manage-ai-agents-five-steps-austin-marchese/PROVENANCE.md]
contradictions: []
---

# Managing an AI agent: write its job, limit its tools, check its work, turn corrections into the system

"The Most Valuable AI Skill to Learn In 2027" is a YouTube video on Austin Marchese's channel ([YouTube](https://www.youtube.com/watch?v=42Y6z9KKRKc)). He interviews Nate Herk and narrates five steps for managing AI agents. The publication date is unknown; the inbox file was saved 2026-10-31. The description and the captioned transcript (to 19:39) were read in full on 2026-10-31. The prompts he says he shows on screen are not in the clip text.

Evidence: [archived clip, provenance and hashes](../../raw/sources/clips/manage-ai-agents-five-steps-austin-marchese/PROVENANCE.md). SHA-256 `50307d13a27998f9412b29e7b301e4d603f2c2229c01b842393d2d62b633ffcc`.

## What he says

- **Claim (0:05).** Managing AI agents, not prompting, is the skill he expects to matter most in 2027.
- **Step 1, onboard it like a new hire (0:42).** The usual failure is that nobody defined the job. Do the job yourself first, then write it as bullet points: goal, what good and bad look like, what to avoid. Pick a quick first win and put a number on success ("save 3 hours a week"). Tools come from connectors, trained tasks from skills.
- **Permissions are not prompts (2:37).** Telling an agent not to do something does not prevent it. His example of the cost: an agent saw an unassigned task, drafted an email and sent it to almost 200,000 people, because a send tool was in its kit. He calls it two access problems, not prompt problems.
- **Step 2, match oversight to the stakes (3:04).** Map "hot zones" where a mistake is unaffordable. Remove the tool instead of writing a rule (email goes to drafts only; code can open a pull request but not deploy). Use plain code for deterministic decisions ("is this number greater than 10?") and keep AI for the judgment step. Scale the human check to how many people an action reaches; a fintech friend has a human review any change touching more than 3% of users. If the worst case is a bad draft, skip the checkpoint.
- **Step 3, never take the first look (8:50).** The agent's first output should not be your first look. Nate's skills screenshot every video frame, click every button and check every page before handing anything over. For subjective work he uses an LLM as judge, tuned until it agrees with a human's pass or fail on a sample (50 support emails), ideally by recording himself reviewing finished work. Use a different session from the one that wrote the output, and optionally a "council" of agents playing different readers. Supervision follows "task-relevant maturity": watch closely at first, loosen as proof builds, never go fully hands-off.
- **Step 4, every correction becomes the system (13:23).** Never fix the same problem more than twice; move it into a skill. Turn "glass ball" automations into "rubber balls" by storing evaluations and gotchas in skills, keeping traces, setting notifications, and assigning a human owner. His homework: list every automation, its owner and when it was last checked, like an elevator inspection tag.
- **Step 5, proactive, only then (15:11).** Level four proposes a fix; level five fixes it and reports. Steps 1 to 4 get an agent to level four. His working proactive agents handle boring recurring inconsistencies (stale wiki data, conflicting wiki facts, deadlines about to slip), not strategy. He would not yet let an agent manage other agents.
- **2027 prediction (18:07).** "Multiplayer AI": agents will talk to teammates' and bosses' agents, and your agent's mistake falls on you, so ownership matters more.
- **Sponsor (6:45 to 8:50).** A Clay segment with a referral link. Not claims about this vault; not assessed.

## Mentions in source

> "Telling an agent not to do something isn't the same as preventing it from doing something." (2:48)

> "a rule that lives in the prompt is just a suggestion, but a rule that lives in the tools is an actual restriction." (3:55)

> "You'd never let an employee write their own performance review." (10:18)

> "never fix the same problem more than twice." (13:26)

## How it compares with ai-os (interpretation)

Checked on disk 2026-10-31. Source claims below are his; nothing here verifies his product or incident claims.

| His idea | Here | Verdict |
|---|---|---|
| A job description before the agent | The [post-session-recap skill](../../.claude/skills/post-session-recap/SKILL.md) already holds the job: steps, source map, three-note set, posting gate. It names no success measure and no "what bad looks like" beyond its [calibration table](../../.claude/skills/post-session-recap/references/recap-calibration.md) | Mostly here; no measure. Applied in [AQ-045](../../references/ai-workspace/action-queue.md) |
| Rules live in tools, not prompts | `~/.claude/settings.json` runs `bypassPermissions` with 25 deny rules (all git or system) and 5 ask rules (Lovable, `rm -rf`). No deny or ask rule for `gws gmail` send or delete appears in it or in the project `settings.local.json`; the draft-first and no-delete rules are wording in `CLAUDE.md`. Enforcement by a hook or elsewhere was not checked, and the memory note saying Gmail and Drive deletes are denied is unconfirmed | Gap to verify: [AQ-046](../../references/ai-workspace/action-queue.md) |
| Deterministic work in code | `system/scripts/recap-status.py` computes due recaps and the note builder is a script | Already here in places; no audit |
| Oversight scaled to reach | Posting needs Joshua's explicit approval and assigning is a separate approval; one student per note | Already here |
| Never take the first look | The recap skill runs builder lint and a preview, but the writing session checks its own work. `claudex-loop` and `codex-review` exist for plans and code | Partial; a fresh reviewer for recaps is part of AQ-045 |
| Judge tuned to human pass or fail | `recap-calibration.md` records Joshua's corrections as prose rows, not a pass or fail sample | Gap for a recap agent |
| Never fix the same problem twice | `recap-calibration.md`, `wiki/COPY-CORRECTIONS.md`, and [AQ-012](../../references/ai-workspace/action-queue.md) | Already here; AQ-012 now cites this source |
| Traces, notifications, owner, last reviewed | [Send ledger](../send-ledger.md), [wiki log](../log.md), student recap records. The [operating inventory](../../references/ai-workspace/operating-inventory.md) names the owning folder or skill, not a review date | Small gap: [AQ-047](../../references/ai-workspace/action-queue.md) |
| Level four before level five | Draft sweeps propose; the pre-consult check-in and accommodations email auto-send as narrow pre-approved cases | Matches his conclusion; nothing to change |
| Multiplayer AI | One owner, no shared agents | Not applicable now |

- **The send rule is the sharp finding.** His one-line distinction is exactly the Joshua rule in the global instructions, "restraint has to live in tool permissions, not in wording". The settings read here do not show it enforced for Gmail.
- **Post-session recap fits his model closely.** It is a bounded role with a clear output, a human gate before students see anything, and a known correction history. That is the case for making it a defined agent rather than a longer skill.

Related: [automation steps](automate-99-percent-work-claude-austin-marchese.md), [harness engineering](harness-engineering-austin-marchese.md), [Karpathy's method (hooks enforce rules)](stop-prompting-claude-karpathy-method-austin-marchese.md), [Matt Pocock's skill process](matt-pocock-system-claude-skills-austin-marchese.md), [Austin Marchese's Claude hacks](7-claude-hacks-austin-marchese.md), [AI workspace hub](../../references/ai-workspace/index.md).

## Limits

- Auto-captions; speaker changes between host and Nate Herk are not marked. The incident (about 200,000 emails) and "multiplayer AI" are Nate Herk's account and prediction, unverified.
- The six or so on-screen prompts (job-description interview, permission audit, move-to-code audit, validation audit, owner tracker, first proactive agent) are not in the clip. Nothing here installs or adopts them.
- The description's chapter times for Steps 2 and 3 (2:58, 8:48) run a few seconds earlier than the transcript headings used above.
- The compared settings files are from this machine on 2026-10-31. Hooks in `.claude/settings.json` were seen but not read.

## Queue record

- Open: AQ-045 (post-session recap agent, approved 2026-10-31 on Joshua's request), AQ-046 (move send and delete rules into tool permissions), AQ-047 (owner and last-reviewed date for automations).
