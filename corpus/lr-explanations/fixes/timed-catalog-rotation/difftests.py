import json, collections, sys
def fails(p):
    d = json.load(open(p, encoding='utf-8')); s = set()
    for t in d['testResults']:
        n = t['name'].replace(chr(92), '/').split('src/', 1)[-1]
        for a in t['assertionResults']:
            if a['status'] == 'failed': s.add(n + ' :: ' + a['fullName'])
        if t['status'] == 'failed' and not any(a['status'] == 'failed' for a in t['assertionResults']): s.add(n + ' :: <file failed to load>')
    return s, d['numFailedTests']
m, mn = fails(sys.argv[1]); b, bn = fails(sys.argv[2])
print('base failed', mn, '| branch failed', bn)
print('NEW on branch:', len(b - m), collections.Counter(x.split(' :: ')[0] for x in b - m))
print('fixed on branch:', len(m - b), collections.Counter(x.split(' :: ')[0] for x in m - b))
