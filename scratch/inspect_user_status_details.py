import sqlite3, base64, re

db_path = r"C:\Users\Joshu\AppData\Roaming\Antigravity IDE\User\globalStorage\state.vscdb"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute("SELECT value FROM ItemTable WHERE key = 'antigravityUnifiedStateSync.userStatus';")
row = cur.fetchone()
if row:
    val = row[0]
    print(f"Raw length: {len(val)}")
    # find base64 parts
    b64_matches = re.findall(r"[A-Za-z0-9+/=]{20,}", val)
    for b in b64_matches:
        try:
            dec = base64.b64decode(b)
            print(f"Decoded {len(dec)} bytes:")
            # print printable strings
            strings = re.findall(rb"[A-Za-z0-9_\.\-\/ :@]{3,}", dec)
            for s in strings:
                print(" ", s.decode('utf-8', errors='ignore'))
        except Exception as e:
            print("Error decoding:", e)

