from pathlib import Path
import html, re, subprocess, sys

ROOT = Path(__file__).resolve().parents[2]
CSS_EXTRA = '''details{border:1px solid var(--line);border-radius:12px;background:#fff;margin:16px 0;padding:16px 20px}summary{cursor:pointer;font-weight:600;color:var(--ink)}summary:focus-visible{outline:3px solid #315b54;outline-offset:5px}details[open]{border-color:#315b54}.path{display:flex;align-items:stretch;gap:12px;margin:22px 0}.path>div{flex:1;background:#edf3ee;border:1px solid #aac1b2;padding:18px;border-radius:12px}.path b{display:block}.path>span{align-self:center;font-size:28px}.source-label{font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-mute)}@media(max-width:600px){.path{flex-direction:column}.path>span{transform:rotate(90deg)}.wrap{overflow-wrap:anywhere}}'''

def section(kicker,title,body):
    return f'<section><div class="wrap"><div class="sec-kicker">{kicker}</div><h2>{title}</h2>{body}</div></section>'
def check(q,a):
    return f'<details><summary>{q}</summary><p>{a}</p></details>'
def card(title,body,colour='assume'):
    return f'<article class="kind {colour}"><span class="bar"></span><h3 class="name">{title}</h3><p class="what">{body}</p></article>'
def page(marker,title,lede,sections):
    return f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="lsatu-interactive-lesson" content="{marker}"><title>{title} · Session Manual</title><style>/*CSS*/\n{CSS_EXTRA}</style></head><body><header class="hero"><div class="wrap"><div class="kicker">Session Manual · October 21</div><h1>{title}</h1><p class="lede">{lede}</p></div></header>{''.join(sections)}<footer class="footer-note"><div class="wrap"><span class="mark">LSAT U</span></div></footer><script>document.querySelectorAll('details').forEach((d,i)=>{{let s=d.querySelector('summary');s.setAttribute('aria-expanded','false');d.addEventListener('toggle',()=>s.setAttribute('aria-expanded',String(d.open)));}});</script></body></html>'''

sofia_sections = [
section('Start here','What does the argument need?', '''<p>A necessary assumption is an unstated idea the argument depends on. Without it, the author's evidence no longer supports the conclusion in the way the author needs.</p><p>That doesn't mean the conclusion becomes false. Someone could reach a true conclusion with a broken argument. Our job is to test this argument's support.</p><div class="callout"><span class="tag">Keep the task precise</span>Ask, “Could the author keep this reasoning if this answer were false?” An answer that merely helps is not enough.</div>'''),
section('Two ways an answer can help','Connect the ideas. Rule out the problem.', '<div class="kinds">'+card('Supply a missing connection','A café has longer opening hours. The author predicts more sales. The argument needs some way for those extra hours to produce sales.')+card('Rule out a damaging possibility','A shop plans to cut delivery costs by changing couriers. The argument needs the new courier not to add fees large enough to wipe out the savings.','object')+'</div><p>These are two ways an assumption can work. An answer can connect what is given to what is claimed, or deny a possibility that would undermine that connection. The wording alone does not tell you which job it does.</p>'),
section('Keep the original strength','A factor is not a requirement', '''<p>“The awning helps keep the pavement dry” says the awning contributes. It does not say dry pavement is impossible without an awning. A rain-free day could leave it dry too.</p><div class="opposite"><div><b>Contributes</b><p>Helps produce an outcome. Other ways may exist.</p></div><div><b>Is required</b><p>Without it, the outcome cannot happen.</p></div></div><p>Keep that distinction while rephrasing the conclusion. If you turn “helps” into “is required,” you'll begin looking for an answer to a stronger argument.</p>'''),
section('Test the finalist','Negate the whole answer', '''<p>Suppose an author says, “Use the courtyard for lunch because it has enough tables for our group.” One required idea is that the group can actually use those tables at lunchtime.</p><div class="path"><div><b>Answer</b>The tables are not all reserved for another group at lunchtime.</div><span aria-hidden="true">→</span><div><b>Negation</b>All the tables are reserved for another group at lunchtime.</div></div><p>Under that negation, having enough tables no longer gives this group a reason to choose the courtyard. The tables cannot serve the purpose the author gives them.</p><p>Here, removing “not” negates the answer correctly. Always check the whole meaning. Don't delete a word mechanically from a sentence with quantities or several clauses.</p><div class="callout"><span class="tag">The trap</span>“Not” is not a correctness signal. A positive answer can be necessary, and a negative answer can be irrelevant. What matters is what happens to the reasoning after the answer is negated.</div>'''),
section('Keep the same subject','General information is not a fact about this group', '''<p>“Extra opening hours can increase sales” gives a general possibility. “These three cafés increased their sales” makes a claim about particular cafés. To connect them, the author needs relevant information about those cafés.</p><p>Likewise, a change can happen during a period without producing a different final total. Spend $10 and receive $10: the balance ends where it began. Don't turn “something happened” into “the total must have changed.”</p><div class="quote">You explained why the author's recommendation needs a connection between the action and the result. You also identified the missing connection in the later question before we worked through the explanation.</div>'''),
section('Say the answer first','Three checks before you reveal',
check('A museum should extend its hours because visitors want more evening access. Must every visitor want evening access?','No. The recommendation could have support without every visitor wanting it. “Every” adds a claim the argument does not need.')+
check('A collection gained five books and lost five books. Must its total have increased?','No. The gains and losses can cancel. Activity is not the same as a net increase.')+
check('The argument says a new chair will reduce discomfort. A finalist says the chair is not too large for the desk. What should you test?','Assume the chair is too large for the desk. Then ask whether that fact defeats the particular reason offered for using the chair. A nearby inconvenience alone does not automatically defeat the reasoning. You need a connection to what the argument claims.')),
section('When two answers remain','Keep this order', '''<ol class="steps"><li>Rephrase the conclusion without changing its group, strength or recommendation.</li><li>Name the evidence. What reason is supposed to support that conclusion?</li><li>Explain what each finalist supplies or rules out.</li><li>Negate the complete answer. Keep the evidence fixed and describe the damage to its support.</li></ol>'''),
section('Before your next section','Warm up, then practise the method', '''<ol class="steps"><li>Use a short warm-up before a section. In our session we discussed getting three or four questions right in a row before beginning. Explain why each is right rather than racing for a streak.</li><li>Do the matching Necessary Assumption practice untimed. For each finalist, write the conclusion, the answer's negation and one sentence explaining what happens to the support.</li><li>Practise earlier when your schedule allows. You noticed that late-night work after other homework was a poor setting for careful reading.</li></ol><p>We also discussed a possible small group session. Its time was not confirmed during our session.</p>''')]

