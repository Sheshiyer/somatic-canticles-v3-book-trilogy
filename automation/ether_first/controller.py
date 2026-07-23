"""Ether-First alchemical autoresearch loop controller."""

from hashlib import sha256
import json
from pathlib import Path


PHASES = (
    "Phase 0: Ether Axiom",
    "Nigredo",
    "Albedo",
    "Citrinitas",
    "Rubedo",
)

VALID_TAGS = frozenset(
    {
        "DERIVED-FROM-FIELD",
        "FIELD-FACET",
        "MATTER-FIRST-ARTIFACT",
    }
)


def validate_claim_tags(tags):
    """Return the sole valid claim tag or reject an invalid tag set."""
    if len(tags) != 1:
        raise ValueError("a candidate must have exactly one claim tag")

    tag = tags[0]
    if tag not in VALID_TAGS:
        raise ValueError(f"invalid claim tag: {tag}")
    return tag


def build_source_manifest(source_groups):
    """Capture immutable source metadata from explicit provenance families."""
    sources = []
    for provenance, paths in source_groups.items():
        for source_path in paths:
            path = Path(source_path)
            content = path.read_bytes()
            digest = sha256(content).hexdigest()
            sources.append(
                {
                    "id": f"sha256:{digest}",
                    "path": str(path),
                    "bytes": len(content),
                    "provenance": provenance,
                }
            )
    return {"sources": sorted(sources, key=lambda source: source["path"])}


def evaluate_candidate(candidate):
    """Evaluate a supplied candidate without generating or modifying claims."""
    tag = validate_claim_tags(candidate["tags"])
    field_grounding_passed = candidate["field_grounding_passed"]
    isa_probe_passed = candidate["isa_probe_passed"]
    findings = []

    if tag == "MATTER-FIRST-ARTIFACT":
        findings.append(
            {
                "code": "CATEGORICAL-LEAK",
                "candidate_id": candidate["id"],
                "message": "Matter-first claim contradicts Ether-first substrate.",
            }
        )

    return {
        "candidate_id": candidate["id"],
        "accepted": field_grounding_passed and isa_probe_passed and not findings,
        "field_grounding_passed": field_grounding_passed,
        "isa_probe_passed": isa_probe_passed,
        "findings": findings,
    }


def _write_json(path, payload):
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_loop(*, source_groups, candidates, cycles, artifacts_root, run_id, dry_run=True):
    """Run a bounded, dry-run-only assessment into a contained artifact directory."""
    if not 3 <= cycles <= 9:
        raise ValueError("cycles must be between 3 and 9")
    if not dry_run:
        raise ValueError("only dry-run execution is supported")

    artifacts_root = Path(artifacts_root).resolve()
    run_directory = (artifacts_root / "ether-first-loop" / run_id).resolve()
    if artifacts_root not in run_directory.parents:
        raise ValueError("run directory escapes the requested artifact root")

    phase_directory = run_directory / "phase-packets"
    phase_directory.mkdir(parents=True, exist_ok=False)

    manifest = build_source_manifest(source_groups)
    evaluations = [evaluate_candidate(candidate) for candidate in candidates]
    score = sum(evaluation["accepted"] for evaluation in evaluations)
    scorecards = []
    stagnant_cycles = 0
    previous_score = None
    for cycle in range(1, cycles + 1):
        scorecards.append({"cycle": cycle, "accepted_candidates": score})
        if previous_score is not None and score <= previous_score:
            stagnant_cycles += 1
        else:
            stagnant_cycles = 0
        previous_score = score
        if stagnant_cycles == 2:
            break

    convergence = {
        "cycles_executed": len(scorecards),
        "dry_run": dry_run,
        "stop_reason": (
            "two_consecutive_stagnant_cycles"
            if stagnant_cycles == 2
            else "cycle_limit_reached"
        ),
    }

    _write_json(run_directory / "manifest.json", manifest)
    _write_json(run_directory / "candidate-ledger.json", {"candidates": candidates})
    _write_json(run_directory / "evaluator-ledger.json", {"evaluations": evaluations})
    _write_json(run_directory / "cycle-scorecard.json", {"cycles": scorecards})
    _write_json(run_directory / "convergence-report.json", convergence)
    for position, phase in enumerate(PHASES, start=1):
        _write_json(phase_directory / f"{phase}.json", {"position": position, "phase": phase})

    return {"run_directory": run_directory, "convergence": convergence}
