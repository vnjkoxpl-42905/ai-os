---
name: lsatu-cc-handoff
description: Create an LSAT U execution brief for Claude Code when Joshua explicitly asks for a CC handoff, paste box, or execution prompt. A screenshot or bug complaint alone requests diagnosis, not this handoff. Preserve source content, current project conventions, and the task's Git authorization.
---

# LSAT U Build Loop: Claude Code Handoff

This is the operational skill for translating Joshua's input into a Claude Code execution prompt. Use it every time the loop runs.

The loop: input -> analyze -> write brief to vault -> hand paste box back to Joshua -> CC executes -> Joshua returns with results.

## Step 1: Analyze before writing

Before writing a single line of brief, do all of the following:

1. **Read the actual current code.** Do not write recommendations from memory. The LSATU repo is at `../ai-os-projects/lsatu/`. The topic modules live in `src/topics/<topic>/`. Read the relevant view files, data files, and store files before recommending changes.

2. **Read the existing vault docs.** Curriculum work lives in `raw/sources/lsat-u/curriculum/<topic>/`. Look for `_BUILD_SPEC*.md`, `MODULE_PLAN.md`, `_HANDOFF/`, `_source/`, `_archive/`. Read sources without modifying or moving them. Record supersession in the new operational brief; preserve contradictions explicitly.

3. **Verify content authenticity.** Joshua authors the LSAT curriculum. Claude does not invent LSAT content. When auditing quiz files, drill banks, or lesson body content, check whether items are verbatim from `_source/` files or from git history (e.g. `git show <sha>:<path>`), or if they were fabricated by a prior Claude Code run. Flag fabrications in an operational `_CONTENT_AUDIT.md` under `handoffs/lsat-u/<topic>/` rather than silently rewriting.

4. **If a screenshot was provided.** Describe what is visible. List specific visual problems with concrete CSS-class-level fixes. Cross-reference against the rendering component (LessonBody.tsx, ModuleView.tsx, the per-quiz renderers) to identify the root cause.

5. **Push back where appropriate.** If Joshua's stated direction will introduce complexity (adding features, more sidebar entries, more drill types, more chrome), say so. The bootcamp default is simpler-not-more. Preservation of the current project design system is required but everything else should reduce cognitive load.

## Step 2: Write the build brief to vault

File path convention, relative to the current AI OS root: `handoffs/lsat-u/<topic>/<BRIEF_NAME>.md`. Never write, move or archive operational briefs under `raw/sources/`.

Name patterns Joshua uses:
- `MODULE_PLAN.md` (architecture-defining)
- `<DOMAIN>_<ACTION>.md` like `LESSON_READABILITY_FIX.md`, `MODULE_QUALITY_UPGRADE.md`, `MODULE_CLOSEOUT.md`
- `_AUDIT_<DATE>.md` for audit findings
- `_HANDOFF/<NN>_<NAME>_BRIEF.md` only if Joshua already has that subfolder convention going

**Required sections in every brief:**

1. Frontmatter line: `For: Claude Code`, plus the current checkout/branch and the actual commit/push authorization. Do not assume main or permission to publish.
2. Goal: one or two sentences.
3. Required reading: explicit list of files CC must read before writing code. Always includes the brief itself, the relevant view files, the architecture spec (`_BUILD_SPEC_v2.0.md` or `MODULE_PLAN.md`), and the current root `CLAUDE.md`. Follow the application's nearest instructions.
4. Hard rules. Always include:
   - No em dashes. `grep -rn '—' src/topics/<topic>/` must return zero before push.
   - Verbatim curriculum content. Do not paraphrase walkthroughs, vocab callouts, worked examples, or LSAT stimuli.
   - Preserve the verified current design system; retain `brutal-*` tokens and `.topic-abstract` only where the owning module uses them.
   - Every Supabase mutation returns `{ ok, error }`. No silent errors. Errors surface as toasts.
   - No `(supabase as any)`. Regenerate types if schema changes.
   - Preserve unrelated changes. Commit/push only when authorized by the task; stage only owned paths on the verified branch.
   - Do not invent LSAT content. Stop and ask if a source is missing.
