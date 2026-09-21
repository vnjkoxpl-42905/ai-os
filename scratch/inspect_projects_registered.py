import os
import glob
import json
import sqlite3

p_dir = r"C:\Users\Joshu\.gemini\config\projects"
print(f"=== Files in {p_dir} ===")
for f in glob.glob(os.path.join(p_dir, "*")):
    print(f"- {os.path.basename(f)} ({os.path.getsize(f)} B):")
    try:
        with open(f, 'r', encoding='utf-8') as fh:
            data = json.load(fh)
            print("  ", json.dumps(data, indent=2))
    except Exception as e:
        print("   Error reading json:", e)

db_p = r"C:\Users\Joshu\.gemini\antigravity\databases\conversation_summaries.db"
print(f"\n=== Projects in {db_p} ===")
if os.path.exists(db_p):
    conn = sqlite3.connect(db_p)
    cur = conn.cursor()
    cur.execute("SELECT id, name, root_path FROM projects")
    for row in cur.fetchall():
        print("  Project row:", row)
    conn.close()
