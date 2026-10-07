"""Authenticated portable credential package; encryption key never enters Git."""
from __future__ import annotations
import argparse, base64, getpass, hashlib, json, os, secrets, stat, zlib
from pathlib import Path, PurePosixPath

FORMAT = b'AIOS-CREDENTIALS-V1\n'
COMPRESSED_FORMAT = b'AIOS-CREDENTIALS-V2-ZLIB\n'
MULTIPART_FORMAT = b'AIOS-CREDENTIALS-MULTIPART-V1\n'
MAX_CHUNK_BYTES = 50 * 1024 * 1024
MAX_DECOMPRESSED_BYTES = 2 * 1024 * 1024 * 1024
FORBIDDEN_NAMES = {'cookies', 'cookies.sqlite', 'login data', 'web data', 'local state', 'state.vscdb', 'keyring', 'keychain'}

def _aes():
    try:
        from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    except ImportError as exc:
        raise RuntimeError('cryptography is required for credential encryption') from exc
    return AESGCM

def _link(path):
    return path.is_symlink() or bool(getattr(path.lstat(), 'st_file_attributes', 0) & 0x400)

def _reject_link_chain(path):
    """Check lexical ancestors before resolve can hide a linked directory."""
    path = Path(os.path.abspath(path))
    for candidate in [path, *path.parents]:
        if candidate.is_symlink() or (candidate.exists() and _link(candidate)):
            raise ValueError('Credential path cannot traverse a link')
    return path

def _safe_name(name):
    path = PurePosixPath(name)
    if not name or '\\' in name or ':' in name or path.is_absolute() or '..' in path.parts or '.' in path.parts or path.as_posix() != name:
        raise ValueError('Unsafe credential output path')
    return path

def collect(sources):
    files = {}
    for source in sources:
        path = _reject_link_chain(Path(os.path.expandvars(source['path'])).expanduser())
        label = str(_safe_name(source['label']))
        if not path.exists(): raise RuntimeError('Configured credential source is unavailable')
        if _link(path): raise RuntimeError('Credential sources may not be links')
        candidates = [path] if path.is_file() else sorted(path.rglob('*'))
        for candidate in candidates:
            if _link(candidate): raise RuntimeError('Credential source contains a link')
            if not candidate.is_file(): continue
            if candidate.name.lower() in FORBIDDEN_NAMES or candidate.suffix.lower() in {'.sqlite', '.sqlite3', '.db', '.keychain'}:
                raise RuntimeError('Native browser and keyring state is not portable')
            relative = label if path.is_file() else label + '/' + candidate.relative_to(path).as_posix()
            _safe_name(relative)
            if relative in files: raise RuntimeError('Duplicate credential destination')
            files[relative] = base64.b64encode(candidate.read_bytes()).decode('ascii')
    return files

def local_key(state):
    state = _reject_link_chain(state); state.mkdir(parents=True, exist_ok=True)
    if _link(state): raise RuntimeError('Credential state directory cannot be a link')
    path = state / 'secrets.key'
    if path.exists() and _link(path): raise RuntimeError('Credential key cannot be a link')
    try:
        descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    except FileExistsError:
        key = path.read_bytes()
    else:
        key = secrets.token_bytes(32)
        with os.fdopen(descriptor, 'wb') as handle: handle.write(key)
    if len(key) != 32: raise RuntimeError('Local credential key has invalid length')
    if os.name != 'nt': path.chmod(stat.S_IRUSR | stat.S_IWUSR)
    return key

