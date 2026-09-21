---
name: inbound-message-triage
description: Multi-platform message triage across LSAT U, Reddit, 7Sage, and Facebook using the stateful high-water mark ledger.
---

# Inbound Message Triage

## Overview
Coordinates message scanning across all four active communication channels:
- LSAT U (`https://lsatprep.study`)
- Reddit (`https://reddit.com`)
- 7Sage (`https://7sage.com`)
- Facebook Messenger (`https://facebook.com/messages`)

It enforces the stateful ledger at `wiki/inbound-handled-ledger.md`:
- High-water mark cursors prevent duplicate reading of already-handled messages.
- Scans only pull forward from the last checkpoint.
- Unresolved items remain in the Pending Queue until Joshua marks them handled.

## Commands

### 1. Check Triage & Ledger Status
Displays current platform cursors, active pending items, and recent handled messages:
```bash
python C:\Users\Joshu\dev\ai-os\system\scripts\inbound_ledger.py status
```

### 2. Mark Item Handled
Moves an item to the Handled Ledger with resolution details and advances cursor:
```bash
python C:\Users\Joshu\dev\ai-os\system\scripts\inbound_ledger.py mark-handled <platform> <message_id_or_sender> "<resolution note>"
```

### 3. Add Pending Item
Adds a message to the active pending queue:
```bash
python C:\Users\Joshu\dev\ai-os\system\scripts\inbound_ledger.py add-pending "<timestamp>" "<platform>" "<sender>" "<message_id>" "<snippet>"
```
