"""Package the interactive quantity lesson for LSAT U's protected Classroom view."""

from pathlib import Path
import base64
import html as html_escape
import re
from urllib.request import Request, urlopen


here = Path(__file__).resolve().parent
source = (here / "08-quantity-statements-visual-preview.html").read_text(encoding="utf-8")
source, removed = re.subn(
    r'<aside class="classroom-sidebar">.*?</aside>\s*',
    "",
    source,
    count=1,
    flags=re.DOTALL,
)
if removed != 1:
    raise RuntimeError("Expected one mock Classroom sidebar")

source = re.sub(
    r'<div class="classroom-detail-actions"><button[^>]*disabled>Ask</button><button[^>]*disabled>Back to notes</button></div>',
    '',
    source,
    count=1,
)
source = source.replace(
    '</head>',
    '''<style>
      .classroom-root { display: block; }
      .classroom-root .classroom-stage { width: 100%; min-height: 100dvh; }
      .classroom-root .classroom-column { width: min(100%, 1100px); margin: 0 auto; }
      @media (max-width: 680px) {
        .classroom-root .classroom-stage { padding-left: 16px; padding-right: 16px; }
      }
    </style></head>''',
    1,
)

classroom_css = (
    here.parents[1] / "projects" / "lsatu" / "src" / "components" / "classroom" / "classroom.css"
).read_text(encoding="utf-8")
embedded = source.replace(
    '<link href="../../projects/lsatu/src/components/classroom/classroom.css" rel="stylesheet">',
    f"<style>{classroom_css}</style>",
    1,
)
# Google Fonts is a runtime dependency inside the student's opaque-origin
# iframe. Keep the Latin faces the lesson uses inside the HTML instead.
font_url = re.search(r'<link href="(https://fonts\.googleapis\.com/[^"]+)" rel="stylesheet">', embedded)
if not font_url:
    raise RuntimeError("Expected the lesson font stylesheet")
request = Request(font_url.group(1).replace('&amp;', '&'), headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
})
font_css = urlopen(request, timeout=20).read().decode('utf-8')
latin_faces = re.findall(r'/\* latin \*/\s*(@font-face\s*\{.*?\})', font_css, flags=re.DOTALL)
if len(latin_faces) < 3:
    raise RuntimeError("Could not package the lesson fonts")
unique_faces = {}
for face in latin_faces:
    url = re.search(r'url\((https://[^)]+)\)', face).group(1)
    weight = int(re.search(r'font-weight:\s*(\d+)', face).group(1))
    if url not in unique_faces:
        unique_faces[url] = [face, []]
    unique_faces[url][1].append(weight)
font_css = '\n'.join(
    re.sub(r'font-weight:\s*\d+;',
           f'font-weight: {min(weights)} {max(weights)};' if len(weights) > 1 else f'font-weight: {weights[0]};',
           face, count=1)
    for face, weights in unique_faces.values()
)
for url in set(re.findall(r'url\((https://[^)]+)\)', font_css)):
    encoded = base64.b64encode(urlopen(url, timeout=20).read()).decode('ascii')
    font_css = font_css.replace(url, f'data:font/woff2;base64,{encoded}')
embedded = re.sub(r'<link rel="preconnect" href="https://fonts\.googleapis\.com">\s*', '', embedded)
embedded = re.sub(r'<link rel="preconnect" href="https://fonts\.gstatic\.com" crossorigin>\s*', '', embedded)
embedded = embedded.replace(font_url.group(0), f'<style>{font_css}</style>')
# The shared Classroom stylesheet includes this unrelated hub component. It
# is absent from the lesson, so remove its unreachable image declarations.
embedded = re.sub(r'background-image: url\("/mainhub/hub-horizon\.png"\);', 'background-image: none;', embedded)
embedded = re.sub(
    r'background-image: image-set\(\s*url\("/mainhub/hub-horizon\.webp"\) type\("image/webp"\),\s*url\("/mainhub/hub-horizon\.png"\) type\("image/png"\)\s*\);',
    'background-image: none;', embedded,
)
embedded = embedded.replace(
    '<head>',
    '<head><meta name="lsatu-interactive-lesson" content="some-most-all">',
    1,
)
for name in (
    "some-books.svg",
    "most-books.svg",
    "all-books.svg",
    "book-quantity-ranges.svg",
    "some-all-witness.svg",
    "all-and-overlap.svg",
    "group-size-comparison.svg",
    "some-some-gap.svg",
):
    encoded = base64.b64encode((here / "assets" / name).read_bytes()).decode("ascii")
    embedded = embedded.replace(
        f'./assets/{name}',
        f'data:image/svg+xml;base64,{encoded}',
    )
if './assets/' in embedded:
    raise RuntimeError("An image was not inlined")
output = here / "10-quantity-statements-student.html"
output.write_text(embedded, encoding="utf-8")
if output.stat().st_size > 500000:
    raise RuntimeError("The classroom note exceeds the MCP post size limit")

iframe_preview = here / "11-quantity-statements-sandbox-check.html"
iframe_preview.write_text(
    '<!doctype html><meta charset="utf-8"><title>Sandbox check</title>'
    '<iframe title="Interactive lesson" sandbox="allow-scripts allow-forms" '
    'style="display:block;width:100%;height:100dvh;border:0" srcdoc="'
    + html_escape.escape(embedded, quote=True)
    + '"></iframe>',
    encoding="utf-8",
)

print(f"{output} ({output.stat().st_size} bytes)")
