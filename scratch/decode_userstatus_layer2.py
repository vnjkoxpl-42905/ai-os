import sqlite3, base64, re

db_path = r"C:\Users\Joshu\AppData\Roaming\Antigravity IDE\User\globalStorage\state.vscdb"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute("SELECT value FROM ItemTable WHERE key = 'antigravityUnifiedStateSync.userStatus';")
val = cur.fetchone()[0]

# Decode layer 1
b64_matches = re.findall(r"[A-Za-z0-9+/=]{50,}", val)
raw1 = base64.b64decode(b64_matches[0])
print(f"Layer 1 decoded: {len(raw1)} bytes")

# Look for base64 inside raw1
b64_layer2 = re.findall(rb"[A-Za-z0-9+/=]{50,}", raw1)
print(f"Found {len(b64_layer2)} base64 strings in Layer 1")
raw2 = base64.b64decode(b64_layer2[0])
print(f"Layer 2 decoded: {len(raw2)} bytes")

# Now search in raw2!
matches = re.findall(rb"(?:Gemini|Claude|GPT-OSS)[A-Za-z0-9\.\-_ \(\)]+", raw2)
print("=== Matches in Layer 2 ===")
for m in sorted(list(set(matches))):
    print(" ", m.decode('utf-8', errors='ignore'))

# Also search around Recommended in raw2
rec_idx = raw2.find(b"Recommended")
if rec_idx != -1:
    print("\n=== Around Recommended ===")
    snippet = raw2[rec_idx-20:rec_idx+600]
    strings = re.findall(rb"[A-Za-z0-9\.\-_ \(\)]{4,}", snippet)
    for s in strings:
        print("  Rec item:", s.decode('utf-8', errors='ignore'))

