"""Bounded admin content publication. No assignment writes or model calls."""
import hashlib, json, subprocess, sys, urllib.parse, urllib.request
from pathlib import Path
sys.path.insert(0, 'C:/Users/Joshu/dev/ai-os/system/scripts')
from lsatu_api import client, _ssl_context

ROOT = Path(__file__).parent
REPO = Path('C:/Users/Joshu/dev/ai-os-projects/lsatu-spot-confirmed-fixes-20261025')
SOURCE = 'src/features/activity-centre/content/spot-the-relationship.json'
ID = '12251bd3-d260-4108-bc35-bcf478e483e6'
SOURCE_SHA256 = '4911D51FD1E04A189FD7B14AC1C40A7D31919D82C2350C1D12BC5B611F75CD14'
def require(condition, message):
    if not condition: raise RuntimeError(message)
def stable(v): return json.dumps(v, sort_keys=True, separators=(',', ':'), ensure_ascii=False)
def digest(v): return hashlib.sha256(stable(v).encode()).hexdigest()
def content(v): return {k:v[k] for k in ('items','instructions','subtitle')}
def save(name,v): (ROOT/name).write_text(json.dumps(v, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
c=client()
rows=c.get('activities', id='eq.'+ID, slug='eq.spot-the-relationship')
require(len(rows)==1, 'Expected one exact canonical activity')
live=rows[0]
assignments=c.get('activity_assignments', select='id,status,started_at,completed_at,items,instructions,subtitle', activity_id='eq.'+ID)
metadata=[{k:a[k] for k in ('id','status','started_at','completed_at')} | {'snapshotHash':digest(content(a))} for a in assignments]
source_bytes=(REPO/SOURCE).read_bytes()
require(hashlib.sha256(source_bytes).hexdigest().upper()==SOURCE_SHA256, 'Authored file changed from reviewed content hash')
authored=json.loads(source_bytes)
require(len(authored['items'])==48 and [i['order'] for i in authored['items']]==list(range(1,49)), 'Expected exactly orders 1-48')
mode=sys.argv[1]
if mode=='preflight':
    baseline=json.loads(subprocess.check_output(['git','show','73dd27e2c68ed9a9b46af274a1366c2817f7030c:'+SOURCE], cwd=REPO, text=True, encoding='utf-8'))
    observed_path=ROOT/'canonical-observed.json'
    if observed_path.exists():
        observed=json.loads(observed_path.read_text(encoding='utf-8'))
        require(content(live)==content(observed) and live['updated_at']==observed['updated_at'], 'Live content changed during reconciliation')
    else:
        save('canonical-observed.json',live)
        save('assignments-observed.json',metadata)
    differences=[]
    def compare(a,b,path=''):
        if isinstance(a,dict) and isinstance(b,dict):
            for k in sorted(a.keys()|b.keys()): compare(a.get(k),b.get(k),path+'.'+k)
        elif isinstance(a,list) and isinstance(b,list) and len(a)==len(b):
            for n,(x,y) in enumerate(zip(a,b)): compare(x,y,path+f'[{n}]')
        elif a!=b: differences.append({'path':path,'live':a,'baseline':b})
    compare(content(live),content(baseline))
    save('canonical-baseline-diff.json',differences)
    baseline_difference_count=len(differences)
    differences=[]
    compare(content(live),content(authored))
    save('canonical-target-diff.json',differences)
    # The coordinator examined the baseline drift and included it in the final
    # review contract. Only this canonical activity's three content fields move.
    save('canonical-before.json',live)
    save('assignments-before.json',metadata)
    print(json.dumps({'mode':mode,'activity':ID,'items':len(live['items']),'baselineDifferenceCount':baseline_difference_count,'targetDifferenceCount':len(differences),'assignments':[{k:v for k,v in a.items() if k!='id'} for a in metadata]}))
elif mode=='apply':
    before=json.loads((ROOT/'canonical-before.json').read_text(encoding='utf-8'))
    require(content(live)==content(before) and live['updated_at']==before['updated_at'], 'Concurrent canonical edit detected')
    query=urllib.parse.urlencode({'id':'eq.'+ID,'slug':'eq.spot-the-relationship','updated_at':'eq.'+before['updated_at']})
    req=urllib.request.Request(c.url+'/rest/v1/activities?'+query, data=json.dumps(content(authored)).encode(), method='PATCH', headers={'apikey':c.anon_key,'Authorization':'Bearer '+c.token,'Content-Type':'application/json','Prefer':'return=representation'})
    with urllib.request.urlopen(req,timeout=45,context=_ssl_context()) as response: result=json.load(response)
    require(len(result)==1 and content(result[0])==content(authored), 'Canonical write readback failed')
    fresh=c.get('activities',id='eq.'+ID)[0]
    require(content(fresh)==content(authored), 'Fresh canonical readback failed')
    save('canonical-after.json',fresh)
    print(json.dumps({'mode':mode,'activity':ID,'canonicalMatches':True,'items':len(fresh['items']),'contentHash':digest(content(fresh)),'assignmentWrites':0}))
elif mode=='verify':
    require(content(live)==content(authored), 'Canonical activity differs from release')
    before={a['id']:a for a in json.loads((ROOT/'assignments-before.json').read_text(encoding='utf-8'))}
    current={a['id']:a for a in metadata}
    missing=sorted(before.keys()-current.keys())
    added=sorted(current.keys()-before.keys())
    common=before.keys() & current.keys()
    changed=[key for key in common if current[key]['snapshotHash']!=before[key]['snapshotHash']]
    state_changes=[key for key in common if any(current[key][field]!=before[key][field] for field in ('status','started_at','completed_at'))]
    verification={'canonicalMatches':True,'items':48,'assignmentsPreserved':len(common)-len(changed),'missingAssignments':missing,'newAssignments':added,'snapshotChanges':changed,'assignmentStateChanges':state_changes,'assignmentWrites':0,'contentHash':digest(content(live))}
    save('content-verification.json',verification)
    require(not missing and not changed, 'Historical assignment snapshot missing or changed; see verification receipt')
    print((ROOT/'content-verification.json').read_text())
else: raise ValueError('Unknown mode')
