# Claude conversation 27e1a8c2-cf49-4a60-a437-d9ec0e080db9-agent-acdb9fa0e7e4bfde7

## user

Read and follow exactly: C:/Users/Joshu/AppData/Local/Temp/claude/C--Users-Joshu-dev-ai-os/27e1a8c2-cf49-4a60-a437-d9ec0e080db9/scratchpad/s3/BRIEF3.md

Your list: C:/Users/Joshu/AppData/Local/Temp/claude/C--Users-Joshu-dev-ai-os/27e1a8c2-cf49-4a60-a437-d9ec0e080db9/scratchpad/s3/items-flaw.json
Output file: C:/Users/Joshu/AppData/Local/Temp/claude/C--Users-Joshu-dev-ai-os/27e1a8c2-cf49-4a60-a437-d9ec0e080db9/scratchpad/s3/out-flaw.jsonl
Your scratch directory: C:/Users/Joshu/AppData/Local/Temp/claude/C--Users-Joshu-dev-ai-os/27e1a8c2-cf49-4a60-a437-d9ec0e080db9/scratchpad/s3/work-flaw/

Do not write to any database or to any file outside the scratch area. Work through every question on the list; append each finished question to the output as you go so progress survives interruption. The checker must report 0 problems when you finish.

## user

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>

## assistant

Tool call: Read
{"file_path": "C:/Users/Joshu/AppData/Local/Temp/claude/C--Users-Joshu-dev-ai-os/27e1a8c2-cf49-4a60-a437-d9ec0e080db9/scratchpad/s3/BRIEF3.md"}

## user

Tool result:
1	# Step 3 brief: rewrite LR explanations rated "Revamp"
2	
3	You are rewriting LSAT U Logical Reasoning explanations that an earlier audit rated **Revamp**: they fail as teaching or contain an error. Students read these after answering a question. You do NOT write to any database. You produce a proposal file. A separate verifier checks every rewrite against the question before anything is applied, so correctness matters more than speed.
4	
5	## Read-only sources
6	Local mirror of the live database (fresh, 2026-10-08): `C:/Users/Joshu/dev/ai-os/system/scripts/lsatlab-pull/data/db/`
7	- `lr_questions.json`: id, qid (e.g. PT146-S3-Q1), stimulus, prompt (the stem), correct_choice, question_type
8	- `lr_answer_choices.json`: question_id, letter, choice_text, tag, is_correct
9	- `lr_explanations.json`: id, question_id, style (`standard`, `brief`, `another_way`, `single`)
10	- `lr_explanation_steps.json`: id, explanation_id, position, label, body (Argument Breakdown steps)
11	- `lr_explanation_choice_notes.json`: id, explanation_id, letter, body (Choice Notes)
12	
13	Question bank students actually read and are graded on: `C:/Users/Joshu/dev/ai-os-projects/lsatu/public/data/PT{n}-S{s}-LR.json` (questionNumber, stimulus, questionStem, answerChoices, correctAnswer). Where DB and bank wording differ, quote the bank. If the bank key and DB key disagree, do not rewrite: record a flag.
14	
15	Load JSON with Python (`python -I`), never by reading whole files into your context. Put helper scripts and scratch files in your own scratch directory (given below), not in the repo.
16	
17	House standard (read these first, they define "good"):
18	- `C:/Users/Joshu/dev/ai-os/corpus/lr-explanations/golden-set.md` (sections "What separates a top-tier explanation" and "Do not copy from the corpus")
19	- `C:/Users/Joshu/dev/ai-os/corpus/lr-explanations/golden-set-observations.md` sections 3, 5, 6
20	- The model file for your question family in `C:/Users/Joshu/dev/ai-os/corpus/lr-explanations/models/` (see `index.md` there)
21	- One finished example of the target shape: `C:/Users/Joshu/dev/ai-os/corpus/lr-explanations/drafts/batch-01-flaw-part-a.md`, item 1.
22	
23	## What to do for each question on your list
24	1. Read the stimulus, stem, all five choices, the key, and every existing style of the explanation (all steps and notes). The list gives the audit's "problem" note; treat it as a lead, not as truth.
25	2. Solve the question yourself first, from the stimulus. Confirm the key. If you cannot get to the credited answer, or think it is mis-keyed, write a `flag` and move on.
26	3. **The primary style** (`standard` if present, else `single`): rewrite it fully to the house standard.
27	   - Breakdown steps in the family's usual sequence (e.g. Conclusion, Evidence, Evaluate, Goal; or the family's equivalent from the model file). Short, concrete. The Evaluate/prediction step teaches the gap or the move before the choices are read.
28	   - Five choice notes. The correct note shows *why it works*, tied to its exact words and the stimulus. Each wrong note names the specific reason it fails (its own words vs. the stimulus), 1 to 3 sentences, not a bare label like "out of scope" or "this is a premise".
29	   - Quote the stimulus and choices exactly when you quote. Paraphrase only when clearly paraphrasing.
30	4. **Secondary styles** (`brief`, `another_way`, when present): keep their purpose (Brief is short; Another Way approaches from a different angle). Fix every error, remove every em dash, remove padding, make them consistent with the primary style's logic. Rewrite as much as needed. If a style currently has zero notes or zero steps, leave it at zero.
31	5. Do not change which answer is credited. Do not edit questions or answer choices.
32	
33	## Writing rules (hard)
34	- **No em dashes** (U+2014) anywhere in new text. No en dash used as a dash. Use a comma, colon, parentheses, or a new sentence.
35	- **No gendered pronouns** (he, she, him, her, his, hers, himself, herself). Use the name, "the author", "the speaker", "they".
36	- Never mention Logic Games (or "games"). Never claim anything about answer placement or how often a letter is right.
37	- No filler or slop: "Great question", "it's important to note", "delve", "key takeaway", "game-changer", "robust", "seamless", "unlock", "elevate". No mocking, no political asides, no outside facts the stimulus does not give.
38	- Plain, direct, confident sentences. Teach the reasoning; the reasoning is the product. Speak to the student as "you" where natural.
39	- Diagram chains go on their own line with `→`. Keep any markdown light (the app renders plain paragraphs; **bold** is fine sparingly).
40	
41	## Row rules (so the update is safe)
42	- You may change the body (and label, for steps) of every existing row. Keep every existing row: **never fewer steps than the style has now**, and the same note letters. You may ADD steps after the existing ones (new positions continue the sequence). If the old breakdown had more steps than you need, merge content so every existing position still holds a meaningful step.
43	- For each existing row include its `row_id` and the exact current text as `old_body` (and `old_label` for steps), copied from the mirror by script, not retyped.
44	
45	## Output
46	Write one JSON object per line (JSON Lines) to your output path:
47	```json
48	{"qid":"PT157-S2-Q12","key":"E","solve":"2-4 sentences: your own solution and why the key is right",
49	 "styles":[{"style":"standard","explanation_id":"<uuid>",
50	   "steps":[{"row_id":"<uuid or null for a new step>","position":0,"old_label":"...","old_body":"...","label":"Conclusion","body":"..."}],
51	   "notes":[{"row_id":"<uuid>","letter":"A","old_body":"...","body":"..."}]}],
52	 "changes":"one or two sentences: what was wrong before and what the rewrite fixes"}
53	```
54	Include every style the question has, with every one of its rows. For a question you will not rewrite: `{"qid":"...","flag":"reason"}`.
55	
56	Generate the file with a script that pulls `row_id`/`old_*` from the mirror and merges your written text, so nothing old is retyped by hand. Before finishing run the checker:
57	`python -I C:/Users/Joshu/AppData/Local/Temp/claude/C--Users-Joshu-dev-ai-os/27e1a8c2-cf49-4a60-a437-d9ec0e080db9/scratchpad/s3/check3.py <your output file>`
58	and fix everything it reports.
59	
60	## Self-check (required, per question)
61	After drafting, re-read each note next to its choice text and the stimulus, as if you were the verifier: every quote exact, every claim about a choice true of that choice's own words, the correct note actually proves the answer, no note contradicts the breakdown, no rule broken.
62	
63	When finished, reply with: number rewritten, number flagged with reasons, and anything you are unsure about.
64	

