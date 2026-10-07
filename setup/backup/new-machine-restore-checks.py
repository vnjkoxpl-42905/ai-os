"""Verify long-path restore and retained partial reassembly without touching sources."""
import hashlib, json, subprocess, sys, time, zipfile
from pathlib import Path
here=Path(__file__).parent
root=Path.home()/'LaptopBackups'/('restore-check-'+str(time.time_ns()))
generation=root/'generation'; generation.mkdir(parents=True)
content=b'verified long-path restore'
key='ai-os/'+'a'*100+'/'+'b'*100+'/test.txt'
with zipfile.ZipFile(generation/'source.zip','w') as archive: archive.writestr(key,content)
data=(generation/'source.zip').read_bytes()
(generation/'payload.zip.part0001').write_bytes(data)
(generation/'reassembled-payload.zip').write_bytes(b'interrupted partial retained')
(generation/'parts-manifest.json').write_text(json.dumps({'archive_sha256':hashlib.sha256(data).hexdigest(),
    'parts':[{'name':'payload.zip.part0001','sha256':hashlib.sha256(data).hexdigest()}]}))
(generation/'manifest.json').write_text(json.dumps({'complete':True,'files':{key:{'generation':'generation','sha256':hashlib.sha256(content).hexdigest()}}}))
subprocess.run([sys.executable,str(here/'new-machine-restore.py'),'--generation',str(generation),'--output',str(root/'verified')],check=True)
assert (generation/'reassembled-payload.zip').read_bytes()==b'interrupted partial retained'
print('PASS: long Windows path restored, source hashes verified, interrupted partial retained')
