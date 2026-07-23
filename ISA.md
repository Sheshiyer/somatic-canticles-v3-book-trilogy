---
task: "Build Ether-First alchemical autoresearch loop controller"
slug: ether-first-alchemical-autoresearch-loop
project: somatic-canticles-v3-book-trilogy
effort: E3
effort_source: context-override
phase: verify
progress: 40/40
mode: interactive
started: 2026-07-23T00:00:00Z
updated: 2026-07-23T00:00:00Z
---

## Problem

The trilogy repository contains canon and supporting manuscript material but no bounded, repeatable mechanism for examining proposed claims against an Ether-first ontology. Without one, future refinement can blur field-grounded claims with matter-first explanations, mutate sources accidentally, or fail to leave an auditable provenance trail.

## Vision

A maintainer can execute one dry-run command and receive a self-contained run directory that makes the loop legible: immutable source inventory, ordered alchemical phase packets, tagged candidate claims, evaluator outcomes, cycle scoring, and a convergence decision. The surprising property is that the system exposes a categorical leak as a first-class finding rather than silently normalizing it.

## Out of Scope

- No automatic edits to canon, approved material, or bibliography.
- No network retrieval, model invocation, publishing, or GitHub mutation.
- No claim of scientific validation for metaphysical premises.
- No dependency manager, third-party package, or non-stdlib runtime requirement.
- No unbounded optimization loop.

## Principles

- Ether, field, and substrate are axiomatic and primary; matter is derived or modulatory.
- Provenance precedes synthesis: every generated record names its source basis.
- A categorical mismatch is a finding, not an error to conceal.
- Dry-run output is inspectable, deterministic, and safe by default.
- Tests specify observable behavior before production implementation.

## Constraints

- Implementation uses Python 3 standard library only.
- The command defaults to dry-run and accepts only 3 through 9 cycles.
- Inputs are read-only; output is confined under `artifacts/ether-first-loop/<run-id>/`.
- Every candidate claim has exactly one of `DERIVED-FROM-FIELD`, `FIELD-FACET`, or `MATTER-FIRST-ARTIFACT`.
- Unsupported substrate claims produce explicit `CATEGORICAL-LEAK` findings.
- Canon, approved source, selected skill, and cross-domain source families appear in a manifest with identifiers, byte counts, and provenance.
- The loop stops after two consecutive stagnant cycles.

## Goal

Ship a standard-library Python controller that runs a bounded Ether-First alchemical autoresearch dry-run, generates the required auditable artifacts without mutating sources, and is covered by behavior-focused `unittest` cases for phase ordering, tagging, provenance, acceptance, stagnation, ISA probes, dry-run safety, and source immutability.

## Criteria

