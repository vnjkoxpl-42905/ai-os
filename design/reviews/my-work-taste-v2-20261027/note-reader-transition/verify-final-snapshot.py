import hashlib
import json
import subprocess
import sys
from pathlib import Path

home = Path(__file__).parent
repo = Path('C:/Users/Joshu/dev/ai-os-projects/lsatu-my-work-20261026')
result = json.loads((home / sys.argv[1] / 'result.json').read_text())
assert result['status'] == 'completed', result['status']
assert result['response']['verdict'] == 'APPROVED', result['response']['verdict']
assert not result['response']['findings'], result['response']['findings']
changed = []
for item in result['snapshot']['files']:
    path = repo / item['path']
    if item['kind'] == 'file':
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != item['sha256']:
            changed.append(item['path'])
assert not changed, changed
check = subprocess.run(['git', 'diff', '--check', '--', *result['scope']], cwd=repo, capture_output=True, text=True)
assert check.returncode == 0, check.stdout + check.stderr
backend = hashlib.sha256((repo / 'supabase/functions/mcp/index.ts').read_bytes()).hexdigest()
assert backend == '5359c2de7a28b626a3d2523d83b6fbd3e1777a0d5a60bb9757ed4bb2ee446f26', backend
tests = json.loads((repo / '.taste-skill/note-reader-final-tests-clean.json').read_text())
assert tests['success'] and tests['numFailedTests'] == 0, tests['numFailedTests']
proof = {'inspection': sys.argv[1], 'verdict': result['response']['verdict'], 'findings': 0,
         'snapshotMatches': True, 'scopedDiffCheck': 0, 'tests': tests['numPassedTests'],
         'backendUnchanged': True, 'plan_sha256': result['plan_sha256']}
(home / 'final-snapshot-proof.json').write_text(json.dumps(proof, indent=2))
print(json.dumps(proof, indent=2))
