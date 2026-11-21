"""Inspect native Codex skills registry over stdio without a model turn."""
import json
from pathlib import Path
import queue
import shutil
import subprocess
import threading
import time

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]
launcher = Path.home() / 'AppData/Roaming/npm/node_modules/@openai/codex/bin/codex.js'
cmd = [shutil.which('node'), str(launcher), 'app-server', '--stdio']
events = queue.Queue()
stderr_path = OUT / 'codex-registry.stderr.txt'
with stderr_path.open('w', encoding='utf-8') as stderr:
    proc = subprocess.Popen(cmd, cwd=ROOT, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                            stderr=stderr, text=True, encoding='utf-8', errors='replace')
    def collect():
        for line in proc.stdout:
            events.put(line)
    threading.Thread(target=collect, daemon=True).start()
    transcript = []
    def send(value):
        proc.stdin.write(json.dumps(value) + '\n')
        proc.stdin.flush()
    def response(ident):
        deadline = time.monotonic() + 45
        while time.monotonic() < deadline:
            try:
                line = events.get(timeout=min(1, max(.01, deadline-time.monotonic())))
            except queue.Empty:
                if proc.poll() is not None:
                    raise RuntimeError(f'App server exited {proc.returncode}')
                continue
            transcript.append(line)
            value = json.loads(line)
            if value.get('id') == ident:
                return value
        raise TimeoutError(f'No response for {ident}')
    try:
        send({'id': 1, 'method': 'initialize', 'params': {'clientInfo': {
            'name': 'skills_audit_registry', 'version': '1.0'},
            'capabilities': {'experimentalApi': True}}})
        initialized = response(1)
        if 'error' in initialized:
            raise RuntimeError(str(initialized['error']))
        send({'method': 'initialized', 'params': {}})
        send({'id': 2, 'method': 'skills/list', 'params': {
            'cwds': [str(ROOT)], 'forceReload': True}})
        registry = response(2)
        (OUT / 'codex-registry.response.json').write_text(json.dumps(registry, indent=2), encoding='utf-8')
        groups = registry.get('result', {}).get('data', [])
        summary = {'method': 'skills/list', 'model_turn': False,
                   'cwd': str(ROOT), 'protocol_error': registry.get('error'),
                   'entries': [{'cwd': entry['cwd'], 'count': len(entry['skills']),
                                'errors': entry['errors'],
                                'repo_skills': [{'name': s['name'], 'path': s['path'], 'enabled': s['enabled']}
                                                for s in entry['skills'] if s['scope'] == 'repo']}
                               for entry in groups]}
        (OUT / 'codex-registry.receipt.json').write_text(json.dumps(summary, indent=2), encoding='utf-8')
        print(json.dumps(summary))
    finally:
        (OUT / 'codex-registry.jsonl').write_text(''.join(transcript), encoding='utf-8')
        proc.terminate()
        proc.wait(timeout=10)
