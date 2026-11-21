import hashlib
import json
import re
import sys
import urllib.request
from pathlib import Path

base = sys.argv[1] if len(sys.argv) > 1 else 'https://lsatprep.study'
def read(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})).read()
html = read(base + '/?release-check=6a167c85').decode()
entries = re.findall(r'src="(/assets/index-[^"]+\.js)"', html)
result = {'entries': []}
for entry in entries:
    data = read(base + entry)
    text = data.decode()
    result['entries'].append({'path': entry, 'sha256': hashlib.sha256(data).hexdigest(), 'reference_ease_marker': 'classroom-reference-out' in text, 'async_motion_marker': 'data-motion-ready' in text, 'gsap_marker': 'ScrollTrigger' in text})
print(json.dumps(result, indent=2))
Path(__file__).with_name('live-verification.json').write_text(json.dumps(result, indent=2))
