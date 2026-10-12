---
name: lovable-prompt
description: Produce a short, paste-ready prompt for Lovable when a change can only happen through the Lovable UI (not code Claude Code can reach directly, not a Supabase migration). Use when Joshua asks "give me the prompt for Lovable", "what do I send Lovable", or a task turns out to require Lovable-side config/UI action. Trigger with /lovable-prompt.
---


## Local execution contract (2026-10-10)

Use current sibling app instructions and an available approved transport. Supabase MCP is not assumed available. Lovable Cloud Edge Functions deploy through Lovable with required authorization; direct SQL is not universally prohibited. Resolve actual safe-push route and separate preview from publication.

## Workflow

Produce a short, paste-ready prompt for Lovable's chat, for the residual class of changes Claude Code cannot reach directly.

## When this applies

Before reaching for this, check whether the task is actually reachable another way:
- **Schema/data change** → use the Supabase MCP tools directly (`apply_migration`, `execute_sql` with `confirm_cost`). Do not hand this to Lovable.
- **Code change in the repo** → make it directly and push via `.claude/safe-push.sh` (see LSATU CLAUDE.md). Do not hand this to Lovable.
- Only fall back to a Lovable prompt for things genuinely gated behind the Lovable UI/platform itself: project-level settings, Lovable's own deploy/preview config, or when Joshua explicitly wants Lovable's agent to do the implementation instead of Claude Code.

## Output format

Joshua's preference (from repeated corrections: "cosie short promts" / concise short prompts): **short**, in a fenced code block, no preamble inside the block, one task per prompt unless he asked for a batch.

```
[imperative, 1-3 sentences: exactly what to change, plaintext, no markdown inside the block]
```

Above the code block, in plain text (not in the block):
- One line on why this needs to go through Lovable rather than being done directly.
- Anything Joshua should verify after Lovable applies it.

## Rules

- No em dashes.
- Never pad the prompt with context Lovable doesn't need (file structure explanations, rationale) — Lovable prompts are terse instructions, not briefs.
- If the change touches product rules in the LSATU CLAUDE.md (Foyer/Mainhub nav, granular feature flags, no fake data, etc.), restate the relevant constraint inside the prompt so Lovable doesn't violate it.
