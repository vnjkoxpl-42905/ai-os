import urllib.request
import json

PORT = 9223

def main():
    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{PORT}/json", timeout=2) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = [t for t in data if t.get('type') == 'page']
            print(f"=== AGENT BROWSER (PORT {PORT}) ===")
            print(f"Total open user tabs: {len(pages)}\n")
            for i, p in enumerate(pages, 1):
                print(f"Tab {i}:")
                print(f"  Title: {p.get('title')}")
                print(f"  URL:   {p.get('url')}\n")
    except Exception as e:
        print(f"Error querying agent browser on port {PORT}: {e}")

if __name__ == "__main__":
    main()
