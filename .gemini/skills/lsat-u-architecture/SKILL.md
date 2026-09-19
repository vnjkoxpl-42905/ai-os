---
name: lsat-u-architecture
description: Architectural source of truth and entry point for LSAT U platform rules. Use this skill whenever building, modifying, speccing, or referencing LSAT U platform features. Trigger when discussing component picks, routing, state models, design tokens, drill mechanics, Foyer navigation, Supabase realtime channels, identity/admin patterns, the always-violate rules, or any decision about how LSAT U is built. Also trigger when writing Claude Code build briefs for LSAT U, when comparing topic modules to the Causation Station architectural template, when explaining LSAT U component patterns, or when reviewing code against platform rules. This skill is the indexed entry point. The canonical full sources live in the vault; this skill gives you the always-violate rules at a glance and routes you to the deeper references. Trigger automatically when Joshua mentions LSAT U code, architecture, components, drill behavior, Foyer, Supabase, build briefs, or topic module integration, even without explicit invocation.
---

# LSAT U Architecture

This skill is the entry point for LSAT U platform architecture. The canonical full content lives in the Obsidian vault and Joshua's memory. This skill gives you the always-violate rules at a glance, the quick decision rules, and explicit pointers to the deeper sources.

Treat the vault as source of truth. Treat this skill as the indexed front door.

## Always-violate rules (NEVER break these)

These are the daily-use rules. Every contributor follows them without exception. Violating one breaks LSAT U.

1. **Granular feature flags, not roles.** Permissions are flag-driven, never role-driven. Admin status is a flag, not a role.
2. **Admin always displays as "Joshua"** via `displayName.ts`. Never expose the underlying account identifier in UI.
3. **No bottom dock.** Foyer is the navigation surface. Do not add a bottom dock anywhere.
4. **Drill is always dark mode** with cleanup restore on exit. Other surfaces follow user preference. Drill is fixed dark.
5. **1:1 messaging only** between admin and student. No group, no broadcast.
6. **Zero layout shift highlighting.** Use `box-decoration-break: clone`. Highlights never reflow content.
7. **SVG ring not Canvas** for the Foyer hero (`radial-orbital-timeline.tsx`). Canvas is banned for that surface.
8. **Postgres-side provisioning** for new users and resources (post Issue #7). Application-side provisioning is removed.
9. **Deterministic channel names** for Supabase realtime. No random IDs in channel names.
10. **DB mutations never swallow errors.** Every mutation surfaces failure to the user or rethrows.
11. **Causation Station is the architectural template** for all topic modules. Inherit its patterns. Do not invent new patterns per topic.
12. **Topic modules are repo-native, not standalone.** No separate apps, no separate hosting. Topic modules live inside the LSAT U repo and share its routing, auth, components.

## When in doubt (quick decision rules)

- Granular flag or role? **Flag.**
- New nav surface or Foyer? **Foyer.**
- Drill light mode or dark? **Dark.**
- Custom component or library? **Library, unless impossible.**
- Swallow the error or rethrow? **Rethrow.**
- Topic module standalone or repo-native? **Repo-native.**
- Random channel ID or deterministic? **Deterministic.**
- Application-side or Postgres-side provisioning? **Postgres.**
- Canvas or SVG for the Foyer ring? **SVG.**
- Invent a new pattern or inherit Causation Station? **Inherit.**

## Canonical sources (read these for deeper context)

For anything beyond the daily-use rules above, route to the canonical content. Authority order when sources conflict, from highest to lowest:

1. **Live repo `~/ai-os/projects/lsatu/`**. Code is ground truth when documentation drifts.
2. **April 2026 audit bundle `~/ai-os/archive/wiki-pre-rebuild-2026-07-16/domains/lsat-u/sources/april-2026-audit.md/`**. 14 files documenting verified bugs (F-IDs), the schema drift chain, audit corrections, persistence layer status. Entry points: `PLAYBOOK.md`, `master-reference.md`, `00-index.md`.
3. **Vault `~/ai-os/CLAUDE.md`**. Architecture rules section plus curriculum/pedagogy rules.
4. **Joshua's memory, edit #4** ("LSAT U architecture rules, never violate"). Short reminder list.

If you find a contradiction between sources, fix the lower-authority source, not the higher one.

## Tech stack (quick reference)

- **Frontend:** React 18, Vite 5, TypeScript (`strict: false`, do not rely on type safety), Tailwind 3.4, shadcn/ui, motion/react
- **Component primitives:** @base-ui/react
- **Backend:** Supabase, project ID `qodidbkoqrmqhdfwvcmk`
- **Hosting:** Lovable, auto-deploy from GitHub
- **Build:** SWC, no type checking at build time

Deeper repo and config details live in the audit bundle and the live repo itself.

## Foyer pattern (the nav surface)

Three-surface architecture:
- **Sidebar:** `FoyerSidebar.tsx`
- **Orbital ring (hero):** `radial-orbital-timeline.tsx`. Three nodes: SMART DRILL, FIND, RESUME. SVG, not Canvas.
- **Dock:** `FoyerDock.tsx`

Topic modules route from Foyer. Never add a bottom dock.

## Component library

27 components, indexed at `~/ai-os/archive/wiki-pre-rebuild-2026-07-16/domains/lsat-u/components/_INDEX.md`. Categories: primitives, forms, overlays, animation, backgrounds, marketing, chat. Pick from this library first. Custom warranted only when the existing library cannot teach the topic mechanic.

## Bug ID conventions

LSAT U bugs use F-prefix IDs (F2.13, F4.1, etc.). The April 2026 audit bundle is canonical. Reference F-IDs in any code change that fixes a known issue. See `raw/lsat-u-audit-2026-04/06-cross-scan-verification.md` for verified IDs.

## What this skill is NOT for

- Writing student-facing content. Use `lsat-u-voice` for that.
- Curriculum decisions about what to teach. Use the curriculum build pipeline.
- Source teaching material analysis. Out of scope.

## Maintenance

When canonical decisions change in the vault or repo, update this skill's always-violate list and when-in-doubt rules to match. The pointers to canonical sources stay stable. The daily-use rules drift, so they live here for fast access.
