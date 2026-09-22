# Student Access Tiers: Brainstorm / Discovery Notes
Date: 2026-09-22 · Goal: Pin down a three-tier access model for LSAT U before any code is written
Status: in progress
Context sources: live `profiles` access flags (13 booleans), `admin-manage-users` edge function, `DeskPeopleSurface` People page, PR #129 (revoke-all fix, merged), PR #130 (archive + permanent delete, merged)

## Starting position (established earlier today, not re-asked)

- Access today is 13 boolean columns on `profiles`, all defaulting to **true**. A new signup gets everything.
- `useUserPermissions` reads them, `ProtectedRoute` gates routes, the classroom rail padlocks items. Admins bypass all flags.
- Grant Full Access / Revoke All Access exist and now work correctly (PR #129). Archive and permanent delete exist (PR #130).
- Per-flag toggles and Trial/Standard/Full templates already exist in `adminUsers.ts` + `AdminDashboard.tsx`, but `AdminDashboard` is **not mounted on any route**, so none of it is reachable today.
- The edge function already supports single-flag `toggle` and `apply_template` actions.
- `profiles` is now in the realtime publication, so a flag change reaches an open tab immediately.
- Neither PR is live on lsatprep.study yet: the migration for #130 is unapplied and the frontend is unpublished.

## Tier sketch as stated (Joshua's words, unverified as final)

- **Tier 1** - triggered by booking one session; that one session grants full access to every feature.
- **Tier 2** - Joshua chooses which features. Individual toggles, instant effect, removing a toggle removes the thing from the platform for that student.
- **Tier 3** - access only to what he strictly assigns (e.g. one practice test section), nothing else.

## Summary / key decisions

(running synthesis, updated as answers land)

## Q&A log

(rounds appended below as they are answered)

## Open flags (pending input)

- (none yet)
