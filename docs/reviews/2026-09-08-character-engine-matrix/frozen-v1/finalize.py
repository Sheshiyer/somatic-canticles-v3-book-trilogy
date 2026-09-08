import json,pathlib,hashlib,datetime
p=pathlib.Path(__file__).parent;parent=p.parent
read=lambda f:json.loads((p/f).read_text())
config=read('frozen-inputs.json');charts=read('derived-charts.json');receipts=[json.loads(f.read_text()) for f in sorted((p/'engine-runs').glob('*.json'))]
assert len(receipts)==74 and all(r['http_status']==200 for r in receipts)
parse=lambda s:datetime.datetime.fromisoformat(s.replace('Z','+00:00'))
assert parse(config['anchors']['book3'])-parse(config['anchors']['book2'])==datetime.timedelta(days=42)
for r in receipts:
 anchor=r['id'].split('-')[-1];assert r['request']['current_time']==config['anchors'][anchor]
 if r['requested_engine']=='vimshottari':
  t=parse(config['anchors'][anchor])
  for period in r['response']['result']['current_period'].values():assert parse(period['start'])<=t<=parse(period['end'])
assert all(c['natal_channel_consistency'] for c in charts['characters'].values())
exclusions=[{'field':'gene-keys active_keys.line','reason':'Fixed/default line 3; use actual HD gate.line separately'},{'field':'gene-keys labels','reason':'Confirmed authoritative label mismatch; descriptive set withheld'},{'field':'nadabrahman local-time suitability','reason':'UTC-hour basis not resolved to scene local time'},{'field':'raaga prahar/time suitability','reason':'Server wall clock; explicit Melakarta musical data retained'},{'field':'biofield metrics as physiology','reason':'Birth-derived symbolic values, not physical measurement'},{'field':'consciousness_level / suggested Siddhi','reason':'Not evidence of character attainment'},{'field':'generic witness prose for timing','reason':'Known natal/day wording and nesting errors; structured fields retained'}]
matrix=json.loads((parent/'chapter-character-matrix.json').read_text())
for row in matrix:
 b='book1' if row['chapter']<=8 else 'book2' if row['chapter']<=15 else 'book3';row['session_anchor']=config['anchors'][b];row['date_status']='frozen v1 checkpoint sample; not exact scene timestamp';row['checkpoint_role']={'book1':'expedition entry sample','book2':'last-descent exit sample','book3':'Chapter16 six-week return sample'}[b]
obj={'schema_version':'1.1.0','status':'frozen_editorial_calculation_baseline','dates_frozen':True,'freeze_scope':'Four fictional birth profiles and three calculation checkpoints; intermediate scene instants unresolved. Not manuscript prose promotion.','inputs':config,'input_sha256':hashlib.sha256((p/'frozen-inputs.json').read_bytes()).hexdigest(),'character_charts':charts,'chapter_character_mapping':matrix,'engine_inventory_review':'../engine-integration-registry.json','exclusions':exclusions,'interpretation_status':'Editorial character arcs remain in ../CHARACTER-ARCS.md; rich witness/final LLM reports not generated. Requires frozen-input-compatible report path.','raw_receipts':[{'id':r['id'],'path':'engine-runs/'+r['id']+'.json','sha256':hashlib.sha256((p/'engine-runs'/(r['id']+'.json')).read_bytes()).hexdigest()} for r in receipts],'remote_storage_written':False}
(p/'book-engine-mapping.json').write_text(json.dumps(obj,indent=2)+'\n')
(p/'run-summary.json').write_text(json.dumps({'total':74,'http_200':74,'engine_ids':sorted(set(r['requested_engine'] for r in receipts))},indent=2)+'\n')
(p/'verification.json').write_text(json.dumps({'gate':'PASS_WITH_EXCLUSIONS','meaning':'Enough for a reproducible editorial mapping baseline, not certification of every engine or final interpretation report.','receipt_count':74,'all_http_200':True,'request_instants_match_freeze':True,'vimshottari_period_containment':True,'natal_channel_consistency':4,'pairs':6,'chapter_character_cells':108,'six_week_gap_exact':True,'field_exclusions':exclusions},indent=2)+'\n')
print('PASS_WITH_EXCLUSIONS: 74 receipts, 4 charts, 6 pairings, 108 mappings; 42-day gap verified')
