import hashlib
import json
from pathlib import Path
import subprocess

repo = Path('C:/Users/Joshu/dev/ai-os-projects/lsatu-conditional-bootcamp')
proof = Path(__file__).parent
base = '67230dfae74a1466515d570fcb7b8a96ab5cb9c5'
scope = ['src/App.tsx', 'src/bootcamps/conditionals', 'src/components/teacher/ConditionalAssignmentFields.tsx', 'src/components/teacher/ConditionalAssignmentFields.test.tsx', 'src/lib/conditionalBootcampAssignment.ts', 'src/lib/conditionalBootcampAssignment.test.ts', 'src/dev/ConditionalOpeningPreview.tsx']
protected = {
    'public/data/_bank.generated.json': '69f34f6dc7c1c2772d0fc212851873ca92a6c0a40e15af83e97b56575e004f75',
    'public/data/finder-address-index.json': '3f8216dacc9a968b6e4e19da90472b8591b32204f912dcf97ed87459b5406007',
    'supabase/functions/mcp/index.ts': 'f731b29c4fcd1517dc99276a998944494a86720e0cd103061e1799d149c7d32c',
}
def git(*args):
    return subprocess.check_output(['git', *args], cwd=repo)
def sha(data):
    return hashlib.sha256(data).hexdigest()

tracked = git('diff', '--name-only', base, '--', *scope).decode().splitlines()
untracked = git('ls-files', '--others', '--exclude-standard', '--', *scope).decode().splitlines()
diff = git('diff', '--binary', base, '--', *scope)
assert not any(name in protected for name in tracked + untracked)
for name, expected in protected.items():
    assert sha((repo / name).read_bytes()) == expected, name
source = Path('C:/Users/Joshu/dev/ai-os/raw/sources/conditional-reasoning-voice-standard/conditional_reasoning_transcription.html')
assert sha(source.read_bytes()) == '13afbb1ecd2d4b0f80ca918d1956690e16493b1addbf273314c9c1124ad380cb'
bundle = '\n'.join(path.read_text(encoding='utf-8') for path in (repo / 'dist/assets').glob('*.js'))
assert 'conditional-opening-preview' not in bundle
for term in ['opening-2026-10-02-v2', 'Personalized If/Then', 'What Test']:
    assert term in bundle, term
prior = proof / 'final-host-snapshot.json'
historical = proof / 'host-snapshot-before-ci3.json'
if prior.exists() and not historical.exists():
    historical.write_bytes(prior.read_bytes())
snapshot = {
    'base': base, 'date': '2026-10-02',
    'independent_verdict': 'FI4 corrections await fresh final inspection5',
    'scoped_diff_sha256': sha(diff),
    'files': {name: sha((repo / name).read_bytes()) for name in tracked + untracked},
    'protected_unchanged': protected,
    'source_html_sha256': sha(source.read_bytes()),
    'production_bundle_guard': 'DEV preview excluded; fixed edition and named methods present',
    'scope': scope,
}
(proof / 'scoped-tracked.diff').write_bytes(diff)
(proof / 'scoped-untracked.txt').write_text('\n'.join(untracked) + '\n', encoding='utf-8')
prior.write_text(json.dumps(snapshot, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'tracked': len(tracked), 'untracked': len(untracked), 'diff_sha256': sha(diff), 'protected_unchanged': True, 'source_unchanged': True}))
