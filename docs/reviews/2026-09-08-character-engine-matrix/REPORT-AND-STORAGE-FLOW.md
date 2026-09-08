# Witness, report and storage flow

## What exists and what it can establish

The source treats Selemene as the canonical witness service and witness-agents as persona/asset reference material. This review did not verify that the historical witness-agents deployment is stopped. A repository retirement note alone cannot prove runtime retirement.

`POST /api/v1/witness/interpret` can return Aletheios, Pichet, synthesis and an inquiry question, with `llm_powered` distinguishing model use from rule-based fallback. Source explicitly runs seven primary engines, not every registered engine. Optional partner context adds HD, numerology, Gene Keys and Vimshottari. A relationship interpretation is not an independently calculated pairwise bodygraph. The route requires `live_scores`, uses server `Utc::now()`, and has no explicit story-date input. Supplying invented camera scores or presenting this as a 2027 reading would corrupt provenance.

`POST /api/v1/assets/generate` accepts rich subjects, relationship context and L0–L5 report depth. The inspected implementation uses six primary-subject engine seeds and deterministic seed rendering for each pass. It does not execute the complete TypeScript LLM pipeline merely because it returns `passes`, `assembled` and `source_pack`. Its time is also server-now. Rich intake metadata does not prove all subjects were calculated.

`packages/witness-pipeline/src/orchestrator/integrated.ts` is the substantive multi-pass layer: injected LLM, mode-defined passes, previous-pass context, optional retrieved patterns, section rubric and extracted patterns. It accepts `engineResultsBySubject`; a future frozen-date report should consume explicit, validated receipts there. Its current `modelUsed` rubric value is copied from the requested pass model, so it is not a provider-resolution receipt. It returns extracted patterns; that alone is not evidence they were persisted.

## KV and Vectorize are different jobs

- Gateway KV holds credentials behind the proxy. `/health` returns presence booleans. This is not a character-data storage API.
- LLM-proxy KV supplies provider credentials after a shared-secret gate. Do not export them into source packs.
- Pattern-memory worker exposes `/patterns` and `/patterns/query`; the inspected entrypoint has no authentication gate. Its configured resource IDs include placeholders. No live deployment, outer protection, query, or write was established in this review.
- The worker attempts R2, otherwise D1, for full pattern records, then upserts embeddings and metadata into Vectorize. If durable persistence fails it can fall back to putting text in vector metadata. That is weaker than a guaranteed canonical JSON record.
- Its privacy filter is heuristic and not an approval gate. The final character dossiers should not be dumped into the pattern index. Keep versioned source packs as canonical records; extract only reviewed reusable patterns for retrieval.

No remote KV/Vectorize writes were made. This review saves local JSON. That fulfils mapping persistence without pretending the production storage pipeline has been verified.

## Freeze and report sequence

1. Review all-engine registry and resolve blocking field-quality issues.
2. Approve fictional births and exact event calendar; record the date convention and local timezone at each event.
3. Hash/version the frozen inputs, then calculate date-dependent records. Select and preserve any draw/seed before interpretation.
4. Retain raw requests/responses unchanged; attach normalization and exclusions separately.
5. Generate character and team interpretations from those explicit records using the full report implementation, with actual provider/model/fallback receipts.
6. Review claims against their engine fields and chapter evidence. Aletheios tests the interpretation; Pichet proposes a bounded act; synthesis retains disagreement and choice.
7. Save reviewed report JSON, source references, chapter links and revision state. Promote a report to canon only with the principal's review; index anonymized reusable patterns separately after deployment/access/durable-storage validation.

Current status: inputs proposed; calculation samples retained; mapping review stored; date freeze and final reports pending. No requirement to run all engines for every character or chapter follows from reviewing the complete inventory.

## Sona: from Melakarta structure to outward practice

The live sample explicitly requested Melakarta 15 at a 220 Hz root. Raaga returned `Mayamalavagaula`, eight swara entries and ratios, ascending/descending indices, and `total_melakartas: 72`. No audio was requested or generated. Nada's spelling is `Mayamalavagowla`; join on numeric identifier 15, preserving display names as returned.

Sona can ask permission to try a phrase, notice where she feels vibration, notice whether the listener wants continuation, change tempo or stop, and carry that learning into a later conversation. The ratios ground the musical object. The person's response grounds the scene. The engine's chakra/dosha correspondences remain interpretive, not proof of an effect. A Melakarta scale alone does not supply the entire artistry of a performed raga.

The returned Raaga prahar is `Night` despite the supplied story instant. Source uses the server's wall clock for time annotations. Nada uses UTC hour; Vedic-clock uses explicit local offset. These three time bases must be reconciled before scene-specific recommendations are finalized. Explicit Melakarta selection still yields a usable musical data sample while time suitability remains excluded.

The absent standalone somatic engine is represented as a practice layer with `engine_id: null`, not a fabricated endpoint. It joins attention, chosen action, observed outcome and recurrence. This also applies outside sound: changing the room, renegotiating workload, keeping an exit usable, or apologizing and making repair.
