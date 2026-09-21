import os, sys, glob, json

app_dir = r"C:\Users\Joshu\AppData\Local\Programs\antigravity"
roaming_dir = r"C:\Users\Joshu\AppData\Roaming\Antigravity"
updater_dir = r"C:\Users\Joshu\AppData\Local\antigravity-updater"

print("=== App directory contents ===")
if os.path.exists(app_dir):
    for root, dirs, files in os.walk(app_dir):
        rel = os.path.relpath(root, app_dir)
        if rel.count(os.sep) > 2:
            continue
        for f in files:
            if f.endswith(('.json', '.txt', '.yaml', '.yml', '.toml', '.manifest')) or 'version' in f.lower() or 'package' in f.lower():
                full = os.path.join(root, f)
                try:
                    size = os.path.getsize(full)
                    print(f"{os.path.relpath(full, app_dir)} ({size} bytes)")
                except:
                    pass

print("\n=== Checking Roaming Antigravity Settings ===")
if os.path.exists(roaming_dir):
    for root, dirs, files in os.walk(roaming_dir):
        rel = os.path.relpath(root, roaming_dir)
        if rel.count(os.sep) > 2:
            continue
        for f in files:
            if f in ['settings.json', 'storage.json', 'Preferences', 'config.json', 'state.vscdb']:
                full = os.path.join(root, f)
                print(f"Config file: {os.path.relpath(full, roaming_dir)} ({os.path.getsize(full)} bytes)")

print("\n=== Checking updater_dir ===")
if os.path.exists(updater_dir):
    for f in os.listdir(updater_dir):
        print(f"Updater item: {f}")
