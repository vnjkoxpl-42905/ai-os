from pathlib import Path
import importlib.util,re,markdown
ROOT=Path(__file__).resolve().parents[2];folder=Path(__file__).parent
s=importlib.util.spec_from_file_location('manual',ROOT/'.agents/skills/post-session-recap/references/session-manual/build_session_manual.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
recap='''# Keep the small words. Keep the meaning.

The gap becomes easier to see when you can say exactly what each claim means. A comparison is not an absolute verdict. A lower accident rate is not the same measure as less serious injury. Keep those distinctions alive while you read.

## Step zero: one claim at a time

Read a manageable piece. Look away and say it in your own words. Keep the group, the comparison, and the strength of the claim. Then connect it to the next piece.

If your retelling is only about the topic, go back to what was actually claimed. A sentence about two groups is not just about health or safety. It says something specific about those groups.

## Better than something does not automatically mean good

<div class="kinds"><article class="kind describe"><span class="bar"></span><h3 class="name">Relative</h3><p class="what">The green route is quicker than the blue route.</p><div class="test"><b>What you know</b>One route takes less time than the other. You do not yet know whether either is quick.</div></article><article class="kind object"><span class="bar"></span><h3 class="name">Absolute</h3><p class="what">The green route is quick.</p><div class="test"><b>What you need</b>A standard or enough further information to judge its actual journey time.</div></article></div>

If the blue route takes four hours and the green route takes three, the comparison is true. The green route can still be slow. The comparison alone does not settle the absolute judgment.

This does not mean comparisons can never help. If you also know a clear cutoff and where the routes fall against it, you may have enough information. The problem is the unsupported step, not the existence of a comparison.

You identified the healthier-versus-healthy distinction after we separated the claims. That is the detail to preserve when you tell an argument back.

## An association does not tell you the cause

Suppose cafés with longer opening hours sell more coffee. That describes an association. Longer hours might increase sales. High demand might lead a café to stay open longer. A busy location might affect both.

Keep these possibilities separate from what you are told. A correlation alone does not identify a causal direction. A causal claim such as the new machine reduced waiting time says that something affected something else; it does not automatically claim that it was the only cause.

You correctly refused to pick a causal direction from the accident statistics alone. Keep that restraint even when a question pushes you to explain why.

## Match the measure before accepting the conclusion

Suppose two delivery services are compared. One damages fewer parcels, but its damaged parcels tend to suffer much more serious damage. The other damages more parcels, usually with small scratches. Which is safer for your goods?

We cannot decide from the counts alone. We need to know how the relevant harms compare. Frequency and severity both concern risk, but they are different measures.

<div class="callout"><span class="tag">Preserve the exact wording</span>No safer means not safer. It allows equal safety or worse safety. Do not quietly change it into exactly equally safe.</div>

In the same way, body weight and body fat are different measures. A change in one is not automatically the same change in the other.

## A flaw answer needs two checks

First, does it accurately describe the argument? Point to the claim or inference it describes. Second, does it identify a real problem for that conclusion?

An answer can mention another cause or missing information without exposing the actual flaw. It may even give the author more support. Ask which direction the answer points before accepting it.

Do not reject an accurate objection merely because it was not the one you predicted. The answer can help you notice a distinction you missed on the first reading. Return to the stimulus and verify it.

## Say it before you reveal it

<details><summary>One laptop is lighter than another. Does that prove it is light?</summary><p>No. Both could be heavy. You know their relative weights, not whether either meets an absolute standard for lightness.</p></details>

<details><summary>A service makes fewer mistakes. Must its mistakes cause less harm overall?</summary><p>No. You need to know more about the seriousness and effects of those mistakes. Frequency alone does not settle overall harm.</p></details>

<details><summary>A flaw choice describes something true about the argument. Is that enough?</summary><p>No. It must also expose a genuine reasoning problem. A true description such as the author discusses two groups does not by itself identify a flaw.</p></details>

## When two answers remain

1. Say the exact conclusion.
2. State its supporting evidence separately.
3. Check every part of each answer against the argument.
4. Ask why the described issue harms the reasoning.

During untimed review, keep working until you can explain the choice. That is the purpose of our deliberate-answer rule. It is not a rule to leave timed-test questions blank while seeking certainty.

## Your next practice

Use Read, Recall, Colour for a full section, starting with PT103 Section 1. Read the accompanying primer before you begin. Preserve the details in each claim, then recall the whole argument in your own words.

The matching guided follow-up is Relative vs. Absolute. Use the comparison check above on each relevant question. After a few days with the recall exercise, send me your thoughts about which details you are now keeping and which still slip away.
'''
primer='''# Read, recall, then say the whole argument

Use this before Read, Recall, Colour · PT103 Section 1. The habit is to keep the meaning of every claim while changing the wording.

## Follow the current activity

1. Read about a sentence silently. If that is too much, take a shorter piece.
2. Look away and tell it back out loud in your own words.
3. React to that content out loud. A question or example is enough. Keep the reaction separate from what the author actually said.
4. Continue through the stimulus. The text remains visible while you do this; deliberately look away to recall.
5. When you have worked through the whole stimulus, press Space. The text disappears. Retell the whole argument from memory with the details you can retain.
6. Press Space again to continue. You cannot go back to an earlier stimulus.

## Check the small words

Lighter than is not light. Less likely is not impossible. No safer is not necessarily equally safe. Keep those meanings in your retelling.

Your wording and order can differ from the original. What matters is that the claims, details and relationships remain. The whole section records in one take; use the activity's pause control when needed.

## What to notice afterwards

Can you say both the evidence and the conclusion? Did a comparison become an absolute claim in your retelling? Did two different measures become one? Send Joshua your thoughts after using the exercise for a few days.

The current activity hides the text for the final whole-stimulus recall, rather than hiding it after each sentence. Follow the on-screen routine.
'''
ref='''# Check a flaw answer against the argument

A flaw answer must describe the reasoning accurately and identify a genuine problem. Keep both requirements in view.

## Get the argument clear first

Identify the conclusion and its reasons. Retell each claim in your own words without dropping comparisons, quantities, conditions or uncertainty. Accept the premises for the task; test whether they support the conclusion.

The conclusion need not repeat the premises. Valid reasoning can draw a new conclusion from them. The question is whether that conclusion is supported, not whether it uses new words.

## Name the unsupported step

| What the evidence gives | What needs checking |
|---|---|
| One thing is better than another | Does that comparison alone prove it is good? |
| Two features occur together | Is a causal direction being assumed without support? |
| A cause contributed to an outcome | Has it been treated as required or as the only possible cause? |
| A lower frequency of harm | Has the seriousness of harm been ignored in the broader judgment? |
| A result on one measure | Does the conclusion switch to a different measure? |

These are checks, not automatic verdicts. Additional evidence may justify the inference. Explain what the specific argument leaves open.

## Verify the description

Map the answer's claims to the stimulus. If it says the author assumes every member has a property, find where that universal assumption is needed. Some, most and all are different. If it alleges a comparison, identify the actual groups being compared.

Do not accept a familiar flaw label unless its description fits this argument. Do not reject a valid description merely because its wording differs from your prediction.

## Verify the objection

Ask why the described issue makes the conclusion less well supported. A statement may be true of the argument without being a flaw. A missing fact might be irrelevant. A proposed possibility might help the conclusion rather than challenge it.

In a relative-to-absolute argument, keep the comparison true and imagine both items below the absolute standard. That shows why the comparison alone is insufficient. You do not have to prove the conclusion is false in the real world.

## Finish with a reason

In untimed review, explain why your choice fits and why the closest alternative fails. Under a timed test, follow your pacing plan and choose the best-supported answer available. The review habit is justification, not a demand for impossible certainty.
'''
for name,body in [('primer-recall.md',primer),('flaw-reference.md',ref)]: (folder/name).write_text(body,encoding='utf8')
parts=re.split(r'^## (.+)$',recap,flags=re.M);first=parts[0].split('\n',1)[1].strip();sections=''.join('<section><div class="wrap"><h2>'+h+'</h2>'+markdown.markdown(b,extensions=['tables'])+'</div></section>' for h,b in zip(parts[1::2],parts[2::2]))
extra='details{margin:16px 0;border:1px solid var(--line);border-radius:10px;background:white}summary{cursor:pointer;padding:16px;font-weight:600}details p{padding:0 16px}summary:focus-visible{outline:3px solid #28594d}body{overflow-wrap:break-word}.kicker{color:#785b16}@media(max-width:600px){.kinds{grid-template-columns:1fr}}'
src='<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="lsatu-interactive-lesson" content="whit-2026-10-19-claim-precision"><title>Keep the small words · Session recap</title><style>/*CSS*/'+extra+'</style></head><body><header class="hero"><div class="wrap"><div class="kicker">Session recap · October 19</div><h1>Keep the small words.<br>Keep the meaning.</h1><p class="lede">'+first+'</p></div></header>'+sections+'<footer class="footer-note"><div class="wrap"><span class="mark">LSAT U</span></div></footer></body></html>'
(folder/'recap.src.html').write_text(src,encoding='utf8');(folder/'recap.html').write_text(src.replace('/*CSS*/',m.CSS),encoding='utf8')
for name,kicker,marker in [('primer-recall.md','Before you start · Read, Recall, Colour','whit-2026-10-19-recall-primer'),('flaw-reference.md','Reference · Keep it open while you drill','whit-flaw-answer-reference')]:
 out=m.from_md(str(folder/name),kicker,marker);(folder/name.replace('.md','.html')).write_text(out,encoding='utf8');m.lint(name,out)
private='''
<!-- PRIVATE CONTINUATION: not student-facing -->

## Source map and commitments | 2026-10-25

Full transcript read: ../sessions/2026-10-19-claim-precision-and-rephrasing/transcript.md. Identity whitwilson929@gmail.com. Fresh live Classroom lookup 2026-10-25 returned zeroitems: intake complete does not mean homework/notes delivered. No posted method reference found for this account.

| Teaching / promise | Timestamp | Status |
|---|---|---|
| Translation, close choices, harder questions requested | 00:02:49 | Student goals |
| Rephrasing drill offered | 00:09:23 to 00:10:28; 00:33:10 | Joshua promise |
| Association versus cause | 00:12:25 to 00:14:21; 00:42:55 to 00:44:41 | Credit correct refusal to infer direction |
| Relative versus absolute | 00:20:03 to 00:31:14 | Credit afterdiscussion; correct overly broad never rule to comparisonalone |
| Deliberate answer justifications | 00:47:38 to 00:48:59; 01:02:09 | Apply untimedreview, not blanktimedtest rule |
| Frequency versus seriousness; two-part flawcheck | 00:56:00 to 01:02:52 | Main teaching |
| Assign spoken full-section recall/rephrase and provide materials | 01:02:52 to 01:05:12; 01:19:35 to 01:20:22 | Joshua promise, pendingdelivery |
| Use exercise for a fewdays; sendexperiencefeedback | 01:19:35 to 01:20:22 | Student task, no exactduestated |
| Completecourse / selectnextfocus | Gemini actionitems only | Specificcourse notconfirmed in spoken transcript; do not invent courseassignment |
| Confirm separateworkspace/accommodations byemail | 01:12:59 to 01:18:41 | Studentfollowup, approval/rulesunverified; noemailauthorized |

Proposed resource PT103 Section1 Read, Recall, Colour IDd17ba306-e3b6-4b21-b26a-1708b75d3b15; Relative vs.Absolute w8-05-relative-vs-absolute native7 beginner1to3 snapshoteligible13. Assistant-proposed matching guidedfollowup, not transcript-namedset. Parent must preflight.

Current app read-recall-colour-section.instructions.json checked: sentencepractice uses deliberate lookaway; Space hides for finalwholeargumentrecall, secondSpace advances. Transcript described hidepereachclaim; primer follows actualcurrentroutine without falsely claiming exactimplementationparity. Do not promise gradingquality or actualstudentcompletion.

Fresh neutral examples routecomparison/cafés/delivery/laptop authoredfortransfer. Do not restate transcript claims about cheating, nationality, remoteavailability, fixeddeadlines or schooladmissions as verifiedadvice. No externalrules researchdone. Preserve no-safer meaning, comparisonalone qualification, no universal restatementofpremises rule, and no forcedtimedcertainty. Draft only; nopost/assignperformed.
'''
target=ROOT/'students/whit-wilson/recaps/2026-10-19-recap.md';target.parent.mkdir(exist_ok=True)
if target.exists():raise RuntimeError('Preserve existingrecap')
target.write_text('---\ntitle: Whitney · Claim precision\nstudent: whit-wilson\nsession_date: 2026-10-19\nstatus: draft\nposted: false\n---\n\n'+recap+private,encoding='utf8');m.lint('recap.html',src)
