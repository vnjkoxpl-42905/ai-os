---
name: audit
description: Use when Joshua asks to audit the OS, score the setup against the Four Cs, or asks "is my AIOS working" / "audit my setup" / "where do we stand" / "find gaps". Produces a Four-Cs scoreboard (/100) with the top-3 leverage-ranked fixes. Read-only. Adapted for the ai-os layout (wiki, students, corpus, native memory, gws connections).
---

## What this skill does

Runs the **Four Cs Audit** on the `~/ai-os` workspace. Reads — never writes — the router, memory, skills, agents, connections, decisions, wiki, and domain folders. Scores each C out of 25. Surfaces strengths + the top-3 leverage-weighted gaps with concrete next-step commands.

**Scope is structural — "is the OS built right?"** It is NOT a capability planner. Capability gaps ("you could build X if you connected Y") belong to `/level-up`. First run is the baseline; re-run to watch the score climb.

> Adapted from the AIS-OS `/audit` skill © 2026 Nate Herk (MIT), tuned to Joshua's ai-os layout.

## Today's context
- **Date:** !`date +%Y-%m-%d`
- **Root:** `C:/Users/Joshu/dev/ai-os`

## The Four Cs (25 each = 100)
| Layer | Test |
|---|---|
| **Context** | Knows the business — identity, voice, decisions, wiki, domain knowledge |
| **Connections** | Reaches Joshua's stuff — gws CLI, Stripe, Cal.com, Supabase, browser MCP |
| **Capabilities** | Knows how to do work — skills + agents |
| **Cadence** | Runs without being asked — launchd jobs, hooks, recurring rituals |

## Execution

### Step 1 — Discover the shape (patterns, not exact paths)
Use Glob/Read/Bash to check:
- **Operating manual:** `CLAUDE.md`, `AGENTS.md` (twin), `.claude/rules/`
- **Memory:** native store `~/.claude/projects/-Users-joshuaf-ai-os/memory/MEMORY.md` (count entries)
- **Context layer:** `context/{about-me,work,priorities}.md`
- **Second brain (Level 2 — a strength, credit it):** `wiki/` (hot.md, index.md, tasks.md, concepts/, entities/), `corpus/` (teaching knowledge), `students/` (client data)
- **Skills:** `.claude/skills/*/SKILL.md` (count + frontmatter)
- **Agents:** `.claude/agents/*.md` (count)
- **Connections:** `connections.md`; `.env` keys (`git check-ignore .env` then count keys, never print values); gws CLI presence (`which gws`); MCP servers in `.claude/settings.json` / integrated-browser
- **Reference guides:** `references/`, `references/{tool}-api.md`
- **Decisions:** `decisions/log.md` (entry count + newest date)
- **Cadence:** `launchctl list | grep brain` (backup job), `.claude/settings.json` hooks, skills named `pickup`/`wrapup`/`daily-*`/`weekly-*`

Don't penalize non-canonical names when the intent is captured elsewhere. This OS uses `corpus/`+`wiki/` where the vanilla kit uses `references/` — credit them as Context.

### Step 2 — Score each C (25 pts)

**Context (25)**
| Criterion | Pts | Detect |
|---|---|---|
| Router exists + substantive | 5 | CLAUDE.md > 200 words |
| Identity / role / voice captured | 5 | `context/about-me.md` + `wiki/teaching-voice.md` exist |
| Persistent memory, multiple entries | 5 | native MEMORY.md > 3 entries |
| Domain knowledge base | 5 | `wiki/` OR `corpus/` populated (this OS: both → full marks) |
| Decisions captured | 5 | `decisions/log.md` ≥ 1 entry |

**Connections (25)** — mechanism-agnostic; a domain counts via MCP, script, gws CLI, or `.env` key + ref guide.
| Criterion | Pts | Detect |
|---|---|---|
| Tier-1 domain coverage | 10 | 1.4 pts per reachable domain (7 domains in `connections.md`), round to 0.5, cap 10 |
| Reference guide presence | 5 | −1 per connected API tool with no `references/{tool}-api.md`, floor 0 |
| Auth / freshness | 5 | −1 per connection in needs-auth/expired, or `last checked` > 30 days, floor 0 |
| Documented in `connections.md` | 3 | 0 missing · 1 sparse · 2 most · 3 all reachable |
| Read-AND-write balance | 2 | ≥1 connection can WRITE (gws send, Supabase write). 0 if all read-only |

**Capabilities (25)**
| Criterion | Pts | Detect |
|---|---|---|
| 3+ skills activated | 10 | count `.claude/skills/*/SKILL.md` |
| 1+ user-built skill | 10 | any skill not in {onboard, audit, level-up, skill-creator, gws-*} — this OS has many (pickup, wrapup, second-brain*, graphify, drafts, etc.) |
| 1+ agent defined | 5 | `.claude/agents/*.md` ≥ 1 (currently 0 → this loses points; flag it) |

**Cadence (25)**
| Criterion | Pts | Detect |
|---|---|---|
| 1+ recurring/scheduled trigger | 10 | `launchctl` shows backup job, OR SessionStart hook in settings, OR skill named `pickup`/`wrapup`/`daily-*` |
| Recent activity signal | 10 | files in `.claude/skills/` modified < 30 days, OR `wiki/log.md`/`decisions/log.md` entry < 30 days |
| Templates / reusable scaffolds | 5 | `references/`, `templates/`, or skill-embedded templates present |

### Step 3 — Top-3 gaps by leverage
leverage = (points lost) × multiplier.
- 0 tier-1 domains: **4x** · router missing/thin: **3x** · ≤2 domains: **3x** · 0 skills: **2x** · no recurring trigger: **2x** · all read-only: **2x** · 0 agents: **1.5x** · 0 ref guides for connected APIs: **1.5x** · no decisions log: **1.5x** · else **1x**.
Sort desc, take top 3, write a one-line concrete next step each (e.g. "write `.claude/agents/<name>.md`", "append to `decisions/log.md`", "save `references/{tool}-api.md`", "build the post-session dispatch skill via `/level-up`").

### Step 4 — Output the report (Markdown, in chat, < 60s)
```
# AIOS Audit — {date}
**Score: {total}/100** ({stage})

Stages: 0-39 Foundation · 40-69 Built · 70-89 Compounding · 90-100 Autonomous

## Scoreboard
Context        {bar}  {n}/25  {label}
Connections    {bar}  {n}/25  {label}
Capabilities   {bar}  {n}/25  {label}
Cadence        {bar}  {n}/25  {label}
(bar = ## per 5pts; label: Strong ≥20 · Solid 15-19 · Thin 8-14 · Missing <8)

## Strengths
- {1-3 bullets from top-scoring criteria}

## Top 3 Gaps (ranked by leverage)
1. **{gap}** (−{pts} × {mult}) → {next step}
2. ...
3. ...

## Suggested next: {single most-leveraged action}

---
Structural gaps only. For CAPABILITY gaps (what the OS could DO but can't yet), run /level-up.
```

### Step 5 — Offer to save
Ask: "Save this to `audits/audit-{date}.md` to track the score over time?" If yes, write it (create `audits/`; it's git-ignored). Only writable side effect.

## Notes
- **Read-only by default.** Never modify router, memory, skills, or vault files. Only optional write is the audit report.
- **Be honest, not generous.** Most real setups land 40-70. A 95 is a flex.
- **Credit the Level-2 wiki** — it's this OS's biggest Context strength and the vanilla kit lacks it.
- **Don't print secret values.** Count `.env` keys; never echo them.
- **Speed matters** — frontmatter-only for skill counts; targeted reads.
