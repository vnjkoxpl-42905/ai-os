import os, sys, glob, json, subprocess

print("=== Running Processes ===")
try:
    cmd = 'powershell -NoProfile -Command "Get-CimInstance Win32_Process | Where-Object { $_.Name -like \'*antigravity*\' -or $_.Name -like \'*gemini*\' -or $_.CommandLine -like \'*antigravity*\' } | Select-Object ProcessId, Name, ExecutablePath, CommandLine | Format-List"'
    res = subprocess.check_output(cmd, shell=True, text=True)
    print(res[:2000])
except Exception as e:
    print("Error getting processes:", e)

print("\n=== AppData directories ===")
localappdata = os.environ.get("LOCALAPPDATA", "")
appdata = os.environ.get("APPDATA", "")
userprofile = os.environ.get("USERPROFILE", "")

for d in [os.path.join(localappdata, "Programs"), localappdata, appdata, os.path.join(userprofile, ".gemini")]:
    if os.path.exists(d):
        items = [x for x in os.listdir(d) if "antigravity" in x.lower() or "gemini" in x.lower()]
        print(f"In {d}: {items}")