celia_sections = [
section('Start with the target','What are you being asked to believe?', '''<p>A conclusion is the claim the author wants you to accept. Evidence gives reasons for it. Once you know the conclusion, return to the evidence and ask how those reasons are supposed to get you there.</p><p>Suppose an author says a whole festival went over budget, so its children's workshop must have gone over budget. You don't need to know the festival's name. You do need to keep the difference between the whole festival and one workshop.</p><div class="path"><div><b>Evidence</b>The whole festival went over budget.</div><span aria-hidden="true">→</span><div><b>Conclusion</b>One workshop went over budget.</div></div><p>The music stage could have caused the overspend while the workshop stayed within budget. The evidence can be true while the conclusion is false.</p>'''),
section('Simplify carefully','Keep what controls the reasoning', '<div class="kinds">'+card('The story','Names and setting can often be shortened: a festival, a workshop, a budget. Understand the original meaning before replacing them.')+card('The relationship','Keep whole versus part, some versus all, sometimes versus always, and what is offered as a reason for what. Those details can decide the answer.','describe')+'</div><p>Generalizing is not just replacing nouns with letters. You can use short ordinary labels. Your version should be simpler while leaving the author making the same claim for the same reason.</p><div class="quote">On the project question, you identified that the evidence concerned the whole while the conclusion concerned a part. Keep trusting that distinction. It is exactly what the argument needed us to track.</div>'),
section('Read the direction','Whole to part is different from part to whole', '''<div class="opposite"><div><b>Whole to part</b><p>The whole festival was expensive, so this workshop was expensive.</p></div><div><b>Part to whole</b><p>This workshop was expensive, so the whole festival was expensive.</p></div></div><p>Neither inference is guaranteed by the information shown. But they are different errors. If an answer describes evidence about each part supporting a conclusion about the whole, it does not match an argument going from the whole to one part.</p><p>Some properties do transfer. If every object in a box is red, a particular object in that box is red. That evidence directly covers each object. Don't reject every sentence involving a group; check what the evidence actually says.</p>'''),
section('Keep the time','Missing now does not mean never there', '''<p>Someone says a recording was deleted. The reply is, “There is no recording in the folder now.” Could both claims be true?</p>'''+check('Think first, then check the reply','Yes. Deleting the recording could explain why it is missing now. Its current absence does not show it never existed, and it does not clear someone of deleting it.')+'''<p>The reply describes the current situation. The accusation concerns what happened earlier. Shortening both to “no recording” would erase the difference the question tests.</p><div class="quote">You gave this distinction yourself: something could be missing because it was destroyed. You also explained it without relying on the original topic.</div>'''),
section('Check whether the reason is new','A conclusion cannot support itself', '''<p>“This bakery is the best because its bread is better than every other bakery's bread.” The reason has restated the judgment. It hasn't offered an independent reason to believe it.</p><p>That is circular reasoning: the support already assumes what the author is supposed to prove. Compare it with “This bakery won a blind tasting against the other bakeries.” That gives a separate reason, even if we still need to inspect how good the test was.</p><div class="callout"><span class="tag">Before naming the flaw</span>Say what the author wants you to accept, then say what the author gives you. If the second just repeats the first, there is no independent support.</div>'''),
section('Keep the amount','Sometimes does not mean always', '''<p>Suppose two duties are said to apply without exception, but one situation makes it impossible to fulfil both. That single situation challenges the claim that both duties can always be fulfilled together.</p><p>It does not show that the duties can never be fulfilled together. A different situation might allow both. In parallel reasoning, keep that difference when comparing conclusions.</p>'''),
section('Try the distinction','Explain before opening',
check('A whole orchestra is loud. Therefore its quietest instrument is loud. What is the direction?','Whole to part. The conclusion concerns one instrument, but the evidence concerns the orchestra together. Other instruments could account for the volume.')+
check('The museum is trustworthy because everything it says can be trusted. Is there an independent reason?','No. The reason repeats the claim of trustworthiness. It gives no separate support for believing it.')+
check('Two tasks conflict on one afternoon. Does that show they can never be completed together?','No. It shows at least one conflict. Other afternoons might allow both. Preserve “sometimes” rather than replacing it with “never.”')),
section('When the wording gets dense','Translate, then match both halves', '''<ol class="steps"><li>State the conclusion in a complete short sentence.</li><li>State the evidence and keep its group, time and strength.</li><li>Describe the gap in ordinary language. Try a case where the evidence is true and the conclusion fails.</li><li>Translate the answer. Point to exactly what each part describes in the argument.</li><li>Check the direction. The same two ideas in the wrong roles do not match.</li></ol>'''),
section('Before your next section','Practise the explanation, not just the letter', '''<ol class="steps"><li>Use the generalization checklist above on your early LR questions. Shorten the story only after you understand it; keep every qualification that affects the reasoning.</li><li>Work through matching abstract Flaw practice untimed. Explain the wrong answers too: what would an argument have to say for that description to fit?</li><li>Use your Reading Center access for a short reading warm-up. We discussed punctuation pauses, variable speed and three-to-five-word highlighting. Your saved 180 speed was a starting setting, not a required target. Slow down if meaning is being lost.</li><li>After a reading chunk, look away and explain its point. If you cannot explain it, adjust the pace before beginning a section.</li></ol><p>We discussed adding retention questions and a demonstration. Those were follow-ups for me, not extra homework for you. We also discussed a possible Sunday group session; it was not confirmed during the session.</p>''')]

