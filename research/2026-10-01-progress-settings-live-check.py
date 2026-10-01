"""Read-only publication metadata. No authentication or student writes."""
import json
import re
from urllib.request import Request, urlopen

with urlopen(Request('https://lsatprep.study/', headers={'Cache-Control': 'no-cache'}), timeout=30) as response:
    html = response.read().decode()
    status = response.status
print(json.dumps({
    'status': status,
    'entry': re.findall(r'assets/index-[^"<> ]+\.js', html),
    'build_metadata': [tag for tag in re.findall(r'<meta[^>]+>', html)
                       if re.search(r'build|commit', tag, re.I)],
}))
