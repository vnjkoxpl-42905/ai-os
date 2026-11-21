"""Read-only retention inventory. Never deletes; local receipts are not live proof."""
import argparse
import json
from pathlib import Path

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--stage', type=Path, required=True)
a = p.parse_args()
records = {}
for path in a.stage.glob('*/manifest.json'):
    records[path.parent.name] = json.loads(path.read_text(encoding='utf-8'))
selected = {}
for generation, manifest in sorted(records.items(), reverse=True):
    receipt = a.stage / generation / 'CLOUD-VERIFIED.json'
    if not manifest.get('complete') or not receipt.exists():
        continue
    proof = json.loads(receipt.read_text(encoding='utf-8'))
    if proof.get('complete') is True and proof.get('account') == 'contact@aspiringattorneys.com' and proof.get('generation') == generation and proof.get('files'):
        selected.setdefault(manifest['scope'], generation)
protected = set(selected.values())
pending = list(protected)
while pending:
    generation = pending.pop()
    if generation not in records:
        raise SystemExit('Missing dependency manifest: ' + generation)
    for record in records[generation]['files'].values():
        dependency = record['generation']
        if dependency not in protected:
            protected.add(dependency)
            pending.append(dependency)
print(json.dumps({'mode': 'dry-run-only', 'selected_from_local_receipts': selected,
    'protected_dependency_closure': sorted(protected),
    'review_only_other_generations': sorted(set(records) - protected),
    'directories_without_manifest_review_only': sorted(str(d.resolve()) for d in a.stage.iterdir() if d.is_dir() and not (d/'manifest.json').exists()),
    'deletion_authorized': False,
    'required_before_deletion': ['live cloud checksum and size verification for every retained dependency',
        'restore verification of retained core and personal chains',
        'explicit approval of exact absolute deletion paths']}, indent=2))