- [x] ISC-1: `automation/ether_first/__init__.py` makes the controller importable.
- [x] ISC-2: `automation/ether_first/controller.py` uses only Python standard-library imports.
- [x] ISC-3: `automation/ether_first/__main__.py --help` exits successfully.
- [x] ISC-4: The CLI defaults `--dry-run` to true.
- [x] ISC-5: The CLI rejects `--cycles` below 3.
- [x] ISC-6: The CLI rejects `--cycles` above 9.
- [x] ISC-7: A source manifest records a stable identifier for each selected source.
- [x] ISC-8: A source manifest records a byte count for each selected source.
- [x] ISC-9: A source manifest records provenance family for each selected source.
- [x] ISC-10: A source manifest includes canon sources.
- [x] ISC-11: A source manifest includes approved-blog sources.
- [x] ISC-12: A source manifest includes selected-skill sources.
- [x] ISC-13: A source manifest includes cross-domain reference sources.
- [x] ISC-14: The packet sequence begins with `Phase 0: Ether Axiom`.
- [x] ISC-15: The packet sequence then contains `Nigredo`.
- [x] ISC-16: The packet sequence then contains `Albedo`.
- [x] ISC-17: The packet sequence then contains `Citrinitas`.
- [x] ISC-18: The packet sequence ends with `Rubedo`.
- [x] ISC-19: A candidate accepts exactly one valid claim tag.
- [x] ISC-20: A candidate rejects zero claim tags.
- [x] ISC-21: A candidate rejects more than one claim tag.
- [x] ISC-22: An unsupported substrate claim emits a `CATEGORICAL-LEAK` finding.
- [x] ISC-23: Candidate acceptance requires a field-grounding probe pass.
- [x] ISC-24: Candidate acceptance requires an ISA probe pass.
- [x] ISC-25: A run writes one phase packet JSON file for each alchemical phase.
- [x] ISC-26: A run writes `candidate-ledger.json`.
- [x] ISC-27: A run writes `evaluator-ledger.json`.
- [x] ISC-28: A run writes `cycle-scorecard.json`.
- [x] ISC-29: A run writes `convergence-report.json`.
- [x] ISC-30: The run stops after two consecutive stagnant cycles.
- [x] ISC-31: Dry-run execution does not modify registered source file bytes.
- [x] ISC-32: Anti: no output path is created outside the requested artifact root.
- [x] ISC-33: The CLI accepts one optional JSON configuration path.
- [x] ISC-34: JSON config requires `source_groups` and `candidates` keys.
- [x] ISC-35: Relative source paths resolve from the config file directory.
- [x] ISC-36: Config loading rejects missing source files before a run.
- [x] ISC-37: Config loading rejects incomplete candidate records before a run.
- [x] ISC-38: Configured candidate records appear in the run ledger.
- [x] ISC-39: MATTER-FIRST-ARTIFACT is never accepted even when both probes pass.
- [x] ISC-40: Source groups config must declare all four canonical provenance families.

## Test Strategy

| isc | type | check | threshold | tool |
| --- | --- | --- | --- | --- |
| ISC-3 | CLI | help exit code | 0 | `python3 -m automation.ether_first --help` |
| ISC-4–6 | unit | parser behavior | boolean / `SystemExit` | `python3 -m unittest tests.test_controller` |
| ISC-7–13 | unit | manifest records source metadata and families | four families present | `python3 -m unittest tests.test_manifest` |
| ISC-14–18 | unit | phase packet order | exact ordered list | `python3 -m unittest tests.test_phases` |
| ISC-19–22 | unit | tag validation and leak finding | expected result | `python3 -m unittest tests.test_claims` |
| ISC-23–24 | unit | acceptance gate probes | both true required | `python3 -m unittest tests.test_evaluation` |
| ISC-25–29 | integration | dry-run output tree | required files exist | `python3 -m unittest tests.test_run` |
| ISC-30 | unit | stagnant cycle control | stop at second stagnation | `python3 -m unittest tests.test_convergence` |
| ISC-31 | integration | SHA-256 source snapshots | equal before and after | `python3 -m unittest tests.test_safety` |
| ISC-32 | integration | output containment | all relative paths safe | `python3 -m unittest tests.test_safety` |
| ISC-33–38 | CLI/config | JSON input validation and configured ledger | valid inputs run; invalid inputs reject | `python3 -m unittest discover -s tests -v` |
| ISC-39 | unit | matter-first rejection regardless of probes | always rejected + CATEGORICAL-LEAK | `python3 -m unittest tests.test_controller` |
| ISC-40 | unit | required source family enforcement | four families present or rejected | `python3 -m unittest tests.test_controller` |

## Features

| name | description | satisfies | depends_on | parallelizable |
| --- | --- | --- | --- | --- |
| Domain schema | Define tags, candidates, findings, and run metadata | ISC-19–24 | none | false |
| Source manifest | Inventory immutable source families with fingerprints | ISC-7–13, ISC-31 | Domain schema | false |
| Phase engine | Create ordered Ether-first phase packets | ISC-14–18, ISC-25 | Domain schema | false |
| Evaluator | Apply field and ISA probes and report leaks | ISC-22–24, ISC-27 | Domain schema | false |
| Run controller | Bound cycles, contain output, and report convergence | ISC-4–6, ISC-26–32 | all above | false |
| CLI | Expose safe dry-run controller | ISC-3–6 | Run controller | false |
| Config input | Validate source paths and candidate records from JSON | ISC-33–38 | CLI, Run controller | false |

## Decisions

