# Find the sections / practice test audit

**Date:** 2026-11-20
**Topic:** Locating where an audit of timed sections and practice tests was written
**Tags:** lsat-u
**File:** C:/Users/Joshu/dev/ai-os/handoffs/2026-11-20_find-sections-audit.md

---

## Summary

Joshua asked where an audit of the practice tests and sections lives. I searched the ai-os vault and the LSAT U checkout. He clarified the audit came from a session working on sections, not on practice tests and sections together. The match is the 2026-11-18 sections audit in the LSAT U repo. I read only its first 25 lines, not the whole file.

## What was decided / built

- Nothing was changed. This was a search only.
- Sections audit (2026-11-18, code and migration read only, app not run): `C:/Users/Joshu/dev/lsatu/docs/audits/2026-11-18-sections-post-section-review-audit.md`. Its companion plan is `C:/Users/Joshu/dev/lsatu/plans/sections-post-section-rebuild.md`. I did not check that the plan exists.
- Practice-test completeness script: `C:/Users/Joshu/dev/ai-os/projects/.lsatu-ops/scripts/audit-practice-tests.mjs`, with its test `projects/.lsatu-ops/src/lib/practiceTest.audit.test.ts`. I read only the script header and did not run it.
- Timed PT writer readiness (2026-09-30): `C:/Users/Joshu/dev/ai-os/research/audit-repairs-2026-10-08/historical-evidence/lsatu-connected-experience/docs/implementation-plans/2026-09-30-timed-pt-writer-readiness.md`.
- Finding from the sections audit header: there are two section systems, a legacy path (`src/pages/Drill.tsx`) and a protected server-sitting path (`TimedStandaloneSectionRunner.tsx`). On the protected path the student sees only "X / total correct" after a section, with no per-question review, timing or blind review. The live split of students between the paths is unverified.

## Open threads

- Joshua has not confirmed that the 2026-11-18 file is the audit he meant.
- The sections audit and its companion plan were not read in full.
- No audit covering practice tests and sections together was found.

## Handoff prompt

> Paste this into a new chat to continue:
>
> ```
> Read C:/Users/Joshu/dev/ai-os/handoffs/2026-11-20_find-sections-audit.md and continue
> from where we left off. Open C:/Users/Joshu/dev/lsatu/docs/audits/2026-11-18-sections-post-section-review-audit.md in full and ask me whether it is the audit I meant.
> ```

---

## Transcript coverage

Source: visible-context export, incomplete history
Available range: this conversation from the first user message on 2026-11-20 to this export
Missing sections: no earlier history. Tool outputs and the system prompt are excluded.

## Available transcript

### User
find the cat whre a audit was done for the practice test and sections if it adn ell me whereh is fid it

### Assistant
Searched the vault and found candidates: the practice-test audit script, a PT writer readiness plan and the 2026-11-18 sections audit.

### User
thre ws time whrethey workingo nthe sections and praice teses

### Assistant
Confirmed the 2026-11-18 sections audit in the LSAT U repo, listed the practice-test script and the 2026-09-30 readiness plan, and said no single audit covers both.

### User
not together it ws secitons but run the chat export skill andsend me theprompt so ican starte new schat send me hteprompt i has use the chat epsort skill ontaht chat
