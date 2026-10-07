import urllib.request
import json
import socket

BROWSERS = [
    {"name": "LSAT U", "port": 9223, "target": "https://lsatprep.study/classroom", "profile": "LSATU-Agent-Chrome"},
    {"name": "Reddit", "port": 9224, "target": "https://chat.reddit.com", "profile": "Reddit-Agent-Chrome"},
    {"name": "7Sage", "port": 9225, "target": "https://7sage.com/accounts/login/", "profile": "7Sage-Agent-Chrome"},
    {"name": "Facebook", "port": 9226, "target": "https://www.facebook.com/messages", "profile": "Facebook-Agent-Chrome"},
]

def check_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.settimeout(1.0)
        res = s.connect_ex(('127.0.0.1', port))
        s.close()
        return res == 0
    except Exception:
        return False

def get_targets(port):
    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{port}/json", timeout=2) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = [t for t in data if t.get('type') == 'page']
            return pages
    except Exception as e:
        return []

def main():
    print("=== MULTI-BROWSER FLEET STATUS ===")
    for b in BROWSERS:
        running = check_port(b['port'])
        if not running:
            print(f"[{b['name'].upper()}] Port {b['port']}: NOT RUNNING")
            continue
        pages = get_targets(b['port'])
        print(f"[{b['name'].upper()}] Port {b['port']}: ACTIVE ({len(pages)} open tab(s))")
        for p in pages:
            print(f"    - Title: {p.get('title')}")
            print(f"      URL:   {p.get('url')}")

if __name__ == "__main__":
    main()
