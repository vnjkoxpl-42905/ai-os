import argparse
import hashlib
import json
import shutil
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('--dest', required=True)
args = parser.parse_args()
source = Path(__file__).resolve().parent
dest = Path(args.dest).resolve()
expected = Path('C:/Users/Joshu/dev/ai-os-projects/lsatu-conditional-pages-20261003').resolve()
if dest != expected:
    raise SystemExit('Destination must be the authorized isolated build checkout.')
manifest = json.loads((source / 'manifest.json').read_text(encoding='utf-8-sig'))
for item in manifest:
    relative = Path(item['path'])
    original = source / relative
    target = (dest / relative).resolve()
    if not target.is_relative_to(dest) or not original.resolve().is_relative_to(source):
        raise SystemExit('Path escaped its authorized root.')
    if hashlib.sha256(original.read_bytes()).hexdigest() != item['sha256']:
        raise SystemExit(f'Source changed: {relative}')
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(original, target)
print(f'Imported {len(manifest)} hash-verified current files. No deletion or commit.')
