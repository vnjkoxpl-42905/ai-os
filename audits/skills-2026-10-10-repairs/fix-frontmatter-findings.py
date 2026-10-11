from pathlib import Path
import hashlib
import json
import re

OUT=Path(__file__).parent
errors=json.loads((OUT/'FINAL-VERIFICATION.json').read_text(encoding='utf-8'))['errors']
ledger=OUT/'frontmatter-final-receipts.json'
rows=json.loads(ledger.read_text(encoding='utf-8')) if ledger.exists() else []
for error in errors:
    if not error.startswith('Frontmatter '):
        continue
    name=error[len('Frontmatter '):].split(': mapping values',1)[0]
    p=Path(name)
    before=p.read_bytes()
    text=before.decode('utf-8')
    match=re.search(r'^description:\s*(.*)$',text,re.M)
    if not match:
        raise RuntimeError('Missing description: '+str(p))
    text=text[:match.start()]+ 'description: '+json.dumps(match.group(1))+text[match.end():]
    backup=OUT/'backups/frontmatter-final'/hashlib.sha256(str(p).encode()).hexdigest()[:20]/p.name
    backup.parent.mkdir(parents=True,exist_ok=True)
    backup.write_bytes(before)
    if p.read_bytes()!=before:
        raise RuntimeError('Concurrent edit')
    p.write_text(text,encoding='utf-8')
    rows.append(dict(path=str(p),backup=str(backup),before_sha256=hashlib.sha256(before).hexdigest(),after_sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
ledger.write_text(json.dumps(rows,indent=2),encoding='utf-8')
print(len(rows),'descriptions quoted')
