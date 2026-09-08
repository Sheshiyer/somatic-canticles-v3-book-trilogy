import json,pathlib,re,itertools,hashlib
p=pathlib.Path(__file__).parent; src=pathlib.Path('/Volumes/madara/2026/Projects/tryambakam-noesis/Selemene-engine/crates/engine-human-design/src/analysis.rs')
channels=[tuple(sorted(map(int,x))) for x in re.findall(r'gate1: (\d+),\s*gate2: (\d+)',src.read_text().split('const CANONICAL_CHANNEL_SPECS')[1].split('];')[0])]; assert len(channels)==36
out={'provenance':{'method':'Union of actual natal activated gates compared against local canonical 36 channels. Derived editorial analysis, NOT a Selemene composite response; no compatibility score or causal claim.','channel_source':str(src),'channel_sha256':hashlib.sha256(src.read_bytes()).hexdigest()},'characters':{},'pairs':[]}
for c in ['corv','sona','jian','gideon']:
 def read(e,b='book1'):return json.loads((p/'engine-runs'/f'{c}-{e}-{b}.json').read_text())['response']['result']
 hd=read('human-design'); gates=sorted(set(a['gate'] for k in ['personality_activations','design_activations'] for a in hd[k].values())); actual={tuple(sorted(map(int,ch.split('-')))) for ch in hd['active_channels']}; calc={ch for ch in channels if set(ch)<=set(gates)}
 out['characters'][c]={'hd':hd,'activated_gates':gates,'natal_channel_consistency':actual==calc,'gene_keys_raw':read('gene-keys'),'periods':{b:read('vimshottari',b)['current_period'] for b in ['book1','book2','book3']}}
 print(c,hd['hd_type'],hd['authority'],hd['profile'],'channels_match',actual==calc)
 for b,v in out['characters'][c]['periods'].items():print(b,' / '.join(v[k]['planet'] for k in ['mahadasha','antardasha','pratyantardasha']))
for a,b in itertools.combinations(out['characters'],2):
 ga=set(out['characters'][a]['activated_gates']);gb=set(out['characters'][b]['activated_gates']);new=[ch for ch in channels if set(ch)<=ga|gb and not set(ch)<=ga and not set(ch)<=gb]
 row={'pair':[a,b],'shared_gates':sorted(ga&gb),'complementary_channels':[{'channel':list(ch),a:sorted(set(ch)&ga),b:sorted(set(ch)&gb)} for ch in new]};out['pairs'].append(row);print(a,b,new)
(p/'derived-charts.json').write_text(json.dumps(out,indent=2)+'\n')
for b in ['book1','book2','book3']:
 d=json.loads((p/'engine-runs'/f'team-panchanga-{b}.json').read_text())['response']['result'];print(b,{k:d[k] for k in ['vara_name','tithi_name','nakshatra_name','yoga_name','karana_name']})