5. Numbered steps. Always called "Step 1, Step 2, ..." not "Phase 1, Phase 2." Joshua dislikes the word "phase."
6. Per step: target files, what changes, expected outcome, proposed commit message when a commit is authorized.
7. Verification block: explicit checklist for the final push (em dash check, build, dev walk, mobile viewport, reduced motion, keyboard-only when relevant).
8. Done-state report template using fenced code block with `DONE:` header, commits list, verification checks, open issues.

**Brief length target:** 100 to 250 lines. Tight. Concrete. No filler.

**Record supersession.** Link the old brief and explain the replacement in the new handoff. Do not move or delete source evidence. Preserve old operational briefs unless Joshua explicitly authorizes relocation.

## Step 3: Hand the paste box back to Joshua

After the brief is saved, give Joshua a paste-box prompt as a markdown code block. The prompt must:

1. Reference the saved brief by its verified absolute path on this machine, quoted for the receiving shell.
2. Tell CC to execute the authorized scope end to end and state the actual Git/publication permissions.
3. Restate the hard rules in one short paragraph.
4. List the steps in one-line summaries.
5. Note any migrations or external actions required (e.g., "Apply migration via Supabase dashboard if CLI not linked").
6. End with: "If a step blocks, stop and post status. Otherwise run all N steps and post the done-state report. Go."

**The paste-box format is the deliverable Joshua actually uses.** It must be inside a single fenced code block so he can copy with one click. No surrounding commentary inside the code block.

## Step 4: Voice and tone rules when writing to Joshua

- No em dashes anywhere. Use colons, periods, or restructure.
- Terse. Direct. Strong opinionated recommendations, not hedged suggestions.
- Push back when Joshua's direction would introduce complexity or break existing rules.
- Skills-check rule: before creating, modifying, or recommending any skill, resolve current `skills/INDEX.md` and relevant creator/catalog instructions first. The source strategy file `raw/sources/lsat-u/skills-reference/00_skills-strategy.md` is optional background; the old `01_skills-detailed-evaluation.md` is absent and must not block a valid task. Follow current authority over historical advice.
- Modules not phases.
- Don't repeat what already shipped. Just acknowledge and move on.
- Don't ask multiple-choice questions when Joshua has given clear autonomy. Make the call, document it, move.

## Common brief types

**Audit brief** — finding gaps in shipped work. Output: `_AUDIT_<DATE>.md` plus a follow-up fix brief.

**Build brief** — implementing new feature or major restructure. Output: `<DOMAIN>_PLAN.md` or `<DOMAIN>_<FEATURE>.md`.

**Fix brief** — closing specific bugs or visual issues. Output: `<DOMAIN>_FIX.md` or `<DOMAIN>_READABILITY_FIX.md`.

**Closeout brief** — finishing items left open by a prior pass. Output: `<DOMAIN>_CLOSEOUT.md`.

**Cleanup brief** — removing zombies, archiving superseded files, regenerating types. Output: `<DOMAIN>_CLEANUP.md`.

## Anti-patterns to avoid

- Writing a brief without reading the current code first.
- Using "Phase 1, Phase 2" language. Always "Step 1, Step 2" or "Module 1, Module 2."
- Adding more sidebar entries when the conversation context is "simplify."
- Including em dashes in vault docs or paste boxes.
- Writing paste boxes that span multiple code blocks or include surrounding prose inside the fenced block.
- Inventing LSAT content. Joshua writes the curriculum.
- Failing to record supersession or moving immutable evidence.
- Asking multiple questions when Joshua has said "take autonomy" or "just do it."
- Putting the brief in `/mnt/user-data/outputs/` or anywhere outside the vault. Vault path is the source of truth.

## Pointers to deeper sources

- LSATU architecture rules: `skills/claude/lsat-u-architecture/SKILL.md`
- LSATU repo: `../ai-os-projects/lsatu/`
- Abstract bootcamp vault: `raw/sources/lsat-u/curriculum/Abstract/`
- Skills strategy: `raw/sources/lsat-u/skills-reference/00_skills-strategy.md`
- Claude folder system: `../ai-os-projects/`, `raw/sources/lsat-u/prompts/`, `handoffs/`, `archive/`
- Historical prompt evidence (read-only): `raw/sources/lsat-u/prompts/`; new operational prompts: `handoffs/lsat-u/`

When in doubt about a convention, check the lsat-u-architecture skill or the Abstract vault for an existing example. Then conform.
