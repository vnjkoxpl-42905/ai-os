# Read-only REST pull of the LR question + explanation tables. Run from the vault root.
# Usage: python system/scripts/lsatlab-pull/db_pull.py [out_dir] [table ...]  (default: data/db next to this file; the four LR explanation tables)
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from project_paths import project_path, VAULT_ROOT
import sys
import json, re, urllib.request, os
env={}
for f in [VAULT_ROOT / '.env', project_path('lsatu', '.env')]:
  for l in open(f,encoding='utf-8'):
    m=re.match(r'([A-Z_]+)=(.*)',l.strip())
    if m: env[m[1]]=m[2].strip('"')
U=env['VITE_SUPABASE_URL'];K=env['VITE_SUPABASE_PUBLISHABLE_KEY']
def req(p,body=None,tok=None):
  r=urllib.request.Request(U+p,data=json.dumps(body).encode() if body else None,headers={'apikey':K,'Content-Type':'application/json','Authorization':'Bearer '+(tok or K)})
  return json.load(urllib.request.urlopen(r))
tok=req('/auth/v1/token?grant_type=password',{'email':env['LSATPREP_ADMIN_EMAIL'],'password':env['LSATPREP_ADMIN_PASSWORD']})['access_token']
out=sys.argv[1] if len(sys.argv)>1 else os.path.join(os.path.dirname(os.path.abspath(__file__)),'data','db')
os.makedirs(out,exist_ok=True)
for t in (sys.argv[2:] or ['lr_questions','lr_explanations','lr_explanation_steps','lr_explanation_choice_notes']):
  rows=[];o=0
  while True:
    b=req(f'/rest/v1/{t}?select=*&limit=1000&offset={o}',tok=tok);rows+=b;o+=1000
    if len(b)<1000:break
  json.dump(rows,open(os.path.join(out,t+'.json'),'w',encoding='utf-8'),ensure_ascii=False)
  print(t,len(rows), sorted(rows[0].keys()) if rows else '')
