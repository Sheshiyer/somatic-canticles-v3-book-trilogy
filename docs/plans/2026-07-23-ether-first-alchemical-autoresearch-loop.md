# Ether-First Alchemical Autoresearch Loop Implementation Plan

> **For Codex:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a bounded Python standard-library controller that produces auditable, immutable-source Ether-First dry-run artifacts.

**Architecture:** The package receives explicit source-family paths and candidate claim records, snapshots sources into a provenance manifest, evaluates candidates under the Ether-first tagging and probe rules, then emits phase packets and run ledgers into a caller-contained artifact directory. A tiny `argparse` CLI defaults to dry-run; the controller has no network, model, filesystem-write-to-source, or dependency-manager behavior.

**Tech Stack:** Python 3.14 standard library: `argparse`, `dataclasses`, `hashlib`, `json`, `pathlib`, `unittest`, `tempfile`.

---

### Task 1: Establish the executable test contract

**Files:**
- Create: `tests/test_controller.py`
- Create: `automation/ether_first/__init__.py`
- Create: `automation/ether_first/controller.py`
- Create: `automation/ether_first/__main__.py`

**Step 1: Write failing tests for phase order and tag validation**

```python
from automation.ether_first.controller import PHASES, validate_claim_tags

self.assertEqual(PHASES, (...))
with self.assertRaises(ValueError):
    validate_claim_tags([])
```

**Step 2: Run the focused test to verify it fails**

Run: `python3 -m unittest tests.test_controller.EtherFirstUnitTests.test_phase_order`
Expected: import failure because the controller package does not exist.

**Step 3: Implement only phase and claim-tag primitives**

```python
PHASES = (...)
VALID_TAGS = frozenset({...})

def validate_claim_tags(tags):
    ...
```

**Step 4: Run focused tests to verify they pass**

Run: `python3 -m unittest tests.test_controller.EtherFirstUnitTests`
Expected: PASS for phase and tag tests.

**Step 5: Commit**

```bash
git add tests/test_controller.py automation/ether_first
git commit -m "feat: add Ether-First claim primitives"
```

### Task 2: Build provenance manifest and evaluator behavior

**Files:**
- Modify: `tests/test_controller.py`
- Modify: `automation/ether_first/controller.py`

**Step 1: Write failing tests for source-family manifest metadata**

```python
manifest = build_source_manifest(source_groups)
self.assertEqual({entry['provenance'] for entry in manifest['sources']}, expected)
self.assertTrue(all(entry['bytes'] > 0 for entry in manifest['sources']))
```

**Step 2: Run the manifest tests to verify failure**

Run: `python3 -m unittest tests.test_controller.EtherFirstUnitTests.test_manifest_records_provenance`
Expected: FAIL because `build_source_manifest` is undefined.

**Step 3: Implement stable SHA-256 identifiers and immutable metadata capture**

```python
def build_source_manifest(source_groups):
    return {'sources': [...]}
```

**Step 4: Write failing evaluator tests**

```python
result = evaluate_candidate({...})
self.assertFalse(result['accepted'])
self.assertEqual(result['findings'][0]['code'], 'CATEGORICAL-LEAK')
```

**Step 5: Implement field/ISA acceptance gates and categorical-leak finding**

```python
def evaluate_candidate(candidate):
    ...
```

**Step 6: Run the focused unit suite**

Run: `python3 -m unittest tests.test_controller.EtherFirstUnitTests`
Expected: PASS.

**Step 7: Commit**

```bash
git add tests/test_controller.py automation/ether_first/controller.py
git commit -m "feat: add provenance and claim evaluation"
```

### Task 3: Implement bounded artifact run and convergence stop

**Files:**
- Modify: `tests/test_controller.py`
- Modify: `automation/ether_first/controller.py`

**Step 1: Write failing integration tests for artifact tree and immutable inputs**

```python
report = run_loop(..., cycles=5, artifacts_root=...)
self.assertTrue((report['run_directory'] / 'manifest.json').is_file())
self.assertEqual(before_hashes, hashes(source_paths))
```

**Step 2: Run the integration test to verify failure**

Run: `python3 -m unittest tests.test_controller.EtherFirstRunTests.test_run_writes_required_artifacts`
Expected: FAIL because `run_loop` is undefined.

**Step 3: Implement output containment, ordered phase packets, ledgers, and scorecard**

```python
def run_loop(*, source_groups, candidates, cycles, artifacts_root, run_id, dry_run=True):
    ...
```

**Step 4: Write a failing stagnation test**

```python
report = run_loop(..., cycles=9, ...)
self.assertEqual(report['convergence']['stop_reason'], 'two_consecutive_stagnant_cycles')
self.assertEqual(report['convergence']['cycles_executed'], 3)
```

**Step 5: Implement monotonic score comparison and second-stagnation stop**

```python
def convergence_from_scores(scores, maximum_cycles):
    ...
```

**Step 6: Run all controller tests**

Run: `python3 -m unittest -v tests.test_controller`
Expected: PASS.

**Step 7: Commit**

```bash
git add tests/test_controller.py automation/ether_first/controller.py
git commit -m "feat: add bounded Ether-First run controller"
```

### Task 4: Expose dry-run CLI and final verification

**Files:**
- Modify: `tests/test_controller.py`
- Modify: `automation/ether_first/__main__.py`
- Modify: `ISA.md`

**Step 1: Write failing CLI parser tests**

```python
parser = build_parser()
self.assertTrue(parser.parse_args([]).dry_run)
with self.assertRaises(SystemExit):
    parser.parse_args(['--cycles', '2'])
```

**Step 2: Run CLI tests to verify failure**

Run: `python3 -m unittest tests.test_controller.EtherFirstCliTests`
Expected: FAIL because the CLI module is absent.

**Step 3: Implement `argparse` CLI with a 3–9 cycle range**

```python
def build_parser():
    ...

def main(argv=None):
    ...
```

**Step 4: Verify the complete suite and actual dry-run output**

Run:
```bash
python3 -m unittest -v
python3 -m automation.ether_first --cycles 3 --artifacts-root /var/folders/zx/_wycnwwx3p1f_4gclpnhr8rm0000gn/T/opencode/ether-first-proof
```
Expected: all tests pass; command prints a run directory under the supplied artifact root.

**Step 5: Verify source immutability and artifact containment**

Run SHA-256 snapshot before and after the actual dry run, then inspect the generated manifest and convergence report.

**Step 6: Update ISA verification evidence and Git inspection**

Run:
```bash
git status --short
git diff --check
git diff -- ISA.md docs/plans automation tests
```

**Step 7: Commit only when explicitly requested**

Do not commit unless the user explicitly asks.
