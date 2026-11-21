# Question finder review context

Date: 2026-10-27. Scope: persistent documents for reviewing the existing fix proposal. No application implementation or publication authorized.

Joshua reported that Find a question in the side rail feels unhelpful and requested investigation of its purpose and alternatives. Subsequent requests authorized independent plan reviews, first Gemini, then Claude, and now document-backed Gemini review. None authorized deployment or a change to student records.

The confirmed problem is that the live teacher LR path selects an address but cannot open it; invoking the rail utility navigates to Drills and dismissal remains there. Current-main snapshots confirm RC has a metadata-first preview, while LR opening is disabled. These observations are dated; they do not establish restricted-student behavior or usage frequency.

## Authority and baseline

- App repository: `vnjkoxpl-42905/lsatu-684d89db`.
- Reviewed source baseline: `dbf78f7e68f995e68cdbe9fa1d83337f9d386ad2`. A fetched ref was unchanged at the start of the Claude pass. Revalidate before any future build.
- `evidence/` holds complete source snapshots at that ref. Filenames flatten `/` to `__`. The primary app working tree is older and contains unrelated edits; do not substitute it for these snapshots.
- Existing `src/components/classroom/CONTEXT.md` owns product terminology, including Question finder, Home and Question screen. Its description of scored finder launches and older Drill routing is historical and disagrees with newer code. Do not silently restore those older behaviors.
- App `CONTEXT-MAP.md` routes Classroom, Guided Drills and RC to separate contexts. No standalone Classroom GLOSSARY.md exists at the baseline; terms live in its CONTEXT.md.
- ADR0008 describes the older LR scored-attempt / RC whole-passage launch design. Current RC metadata preview and LR-disabled behavior supersede that implementation description.

## Decision map

Confirmed scope: diagnose and strengthen the plan; preserve student work and permissions; do not implement.

Host proposals awaiting implementation authorization: remove the global rail shortcut after replacement checks; retain Home and Practice entry points using the same finder; complete safe LR preview or deliver an honestly labeled RC-only capability; preserve RC exposure rules; repair navigation and access handling. These are proposals, not locked Joshua decisions.

No unanswered requirement prevents independent review of these alternatives. The reviewed plan must expose unresolved implementation choices rather than presenting them as completed work. See PLAN.md, GLOSSARY.md and ADR-001-question-finder-placement.md.

## Review history

Earlier Gemini run 1 returned malformed structured output; its raw suggestions were checked by the host and incorporated. Run 2 timed out. Claude returned usage_limit_reached before processing the review. None approved the plan. This explicit new Gemini request authorizes the provider switch for this review pass. Use gemini-4-argon, medium effort, at most five rounds. Record actual completed status and verdict; never infer approval from raw feedback or a launched process.
