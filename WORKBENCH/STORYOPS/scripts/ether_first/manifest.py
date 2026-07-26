#!/usr/bin/env python3
"""Source manifest builder + validator for the Ether-First loop.

A manifest is the immutable record of exactly which source bytes a run
operated on: every canon/blog/skill/reference file, its sha256, byte length,
and role. The artifact writer (artifacts.py) pins the manifest into the run
directory before any phase runs, so every downstream ledger entry is
traceable to hashed inputs.

Roles:
  canon     - CHAPTERS/ manuscript files (never mutated by the controller)
  blog      - published blog/post sources used as evidence
  skill     - skill / rubric / contract definition files
  reference - any other reference material

Usage:
  python3 manifest.py build --out manifest.json \
      --canon CHAPTERS/book_1/*.md [--blog ...] [--skill ...] [--reference ...]
  python3 manifest.py validate manifest.json
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import json
import sys
from pathlib import Path

VALID_ROLES = ("canon", "blog", "skill", "reference")


def _hash_file(path: Path) -> tuple[str, int]:
    """Return (sha256 hex digest, byte length) for a file. Raises FileNotFoundError."""
    if not path.is_file():
        raise FileNotFoundError(f"manifest source not found: {path}")
    h = hashlib.sha256()
    data = path.read_bytes()
    h.update(data)
    return h.hexdigest(), len(data)


def build_manifest(paths: list[tuple[str, str]], version: str) -> dict:
    """Build a manifest dict from (path, role) pairs.

    Hashes each file's bytes and records byte length. Raises FileNotFoundError
    naming the first missing path; raises ValueError on an invalid role.
    """
    entries = []
    for path_str, role in paths:
        if role not in VALID_ROLES:
            raise ValueError(f"invalid role {role!r} for {path_str}; valid: {VALID_ROLES}")
        p = Path(path_str)
        digest, size = _hash_file(p)
        entries.append({
            "path": str(p),
            "sha256": digest,
            "bytes": size,
            "role": role,
            "bytes_recorded": True,
        })
    return {
        "version": version,
        "entries": entries,
        "entry_count": len(entries),
    }


def validate_manifest(m: dict) -> None:
    """Raise ValueError unless the manifest is well-formed and complete."""
    if not isinstance(m, dict):
        raise ValueError("manifest is not a JSON object")
    if not m.get("version"):
        raise ValueError("manifest missing 'version'")
    entries = m.get("entries")
    if not isinstance(entries, list) or len(entries) < 1:
        raise ValueError("manifest must contain at least 1 entry")
    for i, e in enumerate(entries):
        if not isinstance(e, dict):
            raise ValueError(f"entry {i} is not an object")
        for key in ("path", "sha256", "role"):
            if not e.get(key):
                raise ValueError(f"entry {i} missing {key!r}")
        if e.get("role") not in VALID_ROLES:
            raise ValueError(f"entry {i} has invalid role {e.get('role')!r}")
        if e.get("bytes_recorded") is not True:
            raise ValueError(f"entry {i} ({e.get('path')}) does not have bytes_recorded=True")


def load_manifest(path) -> dict:
    """Load a manifest JSON file."""
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save_manifest(m: dict, path) -> None:
    """Write a manifest JSON file deterministically."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(m, f, indent=2, sort_keys=True)
        f.write("\n")


def _collect(patterns: list[str]) -> list[str]:
    """Expand glob patterns (argparse already expands shell globs on most shells;
    this covers quoted patterns and Windows-style invocation)."""
    out: list[str] = []
    for pat in patterns or []:
        expanded = sorted(glob.glob(pat))
        out.extend(expanded if expanded else [pat])
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description="Ether-First source manifest tool")
    sub = parser.add_subparsers(dest="command", required=True)

    b = sub.add_parser("build", help="build a manifest from source files")
    b.add_argument("--out", required=True, help="output manifest JSON path")
    b.add_argument("--version", default="ether-first-manifest-v1")
    for role in VALID_ROLES:
        b.add_argument(f"--{role}", nargs="*", default=[], help=f"{role} source files/globs")

    v = sub.add_parser("validate", help="validate a manifest JSON file")
    v.add_argument("manifest", help="manifest JSON path")

    args = parser.parse_args()

    if args.command == "build":
        pairs: list[tuple[str, str]] = []
        for role in VALID_ROLES:
            for p in _collect(getattr(args, role)):
                pairs.append((p, role))
        try:
            manifest = build_manifest(pairs, args.version)
            validate_manifest(manifest)
        except (FileNotFoundError, ValueError) as e:
            print(f"error: {e}", file=sys.stderr)
            sys.exit(1)
        save_manifest(manifest, args.out)
        print(f"manifest: {args.out} ({manifest['entry_count']} entries, version {manifest['version']})")
    else:
        try:
            m = load_manifest(args.manifest)
            validate_manifest(m)
        except FileNotFoundError:
            print(f"error: manifest not found: {args.manifest}", file=sys.stderr)
            sys.exit(1)
        except (json.JSONDecodeError, ValueError) as e:
            print(f"INVALID: {e}", file=sys.stderr)
            sys.exit(1)
        print(f"VALID: {args.manifest} ({len(m['entries'])} entries, version {m['version']})")


if __name__ == "__main__":
    main()
