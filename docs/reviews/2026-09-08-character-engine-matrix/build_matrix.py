import json,pathlib
p=pathlib.Path(__file__).parent
# Editorial annotations from reviewed source evidence; these are not engine outputs.
notes='''Restraint before interpretation|Waits before declaring victory|Tracks grief without resolving it|Records provisional trust|Tests load before team advances
Memory has a price|Accepts a cost instead of a clean story|Listens to absence|Carries an imprint rather than erasing it|Uses a scalpel rather than a sword
Safety can erase freedom|Recognizes guilt as a control route|Detects coercive comfort|Maps standardized replacement|Questions clean orders
Compassion requires responsibility|Recognizes the cutting reflex|Questions beauty as purchased mercy|Protects the interval before surrender|Owns the cost of closing a gate
Keep the inconvenient evidence|Supports without capturing|Regulates amid noise|Admits discarded outliers|Ensemble support; individual repair needs a clearer beat
Insight does not end relapse|Refuses the offered false binary|Accepts feeling beyond visual proof|Suppresses a shame alert: counterexample|Holds distinct beats together
Repair harmful help|Recognizes compensation architecture|Stops over-soothing after noticing harm|Preserves variability rather than flattening it|Withdraws support enough for self-holding
Carry the practice onward|Refuses old intelligence as law|Maintains a distinct contribution|Accepts a compass with a cost|Uses an embodied steadying habit
Transfer beyond the descent|Participates in a sustainable baseline|Distinguishes rest from enforced quiet|Revises safety as dynamic|Lets the father's command exist without obeying it
Notice diagnosis becoming command|Reclassifies scripts as jurisdictions|Holds possible selves open|Notices protection preceding evaluation|Ensemble evidence; owned choice needs reinforcement
Protect passage rather than form|Negotiates passage|Uses low-demand legibility|Maps handoffs between protections|Refuses shaming an adaptation
Restore authorship|Rejects amnesia as resolution|Keeps difference available to the team|Distinguishes foundation from habit|Practises partnership
Make room for witness|Holds relation without conquest|Tests sameness against differentiated resonance|A no-error log is insufficient proof|Accounts for the weight of exit
Repeat and recalibrate|Sees emergency override becoming law|Responds when called|Records failures and recalibrates slowly|Shares work without pre-emptive control
Resist effortless merger|Replaces master monologue with dialogue|Names the skipped cost of merger|Tracks capacity lost through offloading|Recognizes dependency on a helpful field
Six-week stress test|Mourns without interpreting|Notices clean metrics alongside a cold body|Logs pauses and failures|Admits the missing perimeter
The return of competent control|Refuses premature naming|Distinguishes numbness from rest|Faces the temptation of tidy care|Recognizes protection made breathless
Learn without inevitability|Refuses a theory that makes events necessary|Maintains a distinct team vector|Logs failed timing and pauses before obedience|Maintains relation without enforced agreement
Joy is not a management tool|Recognizes tenderness mismanaged into meaning|Distinguishes joy from morale|Accepts a map that deforms|Faces institutional pressure to relabel learning as risk
Own the harm without purchasing absolution|Stops feeding the wrong rather than decorating confession|Will not forgive on another person's behalf|Records exact strain rather than beautiful totals|Carries bodily cost with the team
Consent changes the baseline|Shares the cost of one bounded test|Keeps differentiated clarity available|Refuses polite averages and lost consent|Interrupts responsibly without owning interpretation
Refusing false rest still hurts|Faces the lure of ready-made meaning|Refuses relief while acknowledging its attraction|Recognizes certainty as absolution|Delays recognizing his own protection trap
Freedom includes maintainability|Uses plain language after beautiful closure|Participates without a compulsory hopeful banner|Tests whether the whole team can maintain a solution|Recognizes safety that shrinks choice
Do not substitute another's refusal|Accounts for the bodily ledger|Rejects help delivered before permission|Notices flattering numbers|Lets each person own their refusal
Beauty must wait for consent|Refuses tidy lesson labels|Remains present without needing a signal|Tolerates invalidity|Recognizes control inside a soft membrane
Inheritance meets choice|Allows gaps in meaning|Recognizes learned inheritance beyond the enemy|Waits at a boundary rather than imposing timing|Practises the boundary as an action
Ordinary life is the test|Values habitable rest and unforced contact|Can be ordinarily tired|Accepts freedom without cleanliness|Shares a door that opens when hands are steady'''
rows=[r.split('|') for r in notes.splitlines()];assert len(rows)==27
packets=json.loads((p/'chapter-review-packets.json').read_text());matrix=[];md=['# Chapter × character integration matrix','','Status: editorial proposal grounded in all 27 chapter evidence packets; not a rewritten manuscript. All chapter texts were scanned; selected source passages were reviewed. This is not a complete line-by-line literary review. Source HEAD: ba74a874fdc43c00b3661d026cb865584b6daaa7.','','Dates are proposed book/session anchors, not established scene dates. Engine lenses identify editorial opportunities, not causes or diagnoses. See CHARACTER-ARCS.md and DATA-QUALITY.md.','','| Ch | Integration test | Corv | Sona | Jian | Gideon |','|---|---|---|---|---|---|']
chars=['corv','sona','jian','gideon'];config=json.loads((p/'proposed-inputs.json').read_text())
for n,(packet,row) in enumerate(zip(packets,rows),1):
 b='book1' if n<=8 else 'book2' if n<=15 else 'book3'
 stage='action and interruption' if n<=4 else 'recurrence and repair' if n<=8 else 'routine and behaviour under pressure' if n<=15 else 'relapse and accountable revision' if n<=20 else 'perspective and ordinary-life transfer'
 md.append('| '+str(n)+' | '+' | '.join(row)+' |')
 for c,note in zip(chars,row[1:]):
  ev=packet['evidence'][c]
  matrix.append({'chapter':n,'character':c,'source_path':packet['path'],'source_sha256':packet['sha256'],'source_evidence':ev,'review_annotation':note,'proposed_integration_test':row[0],'proposed_transformation_focus':stage,'date_status':'proposed session anchor only; scene timing unresolved','session_anchor':config['anchors'][b],'engine_receipts':[f'engine-runs/{c}-human-design-book1.json',f'engine-runs/{c}-gene-keys-book1.json',f'engine-runs/{c}-vimshottari-{b}.json',f'engine-runs/team-panchanga-{b}.json'],'evidence_limit':'Selected passages may be ensemble evidence; annotation is editorial synthesis. Engine-specific practice is a proposed insertion, not asserted present in canon.'})
(p/'chapter-character-matrix.json').write_text(json.dumps(matrix,indent=2)+'\n');(p/'CHAPTER-MATRIX.md').write_text('\n'.join(md)+'\n')
