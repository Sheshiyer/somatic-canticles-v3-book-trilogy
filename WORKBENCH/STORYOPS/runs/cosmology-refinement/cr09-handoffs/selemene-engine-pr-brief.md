# CR-09.01 Selemene engine PR brief

Status: bounded implementation handoff. No Selemene repo files changed.

## Goal

Repair only the paths required for optional symbolic context around the Chapter 6 situation `B1C6-shard-custody`.

## Required behavior cases

1. Facts-in-prompts: a deliberately corrupted second-subject fact must be detected or quarantined before synthesis.
2. Model provenance: every report records actual returned model/provider, not requested tier placeholders.
3. Empty retrieval: no matches, HTTP410, empty KV/Vectorize, and absent context are explicit states, not hidden fallback content.
4. Exclusions remain excluded: chart-line defects, label mismatches, local-time/sound-clock inconsistencies, and unsupported fields cannot enter reader-facing reports.
5. No family-penta/team shortcut: colleague/team readings must not reuse family or commercial relationship modes without explicit frame.

## StoryOps boundary

Engine output may ask: what layer carries cost, what contrast remains unresolved, and what action returns later? It may not decide whether the character/reader transformed, certify moral progress, or promote manuscript canon.

## Suggested tests

- Corrupt one supplied subject fact and assert synthesis refuses or flags it.
- Force empty retrieval and assert report says no retrieved context.
- Assert actual model provenance is present in generated report receipt.
- Assert unsupported fields are omitted from report payload.
