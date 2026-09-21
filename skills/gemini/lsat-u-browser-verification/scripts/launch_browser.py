import os
import sys
import subprocess
import socket
import urllib.request
import time

CHROME_EXE = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PROFILE_DIR = os.path.expandvars(r"%LOCALAPPDATA%\LSATU-Agent-Chrome")
PORT = 9223
DEFAULT_URL = "https://lsatprep.study"

def is_running(port=PORT):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.settimeout(1.0)
        res = s.connect_ex(('127.0.0.1', port))
        s.close()
        return res == 0
    except Exception:
        return False

def launch(url=DEFAULT_URL):
    if is_running(PORT):
        print(f"LSAT U Agent Browser is already running on 127.0.0.1:{PORT}.")
        return True

    os.makedirs(PROFILE_DIR, exist_ok=True)

    cmd = (
        f'"{CHROME_EXE}" '
        f'--remote-debugging-port={PORT} '
        f'--remote-debugging-address=127.0.0.1 '
        f'--remote-allow-origins=* '
        f'--user-data-dir="{PROFILE_DIR}" '
        f'--no-first-run '
        f'--no-default-browser-check '
        f'{url}'
    )

    # Spawn via WMI PowerShell to ensure complete detachment from Antigravity Job Object
    ps_cmd = f"(Invoke-CimMethod -ClassName Win32_Process -MethodName Create -Arguments @{{CommandLine = '{cmd}'}}).ReturnValue"
    res = subprocess.run(["pwsh", "-Command", ps_cmd], capture_output=True, text=True)

    for _ in range(12):
        time.sleep(0.5)
        if is_running(PORT):
            try:
                with urllib.request.urlopen(f"http://127.0.0.1:{PORT}/json/version", timeout=2) as resp:
                    print(f"SUCCESS: LSAT U Agent Browser listening on 127.0.0.1:{PORT} (HTTP 200 OK)")
                    return True
            except Exception:
                pass

    print(f"WARNING: Port {PORT} did not respond within 6 seconds.")
    return False

if __name__ == "__main__":
    target_url = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_URL
    success = launch(target_url)
    sys.exit(0 if success else 1)
