import urllib.request
import json
import os
import sys

API_KEY = "fc-208ce20aa2704a2d8d13f7cd5b05d739"

def firecrawl_search(query, limit=5):
    url = "https://api.firecrawl.dev/v1/search"
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        data=json.dumps({"query": query, "limit": limit}).encode("utf-8")
    )
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data.get("data", [])
    except Exception as e:
        print(f"Error searching '{query}': {e}", file=sys.stderr)
        return []

def firecrawl_scrape(target_url):
    url = "https://api.firecrawl.dev/v1/scrape"
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        data=json.dumps({
            "url": target_url,
            "formats": ["markdown"]
        }).encode("utf-8")
    )
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data.get("data", {}).get("markdown", "")
    except Exception as e:
        print(f"Error scraping '{target_url}': {e}", file=sys.stderr)
        return ""

if __name__ == "__main__":
    queries = [
        ("Outreach", "Outreach App OpenAI ChatGPT 39 actions"),
        ("Docusign", "Docusign App OpenAI ChatGPT 23 actions"),
        ("Sales_Skills", "\"Analyze Account Signals\" \"Build Business Case\" \"Review Rep Call Trends\" ChatGPT skills"),
        ("MacOS_Apps", "\"Build macOS Apps\" OpenAI Developer Tools SwiftUI AppKit ChatGPT skills"),
        ("Anthropic_Skills", "\"Anthropic-managed skills for Claude Desktop\" ChatGPT")
    ]
    
    os.makedirs("scratch/firecrawl_results", exist_ok=True)
    
    results = {}
    for name, q in queries:
        print(f"=== Searching for {name}: {q} ===")
        res = firecrawl_search(q, limit=3)
        results[name] = res
        with open(f"scratch/firecrawl_results/{name}_search.json", "w", encoding="utf-8") as f:
            json.dump(res, f, indent=2)
        print(f"Found {len(res)} results for {name}")
        for r in res:
            print(f"  - {r.get('title')}: {r.get('url')}")