## assistant

Tool call: Bash
{"command": "cd C:/Users/Joshu/AppData/Local/Temp/claude/C--Users-Joshu-dev-ai-os/27e1a8c2-cf49-4a60-a437-d9ec0e080db9/scratchpad/s3; ls; python -I -c \"import json;d=json.load(open('items-flaw.json'));print(len(d));print(json.dumps(d[:2],indent=1)[:1500])\"; ls work-flaw 2>/dev/null; wc -l out-flaw.jsonl 2>/dev/null"}

## user

Tool result:
Exit code 1
BRIEF3.md
check2-ref.py
check3.py
inv.json
inv.py
items-agpar.json
items-flaw.json
items-mbt.json
items-mcrole.json
items-mss.json
items-na.json
items-prpl.json
items-str.json
items-weaken.json
t.jsonl
25
[
 {
  "qid": "PT134-S2-Q6",
  "type": "Flaw",
  "problem": "C note is a broken diagram; A, B, D are \"not relevant\"; C (the near-miss reversal of E) gets no real explanation.",
  "tags": "short-breakdown; verdict-only; thin-correct-note; thin-notes; no-prediction; very-short"
 },
 {
  "qid": "PT119-S2-Q24",
  "type": "Flaw",
  "problem": "Breakdown exists (em-dash heavy, different register) but all five choice notes are missing.",
  "tags": "no-notes; emdash-heavy; very-short"
 }
]

## assistant

Tool call: Bash
{"command": "cd C:/Users/Joshu/AppData/Local/Temp/claude/C--Users-Joshu-dev-ai-os/27e1a8c2-cf49-4a60-a437-d9ec0e080db9/scratchpad/s3; cat check3.py; mkdir -p work-flaw; python -I -c \"import json;[print(x['qid'],'|',x['problem']) for x in json.load(open('items-flaw.json'))]\""}

## user

Tool result:
"""Mechanical checks on a step 3 rewrite file (JSON Lines). Usage: check3.py <file.jsonl>"""
import json, sys, re, collections
DB = 'C:/Users/Joshu/dev/ai-os/system/scripts/lsatlab-pull/data/db/'
L = lambda n: json.load(open(DB + n, encoding='utf-8'))
Q = {q['qid']: q for q in L('lr_questions.json')}
E = collections.defaultdict(list)
for e in L('lr_explanations.json'): E[e['question_id']].append(e)
S = collections.defaultdict(list)
for s in L('lr_explanation_steps.json'): S[s['explanation_id']].append(s)
N = collections.defaultdict(list)
for n in L('lr_explanation_choice_notes.json'): N[n['explanation_id']].append(n)
CH = collections.defaultdict(list)
for c in L('lr_answer_choices.json'): CH[c['question_id']].append(c)
SRC = ''
GENDER = re.compile(r"\b(he|she|him|her|his|hers|himself|herself)\b", re.I)
BANNED = re.compile(r"logic games?|delve|game-changer|robust|seamless|unlock|elevate|great question|it's important to note|key takeaway", re.I)
probs = []; done = 0; flags = 0; seen = set()
def P(qid, msg): probs.append(f'{qid}: {msg}')
def text_ok(qid, where, t):
    if not t or not t.strip(): P(qid, f'{where} empty')
    if '\u2014' in t: P(qid, f'{where} em dash')
    if re.search(r'\s\u2013\s', t): P(qid, f'{where} en dash used as dash')
    for m in GENDER.finditer(t):
        # allowed only inside a quote of the question's own text
        ctx = t[max(0, m.start()-30):m.end()+30]
        if not any(seg and seg in SRC for seg in re.findall(r'["“]([^"”]+)["”]', ctx) ):
            P(qid, f'{where} gendered pronoun "{m.group(0)}" outside a quote'); break
    if BANNED.search(t): P(qid, f'{where} banned word "{BANNED.search(t).group(0)}"')
