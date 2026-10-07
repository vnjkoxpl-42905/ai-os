import json
import os

with open(r'C:\Users\Joshu\Tools\Reddit-Agent\raw_10_conversations.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total conversations: {len(data)}")

parsed = {}
for user, raw in data.items():
    lines = [l.strip() for l in raw.split('\n') if l.strip()]
    
    # Find messages after "Threads"
    cleaned_lines = []
    skip = True
    for line in lines:
        if line == "Threads":
            skip = False
            continue
        if skip:
            continue
        # Skip UI junk
        if any(x in line for x in ["Skip to", "window.", "SML.", ".snoo-", "Mark all", "Create new", "Filter chat", "Group chats", "Direct chats", "Mod mail", "Unread", "Apply", "Send media", "Send an emoji", "Send a GIF", "Send message", "if(window."]):
            continue
        cleaned_lines.append(line)
    
    parsed[user] = cleaned_lines

with open(r'C:\Users\Joshu\Tools\Reddit-Agent\cleaned_10_conversations.json', 'w', encoding='utf-8') as f:
    json.dump(parsed, f, indent=2)

for u, msgs in parsed.items():
    print(f"\n==================== {u} ====================")
    for m in msgs[:25]:
        print(f"  {m}")
