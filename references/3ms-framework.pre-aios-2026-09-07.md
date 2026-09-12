---
type: reference
subject: The Three Ms of AI Mindset, Method, Machine
updated: 2026-07-17
aliases: []
---

# The Three Ms of AI™ — Mindset, Method, Machine

> *Adapted from The Three Ms of AI™. © 2026 Nate Herk. All rights reserved.*
> *The Three Ms of AI™ is a trademark of Nate Herk. Sourced from the MIT-licensed AIS-OS starter kit (github.com/nateherkai/AIS-OS).*

> *"The best automation is the one you barely notice. Start by eliminating what doesn't need to exist, then automate what's left with the least amount of AI possible."*

**Boring is Beautiful.**

---

## Why this is in the OS

This is the operator brain — how to think about, decide on, and build automation, independent of any tool or model. Read once, refer back. The `/level-up` skill walks all three layers weekly.

Tools change every six months. What doesn't change is how you THINK about automation, how you DECIDE what to automate, and how you BUILD and OPERATE the thing once it's running. That's what the Three Ms gives you.

---

## Layer 1 — MINDSET (How to Think)

### 1. The Default Shift
Before doing any task the old way, ask "How could AI do this?" If it can't do all of it: "How could AI assist with the first 30%?" It's never binary — the real question is always **"to what extent can AI be leveraged here?"** You don't know until you ask.

Internalize: **AI is better than you think, and improving faster than you think.** If it can't do something today, try again next month.

### 2. The Function Breakdown
Your role is a set of functions; each breaks into dozens of tiny tasks. **You don't automate your whole job. You automate one tiny piece. Then another. Then chain them.** One small task per day → hundreds automated in six months. Compounding is real.

### 3. The Curiosity Rule
Never accept AI output without asking why. Ask for three alternatives. Ask which it thinks is best and why. This is the antidote to "dark code" — **if you build something and can't explain how it works, you've built a liability, not an asset.** Treat AI as a mentor, not a vending machine.

### Expect the Dip
~20% less output the first week or two. Within two weeks, baseline doubles. **Fail fast, learn faster** — get to your first 10 mistakes safely and quickly. That's where the learning lives.

---

## Layer 2 — METHOD (How to Decide)

### 1. Find the Constraint
- **Q1:** *"If 500 new clients showed up tomorrow, what would break first?"* — finds bottlenecks.
- **Q2:** *"What would give you 500 more clients tomorrow?"* — finds growth levers.
Start with the constraint.

### 2. EAD: Eliminate, Automate, Delegate (in this order)
- **Eliminate first.** *"What happens if we just stop doing this?"* If nobody would notice it disappeared, kill it. **Don't automate waste.**
- **Automate second.** The **60/30/10 Golden Rule:** ~60% fully automated, ~30% AI-assisted (human reviews before it ships), ~10% stays manual. **Full automation is rarely the goal.**
- **Delegate third.** If it can't hit 60/30/10 — too complex/variable/judgment-heavy — hand it to a person.

### 3. Map the Process (five elements, on paper, before any tool)
Trigger · Data Sources · Data Transformations · Decision Points · Destination.
**Rule:** *if you can't explain it to a person, you can't explain it to an AI.*

### 4. The Autonomy Spectrum
| Level | Name | What happens |
|---|---|---|
| L0 | Manual | No AI. Human does it. |
| L1 | Suggested | AI suggests, human decides every step. |
| L2 | Drafted | AI drafts, human reviews and edits. |
| L3 | Supervised | Rules set, AI runs, human validates. |
| L4 | Autonomous | AI handles end-to-end. |

**Default to the LOWEST level that works.** Boring is Beautiful. **Workflows beat agents.** Push autonomy up only after the lower level proves out.

### 5. Tie It to a KPI
Every automation must move a number in one of **the Three Buckets:** (1) get more customers, (2) make each customer worth more, (3) cut costs. If it doesn't move a metric, stop. *"Because it's cool"* isn't a business case.

---

## Layer 3 — MACHINE (How to Build and Operate)

### BUILD
1. **The Lego Principle** — smallest possible steps, one input/one output per block. Start with **zero-AI steps first**; layer AI where actually needed. Modularity is freedom.
2. **The Assembly Line** — each AI step does one specialized job. Don't build a generalist.
3. **The Validation Chain** — validate each step's output before chaining. **Do NOT build the whole pipeline and test end-to-end.**
4. **The Iteration Mindset** — ship the POC, get real-usage feedback, expand. Perfectionism is the enemy of deployment.

### OPERATE
5. **The Bike Method** — roll out in phases:
   - Phase 1 — Training wheels: run manually, watch everything.
   - Phase 2 — Guided: automation drafts, doesn't send; you review every output.
   - Phase 3 — Watched: runs autonomously, you monitor with alerts + batch review.
   - Phase 4 — Hands-off.
   Even at 90% confidence, roll out 10% of volume first.
6. **The Intern Rule** — treat AI like a day-one hire: own identity/credentials (never yours), read-only by default, never impersonates you, full audit trail, scoped minimal permissions. *"You wouldn't trust someone you just met with your bank account."*
7. **The Kill Switch** — if an automation needs constant patching, produces low-quality output, or costs more to maintain than it saves, **tear it down.** Don't fall for sunk cost. Good operators know when to build AND when to destroy.

---

## Governing Principles
1. **Boring is beautiful.** Predictable beats clever.
2. **Deterministic steps can be finished. AI steps are always evolving.** Set expectations accordingly.
3. **Fail fast, learn faster.** Real learning lives in your first 10 mistakes.

---

## Jay-2 note (how this maps to this OS)
- **Intern Rule, one deliberate exception:** Joshua's `.env` intentionally holds passwords + bank info (decided 2026-07-17). Security therefore rests entirely on `.claude/settings.json` deny-lists and scoped keys — the hard tool layer, never prompt instructions. See `decisions/log.md`.
- Every automation built here starts at **L2 (Drafted)** minimum for anything a student/prospect reads — never auto-send without a pre-approved template.

> *The Three Ms of AI™ is a trademark of Nate Herk. © 2026 Nate Herk.*