sofia_primer = '''# Test what the argument cannot lose

Before Necessary Assumption - First Taste, keep one question in mind: if this answer were false, could the author's evidence still support the conclusion in the same way?

## What this drill asks you to do

The published drill contains ten untimed Necessary Assumption questions. It asks you to look for a missing connection, check assumed similarities or differences, and try to accept the evidence while challenging the conclusion. Its answer review includes negative wording and conditional answers.

These are different ways to find the same requirement. Do not invent an objection unrelated to the author's reasoning.

## One habit for every finalist

Write the conclusion first. Negate the whole answer, then explain the damage in one sentence. Keep the evidence fixed. The test concerns its support, not whether the conclusion could happen to be true for another reason.

## A short example

“Hold lunch in the courtyard; there are enough tables.” A finalist says the tables are not all reserved for another group at lunchtime. Negate it: all the tables are reserved for another group then. The available number of tables no longer supports this group's plan.

Removing “not” works for this particular sentence. Read the whole meaning before applying that shortcut elsewhere. A conditional needs a case in which its condition holds but its required result does not; simply swapping its sides is not its negation.

## Keep the practice untimed

Explain why the correct answer is required and why a tempting rival is merely helpful, too strong or unrelated. If a proposed objection doesn't affect the author's reason, it isn't a reason to choose the answer.
'''
sofia_ref = '''# Necessary assumptions: test the support

A necessary assumption is an unstated idea the author's reasoning requires. It need not prove the conclusion by itself. Negating it must undermine the support the argument offers.

## Read before testing answers

1. Name the conclusion, keeping its exact strength and group.
2. Name the evidence.
3. Ask what connection the author needs, or what damaging possibility the author must rule out.
4. Test the answers against that particular reasoning.

## Two useful questions

**Missing connection:** What did the conclusion introduce that the evidence hasn't connected?

**Potential objection:** What could be true alongside the evidence that would undermine its support? An answer denying that problem may be required.

An answer can be necessary even if its topic was not named earlier. An unmentioned detail is not automatically irrelevant. Explain whether it affects the author's reasoning.

## Negate precisely

| Answer says | Its negation says |
|---|---|
| All the lamps work. | At least one lamp does not work. |
| Some lamps work. | No lamps work. |
| No lamps work. | At least one lamp works. |
| The lamp is not broken. | The lamp is broken. |
| Most lamps work. | At most half the lamps work. |

For “If a parcel is marked urgent, it is delivered today,” its negation allows at least one urgent parcel that is not delivered today. The negation is not “If it is not urgent, it is not delivered today.”

Keep complete conditions and the same population. “Not all” does not mean “none.” Quantities can make mechanical word deletion misleading.

## Ask what actually breaks

Suppose the author recommends a route because it is open to cyclists. An answer says the traveller can use a bicycle. If the traveller cannot cycle, openness to cyclists no longer supports that person's route choice in the intended way.

You have not proved the route unusable for everyone. You have tested the reason for this recommendation. A true conclusion can still have inadequate support.

## Helpful is not the same as required

Good weather could help a bicycle trip. But the route recommendation might still make sense on a cloudy day. Negating a merely helpful detail does not necessarily defeat the reasoning.

Do not select the weakest-looking answer automatically. The right answer must be required, whether its wording is strong or modest. Do not select “not” automatically either.

## Compare the last two

For each answer, say: “The author needs this because…” Then negate it and complete: “Without it, this evidence fails to support the conclusion because…” If you cannot explain the connection, return to the exact conclusion rather than defending the answer from general knowledge.
'''
celia_primer = '''# Translate the answer before choosing it

Abstract + Flaw (set 1) is about understanding what abstract answer choices describe. You are practising the explanation behind the letter.

## What this drill asks you to do

The published drill gives ten untimed Flaw questions with abstract answer wording. It asks you to inspect wrong answers too. Name a familiar flaw when it fits, and invent a short example of what the description would mean in an argument.

## Match both halves

First write the conclusion and the evidence in ordinary words. Then translate a finalist. If it says the author gives a part a quality because the whole has it, point to the part, the whole and the quality in this argument.

If those roles do not match, shared vocabulary is not enough.

## Try one before you begin

“The festival went over budget, so its children's workshop went over budget.” The whole is the festival. The part is the workshop. The quality is going over budget. The evidence concerns the whole; the conclusion concerns a part.

An answer describing the opposite direction does not fit. The workshop could have stayed within budget while the music stage caused the overspend.

## One habit for review

For a wrong answer, make up the shortest example that would make it right. Then compare that example with the actual argument. Keep the amount, direction and timing intact.
'''
celia_ref = '''# Read abstract Flaw answers in ordinary words

A Flaw answer describes why the author's evidence fails to justify the conclusion. Translate the description, then check it against the actual argument.

## Begin with the argument

1. Say exactly what the author wants you to accept.
2. Say what reason the author gives.
3. Describe what is missing or confused.
4. Try a concrete situation in which the evidence is true but the conclusion is false.

You do not need a famous name before you can explain the problem. A name helps only when its meaning fits.

## Three kinds of wording

| The answer does this | Ask this |
|---|---|
| Says the author assumes something | Does the reasoning need that unstated idea? |
| Says the author overlooks a possibility | Could that possibility coexist with the evidence and damage its support? |
| Describes what the author does | Can I point to the exact evidence, conclusion and relationship described? |

An overlooked possibility need not be proved true to expose an unsupported inference. It must matter to this reasoning, rather than merely be imaginable.

## Match the same ideas consistently

“Infers that a part has a property because the whole has it” has three things to locate: the part, the whole and the property. The whole supplies the evidence; the part appears in the conclusion.

“The choir is loud, so this singer is loud” fits. “This singer is loud, so the choir is loud” reverses the direction. An answer describing one does not describe the other.

Do not strip away a qualification to force a match. “Every singer is loud” already covers each singer and supports a claim about a named singer in that group.

## Familiar descriptions, with small examples

| Description | What it means | Example |
|---|---|---|
| Assumes the conclusion | The offered reason already takes the conclusion for granted. | The rule is fair because it treats people fairly. |
| Confuses whole and part | A quality of one is transferred to the other without support. | The meal is expensive, so the bread must be expensive. |
| Treats a requirement as enough | Having something required is treated as proving the result. | Every member has a card; Jo has a card, so Jo is a member. |
| Confuses absence now with absence earlier | Current missing evidence is treated as proving it never existed. | The file isn't here now, so nobody deleted it. |

The file example leaves open deletion. It does not prove who deleted a file or even prove deletion occurred. That is why it defeats the reply's reasoning without settling the whole dispute.

## Preserve the strength

“Sometimes two tasks conflict” does not mean they always conflict. “Some members agree” does not mean all members agree. “The result is likely” is not “the result is certain.” Keep those words in your paraphrase and in your reading of the answer.

## When an answer sounds convincing

Translate it into a short fresh example. Then return to the actual argument. If the example describes a different direction, stronger claim, different group or different point in time, the answer does not match merely because it sounds familiar.
'''

