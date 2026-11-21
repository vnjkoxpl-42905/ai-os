"""Index downloaded public teaching clips in the same NotebookLM for narration QA."""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CLI = 'C:/Users/Joshu/.local/bin/notebooklm.exe'
original_order = '--original-order' in sys.argv
manifest_path = ROOT / ('original-order-video-manifest.json' if original_order else 'scoped-video-manifest.json')
manifest = json.loads(manifest_path.read_text())
def run(args):
    response = subprocess.run([CLI, *args], capture_output=True, text=True, encoding='utf-8')
    if response.returncode:
        raise RuntimeError(response.stderr or response.stdout)
    return json.loads(response.stdout)
for asset in manifest['assets']:
    if not asset.get('path'):
        continue
    if not asset.get('narration_source_id'):
        response = run(['source', 'add', asset['path'], '-n', manifest['notebook_id'], '--type', 'file', '--mime-type', 'video/mp4', '--json'])
        asset['narration_source_id'] = response.get('source', response).get('id')
        manifest_path.write_text(json.dumps(manifest, indent=2))
    narration_path = ROOT / (asset['slug'] + ('-original-order' if original_order else '-scoped') + '-narration.json')
    if narration_path.exists():
        continue
    try:
        run(['source', 'wait', asset['narration_source_id'], '-n', manifest['notebook_id'], '--timeout', '45', '--interval', '15', '--json'])
        narration = run(['source', 'fulltext', asset['narration_source_id'], '-n', manifest['notebook_id'], '--json'])
        narration_path.write_text(json.dumps(narration, ensure_ascii=False, indent=2), encoding='utf-8')
        asset['narration_path'] = str(narration_path)
        print(json.dumps({'slug': asset['slug'], 'narration': narration.get('content')}), flush=True)
    except RuntimeError as error:
        asset['narration_error'] = str(error)
    manifest_path.write_text(json.dumps(manifest, indent=2))
