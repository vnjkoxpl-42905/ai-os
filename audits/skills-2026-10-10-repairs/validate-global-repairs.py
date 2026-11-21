import pathlib,json,re,hashlib
O=pathlib.Path('C:/Users/Joshu/dev/ai-os/audits/skills-2026-10-10-repairs');rows=json.loads((O/'global-repairs.json').read_text(encoding='utf-8'))
descriptions={
'firecrawl':'Use Firecrawl for explicitly selected search/scrape/crawl or appropriate web-source collection. Respect explicit browser/tools, official-source requirements and hosted cost authorization; ordinary local file work does not trigger.',
'browser-harness':'Use this installed CDP browser transport for explicitly requested browser interaction when supported. Respect selected browser/tab and prefer purpose-built available tools; not every web question needs browser control.',
'browser':'Use this browser transport when explicitly selected and supported for the requested browser task. Does not authorize public contributions or paid remote browser sessions.',
'firecrawl-parse':'Use explicitly selected Firecrawl remote document conversion when local parsing cannot satisfy the task and upload/credit scope is authorized. Does not trigger on ordinary local Markdown/code paths.',
'frontend-design':'Design requested frontend interfaces while preserving user brief, existing design system, factual data and accessibility. Opinionated legacy creative presets apply only when selected.',
'gws-classroom':'Inspect or operate explicitly Google Classroom API resources. LSAT U classroom/assignment requests route to project lsat-u-platform-actions.',
'docs':'Create or edit documents when requested using available host tools. Read the existing source first; ordinary questions/research do not require document creation.',
'lsat-u-topic-builder':'Explicit legacy topic-builder reference only. New LSAT U topic/module creation uses current bootcamp-builder; preserve useful references without competing automatic triggers.',
}
issues=[]
for r in rows:
 p=pathlib.Path(r['path']);t=p.read_text(encoding='utf-8');n=r['name'];old=t
 if n in descriptions:
  m=re.match(r'---\s*\n(.*?)\n---',t,re.S)
  if m:
   f=re.sub(r'(?ms)^description:.*?(?=^[A-Za-z_][\w-]*:|\Z)','description: '+json.dumps(descriptions[n])+'\n',m.group(1));t='---\n'+f.rstrip()+'\n---'+t[m.end():]
 if n=='claude-api':
  t=t.replace('ask whether they want to switch the file to Claude or want a non-Claude implementation','respect the selected provider and route to its appropriate documentation; do not propose switching providers merely to use this skill')
  t=re.sub(r'Claude-(opus|sonnet|haiku|fable)',lambda m:'claude-'+m.group(1),t)
  t=t.replace('model="claude-opus-5"','model=ACTUAL_VERIFIED_MODEL_ID')
  t=t.replace('client.models.retrieve("claude-opus-5")','client.models.retrieve(ACTUAL_VERIFIED_MODEL_ID)')
 if n=='gws-events':t=t.replace('Agent-task/message streaming entries below are unrelated reference contamination and must not be invoked as Workspace Events.','Agent-task/message streaming methods are not Workspace Events and must not be invoked here.')
 if n=='hatch-pet':
  t=t.replace('Remove prompts, layout guides, generated row strips, extracted frames, PNG intermediates, the 8x9 intermediate atlas, and the imagegen job manifest unless the user wants debug artifacts.','Preserve prompts, layout guides, generated row strips, extracted frames, PNG intermediates, the 8x9 intermediate atlas and the imagegen job manifest. Remove only exact task-owned paths after explicit deletion authorization.')
  t=t.replace('Only mark a visual job complete after its selected output has been copied into the decoded output path.','Only mark a visual job complete after its selected output is copied into decoded and its required deterministic/visual QA passes; repairs must rerun row and whole-sheet QA.')
 if n=='watch':
  t=t.replace('Both keys live in `the current project central .env (do not create another secret store)`. The script prefers Groq when both are set; override with `--whisper openai` to force OpenAI. Use `--no-whisper` to skip the fallback entirely.','Keep keys in the current project central .env and never create a second store. Bundled legacy scripts can read ~/.config/watch/.env or cwd .env and prefer Groq when both are set; do not run their installer. Use --no-whisper by default. Paid fallback runs only with explicit provider/cost authorization and a verified environment/cwd supplying the approved key without printing it.')
  t=t.replace('- Reads / creates `the current project central .env (do not create another secret store)` (mode `0600`) to store the Whisper API key(s) and a `SETUP_COMPLETE` marker. As a fallback, also reads `.env` in the current working directory','- Legacy setup reads/creates ~/.config/watch/.env; it is not run in this workflow. Extraction uses --no-whisper by default. Explicitly approved paid fallback may read central cwd .env/environment after actual helper contract verification; no new secret store is created.')
 if t!=old:
  if p.read_text(encoding='utf-8')!=old:raise RuntimeError(str(p))
  p.write_text(t,encoding='utf-8',newline='')
 r['after_sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
 r['contract']=re.search(r'## Local execution contract \(2026-10-10\)\s*(.*?)(?=\n## Workflow)',t,re.S).group(1).strip()
 fm=re.match(r'---\s*\n(.*?)\n---',t,re.S)
 if not fm or not re.search(r'^name:\s*\S+',fm.group(1),re.M) or not re.search(r'^description:',fm.group(1),re.M):issues.append({'path':str(p),'issue':'frontmatter required fields'})
 if hashlib.sha256(pathlib.Path(r['backup']).read_bytes()).hexdigest()!=r['before_sha256']:issues.append({'path':str(p),'issue':'backup hash'})
 if 'specific acceptance boundary' in t or 'Use the actual host tools and shell; literal Claude Task/Skill/TodoWrite' in t:issues.append({'path':str(p),'issue':'provisional boilerplate'})
 checks={
  'claude-api':['name: Codex-api','Claude-opus-5','Codex API'],
  'academy-guide':['academy.Codex.com'],
  'firecrawl-monitor':['and delete any monitors created for this task'],
  'recipe-find-free-time':['3. Create event','gws calendar +insert'],
  'recipe-create-gmail-filter':['"removeLabelIds": ["INBOX"]'],
  'recipe-copy-sheet-for-new-month':['"sheetId": 123'],
  'using-git-worktrees':['check-ignore -q .worktrees 2>/dev/null ||','Add to .gitignore, commit the change'],
  'qa':['Do NOT ask the user to review first'],
  'test-driven-development':['Delete code. Start over with TDD.','Delete means delete'],
  'writing-skills':['Delete means delete'],
 }
 for bad in checks.get(n,[]):
  if bad in t:issues.append({'path':str(p),'issue':'remaining bad instruction','pattern':bad})
(O/'global-repairs.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False),encoding='utf-8')
result={'entries':len(rows),'changed':sum(r['changed'] for r in rows),'existing_home_claude':sum(r.get('home_claude_added',False) for r in rows),'issues':issues,'support_payloads':'unchanged','native_trigger_acceptance':'not run','live_writes':'none'}
(O/'global-validation.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
lines=['# Global instruction repairs (2026-10-10)','',f'{len(rows)} existing entrypoints repaired; originals retained in backups. No payload/snapshot deletions, new activations, paid calls, publication or live Workspace writes. Existing home-Claude counterparts received separate fresh entrypoint reads and receipts.','', 'Validation: required frontmatter, current SHA256/readback, original backup hashes and targeted negative-instruction checks. Native selector/live workflow acceptance was not run.','', '| Entry | Repair | Original and current SHA256 |','|---|---|---|']
for r in rows:lines.append('| '+r['path'].replace('|','\\|')+' | '+r['contract'].replace('|','\\|').replace('\n',' ')+' | '+r['before_sha256']+' -> '+r['after_sha256']+' |')
(O/'GLOBAL-REPAIRS.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(json.dumps(result))
