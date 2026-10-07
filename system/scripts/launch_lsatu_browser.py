import os
import sys
import subprocess
import socket
import urllib.request
import time

CHROME_EXE = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PROFILE_DIR = os.path.expandvars(r"%LOCALAPPDATA%\LSATU-Agent-Chrome")
URL = "https://lsatprep.study"

def is_running(port=9222):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.settimeout(1.0)
        res = s.connect_ex(('127.0.0.1', port))
        s.close()
        return res == 0
    except Exception:
        return False

def launch_browser():
    if is_running(9222):
        print("LSAT U Agent Browser is already running on 127.0.0.1:9222.")
        return True

    os.makedirs(PROFILE_DIR, exist_ok=True)

    args = [
        CHROME_EXE,
        "--remote-debugging-port=9222",
        "--remote-debugging-address=127.0.0.1",
        "--remote-allow-origins=*",
        f"--user-data-dir={PROFILE_DIR}",
        "--no-first-run",
        "--no-default-browser-check",
        URL
    ]

    # Windows flags to ensure process completely detaches from parent terminal/job
    DETACHED_PROCESS = 0x00000008
    CREATE_NEW_PROCESS_GROUP = 0x00000200
    flags = DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP

    print(f"Launching detached LSAT U Agent Browser...")
    subprocess.Popen(
        args,
        creationflags=flags,
        close_fds=True
    )

    # Wait up to 10 seconds for CDP listener
    for i in range(10):
        time.sleep(1)
        if is_running(9222):
            try:
                with urllib.request.urlopen("http://127.0.0.1:9222/json/version", timeout=2) as resp:
                    print(f"Verified: Chrome is listening on 127.0.0.1:9222 (HTTP 200 OK)")
                    return True
            except Exception as e:
                pass
    
    print("Warning: Port 9222 did not respond within 10 seconds.")
    return False

if __name__ == "__main__":
    success = launch_browser()
    sys.exit(0 if success else 1)
