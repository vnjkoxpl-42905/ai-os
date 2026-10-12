import os,re,json,glob
H=os.path.expanduser('~');V=H+'/dev/ai-os'
roots={'home-claude':H+'/.claude/skills','vault-claude':V+'/.claude/skills','home-agents':H+'/.agents/skills','home-codex':H+'/.codex/skills','vault-agents':V+'/.agents/skills'}
names={}
for k,r in roots.items():
    if os.path.isdir(r):
        for n in os.listdir(r):
            if os.path.isfile(f'{r}/{n}/SKILL.md'): names.setdefault(n,set()).add(k)
logs=glob.glob(H+'/.claude/projects/**/*.jsonl',recursive=True)+glob.glob(H+'/.codex/sessions/**/*.jsonl',recursive=True)
inv={n:0 for n in names};opn={n:0 for n in names}
pat_inv=re.compile(r'"skill\\?"\s*:\s*\\?"(?:[\w-]+:)?([\w-]+)')
pat_open=re.compile(r'[/\\]([\w-]+)[/\\]+SKILL\.md')
pat_cmd=re.compile(r'<command-name>/?([\w-]+)</command-name>')
for f in logs:
    try: t=open(f,encoding='utf-8',errors='ignore').read()
    except: continue
    s1=set(pat_inv.findall(t))|set(pat_cmd.findall(t)); s2=set(pat_open.findall(t))
    for n in s1:
        if n in inv: inv[n]+=1
    if len(s2 & set(names)) > 15: s2 = set()  # bulk audit/sync session, not real use
    for n in s2:
        if n in opn: opn[n]+=1
un=sorted(n for n in names if inv[n]==0 and opn[n]==0)
lo=sorted(n for n in names if inv[n]==0 and 0<opn[n]<=2)
print('logs',len(logs),'skills',len(names),'never',len(un),'opened-only',len(lo))
json.dump({'never':un,'opened_only':{n:opn[n] for n in lo},'used':{n:[inv[n],opn[n]] for n in names if inv[n]}},open(os.path.dirname(__file__)+'/unused.json','w'),indent=1)
