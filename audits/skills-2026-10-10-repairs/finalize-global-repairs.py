import pathlib,json,re,hashlib
O=pathlib.Path('C:/Users/Joshu/dev/ai-os/audits/skills-2026-10-10-repairs');rows=json.loads((O/'global-repairs.json').read_text(encoding='utf-8'))
extra={
'docs':'Inspect the requested existing source before deciding whether a new document is needed. Use actual host document tools and installed skill reference, not assumed docs connectors or Codex.ai artifacts. Create only requested output; do not impose a document artifact on every information task.',
'facebook-consultation-requests':'Discover the actual supported signed-in Messenger browser surface, not a renamed Claude-in-Chrome tool or assumed Work-profile login. Preserve exact prospect thread. Typing a reply is not proof of persistent draft or absence of send; verify composer/thread state. Send only authorized content and read back/log one copy.',
'lsat-drill-builder':'Use this two-option first/rebuttal engine only for compatible requested pedagogy. Apply current teaching voice. Preserve source question identity and data invariants; label/control changes alter rendering and require actual interaction/accessibility verification. Mental walkthrough alone is not acceptance.',
'lsat-lab-question-features':'Use actual available browser transport and current selectors. For read-only extraction avoid Start because it creates an attempt. Save mixed-section output with exact section/question identity to prevent overwrite. Preserve source/provenance and compile through existing corpus ingest.',
'lsat-lab-set-builder':'Use actual supported browser/DOM rather than fixed bridge names/table indices. Respect authorized batch scope; reconcile extras/missing exact question IDs and verify saved set identity/count after Submit. A success banner alone is insufficient.',
'morning':'Resolve actual host launch links and installed browser/render executable. Do not invent https://Codex.ai/new or assume Linux Chromium on Windows. Use actual returned artifact links or local file paths and report rendering limitations.',
'lsat-u-topic-builder':'Legacy topic reference only; current bootcamp-builder owns new module creation. Resolve current sibling ai-os-projects/lsatu app and preserve source material. No old Mac/vault-contained app output, provider substitution or destructive duplicate heuristics.',
}
for r in rows:
 p=pathlib.Path(r['path']);t=p.read_text(encoding='utf-8');old=t;n=r['name']
 if n in extra:
  t=re.sub(r'## Local execution contract \(2026-10-10\)\s*.*?(?=## Workflow)','## Local execution contract (2026-10-10)\n\n'+extra[n]+'\n\n',t,flags=re.S);r['contract']=extra[n]
 if n=='using-git-worktrees':
  t=t.replace('git check-ignore -q .worktrees 2>/dev/null || git check-ignore -q worktrees 2>/dev/null','git check-ignore -q <SELECTED_TARGET_DIRECTORY>')
  t=t.replace('Add to .gitignore, commit the change, then proceed.','Add only the selected target to .gitignore if required, then proceed. Commit only if explicitly authorized.')
  t=t.replace('Add to .gitignore + commit','Add selected path to .gitignore; commit only as authorized')
 if n=='high-end-visual-design':
  t=t.replace('Never place a premium card, image, or container flatly on the background. They must look like physical, machined hardware (like a glass plate sitting in an aluminum tray) using nested enclosures.','When this specific preset is selected, optional double-bezel enclosures may create physical depth. Use flat containers where the existing design system or clarity calls for them.')
  t=t.replace('All major cards and containers use the Double-Bezel nested architecture (outer shell + inner core)','Selected Double-Bezel treatments fit the brief; flat alternatives remain valid')
  t=t.replace('Elements never appear statically on load. As they enter the viewport, they must execute','Elements remain visible/readable by default. If requested and reduced-motion is disabled, they may execute')
  t=t.replace('Before writing code, silently "roll the dice" and select ONE combination','When the user selects this aesthetic, choose a suitable combination')
 if n=='minimalist-ui':
  t=t.replace('DO NOT use gradients, neon colors, or 3D glassmorphism (beyond subtle navbar blurs).','Avoid prominent gradients, neon colors and 3D glassmorphism in this preset; subtle requested background radial treatments below are optional.')
  t=t.replace('Ensure sections have visual depth through imagery, ambient gradients, or subtle textures — no empty flat backgrounds.','Use optional depth treatments only when requested and accessible; flat readable backgrounds are valid.')
 if n=='watch':
  t=re.sub(r'Before every `/watch` run, verify that dependencies and an API key are in place:.*?(?=## |### |\*\*Step 1)', 'Before execution check installed Python, yt-dlp and FFmpeg without reinstalling. An API key is not required for captions or frames. Use current project get_youtube_transcript.py first for transcript-only requests. For frame extraction run the bundled watch script with --no-whisper. Skip the bundled setup wizard because it couples free extraction to a provider key.\n\n',t,count=1,flags=re.S)
  t=t.replace('~/.config/watch/.env','the current project central .env (do not create another secret store)')
  t=t.replace('**Step 5 — clean up.** The script prints a working directory at the end. If the user isn\'t going to ask follow-ups about this video, delete it with `rm -rf <dir>`. If they might, leave it in place.','**Step 5: preserve evidence.** Report the working directory and keep frames/captions/downloads. Delete only after explicit deletion authorization for the verified task-owned path.')
  t=re.sub(r'python3 "\$\{CLAUDE_SKILL_DIR\}/scripts/watch.py"(?! --no-whisper)', 'python "<actual-installed-skill-directory>/scripts/watch.py" --no-whisper',t)
  t=t.replace('You can retry with `--whisper openai` if Groq failed (or vice versa).','Do not change paid providers or retry billable transcription without that provider/cost authorization. Free captions/frames remain available.')
  t=t.replace('**Setup preflight failed** → run','**Setup preflight failed**: inspect installed dependencies; do not create a separate secret store or invoke the key-coupled installer. Legacy helper reference only:')
 if n in ['web-artifacts-builder','algorithmic-art','docs']:
  t=t.replace('Codex.ai','the actual host artifact panel')
 if n in ['assign-lsatu-work','booking-link','bootcamp-builder','bootcamp-parity-audit','lsat-u-platform-actions','lovable-migrate','lovable-prompt','resume','pickup','pull-submissions','lsat-u-architecture','lsat-u-topic-builder']:
  t=t.replace('~/ai-os/projects/lsatu','<current-ai-os-root>/../ai-os-projects/lsatu')
  t=re.sub(r'(?<!ai-os-)projects/lsatu/', '../ai-os-projects/lsatu/',t)
  t=t.replace('ai-os is not a Git repo','ai-os is a Git repository').replace('AI OS is not a git repo','AI OS is a Git repository')
 if n in ['chat-export']:
  t=t.replace('~/Documents/Codex/08_CHAT_EXPORTS','<current-project-root>/handoffs').replace('~/Documents/Claude/08_CHAT_EXPORTS','<current-project-root>/handoffs')
  t=t.replace('full verbatim conversation','available verbatim transcript, with any missing ranges disclosed')
 if t!=old:
  if p.read_text(encoding='utf-8')!=old:raise RuntimeError(str(p))
  p.write_text(t,encoding='utf-8',newline='')
 r['after_sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
(O/'global-repairs.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False),encoding='utf-8')
print('Final routes/direct examples',len(rows))
