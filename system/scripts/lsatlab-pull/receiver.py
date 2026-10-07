"""Local receiver for bulk LSAT Lab pulls.

The logged-in LSAT Lab tab fetches data with its own session and POSTs it here,
so large pulls never pass through the browser tool's output. Listens on
127.0.0.1 only; accepts POSTs from https://app.lsatlab.com only.

Usage: python receiver.py [port]     (default 8765; run in the background)
Each POST body is written to data/received/<name>.json, where <name> comes
from the ?name= query parameter (letters, digits, dash, underscore only).
"""
import json, os, re, sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'data', 'received')
ORIGIN = 'https://app.lsatlab.com'

class H(BaseHTTPRequestHandler):
    def _cors(self):
        if self.headers.get('Origin') == ORIGIN:
            self.send_header('Access-Control-Allow-Origin', ORIGIN)
            self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.send_header('Access-Control-Allow-Private-Network', 'true')

    def do_OPTIONS(self):
        self.send_response(204); self._cors(); self.end_headers()

    def do_POST(self):
        if self.headers.get('Origin') != ORIGIN:
            self.send_response(403); self.end_headers(); return
        name = parse_qs(urlparse(self.path).query).get('name', ['pull'])[0]
        if not re.fullmatch(r'[A-Za-z0-9_-]{1,80}', name):
            self.send_response(400); self._cors(); self.end_headers(); return
        body = self.rfile.read(int(self.headers.get('Content-Length', 0)))
        json.loads(body)  # reject anything that is not JSON
        os.makedirs(OUT, exist_ok=True)
        open(os.path.join(OUT, name + '.json'), 'wb').write(body)
        self.send_response(200); self._cors(); self.end_headers(); self.wfile.write(b'ok')
        print('received', name, len(body), 'bytes', flush=True)

    def log_message(self, *a): pass

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    print('listening on 127.0.0.1:%d' % port, flush=True)
    ThreadingHTTPServer(('127.0.0.1', port), H).serve_forever()
