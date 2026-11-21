"""Disposable, local, source-verified Loophole full-text retrieval (stdlib only)."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sqlite3
import sys
import time
import os
import tempfile
from contextlib import contextmanager

ROOT = Path(__file__).resolve().parents[2]
HOME = ROOT / 'corpus/loophole-online'
CACHE = HOME / 'retrieval'
DB = CACHE / 'knowledge.sqlite3'
LIBRARY = HOME / 'question-database/library'
GUARDS = [HOME / 'source-catalog.generated.json', HOME / 'workouts/catalog.generated.json',
          HOME / 'routines/catalog.generated.json', LIBRARY / 'manifest.json',
          ROOT / 'raw/sources/loophole-routines-2026-10-15/prep-points.json',
          HOME / 'bootcamps/catalog.generated.json', HOME / 'bootcamps/verification.generated.json']
KINDS = ['question', 'lecture', 'notes', 'workout', 'routine', 'prep-map', 'reference', 'bootcamp']
STOP = set('a an the is are was were to of in on for and or how what why can i do me my with this that about all'.split())
ARCHIVE = ROOT / 'raw/sources/old-obsidian-vault-2026-10-07'
RELATED_ARCHIVE_NAMES = ['Assumptions & The Objection.md', 'Objection Mini-Quiz.md',
    'conditional pracitice.md', 'Conditional Practice • LO.md',
    'Clippings/Why Theres No Such Thing as Just a Detail • LO.md']


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))


def fingerprint(path):
    stat = path.stat()
    return {'size': stat.st_size, 'mtime_ns': stat.st_mtime_ns,
            'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}


def local(path):
    result = (ROOT / str(path).replace('\\', '/')).resolve()
    allowed = [HOME, ROOT / 'Loophole Lecture', ARCHIVE / 'Clippings/loophole-online']
    exact = {(ARCHIVE / name).resolve() for name in RELATED_ARCHIVE_NAMES}
    if not any(result.is_relative_to(base.resolve()) for base in allowed) and result not in exact:
        raise ValueError('Source must remain inside registered Loophole collections')
    if any(part.startswith('.') for part in result.relative_to(ROOT).parts):
        raise ValueError('Hidden files are not Loophole sources')
    return result


def citation(value):
    match = re.fullmatch(r'\s*PT\s*([A-Za-z0-9]+)[.\s]+S\s*(\d+)[.\s]+Q\s*(\d+)\s*', value, re.I)
    return f'PT{match[1]}.S{match[2]}.Q{match[3]}'.upper() if match else ''


# Ordered companion roles inside one lecture package. Presence is an exact-path
# check (never inferred from `rg --files`, which skips ignored media).
ARTIFACT_ROLES = [
    ('video.mp4', 'original video'), ('audio.m4a', 'instructor audio'),
    ('source.vtt', 'native automatic captions'), ('native-transcript.md', 'rendered caption transcript'),
    ('rendered-transcript.txt', 'rendered page transcript'), ('how-to-camo-transcript.md', 'rendered caption transcript'),
    ('ellens-notes.txt', 'written notes (text)'), ('ellens-notes.html', 'written notes (original HTML)'),
    ('notes-status.txt', 'notes availability status'), ('book-excerpt.md', 'book excerpt or availability status'),
    ('inline-bootcamp.md', 'lecture-attached quiz (observed branches)'), ('inline-bootcamp.json', 'lecture-attached quiz JSON'),
    ('source.json', 'capture record'), ('how-to-camo-source.json', 'capture record'),
    ('page.png', 'page screenshot'), ('images', 'sampled frames'), ('assets', 'page assets'),
    ('PROVENANCE.md', 'provenance'), ('SHA256SUMS', 'hash manifest'), ('verification.json', 'verification record'),
    ('README.md', 'package readme')]
GENERATIONS = {
    'rc_course_day_2026-10-14': 'RC course-day capture (Days 1-3, 6, 7); folder = Loophole Lecture/Day <N>/<title>',
    'conditional_native_2026-10-18': 'Conditional native lecture batch; folder = Loophole Lecture/Conditional Reasoning 2026-10-18/<title>',
    'rc_activity_native_2026-10-18': 'RC activity/demo native batch; folder = Loophole Lecture/RC Activity Demos 2026-10-18/<title>',
    'camo_transcript_only_2026-10-15': 'How to Camo transcript-only capture (no media); folder = Loophole Lecture/Camo',
}
# Searchable aliases: words agents and Joshua use that the source titles omit.
TERM_ALIASES = [
    (r'party trick', 'party trick partytrick PT demo'), (r'caffeinated', 'caffeinated caffeine demo'),
    (r'decaf', 'decaf decaffeinated translation'), (r'cappuccino', 'cappuccino capp translation'),
    (r'camo', 'camo camouflage'), (r'unless|few|only|and/or|some|most|condition|diagram|contrapositive',
     'conditional conditionals if then diagramming lawgic'), (r'demo', 'demo demonstration example walkthrough'),
    (r'failsafe', 'failsafe failsafes fail safe'), (r'silent', 'silent out loud progression'),
    (r'comparative', 'comparative passage A passage B'), (r'shuffle', 'reverse shuffle'),
]


def slug(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')[:120]


def aliases_for(title, kind, generation=''):
    words = {'lecture': 'video lecture captions transcript watch', 'notes': 'written notes ellen notes instructions',
             'bootcamp': 'bootcamp quiz drill questions feedback', 'workout': 'workout drill instructions',
             'routine': 'routine schedule sequence', 'question': 'question recording audio transcript CLIR',
             'prep-map': 'prep map point', 'reference': 'reference'}[kind]
    extra = [value for pattern, value in TERM_ALIASES if re.search(pattern, title, re.I)]
    day = re.search(r'Day (One|Two|Three|Six|Seven)', generation)
    return ' '.join([words] + extra + ([day[0]] if day else []))


def companions(folder):
    folder = Path(folder)
    out = []
    for name, role in ARTIFACT_ROLES:
        path = folder / name
        if path.is_file() or path.is_dir():
            count = sum(1 for _ in path.rglob('*') if _.is_file()) if path.is_dir() else None
            out.append({'role': role, 'path': str(path.resolve()), **({'files': count} if count is not None else {})})
    legacy_transcript = folder / (folder.name + '.md')
    if legacy_transcript.is_file():
        out.append({'role': 'legacy readable transcript', 'path': str(legacy_transcript.resolve())})
    return out


LECTURE_ROOT = ROOT / 'Loophole Lecture'
PACKAGE_FILES = {'source.vtt', 'ellens-notes.txt', 'inline-bootcamp.md', 'book-excerpt.md', 'how-to-camo-transcript.md'}
DAY_WORDS = {'One': 1, 'Two': 2, 'Three': 3, 'Six': 6, 'Seven': 7}


def enrich(path, meta):
    """Add identity, generation, aliases and package companions without changing source text."""
    meta = dict(meta)
    rel = path.relative_to(ROOT).as_posix()
    package = path.parent if path.name in PACKAGE_FILES and path.is_relative_to(LECTURE_ROOT) else None
    if package:
        top = package.relative_to(LECTURE_ROOT).parts[0]
        day = re.fullmatch(r'Day (\w+)', top)
        generation = meta.get('source_generation') or (
            'rc_course_day_2026-10-14' if day else 'camo_transcript_only_2026-10-15' if top == 'Camo' else top)
        meta['source_generation'] = generation
        if day:
            meta['day'] = DAY_WORDS.get(day[1], meta.get('day'))
        meta['package_folder'] = str(package.resolve())
        meta['package_artifacts'] = companions(package)
        roles = {a['role'] for a in meta['package_artifacts']}
        meta['package_media'] = {'video': 'original video' in roles, 'audio': 'instructor audio' in roles,
                                 'captions': 'native automatic captions' in roles,
                                 'written_notes': 'written notes (text)' in roles,
                                 'lecture_quiz': 'lecture-attached quiz (observed branches)' in roles}
        stem = generation + ':' + slug(package.name)
    elif meta['kind'] == 'question':
        stem = meta['citation']
    elif meta['kind'] == 'prep-map':
        stem = slug(rel)
    else:
        stem = slug(path.parent.name if path.name == 'README.md' else path.stem)
    meta['identity'] = 'loophole:' + meta['kind'] + ':' + stem
    day_alias = ('Day ' + str(meta['day']) + ' ' + next((k for k, v in DAY_WORDS.items() if v == meta['day']), '')) if meta.get('day') else ''
    meta['aliases'] = (aliases_for(meta['title'], meta['kind']) + ' ' + day_alias).strip()
    return meta


def projection_paths(folder, slug):
    if not re.fullmatch(r'[a-z0-9][a-z0-9-]{0,180}', slug):
        raise ValueError('Invalid routine prep-map source slug')
    base = folder.resolve()
    if not base.is_relative_to(HOME.resolve()):
        raise ValueError('Generated prep folder escapes Loophole home')
    path = folder / (slug + '.generated.txt')
    marker = path.with_suffix('.provenance.json')
    for candidate in [path, marker]:
        if candidate.resolve().parent != base or candidate.is_symlink():
            raise ValueError('Generated prep path escapes its owning folder')
    return path, marker


def atomic_generated_write(path, data, expected):
    """Serialized builder plus expected-byte CAS and same-folder atomic replace."""
    current = path.read_bytes() if path.exists() else None
    if current != expected:
        raise ValueError('Generated file changed concurrently: ' + str(path))
    if current == data:
        return
    parent = path.parent.resolve()
    home_map = parent == HOME.resolve() and path.name.endswith('.generated.md')
    if path.resolve().parent != parent or path.is_symlink() or not (parent.is_relative_to(CACHE.resolve()) or home_map):
        raise ValueError('Generated write escaped retrieval cache')
    with tempfile.NamedTemporaryFile(dir=parent, prefix='projection-', suffix='.tmp', delete=False) as stream:
        pending = Path(stream.name)
        stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())
    if (path.read_bytes() if path.exists() else None) != expected:
        raise ValueError('Generated file changed before replacement: ' + str(path))
    if path.parent.resolve() != parent or path.resolve().parent != parent or path.is_symlink():
        raise ValueError('Generated destination changed before replacement')
    pending.replace(path)


def sources():
    catalog = read_json(GUARDS[0])
    for row in read_json(HOME / 'bootcamps/catalog.generated.json'):
        folder = local(HOME / 'bootcamps' / row['chapter'] / row['slug'])
        related = [folder / name for name in ['source.json', 'source.html', 'images.generated.json']]
        if (folder / 'supplement-original-states.json').exists():
            related.append(folder / 'supplement-original-states.json')
        related += sorted((folder / 'assets').glob('*')) if (folder / 'assets').exists() else []
        yield folder / 'README.md', {'title': row['title'], 'kind': 'bootcamp',
            'sections': ['LR'], 'chapter': row['chapter'], 'url': row['url'],
            'status': 'captured resolved source drill; observed feedback only' if row['resolved'] else 'partial or qualified source drill',
            'captured_questions': row['questions'], 'expected_questions': row['total'],
            'source_access_limits': row.get('sourceAccessLimits', []),
            'capture_issues': row['issues'], 'related_files': [str(p.resolve()) for p in related],
            'related_fingerprints': {str(p.resolve()): fingerprint(p) for p in related}}
    for kind, key in [('workout', 'workouts'), ('routine', 'routines')]:
        for row in read_json(HOME / key / 'catalog.generated.json')[key]:
            blanks = [step['order'] for step in row.get('sequence', []) if step.get('source_blank')]
            errors = row.get('source_reference_errors', [])
            yield HOME / key / row['slug'] / 'README.md', {
                'title': row['name'], 'kind': kind, 'sections': row.get('section_types', row.get('section_impact', [])),
                'status': 'captured sourcebook; authored source gap' if blanks or errors else 'captured full sourcebook',
                'source_blank_steps': blanks, 'source_reference_errors': [dict(order=e.get('order'), status=e.get('status')) for e in errors],
                'prep_stages': row['prep_stages']}
    for row in catalog['lectures']:
        folder = local(row['folder'])
        base = {'title': row['title'], 'sections': ['RC'], 'day': row['day'],
                'notes_status': row['notes_status']}
        yield folder / 'source.vtt', dict(base, kind='lecture', status='automatic captions; unreviewed')
        if row['notes']:
            yield folder / 'ellens-notes.txt', dict(base, kind='notes', status='captured written notes')
    for row in catalog['shared_lectures']:
        yield local(row['transcript']), {'title': row['title'], 'kind': 'lecture',
            'sections': ['LR', 'RC'], 'status': 'automatic captions; unreviewed'}
    for row in catalog.get('conditional_lectures', []) + catalog.get('rc_activity_lectures', []):
        folder = local(row['folder'])
        related = [folder/name for name in ['verification.json', 'PROVENANCE.md',
                   'inline-bootcamp.json', 'book-excerpt.json'] if (folder/name).is_file()]
        base = {'title': row['title'], 'sections': row.get('sections', ['LR']), 'url': row['url'],
                'source_generation': 'rc_activity_native_2026-10-18' if 'RC Activity Demos' in row['folder'] else 'conditional_native_2026-10-18',
                'package_complete': row['complete'], 'notes_status': row['notes_status'],
                'related_files': [str(p.resolve()) for p in related],
                'related_fingerprints': {str(p.resolve()): fingerprint(p) for p in related}}
        for name, item in row['artifacts'].items():
            kind = ('lecture' if name == 'source.vtt' else 'notes' if name == 'ellens-notes.txt' else
                    'bootcamp' if name == 'inline-bootcamp.md' else 'reference')
            if name == 'native-transcript.md':
                continue  # source.vtt is the authoritative speech text; avoid duplicate results.
            status = ('automatic native captions; unreviewed' if kind == 'lecture' else
                      'captured written notes' if kind == 'notes' else
                      'observed inline questions and feedback; only observed branches' if name == 'inline-bootcamp.md' else
                      'captured book excerpt or explicit source availability status')
            yield local(item['source']), dict(base, kind=kind, artifact=name, status=status,
                source_role='lecture-attached-video-bootcamp' if kind == 'bootcamp' else name)
    for group in ['recovered_sources', 'related_recovered_notes', 'legacy_sufficient_assumption', 'batch_supplements']:
        for row in catalog[group]:
            if str(row.get('domain', '')).startswith('Excluded'):
                continue
            path = local(row['source'])
            if path.suffix.lower() not in ['.md', '.txt']:
                continue
            domain = row.get('domain', '')
            sections = ['LR'] if group == 'legacy_sufficient_assumption' or domain == 'Logical Reasoning' else (
                ['RC'] if domain == 'Reading Comprehension' else ['LR', 'RC'])
            yield path, {'title': row.get('title', path.stem), 'kind': 'reference',
                'sections': sections, 'catalog_domain': domain or None,
                'source_generation': group,
                'status': 'legacy editorial/recovered reference; not verified speech' if group != 'batch_supplements'
                    else 'capture supplement; preserve its explicit qualifications'}
    for folder in sorted((HOME / 'workouts/prep-map-points').iterdir()):
        if folder.is_dir() and (folder / 'text.txt').exists():
            record = read_json(folder / 'source.json')
            stage = folder.name.split('-')[2].upper()
            title = record.get('title') or record.get('name') or folder.name
            yield folder / 'text.txt', {'title': title + ' [' + stage + ']', 'prep_stage': stage,
                'kind': 'prep-map', 'sections': ['LR', 'RC'],
                'status': 'source error' if record.get('error') or 'error' in str(record.get('status', '')).lower()
                    else 'captured text; consult source status', 'source_status': record.get('status')}
    # Five routine-only captures have a single immutable JSON source container.
    # Publish exact text projections for independent prep-map-kind retrieval.
    prep_folder = CACHE / 'routine-prep-map'
    prep_folder.mkdir(exist_ok=True)
    source_container = GUARDS[4]
    container_fp = fingerprint(source_container)
    for record in read_json(source_container):
        path, marker = projection_paths(prep_folder, record['url'].rstrip('/').rsplit('/', 1)[-1])
        before_text = path.read_bytes() if path.exists() else None
        before_marker = marker.read_bytes() if marker.exists() else None
        body = record['text']
        expected = hashlib.sha256(body.encode('utf-8')).hexdigest()
        if path.exists() and fingerprint(path)['sha256'] != expected:
            if not marker.exists() or read_json(marker).get('generated_sha256') != fingerprint(path)['sha256']:
                raise ValueError('Generated prep text has unrecognized edits: ' + str(path))
        atomic_generated_write(path, body.encode('utf-8'), before_text)
        provenance = {'source_container': str(source_container), 'container_sha256': container_fp['sha256'],
                      'record_url': record['url'], 'generated_sha256': expected,
                      'scope': 'Exact text field, not a summary or new authored instruction'}
        atomic_generated_write(marker, (json.dumps(provenance, ensure_ascii=False, indent=2) + '\n').encode('utf-8'), before_marker)
        yield path, {'title': record['name'], 'kind': 'prep-map', 'sections': ['LR', 'RC'],
            'prep_stage': record['url'].split('/prep-map/')[1].split('/')[0].upper(),
            'status': 'captured routine-linked prep-map text', 'source_status': record.get('status'),
            'source_container': str(source_container), 'source_record_name': record['name'],
            'source_record_url': record['url'], 'source_container_sha256': container_fp['sha256'],
            'related_files': [str(marker)], 'related_fingerprints': {str(marker): fingerprint(marker)}}
    for rel in ['method-library.md', 'question-strategies.generated.md', 'reading-lectures.generated.md',
                'review-workouts.generated.md', 'worked-examples.generated.md']:
        yield HOME / rel, {'title': Path(rel).stem, 'kind': 'reference', 'sections': ['LR', 'RC'],
                          'status': 'compiled reference; source-generation qualifications apply',
                          'source_generation': 'compiled_not_source'}
    for row in read_json(LIBRARY / 'manifest.json'):
        folder = LIBRARY / row['citation'].replace('.', '/')
        related = [folder / name for name in ['original-audio.mp3', 'superwhisper-transcript.txt',
                   'superwhisper-transcript.json', 'superwhisper-transcript.srt', 'source-audio-status.json']
                   if (folder / name).exists()]
        transcript = folder / 'superwhisper-transcript.json'
        silent = (folder / 'source-audio-status.json').exists()
        status = 'digital silence; no speech' if silent else (
            'machine transcript; unreviewed' if transcript.exists() else 'no exposed recording; written CLIR only')
        audio_hash = read_json(transcript).get('audio_sha256') if transcript.exists() else None
        yield folder / 'README.md', {'title': row['citation'] + ' ' + row.get('question_type', ''),
            'kind': 'question', 'sections': ['LR'], 'citation': row['citation'],
            'old_citation': row.get('old_citation', ''), 'status': status,
            'question_type': row.get('question_type'), 'clir_type': row.get('clir_type'),
            'audio_sha256': audio_hash, 'has_audio': bool(row.get('audio_urls')),
            'audio_identity_verification': 'recorded publication identity; MP3 bytes are not rehashed during text retrieval',
            'has_transcript': transcript.exists(), 'silent': silent,
            'subtitle_status': 'available' if (folder / 'superwhisper-transcript.srt').exists()
                else ('timing exception; full text retained' if transcript.exists() else 'not applicable'),
            'related_files': [str(p.resolve()) for p in related],
            'related_fingerprints': {str(p.resolve()): fingerprint(p) for p in related if p.suffix != '.mp3'}}


@contextmanager
def build_lock():
    CACHE.mkdir(exist_ok=True)
    with (CACHE / 'build.lock').open('a+b') as lock:
        lock.seek(0)
        if sys.platform == 'win32':
            import msvcrt
            if lock.read(1) == b'':
                lock.write(b'0')
                lock.flush()
            lock.seek(0)
            try:
                msvcrt.locking(lock.fileno(), msvcrt.LK_NBLCK, 1)
            except OSError as error:
                raise ValueError('Another index builder is running') from error
            try:
                yield
            finally:
                lock.seek(0)
                msvcrt.locking(lock.fileno(), msvcrt.LK_UNLCK, 1)
        else:
            import fcntl
            fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            try:
                yield
            finally:
                fcntl.flock(lock.fileno(), fcntl.LOCK_UN)


def build():
    with build_lock():
        return build_locked()


def build_locked():
    CACHE.mkdir(exist_ok=True)
    start = time.perf_counter()
    guards = {str(p): fingerprint(p) for p in GUARDS}
    pending = CACHE / 'knowledge.building.sqlite3'
    # Rebuild only disposable generated data. Existing source files are never changed.
    connection = sqlite3.connect(pending)
    connection.executescript('DROP TABLE IF EXISTS docs; DROP TABLE IF EXISTS search; DROP TABLE IF EXISTS meta;'
        'CREATE TABLE docs(id INTEGER PRIMARY KEY,path TEXT UNIQUE,body TEXT,metadata TEXT,fingerprint TEXT);'
        'CREATE VIRTUAL TABLE search USING fts5(title,aliases,body,tokenize="unicode61");'
        'CREATE TABLE meta(key TEXT PRIMARY KEY,value TEXT);')
    counts = Counter()
    prepared = [(local(path), enrich(local(path), meta)) for path, meta in sources()]
    identity_counts = Counter(meta['identity'] for _, meta in prepared)
    records = []
    for index, (path, metadata) in enumerate(prepared, 1):
        if identity_counts[metadata['identity']] > 1:
            # Every member receives its portable discriminator; source order and
            # the checkout's machine-specific absolute root cannot change IDs.
            relative = path.relative_to(ROOT).as_posix()
            metadata['identity'] += ':' + hashlib.sha256(relative.encode()).hexdigest()[:16]
        records.append(metadata)
        before = path.stat()
        source_bytes = path.read_bytes()
        after = path.stat()
        if (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns):
            raise ValueError('Source changed during build: ' + str(path))
        body = source_bytes.decode('utf-8-sig')
        source_fp = {'size': after.st_size, 'mtime_ns': after.st_mtime_ns,
                     'sha256': hashlib.sha256(source_bytes).hexdigest()}
        connection.execute('INSERT INTO docs VALUES(?,?,?,?,?)',
            (index, str(path), body, json.dumps(metadata, ensure_ascii=False), json.dumps(source_fp)))
        connection.execute('INSERT INTO search(rowid,title,aliases,body) VALUES(?,?,?,?)',
                           (index, metadata['title'], metadata['aliases'], body))
        counts[metadata['kind']] += 1
    if guards != {str(p): fingerprint(p) for p in GUARDS}:
        raise ValueError('Catalog changed during build; rerun build')
    receipt = {'schema_version': 2, 'built_at': datetime.now(timezone.utc).isoformat(),
        'counts': dict(counts), 'documents': sum(counts.values()), 'guards': guards,
        'index_seconds': round(time.perf_counter() - start, 3),
        'prep_map_scope': '67 independently searchable prep-map records: 62 workout-linked captures '
            '(29 captured, 33 source errors) and 5 exact text projections of routine-linked captures. '
            'Routine-linked instructions also remain embedded in full routine sourcebooks.',
        'limitations': ['Local lexical retrieval, not semantic inference.',
            'Read returned source excerpts and qualified status before answering.',
            'Automatic captions and ASR are unreviewed; source errors remain explicit.',
            'Duplicate archive copies, HTML duplicates, private dictionary backups, and media bytes are not indexed.']}
    connection.execute('INSERT INTO meta VALUES(?,?)', ('receipt', json.dumps(receipt)))
    connection.commit()
    connection.close()
    pending.replace(DB)
    (CACHE / 'index-receipt.generated.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
    target = HOME / 'library-map.generated.md'
    atomic_generated_write(target, library_map(records, receipt).encode('utf-8'),
                           target.read_bytes() if target.exists() else None)
    return receipt


KNOWN_GAPS = [
    ('RC question database', 'not captured', 'The question database is LR only. RC questions appear only inside lectures and demos.'),
    ('Course Days 4 and 5', 'not captured', 'No RC course-day folders exist for Days 4 and 5.'),
    ('Day One written notes (10 of 11 lectures)', 'not checked', 'Only the Decaf notes were recovered; the rest are labeled not checked, not absent.'),
    ('How to Camo (2026-10-15 generation)', 'transcript only', 'Loophole Lecture/Camo has no media. The 2026-10-18 RC activity package holds video, audio and notes.'),
    ('RC activity demo inline quizzes', 'uncaptured', 'Attached quiz attempts were not captured; status is uncaptured, not absent.'),
    ('Bootcamp feedback branches', 'observed only', 'Only response branches that were actually clicked are captured.'),
    ('Gated external LSAT stimuli', 'gated', 'Some Bootcamp and book-excerpt stimuli were behind access gates and are recorded as unavailable.'),
    ('LR question stimuli and answer choices', 'outside capture', 'Question records hold citations, Correct CLIR and recordings, not official question text.'),
    ('Conditional quiz with stale feedback', 'unverified original', 'One historical attempt shows feedback attributed to the wrong selection; the final correct answer was verified separately.'),
    ('Automatic captions and machine transcripts', 'unreviewed', 'Fully extracted but not checked word by word against audio.'),
    ('Prep-map source errors', 'source error', '33 of 67 prep-map URLs returned errors on the source site; they are recorded, not reconstructed.'),
]


def library_map(records, receipt):
    """Generated inventory: what exists, where, how to open it and what is missing."""
    kinds = Counter((r['kind'], '+'.join(sorted(r.get('sections', [])))) for r in records)
    lines = ['---', 'type: generated', 'subject: Loophole library map (inventory, locations, gaps)',
             'generated_by: system/scripts/query-loophole.py build', 'built_at: ' + receipt['built_at'], '---', '',
             '# Loophole library map', '',
             'Generated on every `build`; do not hand-edit. Start at [AI-RETRIEVAL.md](AI-RETRIEVAL.md). '
             'This page answers **what do we have, where is it, how do I open it and what is missing**. '
             'Counts are indexed text records, not media files.', '',
             '## What we have (indexed records by kind and section)', '', '| Kind | Sections | Records |', '|---|---|---:|']
    lines += [f'| {k} | {s or "-"} | {n} |' for (k, s), n in sorted(kinds.items())]
    lines += ['', f'Total indexed records: **{len(records)}**.', '',
              '## Lecture packages by source generation', '',
              'Each lecture package is one folder. Different generations use different folder conventions; '
              'the identity `loophole:<kind>:<generation>:<folder-slug>` is stable across them.', '',
              '| Generation | Folder convention | Packages | Video | Audio | Captions | Written notes | Lecture quiz |',
              '|---|---|---:|---:|---:|---:|---:|---:|']
    packages = {}
    for r in records:
        if r.get('package_folder'):
            packages.setdefault(r['package_folder'], r)
    for generation, label in GENERATIONS.items():
        rows = [r for r in packages.values() if r.get('source_generation') == generation]
        media = lambda key: sum(r['package_media'][key] for r in rows)
        convention = label.split('; ', 1)[1] if '; ' in label else label
        lines.append(f'| {label.split(";")[0]} (`{generation}`) | {convention} | {len(rows)} | {media("video")} | '
                     f'{media("audio")} | {media("captions")} | {media("written_notes")} | {media("lecture_quiz")} |')
    lines += ['', '## Where each content type lives', '', '| Content | Navigation hub | Original files |', '|---|---|---|',
              '| RC lectures (course days) | [reading-comprehension](reading-comprehension/README.md) | `Loophole Lecture/Day <N>/<title>/` |',
              '| RC activities and demos (Caffeinated, Party Tricks, Reverse Shuffle, Camo, Mission Matching, Jail, failsafes) | [activity-demos](reading-comprehension/activity-demos.md) | `Loophole Lecture/RC Activity Demos 2026-10-18/<title>/` |',
              '| Conditional reasoning lectures and attached quizzes | [conditionals](logical-reasoning/conditionals/README.md) | `Loophole Lecture/Conditional Reasoning 2026-10-18/<title>/` |',
              '| Other LR topics | [logical-reasoning](logical-reasoning/README.md) | recovered references under `raw/sources/old-obsidian-vault-2026-10-07/Clippings/loophole-online/` |',
              '| Shared methods (Camo, RTQ, vocabulary, review) | [shared](shared/README.md) | linked per method |',
              '| Workouts (84) | [workouts](workouts/README.md) | `corpus/loophole-online/workouts/<slug>/` |',
              '| Routines (58) | [routines](routines/README.md) | `corpus/loophole-online/routines/<slug>/` |',
              '| Book Extras Bootcamps | [bootcamps](bootcamps/README.md) | `corpus/loophole-online/bootcamps/<chapter>/<slug>/`; evidence in `raw/sources/loophole-bootcamps-2026-10-18/` |',
              '| LR question records, MP3s, transcripts | [question-database](question-database/README.md) | `corpus/loophole-online/question-database/library/PT<n>/S<n>/Q<n>/` (Git-ignored) |',
              '| Every retained source with hashes | [source catalog](source-catalog.generated.md) | per row |', '',
              '## How to open a complete source', '', '```powershell',
              'python system/scripts/query-loophole.py search "<words>" --section LR|RC|shared --kind <kind> --limit 5',
              'python system/scripts/query-loophole.py open "<title, identity or citation>"',
              '```', '',
              '`open` lists every companion artifact in the package with its role (video, audio, captions, rendered transcript, '
              'written notes, book excerpt, attached quiz, frames, provenance, hashes) and the evidence status. '
              'Presence is checked by exact path, never inferred from `rg --files`, which skips ignored media.', '',
              '## What is missing or qualified', '', '| Item | Status | Meaning |', '|---|---|---|']
    lines += [f'| {a} | {b} | {c} |' for a, b, c in KNOWN_GAPS]
    no_media = sorted(r['title'] + ' (`' + r['source_generation'] + '`)' for r in packages.values() if not r['package_media']['video'])
    lines += ['', 'Lecture packages without a local video file: ' + (', '.join(no_media) if no_media else 'none') + '.', '']
    return '\n'.join(lines)


def stale(reason):
    raise ValueError('Stale or missing index: ' + reason + '. Run: python system/scripts/query-loophole.py build')


def excerpt(body, terms, cap):
    # Extract the actual source lines, never FTS markup or generated summaries.
    lines = body.splitlines()
    best = max(range(len(lines)), key=lambda i: sum(term.lower() in lines[i].lower() for term in terms), default=0)
    text = '\n'.join(lines[best:best+8])[:cap]
    return text, best + 1, best + text.count('\n') + 1


def search(query, section=None, kind=None, limit=5, cap=500):
    start = time.perf_counter()
    if not (1 <= limit <= 20 and 100 <= cap <= 2000):
        raise ValueError('limit must be 1..20; excerpt must be 100..2000')
    if not DB.exists():
        stale('build required')
    con = sqlite3.connect(DB.as_uri() + '?mode=ro', uri=True)
    try:
        receipt = json.loads(con.execute('SELECT value FROM meta WHERE key=?', ('receipt',)).fetchone()[0])
        for raw, expected in receipt['guards'].items():
            path = Path(raw)
            if not path.exists() or fingerprint(path) != expected:
                stale('catalog or publication manifest changed')
        exact = citation(query)
        tokens = re.findall(r'[^\W_]+', query, re.UNICODE)
        terms = [term for term in tokens if term.lower() not in STOP][:24]
        if not terms:
            raise ValueError('Query must contain a citation or a meaningful word')
        # Every user token is a quoted literal. FTS operators cannot execute.
        match = ' OR '.join('"' + token.replace('"', '""') + '"' for token in terms)
        where, params = [], [match]
        if section == 'shared':
            where.append('json_array_length(json_extract(d.metadata,"$.sections"))=2')
        elif section:
            where.append('EXISTS(SELECT 1 FROM json_each(json_extract(d.metadata,"$.sections")) WHERE value=?)')
            params.append(section)
        if kind:
            where.append('json_extract(d.metadata,"$.kind")=?')
            params.append(kind)
        suffix = ' AND ' + ' AND '.join(where) if where else ''
        rows = con.execute('SELECT d.*,bm25(search,8,3,1) AS rank FROM search JOIN docs d ON d.id=search.rowid '
            'WHERE search MATCH ?' + suffix + ' ORDER BY rank LIMIT 250', params).fetchall()
        # Keep the explicit instructional phrase meaningful in title ranking.
        # Otherwise stop-word removal makes "how and why decaf video" identical
        # to "decaf video", letting a progression lesson outrank the instructions.
        title_terms = terms + (['how', 'why'] if re.search(r'\bhow\s+and\s+why\b', query, re.I) else [])
        # Stage-qualified and other precise titles should beat popular repeated
        # body terms. Preserve FTS ranking to break equal title-token coverage.
        rows.sort(key=lambda row: (-sum(term.lower() in set(re.findall(r'[^\W_]+',
            json.loads(row[3])['title'].lower())) for term in title_terms), row[-1]))
        # Literal title containment wins over broad body matches. Escape LIKE's own
        # wildcard syntax so user text cannot turn this into an all-title match.
        title_query = query.strip().lower().replace('\\', '\\\\').replace('%', '\\%').replace('_', '\\_')
        titled = con.execute('SELECT *, -100000 FROM docs d WHERE lower(json_extract(metadata,"$.title")) '
            'LIKE ? ESCAPE "\\"' + suffix + ' ORDER BY length(json_extract(metadata,"$.title")) LIMIT 50',
            ['%' + title_query + '%'] + params[1:]).fetchall()
        rows = titled + rows
        if exact:
            direct = con.execute('SELECT *, -1000000 FROM docs d WHERE '
                '(upper(json_extract(metadata,"$.citation"))=? OR upper(json_extract(metadata,"$.old_citation"))=?)' +
                suffix + ' ORDER BY CASE WHEN upper(json_extract(metadata,"$.citation"))=? THEN 0 ELSE 1 END',
                [exact, exact] + params[1:] + [exact]).fetchall()
            rows = direct + rows
        seen, results = set(), []
        for row in rows:
            identifier, raw, body, raw_meta, raw_fp, _rank = row
            if identifier in seen:
                continue
            seen.add(identifier)
            path, expected = Path(raw), json.loads(raw_fp)
            if not path.exists() or fingerprint(path) != expected:
                stale('selected source changed: ' + raw)
            meta = json.loads(raw_meta)
            for related, fp in meta.pop('related_fingerprints', {}).items():
                if not Path(related).exists() or fingerprint(Path(related)) != fp:
                    stale('selected transcript evidence changed: ' + related)
            text, first, last = excerpt(body, terms, cap)
            results.append(dict(meta, source_path=raw, source_sha256=expected['sha256'],
                                excerpt=text, line_start=first, line_end=last))
            if len(results) == limit:
                break
        return {'schema_version': 1, 'query': query, 'section': section, 'kind': kind,
                'citation_match_policy': 'exact current citation precedes exact old-citation aliases; inspect both fields',
                'index_built_at': receipt['built_at'], 'elapsed_ms': round((time.perf_counter()-start)*1000, 3),
                'results': results, 'source_verified': True, 'verification_scope': 'returned text and transcript evidence only; MP3 hashes are recorded publication identities',
                'scope': 'Literal lexical OR search with title weighting; exact current/old citation first. '
                         'Catalog guards and every returned text source are verified. Read the cited file for full context.'}
    finally:
        con.close()


def open_source(query, section=None, kind=None):
    """Resolve one identity and list all of its retained companions and parallel generations."""
    if not DB.exists():
        stale('build required')
    con = sqlite3.connect(DB.as_uri() + '?mode=ro', uri=True)
    try:
        receipt = json.loads(con.execute('SELECT value FROM meta WHERE key=?', ('receipt',)).fetchone()[0])
        for raw, expected in receipt['guards'].items():
            if not Path(raw).exists() or fingerprint(Path(raw)) != expected:
                stale('catalog or publication manifest changed')
        stored = con.execute('SELECT path, metadata, fingerprint FROM docs').fetchall()
        rows = [(r[0], json.loads(r[1])) for r in stored]
        fingerprints = {r[0]: json.loads(r[2]) for r in stored}
    finally:
        con.close()
    wanted = query.strip().lower()
    exact = citation(query)
    def allowed(meta):
        return (not kind or meta['kind'] == kind) and (not section or section in meta.get('sections', []) or
                (section == 'shared' and len(meta.get('sections', [])) == 2))
    pool = [r for r in rows if allowed(r[1])]
    match = (next((r for r in pool if r[1]['identity'].lower() == wanted), None) or
             next((r for r in pool if exact and r[1].get('citation', '').upper() == exact), None) or
             next((r for r in sorted(pool, key=lambda r: (['lecture', 'workout', 'routine', 'bootcamp', 'question', 'notes',
                   'reference', 'prep-map'].index(r[1]['kind']), not (r[1].get('package_media') or {}).get('video')))
                   if r[1]['title'].lower() == wanted), None))
    resolution = 'exact identity, citation or title'
    if not match:
        hits = search(query, section, kind, 20, 100)['results']
        if not hits:
            return {'query': query, 'resolved': False, 'results': [],
                    'next_step': 'No record matched. Try an alias or check library-map.generated.md "What is missing".'}
        candidates, seen = [], set()
        # One candidate per source package, with instructional titles first for
        # short activity names. Never silently equate an activity with a routine.
        hits.sort(key=lambda h: (not h['title'].lower().startswith(('how and why', 'how to')),))
        for hit in hits:
            package = hit.get('package_folder', hit['source_path'])
            if package in seen:
                continue
            seen.add(package)
            candidates.append({k: hit[k] for k in ['identity', 'title', 'kind', 'sections', 'status',
                'source_generation', 'source_path'] if k in hit})
        if len(candidates) > 1:
            return {'query': query, 'resolved': False, 'ambiguous': True,
                    'candidates': candidates[:8], 'results': [],
                    'next_step': 'Choose the intended title or identity and run open again. Lexical OR matches '
                                 'do not prove all query terms or the requested meaning were resolved.'}
        match = next(r for r in rows if r[0] == hits[0]['source_path'])
        resolution = 'top search hit; confirm the title before relying on it'
    path, meta = match
    folder = meta.get('package_folder')
    members = [{'kind': m['kind'], 'status': m['status'], 'path': p, 'identity': m['identity']}
               for p, m in rows if folder and m.get('package_folder') == folder] or \
              [{'kind': meta['kind'], 'status': meta['status'], 'path': path, 'identity': meta['identity']}]
    for member in members:
        selected = Path(member['path'])
        if not selected.exists() or fingerprint(selected) != fingerprints[member['path']]:
            stale('selected source changed: ' + str(selected))
        member_meta = next(m for p, m in rows if p == member['path'])
        for related, expected in member_meta.get('related_fingerprints', {}).items():
            if not Path(related).exists() or fingerprint(Path(related)) != expected:
                stale('selected transcript evidence changed: ' + related)
    def core(title):
        value = '-' + slug(title) + '-'
        for junk in ['-how-and-why-to-do-', '-how-and-why-to-', '-how-to-do-', '-how-to-', '-lo-']:
            value = value.replace(junk, '-')
        return re.sub(r'^-(a|an|the)-', '-', value)
    key = core(meta['title'])
    parallel = sorted({(m['kind'], m.get('source_generation') or '-', m['title'], p) for p, m in rows
                       if p != path and m.get('package_folder', p) != folder and len(key) > 5
                       and m['kind'] not in ('question', 'prep-map') and (key in core(m['title']) or
                       (len(core(m['title'])) > 5 and core(m['title']) in key))})
    artifacts = meta.get('package_artifacts') or [{'role': 'source', 'path': path}] + [
        {'role': 'companion', 'path': p} for p in meta.get('related_files', [])]
    if meta['kind'] == 'question':
        folder_path = Path(path).parent
        roles = [('README.md', 'question source and written CLIR'), ('original-audio.mp3', 'original question audio'),
                 ('superwhisper-transcript.txt', 'machine transcript (unreviewed)'),
                 ('superwhisper-transcript.srt', 'subtitles (timing qualification in source)'),
                 ('superwhisper-transcript.json', 'native machine word data'),
                 (meta['citation'] + '.mp4', 'static title-card MP4 with original audio; not lecture video')]
        artifacts = [{'role': role, 'path': str(folder_path / name)} for name, role in roles]
    for item in artifacts:
        item['present'] = Path(item['path']).exists()
    return {'query': query, 'resolved': True, 'resolution': resolution, 'identity': meta['identity'],
            'title': meta['title'], 'kind': meta['kind'], 'sections': meta.get('sections'),
            'source_generation': meta.get('source_generation'), 'status': meta['status'],
            'package_folder': folder, 'package_media': meta.get('package_media'), 'indexed_records': members,
            'artifacts': artifacts,
            'reading_guide': reading_guide(Path(path), rows),
            'parallel_versions': [dict(zip(['kind', 'generation', 'title', 'path'], p)) for p in parallel][:15],
            'precedence': 'Parallel versions are separate formulations. Use the one the user asked for; '
                          'written notes give exact displayed wording, captions give spoken wording, workouts give the full drill. '
                          'Report material differences; never merge them silently.'}


def reading_guide(path, records):
    """A bounded locator into original headings, never a replacement procedure."""
    lines = path.read_text(encoding='utf-8-sig').splitlines()
    headings = [(i + 1, len(m[1]), m[2]) for i, line in enumerate(lines)
                if (m := re.match(r'^(#{1,6})\s+(.+)', line))]
    chosen = [(line, level, title) for line, level, title in headings
              if level <= 2 or re.match(r'Step \d+:', title)]
    outline = []
    for line, level, title in chosen[:40]:
        end = next((n - 1 for n, depth, _ in headings if n > line and depth <= level), len(lines))
        outline.append({'heading': title, 'line_start': line, 'line_end': end})
    steps = []
    for line, level, title in chosen:
        if not re.match(r'Step \d+:', title):
            continue
        item = next((o for o in outline if o['line_start'] == line), None)
        if item is None:
            break
        name = title.split(':', 1)[1].strip()
        routes = [{'identity': m['identity'], 'title': m['title'], 'path': p}
                  for p, m in records if m['kind'] == 'workout' and m['title'].strip().lower() == name.lower()]
        steps.append(dict(item, drill_routes=routes))
    return {'source_path': str(path), 'total_lines': len(lines), 'outline': outline,
            'ordered_steps': steps, 'truncated': len(chosen) > 40,
            'instruction': 'Read ordered steps in the source, preserving repetitions, timing and modifications. '
                           'Use these original heading line ranges to navigate; this outline does not replace instructions.'}


def compact_search(result):
    """CLI discovery payload; full package inventories remain in open / --details."""
    compact = dict(result, results=[])
    for original in result['results']:
        row = dict(original)
        artifacts = row.pop('package_artifacts', [])
        related = row.pop('related_files', [])
        row['artifact_count'] = len(artifacts) or 1 + len(related)
        row['open_hint'] = 'open "' + row['identity'] + '"'
        compact['results'].append(row)
    return compact


def instruction_blocks(path, kind):
    """Locate authored procedure spans; retain exact text, examples and footnotes."""
    lines = path.read_text(encoding='utf-8-sig').splitlines()
    headings = [(i, len(m[1]), m[2]) for i, line in enumerate(lines)
                if (m := re.match(r'^(#{1,6})\s+(.+)', line))]
    def span(start, level):
        return next((i for i, depth, _ in headings if i > start and depth <= level), len(lines))
    blocks = []
    def add(start, end, role):
        while end > start and not lines[end - 1].strip():
            end -= 1
        blocks.append({'role': role, 'source_path': str(path), 'line_start': start + 1,
                       'line_end': end, 'text': '\n'.join(lines[start:end])})
    if kind == 'workout':
        first = next(((i, depth) for i, depth, title in headings if title == 'Instructions'), None)
        if first:
            start, depth = first
            # Everything between Instructions and the promotional expanded
            # universe is procedural: advice, answer keys, examples and images.
            end = next((i for i, d, title in headings if i > start and
                        (title == 'The Expanded Universe' or d < depth)), len(lines))
            add(start, end, 'authored instructions, advice, examples and answer keys')
        quick = next(((i, depth) for i, depth, title in headings if title == 'Quick Facts'), None)
        if quick:
            add(quick[0], span(*quick), 'applicability and timing conditions')
        footnote = next(((i, depth) for i, depth, title in headings if title == 'Inline instruction footnotes'), None)
        if footnote:
            add(footnote[0], span(*footnote), 'instruction footnotes')
    else:
        selected = ['Routine classification', 'Quick Facts', "Ellen's Advice",
                    'Routine-specific inline footnotes', 'Additional routine instructional resources']
        for title in selected:
            heading = next(((i, d) for i, d, t in headings if t == title), None)
            if heading:
                add(heading[0], span(*heading), title)
        schedule = next(((i, d) for i, d, t in headings if t.startswith('Schedule (')), None)
        if schedule:
            add(schedule[0], span(*schedule), 'routine schedule and repetitions')
        for i, depth, title in headings:
            if not re.match(r'Step \d+:', title):
                continue
            end = span(i, depth)
            end = next((n for n in range(i, end) if lines[n].startswith('<details>')), end)
            add(i, end, 'routine-specific ordered step')
    return sorted(blocks, key=lambda b: b['line_start'])


def instructions(query, section=None, kind=None, page=1):
    if page < 1:
        raise ValueError('page must be at least 1')
    opened = open_source(query, section, kind)
    if not opened['resolved']:
        return opened
    if opened['kind'] not in ('routine', 'workout'):
        return {'query': query, 'resolved': False, 'gap': 'Instruction view supports authored routines and workouts only.',
                'identity': opened['identity'], 'next_step': 'Use open for this content type.'}
    source = Path(opened['indexed_records'][0]['path'])
    blocks = instruction_blocks(source, opened['kind'])
    gaps = []
    if opened['kind'] == 'routine':
        for step in opened['reading_guide']['ordered_steps']:
            if len(step['drill_routes']) != 1:
                gaps.append({'step': step['heading'], 'gap': 'No unique captured full workout route',
                             'candidates': step['drill_routes']})
                continue
            route = step['drill_routes'][0]
            # Direct open applies current evidence/fingerprint verification.
            workout = open_source(route['identity'])
            additions = instruction_blocks(Path(route['path']), 'workout')
            if not additions:
                gaps.append({'step': step['heading'], 'gap': 'No recognized authored instruction headings'})
            for block in additions:
                block['routine_step'] = step['heading']
                block['workout_identity'] = workout['identity']
            blocks.extend(additions)
    if not blocks:
        return {'query': query, 'resolved': False, 'gap': 'No recognized authored instructional spans; inspect full source.',
                'identity': opened['identity'], 'source_path': str(source)}
    # Paginate only at complete source-block boundaries. An individual large
    # block is returned intact and marked; instructions are never token-clipped.
    pages, current, size = [], [], 0
    for block in blocks:
        length = len(block['text'])
        if current and size + length > 24000:
            pages.append(current)
            current, size = [], 0
        current.append(block)
        size += length
    pages.append(current)
    if page > len(pages):
        raise ValueError('page exceeds available instruction pages: ' + str(len(pages)))
    return {'query': query, 'resolved': True, 'identity': opened['identity'], 'title': opened['title'],
            'kind': opened['kind'], 'status': opened['status'], 'source_path': str(source),
            'scope': 'Exact captured authored instruction/advice/example/footnote spans, not the entire sourcebook. '
                     'Routine modifications and repetitions govern linked general workout instructions.',
            'page': page, 'total_pages': len(pages), 'total_blocks': len(blocks),
            'blocks': pages[page - 1], 'gaps': gaps,
            'oversized_complete_block': any(len(b['text']) > 24000 for b in pages[page - 1]),
            'next_page_command': ('instructions "' + opened['identity'] + '" --page ' + str(page + 1))
                                 if page < len(pages) else None}


def verify():
    """Real corpus retrieval and isolated negative-boundary tests, without source mutations."""
    import subprocess
    from unittest.mock import patch
    probes = [
        ('Referential Phrasing', 'bootcamp', 'referential-phrasing/README.md', 'LR'),
        ('Accuracy Failsafe', 'workout', 'accuracy-failsafe', None),
        ('AC Primer + Decaf Routine', 'routine', 'ac-primer-plus-decaf-routine', None),
        ('Beginner Accuracy Routine (Day 1)', 'routine', 'beginner-accuracy-routine-day-1', None),
        ('How to Camo', 'lecture', 'how-to-camo-transcript', 'shared'),
        ('How and Why to Do Decaf RC Translation', 'notes', 'Decaf RC Translation', 'RC'),
        ('How and Why to Do Cappuccino RC Translation', 'notes', 'Cappuccino RC Translation', 'RC'),
        ('Main Point Question Strategy', 'lecture', 'Main Point Question Strategy', 'RC'),
        ('PT101.S2.Q1', 'question', 'PT101/S2/Q1/README.md', 'LR'),
        ('PT24.S2.Q1', 'question', 'PT101/S2/Q1/README.md', 'LR'),
        ('PT 101 S2 Q1', 'question', 'PT101/S2/Q1/README.md', 'LR'),
        ('PT2.S4.Q19', 'question', 'PT2/S4/Q19/README.md', 'LR'),
        ('PT140.S1.Q15', 'question', 'PT140/S1/Q15/README.md', 'LR'),
        ('PT1.S3.Q11', 'question', 'PT1/S3/Q11/README.md', 'LR'),
        ('conditional sa strategy teleprompter', 'reference', 'conditional-sa-strategy-teleprompter', 'LR'),
        ('disrupt your toxic habits', 'prep-map', 'disrupt-your-toxic-habits', None),
        ('Perform Disrupt Your Toxic Habits', 'prep-map', 'prep-map-perform-disrupt-your-toxic-habits', None),
        ('AC Primer + Decaf Routine', 'prep-map', 'ac-primer-plus-decaf-routine.generated.txt', None),
    ]
    checks = []
    if read_json(GUARDS[0]).get('conditional_lectures'):
        probes += [
            ('How to Diagram Unless', 'lecture', 'How to Diagram Unless/source.vtt', 'LR'),
            ('The Three Valid Some Most Inferences', 'lecture', 'The Three Valid Some & Most Inferences/source.vtt', 'LR'),
        ]
    if read_json(GUARDS[0]).get('rc_activity_lectures'):
        probes += [
            ('Caffeinated RC Translation Demo PT135 S3 P3 Passage A', 'lecture', 'Caffeinated RC Translation Demo - PT135.S3.P3 Passage A/source.vtt', 'RC'),
            ('How and Why to Do a Reverse Shuffle', 'lecture', 'How and Why to Do a Reverse Shuffle/source.vtt', 'RC'),
        ]
    for query, kind, expected, section in probes:
        result = search(query, section, kind, 5, 500)
        found = [row for row in result['results'] if expected.lower() in row['source_path'].replace('\\', '/').lower()]
        assert found, (query, [row['title'] for row in result['results']])
        if kind == 'question' or query == 'Accuracy Failsafe':
            assert expected.lower() in result['results'][0]['source_path'].replace('\\', '/').lower(), query
        for row in result['results']:
            source = Path(row['source_path']).read_text(encoding='utf-8-sig').splitlines()
            assert '\n'.join(source[row['line_start']-1:row['line_end']]).startswith(row['excerpt'])
            assert len(row['excerpt']) <= 500
        checks.append({'query': query, 'kind': kind, 'passed': True, 'elapsed_ms': result['elapsed_ms'],
                       'matched_source': found[0]['source_path'], 'status': found[0]['status']})
    # Realistic phrasing (aliases, not displayed titles) must reach the right source.
    realistic = [
        ('decaf video', 'RC', 'lecture', 'Day One/'),
        ('how and why decaf video', 'RC', 'lecture', 'How and Why to Do Decaf RC Translation/source.vtt'),
        ('party trick demo video', 'RC', 'lecture', 'Party Trick/source.vtt'),
        ('caffeinated failsafes', 'RC', None, 'Caffeinated RC Translation Drill Failsafes'),
        ('Day 6 cappuccino', 'RC', 'lecture', 'Day Six'),
        ('unless quiz', 'LR', 'bootcamp', 'nless'),
        ('Mission Matching', None, None, 'ission'),
        ('camo video', None, 'lecture', 'RC Activity Demos 2026-10-18/How to Camo/source.vtt'),
    ]
    for query, section, kind, expected in realistic:
        result = search(query, section, kind, 5, 500)
        found = [r for r in result['results'] if expected.lower() in r['source_path'].replace('\\', '/').lower()]
        assert found, ('realistic', query, [r['title'] for r in result['results']])
        if query == 'how and why decaf video':
            assert result['results'][0] == found[0], ('instructional title ranking', query)
        checks.append({'query': query, 'kind': kind, 'passed': True, 'realistic_alias': True,
                       'elapsed_ms': result['elapsed_ms'], 'matched_source': found[0]['source_path']})
    # `open` must route a concept to every retained companion, across generations.
    opened = open_source('How to Camo')
    assert opened['package_media']['video'] and opened['source_generation'] == 'rc_activity_native_2026-10-18'
    assert any(p['generation'] == 'camo_transcript_only_2026-10-15' for p in opened['parallel_versions'])
    assert any(p['kind'] == 'workout' for p in opened['parallel_versions'])  # Camo Review stays separate
    shuffle = open_source('Reverse Shuffle')
    assert shuffle['kind'] == 'workout' and any(p['kind'] == 'lecture' for p in shuffle['parallel_versions'])
    unless = open_source('How to Diagram Unless', kind='lecture')
    roles = {a['role'] for a in unless['artifacts']}
    assert {'original video', 'instructor audio', 'native automatic captions', 'lecture-attached quiz (observed branches)'} <= roles
    assert all(a['present'] for a in unless['artifacts'])
    decaf = open_source('How and Why to Do Decaf RC Translation', kind='lecture')
    assert decaf['source_generation'] == 'rc_course_day_2026-10-14' and decaf['package_media']['video']
    assert any(a['role'] == 'legacy readable transcript' and a['present'] for a in decaf['artifacts'])
    assert open_source('PT101.S2.Q1')['identity'] == 'loophole:question:PT101.S2.Q1'
    assert open_source('Referential Phrasing', kind='bootcamp')['artifacts'][0]['present']
    # Use absent tokens: real words such as "spoof" may legitimately occur in
    # source bodies and therefore match this intentionally lexical OR search.
    assert not open_source('zzqx qvvzzj kkkzzq')['resolved']
    ambiguous = open_source('Decaf')
    assert not ambiguous['resolved'] and ambiguous['ambiguous']
    assert any(c['title'] == 'How and Why to Do Decaf RC Translation' for c in ambiguous['candidates'])
    rehab = open_source('The Conditional Rehab Routine')['reading_guide']
    assert [s['heading'] for s in rehab['ordered_steps']] == [
        'Step 1: Unless Practice Routine', 'Step 2: Question Stem Training',
        'Step 3: Acronym LR Section', 'Step 4: Unofficial Diagramming Marathon']
    assert all(s['drill_routes'] for s in rehab['ordered_steps'])
    question_artifacts = open_source('PT101.S2.Q1')['artifacts']
    assert all(a['present'] for a in question_artifacts)
    assert any('static title-card' in a['role'] and a['path'].endswith('.mp4') for a in question_artifacts)
    assert any(a['path'].endswith('.mp3') for a in question_artifacts)
    assert any(a['path'].endswith('.srt') for a in question_artifacts)
    full = search('Decaf', 'RC', 'lecture')
    compact = compact_search(full)
    assert all('package_artifacts' not in r and r['open_hint'] and r['artifact_count'] for r in compact['results'])
    assert all('package_artifacts' in r for r in full['results'])
    checks.append({'query': 'agent discovery usability', 'passed': True,
                   'checked': ['compact search preserves full internal payload', 'Decaf ambiguity candidates',
                               'source-derived ordered routine guide', 'question audio/subtitles/title-card artifacts']})
    procedure = instructions('The Conditional Rehab Routine', kind='routine')
    all_blocks = [b for p in range(1, procedure['total_pages'] + 1)
                  for b in instructions(procedure['identity'], page=p)['blocks']]
    assert not procedure['gaps']
    for block in all_blocks:
        original_lines = Path(block['source_path']).read_text(encoding='utf-8-sig').splitlines()
        assert block['text'] == '\n'.join(original_lines[block['line_start'] - 1:block['line_end']])
    procedure_text = '\n'.join(b['text'] for b in all_blocks)
    for condition in ['3+ sections', "don't spoil them", 'New Sections Only', 'three sections in a row',
                      '11.', 'Unless ~B, ~A.', 'Footnote']:
        assert condition in procedure_text, ('missing instructional condition', condition)
    stem = instructions('Question Stem Training', kind='workout')
    stem_text = '\n'.join(b['text'] for b in stem['blocks'])
    assert 'Previously Seen Sections' in stem_text and 'Full Tests' in stem_text and 'Footnote 1' in stem_text
    assert 'The Expanded Universe' not in stem_text
    assert instructions('Decaf')['ambiguous']
    checks.append({'query': 'exact instruction views', 'passed': True,
                   'checked': ['routine order and conditional qualifications', 'four full linked workouts',
                               'source-exact spans', 'footnotes and examples', 'workout instructions without promotional bulk']})
    checks.append({'query': 'open routes', 'passed': True,
                   'checked': ['Camo generations + workout', 'Reverse Shuffle workout->lecture', 'Unless package media + quiz',
                               'Decaf course-day video', 'question citation identity', 'bootcamp source', 'unresolved query']})
    # Confirm special content dispositions and data references with their actual files.
    silent = search('PT2.S4.Q19', kind='question', limit=1)['results'][0]
    assert silent['silent'] and not silent['has_transcript']
    assert 'timing exception' in search('PT140.S1.Q15', kind='question', limit=1)['results'][0]['subtitle_status']
    blank = search('Beginner Accuracy Routine (Day 1)', kind='routine', limit=1)['results'][0]
    assert 3 in blank['source_blank_steps'] or any(e['order'] == 3 for e in blank['source_reference_errors'])
    failed = search('Perform Disrupt Your Toxic Habits', kind='prep-map', limit=1)['results'][0]
    assert failed['status'] == 'source error' and failed['prep_stage'] == 'PERFORM'
    con = sqlite3.connect(DB)
    no_audio = json.loads(con.execute('SELECT metadata FROM docs WHERE json_extract(metadata,"$.has_audio")=0 LIMIT 1').fetchone()[0])
    no_recording = search(no_audio['citation'], kind='question', limit=1)['results'][0]
    assert not no_recording['has_audio'] and 'no exposed recording' in no_recording['status']
    hashes = con.execute('SELECT json_extract(metadata,"$.audio_sha256"),count(*) FROM docs '
                         'WHERE json_extract(metadata,"$.audio_sha256") IS NOT NULL GROUP BY 1 HAVING count(*)>1 LIMIT 1').fetchone()
    assert hashes and hashes[1] > 1
    assert con.execute('SELECT count(*) FROM docs WHERE path LIKE ?', ('%Just a Detail%',)).fetchone()[0] == 1  # named related note only; excluded SQL migration omitted
    for domain, expected_sections in [('Logical Reasoning', ['LR']), ('Reading Comprehension', ['RC'])]:
        known = con.execute('SELECT metadata FROM docs WHERE json_extract(metadata,"$.catalog_domain")=?', (domain,)).fetchall()
        assert known and all(json.loads(row[0])['sections'] == expected_sections for row in known)
    con.close()
    for invalid in ['.env', '../../outside.md', 'raw/data-about-me/private.md']:
        try:
            local(invalid)
        except ValueError:
            continue
        raise AssertionError('Path boundary accepted: ' + invalid)
    for invalid in ['../escape', 'C:\\escape', 'valid\\escape', 'valid:escape']:
        try:
            projection_paths(CACHE / 'routine-prep-map', invalid)
        except ValueError:
            continue
        raise AssertionError('Projection path boundary accepted: ' + invalid)
    existing_projection = next((CACHE / 'routine-prep-map').glob('*.generated.txt'))
    try:
        atomic_generated_write(existing_projection, b'not written', b'simulated stale expected bytes')
    except ValueError as error:
        assert 'changed concurrently' in str(error)
    else:
        raise AssertionError('Generated-file CAS failed to reject stale expected bytes')
    original = fingerprint
    target = Path(silent['source_path'])
    def drift(path):
        fp = original(path)
        return dict(fp, sha256='simulated-stale') if path == target else fp
    with patch(__name__ + '.fingerprint', side_effect=drift):
        try:
            search('PT2.S4.Q19', kind='question', limit=1)
        except ValueError as error:
            assert 'Stale' in str(error)
        else:
            raise AssertionError('Selected-source drift was not rejected')
        for query in [silent['citation'], silent['identity']]:
            try:
                open_source(query)
            except ValueError as error:
                assert 'Stale' in str(error)
            else:
                raise AssertionError('Direct open source drift was not rejected: ' + query)
    with patch(__name__ + '.fingerprint', return_value={'sha256': 'simulated-stale'}):
        try:
            search('Camo')
        except ValueError as error:
            assert 'Stale' in str(error)
        else:
            raise AssertionError('Catalog drift was not rejected')
    assert search('" OR " * NOT title:secret', kind='workout', limit=1)['source_verified']
    latencies = []
    for query in ['How to Camo', 'Accuracy Failsafe', 'PT24.S2.Q1']:
        started = time.perf_counter()
        run = subprocess.run([sys.executable, str(Path(__file__).resolve()), 'search', query, '--limit', '1'],
                             capture_output=True, encoding='utf-8', check=True)
        assert json.loads(run.stdout)['results']
        latencies.append(round((time.perf_counter()-started)*1000, 3))
    proof = {'verified_at': datetime.now(timezone.utc).isoformat(), 'passed': True,
             'query_code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'probes': checks,
             'negative_tests': ['outside/secret path rejected', 'selected-source drift rejected', 'direct open source drift rejected', 'catalog drift rejected',
                                'literal FTS operator text cannot execute query syntax',
                                'source-derived projection path escape rejected', 'generated-file stale expected-byte CAS rejected'],
             'dispositions_checked': ['silent source', 'subtitle timing exceptions', 'no exposed recording',
                                      'shared audio hash retains individual question identities', 'excluded SQL migration omitted',
                                      'authored routine blank/reference gap remains explicit', 'known LR and RC recovered domains remain separated'],
             'cli_end_to_end_ms': latencies, 'cli_median_ms': sorted(latencies)[1]}
    (CACHE / 'query-proof.generated.json').write_text(json.dumps(proof, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return proof


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    commands.add_parser('build')
    commands.add_parser('verify')
    command = commands.add_parser('search')
    command.add_argument('query')
    command.add_argument('--section', choices=['LR', 'RC', 'shared'])
    command.add_argument('--kind', choices=KINDS)
    command.add_argument('--limit', type=int, default=5, help='1 to 20 results (default 5)')
    command.add_argument('--excerpt', type=int, default=500, help='100 to 2000 characters per excerpt')
    command.add_argument('--details', action='store_true', help='Include full artifact inventories (legacy payload)')
    opener = commands.add_parser('open', help='Resolve a title, identity or citation and list every companion artifact')
    opener.add_argument('query')
    opener.add_argument('--section', choices=['LR', 'RC', 'shared'])
    opener.add_argument('--kind', choices=KINDS)
    instructor = commands.add_parser('instructions', help='Read exact authored workout/routine instructions, examples and footnotes')
    instructor.add_argument('query')
    instructor.add_argument('--section', choices=['LR', 'RC', 'shared'])
    instructor.add_argument('--kind', choices=['routine', 'workout'])
    instructor.add_argument('--page', type=int, default=1, help='Complete-block page (never clips an instruction)')
    args = parser.parse_args()
    try:
        if args.command == 'search' and not (1 <= args.limit <= 20 and 100 <= args.excerpt <= 2000):
            raise ValueError('limit must be 1..20; excerpt must be 100..2000')
        result = (build() if args.command == 'build' else verify() if args.command == 'verify' else
                  instructions(args.query, args.section, args.kind, args.page) if args.command == 'instructions' else
                  open_source(args.query, args.section, args.kind) if args.command == 'open' else
                  search(args.query, args.section, args.kind, args.limit, args.excerpt))
        if args.command == 'search' and not args.details:
            result = compact_search(result)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (ValueError, OSError, sqlite3.Error) as error:
        print(json.dumps({'error': str(error), 'results': []}, ensure_ascii=False))
        return 1
    return 0


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    raise SystemExit(main())
