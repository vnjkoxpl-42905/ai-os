from pathlib import Path
import sys, importlib.util, re
ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('manual',ROOT/'.agents/skills/post-session-recap/references/session-manual/build_session_manual.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
folder=Path(__file__).parent
recap='''# Keep the evidence separate from the conclusion

A clear argument can still leave something unproved. Your job is to understand the evidence, name the exact conclusion, and check the connection between them. Start there before sorting the answers.

## Step zero: say what each part claims

The premise is what the author gives as a reason. The conclusion is what the author wants you to accept because of that reason. An argument can contain several premises and an intermediate conclusion that supports a further conclusion.

Keep the reason and the conclusion separate while you test their connection. Accepting a premise does not mean accepting the conclusion built on it.

For example: A shop's customers have different tastes, so the shop should offer several flavours. The customer differences are the reason. Offering several flavours is the recommendation. The missing connection concerns whether that variety will help serve those customers.

You explained that premises and conclusions are separate, and that the gap between them is what we need to inspect. Keep using that distinction when the subject becomes less familiar.

## Two questions that do different jobs

<div class="kinds"><article class="kind describe"><span class="bar"></span><h3 class="name">What does the evidence say?</h3><p class="what">Customers have different tastes.</p><div class="test"><b>Keep it exact</b>This does not yet tell us which menu would serve them best.</div></article><article class="kind object"><span class="bar"></span><h3 class="name">What does the author conclude?</h3><p class="what">The shop should offer several flavours.</p><div class="test"><b>Test the connection</b>Would variety actually help this customer base?</div></article></div>

A strengthening answer adds support for that connection. Suppose a single-flavour menu drives away customers who dislike that flavour. That gives a reason to favour variety. It need not prove the recommendation beyond every possible doubt.

An answer about poor-quality ingredients asks a different question. Unless it connects to the choice between variety and one flavour, it does not help us decide which strategy is better.

<div class="callout"><span class="tag">The trap</span>New information is allowed in strengthening questions. Reject an answer because it fails to support this argument, not simply because its words are new.</div>

## A cause is not automatically the only possible cause

Suppose a heater helped warm a room. That does not show the room could not have become warm without that heater. Sunlight or a second heating system might have produced the same result.

The important difference is between helping produce an outcome and being required for that outcome. Other contributing causes could work alongside the heater. An alternative cause could potentially produce the warmth without it. Ask which claim the conclusion actually needs.

You identified this distinction in the city-layout discussion: showing that something contributed does not show that the outcome could only have happened that way.

## Keep an alternative explanation inside the conclusion's scope

If the conclusion concerns room temperature, an answer saying that sunlight changes people's moods does not address it. Sunlight affecting something is not enough. We need a connection to the temperature we are trying to explain.

This is why you return to the exact conclusion when two choices look close. Name the outcome, the group, and the strength of the claim. Then ask what each answer actually changes.

## Break a long sentence where the meaning breaks

Read a piece you can explain. Pause. Tell it back in ordinary language. Then connect the next piece to it. A shorter piece is useful if it preserves the meaning; a short topic label is not enough.

Words such as because, since, for and after all can introduce reasons. Check their meaning in context: since can also refer to time. A contrast word such as but does not automatically identify a conclusion.

## Say your answer, then check

<details><summary>A lamp helped brighten a room. Must the room have been dark without it?</summary><p>No. Another light source might have brightened it. Helping cause the brightness does not by itself make that lamp necessary.</p></details>

<details><summary>The conclusion concerns quieter classrooms. An answer says a new timetable improves lunch service. Does it address the conclusion?</summary><p>Not by itself. The answer needs a connection to classroom noise. Helping a school in some other way is a different outcome.</p></details>

<details><summary>A strengthening answer mentions something the stimulus did not mention. Is that enough to reject it?</summary><p>No. New information can strengthen. Ask whether it supports the connection between these premises and this conclusion.</p></details>

## When you are down to two answers

1. Say the exact conclusion without looking at the answers.
2. Say the evidence separately.
3. Explain how each answer affects that connection.
4. Give a specific reason for rejecting the other choice. A familiar topic is not enough.

## Your next study session

Resume on Monday, October 26, keeping Sunday as your rest day. Review these notes, then work through the fresh PT104 Section 1 practice selected for you. The same section can support Read, Recall, Colour practice. Keep the earlier unfinished sections as existing work rather than restarting all of them at once.

The guided follow-up is The Core Connection: practise identifying the evidence, conclusion and gap. The accompanying primer explains the separate full-section recall routine. Keep one short explanation of why your chosen answer works and why the closest alternative fails.

[Schedule your next session](https://lsatprep.study/book/oreoluwa-pgavqgtp3weqxmuxy2axt96495). We can use your section to decide what needs attention next.

We discussed conditionals as the next tutoring direction, after using your practice to see where to focus. A complete conditional bootcamp was not part of this session's homework plan.
'''
primer='''# Find the connection. Keep the details.

Before Read, Recall, Colour · PT104 Section 1, use a small enough piece that you can explain exactly what it says. The purpose is to retain the argument, not repeat its wording.

## Before The Core Connection

This seven-question guided set focuses on links inside arguments. Find the conclusion and the main supporting premise before you test the answers. Read each question's stem: the set includes several tasks, so the same answer test does not apply to every question.

On Strengthen, ask what adds support. On Weaken, ask what undermines the connection. On Flaw, ask what reasoning problem the argument actually contains. A necessary assumption must be required; a sufficient assumption must make the conclusion follow when added to the premises. Do not treat those two tasks as interchangeable.

For every question, say one sentence: The evidence says this, but the author concludes that. Then explain what the selected answer does to that connection. The full method reference gives the task boundaries. Follow the guided set's own instructions and feedback as you proceed.

## The current drill routine

1. Read about a sentence silently. Take less if the beginning slips away.
2. Look away and tell it back out loud in your own words.
3. React out loud to that particular content. Ask a question, give an example, or say what seems doubtful. Keep the given claim separate from your reaction.
4. Continue through the stimulus. During these steps, the text remains on screen; looking away is your job.
5. Once you have worked through the whole stimulus, press Space. The text disappears. Retell the whole argument from memory, preserving its details.
6. Press Space again for the next stimulus. You cannot return to a previous one.

## What to keep

Keep names, groups, quantities, comparisons, time limits and connecting words. Customers having different tastes is not the same as customers wanting every available flavour. A cause helping is not the same as that cause being necessary.

Your own wording is required. Changing the order is fine when the meaning and relationships survive. A topic label such as marketing is not a recall of what the author claimed about marketing.

## One habit for this section

Before the final recall, check that you can say the evidence and the conclusion separately. Do not turn an uncertain conclusion into something the evidence already proved.

This is a whole-section spoken exercise. Follow the activity's recording and pause controls. Start carefully; completing the reasoning matters more than racing the clock.
'''
reference='''# Find the conclusion. Test the connection.

Keep this beside argument practice. Identify what the author wants you to believe, what reasons the author gives, and how those reasons are supposed to support the claim.

## First separate the parts

The conclusion is the claim being supported. Premises are the reasons offered for it. Background gives context without necessarily supporting the conclusion. An intermediate conclusion receives support and then helps support another conclusion.

Indicator words are clues, not a substitute for meaning. Because often introduces a reason; therefore often introduces a conclusion. Test the relationship by asking which claim is offered as a reason for the other.

## Preserve the exact claim

Keep the group, outcome, comparison, time and strength. Could happen is weaker than must happen. More successful than a competitor is not the same as successful by an absolute standard. Helping produce an outcome does not show that the outcome requires that cause.

## Find what remains open

Accept the premises for this exercise. Ask whether the conclusion could still fail, or whether an important connection remains unsupported. Do not contradict a premise to manufacture a gap.

For example, a class with more revision sessions improved. The sessions might have helped, but that fact alone does not show they were the only possible route to improvement. Other factors could have contributed, and another approach might have worked instead.

## Let the question determine the task

| Task | What an answer needs to do |
|---|---|
| Strengthen | Add support for this conclusion given these reasons. It need not make the conclusion certain. |
| Weaken | Undermine the support for this conclusion. It need not prove the conclusion false. |
| Flaw | Describe something the argument actually does and explain a genuine problem in its reasoning. |
| Describe the reasoning | Accurately describe how the parts relate; it need not criticise the argument. |
| Must Be True | Follow from the supplied information. Do not add an unsupported assumption. |

## Check scope before choosing

An alternative explanation must concern the relevant outcome. An answer about happier workers does not automatically explain higher output. A choice that merely repeats a topic word may leave the actual reasoning untouched.

When two answers remain, return to the conclusion. Say what each answer contributes and why that contribution matters. In untimed review, keep working until you can justify the choice. Under a timed test, use your pacing plan rather than leaving an answer blank while seeking certainty.
'''
for name,body in [('primer-recall.md',primer),('argument-reference.md',reference)]: (folder/name).write_text(body,encoding='utf8')
page=m.from_md(str(folder/'primer-recall.md'),'Before you start · Read, Recall, Colour','ore-2026-10-23-primer-placeholder')
# Use the shared model shell with the recap's own exact teaching body.
import markdown
parts=re.split(r'^## (.+)$',recap,flags=re.M); first=parts[0].split('\n',1)[1].strip()
sections=''.join('<section><div class="wrap"><h2>'+h+'</h2>'+markdown.markdown(b,extensions=['tables'])+'</div></section>' for h,b in zip(parts[1::2],parts[2::2]))
extra='details{margin:16px 0;border:1px solid var(--line);border-radius:10px;background:white}summary{cursor:pointer;padding:16px;font-weight:600}details p{padding:0 16px}summary:focus-visible{outline:3px solid #28594d}body{overflow-wrap:break-word}.kicker{color:#785b16}@media(max-width:600px){.kinds{grid-template-columns:1fr}.opposite{flex-direction:column}}'
src='<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="lsatu-interactive-lesson" content="ore-2026-10-23-evidence-and-conclusion"><title>Keep the evidence separate · Session Manual</title><style>/*CSS*/'+extra+'</style></head><body><header class="hero"><div class="wrap"><div class="kicker">Session Manual · October 23</div><h1>Keep the evidence<br>separate</h1><p class="lede">'+first+'</p></div></header>'+sections+'<footer class="footer-note"><div class="wrap"><span class="mark">LSAT U</span></div></footer></body></html>'
(folder/'recap.src.html').write_text(src,encoding='utf8');(folder/'recap.html').write_text(src.replace('/*CSS*/',m.CSS),encoding='utf8')
for name,kicker,marker in [('primer-recall.md','Before you start · Read, Recall, Colour','ore-2026-10-23-recall-primer'),('argument-reference.md','Reference · Keep it open while you drill','ore-argument-connection-reference')]:
 out=m.from_md(str(folder/name),kicker,marker);(folder/name.replace('.md','.html')).write_text(out,encoding='utf8');m.lint(name,out)
private='''
<!-- PRIVATE CONTINUATION: not student-facing -->

## Source and delivery map | 2026-10-25

Full source read: ../sessions/2026-10-23-argument-refresher-and-causal-scope/transcript.md. Identity oreoluwavjames@gmail.com. Draft; no posting or assignments performed by this builder.

| Teaching / commitment | Time | Owner / status |
|---|---|---|
| Short consistent study; avoid long burnout cycles | 00:00:41 to 00:03:34 | Student preference; not a daily quota |
| Separate evidence/conclusion; accept evidence while testing inference | 00:08:09 to 00:16:40 | Central teaching |
| Regular section and practice test timetable | 00:19:44 to 00:20:44 | Joshua/Ore; discussed, exact timetable unresolved |
| Correct supported advertising choice and reject unsupported quality variable | 00:35:51 to 00:53:38 | Credit her actual reasoning; fresh shop example in recap |
| Chunk long claims | 01:01:51 to 01:07:11 | Teaching; current app instructions checked |
| Contributing cause versus only possible cause | 01:09:42 to 01:14:59 | Teaching; avoid claiming all causes are deterministic |
| Exact outcome scope of an alternative | 01:15:57 to 01:24:31 | Teaching; no outside-information blanket prohibition |
| Conditionals next session | 01:25:33 | Tentative teaching direction, no bootcamp promise |
| Fresh useful section plus registration link together | 01:27:08 to 01:28:15 | Joshua promise; pending delivery. Monday Oct26 for starting/resuming, not before-Monday deadline |
| Sundays off | 01:27:08 | Preserve; schedule new work Oct26 |

Live Classroom read 2026-10-25: five existing Read, Recall, Colour cards, none are notes/guided drills. PT21 S3 and PT1 S3 in_progress; PT101 S2, PT102 S3 and section-library assigned. Preserve all. Fresh recommended PT104 S1 ID4bb1242b-6b5b-42bb-b4c6-7b4769117115. The Core Connection w1-02-the-core-connection is assistant-proposed matching transfer, native7, beginner1to3 snapshoteligible291; parent must inspect actual content/preflight. Registration link absent from local Ore profile; must resolve current live booking path, not guess.

Current recalled-section instructions checked in sibling app src/features/activity-centre/content/read-recall-colour-section.instructions.json: text remains visible through claim practice; Space hides only for final whole-stimulus recall, second Space advances. Fresh examples are authored illustrations, not quoted test questions. Recap Markdown and generated HTML share the same teaching source, including hidden answers. Appearance and delivery approvals remain separate.
'''
target=ROOT/'students/ore/recaps/2026-10-23-recap.md';target.parent.mkdir(exist_ok=True)
if target.exists() and 'Source and delivery map | 2026-10-25' not in target.read_text(encoding='utf8'): raise RuntimeError('Preserve existing recap, review before replacing')
target.write_text('---\ntitle: Ore · Evidence and conclusion\nstudent: ore\nsession_date: 2026-10-23\nstatus: draft\nposted: false\n---\n\n'+recap+private,encoding='utf8')
m.lint('recap.html',src)
