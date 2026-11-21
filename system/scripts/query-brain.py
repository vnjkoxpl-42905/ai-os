"""Read-only, bounded retrieval from the existing compiled-knowledge catalogs."""
import argparse
import hashlib
import json
import math
import re
import time
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
INDEX = Path('system/generated/brain-search.generated.json')
CATALOGS = ('wiki/index.md', 'references/ai-workspace/index.md',
            'design/README.md', 'corpus/index.md')
ALLOWED = {'wiki', 'references', 'design', 'corpus', 'context', 'decisions'}
STOP = set('a an the is are was were what which how do does did we i my our you your '
           'to of in for and or on with from about can should where find use'.split())
SYNONYMS = {'apology': 'apology apologies', 'emails': 'email emails',
            'booking': 'booking sessions credit', 'retrieval': 'retrieval search routing',
            'retention': 'retention recall decaf cappuccino',
            'karpathy': 'karpathy tokenizer', 'secondbrain': 'second brain'}


def safe_path(root, value):
    """Resolve local Markdown only; raw bytes, credentials and external roots stay out."""
    candidate = (root / unquote(str(value))).resolve()
    try:
        relative = candidate.relative_to(root.resolve())
    except ValueError:
        return None
    if not relative.parts or relative.parts[0] not in ALLOWED:
        return None
    if candidate.suffix.lower() != '.md' or not candidate.is_file():
        return None
    if any(part in {'_snapshots', 'node_modules', '.git'} for part in relative.parts):
        return None
    return candidate


def linked_paths(root, page, text):
    targets = re.findall(r'\[\[([^]|]+)', text)
    targets += re.findall(r'\]\(([^)\n]+)\)', text)
    found = set()
    for value in targets:
        value = value.strip('<>').split('#')[0]
        if not value or '://' in value or value.startswith('#'):
            continue
        if not Path(value).suffix:
            value += '.md'
        choices = [page.parent / value, root / value]
        if '/' not in value and '\\' not in value:
            choices.append(root / 'wiki' / value)
        for choice in choices:
            resolved = safe_path(root, choice)
            if resolved:
                found.add(resolved)
                break
    return sorted(found)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build(root):
    catalogs = [root / name for name in CATALOGS if (root / name).is_file()]
    pages = set(catalogs)
    for page in catalogs:
        pages.update(linked_paths(root, page, page.read_text(encoding='utf-8-sig')))
    # Capture catalogs are navigable hubs; thousands of per-file mirrors stay out.
    rows = []
    for page in sorted(pages):
        text = page.read_text(encoding='utf-8-sig')
        title = re.search(r'^# (.+)$', text, re.M)
        front = re.match(r'---\n(.*?)\n---', text, re.S)
        metadata = front.group(1) if front else ''
        aliases = re.search(r'^aliases:\s*(.+)$', metadata, re.M)
        subject = re.search(r'^subject:\s*(.+)$', metadata, re.M)
        headings = re.findall(r'^#{2,4} (.+)$', text, re.M)
        rows.append({'path': page.relative_to(root).as_posix(),
                     'title': title.group(1) if title else page.stem,
                     'aliases': aliases.group(1) if aliases else '',
                     'subject': subject.group(1) if subject else '',
                     'headings': headings[:80], 'sha256': digest(page),
                     'mtime_ns': page.stat().st_mtime_ns, 'size': page.stat().st_size})
    return {'version': 1, 'catalogs': {p.relative_to(root).as_posix(): digest(p)
                                     for p in catalogs}, 'pages': rows}


def terms(query):
    original = [word for word in re.findall(r'[a-z0-9]+', query.lower())
                if word not in STOP]
    expanded = set(original)
    for word in original:
        expanded.update(SYNONYMS.get(word, '').split())
    return original, expanded


def rank(index, query, limit=3):
    original, expanded = terms(query)
    if not original:
        return []
    result = []
    documents = [set(re.findall(r'[a-z0-9]+',
                    f"{row['title']} {row['aliases']} {row.get('subject', '')} "
                    f"{' '.join(row['headings'])}".lower())) for row in index['pages']]
    weights = {word: 1 + math.log((len(documents) + 1) /
               (1 + sum(word in document for document in documents))) for word in expanded}
    for row in index['pages']:
        name = f"{row['title']} {row['aliases']} {row.get('subject', '')} {row['path']}".lower()
        heading = ' '.join(row['headings']).lower()
        name_words = set(re.findall(r'[a-z0-9]+', name))
        heading_words = set(re.findall(r'[a-z0-9]+', heading))
        score = sum(6 * weights[word] for word in original if word in name_words)
        score += sum(2 * weights[word] for word in original if word in heading_words)
        score += sum(weights[word] for word in expanded & name_words)
        score += sum(weights[word] for word in (expanded - set(original)) & heading_words)
        score += 15 if ' '.join(original) in name else 0
        matched = [word for word in original if word in name_words | heading_words]
        expanded_matches = sorted((expanded - set(original)) & (name_words | heading_words))
        if matched or expanded_matches:
            result.append({**row, 'score': round(score, 3), 'matched': matched,
                           'matched_expansions': expanded_matches})
    return sorted(result, key=lambda row: (-row['score'], row['path']))[:limit]


