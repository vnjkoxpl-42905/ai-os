"""Back up and remove only the known, missing Orca Codex hook registrations."""
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile
from datetime import datetime, timezone

target = Path.home() / '.codex' / 'hooks.json'
missing = Path.home() / '.orca' / 'agent-hooks' / 'codex-hook.cmd'
backup_dir = Path(sys.argv[1])
if missing.exists():
    raise SystemExit('Orca target exists; refusing to change hooks')
original = target.read_bytes()
doc = json.loads(original)
events = doc['hooks']
removed = 0
for event, groups in list(events.items()):
    kept = []
    for group in groups:
        commands = group.get('hooks', [])
        matched = [h for h in commands if h.get('command', '').replace('\\', '/').lower() == str(missing).replace('\\', '/').lower()]
        if matched:
            if len(commands) != 1 or len(group) != 1 or len(matched) != 1:
                raise SystemExit(f'Unexpected mixed registration for {event}; no change made')
            removed += 1
        else:
            kept.append(group)
    if kept:
        events[event] = kept
    else:
        del events[event]
if removed != 9:
    raise SystemExit(f'Expected 9 registrations, found {removed}; no change made')
backup_dir.mkdir(parents=True, exist_ok=True)
stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
backup = backup_dir / f'codex-hooks-{stamp}.json'
with backup.open('xb') as f:
    f.write(original)
digest = hashlib.sha256(original).hexdigest()
if hashlib.sha256(backup.read_bytes()).hexdigest() != digest:
    raise SystemExit('Backup verification failed; no change made')
new = (json.dumps(doc, indent=2, ensure_ascii=False) + '\n').encode('utf-8')
if target.read_bytes() != original:
    raise SystemExit(f'Target changed after backup; no change made. Backup: {backup}')
fd, tmp = tempfile.mkstemp(prefix='hooks-repair-', suffix='.json', dir=target.parent)
with os.fdopen(fd, 'wb') as f:
    f.write(new)
    f.flush()
    os.fsync(f.fileno())
if target.read_bytes() != original:
    raise SystemExit(f'Target changed during preparation; no change made. Prepared file: {tmp}')
os.replace(tmp, target)
if target.read_bytes() != new:
    raise SystemExit('Post-write verification failed')
print(f'Backup: {backup}\nOriginal SHA256: {digest}\nNew SHA256: {hashlib.sha256(new).hexdigest()}\nOrca registrations removed: {removed}')
