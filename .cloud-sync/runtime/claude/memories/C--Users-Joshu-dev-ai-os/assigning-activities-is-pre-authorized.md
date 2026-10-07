---
name: assigning-activities-is-pre-authorized
description: "Joshua pre-authorized assigning LSAT U Activities to a named student — do it immediately, don't ask; the runbook is wiki/ASSIGN-AN-ACTIVITY.md."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 43bf46d8-919d-4b40-a519-e973f038281d
  modified: 2026-09-08T00:12:11.579Z
---

When Joshua says "assign <activity> to <student>", carry it out end to end and
report after. Do not stop to ask permission.

Follow `wiki/ASSIGN-AN-ACTIVITY.md` (the path, the nine Activities, what
`assignWork()` fires) and `wiki/STUDENT-PLATFORM-IDENTITY-MAP.md` (which platform
account is which student). Granted 2026-09-07.

**Why:** assignment is the core loop of the tutoring business — roughly 25
sessions a week, each generating homework. Confirming every assignment made the
capability useless to him. This is a deliberate, narrow exception to his global
"draft, never send" rule, which still holds for email, posts, and messages.

**How to apply:** a single named student is a go. Still confirm first when
assigning to 3+ students at once (each one emails a real person), when the name
is ambiguous — above all **Steven Morris vs "Stevie"**, possibly one person with
two accounts — or when the student is unresolved (**Thaniuska Vivas** has no
platform account, **Amanda** has none found) or absent from the identity map.

Use the **`assign-lsatu-work` skill** — headless, no browser. From
`projects/lsatu`: `npx vite-node scripts/assign.ts -- --student "Celia"
--activity "Read, Recall, Colour"` (also `--drill`, `--message`, `--schedule`,
`--dry-run`). It calls the app's own `assignWork()`, so it can never drift from
what the UI does. Credentials live in `~/ai-os/.env`; never in
`projects/lsatu/.env`, which is tracked in git.

The browser path still works as a fallback: `/activities` → the card's
"Assign <name>" button → tick the student → "Assign to N students". That dialog
is a portal outside `<main>`, so `read_page` sees it and `get_page_text` does not.

See also [[ai-os-safety-rules]], [[ai-os-vault-location]].