for ln, line in enumerate(open(sys.argv[1], encoding='utf-8'), 1):
    if not line.strip(): continue
    try: p = json.loads(line)
    except Exception as ex: probs.append(f'line {ln}: bad JSON {ex}'); continue
    qid = p.get('qid'); q = Q.get(qid)
    if q is None: P(qid, 'unknown qid'); continue
    SRC = (q['stimulus'] or '') + ' ' + (q['prompt'] or '') + ' ' + ' '.join(c['choice_text'] or '' for c in CH[q['id']])
    if qid in seen: P(qid, 'duplicate qid')
    seen.add(qid)
    if 'flag' in p: flags += 1; continue
    done += 1
    if p.get('key') != q['correct_choice']: P(qid, f"key {p.get('key')} != DB {q['correct_choice']}")
    exps = {e['id']: e for e in E[q['id']]}
    got = {s['explanation_id'] for s in p.get('styles', [])}
    if got != set(exps): P(qid, f'styles cover {len(got)} explanations, DB has {len(exps)}')
    for st in p.get('styles', []):
        eid = st['explanation_id']; e = exps.get(eid)
        if e is None: P(qid, f'explanation {eid} not on this question'); continue
        if st.get('style') != e['style']: P(qid, f'style label {st.get("style")} != {e["style"]}')
        old_steps = {s['id']: s for s in S[eid]}; old_notes = {n['id']: n for n in N[eid]}
        new_steps = st.get('steps', []); new_notes = st.get('notes', [])
        ids = [s.get('row_id') for s in new_steps if s.get('row_id')]
        if set(ids) != set(old_steps): P(qid, f'{e["style"]}: steps must include every existing step row ({len(old_steps)}), got {len(ids)}')
        positions = [s['position'] for s in new_steps]
        if positions != list(range(len(new_steps))): P(qid, f'{e["style"]}: positions not 0..n-1 in order: {positions}')
        for s in new_steps:
            rid = s.get('row_id')
            if rid:
                o = old_steps.get(rid)
                if o is None: continue
                if o['body'] != s.get('old_body') or o['label'] != s.get('old_label'): P(qid, f'{e["style"]} step {rid[:8]} old text != mirror')
                if o['position'] != s['position']: P(qid, f'{e["style"]} step {rid[:8]} position moved {o["position"]}->{s["position"]}')
            elif s['position'] < len(old_steps): P(qid, f'{e["style"]} new step at position {s["position"]} collides with existing')
            text_ok(qid, f'{e["style"]} step {s["position"]} body', s.get('body', ''))
            text_ok(qid, f'{e["style"]} step {s["position"]} label', s.get('label', ''))
        if {n.get('row_id') for n in new_notes} != set(old_notes): P(qid, f'{e["style"]}: notes must be exactly the existing note rows ({len(old_notes)})')
        for n in new_notes:
            o = old_notes.get(n.get('row_id'))
            if o is None: continue
            if o['body'] != n.get('old_body'): P(qid, f'{e["style"]} note {n.get("letter")} old text != mirror')
            if o['letter'] != n.get('letter'): P(qid, f'{e["style"]} note letter mismatch')
            text_ok(qid, f'{e["style"]} note {n.get("letter")}', n.get('body', ''))
print(f'rewritten {done}, flagged {flags}, problems {len(probs)}')
for x in probs: print('  ' + x)
PT134-S2-Q6 | C note is a broken diagram; A, B, D are "not relevant"; C (the near-miss reversal of E) gets no real explanation.
PT119-S2-Q24 | Breakdown exists (em-dash heavy, different register) but all five choice notes are missing.
PT123-S3-Q23 | Conclusion and Evaluate labels are fused into the Evidence step body; C note carries two "- paragraph" markup lines.
PT120-S1-Q23 | Breakdown only; all five choice notes missing.
PT102-S3-Q14 | Breakdown only; all five choice notes missing.
PT158-S4-Q4 | Explicit-Standard register (8.5 em-dashes per 1k words; wrong-answer notes average 125.2 words).
PT158-S4-Q18 | Correct; padded.
PT158-S4-Q23 | Notes right, but the breakdown never mentions the new garage, which is the whole answer.
PT157-S2-Q12 | Accurate, but every note is a 90-word em-dash paragraph restating "reverses the conditional".
PT158-S2-Q2 | Explicit-Standard register (7.7 em-dashes per 1k words; wrong-answer notes average 124.0 words).
PT158-S3-Q8 | Explicit-Standard register (6.8 em-dashes per 1k words; wrong-answer notes average 105.0 words).
PT158-S3-Q1 | Explicit-Standard register (10.2 em-dashes per 1k words; wrong-answer notes average 119.5 words).
PT158-S4-Q2 | Explicit-Standard register (8.5 em-dashes per 1k words; wrong-answer notes average 114.5 words).
PT157-S3-Q14 | Explicit-Standard register (8.5 em-dashes per 1k words; wrong-answer notes average 41.5 words).
PT157-S3-Q17 | Explicit-Standard register (14.7 em-dashes per 1k words; wrong-answer notes average 31.5 words).
PT158-S3-Q4 | Explicit-Standard register (3.2 em-dashes per 1k words; wrong-answer notes average 113.5 words).
PT158-S4-Q6 | Explicit-Standard register (7.2 em-dashes per 1k words; wrong-answer notes average 124.0 words).
PT157-S2-Q9 | Explicit-Standard register (8.4 em-dashes per 1k words; wrong-answer notes average 83.5 words).
PT157-S2-Q20 | Explicit-Standard register (6.3 em-dashes per 1k words; wrong-answer notes average 99.0 words).
PT157-S2-Q25 | Explicit-Standard register (6.9 em-dashes per 1k words; wrong-answer notes average 91.2 words).
PT157-S3-Q9 | Explicit-Standard register (7.8 em-dashes per 1k words; wrong-answer notes average 33.0 words).
PT157-S3-Q12 | Explicit-Standard register (11.8 em-dashes per 1k words; wrong-answer notes average 39.0 words).
PT158-S2-Q10 | Explicit-Standard register (7.9 em-dashes per 1k words; wrong-answer notes average 101.0 words).
PT158-S2-Q14 | Explicit-Standard register (6.1 em-dashes per 1k words; wrong-answer notes average 105.2 words).
PT158-S2-Q18 | A note argues against a claim A does not make. (Found in the 2026-09-26 survey; not re-read.)

## assistant

Now the house standard and example.

## assistant

Tool call: Bash
{"command": "cd C:/Users/Joshu/dev/ai-os/corpus/lr-explanations; ls models; cat models/index.md | head -40; grep -n \"^#\" golden-set.md | head -30"}

## assistant

Tool call: Bash
{"command": "cd C:/Users/Joshu/dev/ai-os/corpus/lr-explanations; cat models/flaw.md | head -150"}

## assistant

Tool call: Bash
{"command": "cd C:/Users/Joshu/dev/ai-os/corpus/lr-explanations; sed -n 1,80p drafts/batch-01-flaw-part-a.md"}

## user

Tool result:
---
type: draft
subject: First 20 remaining Flaw slots, batch 01 part A
status: draft, not loaded
created: 2026-09-28
---

# Flaw explanations: first 20 remaining slots

