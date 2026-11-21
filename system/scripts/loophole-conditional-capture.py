"""Preserve browser-observed Loophole lectures, native captions and media.

No browser login, private API or credential extraction. Run again after more
source.json files arrive; verified artifact bytes are reused without downloads.
"""
import argparse
import concurrent.futures
from datetime import datetime, timezone
import hashlib
import html
from html.parser import HTMLParser
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import urllib.request
from urllib.parse import quote, urljoin, urlsplit, urlunsplit

REPO = Path(__file__).resolve().parents[2]
DEFAULT_ROOT = REPO / 'Loophole Lecture/Conditional Reasoning 2026-10-18'


def digest(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def put(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    encoded = text.encode('utf-8')
    if not path.exists() or path.read_bytes() != encoded:
        path.write_bytes(encoded)


def json_put(path, data):
    put(path, json.dumps(data, ensure_ascii=False, indent=2) + '\n')


def executable(name):
    found = shutil.which(name)
    if found:
        return found
    packages = Path(os.environ.get('LOCALAPPDATA', '')) / 'Microsoft/WinGet/Packages'
    patterns = {'yt-dlp': 'yt-dlp.yt-dlp_*/yt-dlp.exe',
                'ffmpeg': 'yt-dlp.FFmpeg_*/ffmpeg-*/bin/ffmpeg.exe',
                'ffprobe': 'yt-dlp.FFmpeg_*/ffmpeg-*/bin/ffprobe.exe'}
    found = sorted(packages.glob(patterns[name])) if packages.exists() else []
    if not found:
        raise FileNotFoundError(f'{name} missing from PATH and documented WinGet installation')
    return str(found[-1])


def safe_error(error):
    return re.sub(r'https?://[^\s\"\']+', '[source URL]', str(error))[-1000:]


def command(args, timeout=1200):
    result = subprocess.run(args, capture_output=True, text=True,
                            encoding='utf-8', errors='replace', timeout=timeout)
    if result.returncode:
        raise RuntimeError(safe_error(result.stderr or result.stdout or f'Exit {result.returncode}'))
    return result.stdout


def cues_from_vtt(value):
    pattern = r'((?:\d{2}:)?\d{2}:\d{2}[.,]\d{3})\s+-->\s+((?:\d{2}:)?\d{2}:\d{2}[.,]\d{3})[^\n]*\n(.*?)(?=\n\s*\n|\Z)'
    return [(start, end, html.unescape(re.sub(r'<[^>]+>', '', text)).strip())
            for start, end, text in re.findall(pattern, value, re.S)]


def seconds(value):
    parts = value.replace(',', '.').split(':')
    return sum(float(part) * 60 ** power for power, part in enumerate(reversed(parts)))


def package_supplements(folder, lecture_data, allow_missing_supplements=False):
    """Make observed interactive states readable without replacing raw JSON."""
    spec = importlib.util.spec_from_file_location('loophole_bootcamp_packager', REPO / 'system/scripts/package-loophole-bootcamps.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    links, warnings, errors, coverage = [], [], [], {}
    for name in ['inline-bootcamp', 'book-excerpt']:
        source = folder / (name + '.json')
        if not source.exists():
            coverage[name] = {'status': 'not captured', 'complete': False,
                              'required': not allow_missing_supplements}
            continue
        data = json.loads(source.read_text(encoding='utf-8-sig'))
        title = name.replace('-', ' ').title()
        body = [f'# {title}', '', f'[Original observed JSON]({source.name})', '', 'Exact observed source content follows. This is separate from the lecture captions.', '']
        questions = data.get('questions', []) if isinstance(data, dict) else []
        if name == 'inline-bootcamp':
            total = data.get('total') if isinstance(data, dict) else None
            resolved = sum(bool(q.get('resolved')) for q in questions)
            verified = sum(module.correct_answer(q)[0] is not None or not (q.get('final') or q.get('initial') or {}).get('buttons') for q in questions)
            explicit_absence = not questions and any(word in str(data.get('status', '')).lower() for word in ['absent', 'no bootcamp', 'no video bootcamp', 'not available'])
            complete = explicit_absence or (total is not None and total == len(questions) == resolved == verified and bool(questions))
            coverage[name] = {'status': data.get('status'), 'questions': len(questions), 'total': total,
                              'resolved': resolved, 'answers_verified': verified, 'complete': complete}
        else:
            status = str(data.get('status', '')) if isinstance(data, dict) else ''
            explicit_absence = 'absent' in status.lower() or ('no ' in status.lower() and ('control' in status.lower() or 'excerpt' in status.lower()))
            content_saved = bool(data.get('html')) and bool(data.get('text'))
            coverage[name] = {'status': status or ('captured' if content_saved else 'content missing'), 'complete': content_saved or explicit_absence}
        image_data = data if questions else dict(data, questions=[{'initial': data}]) if isinstance(data, dict) else {'questions': []}
        image_map, image_records = module.preserve_images(image_data, folder, folder)
        json_put(folder / (name + '-images.generated.json'), image_records)
        for image in image_records:
            if image['status'] != 'captured':
                errors.append({'artifact': name + '-image', 'error': image.get('error', 'Observed instructional image missing')})
        states = []
        for question in questions:
            body += [f'## Question {question.get("number", "unknown")}', '']
            states = [('Initial state', question.get('initial') or {})]
            for attempt in question.get('attempts', []):
                submitted = str(attempt.get('selected', 'unknown'))
                state = attempt.get('state') or {}
                observed = [button.get('label', '') for button in state.get('buttons', [])
                            if any('bg-chartreuse' in classes.split() for classes in re.findall(r'class="([^"]*)"', button.get('html', '')))]
                letter = lambda value: (re.match(r'\s*([A-Z])(?:\s|$)', value) or [None, None])[1]
                mismatch = len(observed) == 1 and letter(submitted) and letter(observed[0]) != letter(submitted)
                if mismatch:
                    warning = f'Question {question.get("number")}: submitted {submitted}, but captured selected response is {observed[0]}; historical feedback attribution unverified.'
                    warnings.append(warning)
                    states.append((f'Unverified historical response: submitted {submitted}; captured selection {observed[0]}', state))
                else:
                    states.append((f'Observed response: {submitted}', state))
            states += [('Final state', question.get('final') or {})]
            for label, state in states:
                body += [f'### {label}', '', module.clean(state.get('html', ''), image_map, data.get('url', '')) or state.get('text', ''), '']
        if not questions:
            if isinstance(data, dict):
                body += [module.clean(data.get('html', ''), image_map, data.get('url', '')) or data.get('text', '') or json.dumps(data, ensure_ascii=False, indent=2), '']
            else:
                body += [json.dumps(data, ensure_ascii=False, indent=2), '']
        put(folder / (name + '.md'), '\n'.join(body))
        links.append(f'- [{title}]({name}.md) | [Original JSON]({name}.json)')
    notes = lecture_data.get('notes') or lecture_data.get('writtenNotes') or {}
    if isinstance(notes, dict) and notes.get('html'):
        observed_images = list(notes.get('images') or [])
        class NoteImages(HTMLParser):
            def handle_starttag(self, tag, attributes):
                if tag == 'img':
                    attributes = dict(attributes)
                    if attributes.get('src'):
                        observed_images.append({'src': urljoin(lecture_data['url'], attributes['src']), 'alt': attributes.get('alt', '')})
        parser = NoteImages(convert_charrefs=True)
        parser.feed(notes['html'])
        image_map, image_records = module.preserve_images({'questions': [{'initial': {'images': observed_images}}]}, folder, folder)
        json_put(folder / 'ellens-notes-images.generated.json', image_records)
        for image in image_records:
            if image['status'] != 'captured':
                errors.append({'artifact': 'ellens-notes-image', 'error': image.get('error', 'Missing observed note image')})
        coverage['written-notes-images'] = {'count': len(image_records), 'complete': all(image['status'] == 'captured' for image in image_records)}
        put(folder / 'ellens-notes-view.html', '<!doctype html><meta charset="utf-8"><title>Original written notes</title><main>' + module.clean(notes['html'], image_map, lecture_data['url']) + '</main>')
        links.append('- [Written notes with local images](ellens-notes-view.html) | [Original HTML](ellens-notes.html)')
    return links, list(dict.fromkeys(warnings)), errors, coverage


def lesson(source, tools, allow_missing_supplements=False, display_capture_date=None):
    folder = source.parent
    old_file = folder / 'verification.json'
    old = json.loads(old_file.read_text(encoding='utf-8')) if old_file.exists() else {}
    artifacts, errors, warnings = {}, [], []
    data = json.loads(source.read_text(encoding='utf-8-sig'))
    source_digest = digest(source)
    def identities(items):
        return [urlunsplit((*urlsplit(item.get('src', ''))[:3], '', '')) for item in items]
    media_identity = identities(data.get('sources', []))
    caption_identity = identities(data.get('tracks', []))
    title, url = data['title'], data['url']
    original_captured = data.get('capturedAt') or data.get('captured') or 'unknown; capture date not recorded'
    captured = (f'{display_capture_date} (documented local date; original timestamp {original_captured})'
                if display_capture_date else original_captured)

    def artifact(name, produce):
        path = folder / name
        previous = old.get('artifacts', {}).get(name, {})
        identity_key, identity = ('caption_source_identity', caption_identity) if name == 'source.vtt' else ('media_source_identity', media_identity)
        same_source = old.get(identity_key) == identity if identity_key in old else old.get('source_sha256') == source_digest
        if same_source and path.exists() and previous.get('status') == 'saved' and digest(path) == previous.get('sha256'):
            artifacts[name] = dict(previous, reused=True)
            return path
        try:
            produce(path)
            if not path.exists() or path.stat().st_size == 0:
                raise ValueError('Artifact is absent or empty after operation')
            artifacts[name] = {'status': 'saved', 'sha256': digest(path), 'bytes': path.stat().st_size, 'reused': False}
            return path
        except Exception as error:
            issue = {'artifact': name, 'error': safe_error(error)}
            artifacts[name] = dict(issue, status='failed')
            errors.append(issue)
            return None

    def download(address, path):
        request = urllib.request.Request(address, headers={'Referer': 'https://new.theloophole.com/'})
        with urllib.request.urlopen(request, timeout=90) as response:
            content = response.read()
        if not content.startswith((b'WEBVTT', b'\xef\xbb\xbfWEBVTT')):
            raise ValueError('Caption response is not native WEBVTT')
        path.write_bytes(content)

    notes = data.get('notes') or data.get('writtenNotes')
    if isinstance(notes, dict) and (notes.get('text') or notes.get('html')):
        put(folder / 'ellens-notes.txt', notes.get('text', ''))
        put(folder / 'ellens-notes.html', notes.get('html', ''))
        notes_status = 'captured exact written notes; text and HTML remain separate from speech'
    else:
        notes_status = (notes.get('status') if isinstance(notes, dict) else None) or data.get('notesStatus') or data.get('notes_status') or 'not captured; source did not record an explicit absence'
        put(folder / 'notes-status.txt', str(notes_status) + '\n')
        if not any(marker in str(notes_status).lower() for marker in ['absent', 'not rendered', 'no ellen']):
            warnings.append('Written-notes absence not established by source record')
    json_put(folder / 'rendered-transcript.json', data.get('transcript', []))
    put(folder / 'rendered-transcript.txt', '\n\n'.join(
        segment if isinstance(segment, str) else
        f'[{segment.get("time", segment.get("timestamp", "unknown"))}]\n{segment.get("text", "")}'
        for segment in data.get('transcript', [])) + '\n')
    put(folder / 'source-page.txt', data.get('pageText', ''))
    if data.get('pageHtml'):
        put(folder / 'source-page.html', data['pageHtml'])
    json_put(folder / 'related-links.json', data.get('relatedLinks', data.get('links', [])))
    tracks = data.get('tracks', [])
    track = next((item for item in tracks if item.get('default')), None) or next(
        (item for item in tracks if str(item.get('srclang', item.get('label', ''))).lower().startswith(('en', 'english'))), None) or (tracks[0] if tracks else {})
    origin = track.get('label') or track.get('srclang') or track.get('kind') or 'native track; language/generation label not exposed'
    caption = artifact('source.vtt', lambda path: download(track['src'], path))
    cues = []
    if caption:
        try:
            cues = cues_from_vtt(caption.read_text(encoding='utf-8-sig'))
            if not cues:
                raise ValueError('No native caption cues parsed')
        except Exception as error:
            errors.append({'artifact': 'native-transcript.md', 'error': safe_error(error)})
    if cues:
        transcript = '\n\n'.join(f'[{start} - {end}]\n{text}' for start, end, text in cues)
        put(folder / 'native-transcript.md', f'# {title}\n\nSource: {url}\n\nCaptured: {captured}. Displayed duration: {data.get("duration", "unknown")}.\n\nCaption origin: {origin}. This is a complete native-caption extraction, not word-by-word listening verification. Caption wording is retained without editorial correction. Original cue bytes remain in source.vtt; rendered site transcript is preserved separately.\n\n{transcript}\n')
    video = artifact('video.mp4', lambda path: command([
        tools['yt-dlp'], '--quiet', '--no-warnings', '--no-progress', '--no-playlist',
        '--concurrent-fragments', '4', '--force-overwrites', '--referer', 'https://new.theloophole.com/',
        '--merge-output-format', 'mp4', '--remux-video', 'mp4',
        '--ffmpeg-location', str(Path(tools['ffmpeg']).parent), '-o', str(path), data['sources'][0]['src']]))
    duration, frame_times = None, []
    if video:
        try:
            probe = json.loads(command([tools['ffprobe'], '-v', 'error', '-show_entries',
                                        'format=duration', '-of', 'json', str(video)], timeout=90))
            duration = float(probe['format']['duration'])
            if duration <= 0:
                raise ValueError('Nonpositive media duration')
        except Exception as error:
            errors.append({'artifact': 'video-duration', 'error': safe_error(error)})
        artifact('audio.m4a', lambda path: command([tools['ffmpeg'], '-hide_banner', '-loglevel', 'error',
            '-y', '-i', str(video), '-vn', '-c:a', 'copy', str(path)], timeout=300))
        if duration:
            frame_times = sorted(set([0, *range(45, max(1, int(duration)), 45),
                                     int(duration * .03), int(duration * .5), int(duration * .9)]))
            for time in frame_times:
                name = f'images/{time // 60:03}-{time % 60:02}.jpg'
                artifact(name, lambda path, time=time: (path.parent.mkdir(exist_ok=True), command([
                    tools['ffmpeg'], '-hide_banner', '-loglevel', 'error', '-y', '-ss', str(time),
                    '-i', str(video), '-frames:v', '1', str(path)], timeout=90)))
            if cues and seconds(cues[-1][1]) > duration + 2:
                errors.append({'artifact': 'caption-duration', 'error': 'Final cue extends more than two seconds beyond media'})
            if cues and duration - seconds(cues[-1][1]) > 20:
                warnings.append('Native captions end more than 20 seconds before media; inspect trailing silence/content')
    status = {'title': title, 'url': url, 'captured': original_captured, 'capture_display': captured, 'processedAt': datetime.now(timezone.utc).isoformat(),
              'source_sha256': source_digest, 'media_source_identity': media_identity, 'caption_source_identity': caption_identity, 'caption_origin': origin, 'cue_count': len(cues),
              'dom_segments': len(data.get('transcript', [])), 'last_caption': cues[-1][1] if cues else None,
              'video_duration': duration, 'frame_times_seconds': frame_times, 'notes_status': notes_status,
              'artifacts': artifacts, 'errors': errors, 'warnings': warnings, 'complete': not errors and bool(cues) and bool(duration),
              'listening_verified': False}
    status['media_complete'] = status['complete']
    supplement_links, supplement_warnings, supplement_errors, supplement_coverage = package_supplements(folder, data, allow_missing_supplements)
    status['warnings'].extend(supplement_warnings)
    status['errors'].extend(supplement_errors)
    status['supplement_coverage'] = supplement_coverage
    status['supplements_complete'] = all(value['complete'] for value in supplement_coverage.values()) and not supplement_errors
    status['required_supplements_complete'] = all(value['complete'] for value in supplement_coverage.values() if value.get('required', True)) and not supplement_errors
    status['complete'] = status['media_complete'] and status['required_supplements_complete']
    status['supplements'] = supplement_links
    if status['complete'] and not status['supplements_complete']:
        status['warnings'].append('Media package complete; optional quiz/excerpt supplements remain not captured. This does not establish their absence.')
    json_put(old_file, status)
    put(folder / 'README.md', f'# {title}\n\nSource: {url}\n\nCaptured: {captured}. Source wording is attributed to Loophole Online / Ellen Cassidy, not adopted LSAT U curriculum.\n\n- [Native caption transcript](native-transcript.md)\n- [Original captions](source.vtt)\n- [Rendered transcript](rendered-transcript.txt)\n- [Exact source record](source.json)\n- [Verification and per-artifact errors](verification.json)\n- [Original video](video.mp4)\n- [Original audio](audio.m4a)\n\nWritten notes: {notes_status}. ' + ('[Text](ellens-notes.txt) | [HTML](ellens-notes.html)\n' if isinstance(notes, dict) and (notes.get('text') or notes.get('html')) else '[Notes status](notes-status.txt)\n') + f'\nNative caption cues: {len(cues)}. Video duration: {duration}. Frames sample at most 45 seconds apart plus 3%, 50% and 90%; samples are not exhaustive slide-change detection. No word-by-word audio verification has been performed.\n\nCapture status: {"complete observed artifacts" if status["complete"] else "partial; see per-artifact errors"}.\n')
    put(folder / 'PROVENANCE.md', f'# {title}\n\nSource: {url}\n\nCaptured {captured} from the authorized rendered browser. Browser-observed media/track URLs only; no cookies or credentials extracted. Caption track label: {origin}. source.vtt preserves original caption bytes; native-transcript.md removes caption markup for reading. Rendered transcript and exact written notes remain separate artifacts. Original media retain instructor audio. Screenshots are derived sampled video frames at <=45-second intervals plus 3%, 50%, 90%, not independently verified complete whiteboard coverage.\n\nNo word-by-word listening verification. This is Loophole source material, not an adaptation or approval of Joshua\'s curriculum. verification.json explicitly records artifact failures and warnings. SHA256SUMS records retained artifact bytes.\n')
    if supplement_links:
        with (folder / 'README.md').open('a', encoding='utf-8') as stream:
            stream.write('\n## Additional observed source material\n\n' + '\n'.join(supplement_links) + '\n')
    files = sorted(path for path in folder.rglob('*') if path.is_file() and path.name != 'SHA256SUMS')
    put(folder / 'SHA256SUMS', ''.join(f'{digest(path)}  {path.relative_to(folder).as_posix()}\n' for path in files))
    print(json.dumps({'title': title, 'complete': status['complete'], 'media_complete': status['media_complete'], 'supplements_complete': status['supplements_complete'], 'cues': len(cues), 'frames': len(frame_times), 'errors': errors}), flush=True)
    return status


def finish_root_manifest(root, title, inventory_path, capture_dates):
    inventory_label = inventory_path.relative_to(REPO).as_posix() if inventory_path.is_relative_to(REPO) else str(inventory_path)
    put(root / 'PROVENANCE.md', f'# {title}\n\nDocumented batch capture dates: {", ".join(capture_dates)}. Original source timestamps remain unchanged in source.json and verification.json; verification-summary.generated.json records the display-date basis. The authorized browser provided the target inventory, source pages, rendered transcripts, exact notes, any captured book excerpts or inline Video Bootcamp states, and observed media URLs. No hidden backend requests, browser credentials, or curriculum adaptations were used.\n\nOriginal media and native VTT remain separate from rendered transcripts and written sources. Native captions are not word-by-word listening verification. Frames sample at <=45-second intervals plus 3%, 50%, and 90%, not every visual change. Historical response/selection mismatches, when present, are labeled unverified without changing original raw captures; final-answer proof is checked independently. Missing optional supplements remain explicitly not captured, never inferred absent.\n\nThe target inventory is {inventory_label}. verification-summary.generated.json records its SHA-256 and final coverage. SHA256SUMS aggregates each lecture\'s byte-verified manifest and hashes the root records. Source pages and raw JSON retain their original identities.\n')
    entries = {}
    for manifest in sorted(root.glob('*/SHA256SUMS')):
        for line in manifest.read_text(encoding='utf-8').splitlines():
            checksum, relative = line.split('  ', 1)
            entries[f'{manifest.parent.name}/{relative}'] = checksum
        entries[manifest.relative_to(root).as_posix()] = digest(manifest)
    for path in root.iterdir():
        if path.is_file() and path.name != 'SHA256SUMS':
            entries[path.name] = digest(path)
    put(root / 'SHA256SUMS', ''.join(f'{checksum}  {name}\n' for name, checksum in sorted(entries.items())))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', nargs='?', type=Path, default=DEFAULT_ROOT)
    parser.add_argument('--workers', type=int, choices=range(1, 4), default=3)
    parser.add_argument('--inventory', type=Path, default=REPO / 'raw/sources/loophole-conditionals-2026-10-18/target-lectures.json')
    parser.add_argument('--title', default='Conditional Reasoning source lectures')
    def capture_date(value):
        try:
            return datetime.strptime(value, '%Y-%m-%d').date().isoformat()
        except ValueError:
            raise argparse.ArgumentTypeError('Capture date must be YYYY-MM-DD')
    parser.add_argument('--capture-date', type=capture_date, help='Documented local capture date for batch summaries; original source timestamps remain unchanged')
    parser.add_argument('--allow-missing-supplements', action='store_true', help='Allow uncaptured quiz/excerpt supplements without claiming their coverage complete; captured incomplete supplements remain failures')
    args = parser.parse_args()
    root = args.root.resolve()
    root.mkdir(parents=True, exist_ok=True)
    tools = {name: executable(name) for name in ['yt-dlp', 'ffmpeg', 'ffprobe']}
    sources = sorted(root.glob('*/source.json'))
    inventory_path = args.inventory.resolve()
    if not inventory_path.exists():
        raise SystemExit(f'Target inventory not found: {inventory_path}')
    inventory = json.loads(inventory_path.read_text(encoding='utf-8-sig'))
    order = {row['url']: index for index, row in enumerate(inventory)}
    sources.sort(key=lambda source: (order.get(json.loads(source.read_text(encoding='utf-8-sig')).get('url'), len(order)), source.parent.name))
    if not sources:
        raise SystemExit('No browser-observed source.json files present')
    def capture_one(source):
        try:
            return lesson(source, tools, args.allow_missing_supplements, args.capture_date)
        except Exception as error:
            status = {'title': source.parent.name, 'complete': False, 'error': safe_error(error)}
            json_put(source.parent / 'verification.json', status)
            print(json.dumps(status), flush=True)
            return status
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        results = list(pool.map(capture_one, sources))
    json_put(root / 'verification.json', results)
    expected_urls = {row['url'] for row in inventory}
    captured_urls = {row.get('url') for row in results}
    missing_urls = sorted(expected_urls - captured_urls)
    unexpected_urls = sorted(url for url in captured_urls - expected_urls if url)
    source_timestamp_dates = sorted({str(row.get('captured', 'unknown'))[:10] for row in results})
    capture_dates = [args.capture_date] if args.capture_date else source_timestamp_dates
    summary = {'title': args.title, 'capture_dates': capture_dates, 'inventory_path': str(inventory_path),
               'allow_missing_supplements': args.allow_missing_supplements,
               'capture_date_basis': 'explicit documented local date' if args.capture_date else 'source timestamp date components; timezone not converted',
               'source_timestamp_dates': source_timestamp_dates,
               'expected_lectures': len(inventory), 'captured_lectures': len(results),
               'missing_target_urls': missing_urls, 'unexpected_source_urls': unexpected_urls,
               'media_complete': sum(bool(row.get('media_complete')) for row in results),
               'complete_lectures': sum(bool(row.get('complete')) for row in results),
               'native_caption_cues': sum(row.get('cue_count', 0) for row in results),
               'media_runtime_seconds': sum(row.get('video_duration') or 0 for row in results),
               'sampled_frames': sum(len(row.get('frame_times_seconds', [])) for row in results),
               'quiz_questions': sum(row.get('supplement_coverage', {}).get('inline-bootcamp', {}).get('questions', 0) for row in results),
               'verified_final_answers': sum(row.get('supplement_coverage', {}).get('inline-bootcamp', {}).get('answers_verified', 0) for row in results),
               'qualified_lectures': [row['title'] for row in results if not row.get('complete')],
               'warnings': [{'title': row['title'], 'warnings': row.get('warnings')} for row in results if row.get('warnings')],
               'errors': [{'title': row['title'], 'errors': row.get('errors', row.get('error'))} for row in results if row.get('errors') or row.get('error')],
               'inventory_sha256': digest(inventory_path) if inventory else None,
               'listening_verified': False}
    json_put(root / 'verification-summary.generated.json', summary)
    quiz_coverage = (f'{summary["verified_final_answers"]}/{summary["quiz_questions"]} observed final quiz answers verified.'
                     if summary['quiz_questions'] else 'Inline Video Bootcamp quizzes were not captured in this demo-media batch. This does not establish their absence.')
    lines = [f'# {args.title}', '', f'Captured {", ".join(capture_dates)} from Loophole Online / Ellen Cassidy. These are original vendor sources, not an adaptation or comparison with Joshua\'s curriculum.', '',
             f'{len(results)} lectures processed; {summary["media_complete"]} media captures complete. {quiz_coverage} Native captions: {summary["native_caption_cues"]} cues. Original media: {summary["media_runtime_seconds"]:.2f} seconds. Sampled frames: {summary["sampled_frames"]}.', '',
             '[Coverage summary](verification-summary.generated.json) | [Per-lecture verification](verification.json)', '',
             'Native captions, rendered transcripts, written notes, and any captured book excerpts or inline Video Bootcamps remain separate artifacts. Native and rendered captions can differ in grouping and wording; neither is word-by-word listening verification. Frames sample at most 45 seconds apart plus 3%, 50% and 90%, rather than every visual change.' + (' Historical response mismatches remain explicitly qualified; final-answer proof is checked separately.' if summary['quiz_questions'] else ''), '']
    for index, (source, row) in enumerate(zip(sources, results)):
        if args.title == 'Conditional Reasoning source lectures' and inventory_path == (REPO / 'raw/sources/loophole-conditionals-2026-10-18/target-lectures.json') and len(inventory) == 26 and index in {0, 18, 25}:
            lines += ['## ' + {0: 'The eighteen core conditional lessons', 18: 'Seven related Loophole explanations', 25: 'The Acronym LR practice walkthrough'}[index], '']
        lines += [f'{index + 1}. [{row["title"]}]({quote(source.parent.name)}/README.md): {"saved" if row["complete"] else "qualified; inspect verification"}']
    lines += ['', 'The browser-observed target inventory determines lecture coverage. This helper processes only existing saved source records. Final-answer success confirms the site\'s response, not independent validation of its teaching claims.']
    put(root / 'README.md', '\n'.join(lines) + '\n')
    finish_root_manifest(root, args.title, inventory_path, capture_dates)
    print(json.dumps({'processed': len(results), 'media_complete': sum(bool(row.get('media_complete')) for row in results), 'complete': sum(row['complete'] for row in results), 'qualified': sum(not row['complete'] for row in results), 'supplement_gaps': [row['title'] for row in results if row.get('media_complete') and not row.get('supplements_complete')]}), flush=True)
    return 0 if all(row['complete'] for row in results) and not missing_urls and not unexpected_urls else 2


if __name__ == '__main__':
    sys.exit(main())
