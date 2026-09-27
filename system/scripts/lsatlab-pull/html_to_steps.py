"""Convert LSAT Lab explanation HTML (from /api/questions/<id>) into LSAT U's
stored format: Argument Breakdown steps [{label, body}] and Choice Note bodies.
Markdown conventions match what the ingest wrote: **bold**, *italic*,
blank line between paragraphs, single newline for <br>.

Emphasis is emitted only at the outermost level (bold inside italic stays
plain inside the italic span), never spans a line break, and whitespace always
sits outside the markers, so "<i>fewer </i>meals" becomes "*fewer* meals".
"""
import html as H, re
from html.parser import HTMLParser

BOLD = {'b', 'strong'}; ITAL = {'i', 'em'}

class _MD(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.lines = [[]]          # list of lines; each line is a list of (text, mark)
        self.stack = []            # open emphasis tags
    def mark(self):
        for t in self.stack:
            return '**' if t in BOLD else '*'
        return ''
    def newline(self, n=1):
        for _ in range(n): self.lines.append([])
    def handle_starttag(self, tag, attrs):
        if tag in BOLD or tag in ITAL: self.stack.append(tag)
        elif tag == 'br': self.newline()
        elif tag == 'li': self.lines[-1].append(('- ', ''))
        elif tag in ('iframe', 'script', 'style'): self.stack.append('#skip')
    def handle_endtag(self, tag):
        if tag in BOLD or tag in ITAL or tag in ('iframe', 'script', 'style'):
            want = '#skip' if tag in ('iframe', 'script', 'style') else None
            for i in range(len(self.stack) - 1, -1, -1):
                if (want and self.stack[i] == want) or (not want and (self.stack[i] in BOLD) == (tag in BOLD) and self.stack[i] != '#skip'):
                    del self.stack[i]; break
        elif tag == 'p': self.newline(2)
        elif tag in ('li', 'ul', 'ol', 'div', 'h5', 'h4', 'h3'): self.newline()
    def handle_data(self, data):
        if '#skip' in self.stack: return
        data = data.replace('\xa0', ' ').replace('\r', '')
        parts = data.split('\n')
        for i, p in enumerate(parts):
            if i: self.newline()
            if p: self.lines[-1].append((p, self.mark()))

def _render_line(chunks):
    # merge adjacent chunks with the same mark, then wrap each run
    runs = []
    for text, m in chunks:
        # touching runs with different emphasis (italic straight into bold) would
        # render as "***"; fold them into the earlier run's emphasis instead
        if runs and (runs[-1][1] == m or (m and runs[-1][1] and not runs[-1][0][-1:].isspace() and not text[:1].isspace())):
            runs[-1][0] += text
        else: runs.append([text, m])
    out = ''
    for text, m in runs:
        if not m or not text.strip():
            out += text; continue
        lead = text[:len(text) - len(text.lstrip())]; trail = text[len(text.rstrip()):]
        core = text.strip()
        # a closing marker glued to a following word needs a space (only if the source had one)
        out += lead + m + core + m + trail
    return re.sub(r'[ \t]{2,}', ' ', out).strip()

def _inline(html):
    p = _MD(); p.feed(html or ''); p.close()
    s = '\n'.join(_render_line(l) for l in p.lines)
    s = re.sub(r'\n{3,}', '\n\n', s)
    return s.strip()

def steps(general_feedback):
    """<h5>Label</h5> ... blocks -> [{'label', 'body'}]."""
    parts = re.split(r'<h5[^>]*>(.*?)</h5>', general_feedback or '', flags=re.S | re.I)
    out = []
    lead = _inline(parts[0])
    if lead: out.append({'label': 'Explanation', 'body': lead})
    for i in range(1, len(parts), 2):
        label = re.sub(r'\s+', ' ', H.unescape(re.sub(r'<[^>]+>', '', parts[i])).replace('\xa0', ' ')).strip()
        body = _inline(parts[i + 1] if i + 1 < len(parts) else '')
        if label or body: out.append({'label': label or 'Explanation', 'body': body})
    return out

def note(feedback):
    """Choice feedback -> (tag, body). The first <h5> is the choice's tag."""
    fb = feedback or ''
    m = re.match(r'\s*<h5[^>]*>(.*?)</h5>', fb, flags=re.S | re.I)
    tag = None
    if m:
        tag = re.sub(r'\s+', ' ', H.unescape(re.sub(r'<[^>]+>', '', m[1])).replace('\xa0', ' ')).strip() or None
        fb = fb[m.end():]
    fb = re.sub(r'<h5[^>]*>(.*?)</h5>', lambda x: '<p><b>' + x[1] + '</b></p>', fb, flags=re.S | re.I)
    return tag, _inline(fb)
