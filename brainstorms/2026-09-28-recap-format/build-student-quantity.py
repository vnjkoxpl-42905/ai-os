"""Package the interactive quantity lesson for LSAT U's protected Classroom view."""

from pathlib import Path
import base64
import html as html_escape
import re
import shutil


here = Path(__file__).resolve().parent
target = here.parents[1] / "projects" / "lsatu" / "public" / "quantity-statements"
target.mkdir(parents=True, exist_ok=True)
assets = target / "assets"
assets.mkdir(exist_ok=True)

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

source = source.replace(
    '../../projects/lsatu/src/components/classroom/classroom.css',
    '/quantity-statements/classroom.css',
)
source = source.replace('./assets/', '/quantity-statements/assets/')
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

(target / "index.html").write_text(source, encoding="utf-8")
classroom_css = (
    here.parents[1] / "projects" / "lsatu" / "src" / "components" / "classroom" / "classroom.css"
).read_text(encoding="utf-8")
shutil.copyfile(
    here.parents[1] / "projects" / "lsatu" / "src" / "components" / "classroom" / "classroom.css",
    target / "classroom.css",
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
    shutil.copyfile(here / "assets" / name, assets / name)

embedded = source.replace(
    '<link href="/quantity-statements/classroom.css" rel="stylesheet">',
    f"<style>{classroom_css}</style>",
    1,
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
        f'/quantity-statements/assets/{name}',
        f'data:image/svg+xml;base64,{encoded}',
    )
if '/quantity-statements/assets/' in embedded:
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

print(target / "index.html")
print(f"{output} ({output.stat().st_size} bytes)")
