"""Publish verified LR reading deliverables locally, preserving Desktop originals."""
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
from urllib.parse import unquote
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
SOURCE = Path.home() / 'Desktop/Loophole LR Recordings'
TARGET = ROOT / 'corpus/loophole-online/question-database/library'
EXPECTED = {}

def generated_write(path, content):
    """Compare and swap a generated output without overwriting a concurrent edit."""
    previous = path.read_bytes() if path.exists() else None
    expected = EXPECTED.get(str(path), hashlib.sha256(previous).hexdigest() if previous is not None else None)
    if (hashlib.sha256(previous).hexdigest() if previous is not None else None) != expected:
        raise RuntimeError(f'Generated output changed since preflight: {path}')
    data = content.encode('utf-8')
    if previous == data:
        return
    import tempfile
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as handle:
        handle.write(data)
        temporary = Path(handle.name)
    if (path.read_bytes() if path.exists() else None) != previous:
        raise RuntimeError(f'Concurrent generated-output edit preserved: {path}')
    temporary.replace(path)

def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()

def verify():
    saved = json.loads((TARGET / 'publication-manifest.json').read_text(encoding='utf-8'))
    for item in saved['files']:
        relative = Path(item['path'])
        assert not relative.is_absolute() and '..' not in relative.parts
        assert sha(SOURCE / item.get('source_path', item['path'])) == item['sha256'] == sha(TARGET / relative), item['path']
    page = (TARGET / 'index.html').read_text(encoding='utf-8')
    data = json.loads(re.search(r'<script id="data" type="application/json">(.*?)</script>', page, re.S).group(1))
    counts = data['counts']
    assert counts['questions'] == 5015 and counts['audio_questions'] == 713
    assert counts['s1_transcript_questions'] == 712 and counts['s1_subtitles_questions'] == 710
    assert counts['unique_audio_recordings'] == 659 and counts['silent_source_questions'] == 1
    assert counts['s1_text_without_valid_subtitles_questions'] == 2
    links = 0
    for row in data['rows']:
        for href in [row['readme']] + [item['href'] for group in row['links'].values() for item in group]:
            local = TARGET / unquote(href)
            assert not re.match(r'^[a-z]+:', href, re.I) and local.resolve().is_relative_to(TARGET.resolve()) and local.is_file(), href
            links += 1
        text = (TARGET / unquote(row['readme'])).read_text(encoding='utf-8')
        for transcript in row['transcripts']:
            assert transcript['text'].strip() in text
    assert 'C:/Users/' not in page and 'C:\\\\Users\\\\' not in page
    generated = [TARGET / name for name in ['manifest.json', 'build-library-index.py', 'index.html', 'INDEX.md', 'PUBLICATION.md']]
    generated.extend(TARGET / unquote(row['readme']) for row in data['rows'])
    views = [{'path': path.relative_to(TARGET).as_posix(), 'sha256': sha(path)} for path in generated]
    if saved.get('regenerated_views'):
        assert saved['regenerated_views'] == views, 'Generated publication changed since publication'
    else:
        saved['regenerated_views'] = views
        saved['source_manifest_sha256'] = sha(SOURCE / 'manifest.json')
        generated_write(TARGET / 'publication-manifest.json', json.dumps(saved, indent=2))
    result = {'status': 'passed', 'verified_at': datetime.now(timezone.utc).isoformat(), 'publisher_sha256': sha(Path(__file__)), 'copied_files_rehashed_against_both_roots': len(saved['files']), 'reader_local_links': links, 'counts': counts, 'all_current_transcripts_inline_in_question_files': True, 'reader_has_no_absolute_desktop_paths': True}
    generated_write(TARGET / 'publication-verification.json', json.dumps(result, indent=2))
    print(json.dumps(result))

