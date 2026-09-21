import os

log_path = r"C:\Users\Joshu\AppData\Roaming\Antigravity\logs\language_server.log"
with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()

print(f"Total lines in language_server.log: {len(lines)}")
for idx, line in enumerate(lines):
    if "fetchavailablemodels" in line.lower():
        print(f"--- Line {idx} ---")
        start = max(0, idx - 5)
        end = min(len(lines), idx + 20)
        for i in range(start, end):
            print(f"[{i}] {lines[i].strip()[:300]}")

