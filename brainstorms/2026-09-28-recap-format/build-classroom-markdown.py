from pathlib import Path
import html
import re

root = Path(__file__).parent
source = (root / '07-quantity-statements-lesson.md').read_text(encoding='utf-8')
source = re.sub(r'^# Some, Most, and All\s*\n', '', source, count=1)
source = re.sub(r'^!\[(.*?)\]\([^\n]+\)$', '', source, flags=re.M)
source = re.sub(r'<details><summary>[^<]+</summary>', '\n**Worked answer**\n', source)
source = source.replace('</details>', '')
source = source.replace('before opening the answers', 'before reading the answers')
source = re.sub(r'\n{3,}', '\n\n', source).strip() + '\n'
if '<details' in source or '![' in source:
    raise RuntimeError('Unconverted local-only content')
(root / '09-quantity-statements-classroom.md').write_text(source, encoding='utf-8')
page = '<!doctype html><meta charset="utf-8"><title>Classroom transfer</title><textarea style="width:98vw;height:90vh">' + html.escape(source) + '</textarea>'
(root / '09-quantity-statements-transfer.html').write_text(page, encoding='utf-8')
print(f'Classroom note prepared: {len(source)} characters')
