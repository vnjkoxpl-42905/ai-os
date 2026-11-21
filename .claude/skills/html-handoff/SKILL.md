---
name: html-handoff
description: Export an existing interface as portable HTML files with handoff prompts for another model. Use for HTML handoff, share this design with another model, or package student and teacher previews. Preserve the current design; this is an export task, not a redesign or deployment.
---

# HTML handoff

Deliver the files quickly. Use the current implementation and sample data, not a separately rebuilt mockup.

## Default path

1. Reuse the active checkout and its existing exporter. For LSAT U, use `scripts/verification/export-role-home.mjs`; its guide is `docs/verification/export-role-home.md`. If the current job already produced verified, unchanged files, package those instead of rebuilding. Do not restart app discovery or design research.
2. Use the wrapper below to export and package all requested views in one invocation. It runs the LSAT U exporter once; that exporter compiles once, embeds React/GSAP/CSS/fonts, blocks backend access, and writes one HTML and one handoff Markdown per role plus `auto-checks.json`. Do not run a separate export first.
3. Run the combined command:

   ```powershell
   python <skill-directory>/scripts/export.py --repo <active-app-checkout> --out <output-directory>
   ```

   To package existing current outputs without another build:

   ```powershell
   python <skill-directory>/scripts/export.py --package-only --out <output-directory>
   ```

   The wrapper verifies the report's HTML hashes, includes only named deliverables, skips older screenshots and creates `html-handoff.zip`. It does not install anything, run app tests, or call another model.
4. Make one focused browser check per HTML: correct role renders, handoff is accessible, no blocking load error, and one representative sample interaction works. If these exact files were already checked in this job, reuse that evidence. Add one PNG per view when the receiving model cannot render HTML or the user requests visuals. Use the browser tool already available; do not introduce a second browser workflow. Repackage after adding screenshots.
5. Every run must generate `START-HERE-PROMPT.md` in the output folder and include it in the ZIP. It must give the resolved absolute folder path, identify each current file and its purpose, explain the reading order, distinguish previews from production, and tell a model without local filesystem access to request the ZIP upload. Use only current packaged filenames, not older folder contents. The wrapper generates this automatically, including in package-only mode.
6. Deliver the ZIP, individual HTML links, and `START-HERE-PROMPT.md` immediately. Include the ready-to-paste routing prompt in a fenced code block in the final response, with actual absolute paths rather than placeholders. Say that sample interactions do not establish backend persistence. Give the repeat command when automation was requested. Further design reviews are separate work unless explicitly requested.

## Prompt contents

Reuse the project's role-specific handoff prompts. Include the goal, approved visual direction, known owner preferences, requested review scope and simulation limits. Embed the prompt in the HTML and provide a companion `.md`. Keep it near the beginning of source so a model can find it without reading a minified bundle. Do not include credentials or live private records.

For creative redesign handoffs, give Claude Code or Codex broad creative ownership. Treat the current UI as context, not mandatory design requirements. Do not freeze colors, typography, card shapes, calendar treatments or layouts unless the current request explicitly requires it. Preserve product truth, permissions and functional semantics, while inviting a bold coherent redesign, local implementation and visual iteration. The export operation itself still preserves the current implementation; creative freedom belongs to the receiving model's task. Match its requested scope, rather than carrying old review-only or preserve-everything language into a newly authorized redesign.

## Stop scope from growing

- Prefer an existing exporter over manual DOM capture, a new mockup, or multiple competing export strategies. Change approach only for a concrete blocker.
- Do not repeat a five-width matrix or full repository suite merely to package an already verified view. Broaden checks only if export changes affect layout, a defect appears, or the user asks.
- Reuse bundled/cached assets. Do not research new fonts or install dependencies to improve an export's appearance. Report a missing asset instead of silently substituting it.
- Browser smoke review is the default. Claude, independent review rounds, extensive accessibility audits and production tests run only when requested or needed for an unresolved material issue. Never claim structural checks are visual approval.
- Stop when the named files exist, hashes/portability checks pass and the focused smoke checks pass. Send usable links before offering further refinement.
- No commit, push, deployment, message sending or live record changes are implied by an HTML handoff.

## Other projects

The wrapper currently supports the LSAT U export adapter. For another project, reuse its existing build/export path and the same compact deliverable/check pattern. Do not run this adapter against an unrelated app or turn a simple export into a general exporter framework. If no adapter exists, create only the smallest project-local export needed for the requested views.

<!-- BEGIN GENERATED DESIGN HUB ROUTE -->
For design work, first read the shared Claude Code/Codex design hub at
`C:/Users/Joshu/dev/ai-os/design/README.md` for relevant principles, sources,
skills, repositories and research. Keep this skill in its required runtime home.
<!-- END GENERATED DESIGN HUB ROUTE -->
