import pathlib,json,re,hashlib
OUT=pathlib.Path('C:/Users/Joshu/dev/ai-os/audits/skills-2026-10-10-repairs')
rows=json.loads((OUT/'global-repairs.json').read_text(encoding='utf-8'))
def desc(t,s):
 m=re.match(r'---\s*\n(.*?)\n---',t,re.S)
 if not m:return t
 f=re.sub(r'(?ms)^description:.*?(?=^[A-Za-z_][\w-]*:|\Z)','description: '+json.dumps(s)+'\n',m.group(1))
 return '---\n'+f.rstrip()+'\n---'+t[m.end():]
def sub(t,a,b):return t.replace(a,b)
for r in rows:
 p=pathlib.Path(r['path']);t=p.read_text(encoding='utf-8');old=t;n=r['name']
 t=re.sub(r'Use the actual host tools and shell; literal Claude Task/Skill/TodoWrite.*?conflicting legacy examples below\.\s*','',t,flags=re.S)
 t=t.replace('## Preserved specialist reference','## Workflow')
 if n=='claude-api':
  t=re.sub(r'## Defaults\s*.*?(?=## Warning)', '## Defaults\n\nUse the user-selected Anthropic model ID when supplied. Otherwise discover supported model IDs through the installed SDK or current official Anthropic documentation before selecting one. Do not infer a model ID from a marketing name or mechanically substitute a provider. Enable thinking/streaming only according to that selected model and current SDK contract.\n\n',t,flags=re.S)
  t=t.replace('python/Claude-api/','python/claude-api/').replace('shared/Claude-platform-on-aws.md','shared/claude-platform-on-aws.md')
  t=re.sub(r'`Claude-([^`]+)`',lambda m:'`claude-'+m.group(1)+'`',t)
 if n=='academy-guide':
  t=desc(t,'Recommend verified Anthropic Academy courses only for explicit Claude/Anthropic learning-resource requests. Does not activate for generic Codex work or ordinary task execution.')
  t=t.replace('or a general\n"how do I use AI for X" question','or an explicit Anthropic learning-resource request')
 if n.startswith('recipe-'):
  # Replace unsafe placeholder mutation steps with real parameter/data mapping.
  # Preserve endpoint discovery without executable writes to example recipients/data.
  methods=sorted(set(re.findall(r'gws ([\w-]+(?: [\w-]+){0,4})',t)))
  head=t.split('## Steps')[0]
  t=head+'## Steps\n\n1. Resolve actual target IDs, requested data, date interval/timezone and existing state. Illustrative names, dates and recipients are not user data.\n2. '+r['contract']+'\n3. Discover the required method using installed `gws <service> --help` and `gws schema <service>.<resource>.<method>`; build parameters from real returned IDs and requested data. For retries reconcile existing output identity first.\n4. Execute only the requested authorized operation. Draft email unless send is authorized. Inspect resulting resource/file and report any missing sections or failed items.\n\n## Relevant endpoint references\n\n'+''.join('- `gws '+m+'` (inspect help/schema before invocation)\n' for m in methods)+'\n'
  t=t.replace('`gws forms forms list` (inspect help/schema before invocation)\n','`gws forms forms responses list` (inspect help/schema before invocation)\n')
  if n=='recipe-create-presentation':
   t=t.replace('        - gws-slides','        - gws-slides\n        - gws-drive')
   t+='\nUse `gws slides presentations batchUpdate` to add requested slides/content before optional `gws drive permissions create`.\n'
  if n=='recipe-create-feedback-form':t+='\nUse `gws forms forms batchUpdate` to add questions after create; inspect `gws forms forms get` before sharing the respondent URL.\n'
  if n=='recipe-draft-email-from-doc':t+='\nDraft helper: `gws gmail +send --draft --to ACTUAL_RECIPIENT --subject ACTUAL_SUBJECT --body ACTUAL_DOCUMENT_TEXT`.\n'
  if n in ['recipe-save-email-to-doc','recipe-generate-report-from-sheet','recipe-create-doc-from-template','recipe-post-mortem-setup']:t+='\nWrite helper: `gws docs +write --document ACTUAL_DOCUMENT_ID --text ACTUAL_TEXT`. Create titles through `gws docs documents create`, not +write --title/--body.\n'
 if n.startswith('persona-'):
  t=desc(t,'Use this specific '+n+' Workspace role when requested; perform only selected operations. Planning or inspection does not authorize sends, invitations, publication or cloud scheduling. Distinct from persona-agent-creator.')
  t=t.replace('gws gmail +send --to','gws gmail +send --draft --to')
 if n=='firecrawl-monitor':
  t=t.replace('and delete any monitors created for this task.','and preserve monitors/evidence. Delete only after explicit deletion authorization.')
  t=t.replace('firecrawl monitor delete <monitorId>','# Only after explicit deletion authorization: firecrawl monitor delete <monitorId>')
  t=t.replace('reserve `delete` for monitors that are permanently done.','reserve `delete` for explicitly authorized removal of monitors that are permanently done.')
 if n in ['test-driven-development','writing-skills']:
  t=re.sub(r'Write (?:code|skill) before (?:the test|testing|test)\? Delete it\. Start over\.', 'Existing work is preserved. Add a meaningful regression/behavior test and demonstrate it detects the failure.',t)
  t=t.replace('Write code before test? Delete it.','Preserve existing code; demonstrate the regression test detects the defect.')
  t=re.sub(r'\*\*No exceptions:\*\*\s*(?:-.*\n)+\s*Implement fresh from tests\. Period\.', 'Preserve useful implementation and unrelated edits. Refactor only when required by the tested behavior.',t)
  t=t.replace('**All of these mean: Delete code. Start over with TDD.**','**These are prompts to inspect test quality, not instructions to delete existing code. Preserve work and repair verification.**')
  t=t.replace('Delete means delete','Preserve work and verify behavior').replace('Delete and rewrite with TDD','Preserve and validate with meaningful regression tests')
  t=t.replace('**Exceptions (ask your human partner):**','**Use proportionate verification for:**').replace('Thinking "skip TDD just this once"? Stop. That\'s rationalization.','Use meaningful tests for behavior changes; do not mirror reversible low-impact edits.')
  t=t.replace('NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST','PRESERVE EXISTING WORK; PROVE CHANGED BEHAVIOR WITH APPROPRIATE CHECKS')
 if n=='using-superpowers':
  t=t.replace('If you think there is even a 1% chance a skill might apply to what you are doing, you ABSOLUTELY MUST invoke the skill.','Consult a skill when explicitly selected or substantively required by the task. Do not invoke skills for speculative one-percent relevance.')
  t=t.replace('IF A SKILL APPLIES TO YOUR TASK, YOU DO NOT HAVE A CHOICE. YOU MUST USE IT.','Use applicable skill guidance through the supported host route while honoring higher-priority instructions and task scope.')
  t=re.sub(r'(?im)^.*skills.*(?:override|supersede).*system.*$', 'System and developer instructions outrank skill guidance.',t)
 if n=='qa':
  t=desc(t,'Inspect and reproduce reported bugs, then produce a findings report. Publish GitHub issues only when explicitly authorized.')
  t=t.replace('and file GitHub issues that are durable','and draft issue reports that are durable')
  t=t.replace('Create issues with `gh issue create`. Do NOT ask the user to review first — just file and share URLs.','Draft issue reports locally by default. When the user explicitly requests issue publication, use `gh issue create` and report actual URLs. Existing authorization needs no repeated confirmation.')
  t=t.replace('### 4. File the GitHub issue(s)','### 4. Draft the report, or file explicitly authorized issues')
 if n=='lsatu-cc-handoff':
  t=t.replace('`~/ai-os/raw/sources/lsat-u/curriculum/<topic>/<BRIEF_NAME>.md`','`<current-ai-os-root>/handoffs/<topic>/<BRIEF_NAME>.md`')
  t=t.replace('`Direct commits to main. Push after each step.`','`Branch/commit/push scope: use actual task authorization; preserve existing dirty work.`')
  t=t.replace('Direct commits to main. Push at the end of each step.','Use task branch and explicitly authorized commit/push scope; no default main mutation.')
  t=t.replace('"execute end to end. Commit and push after each step."','"execute the approved scope end to end; commit/push only as authorized."')
  t=t.replace('move the old one to `_archive/<NAME>_superseded.md`','preserve the old source and record its superseded status in the handoff; moving/deleting sources is not permitted')
  t=t.replace('`~/Documents/Obsidian\\ Vault/...`','`<current-ai-os-root>/handoffs/...`')
  t=t.replace('~/ai-os/projects/lsatu/','<current-ai-os-root>/../ai-os-projects/lsatu/')
 if n=='gws-events':
  t=re.sub(r'### message\s*.*?(?=### operations)','',t,flags=re.S)
  t=re.sub(r'### tasks\s*.*?(?=## Discovering Commands)','',t,flags=re.S)
 if n=='obsidian-vault':
  t=desc(t,'Explicit legacy/new-vault reference only. Existing AI OS work uses project ingest, second-brain-query and second-brain-lint; do not select alternate vault automatically.')
 if n in ['code-review','review','requesting-code-review']:
  t=re.sub(r'(git diff[^\n]*?(?:HEAD|HEAD_SHA)[^\n]*)',r'\1\n# Also inventory requested worktree scope: git status --short; git diff; git diff --cached; inspect relevant untracked files.',t)
 if n=='hatch-pet':
  t=t.replace('remove the selected original','preserve the selected original unless deletion is explicitly authorized; only then remove it').replace('delete the original generated file after the decoded copy exists:','preserve the original generated file. Only after explicit deletion authorization and verified decoded copy may the following cleanup example run:')
  t=re.sub(r'(?m)^\s*(rm |Remove-Item )(.*)$',r'# Only after explicit deletion authorization: \1\2',t)
  t=t.replace('marked complete','marked complete only after repaired-row QA and whole-sheet QA pass')
 if n in ['webapp-testing']:
  t=t.replace("page.wait_for_load_state('networkidle')","page.wait_for_selector('ACTUAL_APP_READY_SELECTOR')").replace('page.wait_for_load_state("networkidle")','page.wait_for_selector("ACTUAL_APP_READY_SELECTOR")')
  t=t.replace('wait for networkidle','wait for the actual app-ready selector/state').replace('wait until networkidle','wait until observed app readiness')
 if n=='design-taste-frontend':t=t.replace('LAYOUT_VARIANCE','DESIGN_VARIANCE')
 if n=='decision-mapping':t=t.replace('domain-modelling','domain-modeling')
 if n in ['link','onboard']:
  t=t.replace('AGENTS.md and AGENTS.md','AGENTS.md and CLAUDE.md').replace('`AGENTS.md` and `AGENTS.md`','`AGENTS.md` and `CLAUDE.md`')
 if n=='superwhisper':
  t=t.replace('sw-Codex-4p5-sonnet','sw-claude-4p5-sonnet').replace('modes/Codex.md','modes/claude-code.md')
 if n=='watch':
  t=re.sub(r'(?m)^\s*(rm |Remove-Item )(.*)$',r'# Explicit deletion authorization required: \1\2',t)
 if n in ['setup-pre-commit','resolving-merge-conflicts','scaffold-exercises','writing-plans']:
  t=t.replace('git add .','git add <EXACT_OWNED_PATHS>').replace('git add -A','git add <EXACT_OWNED_PATHS>')
  t=re.sub(r'(?m)^(\s*)git commit (.*)$',r'\1# Only when task authorizes commit: git commit \2',t)
 if n=='systematic-debugging':t=t.replace('env | grep IDENTITY',"python -c \"import os; print('IDENTITY present:', 'IDENTITY' in os.environ)\"")
 if n.startswith('higgsfield-'):t=re.sub(r'(?im)^.*(?:deploy|publish).*automatically.*$', 'Prepare preview only; public deployment requires explicit publication authorization.',t)
 # Keep local contract concise, no copied audit findings disguised as implementation.
 if 'Before executing this workflow, satisfy this specific acceptance boundary:' in t:
  t=re.sub(r'Before executing this workflow, satisfy this specific acceptance boundary:.*?invent success\.', 'Resolve the actual installed dependency and current project route before execution. Preserve sources and report unsupported capabilities; do not claim runtime acceptance from static instructions.',t,flags=re.S)
 if t!=old:
  if p.read_text(encoding='utf-8')!=old:raise RuntimeError('Concurrent '+str(p))
  p.write_text(t,encoding='utf-8',newline='')
 r['after_sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
 r['validation']='current full entrypoint loaded; direct operative/example fixes plus scoped contract; hash readback; no live execution'
(OUT/'global-repairs.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False),encoding='utf-8')
print('Direct repair pass',len(rows))
