import {readFileSync,writeFileSync,readdirSync} from 'node:fs';
import {createSourcePack} from '/Volumes/madara/2026/Projects/tryambakam-noesis/Selemene-engine/packages/witness-pipeline/src/assets/factory.ts';
import {runChainAudit} from '/Volumes/madara/2026/Projects/tryambakam-noesis/Selemene-engine/packages/witness-pipeline/src/assets/audit.ts';
const root=import.meta.dir, records=[];
for(const file of readdirSync(root+'/reports').filter(x=>x.endsWith('.json'))){
 const d=JSON.parse(readFileSync(root+'/reports/'+file,'utf8')), id=file.slice(0,-5), engines=d.context.subjects.flatMap((s:any)=>s.engine_results);
 const input={personId:id,readingMarkdown:d.output.assembled,engineResults:engines,outputDir:root+'/source-packs/'+id,patternLearning:{extracted:d.output.patterns.length,upserted:0,skipped:d.output.patterns.length}};
 const pack=await createSourcePack(input), audit=runChainAudit(input);
 records.push({id,passes:d.output.passes.map((p:any)=>({id:p.id,rubric:p.rubric})),chain_audit:audit,source_pack:pack.paths,patterns_extracted:d.output.patterns.length,patterns_remote_upserted:0,editorial_status:'CONTEXT_ONLY_NOT_CANON',limits:['Chain audit counts engine envelopes; it does not verify factual prose or empirical validity.','Generated interpretations require selective editorial review. Requested model in rubric is not actual inference provenance; see calls/*.json.']});
}
writeFileSync(root+'/pack-audit.json',JSON.stringify(records,null,2));console.log('Packaged',records.length);
