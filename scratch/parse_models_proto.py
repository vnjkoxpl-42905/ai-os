import sqlite3, base64, re

db_path = r"C:\Users\Joshu\AppData\Roaming\Antigravity IDE\User\globalStorage\state.vscdb"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute("SELECT value FROM ItemTable WHERE key = 'antigravityUnifiedStateSync.userStatus';")
val = cur.fetchone()[0]

# Find base64 chunk
b64_matches = re.findall(r"[A-Za-z0-9+/=]{100,}", val)
raw_bytes = base64.b64decode(b64_matches[0])

print(f"Decoded total bytes: {len(raw_bytes)}")

# Let's inspect all strings and sub-chunks
# Find all model names in the bytes
models = [
    "Gemini 3.8 Flash (High)",
    "Gemini 3.8 Flash (Medium)",
    "Gemini 3.8 Flash (Low)",
    "Gemini 3.7 Flash (High)",
    "Gemini 3.7 Flash (Medium)",
    "Gemini 3.7 Flash (Low)",
    "Gemini 3.6 Flash (High)",
    "Gemini 3.6 Flash (Medium)",
    "Gemini 3.6 Flash (Low)",
    "Gemini 3.1 Pro (High)",
    "Gemini 3.1 Pro (Low)",
    "Claude Sonnet 4.6 (Thinking)",
    "Claude Opus 4.6 (Thinking)",
    "GPT-OSS 120B (Medium)"
]

for m in models:
    pos = raw_bytes.find(m.encode('utf-8'))
    if pos != -1:
        # inspect around pos
        start = max(0, pos - 150)
        end = min(len(raw_bytes), pos + len(m) + 150)
        chunk = raw_bytes[start:end]
        # find hex and printable
        printable = "".join(chr(b) if 32 <= b <= 126 else f"\\x{b:02x}" for b in chunk)
        print(f"\nModel: {m} (Offset {pos}):\n{printable}")

