import json, subprocess, sys, threading, time
from pathlib import Path
root = Path(__file__).parent
deadline = time.monotonic() + 720
print('Waiting for the approved release on lsatprep.study; bounded to 12 minutes.', flush=True)
while time.monotonic() < deadline:
    result = subprocess.run([sys.executable, str(root/'verify-live.py'), 'after'], capture_output=True, text=True)
    if result.returncode == 0:
        print(result.stdout, flush=True)
        sys.exit(0)
    threading.Event().wait(20)
print('Production still does not contain the verified release markers.', flush=True)
sys.exit(1)
