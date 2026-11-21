import json, hashlib, collections, re
from pathlib import Path

ROOT=Path(r'C:\Users\Joshu\dev\ai-os\raw\sources\karpathy-brain\raw')
OUT=Path(__file__).parent
def audit(domain):
    base=ROOT/domain
    m=json.loads((base/'MANIFEST.json').read_text(encoding='utf-8'))
    items=m if isinstance(m,list) else m['items']
    rows=[]; errors=[]; hashes=collections.defaultdict(list)
    for i in items:
        p=base/i['path']
        if not p.is_file(): errors.append({'path':i['path'],'error':'missing'}); continue
        data=p.read_bytes(); h=hashlib.sha256(data).hexdigest(); words=len(data.decode('utf-8',errors='replace').split())
        for key,actual in [('sha256',h),('bytes',len(data)),('words',words)]:
            if i.get(key)!=actual: errors.append({'path':i['path'],'field':key,'recorded':i.get(key),'actual':actual})
        hashes[h].append(i['path'])
        reason=None; lower=i['path'].lower()
        if domain=='github':
            if '/jobs/html/' in lower or lower.endswith('/jobs/occupational_outlook_handbook.html'): reason='Bureau of Labor Statistics source HTML, not Karpathy-authored prose'
            elif lower.endswith('/jobs/prompt.md'): reason='generated BLS data and LLM score compilation, not wholly Karpathy-authored prose'
            elif any(x in lower for x in ['jquery','bootstrap','d3.v','d3.min','marked.min','mathjax','highlight.pack','libsvm','eigen/','eigenlibsvm','sunspot','assets/js/vendor','vendor/','underscore','backbone']): reason='third-party library or vendor candidate'
            elif any(x in lower for x in ['/data/','/datasets/','/input.txt','/names.txt','/enwik8','/tinyshakespeare','/bpe','/vocab','/merges','/encoder.json','/package-lock.json','/yarn.lock','/poetry.lock','/uv.lock','/pnpm-lock','/tokenizer.json']): reason='dataset, vocabulary, or generated dependency candidate'
            elif lower.endswith(('.csv','.tsv','.json','.jsonl','.txt','.min.js','.svg')): reason='data, generated, or asset candidate (review before attribution)'
        rows.append({'path':i['path'],'words':words,'bytes':len(data),'sha256':h,'source_id':i.get('source_id'),'classification_flag':reason})
    extras=[]
    if domain=='blog':
        for i in items:
            p=base/i['html_path']
            if not p.is_file(): errors.append({'path':i['html_path'],'error':'missing HTML'})
        roots=['md','html']
    else: roots=['repos','gists']
    physical=[p for r in roots for p in (base/r).rglob('*') if p.is_file()]
    registered={str((base/i['path']).resolve()) for i in items}
    if domain=='github': extras=[str(p.relative_to(base)) for p in physical if str(p.resolve()) not in registered]
    result={'domain':domain,'manifest_items':len(items),'physical_payload_files':len(physical),'manifest_words':sum(i.get('words',0) for i in items),'verified_words':sum(r['words'] for r in rows),'verified_bytes':sum(r['bytes'] for r in rows),'errors':errors,'unregistered_payload_files':extras,'exact_duplicate_groups':[v for v in hashes.values() if len(v)>1],'top_word_files':sorted(rows,key=lambda x:-x['words'])[:30],'classification_flags':dict(collections.Counter(r['classification_flag'] or 'unflagged, authorship not verified' for r in rows)),'flagged_words':sum(r['words'] for r in rows if r['classification_flag']),'unflagged_words':sum(r['words'] for r in rows if not r['classification_flag']),'rows':rows}
    if domain=='github':
        result.update({'logical_source_count':len(m['sources']),'repo_count':sum(not s[0].startswith('gist:') for s in m['sources']),'gist_count':sum(s[0].startswith('gist:') for s in m['sources']),'license_counts':dict(collections.Counter(s[3] for s in m['sources'])),'invalid_commit_shas':[s for s in m['sources'] if not re.fullmatch('[0-9a-f]{40}',s[2] or '')],'discovery':m['discovered'],'exclusions_count':len(m['exclusions']),'sources':m['sources']})
    return result
OUT.mkdir(parents=True,exist_ok=True)
r={d:audit(d) for d in ['blog','github']}
(OUT/'blog-github-audit.json').write_text(json.dumps(r,indent=2),encoding='utf-8')
for d,a in r.items():
    print(d,json.dumps({k:v for k,v in a.items() if k not in ['rows','sources','top_word_files','exact_duplicate_groups']}))
    print('TOP',json.dumps(a['top_word_files'][:15]))