- 2026-07-23: Refined: Python standard library and `unittest` are the baseline because the target repository has no executable tooling or package manifest.
- 2026-07-23: The source-family paths will be passed to the controller rather than inferred from undocumented repository conventions.
- 2026-07-23: Default candidate generation is intentionally minimal and deterministic; the controller evaluates supplied candidate records rather than synthesizing authoritative manuscript claims.
- 2026-07-23: Delegation floor is not used: the controller's sequential API and test-first implementation share tight interfaces, so parallel writers would increase integration risk.
- 2026-07-23: Real-run inputs use one validated JSON config file; relative source paths are anchored to its directory, and only existing files are admitted.
- 2026-07-23: Refined: MATTER-FIRST-ARTIFACT is categorically rejected regardless of probe results — the tag itself contradicts the Ether-first substrate. The `evaluate_candidate` function now emits CATEGORICAL-LEAK and sets `accepted=False` for any MATTER-FIRST-ARTIFACT tag, even when both boolean probes pass.
- 2026-07-23: Refined: source_groups config must declare all four canonical provenance families (canon, approved-blog, selected-skill, cross-domain-reference). Empty path lists per family are valid; missing families are rejected at config load time.
- 2026-07-23: Infrastructure inventory: the nearby Somatic-Canticles-Webapp wrangler.toml has a placeholder D1 binding (`database_id: "your-database-id-here"`) and a commented-out KV namespace. No active Cloudflare KV namespace, Vectorize index, embedding model, Worker binding, or ingestion/retrieval service exists. Retrieval integration is deferred to a separate scoped feature.

## Changelog

- conjectured: The repository already supplied an executable automation convention.
  refuted by: Repository inspection found only Markdown manuscript files and no package or test configuration.
  learned: The controller needs an explicit minimal Python standard-library foundation.
  criterion now: ISC-1 through ISC-6 define the executable baseline.

## Verification

- ISC-1–2: import and `python3 -m compileall -q automation tests` exited 0.
- ISC-3: `python3 -m automation.ether_first --help` exited 0 and rendered parser help.
- ISC-4–6: `python3 -m unittest discover -s tests -v` passed parser defaults and both rejected cycle bounds; direct invalid CLI invocation exited 2.
- ISC-7–13: manifest provenance test passed for canon, approved-blog, selected-skill, and cross-domain-reference fixture sources.
- ISC-14–24: phase, tag validation, categorical-leak, and acceptance-probe tests passed in the 11-test discovery suite.
- ISC-25–29: dry run under `/var/folders/zx/_wycnwwx3p1f_4gclpnhr8rm0000gn/T/opencode/ether-first-proof/ether-first-loop/verification-proof` reported all required artifacts and five phase packets.
- ISC-30: dry run convergence report returned `two_consecutive_stagnant_cycles` after 3 cycles.
- ISC-31–32: SHA-256 source snapshot check reported `source_unchanged= True` and `contained= True`.
- ISC-33–38: `python3 -m unittest discover -s tests -v` passed 18 tests, including malformed JSON, missing keys/files, incomplete candidates, relative-path normalization, and CLI-configured ledger coverage.
- Configured dry run: `python3 -m automation.ether_first --config /var/folders/zx/_wycnwwx3p1f_4gclpnhr8rm0000gn/T/opencode/ether-first-config.json --artifacts-root /var/folders/zx/_wycnwwx3p1f_4gclpnhr8rm0000gn/T/opencode/ether-first-configured-proof --run-id configured-proof --cycles 3` wrote a contained manifest, accepted one field facet, emitted `CATEGORICAL-LEAK` for the unsupported matter-first candidate, and stopped after 3 stagnant cycles.
- ISC-39: `python3 -m unittest tests.test_controller.EtherFirstUnitTests.test_matter_first_artifact_never_accepted_even_with_both_probes` — MATTER-FIRST-ARTIFACT with both probes True returned `accepted=False` and `findings[0].code == "CATEGORICAL-LEAK"`.
- ISC-40: `python3 -m unittest tests.test_controller.EtherFirstConfigTests.test_load_config_rejects_missing_required_source_family` — config with only `canon` raised `ValueError("source_groups must include approved-blog")`; full 20-test suite passed.
