"""Validated JSON input contract for Ether-First dry runs."""

import json
from pathlib import Path


_REQUIRED_SOURCE_FAMILIES = (
    "canon",
    "approved-blog",
    "selected-skill",
    "cross-domain-reference",
)

_REQUIRED_CANDIDATE_FIELDS = (
    "id",
    "claim",
    "tags",
    "field_grounding_passed",
    "isa_probe_passed",
)


def _require_object(value, name):
    if not isinstance(value, dict):
        raise ValueError(f"{name} must be a JSON object")
    return value


def _resolve_source_path(config_path, source_path):
    if not isinstance(source_path, str) or not source_path:
        raise ValueError("source paths must be non-empty strings")

    path = Path(source_path)
    if not path.is_absolute():
        path = config_path.parent / path
    path = path.resolve()
    if not path.is_file():
        raise ValueError(f"source path does not exist or is not a file: {path}")
    return path


def _validate_candidate(candidate, index):
    candidate = _require_object(candidate, f"candidates[{index}]")
    for field in _REQUIRED_CANDIDATE_FIELDS:
        if field not in candidate:
            raise ValueError(f"candidates[{index}] must include {field}")

    if not isinstance(candidate["id"], str) or not candidate["id"]:
        raise ValueError(f"candidates[{index}].id must be a non-empty string")
    if not isinstance(candidate["claim"], str) or not candidate["claim"]:
        raise ValueError(f"candidates[{index}].claim must be a non-empty string")
    if not isinstance(candidate["tags"], list):
        raise ValueError(f"candidates[{index}].tags must be a list")
    for field in ("field_grounding_passed", "isa_probe_passed"):
        if not isinstance(candidate[field], bool):
            raise ValueError(f"candidates[{index}].{field} must be a boolean")
    return candidate


def load_config(config_path):
    """Load source families and candidates from a validated JSON config file."""
    config_path = Path(config_path).resolve()
    try:
        payload = json.loads(config_path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise ValueError(f"config file does not exist: {config_path}") from error
    except json.JSONDecodeError as error:
        raise ValueError(f"config file must contain valid JSON: {config_path}") from error

    payload = _require_object(payload, "config")
    for field in ("source_groups", "candidates"):
        if field not in payload:
            raise ValueError(f"config must include {field}")

    source_groups = _require_object(payload["source_groups"], "source_groups")
    for family in _REQUIRED_SOURCE_FAMILIES:
        if family not in source_groups:
            raise ValueError(f"source_groups must include {family}")
    normalized_source_groups = {}
    for provenance, source_paths in source_groups.items():
        if not isinstance(provenance, str) or not provenance:
            raise ValueError("source group names must be non-empty strings")
        if not isinstance(source_paths, list):
            raise ValueError(f"source_groups.{provenance} must be a list")
        normalized_source_groups[provenance] = [
            _resolve_source_path(config_path, source_path) for source_path in source_paths
        ]

    if not isinstance(payload["candidates"], list):
        raise ValueError("candidates must be a list")
    candidates = [
        _validate_candidate(candidate, index)
        for index, candidate in enumerate(payload["candidates"])
    ]
    return {"source_groups": normalized_source_groups, "candidates": candidates}
