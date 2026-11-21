import hashlib, json, subprocess, sys
from pathlib import Path
ROOT=Path('C:/Users/Joshu/dev/ai-os-projects/lsatu-spot-confirmed-fixes-20261025')
ART=Path(__file__).parent
result=ART/sys.argv[1]/'result.json'
d=json.loads(result.read_text(encoding='utf-8'))
assert d['status']=='completed' and d['mode']=='inspect' and d['response']['verdict']=='APPROVED','Final inspection not approved'
assert d['observed_models']==['claude-opus-5-5'],'Unexpected reviewer model'
allow={
 '.impeccable/surfaces/src-features-activity-centre.md',
 'src/features/activity-centre/components/CoachFeedback.relationship.test.tsx',
 'src/features/activity-centre/components/CoachFeedback.tsx',
 'src/features/activity-centre/components/RelationshipIntro.test.tsx',
 'src/features/activity-centre/components/RelationshipIntro.tsx',
 'src/features/activity-centre/content/spot-the-relationship.answerKey.test.ts',
 'src/features/activity-centre/content/spot-the-relationship.json',
 'src/features/activity-centre/worlds/observatory/observatory.ts',
 'src/features/activity-centre/worlds/observatory/observatory.test.ts',
}
expected={f['path'] for f in d['snapshot']['files']}
assert expected==allow, 'Review manifest differs from release allowlist'
for f in d['snapshot']['files']:
    assert hashlib.sha256((ROOT/f['path']).read_bytes()).hexdigest()==f['sha256'],f['path']+' changed after review'
assert hashlib.sha256(Path(d['plan']).read_bytes()).hexdigest()==d['plan_sha256'],'Plan changed after review'
staged=set(subprocess.check_output(['git','diff','--cached','--name-only'],cwd=ROOT,text=True).splitlines())
assert staged==allow,'Staged scope differs from reviewed scope'
assert not subprocess.check_output(['git','diff','--name-only'],cwd=ROOT,text=True).strip(),'Unstaged source edits'
assert hashlib.sha256((ART/'content-release.py').read_bytes()).hexdigest().upper()=='B8331BF2B94F0B6DDA50A13C199C76C79EE6587F7F22C87083B91A9E344EAB6C','External publisher changed after review contract'
receipt={'approved':True,'model':d['observed_models'],'snapshot':d['snapshot']['sha256'],'review':str(result),'files':sorted(allow)}
(ART/'approval-check.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
