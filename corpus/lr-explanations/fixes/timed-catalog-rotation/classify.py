import json, collections
from stemtype import stem_type
R = json.load(open('sweep.json', encoding='utf-8'))
for r in R: r['st'] = stem_type(r['stem'])
c = collections.Counter()
for r in R:
    a, d, t = r['app'], r['dbCanon'], r['st']
    if t is None: k = 'none'
    elif a == d == t: k = 'all_agree'
    elif a == t: k = 'db_wrong'
    elif d == t: k = 'bank_wrong'
    elif a == d: k = 'both_disagree_stem'
    else: k = 'three_way'
    r['k'] = k; c[k] += 1
print(c)
json.dump(R, open('classified.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
