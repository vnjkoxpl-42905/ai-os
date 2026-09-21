import os

ls_path = r"C:\Users\Joshu\AppData\Local\Programs\antigravity\resources\bin\language_server.exe"

with open(ls_path, "rb") as f:
    data = f.read()

tiers = [b"MODEL_TIER_FLASH_LITE", b"MODEL_TIER_FLASH", b"MODEL_TIER_PRO"]

for t in tiers:
    pos = 0
    found = []
    while True:
        pos = data.find(t, pos)
        if pos == -1:
            break
        found.append(pos)
        pos += len(t)
    print(f"\n=== {t.decode()} ({len(found)} occurrences) ===")
    for p in found:
        chunk = data[max(0, p-100):min(len(data), p+200)]
        printable = "".join(chr(b) if 32 <= b <= 126 else " " for b in chunk)
        print(f"Offset {p}:\n  {printable.strip()}")

