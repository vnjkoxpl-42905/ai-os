---
type: teaching-notes
subject: Main Conclusion Web App Handoff Bundle
updated: 2026-07-17
aliases: []
---

# Main Conclusion Web App — Handoff Bundle

Lean handoff package for building Main Conclusion v1.0 in Claude Code.

## What's in this folder (essentials)

```
_export_2026-04-29/
├── README.md           ← you are here
├── handoff_prompt.md   ← THE prompt to copy/paste into Claude Code
├── spec.html           ← the full spec (391 KB, all 4 stages + design + features)
└── rules/
    ├── voice_calibration.md      Joshua's two-register voice (preserve verbatim)
    ├── pedagogical_flow.md       teach first, calibrate after (never cold-test)
    └── named_tools_lexicon.md    15 named tools (preserve verbatim)
```

(Older files in subfolders like `stage_summaries/`, `enhancements/`, `memory_snapshot/`, `handoff/`, `source_inventory/` are archived stubs — content lives in `spec.html`.)

## How to use

1. Open `handoff_prompt.md`.
2. Copy the entire fenced code block (between the triple backticks).
3. Paste it into Claude Code as one message.
4. Claude Code reads the spec and the rules, asks you a few setup questions, then builds v1.0.

## What v1.0 produces

- 6 modules of compiled content (Lessons, Reference, Drills, Question Simulator + Trap Master, Reading Hard Sentences, Diagnostics).
- Stage-Gate Tracker as the universal drill wrapper.
- End-of-module calibration drills (post-instruction, never pre-test).
- External PT-question-bank integration (wired to your existing PT bank at build time).
- Concept search across all modules.
- Re-do mode with hindsight on every wrong answer.
- R&R Drill — desktop with live mic, audio + templated diff highlighting (LLM-driven semantic comparison unlocks in v1.0.5).
- AI Tutor in stub mode (templated routing over the spec content; live LLM unlocks in v1.0.5).
- Diagnostic dashboard (mechanic + trait analytics).
- WCAG 2.1 AA compliance.
- Persistence abstraction layer (localStorage + IndexedDB for audio, designed for clean migration later).
- PDF export (session reports + Quick Reference Card).

## What v1.0.5 layers on (specced as commented hooks in v1.0)

- AI Tutor live LLM mode.
- R&R Drill LLM-driven semantic comparison.
- Spaced repetition seeded from end-of-module calibration misses.
- Live AI co-pilot during R&R.

## Inviolable rules

Both rules are reproduced as standalone files in `rules/` and referenced from the handoff prompt:

1. **Voice + content preservation** — preserve all 15 named tools, all worked examples, all voicy passages verbatim. Two-register voice split (whimsical for Lessons, decisive for Reference + Simulator).
2. **Pedagogical flow** — teach first, then calibrate via end-of-module drill. Never cold-test before instruction.

## Quality bar

Top-tier modern UI. Reference: Linear, Vercel, Stripe, Arc Browser, Notion (current), Apple HIG modern. Spec section §3.8 is the polish gate Claude Code measures against before declaring v1.0 done.
