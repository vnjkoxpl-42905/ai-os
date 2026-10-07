"""Final type verdict per slot: manual overrides > stem classifier > agreed label.

Writes verdict.json (every slot) and prints the bank and DB change lists."""
import json, collections

R = json.load(open('classified.json', encoding='utf-8'))

PC, PS, MSS, MBT, MBF = 'Principle-Conform', 'Principle-Strengthen', 'Most Strongly Supported', 'Must Be True', 'Must Be False'
SA, NA, ST, WK, FL = 'Sufficient Assumption', 'Necessary Assumption', 'Strengthen', 'Weaken', 'Flaw'
MR, RO, PF, PR, PX, AD = 'Method of Reasoning', 'Role', 'Parallel Flaw', 'Parallel Reasoning', 'Paradox', 'Agree/Disagree'

# Reviewed by hand against the full stem (and stimulus/choices where the stem was open-ended).
OVR = {
    # none-class rows where bank and DB disagree
    'PT114-S1-Q10': WK, 'PT125-S4-Q10': WK, 'PT126-S3-Q4': WK, 'PT139-S4-Q15': WK, 'PT134-S2-Q9': WK, 'PT156-S4-Q1': WK,
    'PT130-S4-Q12': MR, 'PT138-S4-Q15': FL, 'PT142-S4-Q8': FL,
    # agreed labels the stem plainly contradicts, or the app's synonym table rules on
    'PT102-S2-Q8': PC, 'PT103-S2-Q2': PC, 'PT117-S2-Q17': PC, 'PT121-S1-Q11': PC, 'PT125-S2-Q8': PC, 'PT129-S2-Q10': PC,
    'PT130-S1-Q4': PC, 'PT133-S2-Q5': PC, 'PT133-S3-Q3': PC, 'PT143-S4-Q1': PC, 'PT157-S2-Q6': PC, 'PT134-S3-Q18': PC,
    'PT120-S1-Q7': PC, 'PT129-S3-Q14': PC,
    'PT109-S4-Q15': PS, 'PT139-S1-Q10': MSS, 'PT139-S4-Q2': MSS, 'PT156-S2-Q15': PF, 'PT156-S2-Q16': PX,
    'PT156-S2-Q23': SA, 'PT156-S4-Q13': SA, 'PT144-S2-Q8': MR, 'PT102-S2-Q24': NA,
    # three-way
    'PT104-S1-Q4': WK, 'PT105-S2-Q5': PS, 'PT109-S1-Q16': PC, 'PT109-S3-Q2': FL, 'PT109-S3-Q6': PS, 'PT110-S3-Q12': FL,
    'PT110-S3-Q16': PS, 'PT111-S3-Q19': PC, 'PT115-S2-Q7': NA, 'PT116-S2-Q9': FL, 'PT125-S2-Q24': ST, 'PT126-S3-Q6': PC,
    'PT127-S2-Q20': NA, 'PT129-S3-Q16': PC, 'PT132-S2-Q3': ST, 'PT132-S2-Q18': PC, 'PT132-S4-Q8': MSS, 'PT134-S1-Q17': SA,
    'PT135-S4-Q15': ST, 'PT140-S3-Q6': PS, 'PT140-S3-Q9': PS, 'PT142-S2-Q17': MR, 'PT142-S4-Q12': PS, 'PT142-S4-Q21': PC,
    'PT142-S4-Q23': MBT, 'PT143-S3-Q12': PS, 'PT144-S2-Q14': PS, 'PT144-S3-Q6': PC, 'PT144-S3-Q23': PS, 'PT144-S4-Q9': PC,
    'PT146-S1-Q16': ST, 'PT146-S1-Q24': NA, 'PT147-S1-Q12': ST, 'PT147-S1-Q20': MBF, 'PT147-S4-Q5': FL, 'PT148-S3-Q17': MSS,
    'PT149-S3-Q17': PC, 'PT150-S3-Q10': ST, 'PT150-S3-Q19': WK, 'PT152-S1-Q12': ST, 'PT152-S4-Q8': PC, 'PT154-S2-Q7': PS,
    'PT155-S1-Q4': AD, 'PT155-S2-Q25': PC, 'PT157-S2-Q19': MBT, 'PT158-S4-Q4': FL, 'PT158-S4-Q5': PR, 'PT158-S4-Q21': PS,
    # classifier misfires inside the bank_wrong / db_wrong lists
    'PT112-S4-Q15': SA, 'PT118-S4-Q25': PS, 'PT121-S1-Q16': PS, 'PT149-S4-Q17': WK, 'PT153-S2-Q10': PX,
    'PT109-S3-Q9': ST, 'PT133-S3-Q14': FL, 'PT142-S2-Q23': PF, 'PT143-S1-Q22': PF, 'PT151-S2-Q7': ST,
    'PT155-S1-Q21': PC, 'PT141-S4-Q23': PC,
}

out = []
for r in R:
    s = r['slot']
    if s in OVR:
        v, src = OVR[s], 'manual'
    elif r['k'] in ('all_agree', 'bank_wrong', 'db_wrong'):
        v, src = r['st'], 'stem'
    else:  # none / both_disagree_stem with no override: keep the agreed label
        if r['app'] != r['dbCanon']:
            raise SystemExit(f'unreviewed disagreement {s}: {r["app"]} vs {r["dbCanon"]}')
        v, src = r['app'], 'agreed'
    r['verdict'], r['src'] = v, src
    out.append(r)

json.dump(out, open('verdict.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
bank = [r for r in out if r['app'] != r['verdict']]
db = [r for r in out if r['dbCanon'] != r['verdict'] or (r['dbRaw'] != r['verdict'])]
dbsem = [r for r in out if r['dbCanon'] != r['verdict']]
print('slots', len(out), '| bank changes (student-visible type)', len(bank), '| DB type wrong', len(dbsem), '| DB raw string not canonical', len(db))
print(collections.Counter(r['src'] for r in out))
