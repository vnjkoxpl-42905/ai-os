import argparse
import hashlib
import json
import subprocess
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('--repo', required=True)
parser.add_argument('--output', required=True)
args = parser.parse_args()
repo = Path(args.repo).resolve()
source = Path(__file__).resolve().parent
manifest = json.loads((source / 'manifest.json').read_text(encoding='utf-8-sig'))
known = {item['path']: item for item in manifest}
changed = subprocess.check_output(['git', '-C', str(repo), 'diff', '--name-only', '67230dfae74a1466515d570fcb7b8a96ab5cb9c5'], text=True).splitlines()
untracked = subprocess.check_output(['git', '-C', str(repo), 'ls-files', '--others', '--exclude-standard'], text=True).splitlines()
rows = []
for relative in sorted(set(changed + untracked)):
    target = (repo / relative).resolve()
    if not target.is_relative_to(repo):
        raise SystemExit('Changed path escaped checkout.')
    original = source / relative
    if not target.is_file():
        status = 'deleted-or-nonfile'
    elif relative not in known:
        status = 'new-builder-file'
    elif target.read_bytes() == original.read_bytes():
        status = 'unchanged-import'
    elif target.read_bytes().replace(b'\r\n', b'\n') == original.read_bytes().replace(b'\r\n', b'\n'):
        status = 'newline-only-import'
    else:
        status = 'builder-revision'
    rows.append({'path': relative, 'status': status, 'sha256': hashlib.sha256(target.read_bytes()).hexdigest() if target.is_file() else None})
result = {'repo': str(repo), 'rows': rows, 'revisionFiles': [r for r in rows if r['status'] not in ('unchanged-import', 'newline-only-import')]}
Path(args.output).write_text(json.dumps(result, indent=2), encoding='utf-8')
print(json.dumps({'revisionFiles': result['revisionFiles'], 'imports': len(rows) - len(result['revisionFiles'])}, indent=2))
