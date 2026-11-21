import os, re, json, sys
D = r"C:/Users/Joshu/dev/ai-os-projects/lsatu/supabase/migrations"
files = sorted(os.listdir(D))
def norm(n):
    n = n.strip().strip('"').lower()
    n = n.replace('"', '')
    if n.startswith('public.'): n = n[7:]
    return n
tables = {}   # name -> file
rls = {}      # name -> (bool, file)
policies = {} # (table,name) -> (stmt,file,line)
funcs = {}    # name -> dict
views = {}
grants = []
dollar = re.compile(r"\$([A-Za-z_]*)\$")
def split_statements(sql):
    out=[]; buf=[]; i=0; n=len(sql); start=0; line=1; stline=1
    tag=None
    while i<n:
        c=sql[i]
        if tag is None:
            if sql.startswith('--',i):
                j=sql.find('\n',i); j=n if j<0 else j
                i=j; continue
            if sql.startswith('/*',i):
                j=sql.find('*/',i); j=n if j<0 else j+2
                line+=sql[i:j].count('\n'); i=j; continue
            if c=="'":
                j=i+1
                while j<n:
                    if sql[j]=="'" and (j+1<n and sql[j+1]=="'"): j+=2; continue
                    if sql[j]=="'": break
                    j+=1
                line+=sql[i:j+1].count('\n'); i=j+1; continue
            m=dollar.match(sql,i)
            if m:
                tag=m.group(0); i=m.end(); continue
            if c==';':
                out.append((sql[start:i], stline)); start=i+1; i+=1; stline=line; continue
            if c=='\n': line+=1
            i+=1
        else:
            j=sql.find(tag,i)
            if j<0: j=n
            line+=sql[i:j].count('\n'); i=j+len(tag); tag=None
    out.append((sql[start:],stline))
    return out
for f in files:
    sql=open(os.path.join(D,f),encoding='utf-8',errors='replace').read()
    for st,ln in split_statements(sql):
        st2=st
        while True:
            t=st2.lstrip()
            if t.startswith('--'):
                st2=t[t.find('\n'):] if '\n' in t else ''
            elif t.startswith('/*'):
                st2=t[t.find('*/')+2:]
            else: break
        s=st2.strip()
        ln2=ln+st[:len(st)-len(st2.lstrip())].count('\n')
        sl=s.lower()
        m=re.match(r'create\s+table\s+(if\s+not\s+exists\s+)?([\w\."]+)',sl)
        if m: tables.setdefault(norm(m.group(2)),f)
        m=re.match(r'alter\s+table\s+(if\s+exists\s+)?(only\s+)?([\w\."]+)\s+(enable|disable)\s+row\s+level\s+security',sl)
        if m: rls[norm(m.group(3))]=(m.group(4)=='enable',f)
        m=re.match(r'create\s+policy\s+("[^"]+"|\w+)\s+on\s+([\w\."]+)',s,re.I)
        if m: policies[(norm(m.group(2)),m.group(1).strip('"'))]=(s,f,ln2)
        m=re.match(r'drop\s+policy\s+(if\s+exists\s+)?("[^"]+"|\w+)\s+on\s+([\w\."]+)',s,re.I)
        if m: policies.pop((norm(m.group(3)),m.group(2).strip('"')),None)
        m=re.match(r'alter\s+policy\s+("[^"]+"|\w+)\s+on\s+([\w\."]+)',s,re.I)
        if m:
            k=(norm(m.group(2)),m.group(1).strip('"'))
            if k in policies: policies[k]=(policies[k][0]+'\n/*ALTERED*/ '+s,f,ln2)
        m=re.match(r'create\s+(or\s+replace\s+)?function\s+([\w\."]+)\s*\(',sl)
        if m:
            nm=norm(m.group(2))
            # signature
            funcs[nm]=dict(file=f,line=ln2,secdef=bool(re.search(r'security\s+definer',sl)),sp=bool(re.search(r'set\s+search_path',sl)),body=s)
        m=re.match(r'drop\s+function\s+(if\s+exists\s+)?([\w\."]+)',sl)
        if m: funcs.pop(norm(m.group(2)),None)
        m=re.match(r'create\s+(or\s+replace\s+)?view\s+([\w\."]+)',sl)
        if m: views[norm(m.group(2))]=(s,f,ln2)
        if re.match(r'(grant|revoke)\b',sl): grants.append((s,f,ln2))
        m=re.match(r'drop\s+table\s+(if\s+exists\s+)?([\w\."]+)',sl)
        if m:
            for t in m.group(2).split(','):
                tables.pop(norm(t),None)
out=dict(tables=tables,rls={k:v for k,v in rls.items()},policies={f"{k[0]}::{k[1]}":v for k,v in policies.items()},funcs=funcs,views=views,grants=grants)
json.dump(out,open(sys.argv[1],'w'),indent=0)
print(len(tables),len(rls),len(policies),len(funcs),len(views),len(grants))
