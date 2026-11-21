import hashlib, json, subprocess, sys
from pathlib import Path
root = Path('C:/Users/Joshu/dev/ai-os-projects/lsatu-spot-video-release-20261025')
result = Path(__file__).parent / 'claudex-dhlx1p4r/result.json'
d = json.loads(result.read_text(encoding='utf-8'))
assert d['status'] == 'completed' and d['response']['verdict'] == 'APPROVED', 'latest inspection is not approved'
assert d['observed_models'] == ['claude-opus-5-5'], 'wrong observed model'
expected = {f['path'] for f in d['snapshot']['files']}
for f in d['snapshot']['files']:
    assert hashlib.sha256((root/f['path']).read_bytes()).hexdigest() == f['sha256'], f['path']+' changed after inspection'
staged = set(subprocess.check_output(['git','diff','--cached','--name-only'],cwd=root,text=True).splitlines())
assert staged == expected, {'staged':sorted(staged),'reviewed':sorted(expected)}
assert not any(p.startswith('supabase/') for p in staged), 'backend scope leak'
assert not subprocess.check_output(['git','diff','--name-only'],cwd=root,text=True).strip(), 'unstaged changes'
print(json.dumps({'verdict':d['response']['verdict'],'model':d['observed_models'],'reviewed_files':sorted(expected),'snapshot':d['snapshot']['sha256']}))
