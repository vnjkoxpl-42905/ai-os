import json

with open(r'C:\Users\Joshu\Tools\Reddit-Agent\raw_10_conversations.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for user, raw in data.items():
    # In each thread, the right pane starts after the sidebar threads
    # Let's find where the chat with `user` actually starts
    print(f"\n############################# {user} #############################")
    lines = raw.split('\n')
    # Print lines that look like actual chat messages
    chat_lines = []
    capture = False
    for line in lines:
        l = line.strip()
        if not l:
            continue
        if l == user:
            capture = True
        if capture:
            if any(x in l for x in ["Skip to", "window.", "SML.", ".snoo-", "Mark all", "Create new", "Filter chat", "Group chats", "Direct chats", "Mod mail", "Unread", "Apply"]):
                continue
            chat_lines.append(l)
    
    # Print the last 20 lines
    for cl in chat_lines[-20:]:
        try:
            print(cl.encode('ascii', errors='replace').decode('ascii'))
        except Exception:
            pass
