"""Package observed Bootcamps UI captures; never fetch or infer source answers."""
import argparse
import hashlib
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import shutil
from urllib.parse import urlparse, urljoin, parse_qs
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[2]


class SafeHTML(HTMLParser):
    """Retain instructional structure/emphasis while removing executable markup."""
    allowed = {'div', 'p', 'span', 'strong', 'b', 'em', 'i', 'u', 's', 'ol', 'ul',
               'li', 'br', 'h1', 'h2', 'h3', 'h4', 'blockquote', 'table', 'thead',
               'tbody', 'tr', 'th', 'td', 'button', 'a', 'img', 'sup', 'sub'}

    def __init__(self, image_map=None, page_url=''):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.suppressed = 0
        self.image_map = image_map or {}
        self.page_url = page_url

    def handle_starttag(self, tag, attrs):
        if tag in {'script', 'style', 'svg', 'iframe'}:
            self.suppressed += 1
        if self.suppressed or tag not in self.allowed:
            return
        kept = []
        for key, value in attrs:
            if key == 'src' and tag == 'img':
                value = self.image_map.get(urljoin(self.page_url, value or ''), value)
            if key in {'href', 'src'} and value and not value.startswith(('https://', 'http://', '#')):
                if not (key == 'src' and value.startswith('assets/')):
                    continue
            if key in {'href', 'src', 'alt', 'colspan', 'rowspan'}:
                kept.append(f'{key}="{html.escape(value or "", quote=True)}"')
        self.parts.append('<' + tag + (' ' + ' '.join(kept) if kept else '') + '>')

    def handle_endtag(self, tag):
        if tag in {'script', 'style', 'svg', 'iframe'}:
            self.suppressed = max(0, self.suppressed - 1)
            return
        if not self.suppressed and tag in self.allowed and tag not in {'br', 'img'}:
            self.parts.append(f'</{tag}>')

    def handle_data(self, data):
        if not self.suppressed:
            self.parts.append(html.escape(data))


def clean(value, image_map=None, page_url=''):
    parser = SafeHTML(image_map, page_url)
    parser.feed(value or '')
    return ''.join(parser.parts)


def preserve_images(data, archive, destination):
    """Download only visible image URLs recorded by the browser capture."""
    sources = {}
    for question in data.get('questions', []):
        states = [question.get('initial') or {}, question.get('final') or {}]
        states += [attempt.get('state') or {} for attempt in question.get('attempts', [])]
        for state in states:
            for image in state.get('images', []):
                if image.get('src'):
                    sources.setdefault(image['src'], image.get('alt', ''))
    mapping, records = {}, []
    cache = archive / 'assets'
    cache.mkdir(parents=True, exist_ok=True)
    for url, alt in sources.items():
        identity = hashlib.sha256(url.encode()).hexdigest()
        existing = list(cache.glob(identity + '.*'))
        target = next((p for p in existing if p.suffix != '.json'), None)
        failure = None
        used_url = url
        if target is None:
            candidates = [url]
            parsed = urlparse(url)
            nested = parse_qs(parsed.query).get('url', []) if parsed.path == '/_next/image' else []
            if nested and urlparse(nested[0]).scheme == 'https':
                candidates.append(nested[0])
            for candidate in candidates:
                try:
                    with urlopen(Request(candidate, headers={'User-Agent': 'Mozilla/5.0'}), timeout=25) as response:
                        content = response.read()
                        mime = response.headers.get_content_type()
                    signatures = [(b'\x89PNG\r\n\x1a\n', '.png'), (b'\xff\xd8\xff', '.jpg'), (b'GIF8', '.gif')]
                    extension = next((ext for prefix, ext in signatures if content.startswith(prefix)), None)
                    if content[:4] == b'RIFF' and content[8:12] == b'WEBP':
                        extension = '.webp'
                    if not mime.startswith('image/') or extension is None:
                        raise ValueError('Response is not a supported raster image')
                    target = cache / (identity + extension)
                    target.write_bytes(content)
                    used_url, failure = candidate, None
                    break
                except Exception as error:
                    failure = f'{type(error).__name__}: {error}'
        if target is not None:
            portable = destination / 'assets' / target.name
            portable.parent.mkdir(parents=True, exist_ok=True)
            if target.resolve() != portable.resolve():
                shutil.copyfile(target, portable)
            mapping[url] = 'assets/' + target.name
            records.append({'url': url, 'alt': alt, 'status': 'captured', 'asset': target.relative_to(archive).as_posix(), 'sha256': hashlib.sha256(target.read_bytes()).hexdigest(), 'downloadUrl': used_url})
        else:
            records.append({'url': url, 'alt': alt, 'status': 'failed', 'error': failure})
    return mapping, records


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8')


