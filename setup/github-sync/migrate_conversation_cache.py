"""Hide generated transcript exports from Obsidian without changing cloud paths."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess

from sync import is_link, process_lock


def manifest(root):
    """Hash regular files only; refuse links anywhere in the generated tree."""
    if is_link(root):
        raise RuntimeError('Generated cache root is a link')
    result = {}
    def reject_walk_error(error):
        raise error

    for directory, dirs, files in os.walk(
            root, followlinks=False, onerror=reject_walk_error):
        current = Path(directory)
        for name in dirs + files:
            if is_link(current / name):
                raise RuntimeError('Generated cache contains a link')
        for name in files:
            path = current / name
            digest = hashlib.sha256()
            with path.open('rb') as stream:
                for chunk in iter(lambda: stream.read(1024 * 1024), b''):
                    digest.update(chunk)
            result[path.relative_to(root).as_posix()] = {
                'bytes': path.stat().st_size, 'sha256': digest.hexdigest()}
    return result


def migrate(state):
    """Caller must hold runner.lock and sync.lock with Obsidian closed."""
    state = Path(state)
    if is_link(state):
        raise RuntimeError('State directory is a link')
    state = state.resolve(strict=True)
    old, new = state / 'conversations', state / '.conversations'
    for path in (old, new):
        if path.parent != state or path.resolve().parent != state:
            raise RuntimeError('Cache path escapes the state directory')
        if path.exists() and is_link(path):
            raise RuntimeError('Cache path is a link')
    if new.exists():
        if old.exists():
            raise RuntimeError('Both cache locations exist; resolve explicitly')
        return {'status': 'already-migrated', 'destination': str(new)}
    if not old.is_dir():
        return {'status': 'no-visible-cache'}
    before = manifest(old)
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
    receipt = state / ('conversation-cache-migration-' + stamp + '.json')
    record = {'source': str(old), 'destination': str(new), 'files': before,
              'status': 'prepared'}
    receipt.write_text(json.dumps(record, indent=2) + '\n', encoding='utf-8')
    old.rename(new)
    try:
        if manifest(new) != before:
            raise RuntimeError('Post-rename hashes differ')
    except Exception:
        # Never overwrite another directory while rolling back.
        if old.exists():
            raise RuntimeError('Verification failed; rollback destination occupied')
        new.rename(old)
        raise
    record['status'] = 'verified'
    receipt.write_text(json.dumps(record, indent=2) + '\n', encoding='utf-8')
    return {'status': 'verified', 'files': len(before),
            'bytes': sum(item['bytes'] for item in before.values()),
            'source': str(old), 'destination': str(new), 'receipt': str(receipt)}


def main():
    if os.name == 'nt':
        check = subprocess.run(
            ['powershell', '-NoProfile', '-Command',
             "if (Get-Process -Name Obsidian -ErrorAction SilentlyContinue) { exit 1 }"],
            capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW)
        if check.returncode:
            raise RuntimeError('Close Obsidian before migrating')
    state = Path(__file__).resolve().parent / 'state'
    with process_lock(state / 'runner.lock') as runner:
        if not runner:
            raise RuntimeError('Sync runner is busy; no migration performed')
        with process_lock(state / 'sync.lock') as sync:
            if not sync:
                raise RuntimeError('Snapshot publisher is busy; no migration performed')
            print(json.dumps(migrate(state), indent=2))


if __name__ == '__main__':
    main()
