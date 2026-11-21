from pathlib import Path
import importlib.util,re
from markdownify import markdownify
f=Path(__file__).parent;r=f.parents[1]
s=importlib.util.spec_from_file_location('manual',r/'.agents/skills/post-session-recap/references/session-manual/build_session_manual.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
t=(f/'recap.src.html').read_text(encoding='utf8');(f/'recap.html').write_text(t.replace('/*CSS*/',m.CSS),encoding='utf8')
for name,kicker,marker in [('necessary-assumption.md','Reference · Keep it open while you drill','yahunatan-necessary-assumption-reference'),('primer-negation-station.md','Before you start · Negation Station','yahunatan-2026-10-20-negation-primer')]:
 out=m.from_md(str(f/name),kicker,marker);(f/name.replace('.md','.html')).write_text(out,encoding='utf8');m.lint(name,out)
p=r/'students/yahunatan-zetvy/recaps/2026-10-20-recap.md';old=p.read_text(encoding='utf8');front=re.match(r'---.*?---',old,re.S).group();private=old[old.index('<!-- PRIVATE CONTINUATION'):];body=t[t.index('<header'):t.index('<script>')];body=re.sub(r'<div class="footer-note">.*','',body,flags=re.S);p.write_text(front+'\n\n'+markdownify(body,heading_style='ATX')+'\n\n'+private,encoding='utf8');m.lint('recap',t)
