"""Citrinitas synthesis phase of the Ether-First Alchemical Autoresearch Loop.

Consumes Albedo claim dicts and Nigredo finding dicts, synthesizes
field-grounded candidate statements from clustered claims, probes their
structural consequences, and reports exclusions for contaminated claims.

All behaviour is pure and deterministic; stdlib only. Candidate statements
are structural placeholders for a later LLM prose pass.

Data shapes (sibling modules):
    claim   = {"statement": str, "tag": str, "provenance": list[str], "phase": str}
    finding = {"kind": str, "detail": str, "phase": str, "span": ...}

Tags: DERIVED-FROM-FIELD, FIELD-FACET, MATTER-FIRST-ARTIFACT.
Contaminating finding kinds: MATTER-FIRST-FRAMING, CATEGORICAL-LEAK.
"""

from __future__ import annotations

import string

PHASE = "CITRINITAS"

FIELD_TAGS = frozenset({"DERIVED-FROM-FIELD", "FIELD-FACET"})
MATTER_TAG = "MATTER-FIRST-ARTIFACT"
CONTAMINATING_KINDS = frozenset({"MATTER-FIRST-FRAMING", "CATEGORICAL-LEAK"})

CLUSTER_OVERLAP_THRESHOLD = 2
MIN_GROUP_SIZE = 2
TOP_TERMS_PER_STATEMENT = 3
CONTAMINATION_WINDOW = 5

_PUNCT_TABLE = str.maketrans("", "", string.punctuation)


def _provenance_terms(claim: dict) -> tuple[str, ...]:
    """Normalised, deduplicated, sorted provenance terms for a claim."""
    terms = {str(term).strip().lower() for term in claim.get("provenance", [])}
    terms.discard("")
    return tuple(sorted(terms))


def _statement_words(text: str) -> list[str]:
    """Lowercased, punctuation-stripped word list for a statement."""
    return [
        word
        for word in str(text).lower().translate(_PUNCT_TABLE).split()
        if word
    ]


def _windows(words: list[str], size: int) -> set[tuple[str, ...]]:
    """All contiguous windows of ``size`` words (full text if shorter)."""
    if len(words) <= size:
        return {tuple(words)} if words else set()
    return {tuple(words[i : i + size]) for i in range(len(words) - size + 1)}


def _shares_window(statement_a: str, statement_b: str, size: int) -> bool:
    """True when two statements share at least one contiguous word window."""
    windows_a = _windows(_statement_words(statement_a), size)
    windows_b = _windows(_statement_words(statement_b), size)
    return bool(windows_a & windows_b)


def _is_contaminated(claim: dict, finding: dict) -> bool:
    """True when a claim overlaps a contaminating finding's detail text."""
    return _shares_window(
        claim.get("statement", ""),
        finding.get("detail", ""),
        CONTAMINATION_WINDOW,
    )


def _contamination_index(claims: list[dict], findings: list[dict]) -> dict[int, list[dict]]:
    """Map claim index -> contaminating findings (deterministic order)."""
    flagged: dict[int, list[dict]] = {}
    contaminating = [
        finding
        for finding in findings
        if finding.get("kind") in CONTAMINATING_KINDS
    ]
    for index, claim in enumerate(claims):
        hits = [
            finding
            for finding in contaminating
            if _is_contaminated(claim, finding)
        ]
        if hits:
            flagged[index] = hits
    return flagged


def _cluster_claims(
    claims: list[dict],
    overlap_threshold: int = CLUSTER_OVERLAP_THRESHOLD,
) -> list[tuple[tuple[str, ...], list[dict]]]:
    """Greedy deterministic clustering of claims by shared provenance terms.

    Buckets keyed by sorted matched-term tuples are processed in sorted key
    order; each claim joins the first bucket sharing >= ``overlap_threshold``
    provenance terms, otherwise it starts a new bucket keyed by its own terms.
    """
    buckets: dict[tuple[str, ...], list[dict]] = {}
    for claim in claims:
        terms = _provenance_terms(claim)
        if not terms:
            continue
        placed = False
        for key in sorted(buckets):
            if len(set(key) & set(terms)) >= overlap_threshold:
                buckets[key].append(claim)
                placed = True
                break
        if not placed:
            buckets[terms] = [claim]
    return [(key, buckets[key]) for key in sorted(buckets)]


def _exclusion_entry(claim: dict, findings_for_claim: list[dict]) -> dict:
    """Exclusion record pairing a contaminated claim with finding references."""
    return {
        "claim": claim,
        "finding_refs": [
            {"kind": finding.get("kind"), "detail": finding.get("detail")}
            for finding in findings_for_claim
        ],
    }


def synthesize_candidates(claims: list[dict], findings: list[dict]) -> list[dict]:
    """Build field-grounded synthesis candidates from the Albedo claim pool.

    Returns {"candidates": [...], "exclusions": [...]}. Candidates carry a
    deterministic placeholder statement, the union of member provenance
    terms, member_count, and phase CITRINITAS. Claims contaminated by
    MATTER-FIRST-FRAMING or CATEGORICAL-LEAK findings (shared 5-word window
    with the finding detail) are excluded and reported with their finding
    references.
    """
    contaminated = _contamination_index(claims, findings)
    clean_claims = [
        claim for index, claim in enumerate(claims) if index not in contaminated
    ]
    exclusions = [
        _exclusion_entry(claims[index], contaminated[index])
        for index in sorted(contaminated)
    ]

    candidates: list[dict] = []
    for _key, members in _cluster_claims(clean_claims):
        field_grounded = [
            member for member in members if member.get("tag") in FIELD_TAGS
        ]
        if len(field_grounded) < MIN_GROUP_SIZE:
            continue
        union_terms = sorted(
            {term for member in field_grounded for term in _provenance_terms(member)}
        )
        if not union_terms:
            continue
        top_terms = union_terms[:TOP_TERMS_PER_STATEMENT]
        member_count = len(field_grounded)
        statement = (
            f"Synthesis[{', '.join(top_terms)}]: "
            f"{member_count} field-grounded claims converge on "
            f"{' + '.join(top_terms)}"
        )
        # Synthesis inherits the strongest member tag so Rubedo gates can fire:
        # any DERIVED-FROM-FIELD member promotes the group; else FIELD-FACET.
        member_tags = {member.get("tag") for member in field_grounded}
        inherited_tag = (
            "DERIVED-FROM-FIELD" if "DERIVED-FROM-FIELD" in member_tags else "FIELD-FACET"
        )
        candidates.append(
            {
                "statement": statement,
                "tag": inherited_tag,
                "provenance": union_terms,
                "member_count": member_count,
                "phase": PHASE,
            }
        )
    return {"candidates": candidates, "exclusions": exclusions}


