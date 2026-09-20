import urllib.request
import json
import time
from pathlib import Path

def get_key():
    for line in Path('.env').read_text(encoding='utf-8').splitlines():
        if line.startswith('FIRECRAWL_API_KEY='):
            return line.split('=', 1)[1].strip('"\' ')
    return None

key = get_key()

# Let's search specifically for Claude Opus 4.6, Gemini 3.8 Flash High, and Gemini 3.1 Pro coding benchmarks
queries = [
    "Claude Opus 4.6 coding benchmark frontend",
    "Gemini 3.8 Flash High coding benchmark",
    "Gemini 3.1 Pro coding benchmark frontend",
    "Claude Opus 4.6 vs Gemini 3.1 Pro frontend web design"
]

results = []
for q in queries:
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
                results.append({
                    'query': q,
                    'title': item.get('title'),
                    'url': item.get('url'),
                    'markdown': item.get('markdown', '')[:1500]
                })
    except Exception as e:
        print(f"  Error: {e}")
    time.sleep(1)

Path('scratch/firecrawl_results/exact_models_search.json').write_text(json.dumps(results, indent=2), encoding='utf-8')
print("Search complete.")

# Launch Firecrawl Agent for exact comparison
print("Launching Firecrawl Agent for exact three-way comparison...")
agent_req = urllib.request.Request(
    'https://api.firecrawl.dev/v2/agent',
    headers={'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'},
    data=json.dumps({
        'prompt': 'Compare specifically Claude Opus 4.6 vs Gemini 3.8 Flash (High thinking mode) vs Gemini 3.1 Pro for frontend web development tasks: editing existing React components, Tailwind CSS spacing adjustments, UI hierarchy, and preserving component state. Which of these three is best suited for adjusting UI spacing on an existing production React drill page, and how do they rank?'
    }).encode('utf-8')
)

try:
    with urllib.request.urlopen(agent_req) as resp:
        agent_data = json.loads(resp.read().decode('utf-8'))
        print("Agent launched:", json.dumps(agent_data, indent=2))
        Path('scratch/firecrawl_results/exact_agent_launch.json').write_text(json.dumps(agent_data, indent=2), encoding='utf-8')
except Exception as e:
    print("Agent error:", e)