private_sofia = '''## Private source map and commitments

Full transcript read: students/sofia/sessions/2026-10-21-necessary-assumptions-and-warm-up/transcript.md. Calendar/email identity sofiaminassian@gmail.com. Notes describe the 2026-10-21 session, not a new session on build date.

| Evidence | Timestamp | Use |
|---|---|---|
| Rephrase conclusion, contribution not necessity | 00:10:53 to 00:13:22 | Exact claim strength |
| Required unstated idea; needs vs guarantees | 00:14:52 to 00:19:13 | Definition and two functions |
| Positive/negative wording and negation discussion | 00:21:48 to 00:32:34 | Correctly bounded whole-answer negation; no not-answer preference |
| Oil totals may cancel; particular nations vs general possibility | 00:35:37 to 00:44:02 | Net change and group scope |
| Student independently identifies missing connection; later difficult answer selected before discussion | 00:48:25 to 00:50:20; 00:52:11 to 00:57:43 | Specific credit; not invented mastery |
| Late practice after homework, benefit of break | 00:58:30 to 00:59:16 | Study context |

| Owner | Commitment or work | Timestamp | State |
|---|---|---|---|
| Sofia | Warm up with three or four correct in a row before section | 00:58:30 to 01:00:10 | Session recommendation, no quantity/deadline beyond warm-up |
| Sofia | Practise earlier when feasible | 00:59:16 | Session recommendation |
| Sofia | Repurchase package and report booking difficulty | 01:00:10 | Student said she would do it; current account status unverified |
| Joshua | Invite to mini group; likely that weekend, not confirmed | 01:00:10 to 01:01:26 | Tentative timing; invitation unverified; do not send or book automatically |
| Assistant | Necessary Assumption - First Taste, w2-07-necessary-assumption-first-taste, ten untimed, beginner 1 to 3 | Draft selection 2026-10-25 | Candidate, not yet assigned by this draft |

All courtyard/café/museum/chair examples are new neutral examples, not original test stimuli. Personal ethnicity/religion analogy omitted: not a sound general logical exclusion. Negation weakens the argument's support, not necessarily the truth of its conclusion. Do not reproduce Gemini's implication that negation means deleting not from every answer. Existing Parallel reference/assignment Sep11 does not prove current availability or completion. Method reference requires live posted-note duplicate check before delivery. Assignment dates and final live status belong to the operator's verified plan.

Sources: references/lsatu-guided-drill-catalog.json (exact published instruction_card read, refreshed 2026-10-25); corpus/Curriculum/Necessary Assumption/Notes/_megadoc_notes_necessary_assumption.md (fragmentary export; full method above primarily session-grounded). All three notes DRAFT, not posted.
'''
private_celia = '''## Private source map and commitments

Full transcript read: students/celia-cutler/sessions/2026-10-21-generalization-flaws-and-reading-warm-up/transcript.md. Calendar/email celiacutler@gmail.com, existing class identity 749e2eae-7969-464f-bf96-a4d4cfafe2bf. Speaker label Celia Syrocki is a preserved surname discrepancy, not a new alias.

| Evidence | Timestamp | Use |
|---|---|---|
| Multiword chunks clearer than single words; pauses and variable speed | 00:01:49 to 00:08:23 | Reading warm-up and preferences; 180 is saved setting, not target |
| Early hard questions disrupt pacing | 00:12:08 | Early-question practice; no invented timed quota |
| Initial sociologist B chosen via elimination | 00:15:19 to 00:24:43 | Circularity taught generally, not contradiction |
| Simplify while retaining relationship and conclusion | 00:34:37 to 00:54:38 | Central lesson |
| Sometimes vs always; matching conclusion structure | 00:45:46 to 00:50:20 | Exact strength |
| Celia correct on whole/part; teacher reverses then explicitly corrects | 01:03:03 to 01:07:41, correction 01:05:45 | WHOLE evidence to PART conclusion; credit Celia |
| Independently generalizes destroyed evidence vs present absence, chooses A | 01:09:17 to 01:14:24 | Specific credit |
| Sociologist question resumed and B confirmed | 01:15:59 to 01:28:02 | No invented continuity; independent support |

| Owner | Commitment or work | Timestamp | State |
|---|---|---|---|
| Celia | Reading warm-up with pauses, variable speed, three-to-five-word highlights, pace adjusted for meaning | 00:05:02 to 00:08:23 | Recommended; existing Reading Center in_progress item 3ef6c6db-ec23-4da5-9960-221466605fd1 must be reused |
| Joshua | Add sample retention questions to reading passages | 00:08:23 to 00:09:13 | Began tentative, then explicit “I'll do that”; product delivery unverified |
| Joshua | Fix reported RC recall recognition issue | 00:09:13 | Promised, no exact deadline, not independently reproduced here |
| Joshua | Provide high-quality recall demonstration | 00:10:11 | Promised; completion unverified |
| Joshua | Supply bulleted generalization takeaways in note | 00:52:52 to 00:53:56 | This draft covers teaching; not delivered yet |
| Celia | Apply approach to first ten questions | 01:15:14 and 01:28:02 to 01:30:24 | Session practice recommendation; no fixed new homework set or due date |
| Joshua | Group-session invitation, likely Sunday, confirmation Friday night | 01:30:24 | Tentative event; 2026-10-25 Sunday/2026-10-23 Friday now historical, actual invite unverified |
| Assistant | Abstract + Flaw (set 1), w2-02-abstract-flaw-set-1, ten untimed, intermediate 2 to 4 | Draft selection 2026-10-25 | Candidate, not assigned by this draft |

New festival/orchestra/bakery/file examples deliberately replace original test stimuli. Part/whole direction follows the explicit teacher correction, not erroneous earlier transcript/Gemini summary. Avoid framing simplification as ignoring evidence or reducing all arguments to conditionals. Method reference: reuse/adapt existing Reading Flaw Answer Choices if present in current student notes; this draft preserves separate identity pending live duplicate check. Existing August Parallel note is a different method; do not overwrite it. Check final live assignment state before adding work.

Sources: references/lsatu-guided-drill-catalog.json (exact ten untimed instruction_card read); corpus/Curriculum/Flaw and Famous Flaws/Notes/reference_flaw.md (fragmentary curriculum pointer), approved Session Manual Reading Flaw Answer Choices. All three notes DRAFT, not posted. Product fixes, group invitations and notification receipt are not claimed complete.
'''