def bundle(sources, state, destination, package_name='credentials', visible_originals=None, key_state=None):
    """Return nonsecret metadata and reuse ciphertext if input contents are unchanged."""
    if not sources and not visible_originals: return {'enabled': False, 'file_count': 0}
    if package_name not in {'credentials', 'redacted-context'}: raise ValueError('Unsupported credential package name')
    files = collect(sources) if sources else {}
    if visible_originals:
        for name, content in visible_originals.items():
            _safe_name(name)
            if PurePosixPath(name).suffix.lower() == '.jsonl': raise ValueError('Raw session JSONL cannot enter context package')
            content.decode('utf-8')
            files[name] = base64.b64encode(content).decode('ascii')
    plaintext = json.dumps({'version': 1, 'files': files}, sort_keys=True, separators=(',', ':')).encode()
    state = Path(state); state.mkdir(parents=True, exist_ok=True)
    cache = state / (package_name + '.enc')
    fingerprint_file = state / (package_name + '.fingerprint')
    key = local_key(key_state or state)
    format_marker = COMPRESSED_FORMAT if visible_originals else FORMAT
    fingerprint = hashlib.sha256(format_marker + key + plaintext).hexdigest()
    if not cache.exists() or not fingerprint_file.exists() or fingerprint_file.read_text() != fingerprint:
        nonce = secrets.token_bytes(12)
        payload = zlib.compress(plaintext, level=6) if visible_originals else plaintext
        ciphertext = format_marker + nonce + _aes()(key).encrypt(nonce, payload, format_marker)
        temporary = cache.with_suffix('.tmp')
        temporary.write_bytes(ciphertext); os.replace(temporary, cache)
        fingerprint_file.write_text(fingerprint)
    ciphertext = cache.read_bytes()
    destination = Path(destination); destination.mkdir(parents=True, exist_ok=True)
    package_path = destination / (package_name + '.enc')
    parts = []
    if len(ciphertext) > MAX_CHUNK_BYTES:
        for position in range(0, len(ciphertext), MAX_CHUNK_BYTES):
            block = ciphertext[position:position + MAX_CHUNK_BYTES]
            name = package_path.name + '.part' + str(len(parts) + 1).zfill(4)
            (destination / name).write_bytes(block)
            parts.append({'file': name, 'bytes': len(block), 'sha256': hashlib.sha256(block).hexdigest()})
        descriptor = {'version': 1, 'ciphertext_bytes': len(ciphertext), 'ciphertext_sha256': hashlib.sha256(ciphertext).hexdigest(), 'parts': parts}
        package_path.write_bytes(MULTIPART_FORMAT + json.dumps(descriptor, sort_keys=True).encode('utf-8'))
    else:
        package_path.write_bytes(ciphertext)
    metadata = {'enabled': True, 'format': 2 if visible_originals else 1, 'file_count': len(files), 'paths': sorted(files), 'ciphertext_sha256': hashlib.sha256(ciphertext).hexdigest()}
    if parts: metadata['ciphertext_parts'] = parts
    manifest = 'manifest.json' if package_name == 'credentials' else package_name + '.manifest.json'
    (destination / manifest).write_text(json.dumps(metadata, indent=2) + '\n', encoding='utf-8')
    return metadata

def export_bundle(destination, config):
    sources = list(config.get('credential_sources', []))
    if config.get('auto_credential_sources'):
        existing = {str(Path(os.path.expandvars(item['path'])).expanduser().absolute()).lower() for item in sources}
        for item in discover_env_sources(config):
            if str(Path(item['path']).absolute()).lower() not in existing:
                sources.append(item)
                existing.add(str(Path(item['path']).absolute()).lower())
    state = Path(config['_state_dir']) / 'private'
    metadata = bundle(sources, state, destination)
    if metadata.get('enabled'):
        metadata['cloud_key_required'] = 'Provision AI_OS_SYNC_KEY privately in the cloud environment; the key is never uploaded.'
    return metadata

