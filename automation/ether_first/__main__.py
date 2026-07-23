"""Command-line entry point for the Ether-First dry-run controller."""

import argparse
import json
from pathlib import Path

from .config import load_config
from .controller import run_loop


def cycle_count(value):
    """Parse a loop-cycle count accepted by the bounded controller."""
    cycles = int(value)
    if not 3 <= cycles <= 9:
        raise argparse.ArgumentTypeError("cycles must be between 3 and 9")
    return cycles


def build_parser():
    """Build the safe-by-default command-line parser."""
    parser = argparse.ArgumentParser(
        description="Run the bounded Ether-First alchemical autoresearch dry-run."
    )
    parser.add_argument("--cycles", type=cycle_count, default=3)
    parser.add_argument("--artifacts-root", type=Path, default=Path("artifacts"))
    parser.add_argument("--run-id", default="dry-run")
    parser.add_argument("--config", type=Path)
    parser.add_argument("--dry-run", action=argparse.BooleanOptionalAction, default=True)
    return parser


def main(argv=None):
    """Execute an empty-candidate dry run and print its artifact location."""
    arguments = build_parser().parse_args(argv)
    config = (
        load_config(arguments.config)
        if arguments.config is not None
        else {"source_groups": {}, "candidates": []}
    )
    report = run_loop(
        source_groups=config["source_groups"],
        candidates=config["candidates"],
        cycles=arguments.cycles,
        artifacts_root=arguments.artifacts_root,
        run_id=arguments.run_id,
        dry_run=arguments.dry_run,
    )
    print(json.dumps({"run_directory": str(report["run_directory"])}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
