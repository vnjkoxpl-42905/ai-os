import urllib.request
import json
from pathlib import Path

def get_key():
    for line in Path('.env').read_text(encoding='utf-8').splitlines():
        if line.startswith('FIRECRAWL_API_KEY='):
            return line.split('=', 1)[1].strip('"\' ')
    return None

key = get_key()
job_id = '01a0bc33-cfda-7256-8d07-81b8161cabc2'

req = urllib.request.Request(
    f'https://api.firecrawl.dev/v2/agent/{job_id}',
    headers={'Authorization': f'Bearer {key}'}
)

try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        print('Status:', data.get('status'))
        if data.get('status') == 'completed':
            Path('scratch/firecrawl_results/agent_completed.json').write_text(json.dumps(data, indent=2), encoding='utf-8')
            print('Completed! Saved to scratch/firecrawl_results/agent_completed.json')
        else:
            print('Progress/Data:', json.dumps(data, indent=2)[:500])
except Exception as e:
    print('Error:', e)
