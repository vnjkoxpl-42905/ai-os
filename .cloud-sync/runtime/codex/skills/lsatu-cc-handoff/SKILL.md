---
name: lsatu-cc-handoff
description: Operational skill for the LSAT U build loop. Trigger whenever Joshua is working on the LSAT U codebase and needs to translate a UI screenshot, complaint, idea, or bug into a Claude Code execution prompt. Also trigger on phrases like "send to CC," "paste box," "create a handoff," "fix this and send to terminal," "make a CC prompt," "send this to claude code," or whenever Joshua sends a screenshot of lsatprep.study or the lovable.dev preview with a complaint or change request. The skill enforces the analyze then write-brief-to-vault then give-paste-box pattern, the file path conventions, the hard rules (no em dashes, verbatim content, brutalist palette, no silent errors, direct commits), and Joshua's voice rules (terse, opinionated, no em dashes, modules not phases). This skill is the indexed front door for the build loop. The deeper rules live in LSATU memory and the lsat-u-architecture skill.
---


## Local execution contract (2026-10-10)

Write operational briefs to handoffs, never raw/sources. Preserve source files. Use the current checkout, task branch and actual user authorization; no default main commit, per-step commit or push. Include scoped dirty-state baseline and completion evidence.

## Workflow

# LSAT U Build Loop: Claude Code Handoff

This is the operational skill for translating Joshua's input into a Claude Code execution prompt. Use it every time the loop runs.

The loop: input -> analyze -> write brief to vault -> hand paste box back to Joshua -> CC executes -> Joshua returns with results.

## Phase 1: Analyze before writing

Before writing a single line of brief, do all of the following:

1. **Read the actual current code.** Do not write recommendations from memory. The LSATU repo is at `<current-ai-os-root>/../ai-os-projects/lsatu/`. The topic modules live in `src/topics/<topic>/`. Read the relevant view files, data files, and store files before recommending changes.

2. **Read the existing vault docs.** Curriculum work lives in `~/ai-os/raw/sources/lsat-u/curriculum/<topic>/`. Look for `_BUILD_SPEC*.md`, `MODULE_PLAN.md`, `_HANDOFF/`, `_source/`, `_archive/`. Existing briefs that contradict the new direction must be archived (move to `_archive/`).

3. **Verify content authenticity.** Joshua authors the LSAT curriculum. Claude does not invent LSAT content. When auditing quiz files, drill banks, or lesson body content, check whether items are verbatim from `_source/` files or from git history (e.g. `git show <sha>:<path>`), or if they were fabricated by a prior Claude Code run. Flag fabrications to a `_CONTENT_AUDIT.md` rather than silently rewriting.

4. **If a screenshot was provided.** Describe what is visible. List specific visual problems with concrete CSS-class-level fixes. Cross-reference against the rendering component (LessonBody.tsx, ModuleView.tsx, the per-quiz renderers) to identify the root cause.

5. **Push back where appropriate.** If Joshua's stated direction will introduce complexity (adding features, more sidebar entries, more drill types, more chrome), say so. The bootcamp default is simpler-not-more. Brutalist preservation is non-negotiable but everything else should reduce cognitive load.

## Phase 2: Write the build brief to vault

File path convention: `<current-ai-os-root>/handoffs/<topic>/<BRIEF_NAME>.md`

Name patterns Joshua uses:
- `MODULE_PLAN.md` (architecture-defining)
- `<DOMAIN>_<ACTION>.md` like `LESSON_READABILITY_FIX.md`, `MODULE_QUALITY_UPGRADE.md`, `MODULE_CLOSEOUT.md`
- `_AUDIT_<DATE>.md` for audit findings
- `_HANDOFF/<NN>_<NAME>_BRIEF.md` only if Joshua already has that subfolder convention going

**Required sections in every brief:**

