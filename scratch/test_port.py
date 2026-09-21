import subprocess
import time
import socket
import urllib.request
import os

profile_dir = os.path.expandvars(r"%LOCALAPPDATA%\LSATU-Agent-Chrome")
chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

args = [
    chrome_exe,
    "--remote-debugging-port=9222",
    "--remote-debugging-address=127.0.0.1",
    "--remote-allow-origins=*",
    f"--user-data-dir={profile_dir}",
    "--no-first-run",
    "--no-default-browser-check",
    "https://lsatprep.study"
]

print(f"Launching Chrome: {args}")
proc = subprocess.Popen(args)
print(f"Chrome launched with PID: {proc.pid}")

time.sleep(3)

# Test socket connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = s.connect_ex(('127.0.0.1', 9222))
if result == 0:
    print("SUCCESS: Connected to 127.0.0.1:9222 via TCP socket!")
    s.close()
    try:
        req = urllib.request.urlopen("http://127.0.0.1:9222/json/version", timeout=3)
        data = req.read().decode('utf-8')
        print(f"CDP Version Data: {data}")
    except Exception as e:
        print(f"Error querying /json/version: {e}")
else:
    print(f"FAILED: Port 9222 is NOT listening (socket error code {result})")
    s.close()
