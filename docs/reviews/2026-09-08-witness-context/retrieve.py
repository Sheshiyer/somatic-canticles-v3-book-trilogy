from pathlib import Path
import json,urllib.request,urllib.error,concurrent.futures
p=Path(__file__).parent;env={}
for line in Path('/Users/sheshnarayaniyer/.claude/.env').read_text().splitlines():
 if '=' in line:
  k,v=line.split('=',1)
  if k in ['CLOUDFLARE_API_TOKEN','NVIDIA_API_KEY']:env[k]=v.strip().strip('\"\'')
a='9d9d23b27f32e70ae3afb6a1aa2c0f10';root=f'https://api.cloudflare.com/client/v4/accounts/{a}'
def req(url,key,body=None):
 r=urllib.request.Request(url,data=json.dumps(body).encode() if body is not None else None,headers={'Authorization':'Bearer '+key,'Content-Type':'application/json'})
 try:
  with urllib.request.urlopen(r,timeout=45) as s:status,raw=s.status,s.read()
 except urllib.error.HTTPError as e:status,raw=e.code,e.read()
 for k in env.values():assert k.encode() not in raw
 return {'status':status,'body':json.loads(raw)}
queries={'corv':'Human Design emotional authority Manifesting Generator profile 4/6 Enneagram Nine harmony conflict avoiding closure','sona':'Human Design emotional authority Manifesting Generator profile 4/6 Enneagram Four identity feeling empathy boundaries','jian':'Human Design Generator sacral authority profile 1/3 Enneagram Five experiment certainty external response','gideon':'Human Design Projector splenic authority profile 4/6 Enneagram Eight protection control invitation'}
e=req('https://integrate.api.nvidia.com/v1/embeddings',env['NVIDIA_API_KEY'],{'model':'baai/bge-m3','input':list(queries.values()),'input_type':'query','truncate':'END'});print('embedding',e['status'],flush=True)
if e['status']==200:
 vectors=[x['embedding'] for x in sorted(e['body']['data'],key=lambda x:x['index'])];results=[]
 for (c,q),v in zip(queries.items(),vectors):
  r=req(root+'/vectorize/v2/indexes/witness-wisdom-corpus/query',env['CLOUDFLARE_API_TOKEN'],{'vector':v,'topK':8,'returnMetadata':'all','filter':{'system':{'$in':['human-design','enneagram']}}});results.append({'character':c,'query':q,'embedding_model':'baai/bge-m3','dimensions':len(v),'response':r});print('retrieval',c,r['status'],flush=True)
 (p/'retrieval.json').write_text(json.dumps(results,indent=2)+'\n')
else:(p/'retrieval.json').write_text(json.dumps({'error':e},indent=2))
ns=[]
for page in range(1,5):
 r=req(root+f'/storage/kv/namespaces?page={page}&per_page=20',env['CLOUDFLARE_API_TOKEN']);ns+=r['body'].get('result',[])
selected=[x for x in ns if any(s in x['title'].upper() for s in ['WITNESS','ENGINE_DATA','CONSCIOUSNESS','SELEMENE']) and 'SECRET' not in x['title'].upper()]
kv=[]
for n in selected:
 r=req(root+f"/storage/kv/namespaces/{n['id']}/keys?limit=100",env['CLOUDFLARE_API_TOKEN']);keys=r['body'].get('result',[]);kv.append({'namespace':n,'status':r['status'],'keys_count_first_page':len(keys),'cursor':r['body'].get('result_info',{}).get('cursor'),'generic_wisdom_keys':[x for x in keys if any(x['name'].startswith(t) for t in ['sw:','wisdom:','traits:','archetype:'])]})
(p/'kv-context-inventory.json').write_text(json.dumps(kv,indent=2)+'\n');print('kv',[(r['namespace']['title'],r['keys_count_first_page'],len(r['generic_wisdom_keys'])) for r in kv])
