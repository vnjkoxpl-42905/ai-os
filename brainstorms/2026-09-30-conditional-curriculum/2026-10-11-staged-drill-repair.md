# Repair every drill's learning procedure

User correction: the sufficient-practice route retained an old tabbed lesson panel, despite the integrated source bank. Importing 133 task instances did not import the source procedure or establish a consistent drill experience.

## Required result

- Audit every drill route. Preserve foundation 24, mixed adaptive 24, contrapositive 9, every original sufficient example and all 133 source task instances plus intentional revisits.
- Guided drills: visible rule, one operation at a time, attempted answer, specific feedback, correction before advancing. No generic ungated Next task around lesson blocks.
- Fade support: identify expressions and complete conditions; define symbols; construct the original; reverse and negate; read both forms in English.
- Independent source sets require blank production, including the learner's symbol legend. Models stay hidden until the complete attempt. Written work is self-reviewed, never falsely automatically graded.
- Preserve drafts and invalidate stale completion after revision. Saved local work is not account persistence.
- Teach qualifications, modal strength and symbol definitions before worksheet sets. Teach compound/quantified negation before the contrapositive revisits.
- Polish the actual UI at desktop and narrow widths, with readable stages, consistent hierarchy, visible progress, keyboard controls and reduced-motion support.

## Source procedure evidence

Reference notes audit: `2026-10-11-reference-notes-source-audit.md`. Group 1 zombie/real-estate and Group 2 lasting-accomplishment examples explicitly identify indicators, conditions, assign symbols, write original and contrapositive diagrams, and translate back. Raw homework and notes remain immutable.

## Current implementation scope for independent inspection

App: C:/Users/Joshu/dev/ai-os-projects/lsatu-conditional-bootcamp.
Builder: Codex with Codex workers. Existing checkout was already dirty. Base commit 67230dfae74a1466515d570fcb7b8a96ab5cb9c5 is not a claim that every difference from it belongs to this repair.

Inspect current files primarily:
- components/StagedReasoningDrill.tsx, staged-reasoning-drill.css and test.
- components/SourceWorksheetDrill.tsx, source-worksheet-drill.css and test.
- components/OpeningCourseContent.tsx, OpeningCourse.tsx, OpeningCourse.test.tsx.
- openingCoursePath.ts and content/sourceWorksheetDrills.ts as integration context.
All paths relative to src/bootcamps/conditionals.

Check correctness, stage order, production vs recognition, no answer leakage, inaccessible/unreachable stages, wrong progress, stale state, draft corruption, responsive design risks and complete bank reachability. Open new/untracked files. Do not review unrelated old changes as this repair. Do not edit files.

Host verification: targeted Vitest suites, TypeScript, production build, actual browser attempt/correction and narrow-layout checks. Reviewer has read-only source access; it cannot claim actual browser inspection unless it reads supplied screenshots, and even then should call it screenshot review.

## Review settings

Claude Code inspection requested with Opus and high effort, preserving the user's earlier model preference. At most two fresh inspection rounds. Report actual observed model separately from requested alias. No deployment, commit or push.
