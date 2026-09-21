import os, sqlite3, json, glob

storage_dir = r"C:\Users\Joshu\AppData\Roaming\Antigravity IDE\User\globalStorage"
print("Checking globalStorage...")

dbs = glob.glob(os.path.join(storage_dir, "**", "*.vscdb"), recursive=True)
print(f"Found {len(dbs)} vscdb files:")
for db in dbs:
    print(" ", db, f"({os.path.getsize(db)} bytes)")

for db in dbs:
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute("SELECT key, value FROM ItemTable WHERE key LIKE '%model%' OR key LIKE '%antigravity%' OR key LIKE '%cascade%';")
        rows = cur.fetchall()
        print(f"\nMatches in {os.path.basename(db)} ({len(rows)} matches):")
        for k, v in rows:
            print(f"Key: {k}")
            try:
                # print first 300 chars of value
                val_str = v.decode('utf-8') if isinstance(v, bytes) else str(v)
                print(f"Value: {val_str[:300]}")
            except:
                print("Value: <binary>")
    except Exception as e:
        print("Error reading db:", e)

