import subprocess,json,pathlib,base64,hashlib,re,concurrent.futures
ROOT=pathlib.Path('raw/sources/conditional-gmail-2026-10-02');ROOT.mkdir(parents=True,exist_ok=True)
def call(resource,method,params):
 p=subprocess.run(['C:/Users/Joshu/dev/tools/node/node.exe','C:/Users/Joshu/dev/tools/node/node_modules/@googleworkspace/cli/run.js','gmail','users','messages',*resource,method,'--params',json.dumps(params)],capture_output=True,text=True,encoding='utf-8')
 if p.returncode: raise RuntimeError(p.stderr)
 return json.loads(p.stdout)
queries=['in:sent after:2025/10/01 before:2026/10/03 has:attachment (conditional OR conditionals OR sufficient OR necessary)','in:sent after:2025/10/01 before:2026/10/03 has:attachment (filename:lawgic OR filename:"group 1" OR filename:"group 2" OR filename:IF_THEN OR filename:contrapositive)']
queries += ['after:2025/10/01 before:2026/10/03 has:attachment (filename:conditional OR filename:lawgic OR filename:group OR Queen)']
queries += ['in:sent has:attachment (filename:conditional OR filename:lawgic OR filename:contrapositive)']
ids=set();counts=[]
for q in queries:
 token=None;n=0
 while True:
  p={'userId':'me','q':q,'maxResults':100}
  if token:p['pageToken']=token
  result=call([],'list',p);ids.update(m['id'] for m in result.get('messages',[]));n+=len(result.get('messages',[]));token=result.get('nextPageToken')
  if not token:break
 counts.append({'query':q,'count':n,'pagination_complete':True})
def process(mid):
 cached=ROOT/(mid+'.json')
 msg=json.loads(cached.read_text(encoding='utf-8')) if cached.exists() else call([],'get',{'userId':'me','id':mid,'format':'full'})
 cached.write_text(json.dumps(msg,ensure_ascii=False,indent=2),encoding='utf-8')
 headers={h['name'].lower():h['value'] for h in msg['payload'].get('headers',[])};files=[]
 def visit(part):
  name=part.get('filename');body=part.get('body',{})
  if name:
   data=body.get('data')
   if not data and body.get('attachmentId'):data=call(['attachments'],'get',{'userId':'me','messageId':mid,'id':body['attachmentId']}).get('data')
   if data:
    raw=base64.urlsafe_b64decode(data+'='*(-len(data)%4));safe=re.sub(r'[<>:"/\\|?*]','_',name);path=ROOT/(mid+'_'+safe);path.write_bytes(raw);files.append({'original_filename':name,'path':str(path),'sha256':hashlib.sha256(raw).hexdigest(),'size':len(raw)})
  for child in part.get('parts',[]):visit(child)
 visit(msg['payload'])
 return {'id':mid,'date':headers.get('date'),'subject':headers.get('subject'),'to':headers.get('to'),'from':headers.get('from'),'labels':msg.get('labelIds',[]),'attachments':files}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool: messages=list(pool.map(process,sorted(ids)))
manifest={'date_range':'2025-10-02 through 2026-10-02, plus clearly dated supplemental all-time conditional-filename matches','queries':counts,'messages':messages,'limits':'Gmail searches match message bodies and indexed attachment text. Unknown filenames or unindexed attachments without keywords can be missed. All attachments from matching messages preserved; conditional relevance needs review.'}
(ROOT/'provenance.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'queries':counts,'messages':len(messages),'attachments':sum(len(m['attachments']) for m in messages),'manifest':str(ROOT/'provenance.json')}))
