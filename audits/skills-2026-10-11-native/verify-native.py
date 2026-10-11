"""Read back actual native events and changed-file hashes; no service calls."""
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]

def events(name):
    return [json.loads(line) for line in (HERE / name).read_text(encoding='utf-8').splitlines()]

registry = json.loads((HERE / 'codex-registry.response.json').read_text())['result']['data'][0]
assert not registry['errors']
repo = [s for s in registry['skills'] if s.get('scope') == 'repo']
assert len(repo) == 37 and all(s['enabled'] and Path(s['path']).is_file() for s in repo)

claude = events('claude-triggers.jsonl')
init = next(e for e in claude if e.get('subtype') == 'init')
expected = ['ingest', 'second-brain-query', 'second-brain-lint', 'transcript-intake',
            'karpathy-teach', 'persona-agent-creator', 'session-handoff', 'claudex-loop',
            'codex-build', 'codex-review', 'research-deep', 'bootcamp-parity-audit']
assert all(n in init['slash_commands'] for n in expected)

def tool_blocks(es):
    return [b for e in es for b in e.get('message', {}).get('content', []) if isinstance(b, dict)]

for filename, names in [
    ('claude-triggers.jsonl', ['second-brain-query', 'second-brain-lint']),
    ('claude-dependencies.jsonl', ['research-deep', 'bootcamp-parity-audit',
                                'karpathy-teach', 'persona-agent-creator'])]:
    blocks = tool_blocks(events(filename))
    for name in names:
        call = next(b for b in blocks if b.get('type') == 'tool_use'
                    and b.get('name') == 'Skill' and b.get('input', {}).get('skill') == name)
        result = next(b for b in blocks if b.get('type') == 'tool_result'
                      and b.get('tool_use_id') == call['id'])
        assert not result.get('is_error'), (filename, name)

codex_loads = {}
for filename, names in [
    ('codex-triggers.jsonl', ['second-brain-query', 'second-brain-lint']),
    ('codex-dependencies.jsonl', ['research-deep', 'bootcamp-parity-audit', 'karpathy-teach']),
    ('codex-persona-path.jsonl', ['persona-agent-creator'])]:
    commands = [e['item'] for e in events(filename) if e.get('type') == 'item.completed'
                and e.get('item', {}).get('type') == 'command_execution']
    for name in names:
        assert any(c.get('exit_code') == 0 and 'name: ' + name in c.get('aggregated_output', '')
                   for c in commands), (filename, name)
        codex_loads[name] = filename

hooks = [e for e in events('watch-preflight/claude-native-after.jsonl')
         if e.get('subtype') == 'hook_response']
assert len(hooks) == 2 and all(e['exit_code'] == 0 and not e['output'] for e in hooks)

hashes = {}
for path in [ROOT / 'audits/skills-2026-10-11-dependencies/dependency-receipts.json',
             HERE / 'watch-preflight/receipts.json',
             HERE / 'watch-preflight/claude-global-receipts.json',
             HERE / 'watch-preflight/whisper-root-receipts.json']:
    data = json.loads(path.read_text(encoding='utf-8'))
    for row in data['edits'] if isinstance(data, dict) else data:
        hashes[row['path']] = row.get('after_sha256', row.get('after'))
for path, expected_hash in hashes.items():
    assert hashlib.sha256(Path(path).read_bytes()).hexdigest() == expected_hash, path

result = dict(registry_entries=len(registry['skills']), project_skills=len(repo),
              claude_core_names=len(expected), claude_successful_skill_calls=6,
              codex_successful_entrypoint_reads=codex_loads, silent_native_startup_hooks=len(hooks),
              verified_changed_payload_files=len(hashes), errors=[],
              limits=['Explicit loads and routing samples are not every production workflow.',
                      'Codex description budget remains bounded; no full automatic-selection certification.'])
(HERE / 'FINAL-VERIFICATION.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
print(json.dumps(result, indent=2))