Source: current designated bank (`projects/lsatu-wt-glossary/public/data`) and fresh database dump (`system/scripts/lsatlab-pull/data/db`). Bank and database keys agree for all 20. PT102-S3-Q14 has existing breakdown steps, so this draft supplies only its five missing notes. All other slots supply breakdown and five notes. The quoted question and choices use bank wording, except PT102-S2-Q18 choice C uses the database wording confirmed in LSAT Lab on 2026-09-28. PT101-S3-Q2 choice B has a database typo (“its the cause” for “is the cause”) with no change in meaning. Model references are from the database; weaknesses noted in `models/Flaw.md` were not copied.

## 1. PT101-S3-Q2 · Flaw · Difficulty 1 · Answer E

*Modelled on PT150-S2-Q4 (comparison), PT107-S4-Q18 (test the abstract wording), and PT154-S2-Q12 (missing alternative).*

> Advertisement: Anyone who thinks moisturizers are not important for beautiful skin should consider what happens to the earth, the skin of the world, in times of drought. Without regular infusions of moisture the ground becomes lined and cracked and its lush loveliness fades away. Thus your skin, too, should be protected from the ravages caused by lack of moisture; give it the protection provided by regular infusions of Dewyfresh, the drought-defying moisturizer.
>
> The Dewyfresh advertisement exhibits which one of the following errors of reasoning?
>
> (A) It treats something that is necessary for bringing about a state of affairs as something that is sufficient to bring about that state of affairs.
> (B) It treats the fact that two things regularly occur together as proof that there is a single thing that is the cause of them both.
> (C) It overlooks the fact that changing what people think is the case does not necessarily change what is the case.
> (D) It relies on the ambiguity of the term “infusion,” which can designate either a process or the product of that process.
> (E) It relies on an analogy between two things that are insufficiently alike in the respects in which they would have to be alike for the conclusion to be supported.

### Argument Breakdown

**Conclusion (thus)** Skin should get regular Dewyfresh moisturizer to protect it from damage caused by lack of moisture.

**Evidence** Drought dries and cracks the earth, which the advertisement calls “the skin of the world.”

**Evaluate** Given that dry ground cracks, how could skin still behave differently? Soil and human skin are different materials. The ad needs the two to resemble each other in the very process it is comparing. The phrase “skin of the world” is a metaphor, not evidence that a moisturizer affects skin the way rain affects soil. Even if skin needs moisture, nothing here establishes that Dewyfresh provides the promised protection.

**Goal** Look for a criticism of an analogy between the earth and human skin that has not established the relevant similarity.

### Choice Notes

**(A) Wrong Flaw.** Necessary versus sufficient would require the ad to argue, for example, that because moisture is required for healthy skin, applying Dewyfresh guarantees beautiful skin. It does not make that formal move. Its evidence is the earth analogy.

**(B) Wrong Flaw.** A common cause would explain why two observed events happen together. The ad does not report two correlated events and infer a shared cause. It compares two different things.

**(C) Wrong Flaw.** The argument does not claim that changing beliefs changes physical reality. The opening addresses people who doubt moisturizers, but the evidence is about drought, not a change in what people believe.

**(D) Wrong Flaw.** “Infusion” is used to mean an input of moisture in both places. The conclusion does not switch from a process to its product. The questionable switch is from ground to human skin.

**(E) Correct.** Test the analogy's relevant feature. Dry soil cracks without water; does human skin respond to a moisturizer in the same way? The ad gives no reason to think so. Calling earth “skin” makes the analogy memorable but does not supply the biological similarity the conclusion needs.

## 2. PT102-S2-Q18 · Flaw · Difficulty 3 · Answer E

*Modelled on PT154-S2-Q12 (false choice), PT110-S2-Q11 (best versus only), and PT150-S2-Q4 (plans).*

> President of Central Supply Company: Profits are at an all-time low this fiscal year because of decreased demand for our products. If this situation continues, the company may have to declare bankruptcy. So it is important to prevent any further decrease in profits. Consequently, the only options are to reduce planned expansion or to eliminate some less profitable existing operations.
>
> Which one of the following most accurately describes a flaw in the company president's reasoning?
>
> (A) It presumes without giving justification that survival of the company has been a good thing.
> (B) It does not take into account that there are alternatives to declaring bankruptcy.
> (C) It presumes without giving justification that only decreased demand can ever be the cause of decreased profits.
> (D) It does not allow for the possibility that profits will decrease only slightly during the next fiscal year.
> (E) It does not take into account that there may be other ways to stop the decrease in profits.

### Argument Breakdown

**Conclusion (consequently)** The company's only options are to reduce planned expansion or eliminate some less profitable current operations.

**Evidence** Demand and profit have fallen. Continued decline may cause bankruptcy, so preventing further profit decline matters.

**Evaluate** Granted, the company needs to stop profits falling. Why must it choose one of those two cost cuts? It might increase revenue through a new product, revise prices, or find a third cost saving. The urgency of the goal does not prove an exhaustive list of ways to reach it. We need only one possible third way to challenge “only.”

**Goal** Find the missing alternatives to stopping profit decline, not merely alternatives to bankruptcy.

### Choice Notes

**(A) Bad Assumption.** Whether the company's survival is good does not show that the two listed measures exhaust its ways to prevent further loss.

**(B) Bad Description.** This sounds tempting because bankruptcy is mentioned. But the president's *only options* claim concerns stopping the decrease in profits. A way to survive after profits keep falling would not be a third way to stop that fall.

**(C) Bad Assumption.** The president says decreased demand explains this year's low profits, not that decreased demand is the *only possible cause* of decreased profits. Even if another factor could lower profits, that would not identify the flaw in the supposedly exhaustive list of two measures for preventing a further decline.

**(D) Not an Objection.** Even a slight further decrease is a decrease. Its size does not show that there is another option for preventing it.

## user

Tool result:
# Flaw: model picks

Read in full: all 40 shortlist candidates (shortlist-Flaw.md), plus golden-set-observations sections 3, 4, 6 and golden-set.md. Only one candidate was already golden: PT151-S2-Q3. I did not look beyond the shortlist, because it had more than 10 that deserve to be models.

**Picks: 20** (easy 6, medium 6, hard 8). Rubric order is P X E T C L, each scored 0 to 2, total out of 12.

The existing golden Flaw picks already cover some sub-patterns: slippery slope with abstract answers (PT151-S2-Q3), alternate explanation (PT102-S2-Q9), relative vs absolute (PT139-S4-Q18), an untriggered conditional (PT143-S3-Q18), opinion vs fact (PT118-S3-Q13) and a two-way Nec/Suff (PT142-S4-Q22). So these picks lean toward the flaws the golden set lacks: ad hominem, sampling, anti-causal, percent vs number, aggregate vs subgroup, unproven vs proven false, possible vs actual, best vs only, false choice, and the illegal-negation and illegal-reversal forms at low difficulty.

