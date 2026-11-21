import json, os, sys
d = json.load(open(sys.argv[1], encoding='utf-8'))
print(list(d[0].keys()))
for f in d:
    fn = '/'.join(f['file'].replace(chr(92), '/').split('/')[-2:])
    print(fn, f.get('antipattern') or f.get('name'), '|', str(f.get('snippet') or f.get('selector') or f.get('element') or f.get('evidence'))[:160])
