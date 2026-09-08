# One cosmology, several depths of encounter

DRAFT architecture and editorial plan · 8 September 2026

The book, mobile app, web experience, and Selemene can share continuity without duplicating one another. A reader can complete the novel without an account or a report. A reader who wants practice can follow a chapter's introduction, return to it freely, and choose deeper context when useful. This preserves the already settled introduction/free-reuse decision while making the ecosystem modular.

This is a proposed design supported by source inspection and earlier dated receipts. No UI, backend, database, infrastructure, or publication change is included. Present deployment parity has not been established.

## 1. What stays invariant as detail changes

The shared meaning unit is a situation: stimulus → situated interpretation → choice → effect → possible return. Its implementation should carry stable identity and source revision. Its presentation should fit the surface.

| Surface | Reader's purpose | What it contains | What must survive compression |
|---|---|---|---|
| Novel | Care about people living through a dilemma | Scene, uncertainty, relationship, sensory world, consequence | The characters' agency and the actual cost |
| Mobile encounter | Try one small action in ordinary life | A short scene reminder, one question, an optional action, a way to stop or defer | The difference between observation and interpretation; freedom to decline |
| Web exploration | Compare, reread, and understand | Scene connections, relationship view, selected lens, sources, alternative interpretations | Disagreement and known limits; no manufactured final answer |
| Selemene reading | Examine symbolic context for a chosen question | Versioned inputs, returned facts, interpretation, omissions, provenance | Facts distinguishable from generated narrative; subject and checkpoint identity |
| Reader's own return | Notice what actually happened | Optional private note, changed intention, reuse of an introduced practice | The person's account can contradict the prompt or report |

These are proposed content responsibilities, not separate maturity levels. Longer reading is not higher realization. A five-minute reflection is not a compressed diagnosis. A reader may remain with one surface and still have a complete experience.

## 2. Example of a faithful compression

**Story anchor:** Jian discounts Sona's objection, recognizes the convenience of his explanation, and opens his scanner to her in Chapter 6. [Source scene](/Volumes/madara/2026/Projects/tryambakam-noesis/somatic-canticles-book/.work/chapter-integration-v1/CHAPTERS/book_1/Chapter-06-The-Synaptic-Crossroads.md:43).

**Proposed mobile card:** “Recall a disagreement in which the other person's explanation irritated you. What did they actually notice? If useful, ask them to show you one example before answering. You can stop here.”

**Optional return:** “Did the example change your question, your action, or neither?” An unchanged view is a legitimate response. No journal entry is required to retain access.

**Proposed web expansion:** show two interpretations of the disagreement, the distinction between an observation and its explanation, and how the characters' shared work changed. Offer the engine context only on request, labeled as a symbolic lens. Do not require a birth profile just to understand this scene or try its ordinary action.

**Editorial annotation:** the novel's bodygraph or biorhythm context does not prove a real colleague's motives. The portable part is the act of checking what was noticed before rejecting an interpretation. A reader can use it without adopting the cosmology's entire vocabulary.

This example is a proposed content adaptation, not a released exercise or a validated behavioral intervention.

## 3. Proposed shared content contract

Reuse existing StoryOps/source-pack conventions where possible. Before creating a new schema, check whether an existing manifest can carry these fields additively:

```text
situation_id
manuscript_revision + chapter_id + scene_anchor + source_hash
character_ids + relationship_ids
learning_question
introduced_practice_ids
primary_lens_id? + lens_version? + input_revision?
observation / interpretation / action / consequence
recurrence_scene_ids
short_form / expanded_form / provenance_link
status: draft | reviewed | approved | retired
```

Use practice identity independently of chapter identity. A scene can introduce no new practice, revisit an existing one, or supply a counterexample. One practice can recur in several scenes. Book chapter 5 must not be connected to web entry 5 simply because both have the same integer.

Reader state is a separate responsibility:

```text
reader_id + practice_id + introduction_version + introduced_at
optional attempts
optional reflections
optional timing suggestion
```

This is a proposed logical separation, not a final database schema. Practice access follows the saved introduction event. An attempt, reflection, reading-completion percentage, favorable cycle, or generated report does not prove an introduction or spiritual achievement.

