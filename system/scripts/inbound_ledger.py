"""
C:\\Users\\Joshu\\dev\\ai-os\\system\\scripts\\inbound_ledger.py

Engine and CLI for wiki/inbound-handled-ledger.md
Maintains high-water mark cursors, pending action queue, and append-only handled log.
"""

import os
import re
import sys
from datetime import datetime

LEDGER_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "wiki", "inbound-handled-ledger.md"))

def read_ledger():
    if not os.path.exists(LEDGER_PATH):
        raise FileNotFoundError(f"Ledger file not found at {LEDGER_PATH}")
    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        return f.read()

def write_ledger(content):
    with open(LEDGER_PATH, "w", encoding="utf-8") as f:
        f.write(content)

def parse_high_water_marks(content):
    cursors = {}
    lines = content.split("\n")
    in_section = False
    for line in lines:
        if line.startswith("## High-Water Marks"):
            in_section = True
            continue
        if in_section and line.startswith("## "):
            break
        if in_section and line.strip().startswith("|") and not line.strip().startswith("| Platform") and not line.strip().startswith("|---"):
            parts = [p.strip() for p in line.split("|")[1:-1]]
            if len(parts) >= 4:
                platform, cursor_ts, latest_id, last_checked = parts[:4]
                cursors[platform] = {
                    "cursor_timestamp": cursor_ts,
                    "latest_id": latest_id,
                    "last_checked": last_checked
                }
    return cursors

def parse_pending_queue(content):
    pending = []
    lines = content.split("\n")
    in_section = False
    for line in lines:
        if line.startswith("## Pending Action Queue"):
            in_section = True
            continue
        if in_section and line.startswith("## "):
            break
        if in_section and line.strip().startswith("|") and not line.strip().startswith("| Received") and not line.strip().startswith("|---"):
            parts = [p.strip() for p in line.split("|")[1:-1]]
            if len(parts) >= 6:
                received_at, platform, sender, msg_id, snippet, status = parts[:6]
                pending.append({
                    "received_at": received_at,
                    "platform": platform,
                    "sender": sender,
                    "message_id": msg_id,
                    "snippet": snippet,
                    "status": status
                })
    return pending

def parse_handled_ledger(content):
    handled = []
    lines = content.split("\n")
    in_section = False
    for line in lines:
        if line.startswith("## Handled Ledger"):
            in_section = True
            continue
        if in_section and line.startswith("## "):
            break
        if in_section and line.strip().startswith("|") and not line.strip().startswith("| Handled") and not line.strip().startswith("|---"):
            parts = [p.strip() for p in line.split("|")[1:-1]]
            if len(parts) >= 6:
                handled_at, platform, sender, inbound_at, msg_id, action_note = parts[:6]
                handled.append({
                    "handled_at": handled_at,
                    "platform": platform,
                    "sender": sender,
                    "inbound_at": inbound_at,
                    "message_id": msg_id,
                    "action_note": action_note
                })
    return handled

def advance_cursor(platform, cursor_timestamp, latest_id):
    content = read_ledger()
    lines = content.split("\n")
    new_lines = []
    in_section = False
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    updated = False

    for line in lines:
        if line.startswith("## High-Water Marks"):
            in_section = True
            new_lines.append(line)
            continue
        if in_section and line.startswith("## "):
            in_section = False
            new_lines.append(line)
            continue
        if in_section and line.strip().startswith("|") and not line.strip().startswith("| Platform") and not line.strip().startswith("|---"):
            parts = [p.strip() for p in line.split("|")[1:-1]]
            if len(parts) >= 4 and parts[0].lower() == platform.lower():
                new_line = f"| {parts[0]} | {cursor_timestamp} | {latest_id} | {now_str} |"
                new_lines.append(new_line)
                updated = True
                continue
        new_lines.append(line)

    if not updated and in_section:
        new_lines.append(f"| {platform} | {cursor_timestamp} | {latest_id} | {now_str} |")

    write_ledger("\n".join(new_lines))
    print(f"Advanced cursor for {platform} to {cursor_timestamp} ({latest_id})")

