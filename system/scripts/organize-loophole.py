"""Preserve and route the authorized Loophole source batches; never move originals."""
from pathlib import Path
import hashlib, json, shutil, re, os, sys

ROOT = Path(__file__).resolve().parents[2]
HOME = ROOT / 'corpus/loophole-online'
CAPTURES = ROOT / 'Loophole Lecture'
ARCHIVE = ROOT / 'raw/sources/loophole-rc-2026-10-14'
DAYS = [('One', 1), ('Two', 2), ('Three', 3), ('Six', 6), ('Seven', 7)]

def digest(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()

def link(label, target, owner=HOME):
    return f'[{label}](<{Path(os.path.relpath(target, owner)).as_posix()}>)'

def generated(path, text):
    expected = path.read_bytes() if path.exists() else None
    path.parent.mkdir(parents=True, exist_ok=True)
    if (path.read_bytes() if path.exists() else None) != expected:
        raise RuntimeError(f'Concurrent change: {path}')
    path.write_text(text, encoding='utf-8')

def preserve(source, destination):
    before = digest(source)
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        assert digest(destination) == before, f'Archive conflict: {destination}'
    else:
        shutil.copyfile(source, destination)
    assert digest(source) == before == digest(destination)
    return before

CATALOG_ONLY = '--catalog-only' in sys.argv
if CATALOG_ONLY:
    data = json.loads((HOME/'source-catalog.generated.json').read_text(encoding='utf-8'))
    catalog, old, related, legacy = (data[k] for k in ['lectures','recovered_sources','related_recovered_notes','legacy_sufficient_assumption'])
    extra, supplements, manifest, summary = (data[k] for k in ['other_archive_files','batch_supplements','preserved_copies','source_summaries'])
else:
    catalog = []
    summary = []
    manifest = []
    supplements = []
    for word, number in DAYS:
        batch = CAPTURES / f'Day {word}'
        archive = ARCHIVE / f'day-{number}'
        inventory = json.loads((batch / 'inventory.json').read_text(encoding='utf-8'))
        evidence_parts = []
        originals = {json.loads(p.read_text(encoding='utf-8'))['url']: p for p in batch.glob('*/source.json')}
        for order, lesson in enumerate(inventory, 1):
            source = originals[lesson['url']]
            folder = source.parent
            d = json.loads(source.read_text(encoding='utf-8'))
            dest = archive / f'video-{order:02}'
            if not (folder/'README.md').exists():
                note_link = link('Captured written notes',folder/'ellens-notes.html',folder) if (folder/'ellens-notes.html').exists() else 'Written notes were not checked in this original capture.'
                generated(folder/'README.md', '# '+d['title']+'\n\nSource: '+d['url']+'\n\n'+link('Timestamped transcript',folder/(folder.name+'.md'),folder)+' | [Native captions](source.vtt) | [Video](video.mp4) | [Audio](audio.m4a) | [Frames](images/)\n\n'+note_link+'\n\n[Source metadata](source.json) | [Provenance](PROVENANCE.md) | [Verification](verification.json) | [Hashes](SHA256SUMS)\n\n'+link('Main Loophole library',HOME/'README.md',folder)+' | '+link('RC methods and lectures',HOME/'reading-comprehension/README.md',folder)+' | '+link('Filing router',HOME/'ROUTER.md',folder)+'\n\nAutomatic captions have not been checked word by word against audio.\n')
            records = []
            for name in ['source.json', 'source.vtt', 'ellens-notes.txt', 'ellens-notes.html', 'notes-capture.json', 'notes-status.txt']:
                original = folder / name
                if original.exists():
                    value = preserve(original, dest / name)
                    records.append({'file': name, 'sha256': value})
                    manifest.append({'original': str(original.relative_to(ROOT)), 'archive': str((dest/name).relative_to(ROOT)), 'sha256': value})
            notes_file = folder/'ellens-notes.txt'
            notes_status = 'captured' if notes_file.exists() else ('not checked in original capture' if 'notes' not in d else 'not rendered')
            notes_text = notes_file.read_text(encoding='utf-8') if notes_file.exists() else notes_status
            evidence_parts.append('# '+d['title']+'\n\nSource: '+d['url']+'\n\n'+(folder/'source.vtt').read_text(encoding='utf-8')+'\n\nWritten notes:\n'+notes_text+'\n')
            catalog.append({'domain':'Reading Comprehension', 'day':number, 'order':order, 'title':d['title'], 'folder':str(folder.relative_to(ROOT)), 'source':str(source.relative_to(ROOT)), 'sha256':digest(folder/'source.vtt'), 'notes': notes_file.exists(), 'notes_status':notes_status, 'archived':str(dest.relative_to(ROOT)), 'artifacts':records})
        video_dirs = {p.parent for p in originals.values()}
        for extra_path in sorted(batch.rglob('*')):
            if not extra_path.is_file() or any(parent in video_dirs for parent in extra_path.parents):
                continue
            if extra_path.suffix.lower() not in ['.md','.png','.txt','.html'] or extra_path.name=='SHA256SUMS':
                continue
            supplements.append({'day':number,'source':str(extra_path.relative_to(ROOT)),'sha256':digest(extra_path)})
        evidence = archive / 'evidence.md'
        joined = '\n\n'.join(evidence_parts)
        if evidence.exists():
            if evidence.read_text(encoding='utf-8') != joined:
                # Derived combined evidence revisions are retained, never overwritten.
                evidence = archive / ('evidence-'+hashlib.sha256(joined.encode()).hexdigest()[:12]+'.md')
                if evidence.exists(): assert evidence.read_text(encoding='utf-8') == joined
                else: generated(evidence, joined)
        else:
            generated(evidence, joined)
        generated(archive/'PROVENANCE.md', f'# Day {number} preserved evidence\n\nCaptured 2026-10-14. Original capture home: {batch.relative_to(ROOT)}. Each video retains byte-identical source JSON, native VTT and written notes when present. Copies verified by SHA-256. evidence.md is a separately derived concatenation for source-summary retrieval; original files remain unchanged. Video/audio/frames stay in the original capture home and are linked through its provenance and SHA256SUMS. Caption wording has not been checked word by word against audio. Temporary signed media references in source JSON are private archival metadata, not navigation links to publish.\n')
        hashes = [digest(p)+'  '+p.relative_to(archive).as_posix() for p in sorted(archive.rglob('*')) if p.is_file() and p.name!='SHA256SUMS']
        generated(archive/'SHA256SUMS', '\n'.join(hashes)+'\n')
        owner = ROOT/'wiki/sources'
        page = owner/f'loophole-rc-day-{number}-2026-10-14.md'
        # Exact quotes selected from original notes or native caption cue text, never paraphrased.
        candidates = []
        for part in evidence_parts:
            for line in part.splitlines():
                line = line.strip()
                if 30 < len(line) < 180 and not line.startswith(('#','Source:', 'WEBVTT')) and '-->' not in line and not re.match(r'^\d+$', line) and '"' not in line:
                    candidates.append(line)
        quotes = list(dict.fromkeys(candidates))[:2]
        note_count = sum(1 for item in catalog if item.get('day')==number and item['notes'])
        text = f'''---
    type: source
    subject: Loophole RC Day {number} lecture captures
    created: 2026-10-14
    updated: 2026-10-14
    aliases: [Loophole Day {number}, RC Plan Day {number}]
    evidence: {os.path.relpath(evidence, owner).replace(chr(92), '/')}
    sha256: {digest(evidence)}
    contradictions: []
    sources:
      - {os.path.relpath(evidence, owner).replace(chr(92), '/')}
    ---

    # Day {number}: preserved lecture sources and written notes

    Ellen Cassidy / Loophole Online. Publication dates unknown. Captured 2026-10-14 in the signed-in Codex browser; organized into the second brain 2026-10-14. This batch contains {len(inventory)} lectures and {note_count} written-notes sections.

    ## What is preserved

    {link('Ordered lecture and media index', batch/'README.md', owner)}. Native automatic captions, full written notes when present, original video/audio and sampled frames are retained. Notes and spoken captions remain separate evidence. {link('Preserved evidence and hashes', archive/'PROVENANCE.md', owner)}.

    ## Meaning and placement

    {link('Reading Comprehension home', HOME/'reading-comprehension/README.md', owner)} routes the methods, question strategies and examples. {link('Source comparison and content review', batch/'comparison.md', owner)} carries the existing source-specific analysis and suspected recognition errors. This organization imports and connects that work; it does not certify every spoken word or adopt vendor claims as approved curriculum.

    ## Mentions in source

    '''+ '\n'.join('> "'+q+'" (native caption or written-note evidence)' for q in quotes)+f'''

    ## Limits and open work

    Automatic caption errors and instructor claims retain their qualifications. Existing comparisons preserve unresolved wording/timing differences; nothing is silently reconciled. Signed-in question-panel access and answer keys were not established by lecture capture. The source is routed to {link('the complete catalog', HOME/'source-catalog.generated.md', owner)} and {link('RC methods', HOME/'reading-comprehension/README.md', owner)}. Existing drill practices are reference material, not newly assigned student work.
    '''
        queue_ids = {1:['LQ-001'],2:['LQ-002','LQ-003'],3:['LQ-003'],6:['LQ-001','LQ-004'],7:['LQ-004']}[number]
        text += '\n## Queue record\n\nSource-proposed adoption reviews are new, not approved: '+', '.join(queue_ids)+'. See [LSAT U idea queue](../lsatu-idea-queue.md). Existing teaching references are already filed; recording a proposal does not change student assignments or approve a source prescription.\n'
        if number==1:
            text+='\nDay One notes coverage: only the Decaf video-page notes were later recovered. The other ten pages were not checked for notes in the original capture. Their absence from the archive does not establish absence from the website.\n'
        generated(page,text)
        summary.append(str(page.relative_to(ROOT)))

    old_root = ROOT/'raw/sources/old-obsidian-vault-2026-10-07/Clippings/loophole-online'
    old = []
    for path in sorted(old_root.rglob('*')):
        if not path.is_file(): continue
        if path.suffix.lower()!='.md': continue
        title=path.stem
        lower=title.lower()
        if 'just a detail' in lower: domain='Excluded teaching content: SQL migration capture'
        elif any(s in lower for s in ['decaf',' rc ','rc translation','comparative']): domain='Reading Comprehension'
        elif any(s in lower for s in ['conditional','assumption','weaken','strengthen','unless','clir','stimulus','flaw','objection','method','principle']): domain='Logical Reasoning'
        else: domain='Shared / mixed reference'
        old.append({'domain':domain,'title':title,'source':str(path.relative_to(ROOT)),'sha256':digest(path)})
    related = []
    matrix = (ROOT/'research/obsidian-vault-comparison/2026-10-07/teaching-active-coverage.md').read_text(encoding='utf-8')
    for name in re.findall(r'^\| `([^`]+)` \|', matrix, re.M):
        if name.startswith('Clippings/loophole-online/'):
            continue
        p = ROOT/'raw/sources/old-obsidian-vault-2026-10-07'/name
        if p.exists() and p.is_file():
            related.append({'source':str(p.relative_to(ROOT)), 'sha256':digest(p)})

    legacy = []
    for p in sorted((CAPTURES/'Sufficient Assumption').rglob('*')):
        if p.is_file():legacy.append({'source':str(p.relative_to(ROOT)), 'sha256':digest(p)})
    extra=[]
    for p in CAPTURES.rglob('*'):
        if not p.is_file():continue
        if any(part in p.parts for part in ['Day One','Day Two','Day Three','Day Six','Day Seven','Sufficient Assumption']):continue
        extra.append(str(p.relative_to(ROOT)))

    data={'date':'2026-10-14','lectures':catalog,'recovered_sources':old,'related_recovered_notes':related,'legacy_sufficient_assumption':legacy,'other_archive_files':extra,'batch_supplements':supplements,'preserved_copies':manifest,'source_summaries':summary}


# Refresh navigation only from existing captures. --catalog-only never writes raw evidence.
camo_folder = CAPTURES/'Camo'
camo_json = camo_folder/'how-to-camo-source.json'
camo = json.loads(camo_json.read_text(encoding='utf-8'))
data['date'] = '2026-10-15'
for source_page in ['wiki/sources/loophole-how-to-camo-2026-10-15.md','wiki/sources/loophole-lr-recordings-2026-10-15.md','wiki/sources/loophole-workouts-2026-10-14.md','wiki/sources/loophole-routines-2026-10-15.md']:
    if source_page not in summary:
        assert (ROOT/source_page).is_file(), 'Missing source summary: '+source_page
        summary.append(source_page)
data['source_summaries'] = summary
data['shared_lectures'] = [{
    'title': camo['title'], 'folder': str(camo_folder.relative_to(ROOT)),
    'source': str(camo_json.relative_to(ROOT)), 'source_sha256': digest(camo_json),
    'transcript': str((camo_folder/'how-to-camo-transcript.md').relative_to(ROOT)),
    'transcript_sha256': digest(camo_folder/'how-to-camo-transcript.md'),
    'caption_segments': len(camo['segments']), 'duration_seconds': camo['duration_seconds'],
    'caption_type': camo['caption_type'], 'capture_scope': 'transcript only; no new media capture',
    'source_summary': 'wiki/sources/loophole-how-to-camo-2026-10-15.md'
}]
def native_collection(dirname, sections):
    rows = []
    for source in sorted((CAPTURES/dirname).glob('*/source.json')):
        folder = source.parent
        record = json.loads(source.read_text(encoding='utf-8-sig'))
        verification = folder/'verification.json'
        status = json.loads(verification.read_text(encoding='utf-8')) if verification.exists() else {}
        artifacts = {}
        for name in ['source.vtt', 'native-transcript.md', 'ellens-notes.txt',
                     'inline-bootcamp.md', 'book-excerpt.md']:
            path = folder/name
            if path.is_file():
                artifacts[name] = {'source': str(path.relative_to(ROOT)), 'sha256': digest(path)}
        rows.append({
            'title': record['title'], 'url': record['url'], 'sections': sections,
            'folder': str(folder.relative_to(ROOT)), 'source': str(source.relative_to(ROOT)),
            'source_sha256': digest(source), 'artifacts': artifacts,
            'notes_status': status.get('notes_status', 'see source record'),
            'media_complete': status.get('media_complete', False),
            'supplements_complete': status.get('supplements_complete', False),
            'supplement_coverage': status.get('supplement_coverage', {}),
            'complete': status.get('complete', False)})
    return rows

data['conditional_lectures'] = native_collection('Conditional Reasoning 2026-10-18', ['LR'])
data['rc_activity_lectures'] = native_collection('RC Activity Demos 2026-10-18', ['RC'])
for row in data['rc_activity_lectures']:
    if row['url'].rsplit('/', 1)[-1] in {'how-to-camo', 'mission-matching-and-clir-matching', 'how-and-why-to-enter-party-tricking-jail'}:
        row['sections'] = ['LR', 'RC']
if data['conditional_lectures']:
    data['date'] = '2026-10-18'
    conditional_summary = 'wiki/sources/loophole-conditionals-2026-10-18.md'
    if (ROOT/conditional_summary).is_file() and conditional_summary not in summary:
        summary.append(conditional_summary)
rc_summary = 'wiki/sources/loophole-rc-activity-demos-2026-10-18.md'
if data['rc_activity_lectures'] and (ROOT/rc_summary).is_file() and rc_summary not in summary:
    summary.append(rc_summary)
workouts = json.loads((HOME/'workouts/catalog.generated.json').read_text(encoding='utf-8'))
routines = json.loads((HOME/'routines/catalog.generated.json').read_text(encoding='utf-8'))
points = workouts['prep_map_points']
routine_points = json.loads((ROOT/'raw/sources/loophole-routines-2026-10-15/prep-points.json').read_text(encoding='utf-8'))
assert not ({p['url'] for p in points} & {p['url'] for p in routine_points}), 'Prep-map generations overlap; review identities'
data['collections'] = [
    {'kind':'workouts','count':len(workouts['workouts']),'route':'corpus/loophole-online/workouts/README.md','catalog':'corpus/loophole-online/workouts/catalog.html','source_summary':'wiki/sources/loophole-workouts-2026-10-14.md'},
    {'kind':'routines','count':len(routines['routines']),'ordered_steps':sum(len(r['sequence']) for r in routines['routines']),'route':'corpus/loophole-online/routines/README.md','catalog':'corpus/loophole-online/routines/catalog.html','source_summary':'wiki/sources/loophole-routines-2026-10-15.md'},
    {'kind':'prep-map','count':len(points)+len(routine_points),'workout_points':len(points),'routine_supplements':len(routine_points),'captured':sum(p.get('status')!='source-error' for p in points+routine_points),'source_errors':sum(p.get('status')=='source-error' for p in points+routine_points),'route':'corpus/loophole-online/workouts/prep-map-points/README.md'},
    {'kind':'LR question database','snapshot_date':'2026-10-15','source_summary':'wiki/sources/loophole-lr-recordings-2026-10-15.md','questions':5015,'audio_questions':713,'speech_transcripts':712,'unique_sources':659,'unique_speech':658,'silent_sources':1,'available_subtitles':710,'timing_exceptions':2,'route':'corpus/loophole-online/question-database/README.md','catalog':'corpus/loophole-online/question-database/library/index.html','reading_home':'corpus/loophole-online/question-database/library','status':'verified source inventory; portable-copy verification remains in the library report'}
]
extra = sorted(str(p.relative_to(ROOT)) for p in CAPTURES.rglob('*') if p.is_file() and not any(part in p.parts for part in ['Day One','Day Two','Day Three','Day Six','Day Seven','Sufficient Assumption','Camo','Conditional Reasoning 2026-10-18','RC Activity Demos 2026-10-18']))
data['other_archive_files'] = extra
prep_owner = HOME/'workouts/prep-map-points'
prep_md = '# Prep-map captures and source availability\n\n[Loophole home](../../README.md) | [All workouts](../README.md) | [All routines](../../routines/README.md)\n\nThe workout collection checked 62 distinct prep-map URLs: 29 working captures and 33 source-error pages. Five additional working routine-linked pages are embedded in the complete routine sourcebooks. These are 67 distinct source URL records, with 34 working captures and 33 explicit source errors. A saved error response is evidence of a failed capture, not recovered instruction.\n\n## Workout-linked captures\n\n| Prep-map point | Capture status | Exact local content |\n|---|---|---|\n'
by_url = {}
for source in sorted(prep_owner.glob('*/source.json')):
    item = json.loads(source.read_text(encoding='utf-8'))
    by_url[item['url']] = source
for item in points:
    source = by_url[item['url']]
    title = (item.get('name') or item['url'].rsplit('/',1)[-1]).replace('|',' / ')
    prep_md += '| '+title+' | '+item.get('status','captured')+' | '+link('Text',source.parent/'text.txt',prep_owner)+' / '+link('HTML',source.parent/'original.html',prep_owner)+' / '+link('Metadata',source,prep_owner)+' |\n'
prep_md += '\n## Additional routine-linked captures\n\nFull authored instructions remain embedded in their owning routine sourcebooks; this index adds retrieval routes without a second interpretation.\n\n'
for point in routine_points:
    owners = [r for r in routines['routines'] if any(p.get('url')==point['url'] for p in r.get('inline_prep',[]))]
    assert owners, 'Routine prep capture has no sourcebook owner: '+point['url']
    prep_md += '- '+(point.get('name') or point['url'].rsplit('/',1)[-1])+': '+', '.join(link(r['name'], HOME/'routines'/r['slug']/'README.md',prep_owner) for r in owners)+'\n'
generated(prep_owner/'README.md', prep_md)

generated(HOME/'source-catalog.generated.json',json.dumps(data,ensure_ascii=False,indent=2)+'\n')
md='''---
type: synthesis
subject: Complete Loophole source catalog
created: 2026-10-14
updated: 2026-10-15
aliases: [Loophole source map, Loophole inventory]
contradictions: []
---

# Every source has a route and a preserved home

Generated by system/scripts/organize-loophole.py. [Start here](README.md) | [Routing rules](ROUTER.md) | [Machine-readable identities and hashes](source-catalog.generated.json).

Sources are retained at their existing paths. The RC batches have byte-verified evidence copies in raw/sources/loophole-rc-2026-10-14; media remain at their original paths. Original captions are automatic, and source notes are distinct from speech. No missing day is inferred to have been captured.

## New RC lectures in course order

| Day / order | Lecture and artifacts | Written notes | Native-caption SHA-256 |
|---|---|---|---|
'''
for d in catalog:
    folder=ROOT/d['folder']
    notes=link('Exact text',folder/'ellens-notes.txt')+' / '+link('HTML',folder/'ellens-notes.html') if d['notes'] else d['notes_status']
    md+=f'| {d["day"]} / {d["order"]} | {link(d["title"],folder/"README.md")} | {notes} | `{d["sha256"]}` |\n'
if data['conditional_lectures']:
    md += '\n## Conditional reasoning and directly prescribed support, 2026-10-18\n\n'
    md += link('Conditional source hub', HOME/'logical-reasoning/conditionals/README.md') + '\n\n'
    md += '| Lecture | Package status | Searchable retained source artifacts |\n|---|---|---|\n'
    for row in data['conditional_lectures']:
        artifacts = ' / '.join(link(name, ROOT/item['source']) for name, item in row['artifacts'].items())
        md += '| '+link(row['title'], ROOT/row['folder']/'README.md')+' | '+('complete observed artifacts' if row['complete'] else 'partial; see verification')+' | '+artifacts+' |\n'
if data['rc_activity_lectures']:
    md += '\n## RC activity demonstrations, 2026-10-18\n\n'
    md += link('RC activity demo hub', HOME/'reading-comprehension/activity-demos.md') + '\n\n'
    md += '| Lecture | Package status | Retained artifacts |\n|---|---|---|\n'
    for row in data['rc_activity_lectures']:
        artifacts = ' / '.join(link(name, ROOT/item['source']) for name, item in row['artifacts'].items())
        md += '| '+link(row['title'], ROOT/row['folder']/'README.md')+' | '+('complete observed artifacts' if row['complete'] else 'partial; see verification')+' | '+artifacts+' |\n'
md+='\n## Shared lecture captured on 2026-10-15\n\n'+link('How to Camo: full native transcript',camo_folder/'how-to-camo-transcript.md')+' | '+link('Capture metadata',camo_json)+' | '+link('Source summary',ROOT/'wiki/sources/loophole-how-to-camo-2026-10-15.md')+'\n\n54 automatic-caption segments; 8:25 video runtime. Transcript-only capture: no new audio, video, notes or frames are claimed. Original caption wording is unreviewed and unchanged. The older recovered How to Camo source below remains a distinct generation.\n\n## Complete workout, routine and question collections\n\n'
for collection in data['collections']:
    md+='- '+link(collection['kind'],ROOT/collection['route'])+': '+json.dumps({k:v for k,v in collection.items() if k not in ['route','catalog','source_summary','reading_home','kind']},ensure_ascii=False)+'.'
    if collection.get('catalog'): md+=' '+link('Searchable local catalog',ROOT/collection['catalog'])+'.'
    if collection.get('source_summary'): md+=' '+link('Source summary',ROOT/collection['source_summary'])+'.'
    md+='\n'
md+='\nQuestion collection totals are the pinned 2026-10-15 verified source snapshot and describe exposed source coverage and verified transcripts, with a silent source and subtitle exceptions explicit. See the canonical library verification for copied-byte and local-link integrity. Counts are not evidence of human accuracy review.\n'
md+='\n## Original recovered source files\n\nAll retained Markdown files from the original Loophole tree, classified for navigation; shared/mixed means the title alone does not justify an exclusive RC/LR assignment. Full operational context remains in the method library and subject routes.\n\n| Subject route | Source | SHA-256 |\n|---|---|---|\n'
for d in old:md+=f'| {d["domain"]} | {link(d["title"],ROOT/d["source"])} | `{d["sha256"]}` |\n'
md+='\n## Related recovered notes outside the old Loophole subtree\n\nThese are related references, not all instructor-authored course material. Their existing source-audit dispositions remain authoritative.\n\n'
for d in related:md+='- '+link(Path(d['source']).name, ROOT/d['source'])+'\n'
md+='\n## New source summaries and preservation records\n\n'
for p in summary:md+='- '+link(Path(p).stem,ROOT/p)+'\n'
md+='\n## Older Sufficient Assumption capture\n\n'+link('Logical Reasoning route',HOME/'logical-reasoning/README.md')+' | '+link('Original package',CAPTURES/'Sufficient Assumption/README.md')+'\n\nOlder claims of verbatim completeness and visual verification remain historical until checked against original media. Every retained file is listed below.\n\n'
for d in legacy:md+='- '+link(Path(d['source']).name,ROOT/d['source'])+'\n'
md+='\n## Batch comparisons, checkpoint and screenshots\n\nThe checkpoint is a separately supplied screenshot, filed beside Day Three without claiming that was its original timeline day. Comparisons and indexes are derived work, not original instructor speech.\n\n'
for d in supplements:md+='- Day '+str(d['day'])+': '+link(Path(d['source']).name,ROOT/d['source'])+'\n'
md+='\n## Other files and related records\n\n'
for p in extra:md+='- '+link(Path(p).name,ROOT/p)+'\n'
md+='\n'+link('Historical recovered-source audit, including the five related notes outside the tree',ROOT/'research/obsidian-vault-comparison/2026-10-07/teaching-active-coverage.md')+'\n\n'+link('Original overview and retained caveats',HOME/'index.md')+'\n'
md = md.replace('updated: 2026-10-15', 'updated: '+data['date'], 1)
generated(HOME/'source-catalog.generated.md',md)
print(json.dumps({'lectures':len(catalog),'notes':sum(x['notes'] for x in catalog),'recovered_markdown':len(old),'legacy_files':len(legacy),'verified_preserved_files':len(manifest),'source_summaries':len(summary)},indent=2))
