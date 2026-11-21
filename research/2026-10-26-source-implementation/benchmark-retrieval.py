"""Repeatable local candidate benchmark; does not claim model-token savings."""
import importlib.util
import json
import statistics
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('brain', ROOT / 'system/scripts/query-brain.py')
brain = importlib.util.module_from_spec(spec)
spec.loader.exec_module(brain)

CASES = [
    ('apology emails', ['wiki/teaching-voice.md']),
    ('just taken', ['wiki/LSATU-BOOKING-POLICY.md']),
    ('ARMS applications routines memory skills', ['wiki/sources/ultimate-second-brain-arms-robonuggets.md']),
    ('Karpathy tokenizer', ['references/ai-workspace/karpathy-method.md', 'wiki/karpathy/log.md']),
    ('vocabulary unfamiliar reading', ['corpus/loophole-online/shared/README.md']),
    ('MCAT CARS questions', ['wiki/sources/mcat-cars-three-passages-2026-10-15.md']),
    ('conditional contrapositive', ['wiki/contrapositive-teaching.md', 'corpus/Curriculum/Conditional Logic/Notes/_megadoc_reference_conditionals.md']),
    ('quasarx imaginary thing', []),
]

def main():
    index = brain.build(ROOT)
    rows = []
    for query, expected in CASES:
        elapsed = []
        for _ in range(5):
            started = time.perf_counter()
            result = brain.search(ROOT, index, query, limit=3, max_chars=1400, follow=True)
            elapsed.append((time.perf_counter() - started) * 1000)
        paths = [r['path'] for r in result['results']]
        passed = bool(set(paths) & set(expected)) if expected else not paths
        chars = sum(len(r.get('excerpt', '')) for r in result['results'])
        full_chars = sum(len((ROOT / r['path']).read_text(encoding='utf-8-sig'))
                         for r in result['results'])
        rows.append({'query': query, 'expected_any_in_top3': expected,
                     'top3': paths, 'passed': passed,
                     'five_runs_ms': [round(x, 3) for x in elapsed],
                     'median_ms': round(statistics.median(elapsed), 3),
                     'returned_excerpt_characters': chars,
                     'same_candidate_full_page_characters': full_chars})
    data = {'scope': 'Hand-selected eight-case local top-three retrieval smoke benchmark; not a blind learner or model benchmark.',
            'indexed_pages': len(index['pages']), 'cases': rows,
            'passes': sum(row['passed'] for row in rows),
            'limits': 'Characters compare excerpts with the same candidate pages in full, not an equivalent rg session. Actual model tokens and end-to-end agent cost were not measured.'}
    path = ROOT / 'research/2026-10-26-source-implementation/retrieval-benchmark.json'
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"{data['passes']}/{len(rows)} cases find expected evidence or correctly miss; {data['indexed_pages']} indexed pages.")
    for row in rows:
        print(f"{row['query']}: {'PASS' if row['passed'] else 'FAIL'}, median {row['median_ms']}ms, excerpts {row['returned_excerpt_characters']} chars / full candidate pages {row['same_candidate_full_page_characters']} chars")

if __name__ == '__main__':
    main()
