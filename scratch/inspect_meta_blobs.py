import os, sqlite3, re

db_path = r"C:\Users\Joshu\.gemini\antigravity\conversations\3c03d32c-fd9f-45cb-82ce-11890d7fc349.db"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

print("=== Checking gen_metadata ===")
cur.execute("SELECT idx, data FROM gen_metadata LIMIT 5;")
for idx, data in cur.fetchall():
    # extract printable strings >= 4 chars
    strings = [s for s in re.findall(rb"[A-Za-z0-9_\.\-\/ :]{4,}", data)]
    decoded = [s.decode('utf-8', errors='ignore') for s in strings]
    print(f"Step {idx}:", [s for s in decoded if any(k in s.lower() for k in ["gemini", "claude", "gpt", "model", "flash", "pro"])])

print("\n=== Checking executor_metadata ===")
cur.execute("SELECT idx, data FROM executor_metadata LIMIT 5;")
for idx, data in cur.fetchall():
    strings = [s for s in re.findall(rb"[A-Za-z0-9_\.\-\/ :]{4,}", data)]
    decoded = [s.decode('utf-8', errors='ignore') for s in strings]
    print(f"Step {idx}:", [s for s in decoded if any(k in s.lower() for k in ["gemini", "claude", "gpt", "model", "flash", "pro"])])

print("\n=== Checking trajectory_metadata_blob ===")
cur.execute("SELECT id, data FROM trajectory_metadata_blob;")
for tid, data in cur.fetchall():
    strings = [s for s in re.findall(rb"[A-Za-z0-9_\.\-\/ :]{4,}", data)]
    print(f"Blob {tid}:", [s.decode('utf-8', errors='ignore') for s in strings])

