# Harden the saved material/depth guidance

## Scope and authorization
User asks claudex-loop to perfect the design principles and routes just saved. Documentation only. No app redesign, production interaction, commits, pushes, releases or provider substitution. Codex host/planner/builder; Claude independent plan reviewer and fresh final inspector. Requested Claude Opus 5.5, medium effort. Five plan reviews maximum, two inspections, two fixes maximum.

## Assumptions and evidence
- design/README.md is the shared domain entry point; design/principles.md owns the existing depth synthesis.
- User-selected still: raw/sources/design/2026-10-27-dashboard-material/dashboard.png with PROVENANCE.md and SHA256SUMS. User preference and visual interpretations are not measured usability evidence.
- User prefers warm paper/off-white and charcoal with material depth; palette is LSAT U-specific, principles generalize. Current user brief supersedes historical presets.
- Root AGENTS.md and CLAUDE.md must carry matching design route blocks. Preserve all unrelated content and all existing historical citations.
- Existing checkout has extensive unrelated work. Pre-build HEAD 7e3a37c49aad80bc3d36352b796612425fe9b051. before/ contains byte-exact target copies with inert .before suffixes (including AGENTS.md.before and CLAUDE.md.before) and before.json records their hashes; review is scoped to these targets, not all existing changes.

## Approach
Explicit fixes: link the decision-table depth row to its local material section and provenance; replace transient conversation/live wording with durable supplied-date and unknown capture-time facts; express compact balance as priority order with responsive arrangements; label likely effects as interpretations and interaction states as proposed rather than observed. Keep root route blocks byte-identical and no larger than before copies.

Independently review current documentation for factual overreach, conflicting requirements, retrieval failure, vague implementation guidance and accessibility gaps. Resolve material findings with the smallest edits in the existing owning pages. Ensure notes explain material tones, ground/section/control hierarchy, consistent lighting/contact/ambient shadows, edge definition, radius/spacing/type proportions, restrained semantic accents and state feedback without more cards. Describe patterns as reference-dependent rather than universal rules; preserve responsive adaptation and allow later explicit briefs.

Targets: design/README.md, design/principles.md, root AGENTS.md/CLAUDE.md DESIGN DOMAIN ROUTER blocks only; provenance clarification if warranted. Log changes in design/reviews/material-guidance-20261027/REVIEW-LOG.md and wiki/log.md; decisions/log.md only if user-approved direction needs clarification. No changes to original screenshot bytes or unrelated docs.

## Acceptance and proof
0. Root route blocks must not grow; changes beyond their matching route go in design pages.
1. A fresh reader can follow either root route to README, principles and original evidence and answer how to add depth without extra cards.
2. Matched runtime route blocks; every relative Markdown target in touched design pages and provenance exists. Check fragments for newly introduced links.
3. Archived screenshot SHA256 matches SHA256SUMS and PROVENANCE.md, and byte size matches recorded provenance. If the Temp original exists, compare it too; otherwise explicitly record original unavailable, not a match. Do not invent capture date or claim live runtime/phone evidence from one screenshot.
4. Guidance separates selected palette from general methods, visible observations from suggested interaction behavior, and aesthetics from usability/integration proof. Responsive arrangements follow task and viewport rather than freeze desktop geometry. Contrast/focus are checked on actual surfaces, never shadow alone.
5. Capture before/after file hashes and inspect exact before/ target-copy diff, not an assumption that old HEAD contains the existing guidance. Run a Python focused route/link/hash/required-content check saved outside repo, then python system/scripts/design-catalog.py and python system/scripts/wiki-maintenance.py --index if owning descriptions change. No full app tests needed for documentation. Existing unrelated wiki-lint findings are outside scope.
6. Fresh Claude inspect against pre-build HEAD, using before/ target copies as the authoritative scoped comparison; HEAD is only the runner baseline and includes unrelated older changes. Restricted target coverage disclosed. Runner fingerprints whole checkout; unrelated drift may prevent valid approval. If so report operational limit, never claim approval.

## Reviewer tool limits
Claude Read/Glob/Grep only, no shell or edits. Read target documents and provenance. Binary screenshot reading may be unavailable; host has visually read user-supplied screenshot and must report visual-inspection limitations explicitly. No web research needed; this is user-selected local evidence.

Snapshot policy: all before/ copies end in .before, not .md; they are inert evidence, excluded from Markdown link checks. Original logical path is the before.json key; append .before to locate its snapshot.
