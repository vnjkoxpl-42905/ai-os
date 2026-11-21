"""Read safe account metadata with the existing central Stripe credential."""
import json
from pathlib import Path
import sys
import urllib.error
import urllib.request


def main():
    root = Path(__file__).resolve().parents[2]
    values = {}
    for line in (root / '.env').read_text(encoding='utf-8').splitlines():
        if line.strip() and not line.lstrip().startswith('#') and '=' in line:
            name, value = line.split('=', 1)
            values[name.strip()] = value.strip().strip('"').strip("'")
    key = values.get('STRIPE_SECRET_KEY')
    if not key:
        print('Stripe account read failed: existing credential unavailable', file=sys.stderr)
        return 1
    request = urllib.request.Request('https://api.stripe.com/v1/account',
                                    headers={'Authorization': 'Bearer ' + key})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            account = json.load(response)
        if not account.get('id', '').startswith('acct_'):
            raise ValueError('Unexpected account response')
    except urllib.error.HTTPError as error:
        print(f'Stripe account read failed: HTTP {error.code}', file=sys.stderr)
        return 1
    except Exception as error:
        print(f'Stripe account read failed: {type(error).__name__}', file=sys.stderr)
        return 1
    print(json.dumps({
        'status': 'verified_read',
        'account_id': account['id'],
        'display_name': account.get('settings', {}).get('dashboard', {}).get('display_name'),
        'business_name': account.get('business_profile', {}).get('name'),
        'country': account.get('country'),
        'key_mode': 'live' if key.startswith(('sk_live_', 'rk_live_')) else 'test_or_unknown',
    }, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
