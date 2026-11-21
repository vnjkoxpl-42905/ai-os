"""Check submitted artifacts once; download completed assets without clobbering."""
import hashlib
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent
CLI = 'C:/Users/Joshu/.local/bin/notebooklm.exe'
scoped = '--scoped' in sys.argv
original_order = '--original-order' in sys.argv
manifest_path = ROOT / ('original-order-video-manifest.json' if original_order else 'scoped-video-manifest.json' if scoped else 'manifest.json')
manifest = json.loads(manifest_path.read_text(encoding='utf-8-sig'))
notebook = manifest['notebook_id']
result = subprocess.run([CLI, 'artifact', 'list', '-n', notebook, '--json'], capture_output=True, text=True, encoding='utf-8')
result.check_returncode()
by_id = {a['id']: a for a in json.loads(result.stdout)['artifacts']}
for asset in manifest['assets']:
    artifact_id = asset.get('generation', {}).get('task_id')
    live = by_id.get(artifact_id)
    if not live:
        continue
    asset['status'] = live['status']
    asset['generated_title'] = live['title']
    if live['status'] != 'completed':
        continue
    extension = {'report': 'md', 'flashcards': 'json', 'quiz': 'json', 'infographic': 'png', 'video': 'mp4'}[asset['type']]
    path = ROOT / (asset['slug'] + ('-original-order' if original_order else '-scoped' if scoped else '') + '.' + extension)
    if not path.exists():
        download = subprocess.run([CLI, 'download', asset['type'], str(path), '-n', notebook, '-a', artifact_id, '--no-clobber', '--json'], capture_output=True, text=True, encoding='utf-8')
        if download.returncode:
            asset['download_error'] = download.stderr or download.stdout
            continue
    asset['path'] = str(path)
    asset['sha256'] = hashlib.sha256(path.read_bytes()).hexdigest()
    asset['bytes'] = path.stat().st_size
    asset['review_status'] = asset.get('review_status', 'Downloaded, not yet reviewed')
    print(json.dumps({'slug': asset['slug'], 'path': str(path), 'bytes': asset['bytes']}), flush=True)
manifest_path.write_text(json.dumps(manifest, indent=2), encoding='utf-8')
print(json.dumps({a['slug']: a['status'] for a in manifest['assets']}), flush=True)
