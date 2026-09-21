import sqlite3, base64, re

db_path = r"C:\Users\Joshu\AppData\Roaming\Antigravity IDE\User\globalStorage\state.vscdb"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute("SELECT value FROM ItemTable WHERE key = 'antigravityUnifiedStateSync.userStatus';")
val = cur.fetchone()[0]

b64_matches = re.findall(r"[A-Za-z0-9+/=]{20,}", val)
print(f"Found {len(b64_matches)} base64 strings with len >= 20")

for i, b in enumerate(b64_matches):
    try:
        raw = base64.b64decode(b)
        for m in [
            b"Gemini 3.8 Flash", b"Claude Sonnet 4.6", b"Claude Opus 4.6", b"GPT-OSS 120B", b"Recommended"
        ]:
            if m in raw:
                print(f"Match {i} ({len(raw)} bytes) has {m.decode('utf-8')}")
                idx = raw.find(m)
                print("Snippet around match:")
                print(raw[max(0, idx-100):min(len(raw), idx+150)])
    except Exception as e:
        pass

