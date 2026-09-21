import os, sqlite3, json

# 1. Inspect conversation_summaries.db for distinct workspace_uris and project_ids
db_path = r"C:\Users\Joshu\.gemini\antigravity\conversation_summaries.db"
if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT project_id, workspace_uris FROM conversation_summaries;")
    print("=== Distinct projects and workspace_uris in conversation_summaries ===")
    for row in cur.fetchall():
        print(" ", row)

# 2. Check state.vscdb for sidebarWorkspaces or project registrations
vscdb = r"C:\Users\Joshu\AppData\Roaming\Antigravity IDE\User\globalStorage\state.vscdb"
if os.path.exists(vscdb):
    conn = sqlite3.connect(vscdb)
    cur = conn.cursor()
    cur.execute("SELECT key, value FROM ItemTable WHERE key LIKE '%workspace%' OR key LIKE '%project%';")
    print("\n=== Workspace/Project keys in state.vscdb ===")
    for k, v in cur.fetchall():
        val = str(v)[:200]
        print(f"  {k}: {val}")

# 3. Check workspaceStorage folders in Antigravity IDE
ws_storage = r"C:\Users\Joshu\AppData\Roaming\Antigravity IDE\User\workspaceStorage"
if os.path.exists(ws_storage):
    print("\n=== workspaceStorage folders ===")
    for item in os.listdir(ws_storage):
        sub = os.path.join(ws_storage, item)
        meta = os.path.join(sub, "workspace.json")
        if os.path.exists(meta):
            with open(meta, "r", encoding="utf-8") as f:
                print(f"  {item}: {f.read().strip()}")

