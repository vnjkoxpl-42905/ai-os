---
name: ai-os-safety-rules
description: Delete stays blocked at the tool layer; email sends happen only when Joshua says "send" in chat (rule changed 2026-09-11), never on Claude's initiative.
metadata:
  type: feedback
---

Deleting (Gmail trash/delete, Drive delete) stays denied in the tool layer and in `CLAUDE.md`. Sending changed on 2026-09-11: draft by default, and when Joshua says "send it" in chat, send it and log it in `wiki/send-ledger.md`. The first send under the new rule was the Sandra booking reply (`gws gmail users drafts send` works; the deny list does not block it).

**Why:** He wanted "send" to mean send, without a second confirmation round. The old "draft, never send" line made me hedge after he had already said the word.
**How to apply:** A request to draft is never a request to send. Sending needs the word from him, in chat, for that specific email. One standing exception, granted 2026-09-11: the fixed "Consultation check-in" email sent 30 minutes before a Cal.com consultation by the `pre-consultation-check-in` skill goes out with no per-send approval (see [[pre-consult-check-in-is-auto-send]]). Deleting still needs the deny list narrowed, never removed. Related: [[ai-os-vault-location]], [[email-apology-shape]]
