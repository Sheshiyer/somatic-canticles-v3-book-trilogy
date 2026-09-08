# Calculation provenance and exclusions

2026-09-08. Production endpoint: https://selemene.tryambakam.space. Credentials were read at runtime from the principal-authorized Claude environment, never stored in this review. Requests contain fictional calculation profiles. No manuscript text was submitted with these requests.

66 saved calculation receipts returned HTTP 200: the initial 44 plus 17 timing calculations, four birth-derived biofield calculations and one explicit Melakarta calculation. Two preliminary probes are separate files and are not counted again. Successful HTTP transport is not semantic validation. Live engine inventory and OpenAPI responses are preserved. Live health reported 3.3.1, 19 engines and six workflows; the local capabilities route returned 404 on this deployment.

## Four layers that must stay separate

1. **Canonical source:** chapter passages and existing roster traits, pinned to v3 HEAD ba74a874fdc43c00b3661d026cb865584b6daaa7.
2. **Proposed fiction:** birth dates, local times, Earth reference coordinates, session dates, archetype names, scene insertions.
3. **Returned data:** request/response JSON under engine-runs, including the actual engine version/backend metadata.
4. **Derived analysis:** pairwise gate unions and editorial correspondences. No composite endpoint was invoked and no compatible-partner score was generated.

## Findings that block unqualified prose use

- **Gene Keys lines:** the inspected source (`crates/engine-gene-keys/src/engine.rs`, lines around 123–176) loses line information through scalar HD gates and defaults to line 3. These returns cannot establish a character's actual line. Preserve the full HD activation gate.line separately.
- **Gene Keys labels:** the live response for 44 returns Distraction / Synergy / Synergy. The official [Gene Key 44 page](https://genekeys.com/gene-key-44/) gives Interference / Teamwork / Synarchy. This is a material label mismatch. The returned 49 endpoint “Restraint” also disagrees with the official [49 Rebirth page](https://genekeys.com/pulse/49-rebirth-2024/). Quarantine the returned descriptive label set for authoritative verification before prose use. Do not silently overwrite the raw receipt with corrected labels or call editorial corrections engine-generated.
- **Prompt versus structure:** Vimshottari's generic witness prose reverses the apparent period nesting in the inspected sample. Use structured Mahadasha → Antardasha → Pratyantardasha fields. Panchanga's daily-mode witness still says “born”; do not quote it as session guidance.
- **Clock mismatch:** Nadabrahman source reads `input.current_time.hour()` in UTC; Vedic-clock accepts the +330-minute offset and returns local hour 11. The current music recommendation is unsuitable as local-time evidence for that same scene.
- **Level is not achievement:** `consciousness_level` and suggested Siddhi frequency in output are service/request context, not a measured stage of a character's realization.
- **Enneagram is a lookup:** supplied existing types 9/4/5/8 were request options; the service did not discover these types from birth data.
- **Biorhythm is a calculated cycle:** results are not measured vitality, fatigue, health or prana. Transits and traditional correspondences do not establish moral conclusions or factual causation.

## Verified and bounded

The returned natal channel sets for all four charts exactly match reconstruction from their returned activated gates and the local 36-channel list. This checks internal consistency only. It does not independently validate astronomical calculations, Human Design doctrine, or predictive effectiveness. The pairwise calculation is reproducible with derive_charts.py.

The all-chapter pass scans all 27 chapter bodies and reviews selected passages for each character plus temporal/transition evidence. The matrix has 108 cells, not 108 independently complete character arcs. Shared/ensemble evidence and proposed developmental interpretations remain identified. A full prose edit and a line-by-line continuity pass remain future work.

## Later owning-repository planning handoff

Selemene: preserve gate lines; validate Gene Keys label dataset; correct daily-mode witness text and Vimshottari nesting; unify local-time semantics across clock/music; clarify deployed capability route contract. This file records findings only. No backend, infrastructure, admin, web, or mobile code was changed.
