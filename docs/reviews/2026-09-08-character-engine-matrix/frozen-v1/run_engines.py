"""Explicit editorial replay; reads one credential without printing or persisting it."""
from pathlib import Path
import json, urllib.request, urllib.error, datetime, hashlib, concurrent.futures

ROOT = Path(__file__).resolve().parent
CONFIG = json.loads((ROOT / 'proposed-inputs.json').read_text())
KEY = next(line.split('=', 1)[1].strip().strip('\"\'') for line in
    Path('/Users/sheshnarayaniyer/.claude/.env').read_text().splitlines()
    if line.strip().startswith('SELEMENE_API_KEY='))
OUT = ROOT / 'engine-runs'
OUT.mkdir(exist_ok=True)

def calculate(job):
    character, engine, anchor, options = job
    ident = f"{character['id']}-{engine}-{anchor}"
    destination = OUT / (ident + '.json')
    if destination.exists():
        record = json.loads(destination.read_text())
        return {'id': ident, 'http_status': record['http_status'], 'reused_receipt': True}
    body = {'birth_data': character['birth_data'], 'current_time': CONFIG['anchors'][anchor],
            'location': {'latitude': character['birth_data']['latitude'], 'longitude': character['birth_data']['longitude']},
            'precision': 'standard', 'options': options}
    encoded = json.dumps(body).encode()
    req = urllib.request.Request(f'https://selemene.tryambakam.space/api/v1/engines/{engine}/calculate',
        data=encoded, headers={'X-API-Key': KEY, 'User-Agent': 'SomaticCanticles-Editorial/1.0', 'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=45) as response:
            status, raw = response.status, response.read()
    except urllib.error.HTTPError as error:
        status, raw = error.code, error.read()
    except (TimeoutError, urllib.error.URLError):
        status, raw = 0, b'{"error":"network_or_timeout"}'
    if KEY.encode() in raw:
        raise RuntimeError('Credential echo blocked')
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        data = {'non_json_body_sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}
    record = {'id': ident, 'input_status': CONFIG['status'], 'requested_engine': engine,
              'requested_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'request': body, 'http_status': status, 'response': data}
    destination.write_text(json.dumps(record, indent=2) + '\n')
    return {'id': ident, 'http_status': status}

if __name__ == '__main__':
    jobs = []
    for c in CONFIG['characters']:
        for e in ['numerology', 'human-design', 'gene-keys', 'vimshottari']:
            jobs.append((c, e, 'book1', {}))
        jobs.append((c, 'enneagram', 'book1', {'type': c['canon_enneagram']}))
        for anchor in CONFIG['anchors']:
            jobs.append((c, 'biorhythm', anchor, {}))
            jobs.append((c, 'transits', anchor, {}))
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        results = list(pool.map(calculate, jobs))
    (ROOT / 'run-summary.json').write_text(json.dumps(results, indent=2) + '\n')
    print(json.dumps({'total': len(results), 'http_200': sum(r['http_status']==200 for r in results),
          'other': [r for r in results if r['http_status'] != 200]}, indent=2))
