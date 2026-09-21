import os, glob

print("=== Checking user home directories ===")
user_home = os.path.expanduser("~")
for item in os.listdir(user_home):
    if "antigravity" in item.lower() or "gemini" in item.lower():
        print(os.path.join(user_home, item))

print("\n=== Checking Antigravity IDE extensions ===")
for p in [
    os.path.join(user_home, ".antigravity"),
    os.path.join(user_home, ".antigravity-ide"),
    os.path.join(os.environ.get("LOCALAPPDATA", ""), "Programs", "Antigravity IDE", "resources", "app", "extensions"),
    os.path.join(os.environ.get("APPDATA", ""), "Antigravity IDE", "User"),
    os.path.join(os.environ.get("USERPROFILE", ""), ".gemini", "antigravity")
]:
    if os.path.exists(p):
        print(f"Exists: {p}")
        if os.path.isdir(p):
            sub = os.listdir(p)[:15]
            print(f"  Contents: {sub}")

