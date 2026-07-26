#!/usr/bin/env python3
"""Ether-First Alchemical Autoresearch Loop controller (issue #1, Phase 1 skeleton).

Dry-run-first CLI skeleton. Walks the alchemical phases in strict order
(ETHER_AXIOM -> NIGREDO -> ALBEDO -> CITRINITAS -> RUBEDO), emitting stub
PhasePackets, per-cycle scorecards, and a convergence report. The skeleton
always defers: no candidates are accepted until real phase logic lands.

CANON SAFETY: this controller NEVER mutates canon. There is intentionally no
--canon-write (or similar) flag; --apply only flips a recorded flag in the
convergence report. Do not add canon-mutation flags here — candidate text
lives in the run directory and canon promotion is a separate gated process
(see gating_contract.stage_acceptance).

Usage:
  python3 WORKBENCH/STORYOPS/scripts/ether_first_loop.py \
      --manifest manifest.json [--cycles N] [--apply] [--base DIR]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from ether_first import artifacts, manifest as manifest_mod

# Sibling modules (schemas.py, phases.py) are being built concurrently by
# other agents. Import defensively and use them only when present; this
# skeleton must run standalone without them.
try:
    from ether_first import phases, schemas
except ImportError:
    phases = schemas = None

ROOT = Path(__file__).resolve().parents[3]

MIN_CYCLES, MAX_CYCLES = 3, 9
STAGNATION_STOP = 2

PHASE_ORDER = ["ETHER_AXIOM", "NIGREDO", "ALBEDO", "CITRINITAS", "RUBEDO"]

PHASE_INTENT = {
    "ETHER_AXIOM": "Fix the ether-first axiom set: source-of-truth ordering (field before matter) that every later phase's claims and findings are checked against.",
    "NIGREDO": "Detect contradictions, categorical leaks, and matter-first artifacts across the manifested sources; emit findings, never silently repair.",
    "ALBEDO": "Cleanse and normalize evidence: canonicalize claims, strip preamble residue, enforce epistemic grammar (HOUSE-MODEL never wears empirical syntax).",
    "CITRINITAS": "Synthesize field-grounded candidates from normalized evidence; one variable per candidate, each traceable to hashed sources.",
    "RUBEDO": "Accept/reject/defer candidates against the rubric and write the convergence report; skeleton always defers.",
}


def clamp_cycles(n: int) -> int:
    """Clamp to the autoresearch_loop_policy band (3-9 cycles)."""
    return min(max(n, MIN_CYCLES), MAX_CYCLES)


def phase_names() -> list[str]:
    """Phase names in strict order, preferring the sibling phases module."""
    if phases is not None and hasattr(phases, "Phase"):
        return [p.name for p in phases.Phase]
    return list(PHASE_ORDER)


def stub_packet(phase: str) -> dict:
    """Stub PhasePacket: empty claims/findings/candidates plus intent text."""
    return {
        "phase": phase,
        "stub": True,
        "description": PHASE_INTENT.get(phase, ""),
        "claims": [],
        "findings": [],
        "candidates": [],
    }


def cycle_scorecard(cycle: int, dry_run: bool) -> dict:
    """Stub CycleScorecard for one cycle (no improvements yet)."""
    return {
        "cycle": cycle,
        "stub": True,
        "dry_run": dry_run,
        "candidates_proposed": 0,
        "candidates_kept": 0,
        "candidates_discarded": 0,
        "improvement": False,
    }


def run(manifest: dict, cycles: int, apply: bool, base: str) -> Path:
    """Execute the skeleton loop; return the run directory path."""
    run_dir = artifacts.new_run_dir(base, manifest)
    artifacts.write_source_manifest(run_dir, manifest)

    names = phase_names()
    for phase in names:
        artifacts.write_phase_packet(run_dir, phase, stub_packet(phase))

    stagnant = 0
    cycles_run = 0
    stop_reason = "cycle budget exhausted"

    for cycle in range(1, cycles + 1):
        scorecard = cycle_scorecard(cycle, dry_run=not apply)
        artifacts.write_scorecard(run_dir, cycle, scorecard)
        cycles_run = cycle
        stagnant = stagnant + 1 if not scorecard["improvement"] else 0
        if stagnant >= STAGNATION_STOP:
            stop_reason = f"stagnation: {STAGNATION_STOP} consecutive cycles without improvement"
            break

    report = {
        "run_id": run_dir.name,
        "outcome": "deferred",
        "stop_reason": stop_reason,
        "cycles_run": cycles_run,
        "dry_run": not apply,
        "phases": names,
        "manifest_version": manifest.get("version"),
        "manifest_entries": len(manifest.get("entries", [])),
        "notes": "Phase 1 skeleton: all packets and scorecards are stubs; "
                 "outcome is always deferred. --apply only records intent; "
                 "the controller never mutates canon.",
    }
    artifacts.write_convergence_report(run_dir, report)
    return run_dir


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Ether-First Alchemical Autoresearch Loop (dry-run default)")
    parser.add_argument("--manifest", required=True, help="source manifest JSON")
    parser.add_argument("--cycles", type=int, default=3, help="cycle budget (clamped to 3-9)")
    parser.add_argument("--apply", action="store_true",
                        help="record applied intent in the report (default: dry-run; "
                             "never mutates canon by design)")
    parser.add_argument("--base", default=str(ROOT / "artifacts" / "ether-first-loop"),
                        help="artifact base directory")
    args = parser.parse_args()

    cycles = clamp_cycles(args.cycles)

    try:
        m = manifest_mod.load_manifest(args.manifest)
    except FileNotFoundError:
        parser.error(f"manifest not found: {args.manifest}")
    try:
        manifest_mod.validate_manifest(m)
    except ValueError as e:
        parser.error(f"invalid manifest: {e}")

    run_dir = run(m, cycles, args.apply, args.base)
    report = manifest_mod.load_manifest(run_dir / "convergence-report.json")
    print(f"mode: {'apply' if args.apply else 'dry-run'}  "
          f"cycles_run: {report['cycles_run']}  outcome: {report['outcome']}")
    print(f"stop_reason: {report['stop_reason']}")
    print(f"run dir: {run_dir}")


if __name__ == "__main__":
    main()
