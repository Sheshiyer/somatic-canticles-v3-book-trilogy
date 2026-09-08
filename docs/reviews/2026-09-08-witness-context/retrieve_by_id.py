from pathlib import Path
import json
exec((Path(__file__).parent/'retrieve.py').read_text().split('queries=')[0])
ids=['sw:hd:type:'+t+':desc' for t in ['manifesting-generator','generator','projector']]+['sw:hd:auth:'+t+'-authority:desc' for t in ['emotional','sacral','splenic']]+['sw:enn:'+str(n)+':core' for n in [9,4,5,8]]
r=req(root+'/vectorize/v2/indexes/witness-wisdom-corpus/get_by_ids',env['CLOUDFLARE_API_TOKEN'],{'ids':ids});print('get_by_ids',r['status'],str(r['body'])[:100] if r['status']!=200 else '',flush=True)
if r['status']==200:
 entries=r['body'].get('result',[]);print('entries',len(entries),flush=True)
 (p/'retrieved-exact-context.json').write_text(json.dumps({'method':'exact corpus ids from ingestion source; embedding provider bge-m3 returned HTTP410','status':r['status'],'entries':[{k:v for k,v in x.items() if k!='values'} for x in entries]},indent=2)+'\n')
 out=[]
 for entry in entries:
  if entry['id'].startswith('sw:enn:'):
   q=req(root+'/vectorize/v2/indexes/witness-wisdom-corpus/query',env['CLOUDFLARE_API_TOKEN'],{'vector':entry['values'],'topK':5,'returnMetadata':'all','filter':{'system':'enneagram'}})
   out.append({'seed_id':entry['id'],'method':'nearest neighbors of existing corpus embedding, not a fresh textual query','response':q});print(entry['id'],q['status'],flush=True)
 (p/'retrieved-neighbors.json').write_text(json.dumps(out,indent=2)+'\n')
else:(p/'retrieved-exact-context.json').write_text(json.dumps(r,indent=2)+'\n')
