import sqlite3, base64, re

db_path = r"C:\Users\Joshu\AppData\Roaming\Antigravity IDE\User\globalStorage\state.vscdb"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

keys = [
    "antigravityUnifiedStateSync.userStatus",
    "antigravityUnifiedStateSync.modelPreferences",
    "antigravityUnifiedStateSync.modelCredits",
    "antigravityUnifiedStateSync.agentPreferences"
]

for k in keys:
    cur.execute("SELECT value FROM ItemTable WHERE key = ?;", (k,))
    row = cur.fetchone()
    if row:
        val = row[0]
        print(f"\n================ Key: {k} ================")
        # try base64 decode
        try:
            raw = val.encode('utf-8')
            # often protobuf or base64
            # let's look for base64 blocks inside val
            b64_matches = re.findall(r"[A-Za-z0-9+/=]{16,}", val)
            print(f"Found {len(b64_matches)} base64-like strings")
            for b in b64_matches:
                try:
                    dec = base64.b64decode(b)
                    # find printable ASCII
                    printable = "".join(chr(x) if 32 <= x <= 126 else f"\\x{x:02x}" for x in dec)
                    print(f"Decoded ({len(dec)} bytes):\n{printable}\n")
                except Exception as ex:
                    pass
        except Exception as e:
            print("Error:", e)

