import os

ls_path = r"C:\Users\Joshu\AppData\Local\Programs\antigravity\resources\bin\language_server.exe"

with open(ls_path, "rb") as f:
    data = f.read()

# Let's search around offset 51211731 ("internal error: failed to write agent.md")
# In Go binaries, strings are often referenced by LE pointers or near package paths
target = b"failed to write agent.md"
pos = data.find(target)
print(f"Target found at {pos}")

# Also search for "agent.md" case-sensitive and nearby words
for p in [49319767, 50093540, 50290652, 51211731, 51231475]:
    chunk = data[p-200:p+200]
    printable = "".join(chr(b) if 32 <= b <= 126 else " " for b in chunk)
    print(f"\nAround {p}: {printable}")

