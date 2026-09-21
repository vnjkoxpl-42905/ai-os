import os, json, sqlite3, glob

print("=== Checking current conversation model info ===")
brain_dir = r"C:\Users\Joshu\.gemini\antigravity\brain"
conv_id = "3c03d32c-fd9f-45cb-82ce-11890d7fc349"
current_brain = os.path.join(brain_dir, conv_id)

# Check transcript metadata or header
t_path = os.path.join(current_brain, ".system_generated", "logs", "transcript.jsonl")
if os.path.exists(t_path):
    with open(t_path, "r", encoding="utf-8") as f:
        first_lines = [f.readline() for _ in range(5)]
        for line in first_lines:
            try:
                data = json.loads(line)
                print("Transcript event type:", data.get("type"), "source:", data.get("source"))
                if "model" in line.lower():
                    print("Found model in line:", line[:300])
            except:
                pass

print("\n=== Checking conversation_summaries.db ===")
db_path = r"C:\Users\Joshu\.gemini\antigravity\conversation_summaries.db"
if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()
    print("Tables:", tables)
    for table_name in tables:
        t = table_name[0]
        cur.execute(f"PRAGMA table_info({t});")
        cols = [c[1] for c in cur.fetchall()]
        print(f"Table {t} cols:", cols)
        cur.execute(f"SELECT * FROM {t} ORDER BY rowid DESC LIMIT 3;")
        rows = cur.fetchall()
        for r in rows:
            print(f"Row in {t}:", r)

