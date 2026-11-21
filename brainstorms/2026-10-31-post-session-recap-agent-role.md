---
type: brainstorm
subject: Role draft for a post-session recap agent
created: 2026-10-31
updated: 2026-10-31
aliases: [recap agent job description, post-session recap agent role]
tags: [ai-workspace, post-session-recap, agents]
sources: [../wiki/sources/manage-ai-agents-five-steps-austin-marchese.md]
---

# Post-session recap agent: a draft job description for Joshua to correct

Status: proposal. No agent file exists. Built from [the five-step source](../wiki/sources/manage-ai-agents-five-steps-austin-marchese.md) and the current [post-session-recap skill](../.claude/skills/post-session-recap/SKILL.md). Queue item: AQ-045.

## The job in one line

Turn one finished tutoring session into three draft notes (session recap, drill primer, method reference) and a review report, then stop. Joshua decides what students see.

## Why an agent and not a longer skill

The skill is the procedure. The agent is the worker: it has a fixed tool list, so what it cannot do does not depend on it reading a rule. It also lets a second, separate session review the first one's work, which a single skill run cannot do.

## What good looks like

- Every note is grounded in the full transcript, with Joshua's emphasis map and timestamps shown before anything else.
- Every assignment and promise from the session is in the private table with its real certainty (assigned, promised, offered, proposed).
- The notes use the Session Manual look, the teaching voice, and none of the words in `wiki/COPY-CORRECTIONS.md`.
- The review report ends with a count: "checked N of N" claims, assignments and phrases.

## What bad looks like

- Student-facing labels such as "manual", "Recognition drill", "Step zero", "The finalist" or "concept lesson".
- A tentative offer written as a promise; a drill instruction inferred from its title.
- A fresh visual system instead of the Session Manual.
- Any claim that a draft is posted, assigned or visible to a student when it is not.

## Inputs

Student and date (or "most recent completed session"), `students/<slug>/sessions/` transcript, `recap-calibration.md`, `wiki/teaching-voice.md`, `wiki/COPY-CORRECTIONS.md`, existing posted notes for the question type.

## Outputs

`students/<slug>/recaps/YYYY-MM-DD-recap.md` (with the private continuation), the build folder `brainstorms/YYYY-MM-DD-<student>-post-session/`, and a review report. Nothing else.

## Tools it gets, and the ones it never gets

| Gets | Never gets |
|---|---|
| Read: students, transcripts, corpus, wiki, posted-note reads | `gws gmail` send, reply, forward; any Drive write or delete |
| Write: `students/<slug>/recaps/`, its brainstorm build folder | `lsat-u-platform-actions` publish, assign or message |
| Run: the Session Manual builder and lint, local preview | Supabase writes; Lovable; creating a student folder |

Enforcement, as built and tested 2026-10-31: the agent has no send or publish tool and the `lsat-u-lessons` server is blocked in its frontmatter. Bash is allowed, so `system/scripts/recap_agent_guard.py` runs before each Bash call and refuses `gws` (except calendar), posting and assigning scripts, `lsatu-admin` write commands, email scripts and `git push`. Headless tests confirmed the refusals. Limit: the guard checks direct commands, so an agent that writes and runs its own script is not stopped by it. Codex does not read the allowlist or the hook. Related gap: AQ-046.

## The review layer

A separate session reads the finished notes beside the transcript and the calibration table and reports what it checked. The writer never reviews itself. Optional later: a reviewer that reads as the student would. First calibrate the reviewer on 5 to 10 recaps Joshua already passed or rejected.

## How much to trust it

Start with draft only and every note shown to Joshua. Loosen only on evidence: for example, after several recaps he approves with no edits, the agent may skip the "present three files" pause. Posting and assignment stay Joshua's explicit approval regardless.

## Corrections loop

Each correction Joshua makes lands in `recap-calibration.md` with the failed check. A problem seen twice becomes a rule in the skill or the builder lint.

## Owner and review date

Owner: Joshua. Last reviewed: set when the first dry run passes.

## Questions for Joshua

1. **Where does it run?** Recommended: a Claude Code agent the Recap drawer's Run button calls, with a Codex twin so either runtime works.
2. **Scope.** Recommended: the three-note set plus a homework proposal as text. Choosing and assigning the drill stays with `guided-drill-assignment`.
3. **Autonomy.** Recommended: draft only, never post, until you say otherwise.
4. **How do we know it is working?** Recommended: share of recaps you approve with no edits, and minutes from "run" to a reviewable set.
