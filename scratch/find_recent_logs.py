import os, glob, re

log_dirs = [
    r"C:\Users\Joshu\AppData\Roaming\Antigravity",
    r"C:\Users\Joshu\AppData\Roaming\Antigravity IDE",
    r"C:\Users\Joshu\.gemini\antigravity",
    r"C:\Users\Joshu\AppData\Local\Programs\antigravity",
    r"C:\Users\Joshu\AppData\Local\Programs\Antigravity IDE"
]

print("=== Searching for Antigravity log files ===")
found_logs = []
for d in log_dirs:
    if os.path.exists(d):
        for root, dirs, files in os.walk(d):
            for f in files:
                if f.endswith(('.log', '.txt')) or 'log' in f.lower() or 'model' in f.lower():
                    full = os.path.join(root, f)
                    try:
                        sz = os.path.getsize(full)
                        mtime = os.path.getmtime(full)
                        found_logs.append((mtime, sz, full))
                    except:
                        pass

found_logs.sort(key=lambda x: x[0], reverse=True)
print(f"Found {len(found_logs)} log/model files. Top 15 most recent:")
for mtime, sz, full in found_logs[:15]:
    import datetime
    dt = datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')
    print(f"{dt} | {sz} bytes | {full}")

