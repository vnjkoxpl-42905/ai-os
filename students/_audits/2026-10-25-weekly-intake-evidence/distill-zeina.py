from pathlib import Path
import hashlib

b = Path('students/zeina-borji')
date = '2026-10-22'
name = 'conditional-foundations-and-study-plan'
src = b / 'transcript-downloads' / f'{date}-zeina-borji-notes-by-gemini.md'
raw = src.read_bytes()
text = raw.decode('utf-8-sig')
sha = hashlib.sha256(raw).hexdigest()
p = b / 'sessions' / f'{date}-{name}'
p.mkdir(exist_ok=True, parents=True)
assert not (p / 'transcript.md').exists()
(p / 'transcript.md').write_bytes(raw)
notes = '''- Zeina reported a recent 147 PT and January LSAT goal. Feeling more comfortable with conditionals did not yet yield reliable independent application (00:00:51-00:03:41).
- She called for a conditional indicator and initially defined sufficient as a requirement; both were corrected with prompting. She then correctly diagrammed meaningful participation as sufficient and understanding issues as necessary (00:23:39-00:34:20).
- She initially put some near 50% and excluded all from its maximum, then correctly restated the one-to-all range in the cookie example. Recheck on fresh examples (00:44:31-00:53:49).
- She could identify the contrapositive and distinguish facts from rules with guidance, but needed extensive help matching E to the necessary/sufficient error. This is guided success, not independent mastery (01:03:50-01:07:09; 01:12:17-01:29:08).
- Joshua prioritized accurate conditional recognition/diagramming before question-type application (01:33:24-01:37:22).'''
loops = '''- [ ] Joshua: verify delivery/assignment of conditional boot camp, question sets, notes/recap, statement-type list and claim-strength reference promised during this session. Intake does not send or assign work (00:43:31; 01:19:01; 01:35:05; 01:44:10-01:46:36).
- [ ] Joshua: create the promised study plan and coordinate increased early session frequency. Ten hours and initially twice weekly were proposed, not verified purchased/booked (01:40:09-01:42:41).
- [ ] Joshua: verify the tentative group meeting. Early discussion suggested 2026-10-24/25 and timing by 2026-10-23; later discussion allowed the following weekend, so no fixed appointment is established (00:13:15; 01:42:41).
- [ ] Zeina: complete conditional foundations even when familiar, then apply to assigned questions and send specific questions as needed. Completion unverified (01:44:10-01:45:06).
- [ ] Joshua/Zeina: revisit progress-area navigation after the announced update; neither deployment nor walkthrough verified here (00:16:12-00:18:30).'''
caveat = '''Calendar booking is 2026-10-22 15:30; the native Doc title says 18:33 EDT. Preserve same-date guest-email/content identity without treating booked time as actual start. This is an automatic transcript with recognition errors. Percentage mnemonics are recorded teaching, not exact mathematical definitions: most means more than half; some means at least one rather than a fixed 1% lower bound; modal possibility is not a measured probability. The quick notes overstate a settled UK cancellation: Zeina acknowledged the discussion, reported acceptance and visa, and expressed doubts, but no final cancellation is established. Admissions and cost statements are conversation content, not independently verified guidance.'''
summary = '''Zeina described score frustration and considering the UK. Joshua encouraged a January preparation plan and discussed 155-160 as a target, not a guaranteed outcome. The public-participation parallel-flaw question exposed sufficient/necessary and indicator uncertainty. Guided practice covered rule/fact distinctions, contrapositives, quantifiers, claim type versus argument role, and matching the same error in E. The proposed study sequence was foundation accuracy, then application to must-be-true, parallel, sufficient-assumption and necessary-assumption questions. A ten-hour package with more frequent early sessions and later weekly check-ins was proposed; no payment or booking is established.'''
(p / 'summary.md').write_text(f'# {date} | Zeina Borji | Internal session record\n\nIntake 2026-10-25. [Source export](../../transcript-downloads/{src.name}) · [Full transcript](transcript.md) · [Topic map](topic-map.md) · [Provenance](provenance.md).\n\n## Private distillation\n\n{summary}\n\n{notes}\n\n## Source qualifications and corrections\n\n{caveat}\n\n## Recorded follow-ups\n\n{loops}\n\n## Preserved original Gemini notes\n\nAutomatic notes below are preserved verbatim. Qualifications above are appended intake analysis.\n\n' + text.split('📖 Transcript')[0], encoding='utf-8')
topics = [('00:00:51','Reported PT and January goal'),('00:23:39','Indicator confusion'),('00:27:08','Sufficient versus necessary'),('00:44:31','Some, most, all'),('01:03:50','Contrapositive'),('01:12:17','Rule versus fact'),('01:26:58','Parallel flaw matching'),('01:40:09','Availability and study plan'),('01:44:10','Materials promised')]
(p / 'topic-map.md').write_text('# Topic map\n\nActual source timestamps below; open the full transcript and locate each marker.\n\n| Source time | Topic | Record |\n|---|---|---|\n' + ''.join(f'| {t} | s | [Transcript](transcript.md) |\n'.replace('| s |', f'| {s} |') for t,s in topics) + '\n[Summary](summary.md) · [Teaching notes](../../teaching-notes.md) · [Open loops](../../open-loops.md) · [Student profile](../../zeina-borji.md)\n', encoding='utf-8')
(p / 'provenance.md').write_text(f'# Provenance\n\n- Native Doc: `19Lcsj3EgpyKXgn0MCJF_bcaL2lmrr4l1zHJOHlAyxRk`.\n- [Google Doc](https://docs.google.com/document/d/19Lcsj3EgpyKXgn0MCJF_bcaL2lmrr4l1zHJOHlAyxRk/edit).\n- Intake: 2026-10-25.\n- [Full source export](../../transcript-downloads/{src.name}); package transcript is byte-identical.\n- SHA-256: `{sha}`.\n- [Drive evidence](../../../_audits/2026-10-25-weekly-intake-evidence/drive.json) · [Calendar evidence](../../../_audits/2026-10-25-weekly-intake-evidence/calendar.json).\n- Booked 15:30; Doc title 18:33 EDT. Actual start not inferred.\n', encoding='utf-8')
for file,content in [('teaching-notes.md',notes),('open-loops.md',loops)]:
    with (b/file).open('a',encoding='utf-8') as f:
        f.write(f'\n\n## [{date}] Session intake on 2026-10-25\n\nSource: [full export](transcript-downloads/{src.name}) · [summary and caveats](sessions/{date}-{name}/summary.md).\n\n{content}\n')
