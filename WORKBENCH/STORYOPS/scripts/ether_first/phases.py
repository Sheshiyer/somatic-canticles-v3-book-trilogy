"""Phase sequencing and invariant validation for the Ether-First
Alchemical Autoresearch Loop.

Pure Python 3 standard library. No external dependencies.

Components
----------
- ``Phase``                : the five alchemical phases, in order.
- ``PhaseOrderError``      : raised on any out-of-order phase transition.
- ``PhaseSequencer``       : enforces strict sequential phase progression.
- ``check_ether_first``    : validates the Ether-First invariant over claims.
- ``StagnationDetector``   : halts the loop after consecutive stagnant cycles.
- ``validate_cycle_plan``  : enforces the 3..9 cycle bound.
"""

from __future__ import annotations

import hashlib
import json
from enum import Enum
from typing import Any, Iterable, Mapping, Optional, Sequence


__all__ = [
    "Phase",
    "PhaseOrderError",
    "PhaseSequencer",
    "InvariantViolation",
    "DEFAULT_MATTER_FIRST_MARKERS",
    "MATTER_FIRST_ARTIFACT_TAG",
    "check_ether_first",
    "StagnationDetector",
    "MIN_CYCLES",
    "MAX_CYCLES",
    "CyclePlanError",
    "validate_cycle_plan",
]


# ---------------------------------------------------------------------------
# 1. Phases
# ---------------------------------------------------------------------------

class Phase(Enum):
    """The five phases of the Ether-First Alchemical Autoresearch Loop.

    Declaration order is canonical: each phase's value is its 1-based
    ordinal, so ``Phase.NIGREDO.value > Phase.ETHER_AXIOM.value``.
    """

    ETHER_AXIOM = 1
    NIGREDO = 2
    ALBEDO = 3
    CITRINITAS = 4
    RUBEDO = 5


class PhaseOrderError(RuntimeError):
    """Raised when a phase transition violates strict sequential order."""


class PhaseSequencer:
    """Enforces strict ordering over the alchemical phases.

    Rules:
      - Phases must be entered in declaration order, starting at
        ``Phase.ETHER_AXIOM``.
      - Entering a later phase while an earlier phase is incomplete
        (a skip) raises ``PhaseOrderError``.
      - Re-entering a phase that has already completed raises
        ``PhaseOrderError``.
      - Re-entering the phase currently in progress is a no-op
        (idempotent entry), not an error.

    Every error message names the violated transition, e.g.
    ``"ETHER_AXIOM -> ALBEDO"``.
    """

    def __init__(self) -> None:
        self._completed: list[Phase] = []
        self._current: Optional[Phase] = None

    # -- introspection -----------------------------------------------------

    @property
    def current(self) -> Optional[Phase]:
        """The phase currently in progress, or None."""
        return self._current

    @property
    def completed(self) -> tuple[Phase, ...]:
        """Completed phases, in completion order."""
        return tuple(self._completed)

    def is_complete(self, phase: Phase) -> bool:
        return phase in self._completed

    @property
    def done(self) -> bool:
        """True once RUBEDO has completed."""
        return self._completed[-1:] == [Phase.RUBEDO]

    # -- transitions --------------------------------------------------------

    @staticmethod
    def _transition_label(frm: Optional[Phase], to: Phase) -> str:
        origin = frm.name if frm is not None else "START"
        return f"{origin} -> {to.name}"

    def _check_enter(self, phase: Phase) -> None:
        if not isinstance(phase, Phase):
            raise TypeError(f"expected a Phase, got {type(phase).__name__}")

        # Re-entering a completed earlier phase is forbidden.
        if phase in self._completed:
            raise PhaseOrderError(
                f"PhaseOrderError: cannot re-enter completed phase; "
                f"violated transition: "
                f"{self._transition_label(self._current, phase)}"
            )

        # Idempotent re-entry of the in-progress phase.
        if phase is self._current:
            return

        # Every phase before `phase` must be complete; otherwise this is
        # a skip forward (or a jump backward onto an incomplete phase).
        for earlier in Phase:
            if earlier is phase:
                break
            if earlier not in self._completed:
                raise PhaseOrderError(
                    f"PhaseOrderError: cannot enter {phase.name} before "
                    f"{earlier.name} completes; violated transition: "
                    f"{self._transition_label(self._current, phase)}"
                )

    def enter(self, phase: Phase) -> None:
        """Enter ``phase``, enforcing strict sequential order."""
        self._check_enter(phase)
        self._current = phase

    def complete_current(self) -> Phase:
        """Mark the current phase complete and return it.

        Raises ``PhaseOrderError`` if no phase is in progress.
        """
        if self._current is None:
            raise PhaseOrderError(
                "PhaseOrderError: no phase in progress to complete; "
                "violated transition: START -> COMPLETE"
            )
        finished = self._current
        self._completed.append(finished)
        self._current = None
        return finished

    def advance(self, phase: Phase) -> None:
        """Complete the current phase (if any) and enter ``phase``."""
        if self._current is not None:
            self.complete_current()
        self.enter(phase)