def add_pending(received_at, platform, sender, msg_id, snippet):
    content = read_ledger()
    lines = content.split("\n")
    new_lines = []
    in_section = False
    added = False

    for line in lines:
        if line.startswith("## Pending Action Queue"):
            in_section = True
            new_lines.append(line)
            continue
        if in_section and line.startswith("## "):
            if not added:
                new_lines.append(f"| {received_at} | {platform} | {sender} | {msg_id} | {snippet} | pending |")
                added = True
            in_section = False
            new_lines.append(line)
            continue
        new_lines.append(line)

    if in_section and not added:
        new_lines.append(f"| {received_at} | {platform} | {sender} | {msg_id} | {snippet} | pending |")

    write_ledger("\n".join(new_lines))
    print(f"Added pending item for {platform} from {sender} ({msg_id})")

def mark_handled(platform, msg_id_or_sender, action_note):
    content = read_ledger()
    pending = parse_pending_queue(content)
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    target_item = None
    remaining_pending = []
    for item in pending:
        if item["platform"].lower() == platform.lower() and (
            item["message_id"].lower() == msg_id_or_sender.lower() or 
            item["sender"].lower() == msg_id_or_sender.lower()
        ):
            target_item = item
        else:
            remaining_pending.append(item)

    lines = content.split("\n")
    new_lines = []
    section = None

    for line in lines:
        if line.startswith("## High-Water Marks"):
            section = "hw"
            new_lines.append(line)
            continue
        elif line.startswith("## Pending Action Queue"):
            section = "pending"
            new_lines.append(line)
            continue
        elif line.startswith("## Handled Ledger"):
            section = "handled"
            new_lines.append(line)
            continue
        elif line.startswith("## "):
            section = None
            new_lines.append(line)
            continue

        if section == "pending":
            if line.strip().startswith("| Platform") or line.strip().startswith("| Received") or line.strip().startswith("|---"):
                new_lines.append(line)
            elif line.strip().startswith("|"):
                parts = [p.strip() for p in line.split("|")[1:-1]]
                if len(parts) >= 6:
                    item_plat, item_msg, item_snd = parts[1], parts[3], parts[2]
                    if item_plat.lower() == platform.lower() and (
                        item_msg.lower() == msg_id_or_sender.lower() or 
                        item_snd.lower() == msg_id_or_sender.lower()
                    ):
                        continue
                new_lines.append(line)
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)

    if target_item:
        sender = target_item["sender"]
        inbound_at = target_item["received_at"]
        msg_id = target_item["message_id"]
    else:
        sender = msg_id_or_sender
        inbound_at = now_str
        msg_id = msg_id_or_sender

    handled_entry = f"| {now_str} | {platform} | {sender} | {inbound_at} | {msg_id} | {action_note} |"
    new_lines.append(handled_entry)

    write_ledger("\n".join(new_lines))
    print(f"Marked handled: {platform} - {sender} ({msg_id}): {action_note}")

def print_status():
    content = read_ledger()
    cursors = parse_high_water_marks(content)
    pending = parse_pending_queue(content)
    handled = parse_handled_ledger(content)

    print("=== HIGH-WATER MARKS ===")
    for p, data in cursors.items():
        print(f"  {p.upper()}: Cursor={data['cursor_timestamp']} | Latest ID={data['latest_id']} | Checked={data['last_checked']}")

    print(f"\n=== PENDING ACTION QUEUE ({len(pending)} open) ===")
    for item in pending:
        print(f"  [{item['platform'].upper()}] {item['received_at']} | Sender: {item['sender']} | Ref: {item['message_id']}")
        print(f"    Snippet: {item['snippet']}")

    print(f"\n=== RECENT HANDLED LEDGER (Last 5 of {len(handled)}) ===")
    for item in handled[-5:]:
        print(f"  [{item['platform'].upper()}] Handled: {item['handled_at']} | Sender: {item['sender']} | Ref: {item['message_id']}")
        print(f"    Action: {item['action_note']}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_status()
        sys.exit(0)

    cmd = sys.argv[1].lower()
    if cmd == "status":
        print_status()
    elif cmd == "advance" and len(sys.argv) >= 5:
        advance_cursor(sys.argv[2], sys.argv[3], sys.argv[4])
    elif cmd == "add-pending" and len(sys.argv) >= 7:
        add_pending(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    elif cmd == "mark-handled" and len(sys.argv) >= 5:
        mark_handled(sys.argv[2], sys.argv[3], " ".join(sys.argv[4:]))
    else:
        print("Usage: inbound_ledger.py [status | advance <platform> <ts> <id> | add-pending <ts> <platform> <sender> <id> <snippet> | mark-handled <platform> <id> <note>]")
