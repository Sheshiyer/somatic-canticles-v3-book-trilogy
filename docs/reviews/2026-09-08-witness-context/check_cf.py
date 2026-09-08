from pathlib import Path
import urllib.request,urllib.error,json
p=Path(__file__).parent
lines=Path('/Users/sheshnarayaniyer/.claude/.env').read_text().splitlines();key=next(x.split('=',1)[1].strip().strip('\"\'') for x in lines if x.startswith('CLOUDFLARE_API_TOKEN='))
account='9d9d23b27f32e70ae3afb6a1aa2c0f10'
for name,path in [('vectorize',f'/accounts/{account}/vectorize/v2/indexes'),('kv',f'/accounts/{account}/storage/kv/namespaces')]:
 req=urllib.request.Request('https://api.cloudflare.com/client/v4'+path,headers={'Authorization':'Bearer '+key})
 try:
  with urllib.request.urlopen(req,timeout=25) as r:status,raw=r.status,r.read()
 except urllib.error.HTTPError as e:status,raw=e.code,e.read()
 assert key.encode() not in raw
 d=json.loads(raw);(p/(name+'-account-readback.json')).write_text(json.dumps({'account':account,'status':status,'response':d},indent=2)+'\n');print(name,status,json.dumps(d)[:4000])
