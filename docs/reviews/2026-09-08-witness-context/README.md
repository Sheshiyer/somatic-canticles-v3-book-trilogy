# Witness context pass — 2026-09-08

Status: editorial context and selective chapter revision; no canon promotion or remote writes.

The user requested actual integrated readings and witness retrieval to deepen the all-character stimulus/interpretation mapping. `run_readings.ts` executes Selemene's actual `IntegratedReadingOrchestrator`, mode parser, passes, rubrics and pattern extraction with a runtime LLM callback. Frozen engine receipts and ten retrieved corpus records are supplied explicitly. The current orchestrator does not insert `engineResultsBySubject` into its own pass prompts, so the adapter appends them. Source repositories are unchanged.

## Scope and actual evidence

`mode-inventory.json` reviews ten modes. Four birth-blueprint, four integrated-reading and six pair business-partners readings are requested. Pair roles explicitly mean fictional colleagues; no commercial relationship is inferred. Family, romantic and lineage modes are inapplicable. L0 lacks validated kundali inputs; L4 is an alternative depth, not an additional relationship.

`run-summary.json` records generated or failed jobs. `calls/` records actual returned models, finish reasons, latency and hashes. `reports/` retains raw output and supplied context. `verification.json` records totals, rubric outcomes and output-limited passes. A returned pass is not necessarily complete: `finish_reason=length` marks truncation. All raw reports remain context only. Rubric gate success did not prevent substantive errors.

`package_reports.ts` invokes the source-pack factory and chain audit. Local `source-packs/` contain manifests, reading text and reflection questions; `pack-audit.json` preserves checks and pass rubrics. The chain audit counts engine envelopes; its `facts_count` is not a count of independently verified factual claims. Its ready/passed status does not override this editorial limitation. Patterns are extracted locally; remote upserts are zero.

## Retrieval

The configured Selemene Cloudflare account contains `witness-wisdom-corpus`. Ten exact records were retrieved by known corpus IDs: three HD types, three authorities, and Enneagram 9/4/5/8 core descriptions. See `retrieved-exact-context.json`. These are interpretive corpus entries, not empirical personality findings.

The configured NVIDIA embedding request returned HTTP410 (`retrieval.json`). Four subsequent queries using existing record vectors returned HTTP200 but zero matches (`retrieved-neighbors.json`). There are no retrieved neighbors to add. ENGINE_DATA and CONSCIOUSNESS_KV key listings were empty (`kv-context-inventory.json`). No secrets-namespace values or unrelated private records were fetched. No KV/Vectorize writes occurred.

## Editorial use

`reviewed-mapping.json` maps selected questions to four concrete chapter refinements and records rejected claims. Generated reports repeat supplied arc proposals; that repetition is not independent validation. Sona's report includes wrong planetary assignments, an unsupported connection and a physiological claim derived from biorhythm. They remain visible in raw provenance but are excluded from the book. Other report prose has not received a complete claim-by-claim audit.

Chapter revision v3 changes existing additions in Chapters 1, 3, 6 and 7. The draft remains 13 revised and 14 retained chapters. Corv allows disagreement; Gideon waits for a tested reach; Jian shares his scanner; Sona makes a missed trace accessible for correction. See `../2026-09-08-chapter-integration/` for the exact patch and all-chapter scanner. Writer skill v2.17.0 carries the review rules.

The four frozen births and checkpoint dates are unchanged. Gene Keys label/line exclusions, sound-timing exclusions and unresolved intermediate timestamps remain. No biological measurement or facial personality judgment is introduced.

## Flow boundaries

This pass ran the substantive Selemene integrated-mode path, local source-pack creation and chain audit. It inspected the older witness-agents section/layer retrieval flow but did not run that separate graph end to end. It did not run production worker endpoints, PDF rendering, remote pattern persistence or app unlock flows. The source adapter workaround and failed embedding endpoint are recorded for future backend planning, not repaired in those repositories here.
