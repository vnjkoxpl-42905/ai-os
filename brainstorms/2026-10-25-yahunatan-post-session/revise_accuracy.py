from pathlib import Path
import re,shutil,importlib.util
from markdownify import markdownify
root=Path(__file__).resolve().parents[2];f=Path(__file__).parent
backup=f/'before-accuracy-revision';backup.mkdir(exist_ok=True)
paths=[f/'recap.src.html',f/'necessary-assumption.md',f/'primer-negation-station.md',root/'students/yahunatan-zetvy/recaps/2026-10-20-recap.md']
for p in paths:
 dest=backup/p.name
 if not dest.exists():shutil.copy2(p,dest)
p=f/'recap.src.html';t=p.read_text(encoding='utf8')
if '<h2>Strength is a reason to check, not a reason to reject</h2>' in t:
 import runpy
 runpy.run_path(str(f/'sync_current.py'))
 raise SystemExit(0)
t=t.replace("You caught this on the tax question before I pointed it out: nobody said the plan had to be done in a year. That's the kind of detail that decides these questions. Keep looking for it.","After we separated the plan from the evidence, you explained that the plan had no stated one-year deadline. Keep checking the time limit instead of supplying one.")
t=t.replace('The same rule said a different way. Flip the sides and put a "not" on both.','The same conditional rule said a different way. Reverse the two complete conditions and negate each one. Preserve all qualifications; negating an AND condition uses OR, and negating an OR condition uses AND.')
t=t.replace('The weakest claim that contradicts the original. Nothing gets flipped.','A claim that is true exactly when the original is false. Contradict the complete idea, without inventing a stronger opposite.')
t=t.replace('To test an answer. Negate it. If the argument falls apart, the argument needed it.','To test a candidate assumption. Negate it while keeping the premises true. Ask whether the reasoning can still support the conclusion.')
t=t.replace('Breaks the rule. The argument falls.','Contradicts the original claim. It is not an equivalent rule.')
t=t.replace("If that's true, the conclusion is dead. That's how you know the assumption was necessary.","That possibility preserves the evidence but defeats this inference. The conclusion might still be true for another reason; the evidence no longer gets us there.")
t=t.replace('You put it in your own words: you don\'t flip it, you just put a "not" on it. That\'s the whole difference.','You distinguished negation from the contrapositive in your own words. Keep that distinction, then work out what makes the complete claim false.')
start=t.index('<section><div class="wrap">\n  <div class="sec-kicker">Claim strength</div>');end=t.index('<section><div class="wrap">\n  <div class="sec-kicker">Recognition drill</div>',start)
t=t[:start]+'''<section><div class="wrap"><div class="sec-kicker">Test the actual claim</div><h2>Strength is a reason to check, not a reason to reject</h2><p>A necessary assumption is required for this argument's reasoning. A weak-looking answer can still be irrelevant. A strong answer can be required. Neither its tone nor one word decides.</p><p>Suppose the author concludes that every registered vehicle passed inspection. The argument might need a claim about every vehicle. Do not eliminate it merely because it says every. Ask whether this argument can work if that answer is false.</p><div class="callout"><span class="tag">Keep modality and scope intact</span>Alex will travel is a prediction. Alex must travel can express a requirement or a logical necessity, depending on context. They are not automatically interchangeable. Preserve words such as probably, must and only, and the complete meaning they express.</div><p>A sufficient assumption makes the conclusion follow when added to the premises. A necessary assumption is something the reasoning cannot do without. An answer can be one without being the other.</p></div></section>
<section><div class="wrap"><div class="sec-kicker">Two useful roles</div><h2>Connect an idea or rule out a threat</h2><p>An assumption can connect the evidence to a conclusion, or exclude a possibility that would undermine the connection. Read its meaning. Either role can be worded positively or negatively; the presence of not does not determine whether it is necessary.</p><p>Predict the missing connection if you can, then test the actual answers. Do not select by grammatical shape.</p></div></section>
'''+t[end:]
start=t.index('  <div class="drill">\n    <h3>Safe or too strong?</h3>');end=t.index('</div></section>',start)
t=t[:start]+'''  <div class="drill"><h3>What is actually required?</h3><p class="hint">A club's only voting rule says that a person may vote only if registered. The author concludes that Maya may vote. What must be true?</p><details><summary>Maya is registered.</summary><p>Required. Negate it: Maya is not registered. The supplied rule then rules out permission to vote. Registration alone does not prove permission, but it is necessary.</p></details><details><summary>Every registered person may vote.</summary><p>Not required. Other registered people could be barred while Maya is allowed. The conclusion concerns Maya, not every registered person.</p></details></div>
'''+t[end:]
t=t.replace('<li><b>Read the reasoning.</b> Expect a positive answer or a "not" answer.</li>','<li><b>Read every complete answer.</b> Ask what connection or protection it supplies.</li>').replace('<li><b>Cut the strong answers.</b> Only, always, most, primarily, or a flat certain claim.</li>','<li><b>Check scope and strength.</b> Does this argument require that much, about that group?</li>').replace('<li><b>Negate what\'s left.</b> If the argument falls apart, that\'s your answer.</li>','<li><b>Negate a finalist.</b> Keep the premises true and test whether the reasoning still supports its conclusion.</li>')
t=t.replace('<li><b>A short conditionals bootcamp,</b> just to keep you sharp.</li>','<li><b>Conditionals refresher:</b> we discussed a possible short bootcamp. That remains on hold while the material is being completed.</li>')
t=t.replace('<style>/*CSS*/</style>','<style>/*CSS*/ details{border:1px solid var(--line);border-radius:10px;padding:14px;margin:14px 0;background:white}summary{cursor:pointer;font-weight:600}summary:focus-visible,.chip:focus-visible{outline:3px solid #28594d;outline-offset:3px}.kicker{color:#785b16}body{overflow-wrap:break-word}</style>')
p.write_text(t,encoding='utf8')
ref='''# Necessary Assumption

Keep this beside necessary assumption practice. The answer must be required for the argument's reasoning. It does not have to prove the conclusion by itself.

## Separate what is given from what is claimed

Identify the conclusion and supporting premises. Accept the premises for this task. Keep their exact groups, time limits, comparisons and strength. Primary means main, not necessarily only. Most means more than half; it allows all unless the context says otherwise.

## Find what the reasoning needs

An assumption can connect ideas or rule out a threat to the connection. These are useful roles, not rules about whether the answer contains not. Both can be phrased positively or negatively.

Ask what must be true for these reasons to support this conclusion. The assumption may concern information not expressly discussed in the premises. New wording alone is not a reason to reject it.

## Negate the complete answer

Suppose the candidate answer is false while the premises stay true. Does that undermine a connection the reasoning needs? If the argument can still work without the answer, the answer is not necessary.

You are testing the support, not demanding that the conclusion itself become false. A conclusion could still be true for an unrelated reason even when this argument fails to support it.

| Original | Negation |
|---|---|
| All guests arrived. | At least one guest did not arrive. |
| Some guests arrived. | No guests arrived. |
| The shop is open on Monday. | The shop is not open on Monday. |
| If the café is busy, Sam works late. | The café is busy and Sam does not work late. |
| At least one block was finished. | No block was finished. |

## Keep the two conditional operations separate

The contrapositive reverses the complete conditions and negates each one. It says the same thing as the original conditional. Negating an entire conditional instead gives a counterexample: its starting condition is true and its required result is false. For compound conditions, apply AND/OR negation to the whole condition.

## Test meaning, not strong or weak words

Only, always, most and primarily deserve attention, but none is an automatic elimination. Check whether this particular argument requires that claim. A weak answer can be irrelevant; a strong one can be necessary.

A prediction that someone will travel is not automatically equivalent to a requirement that they must travel. Preserve the actual modality and context rather than upgrading ordinary future tense into necessity.

## Do not confuse necessary with sufficient

Suppose a club permits voting only for registered people. An argument concludes Maya may vote. Maya must be registered, but registration alone need not guarantee permission. Every registered person may vote would be a stronger, different claim, not something that conclusion requires about everyone.

A sufficient assumption, together with the premises, makes the conclusion follow. A necessary assumption passes the requirement test. Strength by itself does not identify either task.
'''
(f/'necessary-assumption.md').write_text(ref,encoding='utf8')
primer=(f/'primer-negation-station.md').read_text(encoding='utf8').replace('Negation never flips anything. You put a "not" on the whole idea and stop there.','Negate the complete idea, not just a word. For an if/then claim, give the case where the starting condition is true and the required result is false. For all, one exception is enough; for some, the negation is none.')
(f/'primer-negation-station.md').write_text(primer,encoding='utf8')
spec=importlib.util.spec_from_file_location('manual',root/'.agents/skills/post-session-recap/references/session-manual/build_session_manual.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
(f/'recap.html').write_text(t.replace('/*CSS*/',m.CSS),encoding='utf8')
for name,kicker,marker in [('necessary-assumption.md','Reference · Keep it open while you drill','yahunatan-necessary-assumption-reference'),('primer-negation-station.md','Before you start · Negation Station','yahunatan-2026-10-20-negation-primer')]:
 out=m.from_md(str(f/name),kicker,marker);(f/name.replace('.md','.html')).write_text(out,encoding='utf8');m.lint(name,out)
canonical=root/'students/yahunatan-zetvy/recaps/2026-10-20-recap.md';old=canonical.read_text(encoding='utf8');front=re.match(r'---.*?---',old,re.S).group();divider=old.find('<!-- PRIVATE CONTINUATION');
if divider<0:divider=old.find('## Private')
private=old[divider:] if divider>=0 else '\n<!-- PRIVATE CONTINUATION -->\n'+old
body=t[t.index('<header'):t.index('<script>')];body=re.sub(r'<div class="footer-note">.*','',body,flags=re.S)
canonical.write_text(front+'\n\n'+markdownify(body,heading_style='ATX')+'\n\n'+private+'\n\n## 2026-10-25 accuracy revision\n\nPreserved earlier source/history above and backups under brainstorms/2026-10-25-yahunatan-post-session/before-accuracy-revision. Corrected false pre-teacher credit using transcript 00:05:13 and 00:28:42; retained accurate after-discussion credit. Transcript 00:54:18 onward gives answer-form and strong-word shortcuts and 01:08:09 to 01:12:06 equates will with must. These are source-backed but logically unsafe as general rules; student copy qualifies/replaces them rather than presenting them as universal. Negation targets required support, not necessarily conclusion truth. Conditional refresher tentative at01:13:09 and now on hold per currentJoshua direction. No assignment/post performed by this revision.\n',encoding='utf8')
m.lint('recap',t)