# ---------------------------------------------------------------------------
# 2. Ether-First invariant
# ---------------------------------------------------------------------------

MATTER_FIRST_ARTIFACT_TAG = "MATTER-FIRST-ARTIFACT"

DEFAULT_MATTER_FIRST_MARKERS: tuple[str, ...] = (
    "the brain generates",
    "brain generates consciousness",
    "neural correlates produce consciousness",
    "neural activity produces consciousness",
    "matter gives rise to mind",
    "matter produces consciousness",
    "consciousness emerges from matter",
    "consciousness is generated by",
    "mind arises from matter",
    "the brain creates consciousness",
    "the brain produces consciousness",
)


class InvariantViolation:
    """One Ether-First invariant violation."""

    def __init__(self, claim: Mapping[str, Any], marker: str, reason: str) -> None:
        self.claim = claim
        self.marker = marker
        self.reason = reason

    def __repr__(self) -> str:  # pragma: no cover - debugging aid
        return (
            f"InvariantViolation(marker={self.marker!r}, "
            f"reason={self.reason!r})"
        )


def _claim_text(claim: Any) -> str:
    """Extract the framing text of a claim (mapping or plain string)."""
    if isinstance(claim, str):
        return claim
    if isinstance(claim, Mapping):
        for key in ("framing", "text", "claim", "statement"):
            value = claim.get(key)
            if isinstance(value, str):
                return value
    return ""


def _claim_tags(claim: Any) -> set[str]:
    if isinstance(claim, Mapping):
        tags = claim.get("tags", ())
        if isinstance(tags, str):
            return {tags}
        try:
            return {str(t) for t in tags}
        except TypeError:
            return set()
    return set()


