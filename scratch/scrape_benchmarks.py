import urllib.request
import json
from pathlib import Path

def get_key():
    for line in Path('.env').read_text(encoding='utf-8').splitlines():
        if line.startswith('FIRECRAWL_API_KEY='):
            return line.split('=', 1)[1].strip('"\' ')
    return None

key = get_key()

urls = [
    ("thomas_wiegold_frontend", "https://thomas-wiegold.com/blog/best-llm-frontend-design/"),
    ("mindstudio_eval", "https://www.mindstudio.ai/blog/gemini-3-5-flash-vs-claude-opus-4-7-agentic-workflows")
]

for name, u in urls:
    req = urllib.request.Request(
        'https://api.firecrawl.dev/v1/scrape',
        headers={'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'},
        data=json.dumps({'url': u, 'formats': ['markdown']}).encode('utf-8')
    )
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            md = data.get('data', {}).get('markdown', '')
            Path(f'scratch/firecrawl_results/{name}.md').write_text(md, encoding='utf-8')
            print(f"Scraped {name} ({len(md)} chars)")
    except Exception as e:
        print(f"Error scraping {name}: {e}")
