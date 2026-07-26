#!/usr/bin/env python3
"""Ether-First Alchemical Autoresearch Loop controller (issue #1, Phase 2).

Dry-run-first CLI. Walks the alchemical phases in strict order
(ETHER_AXIOM -> NIGREDO -> ALBEDO -> CITRINITAS -> RUBEDO). NIGREDO and
ALBEDO run real detection/extraction when their sibling modules
(ether_first/nigredo.py, ether_first/albedo.py) are present, and fall back
to stub packets otherwise. CITRINITAS and RUBEDO remain Phase 3 stubs that
will consume the ALBEDO candidate ledger. The loop always defers: no
candidates are accepted until RUBEDO lands.

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
import re
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

# Phase 2 sibling phase modules (nigredo.py, albedo.py) are being written
# concurrently. When absent, each phase falls back to stub behavior.
try:
    from ether_first import nigredo, albedo
except ImportError:
    nigredo = albedo = None

ROOT = Path(__file__).resolve().parents[3]

MIN_CYCLES, MAX_CYCLES = 3, 9
STAGNATION_STOP = 2

PHASE_ORDER = ["ETHER_AXIOM", "NIGREDO", "ALBEDO", "CITRINITAS", "RUBEDO"]

PHASE_INTENT = {
    "ETHER_AXIOM": "Fix the ether-first axiom set: source-of-truth ordering (field before matter) that every later phase's claims and findings are checked against.",
    "NIGREDO": "Detect contradictions, categorical leaks, and matter-first artifacts across the manifested sources; emit findings, never silently repair.",
    "ALBEDO": "Cleanse and normalize evidence: canonicalize claims, strip preamble residue, enforce epistemic grammar (HOUSE-MODEL never wears empirical syntax).",
    "CITRINITAS": "Synthesize field-grounded candidates from normalized evidence; one variable per candidate, each traceable to hashed sources. Phase 3 stub: will consume the ALBEDO candidate ledger.",
    "RUBEDO": "Accept/reject/defer candidates against the rubric and write the convergence report; skeleton always defers. Phase 3 stub: will consume the ALBEDO candidate ledger.",
}

ETHER_FIRST_VOCAB = {
    "field", "substrate", "ether", "coherence", "witness", "resonance",
    "consciousness", "awareness", "pattern", "modulation", "field-grounded",
}

STOPWORDS = {
    "about", "after", "before", "being", "chapter", "could", "every",
    "first", "their", "there", "these", "those", "under", "where",
    "which", "while", "would", "part", "with", "from", "into", "this",
    "that", "they", "them", "then", "than", "when", "what", "have",
    "been", "were", "will", "shall", "upon", "over", "such", "only",
    "some", "more", "most", "also", "very", "just", "like", "book",
}

SOURCE_READ_ROLES = {"canon", "blog"}
MAX_SOURCE_BYTES = 2 * 1024 * 1024
MAX_FINDINGS_PER_FILE = 50
MAX_CLAIMS_PER_FILE = 100


def derive_manifest_terms(manifest: dict) -> set:
    """Derive the manifest vocabulary from source file stems plus the
    curated Ether-First vocabulary. Significant terms: len >= 5, alphabetic,
    not in the stopword set. Terms are lowercased."""
    terms = set(ETHER_FIRST_VOCAB)
    for entry in manifest.get("entries", []):
        stem = Path(entry.get("path", "")).stem
        for token in re.split(r"[^A-Za-z]+", stem):
            token = token.lower()
            if len(token) >= 5 and token.isalpha() and token not in STOPWORDS:
                terms.add(token)
    return terms


def _read_source_text(path_str: str) -> str | None:
    """Read source file text; skip files > 2MB or unreadable/missing files."""
    path = Path(path_str)
    try:
        if not path.is_file() or path.stat().st_size > MAX_SOURCE_BYTES:
            return None
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None


def _source_entries(manifest: dict) -> list[dict]:
    """Manifest entries whose role is canon or blog, in manifest order."""
    return [
        e for e in manifest.get("entries", [])
        if e.get("role") in SOURCE_READ_ROLES
    ]


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


def run_nigredo_phase(manifest: dict, manifest_terms: set, run_dir: Path) -> dict:
    """Real NIGREDO packet: run the nigredo detector over canon/blog sources.

    Findings per file are capped at MAX_FINDINGS_PER_FILE (first 50 in
    document order — deterministic). Every finding is also appended to the
    evaluator ledger with phase='NIGREDO'.
    """
    packet = {
        "phase": "NIGREDO",
        "stub": False,
        "description": PHASE_INTENT["NIGREDO"],
        "claims": [],
        "findings": [],
        "candidates": [],
    }
    for entry in _source_entries(manifest):
        text = _read_source_text(entry.get("path", ""))
        if text is None:
            continue
        findings = nigredo.run_nigredo(text, manifest_terms)[:MAX_FINDINGS_PER_FILE]
        for finding in findings:
            record = dict(finding)
            record.setdefault("phase", "NIGREDO")
            record["source"] = entry.get("path", "")
            packet["findings"].append(record)
            artifacts.append_eval(run_dir, {
                "phase": "NIGREDO",
                "source": entry.get("path", ""),
                "kind": record.get("kind"),
                "detail": record.get("detail"),
            })
    return packet


def run_albedo_phase(manifest: dict, manifest_terms: set, run_dir: Path) -> dict:
    """Real ALBEDO packet: build, dedupe, and tag claims over canon/blog
    sources. Claims per file are capped at MAX_CLAIMS_PER_FILE. Every claim
    is also appended to the candidate ledger with phase='ALBEDO'.
    """
    packet = {
        "phase": "ALBEDO",
        "stub": False,
        "description": PHASE_INTENT["ALBEDO"],
        "claims": [],
        "findings": [],
        "candidates": [],
    }
    for entry in _source_entries(manifest):
        text = _read_source_text(entry.get("path", ""))
        if text is None:
            continue
        claims = albedo.build_claims(text, manifest_terms)
        claims = albedo.dedupe_claims(claims)[:MAX_CLAIMS_PER_FILE]
        for claim in claims:
            record = dict(claim)
            record.setdefault("phase", "ALBEDO")
            record["source"] = entry.get("path", "")
            packet["claims"].append(record)
            artifacts.append_candidate(run_dir, {
                "phase": "ALBEDO",
                "source": entry.get("path", ""),
                "statement": record.get("statement"),
                "tag": record.get("tag"),
                "provenance": record.get("provenance", []),
            })
    return packet


def _ledger_line_count(run_dir: Path, name: str) -> int:
    path = Path(run_dir) / name
    if not path.exists():
        return 0
    with open(path, encoding="utf-8") as f:
        return sum(1 for line in f if line.strip())


def cycle_scorecard(cycle: int, dry_run: bool, candidates: int,
                    findings: int, improvement: bool) -> dict:
    """CycleScorecard with real cycle metrics from the ledgers."""
    return {
        "cycle": cycle,
        "stub": False,
        "dry_run": dry_run,
        "candidates_proposed": candidates,
        "candidates_kept": 0,
        "candidates_discarded": 0,
        "findings_emitted": findings,
        "improvement": improvement,
    }


def run(manifest: dict, cycles: int, apply: bool, base: str) -> Path:
    """Execute the skeleton loop; return the run directory path."""
    run_dir = artifacts.new_run_dir(base, manifest)
    artifacts.write_source_manifest(run_dir, manifest)

    manifest_terms = derive_manifest_terms(manifest)

    names = phase_names()
    nigredo_findings = 0
    albedo_candidates = 0
    for phase in names:
        if phase == "NIGREDO" and nigredo is not None:
            packet = run_nigredo_phase(manifest, manifest_terms, run_dir)
            nigredo_findings = len(packet["findings"])
        elif phase == "ALBEDO" and albedo is not None:
            packet = run_albedo_phase(manifest, manifest_terms, run_dir)
            albedo_candidates = len(packet["claims"])
        else:
            packet = stub_packet(phase)
        artifacts.write_phase_packet(run_dir, phase, packet)

    stagnant = 0
    cycles_run = 0
    stop_reason = "cycle budget exhausted"
    prev_activity = 0

    for cycle in range(1, cycles + 1):
        candidates = _ledger_line_count(run_dir, "candidate-ledger.jsonl")
        findings = _ledger_line_count(run_dir, "evaluator-ledger.jsonl")
        activity = candidates + findings
        improvement = activity > prev_activity
        scorecard = cycle_scorecard(cycle, dry_run=not apply,
                                    candidates=candidates, findings=findings,
                                    improvement=improvement)
        artifacts.write_scorecard(run_dir, cycle, scorecard)
        cycles_run = cycle
        prev_activity = activity
        stagnant = stagnant + 1 if not improvement else 0
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
        "nigredo_findings": nigredo_findings,
        "albedo_candidates": albedo_candidates,
        "modules_loaded": {
            "nigredo": nigredo is not None,
            "albedo": albedo is not None,
        },
        "notes": "Phase 2: NIGREDO/ALBEDO run real detection/extraction when "
                 "their modules are present, else fall back to stubs. "
                 "CITRINITAS/RUBEDO remain Phase 3 stubs and will consume the "
                 "ALBEDO candidate ledger. Outcome is always deferred; "
                 "--apply only records intent; the controller never mutates canon.",
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
