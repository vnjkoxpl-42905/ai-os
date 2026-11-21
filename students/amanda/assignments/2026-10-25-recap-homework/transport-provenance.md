# Isolated Amanda assignment transport

Created 2026-10-25 because the shared operational checkout contained three tracked hook-file edits belonging to other work. Those files were neither changed nor restored.

- Isolated checkout: `C:/Users/Joshu/dev/ai-os-projects/.lsatu-ops-amanda-20261025`.
- Freshly fetched `origin/main`, detached commit: `6a167c8555b4a404334310aad48a5d748b1b0861`.
- Dependencies are a junction to the existing application's `node_modules`, outside the vault.
- Ordinary activity/bootcamp execution uses the existing `system/scripts/prepare-assign.mjs`, which generates the existing app `scripts/assign.ts` with its vault credential pointer. The generated runner calls the app's own `assignWork()`.
- Guided execution copies `system/scripts/lsatu-guided-plan.ts` unchanged except its existing single vault-root placeholder. The runner handles live content/pool checks, assignment and readback through existing app functions. No alternate database writer was created.
- `transport.mjs` checks the pinned commit and tracked cleanliness before every call, refuses multiline arguments, sets `TZ=America/Toronto`, captures dated preview/assignment evidence, and checks tracked cleanliness afterwards.
- The known Vite plugin rewrites `supabase/functions/mcp/index.ts`. Cleanup accepts only that one changed path with exactly the expected eight-line generated entry referencing this isolated checkout, then restores that generated path. Any unexpected content is preserved and execution fails.

The initial Unless dry-run reached the correct identity/date but the first cleanup guard was narrower than the plugin's actual behavior: the committed entry is a full bundle and Vite replaces it with a local eight-line import entry. Cleanup stopped safely. The actual diff was inspected, the guard was changed to exact expected generated content, and only the isolated plugin file was restored. A subsequent recorded Unless preview passed. No student writes occurred during these previews.

Recorded results:

- Unless dry-run: correct Amanda account, due 2026-11-01, no write.
- General Conditionals exact-title dry-run: no matching Activity. This requires its actual live title/slug before execution.
- Follow-up exact-slug dry-run passed for `conditional-rephrase`, live title `Conditional Rephrase`, correct Amanda account and due 2026-11-01. Root independently read its live ID `7946f46b-e7f8-4c60-b405-4ece9c409deb`; this matches `GENERAL_ID` in `src/features/activity-centre/conditionals/ConditionalPractice.tsx`, which opens it as General Conditionals. The title-only mismatch is resolved without creating content.
- Guided dry-run: Amanda `18319b53-3489-4e01-92aa-f04ade88858e`; MBT six questions at difficulty 1–3; Parallel Flaw five questions at difficulty 2–3; schedule 2026-10-25, due 2026-11-01; both would assign; zero assignments made.

This is headless preflight evidence, not student-browser acceptance or email receipt verification.