q=b/'transcripts.md'
t=q.read_text(encoding='utf-8')
m='|---|---|---|---|'
i=t.index(m)+len(m)
q.write_text(t[:i]+f'\n| {date} | [Full export](transcript-downloads/{src.name}) | [Transcript](sessions/{date}-{name}/transcript.md) · [Summary](sessions/{date}-{name}/summary.md) · [Topic map](sessions/{date}-{name}/topic-map.md) | Native Doc `19Lcsj3EgpyKXgn0MCJF_bcaL2lmrr4l1zHJOHlAyxRk`; full private intake 2026-10-25; [SHA-256 provenance](sessions/{date}-{name}/provenance.md). Booking/title time discrepancy retained. |'+t[i:],encoding='utf-8')
q=b/'zeina-borji.md'
t=q.read_text(encoding='utf-8')
m='## Open this record'
i=t.index(m)+len(m)
t=t[:i]+f'\n\n- [{date} session](sessions/{date}-{name}/summary.md) · [Transcript](sessions/{date}-{name}/transcript.md) · [Topic map](sessions/{date}-{name}/topic-map.md) · [Full export](transcript-downloads/{src.name})'+t[i:]
t+='''\n\n## [2026-10-22] Stated preferences and updated planning\n\nSource: [full export](transcript-downloads/2026-10-22-zeina-borji-notes-by-gemini.md). These newer statements supersede the conflicting older planning snapshot; no prior history is erased.\n\n- January 2027 is her stated LSAT goal; recent self-reported PT was 147. Registration is unverified (00:00:51-00:03:41).\n- She wants more than one session weekly and asked about a package (00:14:52; 01:37:22).\n- She reported switching to part-time work Tuesdays/Wednesdays, 07:30-15:30, to focus on the LSAT. Timezone not spoken; confirm actual availability (01:40:09).\n- She asked to screenshot the claim-strength explanation, supporting a retained visual reference (01:19:01).\n- UK acceptance and visa were reported, with doubts about going; no final cancellation is established (01:45:06-01:46:36).\n'''
q.write_text(t,encoding='utf-8')
assert hashlib.sha256((p/'transcript.md').read_bytes()).hexdigest()==sha
print('Zeina complete',sha)
