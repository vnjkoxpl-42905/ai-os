---
name: lsat-u-platform-actions
description: Operate LSAT U from AI OS. Assign complete interactive Classroom lessons directly through the local lsat-u-lessons MCP server, verify the saved content and student visibility headlessly, and log the assignment. Use the Node CLI for other supported actions.
---

## Current AI OS execution contract

Resolve the actual host browser/CLI before use, preserve marker-based idempotency, exact recipient/action verification and live readback. Do not replace a working transport simply because a reference names another runtime.

For drills, messages, student data, access, signups, due dates, unassign, and unsend, use `assign-lsatu-work`. On Windows, invoke its Node entry point directly instead of relying on Bash being on PATH.


# LSAT U Platform Actions

Joshua's workplace is this brain workspace. LSAT U operations should run headlessly when a supported tool exists. The browser is for checking what a person sees.

## Mechanism

For an interactive HTML lesson, call the `lsat-u-lessons` MCP tool `publish_interactive_lesson` with the student's exact email, absolute HTML path, and title. The local stdio server is `system/scripts/lsatu-lesson-mcp.mjs`; Codex registration is `lsat-u-lessons`. It calls `system/scripts/lsatu-admin.mjs post-lesson`, which authenticates with the existing admin credentials, posts through `mcp_post_classroom_note`, verifies the saved HTML exactly and student visibility, and then archives only earlier versions with the same lesson marker. A repeat of the current version returns the same item without another notification. Use `dry_run: true` when the student or replacement is uncertain; otherwise publish in one call. MCP tools newly registered during a session may only appear in a new Codex session; the direct Node command is the immediate fallback.

The HTML must be a complete document inside AI OS, under 500 KB, with `<meta name="lsatu-interactive-lesson" content="unique-lesson-id">`. Reuse the same lesson ID for revisions of that lesson; use a different ID for a different lesson. Inline the CSS, JavaScript, fonts, and visual assets. Preflight rejects nonembedded resources; do not bypass it or paste HTML into an ordinary sanitized note. The already-live Classroom renderer loads marked HTML in a sandboxed iframe with scripts and forms enabled. **Daily lesson posting is a content operation and never requires Lovable.** Only an actual app renderer change follows the separate app deployment rules.

Routine verification is headless: the publisher reads the new item back, compares its HTML byte for byte, checks that it is visible to the intended student, and confirms one active version. The result includes its route and SHA-256. Use Codex's in-app browser only when a visual or interaction defect is suspected or the page design or renderer changed. A teacher login cannot open another student's `/classroom/item/<id>` route directly. Do not claim a student-session visual check unless one was actually performed.

The student opens the full lesson from Classroom **Notes and recaps**, the in-app notification, or its Inbox link. Classroom Home may show a recent note as a “Read” row, but it has a four-row limit shared with urgent work, so do not promise that every assigned note stays on Home. This does not affect the note's visibility in Notes and recaps or its direct item route.

## UI fallback routing

The current student verification route is `/teacher/students/<student-id>/notes`. Its “Posted to their Classroom” section shows active notes and labels archived notes as hidden from the student. Use the browser's normal controls for any unsupported action, then verify the saved state through a fresh read. In Codex, use the in-app browser, not Chrome. Do not rely on old `/teacher?ws=` routes or old browser-tool names.

**React controlled inputs (learned 2026-07-16).** Setting a field's DOM value programmatically often does not update React state, which leaves the submit button disabled and sends nothing. In the UI fallback, type with real keystrokes, pick `<select>` options with a real click or the keyboard, confirm the submit button is enabled before clicking, and afterwards confirm the mutation request returned 2xx. A screen that merely looks done is not evidence.

## Order of operations (every action)

1. **Identify the student** exactly (roster names include email; ambiguity → one
   concise clarifying question). Check `students/<name>/` for context and
   `assignment-log.md` to avoid repeats.
2. **Do the action** through MCP or the headless Node CLI when supported. Use the UI fallback only for unsupported actions.
3. **Verify it landed**: use the publisher's read-after-write result to confirm exact HTML, student visibility, and one active copy of this lesson ID. It archives earlier versions of that ID and leaves unrelated same-title notes alone. Check notifications where available. If verification fails, inspect current items before retrying; never blindly post twice.
4. **Log it**: append to `students/<name>/assignment-log.md` (create if missing) with
   date, action, item, and evidence; drill verifications also go to
   `wiki/guided-drill-verification-log.md`.

## Guardrails

- Every action here hits **real students on prod**. Anything a student will see
  (message text, homework instructions, note bodies) is written in Joshua's voice —
  route through `wiki/teaching-voice.md`.
- If Joshua's request fully specifies the action ("assign Lydia the conditional
  drill"), execute without re-asking. If content is open-ended (a message body he
  hasn't dictated), draft it and show him before sending.
- Fail closed: if verification is ambiguous, say exactly what was and wasn't
  confirmed. Never report an action complete on the strength of a click alone.
- No student-facing action as a side effect of a different request.

## Paid session credits

Use `node system/scripts/lsatu-admin.mjs passes <exact-email>` for balances and `pass-detail` for evidence. An exhausted pass can be replaced with `pass-create <exact-email> --credits N --minutes 70`; dry-run first, then verify through a fresh read. Preserve exhausted passes.

Before manually restoring a Stripe package, inspect its `stripe_payments` row and the webhook delivery response. The 2026-09-27 policy returned `grant: awaiting_teacher` for intentional teacher approval. On 2026-10-02, Joshua approved and deployed automatic crediting for new validated, confidently matched package Checkouts, including delayed successes. Existing rows default `auto_grant_eligible=false`; historical, dismissed, and granted payments are not automatically recredited. Unmatched payments stay in review. Verify the live row and deployment before diagnosing a bug; an empty `booking_commerce_events` read is not proof of no payment. Evidence: `research/2026-10-02-celia-payment-crediting.md`.

Associate any manual restoration with its exact Stripe payment/event in the booking pass notes. Reconcile the pending teacher grant prompt without adding more credits, using the supported payment-ledger operation after checking its semantics. Do not replay the webhook or invoke `admin_grant_stripe_payment` after manual crediting; either can duplicate sessions. A dismissed payment is not marked granted, and future reconciliation must skip it or explicitly honor the manual fulfillment.
