#!/usr/bin/env python3
"""Deterministic 7-Gate rubric scanner for Somatic Canticles v3 chapters.

Automates the machine-checkable parts of the narrative-weaver rubric:
  Gate 7 (Red Flag): flagged-term density per 1000 words
  Duplication: verbatim repeated paragraphs (NEP expansion residue)
  Epistemic: HOUSE-MODEL vs empirical-syntax markers around house-cosmology constants
  Voice register: per-book register marker share (B1 systems / B2 resonance / B3 perception)
  Opacity (partial): explanatory-aside patterns ("X, which means", "in other words")

Gates 1-6 remain critic-model responsibilities; this tool emits the baseline metrics
the autoresearch loop keeps/discards against.

Usage:
  python3 WORKBENCH/STORYOPS/scripts/rubric_scan.py CHAPTERS/book_3/Chapter-16-The-Wilt.md
  python3 WORKBENCH/STORYOPS/scripts/rubric_scan.py --book 3 --json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

RED_FLAG_TERMS = ["energy", "vibration", "quantum", "universe", "shatter", "frequency", "resonant"]
RED_FLAG_FLOOR_PER_1000 = 3.0

HOUSE_COSMOLOGY_TERMS = [
    "13.7", "Witness Gap", "Khalor", "morphic resonance", "Tryambakam",
    "observer effect", "observer-effect",
]
HOUSE_MODEL_MARKERS = ["house-model", "house model", "in-world", "in the house cosmology",
                       "as the Somanauts frame it", "declared model", "the protocol names it"]

OPACITY_ASIDE_PATTERNS = [
    r"\bwhich means\b", r"\bin other words\b", r"\bthat is to say\b",
    r"\bsimply put\b", r"\bput simply\b",
]

REGISTER_MARKERS = {
    1: ["system", "protocol", "diagnostic", "measure", "calibrat", "signal", "data", "vector"],
    2: ["resonan", "chorus", "heart", "coheren", "rhythm", "pulse", "breath", "synchron"],
    3: ["perceiv", "witness", "author", "see", "perception", "authorship", "lens", "frame"],
}


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text))


def paragraphs(text: str) -> list[str]:
    return [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]


def red_flag_metrics(text: str) -> dict:
    words = max(word_count(text), 1)
    per_term = {}
    total_hits = 0
    lower = text.lower()
    for term in RED_FLAG_TERMS:
        hits = len(re.findall(rf"\b{re.escape(term)}\b", lower))
        per_term[term] = {"hits": hits, "per_1000": round(hits / words * 1000, 2)}
        total_hits += hits
    dense_terms = [t for t, m in per_term.items() if m["per_1000"] > RED_FLAG_FLOOR_PER_1000]
    return {
        "terms": per_term,
        "total_hits": total_hits,
        "total_per_1000": round(total_hits / words * 1000, 2),
        "gate_red_flag": "FAIL" if dense_terms else "PASS",
        "dense_terms": dense_terms,
    }


def duplication_metrics(text: str) -> dict:
    paras = paragraphs(text)
    seen: dict[str, int] = {}
    duplicates = []
    for i, p in enumerate(paras):
        norm = re.sub(r"\s+", " ", p)
        if len(norm) < 120:
            continue
        if norm in seen:
            duplicates.append({"first_paragraph": seen[norm], "repeat_paragraph": i,
                               "preview": norm[:100]})
        else:
            seen[norm] = i
    return {
        "verbatim_duplicate_paragraphs": len(duplicates),
        "duplicates": duplicates,
        "gate_duplication": "FAIL" if duplicates else "PASS",
    }


def epistemic_metrics(text: str) -> dict:
    lower = text.lower()
    house_hits = {t: len(re.findall(re.escape(t.lower()), lower)) for t in HOUSE_COSMOLOGY_TERMS}
    house_hits = {t: n for t, n in house_hits.items() if n}
    marker_hits = sum(len(re.findall(re.escape(m), lower)) for m in HOUSE_MODEL_MARKERS)
    # empirical-syntax wearers: house term adjacent to "measured", "proven", "evidence shows"
    empirical_wearers = 0
    for t in house_hits:
        for m in re.finditer(re.escape(t.lower()), lower):
            window = lower[max(0, m.start() - 80): m.end() + 80]
            if re.search(r"\b(measured|proven|evidence shows|scientifically|empirically)\b", window):
                empirical_wearers += 1
    return {
        "house_terms_present": house_hits,
        "house_model_markers": marker_hits,
        "empirical_syntax_adjacent": empirical_wearers,
        "gate_epistemic": "WARN" if (house_hits and empirical_wearers > 0 and marker_hits == 0) else "PASS",
    }


def opacity_metrics(text: str) -> dict:
    lower = text.lower()
    flagged = len(re.findall(r"\[opacity-review:", lower))
    raw_hits = sum(len(re.findall(p, lower)) for p in OPACITY_ASIDE_PATTERNS)
    unflagged = max(raw_hits - flagged, 0)
    return {
        "explanatory_aside_hits": unflagged,
        "explanatory_aside_flagged_for_review": flagged,
        "gate_opacity_partial": "WARN" if unflagged > 0 else "PASS",
    }


def register_metrics(text: str, book: int) -> dict:
    lower = text.lower()
    shares = {}
    for b, markers in REGISTER_MARKERS.items():
        shares[b] = sum(len(re.findall(m, lower)) for m in markers)
    expected = REGISTER_MARKERS[book]
    expected_hits = sum(len(re.findall(m, lower)) for m in expected)
    total = max(sum(shares.values()), 1)
    expected_share = round(shares[book] / total * 100, 1)
    return {
        "marker_hits_by_book": shares,
        "expected_book": book,
        "expected_share_pct": expected_share,
        "gate_voice_register": "PASS" if shares[book] == max(shares.values()) else "WARN",
    }


def scan_file(path: Path, book: int | None) -> dict:
    text = path.read_text(encoding="utf-8")
    if book is None:
        if "book_1" in str(path):
            book = 1
        elif "book_2" in str(path):
            book = 2
        else:
            book = 3
    result = {
        "file": str(path),
        "book": book,
        "words": word_count(text),
    }
    result.update(red_flag_metrics(text))
    result.update(duplication_metrics(text))
    result.update(epistemic_metrics(text))
    result.update(opacity_metrics(text))
    result.update(register_metrics(text, book))
    gates = {k: v for k, v in result.items() if k.startswith("gate_")}
    result["deterministic_verdict"] = (
        "FAIL" if "FAIL" in gates.values() else ("WARN" if "WARN" in gates.values() else "PASS")
    )
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Deterministic 7-Gate rubric scanner")
    parser.add_argument("path", nargs="?", help="chapter markdown file")
    parser.add_argument("--book", type=int, choices=[1, 2, 3], help="scan all chapters of a book")
    parser.add_argument("--json", action="store_true", help="emit JSON")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[3]
    results = []
    if args.book:
        for p in sorted((root / "CHAPTERS" / f"book_{args.book}").glob("*.md")):
            results.append(scan_file(p, args.book))
    elif args.path:
        results.append(scan_file(Path(args.path), None))
    else:
        parser.error("provide a path or --book")

    if args.json:
        print(json.dumps(results if len(results) > 1 else results[0], indent=2))
        return

    for r in results:
        print(f"== {Path(r['file']).name} (book {r['book']}, {r['words']}w) ==")
        print(f"  red_flag: {r['gate_red_flag']} (total {r['total_per_1000']}/1000; dense: {r['dense_terms'] or 'none'})")
        print(f"  duplication: {r['gate_duplication']} ({r['verbatim_duplicate_paragraphs']} verbatim repeats)")
        print(f"  epistemic: {r['gate_epistemic']} (markers {r['house_model_markers']}, empirical-adjacent {r['empirical_syntax_adjacent']})")
        print(f"  opacity(asides): {r['gate_opacity_partial']} ({r['explanatory_aside_hits']} hits)")
        print(f"  voice register: {r['gate_voice_register']} (expected-book share {r['expected_share_pct']}%)")
        print(f"  VERDICT: {r['deterministic_verdict']}")

    if any(r["deterministic_verdict"] == "FAIL" for r in results):
        sys.exit(1)


if __name__ == "__main__":
    main()
