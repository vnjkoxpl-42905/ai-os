import urllib.request
import json

try:
    with urllib.request.urlopen("http://127.0.0.1:9223/json") as resp:
        targets = json.loads(resp.read().decode('utf-8'))
        print(f"Total CDP targets: {len(targets)}")
        for t in targets:
            if t.get('type') == 'page':
                print(f"[PAGE] Title: {t.get('title')}")
                print(f"       URL:   {t.get('url')}")
                print(f"       ID:    {t.get('id')}\n")
except Exception as e:
    print(f"Error querying CDP: {e}")
