"""Compile original reviewed lesson text; do not alter downloaded evidence."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
slugs = ['01-what-conditionals-are', '02-why-direction-matters', '03-sufficient-means-enough', '04-necessary-means-required']
parts = []
for slug in slugs:
    text = (ROOT / (slug + '-original-order-source.md')).read_text(encoding='utf-8')
    text = '\n\n'.join(paragraph for paragraph in text.split('\n\n') if not paragraph.startswith(('Visual:', 'Show all ready orders')))
    parts.append(text.strip())
for slug in ['05-group-one', '06-group-two']:
    text = (ROOT / (slug + '-source.md')).read_text(encoding='utf-8')
    text = text.replace('Where there is smoke, there is fire.', 'Where a pickup light is green, an order is ready.')
    text = text.replace('Where there is smoke.', 'Where a pickup light is green.')
    text = text.replace('Smoke → Fire', 'Pickup light is green → Order is ready')
    parts.append(text.strip())
notes = '# Conditional opening: original examples\n\nReviewed teaching draft for Joshua. Original pickup-order scenario replaces dog/mammal examples. Compiled from the authorized opening draft and corrected lesson sources, not a verbatim third-party lesson.\n\n' + '\n\n---\n\n'.join(parts)
(ROOT / 'opening-notes-reviewed-original.md').write_text(notes, encoding='utf-8')
print('Compiled original opening notes.')