def check_ether_first(
    claims: Iterable[Any],
    markers: Optional[Sequence[str]] = None,
) -> list[InvariantViolation]:
    """Validate the Ether-First invariant over a sequence of claims.

    The invariant: no claim may frame the field/substrate as derived FROM
    matter. A claim violates the invariant when its framing text contains
    any matter-first marker phrase, UNLESS the claim is explicitly tagged
    ``MATTER-FIRST-ARTIFACT`` AND marked ``under_investigation=True`` —
    such claims are known matter-first artifacts under active
    investigation and are tolerated, not endorsed.

    Parameters
    ----------
    claims:
        Iterable of claims. Each claim is either a plain string (the
        framing text) or a mapping with a ``framing``/``text``/``claim``/
        ``statement`` string, an optional ``tags`` iterable, and an
        optional ``under_investigation`` bool.
    markers:
        Matter-first marker phrases. Matching is case-insensitive
        substring matching. Defaults to ``DEFAULT_MATTER_FIRST_MARKERS``.

    Returns
    -------
    list[InvariantViolation]
        One entry per violating claim, in input order. Empty means the
        invariant holds.
    """
    active_markers = tuple(m.lower() for m in (markers or DEFAULT_MATTER_FIRST_MARKERS))
    violations: list[InvariantViolation] = []

    for claim in claims:
        text = _claim_text(claim)
        if not text:
            continue
        lowered = text.lower()
        hit = next((m for m in active_markers if m in lowered), None)
        if hit is None:
            continue

        tags = _claim_tags(claim)
        tagged_artifact = MATTER_FIRST_ARTIFACT_TAG in tags
        under_investigation = bool(
            isinstance(claim, Mapping) and claim.get("under_investigation", False)
        )
        if tagged_artifact and under_investigation:
            continue

        if tagged_artifact and not under_investigation:
            reason = (
                f"tagged {MATTER_FIRST_ARTIFACT_TAG} but not marked "
                f"under_investigation=True"
            )
        else:
            reason = (
                "framing derives the field/substrate from matter without "
                f"the {MATTER_FIRST_ARTIFACT_TAG} investigation tag"
            )
        violations.append(InvariantViolation(claim, hit, reason))

    return violations


# ---------------------------------------------------------------------------
# 3. Stagnation detector
# ---------------------------------------------------------------------------

class StagnationDetector:
    """Detects a stalled autoresearch loop.

    Each cycle, the caller records a scorecard summary via
    ``record_cycle``. A cycle is *stagnant* when it accepted zero
    candidates. ``stop_required()`` returns True once the loop has
    produced ``threshold`` consecutive stagnant cycles (default 2).

    Scorecard hashes are retained per cycle for auditability.
    """

    def __init__(self, threshold: int = 2) -> None:
        if threshold < 1:
            raise ValueError("threshold must be >= 1")
        self.threshold = threshold
        self._hashes: list[str] = []
        self._accepted_counts: list[int] = []

    @staticmethod
    def _hash_scorecard(scorecard: Any) -> str:
        payload = json.dumps(scorecard, sort_keys=True, default=str)
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()

    def record_cycle(self, scorecard: Any, accepted_count: int = 0) -> str:
        """Record one cycle's scorecard; returns its hash.

        ``accepted_count`` is the number of candidates the cycle accepted
        (default 0 — a stagnant cycle).
        """
        digest = self._hash_scorecard(scorecard)
        self._hashes.append(digest)
        self._accepted_counts.append(int(accepted_count))
        return digest

    @property
    def cycles(self) -> int:
        return len(self._hashes)

    @property
    def hashes(self) -> tuple[str, ...]:
        return tuple(self._hashes)

    def consecutive_stagnant(self) -> int:
        """Length of the trailing run of zero-acceptance cycles."""
        run = 0
        for count in reversed(self._accepted_counts):
            if count > 0:
                break
            run += 1
        return run

    def stop_required(self) -> bool:
        """True after ``threshold`` consecutive stagnant cycles."""
        return self.consecutive_stagnant() >= self.threshold


# ---------------------------------------------------------------------------
# 4. Cycle bounds
# ---------------------------------------------------------------------------

MIN_CYCLES = 3
MAX_CYCLES = 9


class CyclePlanError(ValueError):
    """Raised when a cycle plan falls outside the allowed bounds."""


def validate_cycle_plan(n: int) -> int:
    """Enforce the cycle bound: at least 3, at most 9 cycles.

    Returns ``n`` unchanged when valid; raises ``CyclePlanError``
    otherwise.
    """
    if isinstance(n, bool) or not isinstance(n, int):
        raise CyclePlanError(f"cycle count must be an int, got {n!r}")
    if n < MIN_CYCLES:
        raise CyclePlanError(
            f"cycle plan too short: {n} < minimum {MIN_CYCLES} cycles"
        )
    if n > MAX_CYCLES:
        raise CyclePlanError(
            f"cycle plan too long: {n} > maximum {MAX_CYCLES} cycles"
        )
    return n
