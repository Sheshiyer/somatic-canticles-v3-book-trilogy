#!/usr/bin/env python3
"""Bounded autoresearch loop runner for v3 deeper passes.

Contract (from gating_contract.autoresearch_loop_policy):
  - 3-9 cycles; stop after 2 stagnant cycles
  - one variable per cycle
  - dry-run default; mutation requires --apply
  - every cycle records baseline metric, change, post metric, keep/discard

The runner itself never edits canon. It orchestrates:
  baseline scan -> apply ONE transform (from transforms registry) -> rescan -> keep/discard
Transform outputs land in WORKBENCH/STORYOPS/runs/<chapter-slug>/ as candidates.

Usage:
  python3 WORKBENCH/STORYOPS/scripts/autoresearch_loop.py \
      CHAPTERS/book_3/Chapter-19-The-Three-Point-Problem.md \
      --transforms dedupe --max-cycles 3 --dry-run
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RUNS = ROOT / "WORKBENCH" / "STORYOPS" / "runs"
SCANNER = ROOT / "WORKBENCH" / "STORYOPS" / "scripts" / "rubric_scan.py"

METRIC_KEYS = ["total_per_1000", "verbatim_duplicate_paragraphs", "empirical_syntax_adjacent",
               "explanatory_aside_hits"]


def scan(path: Path) -> dict:
    out = subprocess.run(
        [sys.executable, str(SCANNER), str(path), "--json"],
        capture_output=True, text=True, check=True,
    )
    return json.loads(out.stdout)


def metric_vector(report: dict) -> dict:
    return {k: report.get(k, 0) for k in METRIC_KEYS}


def is_improvement(before: dict, after: dict) -> bool:
    better = any(after[k] < before[k] for k in METRIC_KEYS)
    worse = any(after[k] > before[k] for k in METRIC_KEYS)
    return better and not worse


def transform_dedupe(text: str) -> str:
    """Remove verbatim repeated long paragraphs (keep first occurrence)."""
    paras = [p for p in re.split(r"(\n\s*\n)", text)]
    seen: set[str] = set()
    out = []
    for chunk in paras:
        norm = re.sub(r"\s+", " ", chunk.strip())
        if len(norm) >= 120 and norm in seen:
            continue
        if len(norm) >= 120:
            seen.add(norm)
        out.append(chunk)
    return "".join(out)


def transform_opacity_strip(text: str) -> str:
    """Flag (not remove) explanatory asides by wrapping them in editorial brackets."""
    for pat in [r"\bwhich means\b", r"\bin other words\b", r"\bthat is to say\b",
                r"\bsimply put\b", r"\bput simply\b"]:
        text = re.sub(pat, lambda m: f"[OPACITY-REVIEW:{m.group(0)}]", text, flags=re.IGNORECASE)
    return text


TRANSFORMS = {
    "dedupe": transform_dedupe,
    "opacity-strip": transform_opacity_strip,
}


def run_loop(chapter: Path, transforms: list[str], max_cycles: int, apply: bool) -> dict:
    slug = chapter.stem
    run_dir = RUNS / slug
    run_dir.mkdir(parents=True, exist_ok=True)

    working = chapter.read_text(encoding="utf-8")
    baseline_path = run_dir / "baseline.md"
    if not baseline_path.exists():
        baseline_path.write_text(working, encoding="utf-8")

    trace = {
        "chapter": str(chapter),
        "started": datetime.now(timezone.utc).isoformat(),
        "mode": "apply" if apply else "dry-run",
        "cycles": [],
    }

    current_text = working
    current_report = scan(chapter)
    trace["baseline_metrics"] = metric_vector(current_report)
    stagnant = 0

    cycles = transforms[:max_cycles]
    for i, name in enumerate(cycles, 1):
        if name not in TRANSFORMS:
            trace["cycles"].append({"cycle": i, "transform": name, "status": "skipped-unknown"})
            continue
        candidate_text = TRANSFORMS[name](current_text)
        candidate_path = run_dir / f"cycle-{i:02d}-{name}.candidate.md"
        candidate_path.write_text(candidate_text, encoding="utf-8")
        candidate_report = scan(candidate_path)

        before = metric_vector(current_report)
        after = metric_vector(candidate_report)
        keep = is_improvement(before, after)
        status = "keep" if keep else "discard"
        stagnant = stagnant + 1 if not keep else 0

        trace["cycles"].append({
            "cycle": i,
            "transform": name,
            "before": before,
            "after": after,
            "status": status,
            "candidate": str(candidate_path),
        })

        if keep:
            current_text = candidate_text
            current_report = candidate_report

        if stagnant >= 2:
            trace["stopped"] = f"stagnant after cycle {i}"
            break

    final_path = run_dir / "final.candidate.md"
    final_path.write_text(current_text, encoding="utf-8")
    trace["final_candidate"] = str(final_path)
    trace["final_metrics"] = metric_vector(current_report)
    trace["final_verdict"] = current_report["deterministic_verdict"]

    trace_path = run_dir / "autoresearch-trace.json"
    trace_path.write_text(json.dumps(trace, indent=2), encoding="utf-8")

    if apply and trace["final_verdict"] != "FAIL":
        shutil.copyfile(final_path, chapter)
        trace["applied"] = True
        trace_path.write_text(json.dumps(trace, indent=2), encoding="utf-8")

    return trace


def main() -> None:
    parser = argparse.ArgumentParser(description="Bounded autoresearch loop (dry-run default)")
    parser.add_argument("chapter", help="path to chapter markdown")
    parser.add_argument("--transforms", nargs="+", default=["dedupe"],
                        choices=list(TRANSFORMS) + ["dedupe"], help="ordered one-variable transforms")
    parser.add_argument("--max-cycles", type=int, default=3)
    parser.add_argument("--apply", action="store_true", help="mutate the chapter (default: dry-run)")
    args = parser.parse_args()

    max_cycles = min(max(args.max_cycles, 3), 9)
    chapter = Path(args.chapter)
    if not chapter.exists():
        parser.error(f"chapter not found: {chapter}")

    trace = run_loop(chapter, args.transforms, max_cycles, args.apply)
    kept = [c for c in trace["cycles"] if c.get("status") == "keep"]
    print(f"chapter: {chapter.name}")
    print(f"mode: {trace['mode']}  cycles: {len(trace['cycles'])}  kept: {len(kept)}")
    print(f"baseline: {trace['baseline_metrics']}")
    print(f"final:    {trace['final_metrics']}  verdict: {trace['final_verdict']}")
    print(f"trace: {RUNS / chapter.stem / 'autoresearch-trace.json'}")


if __name__ == "__main__":
    main()
