import pathlib,json,zipfile,re
from pypdf import PdfReader
ROOT=pathlib.Path('raw/sources/conditional-gmail-2026-10-02')
manifest=json.loads((ROOT/'provenance.json').read_text(encoding='utf-8')); results=[]
for message in manifest['messages']:
 for attachment in message['attachments']:
  path=pathlib.Path(attachment['path']);text='';error=None
  try:
   if path.suffix.lower()=='.pdf':text='\n'.join(page.extract_text() or '' for page in PdfReader(path).pages)
   elif path.suffix.lower()=='.docx':
    with zipfile.ZipFile(path) as z:text=re.sub('<[^>]+>',' ',z.read('word/document.xml').decode())
   elif path.suffix.lower()=='.html':text=re.sub('<[^>]+>',' ',path.read_text(encoding='utf-8'))
  except Exception as exc:error=str(exc)
  matches=[]
  for match in re.finditer(r'conditional|sufficient|necessary|contrapositive',text,re.I):matches.append(text[max(0,match.start()-80):match.end()+160])
  if matches:results.append({'path':str(path),'subject':message['subject'],'date':message['date'],'matches':matches,'error':error})
(ROOT/'extracted-relevance.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps([{'path':r['path'],'mentions':len(r['matches'])} for r in results],indent=2))
