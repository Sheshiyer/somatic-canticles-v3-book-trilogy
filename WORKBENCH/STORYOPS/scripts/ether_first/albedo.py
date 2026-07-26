"""Albedo: evidence-normalization phase of the Ether-First Alchemical Autoresearch Loop.

Cleanses and normalizes raw source text and constructs traceable candidate
statements, tagged per the sibling schemas.py taxonomy:

    ClaimTag.DERIVED_FROM_FIELD     -- matter-level phenomenon derived FROM a field term
    ClaimTag.MATTER_FIRST_ARTIFACT  -- identity/equivalence reducing a field term to matter
    ClaimTag.FIELD_FACET            -- otherwise references field vocabulary

Pure, deterministic, stdlib only.
"""

import re
import unicodedata

__all__ = [
    "normalize_text",
    "sentence_split",
    "extract_candidate_statements",
    "tag_candidate",
    "build_claims",
    "dedupe_claims",
]

PHASE = "ALBEDO"

TAG_DERIVED_FROM_FIELD = "DERIVED-FROM-FIELD"
TAG_MATTER_FIRST_ARTIFACT = "MATTER-FIRST-ARTIFACT"
TAG_FIELD_FACET = "FIELD-FACET"

# Causal verbs indicating field -> matter derivation (subject field, object matter).
_CAUSAL_VERBS = (
    "modulates", "shapes", "organizes", "informs", "precedes",
    "modulate", "shape", "organize", "inform", "precede",
    "modulated", "shaped", "organized", "informed", "preceded",
    "modulating", "shaping", "organizing", "informing", "preceding",
)

# Matter-level vocabulary: objects a field term acts upon for DERIVED-FROM-FIELD.
_MATTER_HINTS = (
    "neural", "neuron", "neurons", "brain", "body", "bodily", "soma", "somatic",
    "tissue", "cell", "cells", "cellular", "cortex", "cortical", "synapse",
    "synaptic", "nerve", "nerves", "nervous", "muscle", "muscular", "organism",
    "organ", "organs", "physiology", "physiological", "firing", "matter",
    "material", "particle", "particles", "molecule", "molecules", "molecular",
)

_IDENTITY_PATTERN = re.compile(
    r"\b(?P<field>[\w'-]+)\s+is\s+(?:just\s+|merely\s+|simply\s+|only\s+|nothing\s+but\s+)?(?P<matter>[\w'-]+)",
    re.IGNORECASE,
)

# Abbreviations whose trailing period must not terminate a sentence.
_ABBREVIATIONS = (
    "i.e", "e.g", "vs", "cf", "etc", "viz", "al",
    "Dr", "Mr", "Mrs", "Ms", "Prof", "Sr", "Jr", "St",
    "Fig", "Figs", "Eq", "Eqs", "No", "Nos", "Vol", "pp", "p", "Sec", "Ch",
    "approx", "est", "dept", "Univ",
)
_ABBREV_PLACEHOLDER = "\x00DOT\x00"
_ABBREV_PATTERN = re.compile(
    r"\b(" + "|".join(re.escape(a) for a in _ABBREVIATIONS) + r")\.",
    re.IGNORECASE,
)

_SENTENCE_BOUNDARY = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9\"'(])")

_UNICODE_QUOTES = {
    "‘": "'", "’": "'", "‚": "'", "‛": "'",
    "“": '"', "”": '"', "„": '"', "‟": '"',
    "«": '"', "»": '"',
    "–": "-", "—": "-", "―": "-", "‐": "-", "‑": "-",
    "…": "...",
}

_MARKDOWN_EMPHASIS = re.compile(
    r"(\*\*|__)(?P<bold>.+?)\1"
    r"|(\*|_)(?P<ital>.+?)\3"
    r"|(~~)(?P<strike>.+?)\5"
    r"|`(?P<code>.+?)`"
)

_WHITESPACE = re.compile(r"\s+")


def normalize_text(text: str) -> str:
    """Normalize raw source text.

    Collapses whitespace, converts unicode quotes/dashes to ASCII, strips
    markdown emphasis markers while preserving their content. Case is
    preserved for provenance.
    """
    if not text:
        return ""
    text = unicodedata.normalize("NFKC", text)
    for src, dst in _UNICODE_QUOTES.items():
        text = text.replace(src, dst)
    previous = None
    while previous != text:
        previous = text
        text = _MARKDOWN_EMPHASIS.sub(
            lambda m: m.group("bold") or m.group("ital") or m.group("strike") or m.group("code"),
            text,
        )
    return _WHITESPACE.sub(" ", text).strip()


def sentence_split(text: str) -> list:
    """Deterministic regex sentence segmentation.

    Handles common abbreviations (i.e., vs., Dr., Fig., etc.) so their
    periods do not create false boundaries.
    """
    if not text:
        return []
    protected = _ABBREV_PATTERN.sub(lambda m: m.group(1) + _ABBREV_PLACEHOLDER, text)
    # Protect decimals (e.g., 3.14).
    protected = re.sub(r"(\d)\.(\d)", r"\1" + _ABBREV_PLACEHOLDER + r"\2", protected)
    parts = _SENTENCE_BOUNDARY.split(protected)
    sentences = []
    for part in parts:
        sentence = part.replace(_ABBREV_PLACEHOLDER, ".").strip()
        if sentence:
            sentences.append(sentence)
    return sentences


