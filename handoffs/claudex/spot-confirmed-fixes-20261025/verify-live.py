import json, re, sys, urllib.request
from pathlib import Path
from urllib.parse import urljoin
ROOT='https://lsatprep.study/'
OUT=Path(__file__).parent
stage=sys.argv[1]
def read(url):
    req=urllib.request.Request(url,headers={'Cache-Control':'no-cache','User-Agent':'LSATU-confirmed-fixes-verification'})
    with urllib.request.urlopen(req,timeout=45) as response:return response.read().decode()
html=read(ROOT)
entry=re.search(r'(?:src|href)=["\']([^"\']*/index-[^"\']+\.js)',html).group(1)
entry_url=urljoin(ROOT,entry)
words=['One quotation for each relationship type is enough.','rather than the whole sentence','bolts at the base of the bridge']
queue=[entry_url]; seen=set(); found={}
while queue and len(seen)<12:
    url=queue.pop(0)
    if url in seen:continue
    seen.add(url);body=read(url)
    found[url]=[word for word in words if word in body]
    for ref in re.findall(r'["\']([^"\']*(?:ActivityRunner|CompletionSummary|CoachFeedback|relationshipPresentation)-[^"\']+\.js)["\']',body):
        queue.append(urljoin(ROOT if ref.startswith('assets/') else url,ref))
markers={word:any(word in values for values in found.values()) for word in words}
receipt={'entry':entry,'assets':found,'markers':markers}
(OUT/f'live-{stage}.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
if stage=='after':
    before=json.loads((OUT/'live-before.json').read_text())
    assert entry!=before['entry'],'Entry bundle unchanged'
    assert all(markers.values()),'New production marker missing'
