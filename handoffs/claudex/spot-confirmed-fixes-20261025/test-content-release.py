"""Exercise publication guards with fake backend objects only; no network writes."""
import contextlib, copy, io, json, runpy, sys, types, unittest
from pathlib import Path
from unittest.mock import patch
ROOT=Path(__file__).parent
SCRIPT=ROOT/'content-release.py'
REPO=Path('C:/Users/Joshu/dev/ai-os-projects/lsatu-spot-confirmed-fixes-20261025')
SOURCE=REPO/'src/features/activity-centre/content/spot-the-relationship.json'
ORIGINAL_READ=Path.read_bytes
BEFORE=json.loads((ROOT/'canonical-before.json').read_text(encoding='utf-8'))
AUTHORED=json.loads(SOURCE.read_text(encoding='utf-8'))

class Guards(unittest.TestCase):
    def run_helper(self, *, changed_source=False, concurrent=False):
        calls=[]
        live=copy.deepcopy(BEFORE)
        if concurrent:live['updated_at']='2099-01-01T00:00:00Z'
        class FakeClient:
            url='https://example.invalid';anon_key='fake';token='fake'
            def get(self, table, **kwargs):
                if table=='activity_assignments':return []
                return [{**live, **{k:AUTHORED[k] for k in ('items','instructions','subtitle')}}] if calls else [live]
        module=types.ModuleType('lsatu_api')
        module.client=lambda:FakeClient()
        module._ssl_context=lambda:None
        def read(p):return b'tampered' if changed_source and p==SOURCE else ORIGINAL_READ(p)
        def send(req, **kwargs):
            calls.append(req)
            return io.BytesIO(json.dumps([{**live,**{k:AUTHORED[k] for k in ('items','instructions','subtitle')}}]).encode())
        with patch.dict(sys.modules,{'lsatu_api':module}),patch.object(sys,'argv',[str(SCRIPT),'apply']),patch.object(Path,'read_bytes',read),patch.object(Path,'write_text',lambda p,s,**kw:len(s)),patch('urllib.request.urlopen',send),contextlib.redirect_stdout(io.StringIO()):
            try:runpy.run_path(str(SCRIPT),run_name='__main__')
            except RuntimeError as error:return calls,str(error)
        return calls,None
    def test_modified_source_stops_before_patch(self):
        calls,error=self.run_helper(changed_source=True)
        self.assertEqual(calls,[])
        self.assertIn('reviewed content hash',error)
    def test_concurrent_canonical_edit_stops_before_patch(self):
        calls,error=self.run_helper(concurrent=True)
        self.assertEqual(calls,[])
        self.assertIn('Concurrent canonical edit',error)
    def test_exact_target_only_three_fields_and_cas(self):
        calls,error=self.run_helper()
        self.assertIsNone(error)
        self.assertEqual(len(calls),1)
        self.assertEqual(calls[0].get_method(),'PATCH')
        self.assertIn('12251bd3-d260-4108-bc35-bcf478e483e6',calls[0].full_url)
        self.assertIn('slug=eq.spot-the-relationship',calls[0].full_url)
        self.assertIn('updated_at=eq.',calls[0].full_url)
        self.assertEqual(set(json.loads(calls[0].data)),{'items','instructions','subtitle'})

if __name__=='__main__':unittest.main()