def question_fragment(markup):
    start = re.search(r'<div\b[^>]*class="[^"]*min-w-0[^"]*rounded-tr-lg[^>]*>', markup)
    if not start:
        raise ValueError('Supplement question container not found')
    depth = 0
    for token in re.finditer(r'</?div\b[^>]*>', markup[start.start():]):
        depth += -1 if token.group().startswith('</') else 1
        if depth == 0:
            return markup[start.start():start.start() + token.end()]
    raise ValueError('Supplement question container not balanced')


def supplements(archive, slug):
    path = archive / 'referential-initial.json'
    if slug != 'referential-phrasing' or not path.exists():
        return {}, None
    grouped = {}
    for index, state in enumerate(json.loads(path.read_text(encoding='utf-8-sig')), 1):
        fragment = question_fragment(state['html'])
        match = re.search(r'<h2\b[^>]*>Question (\d+)</h2>', fragment)
        if not match:
            raise ValueError('Supplement question number not found')
        grouped.setdefault(int(match[1]), []).append({'sourceIndex': index, 'html': fragment})
    return grouped, path


def correct_answer(question):
    state = question.get('final') or question.get('initial') or {}
    if not state.get('buttons'):
        return None, 'Information page; no answer required.'
    success = 'bg-seafoam' in state.get('html', '') or 'check-circle-filled-icon' in state.get('html', '')
    selected = [b['label'] for b in state.get('buttons', []) if 'bg-chartreuse' in b.get('html', '')]
    if success and len(selected) == 1:
        return selected[0], 'Observed successful final state and selected answer styling.'
    for attempt in reversed(question.get('attempts', [])):
        markup = attempt.get('state', {}).get('html', '')
        if ('bg-seafoam' in markup or 'check-circle-filled-icon' in markup) and attempt.get('selected'):
            return attempt['selected'], 'Observed successful submitted attempt.'
    return None, 'Correct answer not established by captured success state.'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archive', type=Path, default=ROOT / 'raw/sources/loophole-bootcamps-2026-10-18')
    parser.add_argument('--output', type=Path, default=ROOT / 'corpus/loophole-online/bootcamps')
    parser.add_argument('--finalize', action='store_true')
    args = parser.parse_args()
    inventory_path = args.archive / 'inventory.json'
    inventory = json.loads(inventory_path.read_text(encoding='utf-8-sig'))
    expected = {d['url']: chapter for chapter in inventory for d in chapter.get('drills', [])}
    records, gaps = [], []
    for source in sorted(args.archive.glob('*/*/source.json')):
        data = json.loads(source.read_text(encoding='utf-8-sig'))
        chapter, slug = source.parent.parent.name, source.parent.name
        destination = args.output / chapter / slug
        title = slug.replace('-', ' ').title()
        # Capture title may be the observed action label rather than the drill heading.
        if data.get('title') and data['title'].upper() not in {'START BOOTCAMP', 'RESUME BOOTCAMP', 'RETRY BOOTCAMP'}:
            title = data['title']
        questions = data.get('questions', [])
        extra_states, supplement_path = supplements(args.archive, slug)
        if supplement_path:
            destination.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(supplement_path, destination / 'supplement-original-states.json')
        image_map, image_records = preserve_images(data, args.archive, destination)
        source_clean = lambda markup: clean(markup, image_map, data.get('url', ''))
        if title == slug.replace('-', ' ').title() and questions:
            page_lines = (questions[0].get('initial', {}).get('pageText') or '').splitlines()
            if 'TELL ELLEN' in page_lines:
                previous = [line.strip() for line in page_lines[:page_lines.index('TELL ELLEN')] if line.strip()]
                if previous and previous[-1] not in {'BOOTCAMPS', 'AI Ellen'}:
                    title = previous[-1]
        numbers = [q.get('number') for q in questions]
        missing = sorted(set(range(1, data.get('total', 0) + 1)) - set(numbers))
        issues = []
        if any(image['status'] == 'failed' for image in image_records):
            issues.append('Essential image assets missing; see images.generated.json')
        write(destination / 'images.generated.json', json.dumps(image_records, indent=2, ensure_ascii=False) + '\n')
        if missing:
            issues.append(f'Missing question numbers: {missing}')
        if len(set(numbers)) != len(numbers):
            issues.append('Duplicate question numbers')
        if data.get('errors'):
            issues.append(f'Capture errors: {data["errors"]}')
        body, sections = [], []
        unknown, gated, answerable, information = [], [], 0, 0
        for q in questions:
            number = q['number']
            initial, final = q.get('initial') or {}, q.get('final') or q.get('initial') or {}
            answer, basis = correct_answer(q)
            info = not final.get('buttons')
            if info:
                information += 1
            else:
                answerable += 1
            if 'Upgrade to Practice' in final.get('text', ''):
                gated.append({'question': number, 'citations': sorted(set(re.findall(r'PT\d+\.S\d+\.Q\d+', final.get('text', '')))), 'status': 'Referenced licensed stimulus gated; citation and visible drill choices/feedback captured.'})
            if not q.get('resolved') and not info:
                issues.append(f'Question {number} unresolved')
            if answer is None and not info:
                unknown.append(number)
            body += [f'## Question {number}', '', '### Initial observed question and choices', '', source_clean(initial.get('html', '')) or initial.get('text', ''), '']
            rendered = [f'<h2>Question {number}</h2><h3>Initial observed state</h3>', source_clean(initial.get('html', ''))]
            for index, attempt in enumerate(q.get('attempts', []), 1):
                label = str(attempt.get('selected', 'Unknown'))
                state = attempt.get('state') or {}
                body += [f'### Observed attempt {index}: {label}', '', source_clean(state.get('html', '')) or state.get('text', ''), '']
                rendered += [f'<h3>Observed attempt {index}: {html.escape(label)}</h3>', source_clean(state.get('html', ''))]
            body += ['### Final observed answer and feedback', '', source_clean(final.get('html', '')) or final.get('text', ''), '', f'**Verified answer:** {answer if answer is not None else "No answer required" if info else "Unknown"}', '', f'Capture commentary: {basis}', '']
            rendered += ['<h3>Final observed state</h3>', source_clean(final.get('html', '')), f'<p><strong>Verified answer:</strong> {html.escape(str(answer or ("No answer required" if info else "Unknown")))}</p><p>Capture commentary: {basis}</p>']
            for extra in extra_states.get(number, []):
                label = f'Earlier original observed state {extra["sourceIndex"]}'
                body += [f'### {label}', '', 'Supplementary source capture from the initial traversal. This preserves transient instructor commentary that a revisit may no longer display.', '', source_clean(extra['html']), '']
                rendered += [f'<h3>{label}</h3><p>Supplementary original source state; preserves transient response commentary.</p>', source_clean(extra['html'])]
            sections.append('\n'.join(rendered))
        if unknown:
            issues.append(f'Correct answer unverified for questions: {unknown}')
        relative = source.relative_to(ROOT).as_posix() if source.is_relative_to(ROOT) else str(source)
        preamble = [f'# {title}', '', '[Bootcamps](../../README.md) | [Chapter](../README.md) | [Formatted capture](source.html) | [Original captured JSON](source.json)', '', f'Source: {data.get("url", "Unknown")}', '', f'Captured: {data.get("capturedAt", "Unknown")}. Instructor/source: Loophole Online / Ellen Cassidy.', '', f'Coverage: {len(questions)}/{data.get("total", "unknown")} questions. ' + ('Complete observed question sequence and resolved states.' if not issues else 'Partial or qualified capture; see verification report.'), '', 'Original source wording follows. Capture commentary and verified-answer labels are archival annotations. Already-answered questions may have no new attempts. Only observed feedback is preserved; unvisited alternative-answer feedback is not claimed.', '', f'Archived evidence: `{relative}`.', '']
        write(destination / 'README.md', '\n'.join(preamble + body))
        write(destination / 'source.html', '<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>' + html.escape(title) + '</title><style>body{max-width:920px;margin:3rem auto;padding:0 1rem;font:18px/1.6 system-ui;color:#202020}button{display:block;width:100%;text-align:left;background:#f7f7f7;border:1px solid #bbb;padding:1rem;margin:.4rem 0;font:inherit}img{max-width:100%}h2{margin-top:3rem;border-top:2px solid #aaa;padding-top:1rem}li{margin:.3rem 0}</style><body><h1>' + html.escape(title) + '</h1><p>Source wording and observed response states. Observed instructional images are archived locally where available; consult image coverage for failures.</p>' + '\n'.join(sections) + '</body></html>')
        destination.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination / 'source.json')
        record = {'title': title, 'chapter': chapter, 'slug': slug, 'url': data.get('url'), 'questions': len(questions), 'total': data.get('total'), 'resolved': not issues, 'issues': issues, 'unknownAnswers': unknown, 'images': image_records, 'answerableQuestions': answerable, 'informationPages': information, 'sourceAccessLimits': gated, 'supplementStates': sum(map(len, extra_states.values()))}
        records.append(record)
        gaps.extend(f'{chapter}/{slug}: {issue}' for issue in issues)
    captured_urls = {r['url'] for r in records}
    gaps.extend('Missing drill: ' + url for url in expected if url not in captured_urls)
    complete = len(expected) == 57 and len(records) == 57 and not gaps
    access_limits = [dict(drill=r['slug'], **limit) for r in records for limit in r['sourceAccessLimits']]
    report = {'expectedDrills': len(expected), 'capturedDrills': len(records), 'capturedQuestions': sum(r['questions'] for r in records), 'answerableQuestions': sum(r['answerableQuestions'] for r in records), 'informationPages': sum(r['informationPages'] for r in records), 'uiCaptureComplete': complete, 'fullReferencedStimuliCaptured': not access_limits, 'sourceAccessLimits': access_limits, 'complete': complete and not access_limits, 'finalized': args.finalize and complete, 'gaps': gaps, 'records': records, 'limits': ['Only observed response branches captured.', 'Some referenced licensed stimuli are gated by Upgrade to Practice; UI capture completion does not mean their hidden text was recovered.', 'HTML retains instructional emphasis and structure; source site CSS is not reproduced.', 'Observed instructional image URLs are downloaded to stable local assets; any failures block completion.']}
    write(args.output / 'verification.generated.json', json.dumps(report, indent=2, ensure_ascii=False) + '\n')
    write(args.output / 'catalog.generated.json', json.dumps(records, indent=2, ensure_ascii=False) + '\n')
    root_lines = ['# Loophole Bootcamps', '', '[Loophole home](../README.md) | [Coverage report](verification.generated.json)', '', f'{len(records)}/{len(expected)} drills captured; {report["capturedQuestions"]} question states. Status: {"complete observed UI sequence" if complete else "partial capture"}.', '', f'{len(access_limits)} question occurrences reference licensed stimuli hidden behind Upgrade to Practice. Their citations, visible choices and observed answer feedback are preserved; the hidden source stimuli are not recovered.', '', 'These are attributed source captures, not approved LSAT U curriculum. Captured correct responses and commentary appear in each drill. Alternative feedback is included only where observed.', '']
    for chapter in inventory:
        chapter_slug = urlparse(chapter['url']).path.rstrip('/').split('/')[-1]
        title = re.sub(r'\s+', ' ', chapter.get('title', chapter_slug)).strip()
        chapter_lines = [f'# {title}', '', '[All Bootcamps](../README.md)', '']
        root_lines += [f'## {title}', '']
        for drill in chapter.get('drills', []):
            slug = urlparse(drill['url']).path.rstrip('/').split('/')[-1]
            match = next((r for r in records if r['url'] == drill['url']), None)
            name = match['title'] if match else slug.replace('-', ' ').title()
            if match:
                suffix = f' ({match["questions"]}/{match["total"]}; {"resolved" if match["resolved"] else "qualified"})'
                chapter_lines.append(f'- [{name}]({slug}/README.md){suffix}')
                root_lines.append(f'- [{name}]({chapter_slug}/{slug}/README.md){suffix}')
            else:
                chapter_lines.append(f'- {name}: not captured')
                root_lines.append(f'- {name}: not captured')
        write(args.output / chapter_slug / 'README.md', '\n'.join(chapter_lines) + '\n')
        root_lines.append('')
    write(args.output / 'README.md', '\n'.join(root_lines) + '\n')
    if args.finalize:
        if not complete:
            raise SystemExit('Refusing finalization: expected all 57 drills with resolved, verified states. See verification.generated.json.')
        evidence = sorted(p for p in args.archive.rglob('*') if p.is_file() and p.name not in {'SHA256SUMS', 'PROVENANCE.md'})
        write(args.archive / 'SHA256SUMS', ''.join(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(args.archive).as_posix()}\n' for p in evidence))
        write(args.archive / 'PROVENANCE.md', '# Loophole Bootcamps capture\n\nCaptured 2026-10-18 from the authorized signed-in browser using rendered UI and observed answer interactions. Original JSON includes exact text, HTML, choices, observed attempts and feedback. No hidden API, authentication extraction or inferred answers. SHA256SUMS records evidence bytes at finalization. Source: Loophole Online / Ellen Cassidy. Portable pages are derived separately by system/scripts/package-loophole-bootcamps.py.\n')
    print(json.dumps({k: report[k] for k in ['expectedDrills', 'capturedDrills', 'capturedQuestions', 'complete', 'finalized']}, indent=2))


if __name__ == '__main__':
    main()