## 1. The picks

| # | Slot | Diff | Sub-pattern / features | Rubric /12 | What makes it a model | Weakness | Already golden? |
|---|---|---|---|---|---|---|---|
| 1 | PT134-S3-Q6 | 1 | Correlation to causation, third factor (common cause); "ignores the possibility" answers | 11 (P2 X2 E2 T2 C1 L2) | The Goal predicts both shapes: the formal "correlation is not causation" answer, and a named alternate explanation (reverse cause: dead fish feed algae; third factor: factory pollution). Every note runs "would it weaken?", and the correct note gives the reflex rule: "whenever an author looks at a correlation between X and Y ... two alternate explanations to reflexively consider." E is killed with a too-much/too-little sunlight example. | The Evaluate step is one dense paragraph and spends a sentence on what "must" means. | N |
| 2 | PT150-S2-Q4 | 1 | Comparison / analogy (scholars vs politicians); plan; different audience | 11 (P2 X2 E2 T2 C2 L1) | The Evaluate step teaches the comparison move with a parallel (marathon runners vs LSAT practice tests), then asks for "any salient difference". The B note gives a transferable rule: an objection never attacks the if-condition; you have to describe a world where the plan is carried out and still fails. C is rewritten into the version that would have worked ("suited to different audiences"). | The 91% key leaves no real trap to work on. The correct note is short. | N |
| 3 | PT113-S2-Q3 | 2 | Nec vs Suff, illegal negation; answers split by prefix | 12 (P2 X2 E2 T2 C2 L2) | Before the choices, the Evaluate step writes out both illegal moves (reversal and negation) for this rule, then says "that second thing is exactly what the argument did!" The Goal gives the formal phrasing and the conversational one ("doctor's note / extra credit"). The A note is the best prefix lesson in the set: A's content is exactly what the author assumes, so it would be right with "presumes" and is wrong with "ignores the possibility". D uses "X is bigger than Y = Y is smaller than X" to show a contrapositive is not a new idea. | None significant. | N |
| 4 | PT154-S1-Q12 | 2 | Ad hominem, "you do it too" version; rebuttal argument | 11 (P2 X2 E2 T2 C2 L1) | The Evaluate step lists the two rebuttal flaws (ad hominem, unproven vs proven false) and picks one by the conclusion's wording ("discounted", not "wrong"). The analogies are everyday: Timmy and the matches, and the DUI driver who is still right that you have had too much. The correct note offers two routes, recognizing the famous flaw or matching "X merely on the grounds that Y" piece by piece. | The popular choices are all under 5%, so no note has to handle a real trap. | N |
| 5 | PT147-S1-Q6 | 2 | Sampling (unrepresentative); two sampling answers | 11 (P2 X2 E2 T1 C1 L2) | E (12%) is a second sampling answer, and the note separates the two sampling complaints precisely. We are never told how many students or ads were used ("If 1,000 students were questioned ... we would not call that a very small number"), but a big sample of the wrong people is still unrepresentative. The nursing-home Christmas analogy shows why the source is the problem. | The Evaluate step is one long paragraph with a pun. The notes lean on famous-flaw definitions. | N |
| 6 | PT124-S2-Q11 | 2 | Nec vs Suff, illegal reversal; "fails to take into account that" stem; two conditionals that do not chain | 11 (P2 X2 E2 T2 C1 L2) | It diagrams both premises and explains why they do not chain ("high" standard of living vs "higher"), then finds the reversal in the conclusion. Every note runs one consistent test: "Saying X need not be Y is an objection to an author who said X must be Y," then asks whether this author said that. This is the right test for a stem that builds "fails to consider" into the question. | One chain line is garbled in transcription. B and E partly repeat each other. | N |
| 7 | PT141-S4-Q3 | 3 | Anti-causal ("X does not work"); groups not fair to compare | 12 (P2 X2 E2 T2 C2 L2) | The contact-lens analogy shows why equal outcomes can hide a working cause. The Goal says to "make an excuse for the evidence". The popular trap B (17%) gets the longest wrong-answer note and turns on one verb: "block" makes any case of cancer count against the sunscreen, so severity does not help. The correct note states the two anti-causal objections as a rule ("it would be even worse without X"; "these two groups aren't fair to compare"). | None significant. | N |
| 8 | PT148-S1-Q2 | 3 | Percent vs number (market share vs sales volume); math | 12 (P2 X2 E2 T2 C2 L2) | It argues with numbers before the choices: one table where the author is right (100 sold) and one where the author is wrong (200 sold). A third table in the correct note (120 sold, $300 vs $500) shows that even a modest change breaks "exactly half". D (13%) is refuted with price-and-cost arithmetic against the fixed net-income premise. B carries the recurring rule that asking for specific data "is never right on Flaw". | None significant. | N |
| 9 | PT151-S4-Q23 | 3 | Nec vs Suff, illegal reversal hidden by conclusion-first order and synonyms | 11 (P2 X2 E2 T2 C1 L2) | A lottery analogy ("Bob is wealthy, so he won the lottery") gives the conversational objection before the formal one. The Evaluate step names the two disguises: the conclusion comes first, and the words are not a verbatim match ("unhappy" for "not satisfied"). D is handled by negation, and E ("different kind of case") by pointing out the principle does apply; it was just run backward. | "The #1 famous flaw" preamble repeats. The C note is thin ("We don't have any such term here"). | N |
| 10 | PT120-S3-Q8 | 3 | Alternate explanation, base rate (the most common model gets stolen most) | 11 (P2 X2 E2 T2 C1 L2) | It predicts the base-rate explanation in the Evaluate step (the Honda Civic) and proves it with numbers in the correct note (1% of 1,000 Teslas vs 1% of 100,000 Civics). The C note is the lesson: resale value is still something about the model, so it supports the author's causal story instead of offering an alternative. B is killed with "a factor is not the only factor" (smoking example). | The three "fails to consider" notes share one opening sentence, word for word. | N |
| 11 | PT128-S3-Q14 | 3 | Correlation to causation ("more likely" language); third factor; reverse cause ruled out | 11 (P2 X2 E2 T2 C1 L2) | The Evaluate step teaches students to notice the language: "People who are A are more likely than those who aren't to be B" nearly guarantees a causal assumption. It rules reverse causation out on timing, so only third-factor explanations are left. The C trap (17%) gets the sharpest distinction in the Flaw set: "reduce" assumes plagiarism is *a* factor, and only "eliminate" would assume it is the *only* factor. The Tesla/hotel example finishes the correct note. | The Evaluate step is one paragraph. The C example uses suicide rates, which is heavier than it needs to be. | N |
| 12 | PT144-S3-Q15 | 3 | Aggregate vs subgroup (a majority overall hides a head-to-head loss); math | 10 (P2 X2 E1 T1 C2 L2) | The worked table (five groups of 20; Soda X wins 20-0 while Sparkle takes 52 of 100) makes an abstract answer concrete before the choices. The correct note walks the abstract wording piece by piece onto the table, and it says why predicting first matters on answers like this one. | C (18%, the top trap) gets one sentence. It is correct, but it does not say why the trap tempts. | N |
| 13 | PT154-S1-Q9 | 4 | Two conditionals: one used correctly (contrapositive), one negated illegally; intermediate conclusion | 12 (P2 X2 E2 T2 C2 L2) | It checks each step of the argument separately: the first move is "airtight", the second is an illegal negation, and the diagrams show both. A (24%) is explained as an answer that itself confuses necessary and sufficient, and it would only fit if the author had botched the *first* rule. The correct note teaches a reusable habit: diagram a conditional answer and check its contrapositive, "because correct answers are usually written in a contraposed form". C is rewritten into the answer that would have worked. | The parenthetical "(the only is sufficient)" is confusing. | N |
| 14 | PT101-S3-Q25 | 4 | Two-step argument; an upper limit is not a calculated value; "gives no reason for thinking" = assumption answer | 11 (P2 X2 E2 T2 C1 L2) | It runs "Given that ... does that prove that ..." on each step with a $50 trillion figure, and offers two targets. The sushi analogy ("doesn't want sushi, so she must know what she does want") and the antique-necklace analogy make the point stick. The D note teaches the less common assumption prefixes ("fails to establish / gives no reason for thinking"). | The E note is one line. The note that calls Circular "almost always wrong" drifts into advice about guessing. | N |
| 15 | PT110-S2-Q11 | 4 | Best way vs only way; refutation by false implication; abstract answers | 11 (P2 X2 E2 T2 C1 L2) | It shows the valid shell of the argument ("If X were right, A would follow; not A; so not X") and isolates the one shaky step. The analogy is an impossible "best way" to heal political division that does not mean there is no way. B (26%) gets the explanation it needs: supposing something for the sake of argument and then rejecting it is not a contradiction ("hypothetical claims" vs "actual claims"). | The correct note restates the chain three times before it lands. | N |
| 16 | PT155-S1-Q20 | 4 | Unproven vs proven false, modern version (a bad argument for X, so X is false); rebuttal of a rebuttal | 12 (P2 X2 E2 T2 C2 L2) | It names the spotting cue: "the author's conclusion is the complete opposite of the opponent's conclusion". It also explains how the flaw evolved, from "no one has proven X" on older tests to "someone made a bad argument for X" on newer ones. The C trap (13%) is handled precisely: Klemke committed the ad hominem, and "our author didn't commit this flaw." The correct note gives both routes (know the famous flaw, or match "concludes X on the grounds that Y"). | One political aside in the Goal ("dealings with Russia"). | N |
| 17 | PT107-S4-Q18 | 4 | Could be vs is (possible description taken as the true one); abstract answers | 11 (P2 X2 E2 T2 C2 L1) | When no famous flaw fits, it argues the anti-conclusion with a concrete case (holding a door open). The Goal's pencil/letter-opener line makes "could be described as" vs "is" clear. D (23%) is dismantled step by step: it sounds like Nec/Suff, so the note checks for a reversal or negation, finds neither, then runs the weaken test. | The D note's diagram is garbled ("Action appears → could be describe in altruistic terms"), and one sentence ends in a blank. | N |
| 18 | PT120-S3-Q23 | 5 | Anti-causal; "steadily advances" does not mean "not impeded"; past vs present comparison | 12 (P2 X2 E2 T2 C2 L2) | Its Goal gives two acceptable objections. The mold-spray analogy and the traffic line ("To impede the flow of traffic ≠ to STOP the flow of traffic") explain the key. E (23%) gets the most careful note in the set: "Pause after the first part of the answer to match up the abstract wording", then it shows the two halves cannot both be mapped. C (12%) gets a freckles argument that the answer *would* fit. | None significant. | N |
| 19 | PT120-S4-Q23 | 5 | Averages taken literally; plan compared with the status quo; extreme-assumption traps | 11 (P2 X2 E2 T2 C1 L2) | It does the headcount arithmetic (990 present now, 980 present after firing 10) that makes B click, and names the recurring LSAT move of reading "average" too literally. D is rewritten into the version that would weaken. E (19%) closes with a named trap rule: "Extreme Assumptions ... beware stuff that sounds more extreme than anything the author needed to assume." | The C note's diagram is wrong (see fidelity). | N |
| 20 | PT154-S2-Q12 | 4 | False choice / implausible alternative (defends the status quo against an extreme alternative) | 10 (P2 X2 E2 T1 C1 L2) | The lentil-soup exchange ("too hot" / "would you rather it had ice cubes?") shows the flaw exactly, and the Goal predicts the "middle ground" objection. A (22%) gets the longest note and says why it tempts ("That first verb is perfect") before showing that overzealous enforcement is a way of carrying out the practice, not a consequence of it. | It labels the flaw "Straw Man", then "False Choice"; neither matches the key's wording cleanly. The Evaluate step has a partisan aside (unemployment benefits "well below the poverty line"). The D note overclaims ("always wrong"). | N |