def main():
    if '--check-safety' in sys.argv:
        from unittest.mock import Mock, patch
        path = Mock()
        path.parent = TARGET
        path.exists.return_value = True
        path.read_bytes.side_effect = [b'old generated view', b'concurrent edit']
        handle = Mock()
        handle.name = str(TARGET / 'mock-never-created.tmp')
        manager = Mock()
        manager.__enter__ = Mock(return_value=handle)
        manager.__exit__ = Mock(return_value=False)
        with patch('tempfile.NamedTemporaryFile', return_value=manager):
            try:
                generated_write(path, 'new generated view')
            except RuntimeError as error:
                assert 'Concurrent generated-output edit preserved' in str(error)
            else:
                raise AssertionError('CAS failed to reject concurrent edit')
        path.read_bytes.side_effect = None
        path.read_bytes.return_value = b'edit during source copy'
        EXPECTED[str(path)] = hashlib.sha256(b'original preflight bytes').hexdigest()
        try:
            generated_write(path, 'new generated view')
        except RuntimeError as error:
            assert 'changed since preflight' in str(error)
        else:
            raise AssertionError('Preflight CAS failed to reject long-copy concurrent edit')
        print(json.dumps({'generated_compare_and_swap_conflict': 'rejected', 'preflight_to_write_conflict': 'rejected', 'filesystem_mutations_in_mock': 0}))
        return
    if '--verify' in sys.argv:
        verify()
        return
    assert SOURCE.is_dir() and TARGET.resolve().is_relative_to(ROOT.resolve())
    rows = json.loads((SOURCE / 'manifest.json').read_text(encoding='utf-8-sig'))
    assert len(rows) == 5015
    TARGET.mkdir(parents=True, exist_ok=True)
    assert TARGET.resolve().is_relative_to(ROOT.resolve())
    previous_manifest = TARGET / 'publication-manifest.json'
    if previous_manifest.exists():
        prior = json.loads(previous_manifest.read_text(encoding='utf-8'))
        known_generated = {item['path'] for item in prior.get('regenerated_views', [])}
        for item in prior.get('regenerated_views', []):
            assert sha(TARGET / item['path']) == item['sha256'], f'Generated output edited; preserved: {item["path"]}'
        candidates = ['manifest.json', 'build-library-index.py', 'index.html', 'INDEX.md', 'PUBLICATION.md'] + [str(Path(*row['citation'].split('.')) / 'README.md').replace('\\', '/') for row in rows]
        for relative in candidates:
            assert not (TARGET / relative).exists() or relative in known_generated, f'Unknown generated output preserved: {relative}'
    else:
        assert not any((TARGET / name).exists() for name in ['manifest.json', 'build-library-index.py', 'index.html', 'INDEX.md', 'PUBLICATION.md']), 'Existing unowned generated output preserved'
        candidates = ['manifest.json', 'build-library-index.py', 'index.html', 'INDEX.md', 'PUBLICATION.md'] + [str(Path(*row['citation'].split('.')) / 'README.md').replace('\\', '/') for row in rows]
    for relative in candidates + ['publication-manifest.json', 'publication-write-baseline.json']:
        path = TARGET / relative
        EXPECTED[str(path)] = sha(path) if path.exists() else None
    view_baselines = {str((TARGET / relative).resolve()): EXPECTED[str(TARGET / relative)] for relative in candidates}
    ignore = TARGET / '.gitignore'
    expected_ignore = '# Local licensed source publication. Never upload these captures.\n*\n!.gitignore\n'
    if ignore.exists() and ignore.read_text() != expected_ignore:
        raise RuntimeError('Existing publication ignore policy differs')
    ignore.write_text(expected_ignore)
    inventory = []
    def copy(relative, destination=None):
        destination = destination or relative
        src, dst = SOURCE / relative, TARGET / destination
        assert src.is_file() and not src.is_symlink()
        assert src.resolve().is_relative_to(SOURCE.resolve()) and dst.resolve().is_relative_to(TARGET.resolve())
        digest = sha(src)
        if dst.exists() and sha(dst) != digest:
            raise RuntimeError(f'Publication conflict, existing bytes preserved: {relative}')
        dst.parent.mkdir(parents=True, exist_ok=True)
        if not dst.exists():
            shutil.copy2(src, dst)
        assert sha(dst) == digest
        inventory.append({'path': destination.as_posix(), 'source_path': relative.as_posix(), 'bytes': src.stat().st_size, 'sha256': digest})
    for name in ['source-coverage.json', 'citation-validation.json', 'library-verification.json']:
        copy(Path(name))
    for name in ['manifest.json', 'build-library-index.py']:
        copy(Path(name), Path('provenance') / name)
    for row in rows:
        citation = row['citation']
        assert re.fullmatch(r'[A-Za-z0-9-]+\.S\d+\.Q\d+', citation)
        relative = Path(*citation.split('.'))
        folder = SOURCE / relative
        for name in ['metadata.json', 'correct-clir.txt', 'download.json', 'original-audio.mp3', 'superwhisper-transcript.txt', 'superwhisper-transcript.json', 'superwhisper-transcript.srt', 'source-audio-status.json', 'source-audio-status.txt', citation + '.mp4', citation + '.mp4.json']:
            if (folder / name).is_file():
                copy(relative / name)
    local_rows = []
    for row in rows:
        local = dict(row)
        local['audio_urls'] = ['original-audio.mp3'] if row.get('audio_urls') else []
        local.pop('url', None)
        local_rows.append(local)
    generated_write(TARGET / 'manifest.json', json.dumps(local_rows, ensure_ascii=False, indent=2))
    builder = (SOURCE / 'build-library-index.py').read_text(encoding='utf-8-sig')
    old = "processed = path.parent / ('superwhisper-audio' + suffix + '.wav')"
    assert builder.count(old) == 1
    builder = builder.replace(old, "processed = path.parent / ('original-audio' + suffix + '.mp3')  # Published MP3 bytes verified in publication-manifest.json")
    builder = builder.replace('[Pipeline instructions](PIPELINE.md)', '[Publication policy and provenance](PUBLICATION.md)')
    builder = builder.replace(r"& '.\.venv\Scripts\python.exe' '.\build-library-index.py'", 'python build-library-index.py')
    builder = builder.replace('    path.parent.mkdir(parents=True, exist_ok=True)\n', '    path.parent.mkdir(parents=True, exist_ok=True)\n    previous_bytes = path.read_bytes() if path.exists() else None\n', 1)
    builder = builder.replace('import argparse\n', 'import argparse\nimport hashlib\n', 1)
    builder = builder.replace('def write(path, content):\n', "_PUBLICATION_BASELINES = json.loads((Path(__file__).parent / 'publication-write-baseline.json').read_text(encoding='utf-8'))\n\ndef write(path, content):\n", 1)
    builder = builder.replace('    previous_bytes = path.read_bytes() if path.exists() else None\n', "    previous_bytes = path.read_bytes() if path.exists() else None\n    current_hash = hashlib.sha256(previous_bytes).hexdigest() if previous_bytes is not None else None\n    if current_hash != _PUBLICATION_BASELINES.get(str(path.resolve())):\n        raise RuntimeError('Generated view changed since publication preflight: ' + str(path))\n", 1)
    builder = builder.replace('    temporary.replace(path)\n', "    if (path.read_bytes() if path.exists() else None) != previous_bytes:\n        raise RuntimeError('Concurrent generated view edit preserved: ' + str(path))\n    temporary.replace(path)\n", 1)
    generated_write(TARGET / 'build-library-index.py', builder)
    generated_write(TARGET / 'publication-write-baseline.json', json.dumps(view_baselines, indent=2))
    subprocess.run([sys.executable, str(TARGET / 'build-library-index.py'), '--root', str(TARGET)], check=True, capture_output=True, text=True)
    # The builder has already CAS-published all reader and question views.
    generated_write(TARGET / 'PUBLICATION.md', '# Local LR source publication\n\nThis is the canonical reading copy inside the Loophole folder. Open [the searchable reader](index.html) or [the question index](INDEX.md). All navigation and media links are relative.\n\nDesktop originals remain unchanged and serve as the processing archive. Current clean-dictionary transcripts, original MP3s, valid SRT files, native timestamp JSON, written CLIR, captured metadata and existing MP4 derivatives are copied byte for byte. Per-question README files and the reader are regenerated from those bytes.\n\nPersonal dictionaries, virtual environments, models, runtime logs, processing WAVs, caches, obsolete transcript generations and credentials are deliberately excluded. Those source files remain on Desktop. Full text is distinct from subtitle validity. One recording is verified digital silence; two speech recordings have invalid source timing but complete text. All transcripts remain machine-generated and unreviewed.\n\n[Publication hashes](publication-manifest.json) record each copied file. The original evidence verification is retained in library-verification.json. This entire generated local publication is excluded from Git. To refresh, run the maintained system/scripts/publish-loophole-question-library.py from the vault; conflicting existing evidence fails closed instead of being overwritten.\n')
    derived_paths = [TARGET / name for name in ['manifest.json', 'build-library-index.py', 'index.html', 'INDEX.md', 'PUBLICATION.md']]
    derived_paths.extend(TARGET.joinpath(*row['citation'].split('.')) / 'README.md' for row in rows)
    derived = [{'path': path.relative_to(TARGET).as_posix(), 'sha256': sha(path)} for path in derived_paths]
    report = {'generated_at': datetime.now(timezone.utc).isoformat(), 'source': str(SOURCE), 'target': str(TARGET), 'status': 'copied_and_sha256_verified', 'source_unchanged': True, 'source_manifest_sha256': sha(SOURCE / 'manifest.json'), 'files': inventory, 'regenerated_views': derived}
    generated_write(TARGET / 'publication-manifest.json', json.dumps(report, indent=2))
    print(json.dumps({'files': len(inventory), 'bytes': sum(x['bytes'] for x in inventory), 'status': report['status']}))

if __name__ == '__main__':
    main()
