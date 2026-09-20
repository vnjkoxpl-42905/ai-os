import urllib.request
import json
import os
import sys
from pathlib import Path

def get_key():
    for line in Path('.env').read_text(encoding='utf-8').splitlines():
        if line.startswith('FIRECRAWL_API_KEY='):
            return line.split('=', 1)[1].strip('"\' ')
    return None

key = get_key()
if not key:
    print("No API key found")
    sys.exit(1)

print("Key loaded successfully")

# Test 1: Firecrawl Search
search_queries = [
    "Claude Opus vs Gemini Flash frontend UI design coding benchmark",
    "best LLM model frontend web design React Tailwind CSS spacing layout",
    "Claude 3.7 Sonnet Claude 4 Opus frontend styling Tailwind vs Gemini Flash"
]

search_results = []
for q in search_queries:
    print(f"Searching: {q}")
    req = urllib.request.Request(
        'https://api.firecrawl.dev/v1/search',
        headers={'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'},
        data=json.dumps({'query': q, 'limit': 3, 'scrapeOptions': {'formats': ['markdown']}}).encode('utf-8')
    )
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            items = data.get('data', [])
            print(f"  Got {len(items)} results")
            for item in items:
                search_results.append({
                    'query': q,
                    'title': item.get('title'),
                    'url': item.get('url'),
                    'markdown': item.get('markdown', '')[:1000]
                })
    except Exception as e:
        print(f"  Search error: {e}")

# Save search results
Path('scratch/firecrawl_results').mkdir(parents=True, exist_ok=True)
Path('scratch/firecrawl_results/frontend_model_search.json').write_text(json.dumps(search_results, indent=2), encoding='utf-8')
print("Search results saved.")

# Test 2: Firecrawl v2 Agent
print("Testing Firecrawl v2 Agent launch...")
agent_req = urllib.request.Request(
    'https://api.firecrawl.dev/v2/agent',
    headers={'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'},
    data=json.dumps({
        'prompt': 'Compare Claude Opus vs Gemini Flash for frontend UI development, focusing on React, Tailwind CSS, layout spacing, visual aesthetics, and component hierarchy. Which model is superior for fine UI adjustments and why?'
    }).encode('utf-8')
)

try:
    with urllib.request.urlopen(agent_req) as resp:
        print("Agent response status:", resp.status)
        agent_data = json.loads(resp.read().decode('utf-8'))
        print("Agent data:", json.dumps(agent_data, indent=2))
        Path('scratch/firecrawl_results/agent_launch.json').write_text(json.dumps(agent_data, indent=2), encoding='utf-8')
except Exception as e:
    print("Agent launch error:", e)