When content changes, retain source lineage. Do not silently replace a reader's earlier reflection context with a revised scene. State migration must preserve legitimate access while distinguishing legacy chapter unlocks from verified practice introductions.

## 4. Existing capabilities to reuse, with limits

| Existing surface | Useful role | Evidence level and boundary |
|---|---|---|
| v3 CHAPTERS and StoryOps | Canonical narrative, candidates, rejection/keep records, source hashes | Current remote chapter identity freshly checked. No new revision made. |
| `rubric_scan.py`, `gating_contract.py` | Cheap checks for duplication, style proxies, epistemic patterns | Source/prior tests. They cannot assess chemistry, consent, or moral complexity by keyword. Review the legacy anti-compression rule before a new compression campaign. |
| Ether-First tooling | Hashed source ingestion, findings, claim normalization, reversible candidates | Earlier review reports 45 passing tests. No fresh full test run here; deterministic candidates do not constitute independent literary judgment. |
| Noesis Writer v2.17.0 Route E | Continuity of settled intention and claim boundaries | Skill read fresh. Proposed relation packet should be tested before changing the reusable skill. |
| Selemene calculation/workflow registry | Select a bounded lens and preserve returned data | Source inspected; earlier 66 HTTP200 calculation receipts are historical transport evidence, not general correctness. |
| IntegratedReadingOrchestrator | Mode-based passes, relationship framing, retrieval, source-pack input | Source path requires explicit fact injection in the adapter; current rubric input covers only the first subject array. |
| L4 / colleague-pair modes | Depth and pair context when applicable | L4 max two subjects. Family-penta cannot be repurposed as an expedition merely because four people fit the count. |
| Source-pack factory and chain audit | Package the selected reading, engine provenance, and reflection questions | Prior local invocation exists. Envelope counts do not prove the factual quality of every sentence. |
| Vectorize and KV | Potential retrieval and continuity storage | Earlier exact-record retrieval succeeded; similarity returned no matches, embedding request failed, inspected context KV was empty. No fresh remote writes or all-service health claim. |
| Web companion | Existing practice/reflection presentation and database-backed reader routes | Prior source/function audit identifies 12 developed entries and 15 placeholders. Static content does not prove current production database content. |
| Mobile companion | 27-chapter content, chapter authority selection, Selemene client | Prior source/function audit shows access can relock with cycle changes; native reflection parity still needs verification. |
| Brandmint/wiki/audio/source assets | Discovery, accessible formats, deeper presentation | Recorded artifacts exist. Present delivery/media health and reader outcomes were not tested here. |
| Sankalpa and other Noesis organs | Potential daily-practice continuity | Prior integration references exist. Inspect their owning sources before proposing shared state or duplicating an established feature. |

See [prior app audit](/Volumes/madara/2026/Projects/tryambakam-noesis/somatic-canticles-book/docs/reviews/2026-09-08-lived-noesis/CHAPTER-PRACTICE-AUDIT.md), [prior tooling review](/Volumes/madara/2026/Projects/tryambakam-noesis/somatic-canticles-book/docs/reviews/2026-09-08-v3-understanding/UNDERSTANDING.md), and [witness path](/Volumes/madara/2026/Projects/tryambakam-noesis/Selemene-engine/packages/witness-pipeline/src/orchestrator/integrated.ts:105).

Use caching for reproducible calculation envelopes keyed by input/version; keep interpretations replaceable. Keep readers' optional private reflections out of shared pattern retrieval by default. A pattern memory should preserve corrections and exclusions, not recycle a rejected report as support for the next report. These are design proposals for the owning repositories.

## 5. Reconcile the contracts before implementation

