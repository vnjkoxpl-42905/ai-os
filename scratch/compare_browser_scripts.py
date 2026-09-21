import os
import hashlib
import glob

browser_scripts = [
    "launch_browser.py",
    "launch_lsatu_browser.py",
    "agent-browser.mjs",
    "verify-viewports.mjs",
    "verify_localhost.mjs",
    "verify_control_drill.mjs",
    "check_auth.mjs",
    "check_session.py",
    "start-dev-session.ps1",
    "launch-agent-browser.ps1",
    "test_persistence_cycle.mjs"
]

search_roots = [
    r"C:\Users\Joshu\Tools\LSATU-Agent",
    r"C:\Users\Joshu\dev\ai-os\system\scripts",
    r"C:\Users\Joshu\dev\ai-os\scratch",
    r"C:\Users\Joshu\dev\ai-os\.gemini",
    r"C:\Users\Joshu\.gemini"
]

def hash_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

print("=== Browser Script Duplicate / Hash Comparison ===")
for script_name in browser_scripts:
    found = []
    for r in search_roots:
        if os.path.exists(r):
            for root, dirs, files in os.walk(r):
                if script_name in files:
                    fp = os.path.join(root, script_name)
                    found.append(fp)
    if found:
        print(f"\nScript: {script_name} (Found {len(found)} copies):")
        hashes = {}
        for p in found:
            sh = hash_file(p)
            hashes[p] = sh
            print(f"  - {p} (SHA256: {sh[:16]}..., Size: {os.path.getsize(p)} B)")
        unique_hashes = set(hashes.values())
        if len(unique_hashes) == 1:
            print("    Status: IDENTICAL")
        else:
            print("    Status: DIVERGENT (Different content across paths!)")
    else:
        print(f"\nScript: {script_name}: NOT FOUND in searched roots")
