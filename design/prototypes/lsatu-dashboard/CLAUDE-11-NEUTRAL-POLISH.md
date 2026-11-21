# Review and polish version 11, palette locked

2026-10-26. Explicit user request: "have claude opus 5.5 medium review this version again and polish it, but keep the charcoal and off white palette". Claude designs/implements; Codex independently verifies. Standalone authorized work order, not covered by the old apricot or navy/gold review approvals. No new requirements interview is needed.

## Palette is a hard constraint

Keep charcoal #131718 / #252b26 and off-white #f7f4ee, with neutral intermediate surfaces, neutral shadows and restrained grayscale or near-neutral accents. NO gold, brass, navy, blue, claret, orange, apricot, metallic gradients or new coloured chips. Existing CSS variable names such as lamp/brass/blue/claret are historical aliases: their values in the CURRENT source are neutral and must remain neutral. Do not read the old README's colour descriptions as current instructions. User explicitly rejected the navy/gold original and Codex corrected it. Palette correction is settled and takes precedence over all older design documents. Maintain depth with tonal separation, border craft and shadows, not added colours or blur.

## Scope and ownership

You are not alone in this codebase. Do not revert others' work. You exclusively own NEW output files in this clean sparse worktree:
design/prototypes/lsatu-dashboard/new-versions/11-neutral-polish/style.css
design/prototypes/lsatu-dashboard/new-versions/11-neutral-polish/POLISH.md

Read the CURRENT version, review the actual neutral screenshots and implement a thoughtful bounded CSS polish. Deliver a complete replacement stylesheet, plus a short findings/disposition note explaining what mattered and what changed. This is review AND implementation; do not stop at advice or ask approval for delegated polish choices. Never invent a quota of problems. No new full redesign, no copying original navy/gold colours, no new dependencies, downloads, font changes or new imagery. Do not edit app.js or index.html: preserve every working interaction and route. Codex will integrate your stylesheet into the existing version11 after validation, preserving the old neutral stylesheet. Do not write to the original archive, other generations, app repositories or external services. No commits/staging/push/deploy/messages.

## Exact reference inputs

Current source root: C:/Users/Joshu/dev/ai-os/design/prototypes/lsatu-dashboard/new-versions/11-claude-studio/
- Read style.css in full and relevant app.js/index.html markup to understand selectors.
- View artifacts/neutral-1048.png and artifacts/neutral-390.png. These show the palette correction; artifacts/home-* and final-preview-* may show the older navy/gold state and are NOT the target palette.
- Read VERIFICATION.md's palette correction and prior checks for technical context. README's original design rationale is historical; preserve the charcoal/off-white correction over it.
- Shared design hub: C:/Users/Joshu/dev/ai-os/design/README.md. Use only directly relevant existing resources. Do not load the entire vault or revisit unrelated source generations.

Local original app preview http://127.0.0.1:5203/?palette=neutral#home is synthetic only. No live production inspection exists. You have file/Read/Write tools; prior headless Bash commands were denied. Do not retry shell after a denial or weaken permissions. Host handles setup, assets and browser proofs. Font/assets paths in CSS must remain unchanged.

## Review focus

Judge visible hierarchy, text clarity, density, alignment, spacing rhythm, control consistency and depth at1048 and390. Consider whether desktop hero scale/greeting spacing makes assignments unnecessarily hard to reach; refine rather than flatten or strip all character. Keep expressive Newsreader headings and readable Manrope work text. Avoid tiny tracked caps, weak metadata or broad blur. Make hovered/active states and focus rings fit the same neutral palette. Fix obvious small inconsistencies only when supported by source or the supplied image.

Keep accessibility fixes: whole labels, touch-friendly controls, visible keyboard focus, protected modal text, responsive sidebar, scrollable teacher table, reduced motion. Preserve the calendar container queries at the end of the CURRENT stylesheet: .week inline-size container,36rem list threshold and12rem note-row threshold. Those fixed subtle internal overlap at320–1048 and100/200% root text. Do not replace them with viewport-only queries or hide overflow. Preserve countable12-cell statement progress, with5done/next6, intrinsic wrapping, clear state differences without colour reliance. User data remains browser-local/synthetic.

## Delivery, verification and limits

POLISH.md: state actual review coverage (which source and images you read), concrete findings with decisions and changes, palette commitment and remaining limits. Do not claim a browser run or independent review of your own earlier design. Record author as Claude Opus5.5 medium, but distinguish requested flags from observed runtime identity if unavailable to you.

No build step. Required proof command for the host: node --check C:/Users/Joshu/dev/ai-os/design/prototypes/lsatu-dashboard/new-versions/11-claude-studio/app.js

Host will stage the candidate against a read-only copy of current runtime/assets, capture desktop1440/1048 and phone390/320, check local asset loads, typography and no document overflow, enlarged text and the calendar internal bounds, and affected hover/focus/modal behaviour. Existing13 interaction/21 feature checks available in current artifacts; rerun only relevant checks when justified. Candidate must stay portable file:// and offline. Codex independently inspects changed CSS and POLISH.md, with a fresh CLI inspection if available (previous Codex MCP discovery failed); otherwise disclose native read-only fallback. Max2builder fix rounds and2independent inspection rounds. No production changes or user visual approval claimed.
