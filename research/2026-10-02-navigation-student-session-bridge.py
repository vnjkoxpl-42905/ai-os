"""One-request loopback bridge for the authorized app's administrator QA session.

Secrets are read from existing env stores, held in memory, and never printed.
Accepts only the local app origin; does not write student records.
"""
import json
from pathlib import Path
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.request import Request, urlopen


def env(path):
    values = {}
    for line in Path(path).read_text(encoding='utf-8').splitlines():
        if '=' not in line or line.lstrip().startswith('#'):
            continue
        key, value = line.split('=', 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


private = env('C:/Users/Joshu/dev/ai-os/.env')
public = env('C:/Users/Joshu/dev/lsatu-week-settings-180/.env')
key = public.get('VITE_SUPABASE_PUBLISHABLE_KEY') or public.get('VITE_SUPABASE_ANON_KEY')
req = Request(public['VITE_SUPABASE_URL'] + '/auth/v1/token?grant_type=password',
              data=json.dumps({'email': private['LSATPREP_TESTER_EMAIL'],
                               'password': private['LSATPREP_TESTER_PASSWORD']}).encode(),
              headers={'Content-Type': 'application/json', 'apikey': key}, method='POST')
with urlopen(req, timeout=30) as response:
    session = response.read()
private = None


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *_):
        pass

    def do_GET(self):
        if self.path != '/session' or self.headers.get('Origin') != 'http://127.0.0.1:8168':
            self.send_error(403)
            return
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', 'http://127.0.0.1:8168')
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(session)


with HTTPServer(('127.0.0.1', 8184), Handler) as server:
    server.timeout = 120
    print('One-request local QA session bridge ready.', flush=True)
    server.handle_request()
session = None
