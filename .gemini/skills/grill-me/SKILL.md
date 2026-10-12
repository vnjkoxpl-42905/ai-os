---
name: grill-me
description: A relentless interview to sharpen a plan, design, or topic, checkpointing every answer to a brainstorm file so nothing is lost. Use when the user wants to stress-test a plan, get grilled on a design, run a brainstorm or discovery session, extract what's in their head into a doc, build up their AI OS context over time, or says "grill me".
---

## Current AI OS execution contract

Preserve the current host-specific checkpoint behavior and explain it accurately in routers. Do not erase saved brainstorm state merely to make another host stateless. Reuse answered questions and prior approval.

# Grill Me

Two layers. The **interview method** comes from the `grilling` skill and is not restated here. The **capture discipline** below is what this wrapper adds: every answer lands in a durable markdown file, so nothing is lost as context fills up.

If the topic is implementation work, finish the interview here, then hand the agreed design to `claudex-loop` to plan and build.

## Step 1: set up the capture file (BEFORE the first question)

1. Read the applicable `AGENTS.md` and `CLAUDE.md`, then only the context pages and prior captures relevant to the topic. Starter-kit context lives in `context/`; in an established project follow its declared routes instead of creating a duplicate knowledge store. Reuse facts already supplied; ask about gaps, changes, decisions, and tradeoffs. Installing the skill does not start an interview.
2. Create the capture file at `brainstorms/{YYYY-MM-DD}-{topic-slug}.md` (create `brainstorms/` if missing). Every capture lives here, one predictable home regardless of topic. Do NOT scatter captures into project folders. A polished deliverable (plan, map, spec) may later move into the relevant `projects/` folder; the raw capture always stays in `brainstorms/`.
   - Get today's real date from the clock or shell (`Get-Date -Format yyyy-MM-dd` in PowerShell, `date +%F` in Bash).
   - Never overwrite an existing capture. Same date and topic: add a time or unique suffix and create exclusively. Resume an existing capture only when the user asks or clearly refers to that session; read it first and continue its question numbering.
   - No topic supplied or inferable: create an `untitled-discovery` capture with goal pending, ask what to explore, record the chosen topic and goal in that same file.
3. Write the header immediately: title, date, goal of the session, empty "Open flags" section.
4. Tell the user where you are saving, in one line.

## Step 2: run the interview

Call the Skill tool with "grilling". Follow it exactly: map the design tree, ask the whole frontier as a numbered round with a recommended answer per question, dispatch sub-agents for facts instead of asking the user, wait for answers, recompute the frontier, repeat until it is empty.

Two adjustments the capture layer imposes on the method:

- For **decisions**, give a recommended answer grounded in context and label it as a recommendation. For **personal or business facts**, ask neutrally. Never lead with invented facts, and never save your inference as the user's answer.
- When the user **cannot answer** something, capture it as a flag with the right owner and move on. Do not stall the round on it.

## Step 3: the checkpoint rule (non-negotiable)

After EVERY round of answers, BEFORE you ask the next round:

- Append one structured entry per answered question: the question, the key facts and decisions from the answer (in the user's words where wording matters), and any flags (things they could not answer, plus who should).
- Update the running summary when a later answer changes it. Preserve the original entry, mark it superseded, and link to the correcting answer so the reasoning stays traceable.
- Read back the saved entries before continuing. If the write fails, say so, keep the answers visible in chat, and do not claim they were saved or collect more answers without a working checkpoint.
- Only then ask the next round.

Never let two rounds pile up in your head before writing. The file, not your context, is the source of truth. Never make the user ask you to save progress.

Keep user-confirmed facts, tentative ideas, your recommendations, and unresolved questions distinguishable in the capture.

## Capture file structure

```
# {Topic}: Brainstorm / Discovery Notes
Date: {date} · Goal: {one line}
Status: in progress / paused / complete
Context sources: {relevant existing pages, if any}

## Summary / key decisions
(running synthesis, updated as you go)

## Q&A log
### Round 1
#### Q1 - {topic}
- Asked: {question}
- Recommended: {your recommendation, labeled}
- Captured: {user-confirmed facts and decisions, in their words where it matters}
- Tentative: {unconfirmed ideas, clearly labeled}
- Flags: {open item -> owner}
#### Q2 - ...
### Round 2
...

## Open flags (pending input)
- {item} -> {who can answer}
```

## At the end or on pause

Respect an explicit stop immediately; do not add a new question. Near the end, offer a completeness backstop ("anything we haven't touched?"). Then:

- Read the capture for contradictions or gaps. Mark unresolved conflicts explicitly; do not choose a business fact on the user's behalf. Update status and resume point.
- For sessions explicitly about building or updating AI OS context, merge user-confirmed durable facts and preferences into the appropriate existing context page, with a dated link back to the capture. Preserve unrelated content. Record confirmed meaningful decisions in the existing decision log without duplicating entries. Unknowns, brainstorm ideas, and your recommendations stay labeled in the capture until confirmed.
- For a plan or design interview without a request to update canonical context, the raw capture is the output. Suggest `/link` for routing a useful result, or `/level-up` for turning a selected opportunity into one improvement. Do not run either automatically.
- Ensure the operating manual or an existing index routes to `brainstorms/` when capture routing is absent, using the project's conventions and preserving shared manual parity. Individual captures do not each need a root-manual entry. Raw captures are dated interview evidence, not automatically current business truth.
- Give a short recap: clickable capture path, context pages actually updated, remaining flags, next step or resume point.

As `grilling` requires: do not act on the plan until the user confirms you have reached a shared understanding.

## Boundaries and verification

- Scope is the local interview capture and any requested context updates. No global-memory edits, publication, messages, or external-system changes. Do not request or save credentials; use references or redactions for secrets.
- The starter kit ignores `brainstorms/` in Git by default. This does not remove captures already tracked in an existing repository.
- Validate a fresh session, a same-day name collision, a resume, a correcting answer, a stop request, and a failed write. Verify that only confirmed facts reach canonical context and that earlier answers remain traceable.
