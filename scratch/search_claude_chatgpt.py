import urllib.request
import json

API_KEY = 'fc-208ce20aa2704a2d8d13f7cd5b05d739'

def search(q):
    req = urllib.request.Request(
        'https://api.firecrawl.dev/v1/search',
        headers={'Authorization': f'Bearer {API_KEY}', 'Content-Type': 'application/json'},
        data=json.dumps({'query': q, 'limit': 5}).encode('utf-8')
    )
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return data.get('data', [])
    except Exception as e:
        print('Error:', e)
        return []

for item in search('Claude Desktop skills in ChatGPT OR Codex'):
    print(item.get('title'), item.get('url'))

print('---')
for item in search('ChatGPT macOS app plugins skills local directory'):
    print(item.get('title'), item.get('url'))
