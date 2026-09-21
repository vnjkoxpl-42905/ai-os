---
title: Inbound handled ledger
type: operating-layer
record_kind: primary
tags: [operating-layer, correspondence, triage]
created: 2026-09-21
status: active
subject: Inbound handled ledger
updated: 2026-09-21
aliases: []
---

# Inbound handled ledger

Append-only and stateful record of inbound messages, questions, and inquiries across platforms (LSAT U, Reddit, 7Sage, Facebook).

It answers: **"has this message been handled yet?"** and provides the high-water mark cursors so future triage runs only pull forward from the last checkpoint.

## Rules

- **Append only for handled items.** Once marked handled, a message never gets re-triaged.
- **High-water mark cursors.** Each platform tracks the latest timestamp and message ID processed. Future scans only pull forward from that point.
- **Pending retention.** Any message that is not resolved stays in the Pending Queue until Joshua confirms it is handled.
- **Single truth across platforms.** Reddit, LSAT U, 7Sage, and Facebook report into this ledger.

## High-Water Marks

| Platform | Cursor Timestamp | Latest Message / Thread ID | Last Checked |
|---|---|---|---|
| lsatu | 2026-09-19T20:54:33Z | msg-zeina-20260919 | 2026-09-21 03:30 |
| reddit | 2026-09-21T03:00:00Z | ConstantPlenty7292 | 2026-09-21 03:00 |
| 7sage | 1970-01-01T00:00:00Z | initial | 2026-09-21 00:00 |
| facebook | 1970-01-01T00:00:00Z | initial | 2026-09-21 00:00 |

## Pending Action Queue

| Received At | Platform | Sender | Message ID / Ref | Snippet / Context | Status |
|---|---|---|---|---|---|
| 2026-09-21 02:45 | reddit | ConstantPlenty7292 | chat-thread-ConstantPlenty7292 | Wants to meet over zoom or FaceTime for LSAT prep inquiry | pending |

## Handled Ledger

| Handled At | Platform | Sender | Inbound At | Message ID / Ref | Action Taken / Note |
|---|---|---|---|---|---|
| 2026-09-21 03:30 | lsatu | Zeina | 2026-09-19 16:54 | msg-zeina-20260919 | Marked handled per Joshua instruction (previous batch considered read) |
| 2026-09-21 03:30 | lsatu | Celia | 2026-09-19 15:16 | msg-celia-20260919b | Marked handled per Joshua instruction |
| 2026-09-21 03:30 | lsatu | Celia | 2026-09-19 14:49 | msg-celia-20260919a | Marked handled per Joshua instruction |
