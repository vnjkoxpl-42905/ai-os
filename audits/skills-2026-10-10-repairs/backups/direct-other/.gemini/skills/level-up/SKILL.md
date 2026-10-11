---
name: level-up
description: Use weekly (or when Joshua says "let's level up", "what should I automate next", "find me leverage this week") to surface and ship ONE new automation. Walks the 3Ms interview — Mindset (find the candidate) → Method (scope it) → Machine (build it). One run = one shipped artifact. Adapted for the ai-os EA workspace.
---

## Current AI OS execution contract

New shared skills require their matching catalog and project activation copies for Claude and Codex, with deliberate differences documented. Application code/dependencies live in sibling ai-os-projects. Eliminating an unnecessary workflow can be a completed result without creating a new artifact.

> *Adapted from The Three Ms of AI™. © 2026 Nate Herk (MIT — github.com/nateherkai/AIS-OS).*
> *The Three Ms of AI™ is a trademark of Nate Herk.*

## What this skill does

Walks Joshua through the 3Ms each week to surface and ship one new automation for the Jay-2 EA workspace. **One interview = one artifact.** Over 4-6 runs it installs the 3Ms as internal defaults — the real payoff. Read `references/3ms-framework.md` before running; quote its principles back during the interview.

## What this is NOT
- Not `/audit` (structural). This is functional: "what business leverage am I missing?" Run `/audit` first if structure is messy.
- Not a multi-candidate planner. One run = one artifact.
- The user does the thinking; the skill conducts the interview.

## When it runs
- Weekly ritual (pairs with `wrapup`), or on-demand when a manual task itches.

## Inputs to read first
- `context/priorities.md` — the 90-day slate
- `context/about-me.md` + `context/work.md` — role, business, weekly time-sucks
- `connections.md` — what's reachable, by what mechanism
- `references/3ms-framework.md` — the framework
- `decisions/log.md` — what's already shipped/considered (don't re-pitch)
- `wiki/tasks.md` + latest `wiki/log.md` — recent activity
- `.claude/skills/*/SKILL.md` frontmatter — existing capabilities

## Execution — three phases

### Phase 1 — Mindset (find the candidate)
Ask conversationally, in order:
1. *"Walk me through your week. What did you do 3+ times?"* (frequency)
2. *"Anything that felt manual, boring, or copy-paste?"* (drudgery)
3. *"Anything where a smart intern could've handled it?"* (delegation)
4. *"If 500 new students showed up tomorrow, what breaks first?"* (constraint)
5. *"What would give you 500 more students tomorrow?"* (growth lever)

Quote Mindset principles when they fit (Default Shift, Function Breakdown, "AI is better than you think"). **Output:** 1-3 candidates, one-line "why this is leverage" each. Ask: *"Pick one to scope."*

Seed candidates from known gaps if Joshua is blank: post-session dispatch (Gemini note → `students/<name>/` + drill + recap), daily inbox-triage (gws → priority buckets + drafts), consultation-followup batching.

### Phase 2 — Method (scope one)
1. **Find the constraint** — which bottleneck/growth lever, tied to Phase 1.
2. **EAD:**
   - *Eliminate first:* "What if we just stop doing this?" If nothing breaks → exit cheerfully, log the win to `decisions/log.md`, stop. **Don't automate waste.**
   - *Automate:* frame 60/30/10.
   - *Delegate:* if too complex/variable → suggest a person, log it, stop.
3. **Map the process** — Trigger · Data Sources · Transformations · Decision Points · Destination. If Joshua can't name all five: *"If you can't explain it to a person, you can't explain it to an AI"* → stop.
4. **Pick autonomy (L0–L4).** **Default = lowest that works.** Push back hard on L4. *Standing rule for this OS: anything a student/prospect reads is L2 minimum (drafts, human reviews) — never auto-send without a pre-approved template.*
5. **Tie to a KPI** — one of the Three Buckets (more customers / more per customer / less cost) + a specific metric. If none → stop.

**Output:** scoped spec appended to `decisions/log.md` as a dated entry (all five map answers + autonomy level + KPI).

### Phase 3 — Machine (build it)
Ask: *"How do you want to ship this?"* Ordered by Boring-is-Beautiful default:
1. **Prompt-only** — saved template Joshua runs by hand.
2. **Deterministic skill** — SKILL.md running a script, no AI step.
3. **AI-assisted skill** — SKILL.md with one AI call (drafts/classifies/summarizes).
4. **Sub-agent** — multi-step, own context. Last resort.

**Default = highest non-AI option that solves it.** More autonomy requires explicit choice.

**Save-to-both (this OS's standing rule):** write every new skill/agent to BOTH `.claude/skills/<name>/SKILL.md` (activated) AND the DB `skills/claude/<name>/SKILL.md`, project-scoped. For a Codex twin, mirror to `.agents/skills/`. Then note it for `system/scripts/gen-skill-index.py`.

**Every scaffolded artifact ships with:**
```markdown
---
bike-method-phase: 1  # Phase 1 — Training wheels. Run manually first.
three-ms-attribution: Adapted from The Three Ms of AI™ © 2026 Nate Herk.
---
```
Locks Phase 1 of the Bike Method; advances only by explicit edit. Surface Lego Principle, Validation Chain, Iteration Mindset while scaffolding.

## Output contract
Every run produces: (1) one `decisions/log.md` entry, (2) one scaffolded artifact saved-to-both, (3) a one-screen close (what was scoped, what shipped, Bike-Method Phase-1 reminder).

## Critical rules
1. One interview = one artifact.
2. Mindset phase always runs first, even with a pre-formed idea.
3. EAD enforces eliminate-first; exiting on Eliminate is a win.
4. Default to the lowest autonomy that works; push back on L4.
5. Boring-is-Beautiful default in Machine handoff.
6. Tie-to-KPI is mandatory or the skill stops.
7. `bike-method-phase: 1` in every artifact.
8. Save-to-both, every time.
9. Read-only on existing files except `decisions/log.md` and the new artifact.
10. Trademark + attribution on output.

---
> *The Three Ms of AI™ is a trademark of Nate Herk. © 2026 Nate Herk.*
