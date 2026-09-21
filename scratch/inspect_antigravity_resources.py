import os, sys

for p in [
    r"C:\Users\Joshu\AppData\Local\Programs\antigravity\resources\app-update.yml",
    r"C:\Users\Joshu\AppData\Roaming\Antigravity\Preferences"
]:
    if os.path.exists(p):
        print(f"=== {p} ===")
        with open(p, "r", encoding="utf-8", errors="ignore") as f:
            print(f.read())

print("=== Checking resources directory ===")
res_dir = r"C:\Users\Joshu\AppData\Local\Programs\antigravity\resources"
if os.path.exists(res_dir):
    for item in os.listdir(res_dir):
        full = os.path.join(res_dir, item)
        print(f"{item} ({os.path.getsize(full)} bytes)")

print("=== Checking Antigravity IDE directory ===")
ide_dir = r"C:\Users\Joshu\AppData\Local\Programs\Antigravity IDE"
if os.path.exists(ide_dir):
    for root, dirs, files in os.walk(ide_dir):
        rel = os.path.relpath(root, ide_dir)
        if rel.count(os.sep) > 1:
            continue
        for f in files:
            if f.endswith(('.json', '.yml', '.yaml', '.txt', '.exe')):
                full = os.path.join(root, f)
                print(f"{os.path.relpath(full, ide_dir)} ({os.path.getsize(full)} bytes)")

