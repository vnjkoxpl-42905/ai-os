"""Read-only client for the LSAT U backend (Lovable Cloud, project atrcqxpmqrynmtvvyjju).

Lovable Cloud is a managed Supabase stack, so the ordinary Supabase public APIs
apply: authenticate as admin against /auth/v1, then query PostgREST with that
JWT. RLS grants admin broad access via has_role(auth.uid(),'admin').

This is the DATA path. Schema changes (DDL) are Lovable-UI-only and go through
the `lovable-migrate` skill instead. See connections.md.

Credentials, never hardcoded:
  LSATPREP_ADMIN_EMAIL / LSATPREP_ADMIN_PASSWORD   root .env
  VITE_SUPABASE_URL / VITE_SUPABASE_PUBLISHABLE_KEY  projects/lsatu/.env

Everything here raises BackendUnavailable rather than exiting, so callers can
degrade to local-only output instead of dying when offline or uncredentialed.

Usage:
    from lsatu_api import client, BackendUnavailable
    try:
        c = client()
        passes = c.get("booking_passes", select="booking_slug,student_email,status")
    except BackendUnavailable as e:
        ...  # fall back to local data, and SAY the data is local
"""
import json
import os
import re
import ssl
import urllib.error
import urllib.parse
import urllib.request


def _ssl_context():
    """TLS context with a CA bundle that actually exists on this machine.

    The stock python.org build ships no CA store, so urllib fails with
    CERTIFICATE_VERIFY_FAILED on hosts curl handles fine. Prefer certifi, then
    the common system bundle locations. Verification is never disabled: this
    client authenticates with real admin credentials, so an unverified channel
    is not an acceptable fallback.
    """
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        pass
    for path in ("/etc/ssl/cert.pem",
                 "/usr/local/etc/openssl@3/cert.pem",
                 "/opt/homebrew/etc/openssl@3/cert.pem",
                 "/etc/pki/tls/certs/ca-bundle.crt"):
        if os.path.exists(path):
            return ssl.create_default_context(cafile=path)
    return ssl.create_default_context()

from pathlib import Path

BRAIN = str(Path(__file__).resolve().parents[2])
ROOT_ENV = os.path.join(BRAIN, ".env")
APP_ENV = os.path.join(BRAIN, "projects", "lsatu", ".env")
EXPECTED_REF = "atrcqxpmqrynmtvvyjju"  # never resolve this project by name


class BackendUnavailable(Exception):
    """Raised when the backend cannot be reached or credentials are missing."""


def _read_env(path):
    out = {}
    if not os.path.isfile(path):
        return out
    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            m = re.match(r'^(?:export\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.*)$', line)
            if m:
                out[m.group(1)] = m.group(2).strip().strip('"').strip("'")
    return out


class Client:
    def __init__(self, url, anon_key, token):
        self.url = url.rstrip("/")
        self.anon_key = anon_key
        self.token = token

    def get(self, table, select="*", timeout=30, **filters):
        """GET a PostgREST table. Extra kwargs become query params (e.g. order='id')."""
        params = {"select": select}
        params.update({k: str(v) for k, v in filters.items()})
        q = urllib.parse.urlencode(params, safe="*,.()")
        req = urllib.request.Request(
            f"{self.url}/rest/v1/{table}?{q}",
            headers={"apikey": self.anon_key,
                     "Authorization": f"Bearer {self.token}",
                     "Accept": "application/json"},
        )
        try:
            with urllib.request.urlopen(req, timeout=timeout, context=_ssl_context()) as r:
                body = json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            raise BackendUnavailable(f"{table}: HTTP {e.code} {e.read()[:200]!r}") from e
        except Exception as e:
            raise BackendUnavailable(f"{table}: {e}") from e
        if isinstance(body, dict) and "message" in body:
            # PostgREST reports SQL errors as 200-with-body in some configurations
            raise BackendUnavailable(f"{table}: {body.get('message')}")
        return body


def client(timeout=30):
    """Authenticate as admin and return a Client. Raises BackendUnavailable."""
    root = _read_env(ROOT_ENV)
    app = _read_env(APP_ENV)
    email = os.environ.get("LSATPREP_ADMIN_EMAIL") or root.get("LSATPREP_ADMIN_EMAIL")
    password = os.environ.get("LSATPREP_ADMIN_PASSWORD") or root.get("LSATPREP_ADMIN_PASSWORD")
    url = app.get("VITE_SUPABASE_URL")
    anon = app.get("VITE_SUPABASE_PUBLISHABLE_KEY")

    missing = [n for n, v in (("LSATPREP_ADMIN_EMAIL", email),
                              ("LSATPREP_ADMIN_PASSWORD", password),
                              ("VITE_SUPABASE_URL", url),
                              ("VITE_SUPABASE_PUBLISHABLE_KEY", anon)) if not v]
    if missing:
        raise BackendUnavailable("missing credentials: " + ", ".join(missing))

    if EXPECTED_REF not in url:
        # Guard against the wrong-project trap documented in connections.md:
        # a different Supabase project is also named "LSATU".
        raise BackendUnavailable(
            f"refusing to use {url}: expected project ref {EXPECTED_REF}")

    payload = json.dumps({"email": email, "password": password}).encode()
    req = urllib.request.Request(
        f"{url.rstrip('/')}/auth/v1/token?grant_type=password",
        data=payload,
        headers={"apikey": anon, "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=_ssl_context()) as r:
            tok = json.loads(r.read().decode()).get("access_token")
    except Exception as e:
        raise BackendUnavailable(f"admin auth failed: {e}") from e
    if not tok:
        raise BackendUnavailable("admin auth returned no access_token")
    return Client(url, anon, tok)
