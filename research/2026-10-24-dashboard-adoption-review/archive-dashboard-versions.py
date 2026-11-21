"""Archive the explicitly selected local dashboard studies; never alter sources."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib
import html
import json
import os
import re
import shutil
import urllib.request

VAULT = Path(__file__).resolve().parents[2]
DOWNLOADS = Path('C:/Users/Joshu/Downloads')
ROOT = VAULT / 'design/prototypes/lsatu-dashboard'
SOURCES = [
    ('01-original', DOWNLOADS / 'LSAT-U-Dashboard-2026-10-22'),
    ('02-role-handoff', DOWNLOADS / 'LSAT-U-Dashboard-Handoff-2026-10-22'),
    ('03-first-directions', DOWNLOADS / 'LSAT-U-Dashboard-Three-Directions'),
    ('04-claude-v2', DOWNLOADS / 'LSAT-U-Dashboard-Three-Directions-v2'),
    ('05-new-directions', DOWNLOADS / 'LSAT-U-Dashboard-New-Directions'),
    ('06-motion-studies', DOWNLOADS / 'LSAT-U-Motion-Studies-2026-10-22'),
    ('07-motion-refinement', DOWNLOADS / 'LSAT-U-LexPrep-Motion-2026-10-22'),
    ('08-adoption-review', VAULT / 'research/2026-10-24-dashboard-adoption-review'),
]
MANIFEST = []
DERIVED = []
VENDOR = {}


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def copy_verified(source, destination, family):
    if source.is_symlink():
        raise RuntimeError(f'Refusing source symlink: {source}')
    destination.parent.mkdir(parents=True, exist_ok=True)
    before = digest(source)
    shutil.copy2(source, destination)
    after = digest(source)
    copied = digest(destination)
    if before != after or copied != before:
        raise RuntimeError(f'Source changed or copy mismatch: {source}')
    MANIFEST.append({'family': family, 'source': str(source),
                     'path': destination.relative_to(ROOT).as_posix(),
                     'bytes': destination.stat().st_size, 'sha256': copied})


def copy_family(key, source):
    destination = ROOT / 'families' / key
    for directory, dirs, files in os.walk(source, followlinks=False):
        parent = Path(directory)
        for name in dirs:
            if (parent / name).is_symlink():
                raise RuntimeError(f'Refusing source directory symlink: {parent / name}')
        for name in files:
            file = parent / name
            # This tool is operational provenance, outside the captured design generation.
            if key == '08-adoption-review' and file.resolve() == Path(__file__).resolve():
                continue
            copy_verified(file, destination / file.relative_to(source), key)


def add_card(cards, title, group, description, links, image=None, note=''):
    card = {'title': title, 'group': group, 'description': description,
            'links': [{'label': label, 'path': path} for label, path in links],
            'image': image, 'note': note}
    cards.append(card)


def vendor_download(url):
    """Public static font/animation dependencies only, without credentials."""
    if url in VENDOR:
        return VENDOR[url]
    allowed = ('https://fonts.googleapis.com/', 'https://fonts.gstatic.com/',
               'https://cdnjs.cloudflare.com/ajax/libs/gsap/')
    if not url.startswith(allowed):
        raise RuntimeError(f'Unapproved runtime dependency domain: {url}')
    ext = '.css' if 'fonts.googleapis.com' in url else Path(url.split('?')[0]).suffix
    relative = Path('vendor') / (hashlib.sha256(url.encode()).hexdigest()[:18] + ext)
    destination = ROOT / relative
    destination.parent.mkdir(exist_ok=True)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 Chrome/130.0.0.0 Safari/537.36'})
    with urllib.request.urlopen(req, timeout=30) as response:
        content = response.read()
    VENDOR[url] = relative.as_posix()
    if ext == '.css':
        css = content.decode('utf-8')
        for linked in set(re.findall(r'https://fonts\.gstatic\.com/[^\s\"\'\)]+', css)):
            local = vendor_download(linked)
            css = css.replace(linked, Path(local).name)
        content = css.encode('utf-8')
    destination.write_bytes(content)
    return relative.as_posix()


def portable_tree(source, destination):
    """Keep original families byte-identical; change only separate openable derivatives."""
    shutil.copytree(source, destination,
                    ignore=shutil.ignore_patterns('_research', '_verify', 'artifacts', '__pycache__'))


def localize_runtime():
    # Only these older families require localization. Later previews are already local.
    portable_tree(ROOT / 'families/03-first-directions', ROOT / 'open/first-directions')
    portable_tree(ROOT / 'families/04-claude-v2', ROOT / 'open/claude-v2')
    pass3 = ROOT / 'open/claude-pass-3'
    pass3.mkdir()
    original = ROOT / 'families/04-claude-v2'
    for name in ('carrel', 'lamplight', 'marginalia'):
        shutil.copytree(original / f'_research/backup-pass3-{name}', pass3 / name)
    shutil.copytree(original / 'shared', pass3 / 'shared')
    shutil.copytree(original / 'screenshots/thumbs', pass3 / 'screenshots/thumbs')
    shutil.copy2(original / '_research/backup-pass3-index.html', pass3 / 'index.html')
    files = [p for p in (ROOT / 'open').rglob('*') if p.suffix.lower() in ('.html', '.css')]
    urls = set()
    for file in files:
        for url in re.findall(r'https://[^\s\"\'<>\)]+', file.read_text(encoding='utf-8')):
            if 'fonts.googleapis.com/css' in url or 'cdnjs.cloudflare.com/ajax/libs/gsap/' in url:
                urls.add(html.unescape(url))
    # Each CSS can have dependent fonts; downloading one URL is a sequential dependency chain.
    for url in sorted(urls):
        vendor_download(url)
    for file in files:
        before = digest(file)
        text = file.read_text(encoding='utf-8')
        text = re.sub(r'<link\b[^>]*\brel=[\"\']preconnect[\"\'][^>]*>', '', text, flags=re.I)
        for url, relative in VENDOR.items():
            local = os.path.relpath(ROOT / relative, file.parent).replace('\\', '/')
            text = text.replace(html.escape(url, quote=True), local).replace(url, local)
        file.write_text(text, encoding='utf-8')
        after = digest(file)
        if before != after:
            DERIVED.append({'path': file.relative_to(ROOT).as_posix(),
                            'before_sha256': before, 'after_sha256': after,
                            'change': 'Localized public font/GSAP URLs and removed network preconnect hints.'})


def evidence_gallery(key, title, source_dir):
    images = sorted(p for p in source_dir.rglob('*') if p.suffix.lower() in ('.png', '.jpg', '.jpeg', '.webp'))
    videos = sorted(p for p in source_dir.rglob('*.mp4'))
    pages = sorted(p for p in source_dir.rglob('*.html'))
    reports = sorted(p for p in source_dir.rglob('*') if p.suffix.lower() in ('.md', '.json') and p.stat().st_size < 200000)
    target = ROOT / 'evidence' / (key + '.html')
    target.parent.mkdir(exist_ok=True)
    def rel(p): return os.path.relpath(p, target.parent).replace('\\', '/')
    sections = ''.join(f'<a class="shot" href="{html.escape(rel(p))}" target="_blank"><img loading="lazy" src="{html.escape(rel(p))}" alt="{html.escape(p.name)}"><span>{html.escape(str(p.relative_to(source_dir)))}</span></a>' for p in images)
    others = ''.join(f'<li><a href="{html.escape(rel(p))}">{html.escape(str(p.relative_to(source_dir)))}</a></li>' for p in videos + pages + reports)
    target.write_text(f'<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title><link rel="stylesheet" href="../archive.css"><header><a href="../index.html">← All dashboard versions</a><h1>{html.escape(title)}</h1><p>Preserved evidence files. Screenshots do not prove current production state or motion behavior. Click an image to inspect its full size.</p><p>{len(images)} images · {len(videos)} recordings</p></header><main class="evidence-grid">{sections}</main><section class="file-list"><h2>Recordings, pages and reports</h2><ul>{others}</ul></section></html>', encoding='utf-8')
    return target.relative_to(ROOT).as_posix()


def build_index():
    cards = []
    prefix = 'families/'
    family_keys = [key for key, _ in SOURCES]
    galleries = {key: evidence_gallery(key, label, ROOT / 'families' / key)
                 for key, label in [('01-original', 'Original dashboard screenshots'),
                                    ('02-role-handoff', 'Student and teacher handoff evidence'),
                                    ('03-first-directions', 'First directions evidence'),
                                    ('04-claude-v2', 'Claude Code v2 evidence and passes'),
                                    ('05-new-directions', 'New Directions evidence, versions 01–08'),
                                    ('06-motion-studies', 'Motion study evidence'),
                                    ('07-motion-refinement', 'LexPrep motion refinement evidence'),
                                    ('08-adoption-review', 'Adoption comparison evidence')]}
    new = prefix + '05-new-directions/'
    add_card(cards, '08 · Combined Home', 'Latest', 'The combined local version. Persistent sidebar, compact atmospheric assignment card, separate work, finder, review and curriculum views.',
             [('Open combined version', new+'08-combined-home/index.html'), ('Files and evidence', galleries['05-new-directions'])], new+'08-combined-home/artifacts/home-1440.png', 'Student and teacher previews use sample data. No production connection.')
    add_card(cards, 'Original dashboard snapshots', 'Originals', 'Student and teacher captures, including before, first-pass, light, dark and responsive states.', [('Browse all screenshots', galleries['01-original'])], prefix+'01-original/teacher-before-1440.png', 'Screenshots only. This source folder contains no playable HTML.')
    add_card(cards, 'Role-specific handoff', 'Originals', 'Original student and teacher HTML exports with screenshots and handoff notes.', [('Student', prefix+'02-role-handoff/student-dashboard.html'), ('Teacher', prefix+'02-role-handoff/teacher-dashboard.html'), ('Evidence', galleries['02-role-handoff'])], prefix+'02-role-handoff/student-dashboard.png')
    for folder, label, desc in [('broadsheet','The Brief / Broadsheet','Editorial masthead, serif titles and fine rules.'),('meridian','Meridian','Timeline and precise progress study.'),('therefore','Therefore','Reasoning-led next-action composition.')]:
        add_card(cards,label,'Earlier artifact',desc,[('Student',f'open/first-directions/{folder}/student.html'),('Teacher',f'open/first-directions/{folder}/teacher.html')],f'families/03-first-directions/screenshots/{folder}-student-1440-top.jpg','Local font dependencies included. Exact per-file assistant authorship is not established.')
    for folder,label,desc in [('lamplight','Lamplight','One task under the light; dark study and warm paper.'),('carrel','Carrel','Tactile work cards, messages and teacher student lookup.'),('marginalia','Marginalia','Contextual sidenotes and a letter-like study plan.')]:
        add_card(cards,label,'Claude Code v2',desc,[('Student',f'open/claude-v2/{folder}/student.html'),('Teacher',f'open/claude-v2/{folder}/teacher.html'),('Evidence',galleries['04-claude-v2'])],f'families/04-claude-v2/screenshots/thumbs/{folder}-student-1440.jpg')
        add_card(cards,label+' · preserved pass 3','Intermediate passes','Earlier source snapshot preserved alongside the later version.', [('Student',f'open/claude-pass-3/{folder}/student.html'),('Teacher',f'open/claude-pass-3/{folder}/teacher.html')],None,'Shared-asset paths repaired only in this openable copy. Original backup files remain byte-identical in families/04-claude-v2/_research/. No unique pass-3 screenshot is claimed.')
    versions=[('01-lumen','01 · Lumen','Quiet light surfaces and compact day cards.','artifacts/student-1440.png'),('02-margin','02 · Margin','Charcoal next action with editorial typography and contextual notes.','artifacts/margin-1440.png'),('03-studio','03 · Studio','Paper folio and session preparation exploration.','studio-1440.png'),('04-refined','04 · Refined','Neutral hierarchy, rounded week and a balanced study plan.','artifacts/refined-1440.png'),('05-studio','05 · Studio colour study','Rejected overall palette, preserved for useful search and result ideas.','artifacts/pass-final-1440.png'),('06-refined-studio','06 · Refined Studio','Neutral synthesis, reference console and result strips.','artifacts/final-desktop.png'),('07-atmosphere','07 · Atmosphere','Original paper landscape and restrained atmospheric materials.','artifacts/atmosphere-final-hero.png')]
    for folder,label,desc,image in versions:
        add_card(cards,label,'New Directions',desc,[('Open version',new+folder+'/index.html'),('Evidence and earlier captures',galleries['05-new-directions'])],new+folder+'/'+image,'Preserved local sample-data study. Historical labels and layouts have not been silently updated.')
    for name in sorted((ROOT/'saved-pages').glob('*.html')):
        refined=name.name.startswith('Refined')
        add_card(cards,'Saved '+('Refined' if refined else 'Studio charcoal'),'Saved pages','SingleFile page saved on 2026-10-24 at '+('05:47' if refined else '05:53')+'.',[('Open saved file',name.relative_to(ROOT).as_posix())],None,'Historical snapshot of '+('04-refined' if refined else '03-studio/?palette=charcoal')+', not an independent design family.')
    for name,label,desc in [('01-scroll.html','Motion study · Scroll','Content reveal and scroll composition study.'),('02-interface.html','Motion study · Interface','Selected tabs and Apply/Cancel configuration study.')]:
        add_card(cards,label,'Motion',desc,[('Open study',prefix+'06-motion-studies/'+name),('Evidence',galleries['06-motion-studies'])],prefix+'06-motion-studies/'+('01-desktop.jpg' if name.startswith('01') else '02-desktop.jpg'))
    add_card(cards,'LexPrep motion refinement','Motion','Preserved application screenshots, recordings and review evidence.', [('Browse recordings and evidence',galleries['07-motion-refinement'])],prefix+'07-motion-refinement/home-desktop.png','Evidence collection; no standalone HTML app existed in this source folder.')
    add_card(cards,'What to adopt from every version','Comparison','The 21-entry comparison board, recommendations and evidence from the review preceding 08.', [('Open comparison board',prefix+'08-adoption-review/index.html'),('Read adoption report',prefix+'08-adoption-review/REPORT.md')],None,'Historical comparison snapshot. Archive links above include the subsequently built version 08.')
    for card in cards:
        for link in card['links']:
            if not (ROOT/link['path']).is_file(): raise RuntimeError(f'Broken index target: {link}')
        if card['image'] and not (ROOT/card['image']).is_file(): raise RuntimeError(f'Missing thumbnail: {card["image"]}')
    (ROOT/'catalog.json').write_text(json.dumps(cards,indent=2),encoding='utf-8')
    groups=['All']+list(dict.fromkeys(card['group'] for card in cards))
    buttons=''.join(f'<button data-filter="{html.escape(group)}" aria-pressed="{str(group=="All").lower()}">{html.escape(group)}</button>' for group in groups)
    content=''
    for card in cards:
        image=f'<a class="preview-image" href="{html.escape(card["image"])}" target="_blank"><img loading="lazy" src="{html.escape(card["image"])}" alt="{html.escape(card["title"])} screenshot"></a>' if card['image'] else '<div class="text-preview">Preserved source files</div>'
        links=''.join(f'<a class="open-link" href="{html.escape(link["path"])}">{html.escape(link["label"])}</a>' for link in card['links'])
        content+=f'<article data-group="{html.escape(card["group"])}" data-search="{html.escape((card["title"]+" "+card["description"]).lower())}">{image}<div class="card-copy"><p class="category">{html.escape(card["group"])}</p><h2>{html.escape(card["title"])}</h2><p>{html.escape(card["description"])}</p><div class="links">{links}</div><p class="note">{html.escape(card["note"])}</p></div></article>'
    page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>LSAT U dashboard versions</title><link rel="icon" href="data:,"><link rel="stylesheet" href="archive.css"></head><body><header><a href="../../README.md">Design folder</a><p class="category">LSAT U · LOCAL DESIGN ARCHIVE</p><h1>Every version, kept together.</h1><p>Browse the original dashboards, Claude studies, Codex iterations and intermediate passes. Open any preview directly from these files. The originals in Downloads are preserved.</p><p><a class="latest-link" href="{new}08-combined-home/index.html">Open the latest combined Home →</a></p><label for="search">Find a version</label><input id="search" type="search" placeholder="Try Atmosphere, Carrel, motion or saved"><nav class="filters" aria-label="Filter archive">{buttons}</nav><p id="count" role="status" aria-live="polite">{len(cards)} labelled entries</p></header><main class="cards">{content}</main><footer><p>Local reference archive · Sample-data prototypes and historical evidence. No production connection or deployment. Older studies retain their original copy and behavior.</p><p><a href="README.md">Archive guide and provenance</a> · <a href="archive-manifest.json">Verified file manifest</a> · <a href="catalog.json">Version catalogue</a></p></footer><script>let group='All';function filter(){{let n=0;const query=document.querySelector('#search').value.toLowerCase().trim();document.querySelectorAll('article').forEach(a=>{{a.hidden=(group!=='All'&&a.dataset.group!==group)||(query&&!a.dataset.search.includes(query));if(!a.hidden)n++}});document.querySelector('#count').textContent=n+' labelled entries';}}document.querySelectorAll('[data-filter]').forEach(b=>b.addEventListener('click',()=>{{group=b.dataset.filter;document.querySelectorAll('[data-filter]').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));filter();}}));document.querySelector('#search').addEventListener('input',filter);</script></body></html>'''
    (ROOT/'index.html').write_text(page,encoding='utf-8')
    (ROOT/'archive.css').write_text('''*{box-sizing:border-box}:root{color-scheme:light;font-family:system-ui,sans-serif;color:#252b26;background:#f7f4ee}body{margin:0}header,main,footer,.file-list{max-width:1450px;margin:auto;padding:32px}header{max-width:1450px}h1{font:400 clamp(32px,4vw,54px)/1.1 Georgia,serif;margin:16px 0}h2{font:400 27px/1.2 Georgia,serif;margin:8px 0 16px}p{max-width:86ch;line-height:1.65}a{color:#244c65;text-underline-offset:3px}a:focus-visible,button:focus-visible,input:focus-visible{outline:3px solid #244c65;outline-offset:3px}.category{font-size:12px;letter-spacing:.06em;color:#5a6058}.latest-link{display:inline-block;padding:12px 18px;background:#252b26;color:#f7f4ee;border-radius:6px;text-decoration:none}label{display:block;font-size:13px;font-weight:600;margin:24px 0 8px}input{width:min(100%,520px);font:inherit;border:1px solid #85877d;padding:12px;border-radius:6px;background:#fcfaf6;color:inherit}.filters{display:flex;flex-wrap:wrap;gap:8px;margin-top:20px}button{font:inherit;font-size:13px;min-height:44px;padding:9px 14px;border:1px solid #85877d;border-radius:6px;background:transparent;color:inherit;cursor:pointer}button[aria-pressed=true]{background:#252b26;color:#f7f4ee}.cards{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px}article{border:1px solid #d3d2c8;background:#fcfaf6;border-radius:9px;overflow:hidden}article[hidden]{display:none}.preview-image{display:block;height:240px;overflow:hidden;background:#e7e6df}.preview-image img{display:block;width:100%;height:100%;object-fit:cover;object-position:top}.text-preview{height:120px;display:flex;align-items:center;justify-content:center;background:#ebeae1;font:24px Georgia,serif;color:#66685d}.card-copy{padding:22px}.card-copy p{font-size:14px}.links{display:flex;flex-wrap:wrap;gap:12px}.open-link{padding-block:7px;font-size:14px}.note{color:#62665c;font-size:12px!important}footer{font-size:13px}.evidence-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}.shot{display:block;border:1px solid #c9ccc0;overflow:hidden;border-radius:6px}.shot img{width:100%;height:230px;object-fit:cover;object-position:top;display:block}.shot span{display:block;padding:12px;overflow-wrap:anywhere;font-size:12px}.file-list li{margin-block:10px;overflow-wrap:anywhere}@media(max-width:1050px){.cards,.evidence-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}@media(max-width:650px){header,main,footer,.file-list{padding:20px}.cards,.evidence-grid{grid-template-columns:minmax(0,1fr)}h1{font-size:36px}.preview-image{height:250px}}''',encoding='utf-8')
    return cards


def main():
    if ROOT.exists(): raise RuntimeError(f'Destination already exists: {ROOT}; inspect before writing.')
    ROOT.mkdir(parents=True)
    for key, source in SOURCES:
        copy_family(key, source)
        print(f'Copied and hash-verified {key}',flush=True)
    for pattern in ('Refined · LSAT U student home*.html','Studio · LSAT U*.html'):
        for source in DOWNLOADS.glob(pattern): copy_verified(source,ROOT/'saved-pages'/source.name,'saved-pages')
    # Save initial manifest before any optional portable localization.
    (ROOT/'archive-manifest.json').write_text(json.dumps({'date':'2026-10-24','files':MANIFEST},indent=2),encoding='utf-8')
    localize_runtime()
    cards=build_index()
    (ROOT/'portable-changes.json').write_text(json.dumps({'changes':DERIVED,'dependencies':VENDOR},indent=2),encoding='utf-8')
    size=sum(item['bytes'] for item in MANIFEST)
    (ROOT/'README.md').write_text(f'''# LSAT U dashboard versions\n\nOpen [index.html](index.html) to browse **{len(cards)} labelled entries**. This works as a local file and does not depend on the temporary preview servers.\n\n## What is saved\n\n- `families/`: complete byte-identical snapshots of the seven dashboard/motion source folders plus the adoption comparison folder. Includes source, images, reports, recordings, earlier captures and intermediate backups.\n- `saved-pages/`: the standalone SingleFile Refined and Studio saves.\n- `open/`: separate portable copies of the first directions, Claude Code v2 and preserved pass 3. Only these copies have font/GSAP dependencies localized. Pass-3 shared-asset layout is repaired here; raw backup originals remain unchanged.\n- `vendor/`: public font and GSAP dependencies needed by those portable copies.\n- `evidence/`: navigable image/recording/report indexes. These add navigation and do not alter preserved evidence.\n- `archive-manifest.json`: {len(MANIFEST)} copied files, {size:,} source bytes, original locations and verified SHA-256 hashes.\n- `portable-changes.json`: explicit derived-file changes and dependency URL mapping.\n- `catalog.json`: the labelled version list used by the browser index.\n\n## Versions and labels\n\nOriginal role screenshots and handoff exports; Broadsheet, Meridian and Therefore; Lamplight, Carrel and Marginalia; their intermediate pass-3 backups; New Directions 01 Lumen, 02 Margin, 03 Studio, 04 Refined, 05 Studio colour study, 06 Refined Studio, 07 Atmosphere, 08 Combined Home; standalone saved Refined/Studio; both motion demos; LexPrep motion refinement evidence; the adoption comparison board and report.\n\nThe saved Refined and Studio files are snapshots of 04 and 03 charcoal respectively. The original dashboard and LexPrep folders contain evidence rather than a standalone application; the index labels them accordingly. Exact authorship of every early artifact file is not established. Historical test reports stay historical.\n\n## Preservation and limits\n\nAll original source folders in Downloads remain untouched. Every copied source file was hashed before and after copying and compared with the destination. No source symlinks were followed. Existing provenance files are preserved verbatim; old absolute paths in historical notes remain historical paths. Use this archive's index for current local navigation.\n\nThese are local reference studies and historical signed-in screenshots, not a public website. No publishing, Git commit/push, application migration or production change was performed. Some historical images may contain account or student information; no anonymity claim is made.\n\nDo not infer production acceptance from a local preview or screenshot. Version 08 remains a sample-data prototype, not live-data integration. Browser validation of the copied archive is recorded separately in `archive-check.json`.\n''',encoding='utf-8')
    print(json.dumps({'archive':str(ROOT),'files':len(MANIFEST),'entries':len(cards),'source_bytes':size,'vendor_files':len(VENDOR)}),flush=True)


if __name__ == '__main__': main()