def _matched_terms(statement: str, manifest_terms: set) -> list:
    lowered = statement.lower()
    return sorted(
        term for term in manifest_terms
        if term and re.search(r"\b" + re.escape(term.lower()) + r"\b", lowered)
    )


def extract_candidate_statements(text: str, manifest_terms: set, min_terms: int = 1) -> list:
    """Extract sentences referencing >= min_terms manifest vocabulary terms.

    Returns dicts of {statement, matched_terms, source_span} where
    source_span is the (start, end) character offset in the input text.
    """
    candidates = []
    cursor = 0
    for sentence in sentence_split(text):
        index = text.find(sentence, cursor)
        if index == -1:
            index = text.find(sentence)
        if index == -1:
            index = cursor
        span = (index, index + len(sentence))
        cursor = span[1]
        matched = _matched_terms(sentence, manifest_terms)
        # Reduction-identity candidates (e.g., 'Consciousness is just neurons
        # firing') may match zero manifest terms but are exactly the
        # matter-first artifacts this phase must surface; retain them too.
        is_reduction = any(
            _mentions_matter(m.group("matter"))
            for m in _IDENTITY_PATTERN.finditer(sentence)
        )
        if len(matched) >= min_terms or is_reduction:
            candidates.append({
                "statement": sentence,
                "matched_terms": matched,
                "source_span": span,
            })
    return candidates


def _causal_verb_between(prefix: str, suffix: str) -> bool:
    for verb in _CAUSAL_VERBS:
        if re.search(r"\b" + verb + r"\b", prefix + " " + suffix, re.IGNORECASE):
            return True
    return False


def _mentions_matter(text: str) -> bool:
    lowered = text.lower()
    return any(re.search(r"\b" + re.escape(hint) + r"\b", lowered) for hint in _MATTER_HINTS)


def _mentions_field(text: str, manifest_terms: set) -> bool:
    return bool(_matched_terms(text, manifest_terms))


def tag_candidate(statement: str, manifest_terms: set) -> str:
    """Deterministically assign a ClaimTag to a candidate statement.

    DERIVED-FROM-FIELD:     field-term subject + causal verb + matter-term object.
    MATTER-FIRST-ARTIFACT: identity/equivalence reducing a field term to matter.
    FIELD_FACET:            otherwise references field vocabulary at all.
    """
    matched = _matched_terms(statement, manifest_terms)
    matched_lowered = {t.lower() for t in matched}

    # MATTER-FIRST-ARTIFACT: 'X is [just/merely/...] Y' where Y is a matter
    # term, and X is either a manifest (field) term or -- with zero manifest
    # matches -- an epistemic abstraction being reduced to matter.
    for m in _IDENTITY_PATTERN.finditer(statement):
        field_word = m.group("field").lower()
        matter_word = m.group("matter").lower()
        if not _mentions_matter(matter_word):
            continue
        if not matched or field_word in matched_lowered:
            return TAG_MATTER_FIRST_ARTIFACT

    if not matched:
        return TAG_FIELD_FACET

    # DERIVED-FROM-FIELD: field-term subject + causal verb + matter-term object.
    for verb in _CAUSAL_VERBS:
        verb_match = re.search(r"\b" + verb + r"\b", statement, re.IGNORECASE)
        if not verb_match:
            continue
        prefix = statement[:verb_match.start()]
        suffix = statement[verb_match.end():]
        if _mentions_field(prefix, set(matched)) and _mentions_matter(suffix):
            return TAG_DERIVED_FROM_FIELD

    return TAG_FIELD_FACET


def build_claims(text: str, manifest_terms: set) -> list:
    """Full Albedo pipeline: normalize -> split -> extract -> tag.

    Returns claim dicts {statement, tag, provenance, phase}.
    """
    normalized = normalize_text(text)
    claims = []
    for candidate in extract_candidate_statements(normalized, manifest_terms):
        claims.append({
            "statement": candidate["statement"],
            "tag": tag_candidate(candidate["statement"], manifest_terms),
            "provenance": candidate["matched_terms"],
            "phase": PHASE,
        })
    return claims


def dedupe_claims(claims: list) -> list:
    """Drop exact-duplicate statements (case-insensitive, whitespace-normalized),
    keeping the first occurrence."""
    seen = set()
    unique = []
    for claim in claims:
        key = _WHITESPACE.sub(" ", claim["statement"]).strip().lower()
        if key in seen:
            continue
        seen.add(key)
        unique.append(claim)
    return unique


if __name__ == "__main__":
    manifest_terms = {"field", "substrate", "coherence"}
    sample = (
        "The field modulates neural coherence. "
        "Consciousness is just neurons firing. "
        "The substrate holds the pattern. "
        "Field coherence precedes cortical organization."
    )
    claims = build_claims(sample, manifest_terms)
    for claim in claims:
        print(f"[{claim['tag']}] {claim['statement']}")
        print(f"    provenance: {claim['provenance']}  phase: {claim['phase']}")
