import os, re

log_dir = r"C:\Users\Joshu\AppData\Roaming\Antigravity\logs"
print(f"Files in {log_dir}:")
if os.path.exists(log_dir):
    for f in os.listdir(log_dir):
        full = os.path.join(log_dir, f)
        print(f"  {f} ({os.path.getsize(full)} bytes)")

# Read language_server.log
ls_log = os.path.join(log_dir, "language_server.log")
if os.path.exists(ls_log):
    print(f"\n=== Searching {ls_log} for model, tier, auth, and fetchAvailableModels ===")
    with open(ls_log, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
        print(f"Total lines: {len(lines)}")
        matching = []
        for line in lines:
            if any(k in line.lower() for k in [
                "model", "available", "tier", "fetch", "gemini", "claude", "gpt", "sonnet", "opus", "pro", "flash"
            ]):
                matching.append(line.strip())
        print(f"Found {len(matching)} matching lines.")
        for l in matching[-30:]:
            print(l)

