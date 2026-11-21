"""Correct only PT119-S2-Q19's obsolete bank match, difficulty and features."""
from pathlib import Path
import csv
import hashlib
import io
import json
import sys

root = Path(__file__).resolve().parent
inventory = root.parent / 'revamp-inventory.csv'
before = inventory.read_bytes()
lines = before.decode('utf-8').splitlines(keepends=True)
header = next(csv.reader([lines[0]]))
matches = [i for i, line in enumerate(lines[1:], 1) if next(csv.reader([line]))[0] == 'PT119-S2-Q19']
if len(matches) != 1:
    raise RuntimeError('Expected one inventory row')
index = matches[0]
old_row = dict(zip(header, next(csv.reader([lines[index]]))))
expected = {'bank_match': 'moved:PT103-S2-Q24', 'difficulty': '3', 'features': '2-Speaker; Causal Difference-Maker; Principles in Answers'}
if any(old_row[k] != v for k, v in expected.items()):
    raise RuntimeError('Inventory row changed; stop')
bank = next(x['question'] for x in json.loads((root / 'live-bank-source.json').read_text(encoding='utf-8')) if x['qid'] == 'PT119-S2-Q19')
db = next(x for x in json.loads((root / 'initial-live-snapshot.json').read_text(encoding='utf-8'))['sources']['structuredContent']['rows'] if x['qid'] == 'PT119-S2-Q19')
if bank['stimulus'] != db['stimulus'] or bank['questionStem'] != db['prompt'] or bank['correctAnswer'] != db['correct_choice'] or any(bank['answerChoices'][c['letter']] != c['text'] for c in db['choices']):
    raise RuntimeError('Bank and live DB do not match')
new_fields = {'bank_match': 'Y', 'difficulty': str(bank['questionDifficulty']), 'features': '; '.join(bank['questionFeatures'])}
new_row = {**old_row, **new_fields}
stream = io.StringIO(newline='')
csv.writer(stream, lineterminator='\r\n' if lines[index].endswith('\r\n') else '\n').writerow([new_row[k] for k in header])
lines[index] = stream.getvalue()
after = ''.join(lines).encode('utf-8')
receipt = {'qid': db['qid'], 'old_fields': expected, 'new_fields': new_fields, 'unchanged_fields': all(old_row[k] == new_row[k] for k in header if k not in new_fields), 'before_sha256': hashlib.sha256(before).hexdigest(), 'after_sha256': hashlib.sha256(after).hexdigest(), 'applied': '--apply' in sys.argv}
if receipt['applied']:
    snapshot = root / 'revamp-inventory-before.csv'
    if snapshot.exists() and snapshot.read_bytes() != before:
        raise RuntimeError('Existing snapshot differs')
    snapshot.write_bytes(before)
    if inventory.read_bytes() != before:
        raise RuntimeError('Inventory changed during preparation')
    inventory.write_bytes(after)
    if inventory.read_bytes() != after:
        raise RuntimeError('Inventory readback differs')
    (root / 'inventory-receipt.json').write_bytes((json.dumps(receipt, indent=2) + '\n').encode('utf-8'))
print(json.dumps(receipt))
