import os, sqlite3, re

db_path = r"C:\Users\Joshu\.gemini\antigravity\conversations\d2f4d24d-4466-40e8-a08a-e291ce502226.db"
print(f"Checking subagent DB: {db_path}")

if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT idx, data FROM gen_metadata LIMIT 5;")
    for idx, data in cur.fetchall():
        strings = [s.decode('utf-8', errors='ignore') for s in re.findall(rb"[A-Za-z0-9_\.\-\/ :]{4,}", data)]
        print(f"Subagent Step {idx} gen_metadata:", [s for s in strings if any(k in s.lower() for k in ["gemini", "claude", "model", "flash", "pro"])])

