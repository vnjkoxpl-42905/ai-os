import json,re,urllib.request
from pathlib import Path
site="https://lsatprep.study"
def read(url):
    request=urllib.request.Request(url,headers={"Cache-Control":"no-cache","User-Agent":"LSATU-release-verification"})
    with urllib.request.urlopen(request,timeout=40) as response:
        return response.read().decode("utf-8")
html=read(site)
entry=re.search(r'src="(/assets/index-[^"]+\.js)"',html).group(1)
js=read(site+entry)
css=set(re.findall(r'(?:/)?assets/[^"\s<>]+\.css',html+js))
selected=[p for p in css if any(name in p for name in ["OfficialQuestionPane","InlineChoice","Drill-","index-"])]
checks=[]
for asset in selected[:8]:
    content=read(site+"/"+asset.lstrip("/"))
    checks.append({"asset":asset,"explanationSelectorPresent":".choice-note__panel" in content,"openStatePresent":'aria-expanded="true"' in content or "aria-expanded=true" in content})
result={"site":site,"entry":entry,"previousEntry":"/assets/index-Cs6GFrK8.js","bundleChanged":entry!="/assets/index-Cs6GFrK8.js","cssChecks":checks}
Path(__file__).with_name("live-assets.json").write_text(json.dumps(result,indent=2))
print(json.dumps(result))
