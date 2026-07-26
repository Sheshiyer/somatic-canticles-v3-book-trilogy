"""Machine-readable schemas for the Ether-First Alchemical Autoresearch Loop.

Stdlib only. Every schema is a dataclass with validate() (fail-fast ValueError),
to_dict()/from_dict() (JSON-lossless round-trip), and precise error messages.
Three hard gates: source bytes recorded + hashed; exactly one ClaimTag per claim;
MATTER-FIRST-ARTIFACT claims quarantined unless under_investigation=True.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional, Set


class SourceRole(str, Enum):
    CANON = "canon"
    BLOG = "blog"
    SKILL = "skill"
    REFERENCE = "reference"


class ClaimTag(str, Enum):
    DERIVED_FROM_FIELD = "DERIVED-FROM-FIELD"
    FIELD_FACET = "FIELD-FACET"
    MATTER_FIRST_ARTIFACT = "MATTER-FIRST-ARTIFACT"


class FindingKind(str, Enum):
    CATEGORICAL_LEAK = "CATEGORICAL-LEAK"
    MATTER_FIRST_FRAMING = "MATTER-FIRST-FRAMING"
    UNSUPPORTED_CLAIM = "UNSUPPORTED-CLAIM"


class ConvergenceOutcome(str, Enum):
    CONVERGED = "converged"
    DEFERRED = "deferred"
    STOPPED = "stopped"


def _coerce_enum(enum_cls, value, field_name: str):
    """Return enum_cls member for value; raise ValueError naming the bad input.

    Accepts an existing member or its value string. Anything else — None,
    collections, unknown strings — is rejected, never silently coerced.
    """
    if isinstance(value, enum_cls):
        return value
    if value is None:
        raise ValueError(f"{field_name} is None — expected one of {[m.value for m in enum_cls]}")
    if isinstance(value, (list, tuple, set)):
        raise ValueError(
            f"{field_name} carries multiple values {sorted(map(str, value))} — exactly one {enum_cls.__name__} required"
        )
    try:
        return enum_cls(value)
    except (ValueError, KeyError):
        raise ValueError(
            f"{field_name} has invalid value {value!r} — expected one of {[m.value for m in enum_cls]}"
        ) from None


def sha256_of_file(path: str, chunk_size: int = 1 << 16) -> str:
    """Stream a file and return its hex sha256 digest."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        while True:
            chunk = handle.read(chunk_size)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def _require_non_empty(value: str, field_name: str, owner: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{owner}.{field_name} must be a non-empty string, got {value!r}")
    return value


@dataclass
class SourceEntry:
    path: str
    sha256: str
    role: SourceRole
    bytes_recorded: bool
    entry_id: str = ""

    def __post_init__(self) -> None:
        self.role = _coerce_enum(SourceRole, self.role, "SourceEntry.role")
        if not self.entry_id:
            self.entry_id = self.path.replace("\\", "/").rsplit("/", 1)[-1] if isinstance(self.path, str) else ""

    def validate(self) -> None:
        _require_non_empty(self.path, "path", "SourceEntry")
        if not isinstance(self.sha256, str) or len(self.sha256) != 64 or any(
            c not in "0123456789abcdefABCDEF" for c in self.sha256
        ):
            raise ValueError(
                f"SourceEntry.sha256 must be a 64-char hex digest, got {self.sha256!r} (path {self.path!r})"
            )
        if self.bytes_recorded is not True:
            raise ValueError(
                f"SourceEntry.bytes_recorded is {self.bytes_recorded!r} for path {self.path!r} — "
                "run cannot proceed: source bytes must be recorded before validation"
            )
        _require_non_empty(self.entry_id, "entry_id", "SourceEntry")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "path": self.path,
            "sha256": self.sha256,
            "role": self.role.value,
            "bytes_recorded": self.bytes_recorded,
            "entry_id": self.entry_id,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "SourceEntry":
        return cls(
            path=data["path"],
            sha256=data["sha256"],
            role=_coerce_enum(SourceRole, data["role"], "SourceEntry.role"),
            bytes_recorded=data["bytes_recorded"],
            entry_id=data.get("entry_id", ""),
        )


@dataclass
class SourceManifest:
    version: int
    entries: List[SourceEntry] = field(default_factory=list)

    def validate(self) -> None:
        if not isinstance(self.version, int) or self.version < 1:
            raise ValueError(f"SourceManifest.version must be an int >= 1, got {self.version!r}")
        seen: Set[str] = set()
        for entry in self.entries:
            entry.validate()
            if entry.entry_id in seen:
                raise ValueError(
                    f"SourceManifest has duplicate entry_id {entry.entry_id!r} (path {entry.path!r})"
                )
            seen.add(entry.entry_id)

    def entry_ids(self) -> Set[str]:
        return {e.entry_id for e in self.entries}

    def find(self, entry_id: str) -> Optional[SourceEntry]:
        for entry in self.entries:
            if entry.entry_id == entry_id:
                return entry
        return None

    def to_dict(self) -> Dict[str, Any]:
        return {"version": self.version, "entries": [e.to_dict() for e in self.entries]}

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "SourceManifest":
        return cls(
            version=data["version"],
            entries=[SourceEntry.from_dict(e) for e in data["entries"]],
        )


@dataclass
class Claim:
    statement: str
    tag: Optional[ClaimTag]
    provenance: List[str] = field(default_factory=list)
    under_investigation: bool = False

    def validate(self) -> None:
        _require_non_empty(self.statement, "statement", "Claim")
        if self.tag is None:
            raise ValueError(
                "Claim has no ClaimTag: every claim must carry exactly one of "
                "DERIVED-FROM-FIELD | FIELD-FACET | MATTER-FIRST-ARTIFACT "
                f"(statement {self.statement!r})"
            )
        self.tag = _coerce_enum(ClaimTag, self.tag, "Claim.tag")
        if self.tag is ClaimTag.MATTER_FIRST_ARTIFACT and not self.under_investigation:
            raise ValueError(
                f"MATTER-FIRST-ARTIFACT claim {self.statement!r} is only valid when "
                "explicitly flagged under_investigation=True"
            )
        for pid in self.provenance:
            if not isinstance(pid, str) or not pid:
                raise ValueError(f"Claim.provenance contains invalid entry id {pid!r}")

    def to_dict(self) -> Dict[str, Any]:
        tag = _coerce_enum(ClaimTag, self.tag, "Claim.tag") if self.tag is not None else None
        return {
            "statement": self.statement,
            "tag": tag.value if tag is not None else None,
            "provenance": list(self.provenance),
            "under_investigation": self.under_investigation,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Claim":
        raw_tag = data.get("tag")
        return cls(
            statement=data["statement"],
            tag=_coerce_enum(ClaimTag, raw_tag, "Claim.tag") if raw_tag is not None else None,
            provenance=list(data.get("provenance", [])),
            under_investigation=data.get("under_investigation", False),
        )


@dataclass
class Candidate:
    statement: str
    tag: ClaimTag
    phase_origin: str

    def validate(self) -> None:
        _require_non_empty(self.statement, "statement", "Candidate")
        self.tag = _coerce_enum(ClaimTag, self.tag, "Candidate.tag")
        _require_non_empty(self.phase_origin, "phase_origin", "Candidate")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "statement": self.statement,
            "tag": _coerce_enum(ClaimTag, self.tag, "Candidate.tag").value,
            "phase_origin": self.phase_origin,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Candidate":
        return cls(
            statement=data["statement"],
            tag=_coerce_enum(ClaimTag, data["tag"], "Candidate.tag"),
            phase_origin=data["phase_origin"],
        )


@dataclass
class Finding:
    kind: FindingKind
    detail: str
    phase: str

    def validate(self) -> None:
        self.kind = _coerce_enum(FindingKind, self.kind, "Finding.kind")
        _require_non_empty(self.detail, "detail", "Finding")
        _require_non_empty(self.phase, "phase", "Finding")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "kind": _coerce_enum(FindingKind, self.kind, "Finding.kind").value,
            "detail": self.detail,
            "phase": self.phase,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Finding":
        return cls(
            kind=_coerce_enum(FindingKind, data["kind"], "Finding.kind"),
            detail=data["detail"],
            phase=data["phase"],
        )


@dataclass
class PhasePacket:
    phase: str
    claims: List[Claim] = field(default_factory=list)
    findings: List[Finding] = field(default_factory=list)
    candidates: List[Candidate] = field(default_factory=list)

    def validate(self) -> None:
        _require_non_empty(self.phase, "phase", "PhasePacket")
        for claim in self.claims:
            claim.validate()
        for finding in self.findings:
            finding.validate()
        for candidate in self.candidates:
            candidate.validate()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "phase": self.phase,
            "claims": [c.to_dict() for c in self.claims],
            "findings": [f.to_dict() for f in self.findings],
            "candidates": [c.to_dict() for c in self.candidates],
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PhasePacket":
        return cls(
            phase=data["phase"],
            claims=[Claim.from_dict(c) for c in data.get("claims", [])],
            findings=[Finding.from_dict(f) for f in data.get("findings", [])],
            candidates=[Candidate.from_dict(c) for c in data.get("candidates", [])],
        )


@dataclass
class CycleScorecard:
    cycle: int
    kept: int
    rejected: int
    deferred: int
    stagnant_flag: bool

    def validate(self) -> None:
        if not isinstance(self.cycle, int) or self.cycle < 0:
            raise ValueError(f"CycleScorecard.cycle must be an int >= 0, got {self.cycle!r}")
        for name in ("kept", "rejected", "deferred"):
            value = getattr(self, name)
            if not isinstance(value, int) or value < 0:
                raise ValueError(f"CycleScorecard.{name} must be an int >= 0, got {value!r}")
        if not isinstance(self.stagnant_flag, bool):
            raise ValueError(f"CycleScorecard.stagnant_flag must be bool, got {self.stagnant_flag!r}")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "cycle": self.cycle,
            "kept": self.kept,
            "rejected": self.rejected,
            "deferred": self.deferred,
            "stagnant_flag": self.stagnant_flag,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CycleScorecard":
        return cls(
            cycle=data["cycle"],
            kept=data["kept"],
            rejected=data["rejected"],
            deferred=data["deferred"],
            stagnant_flag=data["stagnant_flag"],
        )


@dataclass
class ConvergenceReport:
    outcome: ConvergenceOutcome
    stop_reason: str
    cycles_run: int

    def validate(self) -> None:
        self.outcome = _coerce_enum(ConvergenceOutcome, self.outcome, "ConvergenceReport.outcome")
        _require_non_empty(self.stop_reason, "stop_reason", "ConvergenceReport")
        if not isinstance(self.cycles_run, int) or self.cycles_run < 0:
            raise ValueError(f"ConvergenceReport.cycles_run must be an int >= 0, got {self.cycles_run!r}")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "outcome": _coerce_enum(ConvergenceOutcome, self.outcome, "ConvergenceReport.outcome").value,
            "stop_reason": self.stop_reason,
            "cycles_run": self.cycles_run,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ConvergenceReport":
        return cls(
            outcome=_coerce_enum(ConvergenceOutcome, data["outcome"], "ConvergenceReport.outcome"),
            stop_reason=data["stop_reason"],
            cycles_run=data["cycles_run"],
        )


def validate_manifest(manifest: SourceManifest) -> None:
    """Gate: a run cannot proceed unless every entry is hashed and byte-recorded."""
    if not isinstance(manifest, SourceManifest):
        raise ValueError(f"validate_manifest expects SourceManifest, got {type(manifest).__name__}")
    try:
        manifest.validate()
    except ValueError as exc:
        raise ValueError(f"SourceManifest: {exc}") from None


def validate_claim(claim: Claim, manifest: Optional[SourceManifest] = None) -> None:
    """Gate: exactly one valid tag; matter-first claims quarantined; provenance resolvable."""
    if not isinstance(claim, Claim):
        raise ValueError(f"validate_claim expects Claim, got {type(claim).__name__}")
    claim.validate()
    if manifest is not None:
        for pid in claim.provenance:
            if manifest.find(pid) is None:
                raise ValueError(
                    f"Claim provenance references unknown manifest entry id {pid!r} "
                    f"(statement {claim.statement!r})"
                )


# --- usage example ---
# entry = SourceEntry(path="canon/ether-first.md", sha256=sha256_of_file("canon/ether-first.md"), role="canon", bytes_recorded=True)
# manifest = SourceManifest(version=1, entries=[entry]); validate_manifest(manifest)
# claim = Claim(statement="Ether precedes matter in the canticle order", tag="DERIVED-FROM-FIELD", provenance=[entry.entry_id])
# validate_claim(claim, manifest)  # provenance resolves against the manifest
# quarantined = Claim(statement="Laboratory salt residue mirrors the field", tag="MATTER-FIRST-ARTIFACT", provenance=[], under_investigation=True)
# validate_claim(quarantined)  # passes only because the under-investigation flag is set
# packet = PhasePacket(phase="NIGREDO", claims=[claim], findings=[Finding(kind="CATEGORICAL-LEAK", detail="matter leak", phase="NIGREDO")])
# packet.validate(); blob = json.dumps(packet.to_dict()); restored = PhasePacket.from_dict(json.loads(blob))
# assert restored == packet  # lossless round-trip through JSON
# print(ConvergenceReport(outcome="converged", stop_reason="scorecard stable", cycles_run=3).to_dict())
