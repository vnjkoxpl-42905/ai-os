import json, re, sys, urllib.request
from pathlib import Path
from urllib.parse import urljoin

out = Path(__file__).parent
stage = sys.argv[1]
def read(url):
    req = urllib.request.Request(url, headers={'Cache-Control': 'no-cache', 'User-Agent': 'LSATU-release-verification'})
    with urllib.request.urlopen(req, timeout=45) as response:
        return response.read().decode('utf-8')
root = sys.argv[2] if len(sys.argv) > 2 else 'https://lsatprep.study/'
html = read(root)
index = re.search(r'(?:src|href)=["\']([^"\']*/index-[^"\']+\.js)', html).group(1)
bundle = read(urljoin(root, index))
runner = re.search(r'["\']([^"\']*ActivityRunner-[^"\']+\.js)', bundle)
runner_path = runner.group(1).removeprefix('./') if runner else None
runner_url = urljoin(root if runner_path and runner_path.startswith('assets/') else urljoin(root, index), runner_path) if runner_path else None
code = read(runner_url) if runner_url else bundle
words = ['relationship-video-shell', 'Expand video', 'Close video', 'relationship-video-fallback-expanded']
marker_assets = {}
for asset_url, asset_code in [(urljoin(root,index),bundle),(runner_url,code)]:
    found = [word for word in words if word in asset_code]
    if found: marker_assets[asset_url] = found
if stage != 'before' and not marker_assets and runner_url:
    # ActivityIntro is shared with the completion module in the production build.
    # Follow the actual runner import, never a guessed asset filename.
    refs = re.findall(r'["\'](\.?\.?/[^"\']*CompletionSummary-[^"\']+\.js)["\']',code)
    for ref in refs:
        asset_url=urljoin(runner_url,ref)
        asset_code=read(asset_url)
        marker_assets[asset_url]=[word for word in words if word in asset_code]
markers = {word: any(word in found for found in marker_assets.values()) for word in words}
receipt = {'index': index, 'runner': runner_url, 'marker_assets':marker_assets, 'markers': markers}
(out / f'live-{stage}.json').write_text(json.dumps(receipt, indent=2), encoding='utf-8')
print(json.dumps(receipt))
if stage == 'after':
    before = json.loads((out / 'live-before.json').read_text())
    assert index != before['index'], 'index hash unchanged'
    assert all(markers.values()), 'release marker missing from reachable chunk'
