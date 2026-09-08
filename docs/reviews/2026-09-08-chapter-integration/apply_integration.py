from pathlib import Path
import json,hashlib,difflib
SOURCE=Path('/tmp/somatic-v3-review-20260908');TARGET=Path('/Volumes/madara/2026/Projects/tryambakam-noesis/somatic-canticles-book/.work/chapter-integration-v1');OUT=Path(__file__).parent
packets=json.loads((OUT.parent/'2026-09-08-character-engine-matrix/chapter-review-packets.json').read_text());edits=[]
def add(n,anchor,new,why,engines=(),replace=False):
 path=packets[n-1]['path'];edits.append({'chapter':n,'path':path,'anchor':anchor,'replacement':new if replace else anchor+'\n\n'+new,'change_summary':why,'engine_receipts_used':list(engines),'claim_mode':'AUTHORED FICTION grounded in reviewed action; engine correspondences are interpretive, not causal'})
add(1,'“The charge is credible.”', '''Corv opened his mouth to improve the joke, then shut it. The Type Nine lookup in his vessel’s margin named the wish to preserve harmony. He had selected the type himself; it was a question he kept near, not a finding about this room. What came from the room was the missing interval. What came from him was the urge to make it bearable before anyone had answered for it.

“Tell me what you need me to hold.”

“The question,” Sona said. “Until there’s someone here who can answer it.”

He left the slate alone. Sona had not asked him to make the room agree. The blank place remained blank. It cost him more effort than naming it would have.''','Corv compares a selected Enneagram prompt with an external absence and his internal urge, then chooses a question over closure.',['corv-enneagram-book1.json'])
add(3,'Tonight the axiom felt less like creed and more like confession.', '''He nearly told Sona where to stand. The birth-derived biofield map he had opened before entry placed its strongest symbolic emphasis on the Root. He used the emphasis to ask where he was bracing; it could not tell him whether the membrane ahead would hold. For that he watched the seam flex beneath the passing load. He had already read the movement as a threat.

He showed Sona the weak edge with two fingers.

“Can you keep that in reach?”

She moved a half-step farther out than he would have chosen. His jaw tightened. He marked the wider span he would have to cover. She still had room to turn. He waited until she tested the reach before fixing the span he would cover. He had read the same movement first as a reason to close the space, then as a reason to make her passage visible.''','Gideon separates symbolic body-map emphasis, actual membrane movement and his protective interpretation; adjusts an outward action.',['gideon-biofield-book1.json'])
add(5,'“Understood,” Corv answered, the word tasting of copper and regret.', '''“Record that I told you to leave it,” Corv added.

Jian looked up.

“The anomaly. Don’t file the delay under instrument error.”

He wanted to explain the pressure, the noise, the speed with which the choice had arrived. All of it was true. None of it belonged in place of the choice. Jian restored the discarded trace and attached Corv’s instruction to it. The next surge still came.''','Connect Corv’s admission to a corrected record; circumstances explain but do not absolve harm.')
add(6,'He killed the alert. Not useful.', '''His thumb hovered over the cleared space. They had just agreed to keep the outliers. The biorhythm sample he had carried in marked the emotional cycle low. For a moment it offered a convenient account of his irritation. Then he listened to Sona’s actual objection: wrong scale. A curve calculated from his birthday had not heard her argument.

He restored the mark to the private log and opened a second scanner view to look for recurrence beneath the largest peaks. He turned the second view toward her. “Show me where you’d start.” He could test her objection without first deciding whether either of them was calm enough to be right. The shame remained; it no longer had the job of choosing what counted as signal.''','Jian tests a calculated expectation against an external objection, separates shame from signal selection, and changes what he inspects.',['jian-biorhythm-book1.json'])
add(7,"She looked again. This time she did not focus on the whole breath.",'''Sona glanced at the selected Type Four reflection: making identity out of inner experience. She had been treating the relief in herself as evidence that the host was recovering. Jian’s falling-amplitude trace said otherwise. She left the trace visible.

Before looking again, she mouthed a phrase from Mayamalavagowla, the fifteenth Melakarta. She kept it below a hum, feeling where her own tongue hurried the return to Sa. The familiar pattern gave her something small enough to notice. Her hands were still shaking when she finished.

“Watch the variability,” she told Jian. “If I start chasing smoothness again, stop me.”

“I did.”

“Yes. Keep doing it.”

She moved her hand away from the trace so he could mark the point she had passed over.

She kept the note pattern on her own side of the work. The next thing she followed was the host’s uneven response, not the shape the scale made easy for her to expect.

She looked again. This time she did not focus on the whole breath.''','Ground Sona’s self-observation in actual Melakarta15, followed by an explicit correction channel; no therapeutic promise.',['sona-raaga-book1.json','sona-enneagram-book1.json'],True)
add(9,'He let it sit there, a dead weight in a room that had just learned to float.', '''The familiar order still offered him relief: decide once, make everyone safe, carry the blame afterward. He had mistaken that last promise for generosity often enough. Sona shifted toward the edge of his cover. This time he asked whether she needed more room before tightening it.''','Recur Gideon’s boundary practice in a different context; admitting blame is not permission to control.')
add(14,'They changed posture together.', '''“Separate checks,” Jian said.

The old bodygraph shorthand waited at the edge of his display: two Manifesting Generators with emotional authority, his own Generator’s sacral response, Gideon’s Projector and splenic authority. Useful until he tried to turn four people into four settings.

“Ready,” Sona said.

“Another moment,” Corv said.

Same type, different answer. Jian left both in the record. His own readiness did not settle the timing for them. Gideon indicated the opening he was watching and kept his hands away from the others’ controls.''','Show actual HD types through different answers and shared procedure, without treating readiness as certainty.',['corv-human-design-book1.json','sona-human-design-book1.json','jian-human-design-book1.json','gideon-human-design-book1.json'])
add(16,'Jian stood at his station in the Anamnesis Engine chamber,', '''Gideon’s Vimshottari entry had changed since the last descent: the Moon’s long period continued, but Mercury had replaced Saturn in the period nested beneath it. Jian had flagged the change for their review. He had also watched Gideon reach for the same old perimeter settings that morning.

Beside the period pane he kept the correction log. At yesterday’s review, Sona had asked for a pause. Jian had asked for one more reading. She had left the table. He had finished alone, and the neat report concealed that fact until he added it himself.

Jian stood at his station in the Anamnesis Engine chamber,''','Locate computed long-period context in existing six-week review, subordinate to actual conduct.',['corv-vimshottari-book3.json','sona-vimshottari-book3.json','jian-vimshottari-book3.json','gideon-vimshottari-book3.json'],True)
add(18,'They read the four conditions back in silence.', '''Jian added a second column: who would have to change what on the next attempt. He put his own name beside the demand for a cleaner signal. It had survived three revisions by hiding inside the calibration settings.

Sona tapped that entry, then wrote her own. No one crossed out a failure because someone had understood it.''','Translate reflection into the next observable correction rather than declaring learning from recorded failure alone.')
add(20,'"And if I make it mercy, I will start forgiving things that have not asked to be forgiven."' ,'''She felt the old wish to give the chamber a gentler ending. Her throat knew how. She let the wish remain without lending it her voice. There were people who would have to live with what happened here; relief in her own chest could not answer for them.''','Make Sona’s boundary against proxy forgiveness embodied without inventing a victim’s response.')
add(22,'At second glance, it looked like obedience that had learned medical language.', '''Sona noticed how badly she wanted the display to be right. The remembered Melakarta rose to her lips. She left it there, unvoiced, and listened to the breathing beside her. This was not a moment to supply the room with a prettier answer.''','Revisit Sona’s freely available musical practice through contextually choosing not to use it.',['sona-raaga-book1.json'])
add(26,'They did not begin by inventing physics.', '''They had not arrived without an inheritance. Gideon still noticed an exposed edge before an open way; Corv still reached for a story. Corv could feel the latent pull he called destiny without knowing everything it might make possible. The old habits were familiar; they were not the whole blueprint. Neither the habit nor the possibility could take the next step for him.

He watched Gideon leave a gap in the boundary, large enough to choose an exit, and kept himself from explaining the gap away.

They did not begin by inventing physics.''','Preserve destiny as latent inheritance alongside chosen responsibility, within fictional world mechanics.',replace=True)
add(27,'The rest itself was doing too much work to interrupt.', '''Sona lifted a finger, the beginning of an offer.

“Could we keep the quiet a little longer?” Jian asked.

“I’d like that,” she said, and let her hand fall. Gideon eased back from the best lookout until his shoulders touched the trunk. Corv almost remarked on the progress. Instead he shifted to make room.

For once, none of them had to turn the moment into evidence.''','End the recurrence with ordinary rest, a declined offering, shared space and unannounced practice.')
records=[]
for entry in packets:
 n=entry['chapter'];rel=entry['path'];src=(SOURCE/rel).read_text();body=src;changes=[x for x in edits if x['chapter']==n]
 for e in changes:
  assert body.count(e['anchor'])==1,(n,e['anchor'],body.count(e['anchor']));body=body.replace(e['anchor'],e['replacement'],1)
 if changes:(TARGET/rel).write_text(body)
 records.append({'chapter':n,'path':rel,'disposition':'revised' if changes else 'retained','source_sha256':hashlib.sha256(src.encode()).hexdigest(),'candidate_sha256':hashlib.sha256(body.encode()).hexdigest(),'source_evidence':entry['evidence'],'changes':changes,'retention_reason':None if changes else 'Existing chapter evidence carries the mapped action; preserve it as context/recurrence rather than add a redundant explanation. See CHAPTER-MATRIX.md for the specific reviewed function.','state':'DRAFT','limitations':['Selected passage integration review, not a full line-by-line literary certification.','No exact intermediate scene dates or excluded engine fields introduced.']})
(TARGET/'EDITORIAL-INTEGRATION.json').write_text(json.dumps({'state':'DRAFT','chapters':records},indent=2)+'\n');(OUT/'integration-ledger.json').write_text(json.dumps(records,indent=2)+'\n')
patch=''.join(''.join(difflib.unified_diff((SOURCE/r['path']).read_text().splitlines(True),(TARGET/r['path']).read_text().splitlines(True),fromfile='a/'+r['path'],tofile='b/'+r['path'])) for r in records);(OUT/'chapter-integration.patch').write_text(patch)
print('Reviewed',len(records),'revised',sum(bool(r['changes']) for r in records),'retained',sum(not r['changes'] for r in records))