| Conflict | Source basis | Proposed resolution / decision boundary |
|---|---|---|
| Perfect coherence versus continued vulnerability | Legacy thirteenth-lens doctrine; Chapter 24; newer lived-integration guidance | Author reviews a bounded post-ripening model; no automatic rewrite. |
| Sixteen engines versus other source/live counts | Aleph corpus, README, narrative types, previous inventory | Publish versioned registries by surface, with aliases. Keep 13 fictional lenses separate. |
| “256” combinations from 16 × 4 | Product description line 70 | Correct arithmetic to 64 unless an additional independent dimension is actually specified. |
| No chapter gating versus biorhythm-based access | Brand says all chapters accessible; prior mobile evaluator relocks | Treat chapter access and introduced-practice access as separate policies. User's practice-reuse decision is fixed; chapter-access migration needs its own proposal. |
| System determines direction versus reader authorship | Product's compass language and newer choice commitments | Present direction as a situated recommendation with disclosed basis and a way to decline. Do not silently claim this is implemented. |
| Progression versus outgrowing the system | Brand anti-dependency; guided introduction | Reveal a repertoire, then let it remain usable without streaks, favorable timing, or repeated assessments. |
| Biological readiness rhetoric versus symbolic calculations | Brand cycle/readiness copy and existing data-quality exclusions | State whether input is measured, reported, calculated, traditional, or fictional. Avoid implying that birth cycles measure fatigue or suitability. |
| 27 manuscript chapters versus 12 developed web entries | Prior exported content audit | Reconcile using actual scene/source references, preserve recurrence, do not create 15 exercises merely to fill a grid. |

Octalysis is already the user's selected interaction framework. This plan carries that choice forward without importing new claims about its effectiveness. Design progress as access to a growing repertoire, curiosity as optional depth, and social connection as voluntary witnessing. Test scarcity or streak mechanics against the established compassionate-return behavior; do not attach moral worth to engagement.

## 6. Proposed work sequence and exit evidence

| Step | Concrete output | Dependency | Exit evidence |
|---|---|---|---|
| A. Canon reconciliation | Short reviewed note for lenses, sheaths, destiny, and post-ripening limits | This critique | Each conflicting source is explicitly retained, narrowed, or superseded by the author |
| B. Relational pilot | Chapter 6 candidate and later recurrence, plus before/after packet | A where affected; existing chapter evidence | Distinct motives, changed burden, persistent dissent, voice/humor intact; human editorial acceptance |
| C. Team development | Six pair arcs and group coalition/workload changes across books | Accepted B | Each arc has setup, cost, altered cooperation, and a transfer or relapse scene |
| D. Structural manuscript pass | Review long/repeated sequences and process-language leaks | Stable scene/arc priorities | Cuts preserve causal change; no automatic word floor/ceiling; continuity readback |
| E. Content identity | Reconciled manuscript-to-practice manifest | Accepted relevant scenes | Every developed companion entry has a real source; placeholders and recurrence are explicit |
| F. Companion policy design | Introduction event, permanent practice access, optional reflection, migration | E and existing user decisions | State transitions reviewed against prior access; preserving access does not require private disclosure |
| G. Owning-repository implementation | Small source-pack/API/UI slice in web and mobile | Approved F | Behavior-level database tests, fresh UI/device evidence, offline/reload cases, no cross-reader leakage |
| H. Accepted export and delivery | Compiled book/audio/wiki/source-pack versions | Accepted manuscript and content | Source hashes match artifacts; actual links/media verified; publication separately authorized |

Backend improvements can be bounded in parallel with editorial work: preserve Human Design lines into Gene Keys, validate labels, unify time semantics, insert all-subject facts into witness prompts, ground multi-subject auditing, record actual model receipts, and repair retrieval only where a planned use needs it. Those changes belong to Selemene and do not require delaying the first literary pilot that uses already validated receipts.

When implementation reaches persistence, verify the real database behavior rather than infer production parity from an in-memory helper. When it reaches mobile, verify the device flow rather than infer feature parity from shared content. Neither is a requirement to deploy infrastructure during this review.

## 7. What to measure without turning growth into a score

For an editorial test, ask a reader to retell the choice, name the different motives, identify who paid, and explain what changed in the relationship. Record confusion and counter-readings, including whether the text felt preachy or whether engine language displaced the scene.

For a companion test, verify that a reader finds an introduced practice, can decline it, can return without losing access, and understands the difference between their observation and the suggested interpretation. Usability evidence answers those questions. Completion, streaks, and report depth cannot establish a changed worldview.

For compression, compare the short and long forms: does each preserve the same agent, choice, uncertainty, and consequence? A short form fails if it turns “test another person's observation” into “trust intuition,” or turns a symbolic prompt into a verdict. The smaller form should be complete enough to use, with a voluntary route back to depth.
