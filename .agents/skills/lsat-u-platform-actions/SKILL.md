---
name: lsat-u-platform-actions
description: Operate LSAT U from AI OS. Assign complete interactive Classroom lessons directly through the local lsat-u-lessons MCP server, verify the saved content and student visibility headlessly, and log the assignment. Use the Node CLI for other supported actions.
---

## Current AI OS execution contract

Resolve the actual host browser/CLI before use, preserve marker-based idempotency, exact recipient/action verification and live readback. Do not replace a working transport simply because a reference names another runtime.

For drills, messages, student data, access, signups, due dates, unassign, and unsend, use `assign-lsatu-work`. On Windows, invoke its Node entry point directly instead of relying on Bash being on PATH.


# LSAT U Platform Actions

Joshua's workplace is this brain workspace. LSAT U operations should run headlessly when a supported tool exists. The browser is for checking what a person sees.

## One-call assignment route (2026-10-25)

For approved student work and notes, prefer local MCP `assign_student_work` using the authoritative AI OS `references/lsatu-work-batch.md`. One call covers the entire mixed package with live preflight, serialized app writes, exact content/date/visibility verification and a generated audit. Separate preview, per-item CLI setup and repeat readback are not routine requirements. `publish_interactive_lesson` remains a single-note compatibility entry to the same engine and lock. The older direct `lsatu-admin.mjs post-lesson` mechanism below is a legacy fallback; do not run it concurrently with unified MCP publishing. The immediate MCP client is `node system/scripts/lsatu-mcp-call.mjs assign_student_work --file <plan.json>`.

## Mechanism

For complete approved packages, call local MCP `assign_student_work`. For one note, `publish_interactive_lesson` is a compatibility adapter into that same engine and cross-process lock. Both authenticate with the existing admin identity and post notes through `mcp_post_classroom_note`, verify exact saved HTML and student visibility, then hide only older versions with the same embedded lesson marker. Repeating current content reuses the saved item without another notification. The local server is `system/scripts/lsatu-lesson-mcp.mjs`; no Lovable publish or browser is required. The direct Node admin `post-lesson` command is a legacy fallback with a different lock and must not run concurrently with the unified publisher.

The HTML must be a complete document inside AI OS, under 500 KB, with `<meta name="lsatu-interactive-lesson" content="unique-lesson-id">`. Reuse the same lesson ID for revisions of that lesson; use a different ID for a different lesson. Inline the CSS, JavaScript, fonts, and visual assets. Preflight rejects nonembedded resources; do not bypass it or paste HTML into an ordinary sanitized note. The already-live Classroom renderer loads marked HTML in a sandboxed iframe with scripts and forms enabled. **Daily lesson posting is a content operation and never requires Lovable.** Only an actual app renderer change follows the separate app deployment rules.

Routine verification is headless: the publisher reads the new item back, compares its HTML byte for byte, checks that it is visible to the intended student, and confirms one active version. The result includes its route and SHA-256. Use Codex's in-app browser only when a visual or interaction defect is suspected or the page design or renderer changed. A teacher login cannot open another student's `/classroom/item/<id>` route directly. Do not claim a student-session visual check unless one was actually performed.

The student opens the full lesson from Classroom **Notes and recaps**, the in-app notification, or its Inbox link. Classroom Home may show a recent note as a “Read” row, but it has a four-row limit shared with urgent work, so do not promise that every assigned note stays on Home. This does not affect the note's visibility in Notes and recaps or its direct item route.

## UI fallback routing

The current student verification route is `/teacher/students/<student-id>/notes`. Its “Posted to their Classroom” section shows active notes and labels archived notes as hidden from the student. Use the browser's normal controls for any unsupported action, then verify the saved state through a fresh read. In Codex, use the in-app browser, not Chrome. Do not rely on old `/teacher?ws=` routes or old browser-tool names.

**React controlled inputs (learned 2026-07-16).** Setting a field's DOM value programmatically often does not update React state, which leaves the submit button disabled and sends nothing. In the UI fallback, type with real keystrokes, pick `<select>` options with a real click or the keyboard, confirm the submit button is enabled before clicking, and afterwards confirm the mutation request returned 2xx. A screen that merely looks done is not evidence.

## Order of operations (every action)

1. **Identify the student** exactly. Reuse identity and teaching context already verified in the conversation. The unified engine checks live existing assignments; do not separately read historical ledgers just to detect duplicates. Retrieve student context only when the teaching goal is unclear, and ask only if live lookup remains ambiguous.
2. **Do the action** through MCP or the headless Node CLI when supported. Use the UI fallback only for unsupported actions.
3. **Verify it landed**: use the publisher's read-after-write result to confirm exact HTML, student visibility, and one active copy of this lesson ID. It archives earlier versions of that ID and leaves unrelated same-title notes alone. Check notifications where available. If verification fails, inspect current items before retrying; never blindly post twice.
4. **Keep the generated evidence**: the batch returns `audit_file` with exact outcomes and IDs, under the existing student folder when supplied. That is the machine delivery record. Add human context to the existing assignment ledger only when useful; do not build another proof pipeline or repeat verified reads. Legacy operations without a generated audit still need a delivery entry.

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
