---
name: inbound-message-triage
description: Cross-platform inbound message triage and state tracking. Pulls messages from LSAT U, Reddit, 7Sage, and Facebook, compares against high-water marks and the handled ledger, queues pending action items, and logs handled messages so they are never revisited.
---

# Inbound Message Triage & Handled Ledger

This skill tracks and triages all incoming messages across Joshua's communication channels:
1. **LSAT U** (Teacher Desk Inbox on lsatprep.study via port 9223)
2. **Reddit** (Reddit Chat & Inbox via port 9224)
3. **7Sage** (7Sage LSAT platform via port 9225)
4. **Facebook** (Messenger inbox via port 9226)

The ground truth of what has been seen and handled is maintained in [inbound-handled-ledger.md](file:///c:/Users/Joshu/dev/ai-os/wiki/inbound-handled-ledger.md).

## Core Principles

- **Never repeat handled messages**: Once a message is marked handled in the ledger, future triage runs ignore it.
- **High-Water Marks**: Each platform maintains a cursor timestamp and latest message ID. Pulls only surface items newer than the cursor.
- **Pending Action Queue**: Inbound inquiries needing action remain in Pending until Joshua confirms they are dealt with.
- **Append-Only Handled Log**: Every resolution is logged with timestamp, platform, sender, inbound timestamp, reference ID, and action taken.

## Ledger Engine CLI

Run the ledger script from the repo root:

### 1. Check Current Status
```powershell
python system/scripts/inbound_ledger.py status
```
Displays:
- Platform cursors (high-water marks)
- Open pending action items
- Recent handled items

### 2. Mark a Message as Handled
```powershell
python system/scripts/inbound_ledger.py mark-handled <platform> <sender_or_id> "<action note>"
```
Examples:
```powershell
python system/scripts/inbound_ledger.py mark-handled lsatu Zeina "Answered question regarding rebuttals/premises"
python system/scripts/inbound_ledger.py mark-handled reddit ConstantPlenty7292 "Sent consultation booking link"
```
This automatically:
- Removes the item from `Pending Action Queue`
- Appends the resolution to `Handled Ledger` with current timestamp

### 3. Advance High-Water Mark Cursor
```powershell
python system/scripts/inbound_ledger.py advance <platform> <iso_timestamp> <latest_message_id>
```
Example:
```powershell
python system/scripts/inbound_ledger.py advance lsatu 2026-09-20T12:00:00Z msg-ivory-20260920
```

### 4. Add an Item to Pending Queue
```powershell
python system/scripts/inbound_ledger.py add-pending <iso_timestamp> <platform> <sender> <message_id> "<snippet>"
```

## Pull & Ingest Commands by Platform

| Platform | Extraction Script | Browser Port |
| :--- | :--- | :--- |
| **LSAT U** | `node C:\Users\Joshu\Tools\LSATU-Agent\pull_platform_messages.mjs` | 9223 |
| **Reddit** | `node C:\Users\Joshu\Tools\Reddit-Agent\pull_reddit_messages.mjs` | 9224 |
| **7Sage** | `node C:\Users\Joshu\Tools\7Sage-Agent\pull_7sage_messages.mjs` | 9225 |
| **Facebook** | `node C:\Users\Joshu\Tools\Facebook-Agent\pull_facebook_messages.mjs` | 9226 |

## Standard Workflow

1. **Pull**: Execute the platform extraction script or run status.
2. **Filter**: Compare retrieved items against `wiki/inbound-handled-ledger.md`.
   - Skip any item already present in the `Handled Ledger`.
   - Skip any item with timestamp at or before the platform's `High-Water Mark`.
3. **Present**: Show only actionable or unhandled messages to Joshua.
4. **Action**:
   - Draft response (e.g. using `inbound-tutoring-replies` for leads).
   - If Joshua confirms sent / dealt with, immediately run `mark-handled`.
   - Advance the platform cursor.
