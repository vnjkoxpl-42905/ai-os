import sqlite3, re

db_path = r"C:\Users\Joshu\AppData\Roaming\Antigravity IDE\User\globalStorage\state.vscdb"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute("SELECT value FROM ItemTable WHERE key = 'antigravityUnifiedStateSync.userStatus';")
val = cur.fetchone()[0]

# Extract all model-like names from val directly
print("=== All Model-like strings in userStatus ===")
matches = re.findall(r"(?:Gemini|Claude|GPT-OSS)[A-Za-z0-9\.\-_ \(\)]+", val)
for m in set(matches):
    print(" ", m)

# Let's see the Recommended section and other sections
rec_idx = val.find("Recommended")
if rec_idx != -1:
    print("\n=== Context around Recommended ===")
    print(repr(val[rec_idx-50:rec_idx+500]))

