import urllib.request
import json
from pathlib import Path

def get_key():
    for line in Path('.env').read_text(encoding='utf-8').splitlines():
        if line.startswith('FIRECRAWL_API_KEY='):
            return line.split('=', 1)[1].strip('"\' ')
    return None

key = get_key()

queries = [
    "Claude 4.6 Opus coding",
    "Gemini 3.8 Flash High coding capabilities",
    "Claude Opus vs Gemini Flash frontend UI design CSS",
    "Claude vs Gemini frontend spacing Tailwind UI precision"
]

results = []
for q in queries:
    req = urllib.request.Request(
        'https://api.firecrawl.dev/v1/search',
        headers={'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'},
        data=json.dumps({'query': q, 'limit': 3, 'scrapeOptions': {'formats': ['markdown']}}).encode('utf-8')
    )
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            items = data.get('data', [])
            for item in items:
                results.append({
                    'query': q,
                    'title': item.get('title'),
                    'url': item.get('url'),
                    'markdown': item.get('markdown', '')[:2000]
                })
    except Exception as e:
        print(f"Error searching {q}: {e}")

Path('scratch/firecrawl_results/queries_deep.json').write_text(json.dumps(results, indent=2), encoding='utf-8')
print(f"Saved {len(results)} results")
