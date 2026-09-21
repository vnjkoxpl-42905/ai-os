import sqlite3, base64, re

db_path = r"C:\Users\Joshu\AppData\Roaming\Antigravity IDE\User\globalStorage\state.vscdb"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute("SELECT value FROM ItemTable WHERE key = 'antigravityUnifiedStateSync.userStatus';")
val = cur.fetchone()[0]

b64_matches = re.findall(r"[A-Za-z0-9+/=]{50,}", val)
raw1 = base64.b64decode(b64_matches[0])
b64_layer2 = re.findall(rb"[A-Za-z0-9+/=]{50,}", raw1)
raw2 = base64.b64decode(b64_layer2[0])

# Parse protobuf records
# In protobuf, strings are wire type 2 (length-delimited)
# Let's find every model block in raw2
model_names = [
    b"Gemini 3.8 Flash (High)",
    b"Gemini 3.8 Flash (Medium)",
    b"Gemini 3.8 Flash (Low)",
    b"Gemini 3.7 Flash (High)",
    b"Gemini 3.7 Flash (Medium)",
    b"Gemini 3.7 Flash (Low)",
    b"Gemini 3.6 Flash (High)",
    b"Gemini 3.6 Flash (Medium)",
    b"Gemini 3.6 Flash (Low)",
    b"Gemini 3.1 Pro (High)",
    b"Gemini 3.1 Pro (Low)",
    b"Claude Sonnet 4.6 (Thinking)",
    b"Claude Opus 4.6 (Thinking)",
    b"GPT-OSS 120B (Medium)"
]

print("=== Analyzing Model Records ===")
for m in model_names:
    pos = raw2.find(m)
    if pos != -1:
        # scan backwards to find the start of this record
        # and forwards to see fields
        snippet = raw2[pos-10:pos+len(m)+150]
        hex_dump = " ".join(f"{b:02x}" for b in snippet[:60])
        printable = "".join(chr(b) if 32 <= b <= 126 else "." for b in snippet)
        print(f"\nModel: {m.decode('utf-8')}")
        print(f"  Offset: {pos}")
        print(f"  Hex: {hex_dump}")
        print(f"  Printable: {printable}")

