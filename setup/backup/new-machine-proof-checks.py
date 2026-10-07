"""Verify receipt validation in isolation; never invokes cloud mutations."""
import ast, json, time
from pathlib import Path
here=Path(__file__).parent
root=Path.home()/'LaptopBackups'/('receipt-test-'+str(time.time_ns()))
base=root/'base'; final=root/'final'
base.mkdir(parents=True); final.mkdir()
for script in ['new-machine-cloud.py','new-machine-run.py']:
    tree=ast.parse((here/script).read_text())
    function=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='verified_receipt')
    namespace={'json':json}
    exec(compile(ast.Module(body=[function],type_ignores=[]),script,'exec'),namespace)
    check=namespace['verified_receipt']
    (base/'CLOUD-VERIFIED.json').write_text('')
    assert not check(base)
    (base/'CLOUD-VERIFIED.json').write_text('{broken')
    assert not check(base)
    for directory in [base,final]:
        receipt={'complete':True,'generation':directory.name,'account':'contact@aspiringattorneys.com',
            'files':[{'id':'synthetic-file-id','md5Checksum':'0'*32,'size':'1'}]}
        (directory/'CLOUD-VERIFIED.json').write_text(json.dumps(receipt))
    assert all(check(directory) for directory in [base,final])
    receipt['account']='wrong-account@example.invalid'
    (final/'CLOUD-VERIFIED.json').write_text(json.dumps(receipt))
    assert not all(check(directory) for directory in [base,final])
    print('PASS',script,'rejects empty/malformed/wrong-account receipts and accepts valid dependency chain')