1. Frontmatter line: `For: Claude Code`, `Branch/commit/push scope: use actual task authorization; preserve existing dirty work.`
2. Goal: one or two sentences.
3. Required reading: explicit list of files CC must read before writing code. Always includes the brief itself, the relevant view files, the architecture spec (`_BUILD_SPEC_v2.0.md` or `MODULE_PLAN.md`), and `~/ai-os/CLAUDE.md`.
4. Hard rules. Always include:
   - No em dashes. `grep -rn '—' src/topics/<topic>/` must return zero before push.
   - Verbatim curriculum content. Do not paraphrase walkthroughs, vocab callouts, worked examples, or LSAT stimuli.
   - Brutalist palette preserved. Same `brutal-*` tokens. Same `.topic-abstract` wrapper.
   - Every Supabase mutation returns `{ ok, error }`. No silent errors. Errors surface as toasts.
   - No `(supabase as any)`. Regenerate types if schema changes.
   - Use task branch and explicitly authorized commit/push scope; no default main mutation.
   - Do not invent LSAT content. Stop and ask if a source is missing.
5. Numbered steps. Always called "Step 1, Step 2, ..." not "Phase 1, Phase 2." Joshua dislikes the word "phase."
6. Per step: target files, what changes, expected outcome, commit message.
7. Verification block: explicit checklist for the final push (em dash check, build, dev walk, mobile viewport, reduced motion, keyboard-only when relevant).
8. Done-state report template using fenced code block with `DONE:` header, commits list, verification checks, open issues.

**Brief length target:** 100 to 250 lines. Tight. Concrete. No filler.

**Archive superseded briefs.** When a new brief replaces a prior plan in the same domain, preserve the old source and record its superseded status in the handoff; moving/deleting sources is not permitted. The vault stays clean.

## Phase 3: Hand the paste box back to Joshua

After the brief is saved, give Joshua a paste-box prompt as a markdown code block. The prompt must:

1. Reference the brief by full vault path with `<current-ai-os-root>/handoffs/...` (escape the space).
2. Tell CC to "execute the approved scope end to end; commit/push only as authorized."
3. Restate the hard rules in one short paragraph.
4. List the steps in one-line summaries.
5. Note any migrations or external actions required (e.g., "Apply migration via Supabase dashboard if CLI not linked").
6. End with: "If a step blocks, stop and post status. Otherwise run all N steps and post the done-state report. Go."

**The paste-box format is the deliverable Joshua actually uses.** It must be inside a single fenced code block so he can copy with one click. No surrounding commentary inside the code block.

## Phase 4: Voice and tone rules when writing to Joshua

- No em dashes anywhere. Use colons, periods, or restructure.
- Terse. Direct. Strong opinionated recommendations, not hedged suggestions.
- Push back when Joshua's direction would introduce complexity or break existing rules.
- Skills-check rule: before creating, modifying, or recommending any skill, read `~/ai-os/raw/sources/lsat-u/skills-reference/00_skills-strategy.md` and `01_skills-detailed-evaluation.md` first. Conform to documented patterns.
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
- Skipping the archive step when a brief supersedes prior work.
- Asking multiple questions when Joshua has said "take autonomy" or "just do it."
- Putting the brief in `/mnt/user-data/outputs/` or anywhere outside the vault. Vault path is the source of truth.

## Pointers to deeper sources

- LSATU architecture rules: `/Users/joshuaf/ai-os/skills/lsat-u-architecture/SKILL.md`
- LSATU repo: `<current-ai-os-root>/../ai-os-projects/lsatu/`
- Abstract bootcamp vault: `~/ai-os/raw/sources/lsat-u/curriculum/Abstract/`
- Skills strategy: `~/ai-os/raw/sources/lsat-u/skills-reference/00_skills-strategy.md`
- Claude folder system: `~/ai-os/projects/`, `~/ai-os/raw/sources/lsat-u/prompts/`, `~/ai-os/raw/inbox/chat-exports/`, `~/ai-os/archive/`
- Cowork prompts: `~/ai-os/raw/sources/lsat-u/prompts/`

When in doubt about a convention, check the lsat-u-architecture skill or the Abstract vault for an existing example. Then conform.
