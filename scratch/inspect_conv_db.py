import os, sqlite3, json

conv_id = "3c03d32c-fd9f-45cb-82ce-11890d7fc349"
db_path = fr"C:\Users\Joshu\.gemini\antigravity\conversations\{conv_id}.db"

print(f"Checking {db_path}...")
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
        print(f"\nTable {t} cols:", cols)
        cur.execute(f"SELECT * FROM {t} LIMIT 3;")
        rows = cur.fetchall()
        for r in rows:
            print(f"Row in {t}:", [str(x)[:100] for x in r])
else:
    print("Database file does not exist for current conv yet, checking latest db...")
    import glob
    dbs = glob.glob(r"C:\Users\Joshu\.gemini\antigravity\conversations\*.db")
    latest = max(dbs, key=os.path.getmtime)
    print("Latest DB:", latest)
    conn = sqlite3.connect(latest)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print("Tables:", cur.fetchall())

