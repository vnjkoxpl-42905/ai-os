"""Execute actual revised skill snippets against hostile fixture inputs."""
import json
import re
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORT = Path(__file__).parent


def node(code):
    result = subprocess.run(['node', '--input-type=module'], input=code, text=True,
                            encoding='utf-8', capture_output=True, timeout=30)
    if result.returncode:
        raise AssertionError(result.stderr or result.stdout)
    return result.stdout


class ScaffoldTests(unittest.TestCase):
    def test_paths_allow_real_inside_and_deny_traversal_absolute_and_junction(self):
        text = (ROOT / 'skills/claude/build-mcpb/SKILL.md').read_text(encoding='utf-8')
        helper = re.search(r'async function confinedPath\(path\) \{.*?\n\}', text, re.S).group()
        with tempfile.TemporaryDirectory(prefix='mcp-root-fixture-') as temp:
            base = Path(temp)
            allowed = base / 'allowed'
            outside = base / 'outside'
            allowed.mkdir()
            outside.mkdir()
            (allowed / 'good.txt').write_text('inside', encoding='utf-8')
            (outside / 'secret.txt').write_text('outside fixture', encoding='utf-8')
            code = '''import assert from 'node:assert/strict';
import {realpath, readFile, symlink} from 'node:fs/promises';
import {resolve, relative, isAbsolute, sep, join} from 'node:path';
const ROOT = await realpath(ALLOWED);
HELPER
assert.equal(await readFile(await confinedPath('good.txt'), 'utf8'), 'inside');
assert.equal(await confinedPath('.'), ROOT);
await assert.rejects(() => confinedPath('../outside/secret.txt'), /escapes ROOT/);
await assert.rejects(() => confinedPath(join(OUTSIDE, 'secret.txt')), /relative/);
await symlink(OUTSIDE, join(ROOT, 'escape'), process.platform === 'win32' ? 'junction' : 'dir');
await assert.rejects(() => confinedPath('escape/secret.txt'), /escapes ROOT/);
assert.equal(await readFile(join(ROOT, '../outside/secret.txt'), 'utf8'), 'outside fixture');
console.log('allowed child/root; denied parent traversal, absolute path and symlink/junction; old join counterexample reproduced');
'''.replace('ALLOWED', json.dumps(str(allowed))).replace('OUTSIDE', json.dumps(str(outside))).replace('HELPER', helper)
            print(node(code).strip())

    def test_picker_renders_hostile_strings_as_text_and_keeps_click_behavior(self):
        text = (ROOT / 'skills/claude/build-mcp-app/SKILL.md').read_text(encoding='utf-8')
        widget = text.split('**Widget (`widgets/picker.html`):**', 1)[1]
        script = re.search(r'<script type="module">(.*?)</script>', widget, re.S).group(1)
        code = '''import assert from 'node:assert/strict';
import vm from 'node:vm';
class Element {
  constructor(tag) { this.tag = tag; this.children = []; this.events = {}; this.textContent = ''; }
  set innerHTML(value) { if (value !== '') throw new Error('Untrusted HTML rendering'); this.children = []; }
  append(...children) { this.children.push(...children); }
  addEventListener(name, fn) { this.events[name] = fn; }
}
const list = new Element('ul');
const sent = []; let instance;
class App { constructor() { instance = this; } async connect() {} sendMessage(m) { sent.push(m); } }
const context = { document: {getElementById: () => list, createElement: t => new Element(t)},
  ExtApps: {App}, JSON };
await vm.runInNewContext(SCRIPT, context);
const contact = {id: '17', name: '<img src=x onerror=alert(1)>', email: '<script>bad()</script>'};
instance.ontoolresult({content: [{text: JSON.stringify([contact])}]});
assert.equal(list.children.length, 1);
assert.equal(list.children[0].children[0].textContent, contact.name);
assert.equal(list.children[0].children[1].textContent, contact.email);
assert.equal(list.children[0].children[1].className, 'sub');
list.children[0].events.click();
assert.equal(sent.length, 1);
assert.equal(sent[0].content[0].text, `Selected contact: ${contact.id} (${contact.name})`);
assert.throws(() => { new Element('li').innerHTML = contact.name; }, /Untrusted HTML/);
console.log('hostile name/email stay text; click preserved; old innerHTML sink rejected');
'''.replace('SCRIPT', json.dumps(script))
        print(node(code).strip())


if __name__ == '__main__':
    unittest.main(verbosity=2)
