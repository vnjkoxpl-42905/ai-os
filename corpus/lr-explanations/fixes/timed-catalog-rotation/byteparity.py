import subprocess, glob, sys, os
os.chdir(sys.argv[1])
pats = sys.argv[2:] or ['public/data/PT*-S*-LR.json']
bad = []; crlf = 0; n = 0
for p in pats:
    for f in sorted(glob.glob(p, recursive=True)):
        f = f.replace(os.sep, '/'); n += 1
        wt = open(f, 'rb').read()
        st = subprocess.run(['git', 'show', ':' + f], capture_output=True).stdout
        crlf += b'\r\n' in wt
        if wt != st: bad.append(f)
print('files', n, 'mismatches', len(bad), bad[:8], 'crlf', crlf)
