# Put a functioning Question finder in Home and Practice

Date: 2026-10-27
Status: PROPOSED. Independent review and implementation authorization outstanding. This is a review-local record; it does not amend app ADR0008 or lock a Joshua decision.

## Problem

The rail shortcut navigates to Practice before opening a modal, fails to open LR results, and leaves the user on Practice after dismissal. RC preview is useful and working in source. Removing the entire finder discards the known-question lookup task and Joshua's historically requested Home entry.

## Proposal

Remove the permanent rail shortcut after usable replacement checks. Retain Home and Practice triggers with the established Question finder terminology. Share the existing component rather than introduce a global shell service. Complete a safe LR preview using existing builder presentation where feasible; otherwise scope the delivery to RC with explicit labels. Preserve existing URL entry points, access checks and preview semantics.

## Alternatives

- Rename only: low cost but does not fix the LR dead end or cancellation detour.
- Delete all lookup: simpler navigation but removes useful known-reference access and working RC preview.
- Complete a global in-place overlay: viable if cross-page use justifies its lifecycle and shell integration cost. Usage frequency has not been measured, so this option is not rejected as useless.
- Retain the existing rail unchanged: preserves convenience but leaves the reproduced problems unresolved.

## Consequences and reversal

Users outside Home/Practice need an extra navigation step. The proposal favors a smaller permanent rail and functioning entry points. Preserve routing compatibility so the rail can be restored later without changing question identity or data. No existing student work, assignment, answer or exposure record is deleted or migrated. Future code must update the owning context/ADR descriptions to match delivered behavior, while preserving historical rationale.

## What would change the recommendation

Demonstrated cross-page lookup needs, credible evidence that a shared global overlay is simpler, or inability to retain useful Home/Practice access. Plan review must challenge these conditions rather than assume rail removal is automatically best.
