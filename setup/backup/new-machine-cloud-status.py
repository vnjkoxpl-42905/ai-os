"""Read-only cloud progress summary; emits only generated backup metadata."""
import json, subprocess
root='1vQ_Xm9GqDd7SlahE4sp6znQKiYkW8xOe'
def get(params):
    return json.loads(subprocess.run(['gws','drive','files','list','--params',json.dumps(params)],capture_output=True,text=True,check=True).stdout)['files']
folders=get({'q':"trashed=false and '%s' in parents"%root,'fields':'files(id,name)','pageSize':100})
for folder in folders:
    files=get({'q':"trashed=false and '%s' in parents"%folder['id'],'fields':'files(name,size)','pageSize':100})
    print(json.dumps({'generation':folder['name'],'files':len(files),
        'bytes':sum(int(f.get('size',0)) for f in files),
        'helper_names':[f['name'] for f in files if not f['name'].startswith('payload.zip')]}))
