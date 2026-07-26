#!/usr/bin/env python3
"""Deterministic run-directory artifact writer for the Ether-First loop.

Artifact Contract (issue #1): every run produces one directory

    <base>/<run-id>/
        source-manifest.json        immutable, written exactly once
        phase-packets/<phase>.json  one per alchemical phase
        candidate-ledger.jsonl      append-only, one candidate per line
        evaluator-ledger.jsonl      append-only, one evaluation per line
        scorecards/cycle-<n>.json   one per loop cycle
        convergence-report.json     final machine-readable report
        convergence-report.md       final human-readable summary

run-id = UTC timestamp YYYYMMDDTHHMMSSZ + 6-char sha256 prefix of the
canonical (sorted-keys) manifest JSON, so identical manifests started in the
same second collide loudly instead of silently overwriting.

All JSON is written with indent=2, sort_keys=True for reproducibility.
This module never mutates canon; it only creates new files under <base>.
"""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_BASE = "artifacts/ether-first-loop"


def _dump_json(obj: dict, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, sort_keys=True)
        f.write("\n")


def manifest_hash(manifest: dict) -> str:
    """6-char sha256 prefix of the canonical manifest JSON (run-id suffix)."""
    canonical = json.dumps(manifest, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:6]


def new_run_dir(base: str | Path = DEFAULT_BASE, manifest: dict | None = None) -> Path:
    """Create and return <base>/<run-id>/ with contract subdirectories."""
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    suffix = manifest_hash(manifest) if manifest is not None else "000000"
    run_dir = Path(base) / f"{stamp}-{suffix}"
    run_dir.mkdir(parents=True, exist_ok=False)
    (run_dir / "phase-packets").mkdir()
    (run_dir / "scorecards").mkdir()
    return run_dir


def write_source_manifest(run_dir, manifest: dict) -> Path:
    """Write source-manifest.json exactly once; second call raises FileExistsError."""
    path = Path(run_dir) / "source-manifest.json"
    if path.exists():
        raise FileExistsError(f"source manifest already written (immutable): {path}")
    _dump_json(manifest, path)
    return path


def write_phase_packet(run_dir, phase: str, packet: dict) -> Path:
    """Write phase-packets/<phase>.json."""
    path = Path(run_dir) / "phase-packets" / f"{phase}.json"
    _dump_json(packet, path)
    return path


def _append_jsonl(run_dir, name: str, record: dict) -> Path:
    path = Path(run_dir) / name
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, sort_keys=True) + "\n")
    return path


def append_candidate(run_dir, candidate: dict) -> Path:
    """Append one candidate record to candidate-ledger.jsonl (append-only)."""
    return _append_jsonl(run_dir, "candidate-ledger.jsonl", candidate)


def append_eval(run_dir, evaluation: dict) -> Path:
    """Append one evaluation record to evaluator-ledger.jsonl (append-only)."""
    return _append_jsonl(run_dir, "evaluator-ledger.jsonl", evaluation)


def write_scorecard(run_dir, cycle: int, scorecard: dict) -> Path:
    """Write scorecards/cycle-<n>.json."""
    path = Path(run_dir) / "scorecards" / f"cycle-{cycle}.json"
    _dump_json(scorecard, path)
    return path


def write_convergence_report(run_dir, report: dict) -> Path:
    """Write convergence-report.json plus a human-readable .md summary."""
    path = Path(run_dir) / "convergence-report.json"
    _dump_json(report, path)

    lines = [
        "# Ether-First Loop — Convergence Report",
        "",
        f"- **outcome:** {report.get('outcome', 'unknown')}",
        f"- **stop_reason:** {report.get('stop_reason', 'unknown')}",
        f"- **cycles_run:** {report.get('cycles_run', 0)}",
        f"- **dry_run:** {report.get('dry_run', True)}",
        f"- **run_id:** {report.get('run_id', 'unknown')}",
        "",
        "## Phases",
        "",
    ]
    for phase in report.get("phases", []):
        lines.append(f"- `{phase}`")
    notes = report.get("notes")
    if notes:
        lines += ["", "## Notes", "", str(notes)]
    md_path = Path(run_dir) / "convergence-report.md"
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path