def section(text, query, max_chars):
    text = re.sub(r'\A---\n.*?\n---\n', '', text, count=1, flags=re.S)
    chunks = re.split(r'(?=^#{1,4} )', text, flags=re.M)
    original, expanded = terms(query)
    def score(chunk):
        words = set(re.findall(r'[a-z0-9]+', chunk.lower()))
        return 3 * len(set(original) & words) + len(expanded & words)
    chosen = max(chunks, key=score)
    return chosen[:max_chars], len(chosen) > max_chars


def search(root, index, query, limit=3, max_chars=1400, follow=False):
    current_catalogs = {name for name in CATALOGS if (root / name).is_file()}
    stale_catalogs = [name for name, value in index['catalogs'].items()
                      if not (root / name).is_file() or digest(root / name) != value]
    stale_catalogs += sorted(current_catalogs - set(index['catalogs']))
    stale_pages = []
    for row in index['pages']:
        page = safe_path(root, row['path'])
        if not page:
            stale_pages.append(row['path'])
            continue
        stat = page.stat()
        if stat.st_mtime_ns != row.get('mtime_ns') or stat.st_size != row.get('size'):
            stale_pages.append(row['path'])
    if stale_catalogs or stale_pages:
        return {'status': 'stale-index', 'rebuild': 'py -3.12 system/scripts/query-brain.py --build',
                'changed_catalogs': stale_catalogs, 'changed_pages': stale_pages, 'results': []}
    matches = rank(index, query, limit)
    results = []
    for match in matches:
        page = safe_path(root, match['path'])
        if not page:
            continue
        if digest(page) != match['sha256']:
            results.append({'path': match['path'], 'status': 'stale-page',
                            'rebuild': 'py -3.12 system/scripts/query-brain.py --build'})
            continue
        text = page.read_text(encoding='utf-8-sig')
        excerpt, truncated = section(text, query, max_chars)
        row = {'path': match['path'], 'title': match['title'], 'score': match['score'],
               'matched': match['matched'], 'matched_expansions': match['matched_expansions'],
               'excerpt': excerpt, 'truncated': truncated}
        if follow:
            # One hop, metadata only; the caller chooses what to open next.
            row['pointers'] = [p.relative_to(root).as_posix()
                               for p in linked_paths(root, page, excerpt)][:5]
        results.append(row)
    tied = len(matches) > 1 and matches[0]['score'] == matches[1]['score']
    return {'status': 'candidates' if results else 'not-in-compiled-index',
            'query': query, 'ambiguous_top_match': tied, 'results': results,
            'limits': 'Candidate sections are evidence pointers, not an answer or live-state verification.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('query', nargs='?')
    parser.add_argument('--build', action='store_true')
    parser.add_argument('--limit', type=int, default=3)
    parser.add_argument('--chars', type=int, default=1400)
    parser.add_argument('--follow', action='store_true')
    args = parser.parse_args()
    target = ROOT / INDEX
    if args.build:
        data = build(ROOT)
        expected = digest(target) if target.exists() else None
        output = json.dumps(data, ensure_ascii=False, indent=2) + '\n'
        target.parent.mkdir(parents=True, exist_ok=True)
        if (digest(target) if target.exists() else None) != expected:
            raise SystemExit('Index changed concurrently; rerun build.')
        target.write_text(output, encoding='utf-8')
        print(f"Indexed {len(data['pages'])} compiled pages; raw/student/export trees excluded.")
    elif args.query:
        if not target.exists():
            raise SystemExit('Index missing. Run with --build first.')
        if not 1 <= args.limit <= 10 or not 100 <= args.chars <= 5000:
            raise SystemExit('Use --limit 1..10 and --chars 100..5000.')
        started = time.perf_counter()
        result = search(ROOT, json.loads(target.read_text(encoding='utf-8')),
                        args.query, args.limit, args.chars, args.follow)
        result['elapsed_ms'] = round((time.perf_counter() - started) * 1000, 2)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        parser.error('Supply a query or --build.')


if __name__ == '__main__':
    main()
