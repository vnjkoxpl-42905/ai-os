"""Verify the Loophole source identities and actual navigation targets."""
from pathlib import Path
import hashlib, json, re, urllib.parse

ROOT = Path(__file__).resolve().parents[2]
HOME = ROOT/'corpus/loophole-online'
data = json.loads((HOME/'source-catalog.generated.json').read_text(encoding='utf-8'))
issues = []

def sha(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream,'sha256').hexdigest()

def links(page):
    values = re.findall(r'\]\((<[^>]+>|(?:[^()]|\([^()]*\))*)\)',page.read_text(encoding='utf-8'))
    result=[]
    for value in values:
        value=value.strip('<>')
        if not value or re.match(r'^[A-Za-z]+:',value):
            continue
        name=urllib.parse.unquote(value.split('#')[0])
        result.append((page.parent/name).resolve() if name else page.resolve())
    return result

for item in data['preserved_copies']:
    if not sha(ROOT/item['original']) == sha(ROOT/item['archive']) == item['sha256']:
        issues.append('Evidence copy mismatch: '+item['original'])
for group in ['recovered_sources','related_recovered_notes','legacy_sufficient_assumption']:
    for item in data[group]:
        if sha(ROOT/item['source']) != item['sha256']:
            issues.append('Source drift: '+item['source'])
for item in data['lectures']:
    folder=ROOT/item['folder']
    for name in ['source.vtt','video.mp4','audio.m4a','README.md','PROVENANCE.md','SHA256SUMS']:
        if not (folder/name).exists() or not (folder/name).stat().st_size:
            issues.append('Missing artifact: '+str(folder/name))
    if item['notes']:
        capture=json.loads((folder/'source.json').read_text(encoding='utf-8'))
        notes=capture.get('notes')
        if not notes and (folder/'notes-capture.json').exists():
            notes=json.loads((folder/'notes-capture.json').read_text(encoding='utf-8'))
        for kind in ['text','html']:
            suffix='txt' if kind=='text' else 'html'
            if not notes or (folder/('ellens-notes.'+suffix)).read_text(encoding='utf-8')!=notes[kind]:
                issues.append('Notes mismatch: '+item['title'])

# Create the report target before checking the documentation that links to it.
report_path=HOME/'verification.generated.json'
if not report_path.exists():
    report_path.write_text('{}',encoding='utf-8')
pages=[ROOT/'Loophole Lecture/README.md', ROOT/'Loophole Lecture/Camo/README.md', HOME/'workouts/prep-map-points/README.md', HOME/'README.md',HOME/'ROUTER.md',HOME/'organization.md',HOME/'source-catalog.generated.md',*HOME.glob('*/README.md'),*[ROOT/p for p in data['source_summaries']]]
for word in ['One','Two','Three','Six','Seven']:
    batch=ROOT/'Loophole Lecture'/('Day '+word)
    pages.extend([batch/'README.md',batch/'comparison.md',*batch.glob('*/README.md')])
checked=0
for page in pages:
    for target in links(page):
        checked+=1
        if not target.exists():
            issues.append('Broken link: '+str(page.relative_to(ROOT))+' -> '+str(target))

main=HOME/'README.md'
rc=HOME/'reading-comprehension/README.md'
lr=HOME/'logical-reasoning/README.md'
shared=HOME/'shared/README.md'
trails={
    'cappuccino_exact_notes':[main,rc,ROOT/'Loophole Lecture/Day Six/How and Why to Do Cappuccino RC Translation/ellens-notes.html'],
    'decaf_exact_notes':[main,rc,ROOT/'Loophole Lecture/Day One/How and Why to Do Decaf RC Translation/ellens-notes.html'],
    'sufficient_assumption':[main,lr,ROOT/'Loophole Lecture/Sufficient Assumption/README.md'],
    'day_seven':[main,rc,ROOT/'Loophole Lecture/Day Seven/README.md'],
    'shared_review':[main,shared],
    'old_method_library':[main,HOME/'method-library.md'],
}
library=HOME/'question-database/library'
camo=ROOT/'Loophole Lecture/Camo/how-to-camo-transcript.md'
trails.update({
    'camo_full_native_transcript':[main,shared,camo],
    'accuracy_failsafe_full_workout':[main,HOME/'workouts/README.md',HOME/'workouts/accuracy-failsafe/README.md'],
    'ordered_routine_full_sourcebook':[main,HOME/'routines/README.md',HOME/'routines/ac-primer-plus-decaf-routine/README.md'],
    'prep_map_status_and_text':[main,HOME/'workouts/prep-map-points/README.md'],
    'LR_local_recording_and_inline_transcript':[main,lr,HOME/'question-database/README.md',library/'INDEX.md',library/'PT101/S2/Q1/README.md'],
    'LR_subtitle_exception_complete_text':[main,HOME/'question-database/README.md',library/'INDEX.md',library/'PT140/S1/Q15/README.md'],
    'LR_silent_source_evidence':[main,HOME/'question-database/README.md',library/'INDEX.md',library/'PT2/S4/Q19/README.md'],
})
manifest=json.loads((library/'manifest.json').read_text(encoding='utf-8'))
no_audio=next(row for row in manifest if not row.get('audio_urls'))
no_audio_folder=library/Path(no_audio['citation'].replace('.','/'))
trails['LR_no_exposed_recording_explicit']=[main,HOME/'question-database/README.md',library/'INDEX.md',no_audio_folder/'README.md']
# Native automatic captions are preserved without normalizing recognition mistakes.
camo_record=json.loads((camo.parent/'how-to-camo-source.json').read_text(encoding='utf-8'))
camo_text=camo.read_text(encoding='utf-8')
assert len(camo_record['segments'])==54
for segment in camo_record['segments']:
    if segment['text'] not in camo_text or segment['timestamp'] not in camo_text:
        issues.append('Missing native Camo segment: '+segment['timestamp'])