def test_structural_consequences(candidate: dict, all_claims: list[dict]) -> dict:
    """Deterministic consequence probe for one synthesis candidate.

    supports: claims sharing >= 1 provenance term with the candidate and a
    matching field-grounded tag. tensions: claims sharing >= 1 provenance
    term that carry the MATTER-FIRST-ARTIFACT tag. grounding_score is
    len(supports) / (len(supports) + len(tensions)); when neither supports
    nor tensions exist it is 1.0 (vacuous grounding), and it is 1.0
    whenever at least one support exists and no tensions do.
    """
    candidate_terms = set(candidate.get("provenance", []))
    candidate_statement = candidate.get("statement", "")
    supports: list[str] = []
    tensions: list[str] = []
    for claim in all_claims:
        claim_statement = claim.get("statement", "")
        if claim_statement == candidate_statement:
            continue
        claim_terms = _provenance_terms(claim)
        if not candidate_terms & set(claim_terms):
            continue
        if claim.get("tag") == MATTER_TAG:
            tensions.append(claim_statement)
        elif claim.get("tag") in FIELD_TAGS:
            supports.append(claim_statement)
    denominator = len(supports) + len(tensions)
    grounding_score = (len(supports) / denominator) if denominator else 1.0
    return {
        "consistent": not tensions,
        "supports": supports,
        "tensions": tensions,
        "grounding_score": grounding_score,
    }


def run_citrinitas(claims: list[dict], findings: list[dict]) -> dict:
    """Run the full Citrinitas phase over claims and findings.

    Returns {"candidates": [...], "exclusions": [...],
    "consequence_reports": {candidate_statement: report}} with candidates
    sorted by grounding_score descending, then statement ascending.
    """
    synthesis = synthesize_candidates(claims, findings)
    candidates = synthesis["candidates"]
    reports = {
        candidate["statement"]: test_structural_consequences(candidate, claims)
        for candidate in candidates
    }
    candidates.sort(
        key=lambda candidate: (
            -reports[candidate["statement"]]["grounding_score"],
            candidate["statement"],
        )
    )
    return {
        "candidates": candidates,
        "exclusions": synthesis["exclusions"],
        "consequence_reports": reports,
    }


def _demo() -> None:
    claims = [
        {
            "statement": "The field maintains coherence across distributed somatic sites",
            "tag": "DERIVED-FROM-FIELD",
            "provenance": ["field", "coherence"],
            "phase": "ALBEDO",
        },
        {
            "statement": "Coherence in the field precedes any local articulation of form",
            "tag": "DERIVED-FROM-FIELD",
            "provenance": ["coherence", "field"],
            "phase": "ALBEDO",
        },
        {
            "statement": "Breath rhythm entrains the field into measurable coherence",
            "tag": "FIELD-FACET",
            "provenance": ["field", "coherence", "breath"],
            "phase": "ALBEDO",
        },
        {
            "statement": "Tissue memory stores imprints of prior field states",
            "tag": "MATTER-FIRST-ARTIFACT",
            "provenance": ["tissue", "memory"],
            "phase": "ALBEDO",
        },
        {
            "statement": "Resonance between cells couples distant regions of the field",
            "tag": "FIELD-FACET",
            "provenance": ["field", "resonance"],
            "phase": "ALBEDO",
        },
        {
            "statement": "The body is a machine of discrete mechanical parts",
            "tag": "MATTER-FIRST-ARTIFACT",
            "provenance": ["machine", "parts"],
            "phase": "ALBEDO",
        },
    ]
    findings = [
        {
            "kind": "CATEGORICAL-LEAK",
            "detail": "The body is a machine of discrete mechanical parts",
            "phase": "NIGREDO",
            "span": [0, 46],
        },
        {
            "kind": "MATTER-FIRST-FRAMING",
            "detail": "Cartesian mechanism smuggled into somatic description",
            "phase": "NIGREDO",
            "span": [12, 60],
        },
    ]

    result = run_citrinitas(claims, findings)

    print("=== Citrinitas phase report ===")
    print(f"candidates: {len(result['candidates'])}")
    for candidate in result["candidates"]:
        report = result["consequence_reports"][candidate["statement"]]
        print(f"  - {candidate['statement']}")
        print(
            f"      members={candidate['member_count']} "
            f"grounding_score={report['grounding_score']:.3f} "
            f"consistent={report['consistent']}"
        )
        print(f"      supports={len(report['supports'])} tensions={len(report['tensions'])}")

    print(f"exclusions: {len(result['exclusions'])}")
    for exclusion in result["exclusions"]:
        refs = ", ".join(ref["kind"] for ref in exclusion["finding_refs"])
        print(f"  - {exclusion['claim']['statement']}  [{refs}]")


if __name__ == "__main__":
    _demo()
