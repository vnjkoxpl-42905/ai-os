"""Materialize a selected generation into a NEW folder; never overwrite live data."""
import argparse, hashlib, json, zipfile, uuid, os
from pathlib import Path
p = argparse.ArgumentParser()
p.add_argument('--generation', required=True)
p.add_argument('--output', required=True)
a = p.parse_args()
generation = Path(a.generation).resolve()
output = Path(a.output).resolve()
if os.name=='nt': output=Path('\\\\?\\'+str(output))
if output.exists(): raise SystemExit('Output must be a new folder, preventing overwrite.')
manifest = json.loads((generation / 'manifest.json').read_text(encoding='utf-8'))
if not manifest['complete']: raise SystemExit('Generation has capture errors; inspect manifest first.')
output.mkdir(parents=True)
archives = {}
for key, record in manifest['files'].items():
    target = (output / key).resolve()
    if not target.is_relative_to(output): raise SystemExit('Unsafe archive path')
    origin = record['generation']
    if origin not in archives:
        origin_dir = generation.parent / origin
        payload = origin_dir / 'payload.zip'
        if not payload.exists():
            parts = json.loads((origin_dir / 'parts-manifest.json').read_text())
            payload = origin_dir / 'reassembled-payload.zip'
            if payload.exists():
                existing = hashlib.sha256()
                with payload.open('rb') as src:
                    while chunk := src.read(1024 * 1024): existing.update(chunk)
                if existing.hexdigest() == parts['archive_sha256']:
                    archives[origin] = zipfile.ZipFile(payload)
                    # Skip reassembly of an already verified complete archive.
                    target.parent.mkdir(parents=True, exist_ok=True)
                    digest = hashlib.sha256()
                    with archives[origin].open(key) as src, target.open('xb') as dst:
                        while chunk := src.read(1024 * 1024): digest.update(chunk); dst.write(chunk)
                    if digest.hexdigest() != record['sha256']: raise SystemExit('Checksum mismatch: '+key)
                    continue
                payload = origin_dir / ('reassembled-payload-'+uuid.uuid4().hex+'.zip')
            full = hashlib.sha256()
            with payload.open('xb') as dst:
                for part in parts['parts']:
                    path = origin_dir / part['name']
                    if not path.exists(): path = origin_dir / 'cloud-parts' / part['name']
                    digest_part = hashlib.sha256()
                    with path.open('rb') as src:
                        while chunk := src.read(1024 * 1024):
                            full.update(chunk); digest_part.update(chunk); dst.write(chunk)
                    if digest_part.hexdigest() != part['sha256']: raise SystemExit('Part checksum mismatch')
            if full.hexdigest() != parts['archive_sha256']: raise SystemExit('Whole archive checksum mismatch')
        archives[origin] = zipfile.ZipFile(payload)
    target.parent.mkdir(parents=True, exist_ok=True)
    digest = hashlib.sha256()
    with archives[origin].open(key) as src, target.open('xb') as dst:
        while chunk := src.read(1024 * 1024):
            digest.update(chunk); dst.write(chunk)
    if digest.hexdigest() != record['sha256']: raise SystemExit('Checksum mismatch: ' + key)
for archive in archives.values(): archive.close()
print('Verified materialization complete:', len(manifest['files']), 'files in', output)
