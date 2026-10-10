"""Copy newline transport receipts and hash the preserved Step 3 evidence."""
from pathlib import Path
import hashlib
import json
import shutil

root = Path(__file__).resolve().parent
source = Path(r'C:\Users\Joshu\AppData\Local\Temp\claude\C--Users-Joshu-dev-ai-os\699dc587-39bd-4a08-a0c2-306235d0ae46\scratchpad\step3\audit-codex')
target = root / 'artifacts' / 'audit-codex'
names = [p.name for p in source.glob('*-lf.sql')] + ['newline-transport-receipt.json']
for name in names:
    src, dst = source / name, target / name
    if dst.exists() and dst.read_bytes() != src.read_bytes():
        raise RuntimeError(f'Existing evidence differs: {name}')
    if not dst.exists():
        shutil.copy2(src, dst)
    if src.read_bytes() != dst.read_bytes():
        raise RuntimeError(f'Copy verification failed: {name}')
lines = []
for path in sorted(root.rglob('*')):
    if path.is_file() and path.name != 'SHA256SUMS':
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        lines.append(f'{digest}  {path.relative_to(root).as_posix()}')
(root / 'SHA256SUMS').write_bytes(('\n'.join(lines) + '\n').encode('utf-8'))
print(json.dumps({'transport_files_copied': len(names), 'hashed_files': len(lines)}))
