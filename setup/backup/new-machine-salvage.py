"""Validate a historical socket-failed capture; optionally create a new derivative.

Never changes the source generation. This is historical recovery, not a current capture.
"""
import argparse
import hashlib
import json
import stat
import time
import zipfile
from pathlib import Path

SOCKETS = {'app-server-control.sock', 'daemon-updater.sock'}

def validate_errors(manifest):
    errors = manifest.get('errors', [])
    if len(errors) != 2:
        raise ValueError('Exactly two known runtime socket errors required')
    names = set()
    for error in errors:
        path = Path(error['path'])
        names.add(path.name)
        if path.name not in SOCKETS or '.codex' not in path.parts:
            raise ValueError('Unexpected error path')
        if 'Invalid argument' not in error.get('error', ''):
            raise ValueError('Unexpected error type')
        if getattr(path.stat(), 'st_reparse_tag', 0) != 0x80000023:
            raise ValueError('Runtime socket not confirmed as Windows AF_UNIX')
    if names != SOCKETS:
        raise ValueError('Duplicate socket errors')

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--generation', type=Path, required=True)
    parser.add_argument('--report', type=Path, required=True)
    parser.add_argument('--create', action='store_true', help='Create derivative only after all validation passes')
    args = parser.parse_args()
    original = args.generation.resolve()
    raw = (original / 'manifest.json').read_bytes()
    manifest = json.loads(raw)
    if manifest.get('complete') is not False or manifest.get('scope') != 'core':
        raise ValueError('Only incomplete core capture supported')
    validate_errors(manifest)
    grouped = {}
    for key, record in manifest['files'].items():
        if Path(key).is_absolute() or '..' in Path(key).parts:
            raise ValueError('Unsafe key')
        origin = record['generation']
        if Path(origin).name != origin:
            raise ValueError('Unsafe generation')
        grouped.setdefault(origin, {})[key] = record
    verified = []
    for origin, required in sorted(grouped.items()):
        directory = original.parent / origin
        baseline = json.loads((directory / 'manifest.json').read_text())
        if any(baseline['files'].get(k) != v for k, v in required.items()):
            raise ValueError('Dependency manifest mismatch')
        archive = directory / 'payload.zip'
        digest = hashlib.sha256()
        with archive.open('rb') as source:
            while chunk := source.read(4 * 1024 * 1024):
                digest.update(chunk)
        if digest.hexdigest() != baseline['archive_sha256']:
            raise ValueError('Archive SHA256 mismatch: ' + origin)
        with zipfile.ZipFile(archive) as zipped:
            names = zipped.namelist()
            if len(names) != len(set(names)):
                raise ValueError('Duplicate ZIP entries')
            if origin == original.name and set(names) != set(required):
                raise ValueError('Unexpected/missing source ZIP entries')
            for key, record in required.items():
                digest = hashlib.sha256()
                size = 0
                with zipped.open(key) as source:
                    while chunk := source.read(1024 * 1024):
                        digest.update(chunk)
                        size += len(chunk)
                if digest.hexdigest() != record['sha256'] or size != record['size']:
                    raise ValueError('File checksum mismatch: ' + key)
        verified.append({'generation': origin, 'files_sha256_crc_verified': len(required)})
        print(json.dumps(verified[-1]), flush=True)
    if (original / 'manifest.json').read_bytes() != raw:
        raise RuntimeError('Source manifest changed during audit')
    report = {'historical_source': str(original), 'source_manifest_sha256': hashlib.sha256(raw).hexdigest(),
              'verified_dependencies': verified, 'excluded_errors': manifest['errors'],
              'warning': 'Historical capture only; does not represent current machine state'}
    if args.create:
        stamp = time.strftime('%Y%m%d-%H%M%S')
        target = original.parent / stamp
        target.mkdir(exist_ok=False)
        with zipfile.ZipFile(target / 'payload.zip', 'x'):
            pass
        checksum = hashlib.sha256((target / 'payload.zip').read_bytes()).hexdigest()
        derived = dict(manifest, generation=stamp, complete=True, errors=[],
                       archive_sha256=checksum, archive_bytes=(target / 'payload.zip').stat().st_size,
                       recovery_provenance=report)
        (target / 'manifest.json').write_text(json.dumps(derived, indent=2))
        (target / 'SHA256SUMS.txt').write_text(checksum + '  payload.zip\n')
        report['derivative'] = str(target)
    args.report.write_text(json.dumps(report, indent=2))
    print(json.dumps(report), flush=True)

if __name__ == '__main__':
    main()
