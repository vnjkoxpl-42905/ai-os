---
type: source
subject: ChatGPT-era project memory for post-consultation follow-up emails, dated 2026-07-07
created: 2026-10-14
updated: 2026-10-14
aliases: [Post-Consultation Follow-Up Workflow Memory, post_consultation_follow_up_workflow_memory, consultation follow-up workflow memory]
tags: [consultations, email, workflow, superseded]
evidence: "../../raw/sources/consultation-followup-workflow-memory-2026-07-07/post_consultation_follow_up_workflow_memory (1) (1).md"
sha256: 63d28b1734687a40e4703950e86523195df4cd1bf2d03d2a0e1ce8b06803d852
sources: [../../raw/sources/consultation-followup-workflow-memory-2026-07-07/PROVENANCE.md]
contradictions: []
---

# The July consultation follow-up memory: mostly superseded, two checks still worth keeping

"Post-Consultation Follow-Up Workflow Memory" is a Markdown note written as project memory for ChatGPT sessions, last updated 2026-07-07 by its own header. Author unknown (it addresses "the assistant"). The file was found loose in `raw/` (modified 2026-09-06) and read in full on 2026-10-14.

Evidence: [archived document, provenance and hashes](../../raw/sources/consultation-followup-workflow-memory-2026-07-07/PROVENANCE.md). SHA-256 `63d28b1734687a40e4703950e86523195df4cd1bf2d03d2a0e1ce8b06803d852`.

## What the note says

- **Template first.** Use the saved post-consultation template every time, add only one or two personalized lines, never rewrite from scratch.
- **Personalization source.** Gemini notes or the transcript, not the email thread. Focus on goal score, scholarship or law school goal, test date or timeline; avoid the diagnostic or current score unless clearly needed. Weak notes mean minimal personalization, not a question to Joshua.
- **Required links.** Session booking link, the relevant payment or package link, and the platform signup link. Never invent a payment link.
- **Readiness gate, three checks in order.** The calendar end time has passed (Eastern time); Gemini notes exist; no follow-up was already sent. If the first check fails, stop for that student without searching notes.
- **Timing and sending.** Schedule for 3:00 PM Eastern the day after the consultation and send automatically unless Joshua says not to.
- **Point-in-time context.** It records a July pre-consultation reminder week (Favour sent, Yahunathan removed, others named). That is stale operational state; Gmail and the calendar own it.

## How it compares with the current workflow

Checked 2026-10-14 against [the follow-up template](../CONSULTATION-FOLLOW-UP-TEMPLATE.md), the `consultation-followup-drafts` skill (`skills/claude/consultation-followup-drafts/SKILL.md`, identical to the loaded home copy) and [the decision log](../../decisions/log.md).

| Note's rule | Current state | Outcome |
|---|---|---|
| One or two personalized lines | Template (rebuilt 2026-09-11 from five real sends): "Do not add a personalized recap sentence." | Superseded by later evidence |
| Auto-send next day 3:00 PM Eastern | Skill and template: draft only, Joshua sends. Root rules: send only on "send" (changed 2026-09-11). But decision log 2026-07-20 still locks a scheduled 3:00 PM Toronto auto-send. | Superseded in practice; decision log not reconciled (queued as AQ-009) |
| Booking, package and signup links | Template carries Cal.com, both Stripe packages and `https://lsatprep.study` | Already here |
| End time passed, notes exist, no prior follow-up | Skill steps 2 and 4 | Already here |
| Stop before reading notes when the end time has not passed | Skill filters past events first | Already here |
| Never invent a payment link | Decision log 2026-07-20 requires validating price-to-link mapping and failing closed; the skill has no explicit link check before drafting | Gap, folded into AQ-009 |
| Avoid the diagnostic score | Moot: the template has no personalized line | Skip |

The note's real value now is historical: it shows where the one-or-two-line personalization and the auto-send rule came from before the 2026-09-11 rebuild moved to a fixed, draft-only template.

## Mentions in source

> "Add only 1 to 2 personalized lines based on the transcript." (Assistant Role)

> "Do not invent payment links." (Required Links)

> "If check 1 fails, stop immediately." (Readiness Verification Rule)

## Related pages

- [Consultation follow-up email template](../CONSULTATION-FOLLOW-UP-TEMPLATE.md)
- [Teaching voice](../teaching-voice.md)
- [Send ledger](../send-ledger.md)
- [AI action queue](../../references/ai-workspace/action-queue.md), item AQ-009


## Queue record

Partial 2026-10-26: AQ-009. Draft-only rule reconciled and local standard/higher checker positive/negative tests pass; Cal.com GET returned HTTP200. Remaining: verify the unusual $60 Stripe link identity and amount with Stripe authority. No sends/payments. [Implementation record](../../research/2026-10-26-source-implementation/REPORT.md).