**Runners-up** (strong, left out for variety or a flaw noted below): PT122-S2-Q23 (d4, the rare *correct* Circular answer; the note says so outright; lost for the transcription fragment "(I even wrote )"). PT127-S1-Q20 (d4, attributes one group's outcome to a different plan; military-exercise analogy; honest "not perfect" note on the key). PT120-S3-Q16 (d3, alternate explanation; overlaps #10). PT148-S3-Q14 (d3, correlation to causation; overlaps #11, but its "overconfident wording" point in the correct note is worth borrowing). PT103-S2-Q21 (d5, absence-of-evidence version of unproven vs proven false; B at 37% is handled well; overlaps #16 and has two slips). PT151-S2-Q3 (golden; scores 10 here because its Goal admits it cannot narrow the objection, and the correct note uses a partisan slippery-slope example; the golden pick stands).

## 2. What the best Flaw explanations do

- **Build the objection in the Evaluate step, not just the label.** The best ones run "Given that ... how could we still argue that ..." and produce a concrete counter-story before the choices: the base-rate Civic (PT120-S3-Q8), and "990 present now, 980 after the firing" (PT120-S4-Q23). The famous-flaw label comes after the objection, not in place of it.
- **The Goal gives two acceptable shapes: formal and conversational.** "Look for the formal answer, saying this author scrambled a condition that is Sufficient ... Or look for the conversational answer saying, 'That's one possible reason'" (PT151-S4-Q23; also PT113-S2-Q3, PT154-S1-Q9). On causal arguments the two shapes are "infers causation from correlation" or "fails to consider [reverse cause / third factor]" (PT134-S3-Q6).
- **Each choice note runs the test its prefix calls for, and says so in the first line.** "Fails to consider / overlooks X" means ask whether X weakens. "Presumes / takes for granted X" means negate it and ask whether that weakens. "Concludes X on the grounds of Y" or "mistakes X for Y" means X must match the conclusion and Y the evidence (PT155-S1-Q20, PT148-S1-Q2). The strongest version shows that a choice's content can be right while its prefix makes it wrong (PT113-S2-Q3 A).
- **Do the arithmetic with small round numbers, in a table.** PT148-S1-Q2 uses three tables (100, 200, 120 sold). PT144-S3-Q15 uses five groups of 20. PT101-S3-Q25 uses "$50 trillion". PT121-S4-Q25 turns 75% of 60 problems into 45 and 15. Numbers are what make the abstract answers on math flaws legible.
- **One everyday analogy that has the same structure, placed where the student needs it.** Lottery winner (reversal, PT151-S4-Q23), contact lenses (anti-causal, PT141-S4-Q3), Timmy and the matches (ad hominem, PT154-S1-Q12), pencil as letter-opener (could be vs is, PT107-S4-Q18), traffic past a fender bender (impede vs stop, PT120-S3-Q23), lentil soup (false choice, PT154-S2-Q12).
- **The popular trap gets the longest wrong-answer note, and the note says why it tempts before saying why it fails.** "This one is very tempting. That first verb is perfect" (PT154-S2-Q12 A, 22%). "Pause after the first part of the answer" (PT120-S3-Q23 E, 23%). "This answer is itself making a Necessary vs. Sufficient error" (PT154-S1-Q9 A, 24%). Supposing something for the sake of argument is not a contradiction (PT110-S2-Q11 B, 26%).
- **Rewrite a wrong answer into the version that would have been right.** PT154-S1-Q9 C ("small populations or no populations of gnats ... in climates that are wet"), PT120-S4-Q23 D ("the workers most likely to be fired are way more productive"), PT150-S2-Q4 C ("suited to different audiences"). This shows the student exactly which word broke the answer.
- **State the recurring rules plainly, as rules.** Answers asking for a number, name or definition are never the flaw (PT148-S1-Q2 B, PT107-S4-Q18 C). "A factor" is not "the only factor"; "reduce" vs "eliminate" (PT128-S3-Q14 C, PT120-S3-Q8 B). Circular, Equivocation and Self-Contradiction show up often and are almost never right. Rebuttal arguments point to ad hominem or unproven vs proven false (PT154-S1-Q12, PT155-S1-Q20). There are two anti-causal objections: "even worse without it" and "groups not fair to compare" (PT141-S4-Q3).
- **Check each step on multi-step arguments.** Say which inference is sound and which is not, before predicting (PT154-S1-Q9 "This mini-argument seems airtight"; PT101-S3-Q25; PT110-S2-Q11 "we can really only complain about the move ... to her intermediate conclusion").
- **A conditional answer gets diagrammed, contrapositive included.** "Correct answers are usually written in a contraposed form of how we would recognize the argument" (PT154-S1-Q9 B). "A conditional and its contrapositive have the same meaning, just like 'X is bigger than Y' has the same meaning as 'Y is smaller than X'" (PT113-S2-Q3 D).

## 3. What the weaker candidates got wrong

- **Goals that give up on predicting.** "I would not know exactly what I'm looking for here" (PT117-S4-Q20). A two-part "is it true / is it a complaint" checklist instead of a target (PT121-S4-Q25). "It's pretty hard to limit our focus" (PT151-S2-Q3, golden). These cost P even when the notes are good.
- **The top trap gets a one-liner, or the same note as a minor choice.** PT122-S4-Q23 E (19%) gets one sentence. PT117-S4-Q20 C (21%) and E (16%) get two sentences each. PT113-S2-Q25 B (22%) says only that the idea "would strengthen". PT153-S3-Q19 spends its longest note on B (4%) and gives E (10%) a copy of the C note.
- **Pasted notes.** "This answer is almost always wrong" three times (PT106-S1-Q19 B, C, D). A and B share their reasoning word for word (PT117-S4-Q20). The C and E notes are identical (PT153-S3-Q19). The "Cool, yeah" author reply is reused (PT121-S4-Q25 A, C).
- **Imported facts or editorializing inside the reasoning.** Cars "get their best gas mileage" at 55 mph, used to build the objection that the key then rests on (PT114-S4-Q14). A long generational and climate aside in the correct note (PT113-S3-Q9). Partisan asides (PT154-S2-Q12 Evaluate, PT151-S2-Q3 D). A digression citing an outside RC passage (PT106-S1-Q19).
- **Wrong or mixed flaw labels.** "Unproven vs. Proven True" (PT147-S1-Q15). Straw Man and False Choice used for the same argument (PT154-S2-Q12). "Ad Hominem / Unproven vs. Proven False" named for what is really a source-of-belief (genetic) flaw (PT153-S3-Q19). In PT147-S1-Q15 the B note also describes the choice without rejecting it.

## 4. Fidelity problems found

- **PT146-S3-Q1 (A note):** reads the answer back as "quite unlikely to be unrepresentative". The choice says "quite likely to be unrepresentative". This inverts the key's own wording. (slip)
- **PT120-S4-Q23 (C note):** diagrams the answer as "if more than 10 absent → normal rate". C says the normal rate is reached *only when* no more than the average are absent, so the diagram should end "→ not normal rate". (slip; picked anyway, and the note should be corrected before anyone copies it)
- **PT113-S2-Q25 (B note):** "Since this answer starts with fails to consider / ignores the possibility". B actually starts "denies the possibility". The prefix-driven test is applied to a prefix the choice does not have. (misdescribes the choice)
- **PT111-S1-Q17 (Evidence step):** "under the ice sheet covering central America". The stimulus says central Antarctica. (slip)
- **PT103-S2-Q21:** the A note says "The prosecution isn't arguing ...", but the speaker is Ziegler's attorney (the defense). The Evaluate step has a garbled sentence ("what is the evidence he was that we was insane"). (slip)
- **PT122-S2-Q23 (Evaluate):** a truncated parenthetical, "(I even wrote )". (transcription)
- **PT138-S3-Q16 (Evidence step):** the conditional is scrambled across columns ("If people believe that important problems can then people be addressed only by → become large numbers of ppl unenthusiastic ..."). It cannot be read. (transcription)
- **PT124-S2-Q11 (Evaluate):** the chain line "major invest → high S.O.L → maintain in impr Inf. funct. Inf" is garbled. (transcription, minor)
- **PT107-S4-Q18 (D note):** the diagram "Action appears → could be describe in altruistic terms of self-interest" puts "altruistic" on the wrong side, and "it must be true that ." ends in a blank. (transcription)
- **PT147-S1-Q15 (Evaluate):** "Unproven vs. Proven True" should be "Proven False". (slip)
- **PT154-S1-Q9 (Evaluate):** "Only / only if are necessary indicators (the only is sufficient)" is a confusing parenthetical. (minor slip)
- **PT138-S2-Q24 (A note):** "Any time on LSAT that we see 'If [conclusion] ...', it will be wrong" is an overbroad rule stated as fact. The C note puts a sample answer labeled "A)" inside the C note. (register / slip)
- **PT154-S2-Q12 (D note):** "this formulation of the Causal flaw answer is always wrong" is an overclaim. (register)

No candidate had a correct-answer note arguing for the wrong key. There was no mocking of the question at the "hot garbage" level. The worst tone is PT113-S3-Q9's aside in the correct note.

## user

Tool result:
Flaw.md
MBT-MBF.md
MC-Role-Agree.md
NA.md
Paradox-Method.md
Parallel.md
Principle.md
Strengthen-SA.md
Weaken-Evaluate.md
index.md
---
type: teaching-notes
subject: LR explanation model library, 10 to 20 top-tier models per question type
updated: 2026-09-27
---

# LR explanation model library

334 existing explanations from the LSAT U database, picked as models for writing the missing ones. The [[../golden-set|golden set]] (51) is the short list of the very best; this library is the deep bench, 10 to 20 per question type, spread across difficulty and across each type's sub-patterns (each famous flaw on Flaw, conditional vs story-style on Parallel, and so on). Most picks are new; golden picks that turned up are marked.

**How it was built.** `system/scripts/lr-explanations/score_corpus.py` scored all 3,640 complete explanations (Evaluate depth, a Goal that names the answer, verdict-only notes, explicit tests, examples, stated rules, correct-answer note length, whether the most popular trap got the most attention; penalties for the em-dash register and for mocking the question). The top 25 to 40 per type were then read in full, every choice note checked against the printed answer text, and scored on the golden-set rubric (P prediction, X precision, E eliminations, T transfer, C clarity, L learner value; /12). Reading was split across 9 parallel readers; each file is one reader's judgment, so treat 11 vs 12 as a tie.

**How to use it.** When writing a missing explanation, find its type here, read the 2 or 3 picks that share its sub-pattern, and follow the "What the best ones do" section for that type. `system/scripts/lr-explanations/neighbors.py` finds the closest picks by features and stimulus shape; `show.py SLOT` prints one in full. Joshua's cram sheet and LR guideline PDFs (paths in [[../golden-set]]) name the moves and traps.

| Type | Models | File | Notes |
|---|---|---|---|
| Flaw | 20 | [[Flaw]] | Leans on flaws the golden set lacks: ad hominem, sampling, anti-causal, percent vs number, aggregate vs subgroup, best vs only, false choice |
| Must Be True / Most Supported | 20 | [[MBT-MBF]] | Conditional chains, Most + conditional, weighted averages, pivots, logical completion |
| Must Be False | 17 | [[MBT-MBF]] | Only 8 are truly top-tier; the type has 42 complete explanations in total |
| Necessary Assumption | 20 | [[NA]] | EXCEPT is thin: one usable model (PT103-S2-Q22, 8/12) |
| Sufficient Assumption | 20 | [[Strengthen-SA]] | Includes PT129-S2-Q7, a clean Refute-a-Conditional model the golden set lacked |
| Strengthen | 20 | [[Strengthen-SA]] | Plausibility boosters, ruled-out alternatives, plans, EXCEPT |
| Weaken | 20 | [[Weaken-Evaluate]] | Third factor, reverse cause, base rate, analogies, term shifts, EXCEPT |
| Evaluate | 17 | [[Weaken-Evaluate]] | About 12 are true models; the type has 25 complete explanations |
| Paradox | 20 | [[Paradox-Method]] | Difference-makers, math, plan-didn't-work, EXCEPT |
| Method | 20 | [[Paradox-Method]] | Includes three Method on Plans / Recommendations models the golden set lacked |
| Principle-Strengthen | 20 | [[Principle]] | Principles in answers and in the stimulus, weighing tradeoffs |
| Principle-Conform | 20 | [[Principle]] | Stimulus principles as checklists, implicit principles as slogans |
| Main Conclusion | 20 | [[MC-Role-Agree]] | Only 5 are difficulty 1-2; more easy models would need a second search |
| Role | 20 | [[MC-Role-Agree]] | Concessions, opposing views, intermediate-conclusion chains |
| Agree / Disagree | 20 | [[MC-Role-Agree]] | Explicit and assumption-level clashes, EXCEPT, Agree stems |
| Parallel | 20 | [[Parallel]] | No difficulty-1 pick besides the golden PT154-S1-Q10 |
| Parallel Flaw | 20 | [[Parallel]] | Each famous flaw; no clean Unproven vs Proven False model |

**Do not copy from a pick without reading its Weakness column.** Several picks carry a slip, a political example or a flattened diagram that has to be fixed in the new writing, not reproduced. Every defect found, picked or not, is in [[../fixes/model-library-defects]].

**Recurring moves across all types** (each file has the type-specific version):
- The Evaluate step argues with the argument before the choices ("Given that ... how could we argue ..."), with worked numbers or one everyday analogy.
- The Goal names the answer's content, often in two acceptable shapes (formal and conversational, or linking and defender).
- Each choice note runs the test its type or wording calls for, and says so in the first line.
8:# LR golden set: the 51 explanations new ones are modelled on
17:## What separates a top-tier explanation from a loose one
29:## Do not copy from the corpus
37:## The set
95:## Where the set is thin
