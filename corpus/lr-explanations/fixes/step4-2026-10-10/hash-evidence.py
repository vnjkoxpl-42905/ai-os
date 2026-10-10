import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / 'SHA256SUMS'


def files():
    return sorted(
        (path for path in ROOT.rglob('*') if path.is_file()
         and path != MANIFEST and '__pycache__' not in path.relative_to(ROOT).parts),
        key=lambda path: path.relative_to(ROOT).as_posix(),
    )


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


mode = sys.argv[1] if len(sys.argv) > 1 else 'verify'
if mode == 'generate':
    content = ''.join(digest(path) + '  ' + path.relative_to(ROOT).as_posix() + '\n' for path in files())
    MANIFEST.write_bytes(content.encode('utf-8'))
elif mode != 'verify':
    raise SystemExit('Usage: python -I hash-evidence.py generate|verify')

expected = {}
for line in MANIFEST.read_text(encoding='utf-8').splitlines():
    sha, relative = line.split('  ', 1)
    if relative in expected:
        raise SystemExit('Duplicate manifest path: ' + relative)
    expected[relative] = sha
actual = {path.relative_to(ROOT).as_posix(): digest(path) for path in files()}
if expected != actual:
    mismatches = sorted(name for name in set(expected) | set(actual) if expected.get(name) != actual.get(name))
    raise SystemExit('Hash verification failed: ' + ', '.join(mismatches))
print(f'Verified {len(actual)} files; manifest excluded; __pycache__ excluded')
