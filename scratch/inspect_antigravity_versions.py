import os, json, subprocess

print("=== Antigravity IDE package.json ===")
pkg_path = r"C:\Users\Joshu\AppData\Local\Programs\Antigravity IDE\resources\app\package.json"
if os.path.exists(pkg_path):
    with open(pkg_path, "r", encoding="utf-8") as f:
        pkg = json.load(f)
        for k in ["name", "version", "description", "main"]:
            print(f"{k}: {pkg.get(k)}")

print("\n=== Antigravity IDE product.json ===")
prod_path = r"C:\Users\Joshu\AppData\Local\Programs\Antigravity IDE\resources\app\product.json"
if os.path.exists(prod_path):
    with open(prod_path, "r", encoding="utf-8") as f:
        prod = json.load(f)
        for k in ["nameShort", "nameLong", "applicationName", "version", "commit", "date"]:
            print(f"{k}: {prod.get(k)}")

print("\n=== File Versions ===")
for exe in [
    r"C:\Users\Joshu\AppData\Local\Programs\antigravity\Antigravity.exe",
    r"C:\Users\Joshu\AppData\Local\Programs\Antigravity IDE\Antigravity IDE.exe"
]:
    if os.path.exists(exe):
        try:
            cmd = f'powershell -NoProfile -Command "(Get-Item \'{exe}\').VersionInfo | Format-List"'
            print(f"--- {exe} ---")
            print(subprocess.check_output(cmd, shell=True, text=True))
        except Exception as e:
            print("Error:", e)