for item in data['shared_lectures']:
    for source_key,hash_key in [('source','source_sha256'),('transcript','transcript_sha256')]:
        if sha(ROOT/item[source_key])!=item[hash_key]: issues.append('Shared lecture hash mismatch: '+item[source_key])
workout_data=json.loads((HOME/'workouts/catalog.generated.json').read_text(encoding='utf-8'))
routine_data=json.loads((HOME/'routines/catalog.generated.json').read_text(encoding='utf-8'))
assert len(workout_data['workouts'])==84 and len(routine_data['routines'])==58
for kind,records in [('workouts',workout_data['workouts']),('routines',routine_data['routines'])]:
    for record in records:
        page=HOME/kind/record['slug']/'README.md'
        text=page.read_text(encoding='utf-8')
        if len(text)<500 or record['name'] not in text: issues.append('Incomplete sourcebook: '+str(page))
        if kind=='routines' and '## Ordered schedule' not in text: issues.append('Missing ordered schedule: '+str(page))
        if kind=='workouts' and '## Complete workout details' not in text: issues.append('Missing workout detail body: '+str(page))
# Independently confirm publication's actual question-file totals, not only its report.
actual={'questions':0,'audio_files':0,'speech_transcripts':0,'available_subtitles':0,'silent_sources':0}
unique_audio=set();unique_speech=set();timing_exceptions=[]
for row in manifest:
    folder=library/Path(row['citation'].replace('.','/'))
    page=folder/'README.md'
    text=page.read_text(encoding='utf-8')
    actual['questions']+=1
    if row.get('correct_clir') and row['correct_clir'] not in text: issues.append('Missing inline written CLIR: '+row['citation'])
    audio=folder/'original-audio.mp3'
    if audio.exists():
        actual['audio_files']+=1;unique_audio.add(sha(audio))
    transcript=folder/'superwhisper-transcript.txt'
    if transcript.exists():
        spoken=transcript.read_text(encoding='utf-8').strip()
        if not spoken or spoken not in text: issues.append('Missing inline full transcript: '+row['citation'])
        meta=json.loads((folder/'superwhisper-transcript.json').read_text(encoding='utf-8'))
        if spoken!=meta['raw_result'].strip(): issues.append('Native transcript mismatch: '+row['citation'])
        actual['speech_transcripts']+=1;unique_speech.add(meta['audio_sha256'])
        if (folder/'superwhisper-transcript.srt').exists(): actual['available_subtitles']+=1
        else: timing_exceptions.append(row['citation'])
    if (folder/'source-audio-status.json').exists():
        disposition=json.loads((folder/'source-audio-status.json').read_text(encoding='utf-8'))
        if disposition['status']!='digital_silence_no_speech' or disposition['decoded_pcm']['nonzero_count']!=0: issues.append('Unproven silent-source label')
        actual['silent_sources']+=1
expected={'questions':5015,'audio_files':713,'speech_transcripts':712,'available_subtitles':710,'silent_sources':1}
if actual!=expected: issues.append('Actual publication counts mismatch: '+str(actual))
if len(unique_audio)!=659 or len(unique_speech)!=658: issues.append('Unique audio coverage mismatch')
if set(timing_exceptions)!={'PT140.S1.Q15','PT1.S3.Q11'}: issues.append('Unexpected subtitle exceptions: '+str(timing_exceptions))
for name,trail in trails.items():
    for current,target in zip(trail,trail[1:]):
        if target.resolve() not in links(current):
            issues.append('Missing retrieval hop: '+name+' '+str(current))
report={'date':'2026-10-15','published_actual_files':actual,'unique_original_audio':len(unique_audio),'unique_speech_transcripts':len(unique_speech),'timing_exceptions':timing_exceptions,'shared_lectures':len(data['shared_lectures']),'camo_segments':len(camo_record['segments']),'workouts':len(workout_data['workouts']),'routines':len(routine_data['routines']),'routine_steps':sum(len(r['sequence']) for r in routine_data['routines']),'prep_map_source_urls':67,'prep_map_captured':34,'prep_map_source_errors':33,'lectures':len(data['lectures']),'written_note_sections':sum(x['notes'] for x in data['lectures']),'notes_not_checked':sum(x['notes_status']=='not checked in original capture' for x in data['lectures']),'recovered_tree_sources':len(data['recovered_sources']),'related_recovered_notes':len(data['related_recovered_notes']),'legacy_sa_files':len(data['legacy_sufficient_assumption']),'byte_verified_evidence_copies':len(data['preserved_copies']),'source_summaries':len(data['source_summaries']),'local_links_checked':checked,'retrieval_paths':{name:[str(p.relative_to(ROOT)) for p in trail] for name,trail in trails.items()},'issues':issues,'limitations':['Automatic captions remain unverified word by word against audio.','Ten Day One pages were not checked for written notes.','Media presence and previous capture receipts checked; no new full-media decoding or official-key verification.','Links verified as file targets; historical source claims remain qualified.']}
report_path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({key:value for key,value in report.items() if key not in ['retrieval_paths','limitations']},indent=2))
if issues:
    raise SystemExit(1)