def discover_env_sources(config):
    roots = config.get('_allowed_roots', [config['ai_os']])
    pruned = {'.git', 'node_modules', '.venv', 'venv', '__pycache__', '.cache', '.next', '.nuxt', 'dist', 'raw', 'temp', 'tmp', 'scratch', '.firecrawl', '.cloud-sync'}
    results = []
    vault = Path(config['ai_os']).resolve()
    for root_name in roots:
        root = Path(root_name).resolve()
        label = 'ai-os' if root == vault else 'projects/' + root.name
        for directory, dirs, files in os.walk(root, followlinks=False):
            current = Path(directory)
            dirs[:] = [name for name in dirs if name.lower() not in pruned and not _link(current / name) and not ((current / name) / '.git').exists() and (current / name).relative_to(root).as_posix().lower() != 'setup/github-sync/state']
            for name in files:
                lower = name.lower()
                if not (lower == '.env' or lower.startswith('.env.')) or lower.endswith(('.example', '.template')): continue
                path = current / name
                if _link(path): continue
                results.append({'path': str(path), 'label': label + '/' + path.relative_to(root).as_posix()})
    return results

def decrypt(package, destination, key):
    package = _reject_link_chain(package)
    data = package.read_bytes()
    if data.startswith(MULTIPART_FORMAT):
        descriptor = json.loads(data[len(MULTIPART_FORMAT):])
        if descriptor.get('version') != 1: raise ValueError('Unsupported multipart format')
        blocks = []
        for position, item in enumerate(descriptor['parts'], 1):
            expected_name = package.name + '.part' + str(position).zfill(4)
            if item['file'] != expected_name or not (0 < item['bytes'] <= MAX_CHUNK_BYTES):
                raise ValueError('Invalid multipart chunk descriptor')
            path = _reject_link_chain(package.parent / item['file'])
            block = path.read_bytes()
            if len(block) != item['bytes'] or hashlib.sha256(block).hexdigest() != item['sha256']:
                raise ValueError('Encrypted chunk integrity check failed')
            blocks.append(block)
        data = b''.join(blocks)
        if len(data) != descriptor['ciphertext_bytes'] or hashlib.sha256(data).hexdigest() != descriptor['ciphertext_sha256']:
            raise ValueError('Multipart credential integrity check failed')
    marker = COMPRESSED_FORMAT if data.startswith(COMPRESSED_FORMAT) else FORMAT
    if len(key) != 32 or not data.startswith(marker): raise ValueError('Invalid credential package or key')
    nonce = data[len(marker):len(marker) + 12]
    try:
        plaintext = _aes()(key).decrypt(nonce, data[len(marker) + 12:], marker)
    except Exception as exc:
        raise ValueError('Credential authentication failed') from exc
    if marker == COMPRESSED_FORMAT:
        decoder = zlib.decompressobj()
        plaintext = decoder.decompress(plaintext, MAX_DECOMPRESSED_BYTES)
        if not decoder.eof or decoder.unconsumed_tail: raise ValueError('Context decompression limit exceeded')
    payload = json.loads(plaintext)
    if payload.get('version') != 1: raise ValueError('Unsupported credential format')
    destination = _reject_link_chain(destination).resolve()
    validated = []
    for name, value in payload['files'].items():
        path = destination.joinpath(*_safe_name(name).parts)
        for ancestor in [path, *path.parents]:
            if ancestor == destination.parent: break
            if ancestor.exists() and _link(ancestor): raise ValueError('Credential output cannot traverse a link')
        if path.exists(): raise ValueError('Credential output already exists; refusing overwrite')
        validated.append((path, base64.b64decode(value, validate=True)))
    for path, contents in validated:
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'xb') as handle: handle.write(contents)
        if os.name != 'nt': path.chmod(0o600)
    return {'file_count': len(validated)}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--decrypt', required=True)
    parser.add_argument('--destination', required=True)
    parser.add_argument('--key-file')
    args = parser.parse_args()
    if args.key_file: key = Path(args.key_file).read_bytes()
    else:
        encoded = os.environ.get('AI_OS_SYNC_KEY') or getpass.getpass('Credential package key (base64): ')
        try: key = base64.b64decode(encoded, validate=True)
        except ValueError: raise SystemExit('Invalid encoded key')
    print(json.dumps(decrypt(args.decrypt, args.destination, key)))

if __name__ == '__main__': main()