for slug, title, lede, secs, primer, ref, private in [
('sofia','What the Argument<br>Cannot Lose','Keep the author’s exact claim in view. Then test which unstated idea its support cannot do without. The answer can be required without being enough to prove the conclusion.',sofia_sections,sofia_primer,sofia_ref,private_sofia),
('celia-cutler','Keep the Reasoning.<br>Shorten the Story.','A shorter version should make the argument easier to inspect. Keep the conclusion, the reason and the details that control their relationship. Those are the pieces an abstract answer must describe.',celia_sections,celia_primer,celia_ref,private_celia)]:
    folder=ROOT/'brainstorms'/f'2026-10-25-{slug}-post-session'
    folder.mkdir(parents=True,exist_ok=True)
    src=page(f'{slug}-2026-10-21-session-recap',title,lede,secs)
    for name,content in [('recap.src.html',src),('drill-primer.md',primer),('method-reference.md',ref)]:
        target=folder/name
        if target.exists(): raise RuntimeError(f'Refusing to overwrite {target}')
        target.write_text(content,encoding='utf8')
    text=re.sub(r'<script>.*?</script>|<style>.*?</style>','',src,flags=re.S)
    text=re.sub(r'</(?:p|h[1-6]|section|div|li|summary|details|article|header)>','\n\n',text)
    text=html.unescape(re.sub('<[^>]+>','',text))
    text=re.sub(r'\n\s*\n(?:\s*\n)+','\n\n',text).strip()
    canonical=ROOT/'students'/slug/'recaps'/'2026-10-21-recap.md'
    canonical.parent.mkdir(exist_ok=True)
    if canonical.exists(): raise RuntimeError(f'Refusing to overwrite {canonical}')
    canonical.write_text(f'---\ntitle: {html.unescape(re.sub("<[^>]+>"," ",title))}\nstudent: {slug}\nsession_date: 2026-10-21\nbuilt: 2026-10-25\nstatus: draft\nposted: false\n---\n\n{text}\n\n<!-- PRIVATE CONTINUATION: not student-facing -->\n\n{private}',encoding='utf8')
    subprocess.run([sys.executable,str(ROOT/'.agents/skills/post-session-recap/references/session-manual/build_session_manual.py'),str(folder),f'drill-primer.md|Before you start · Matching guided drill|{slug}-2026-10-21-drill-primer',f'method-reference.md|Reference · Keep it open while you drill|{slug}-2026-10-21-method-reference'],check=True)
