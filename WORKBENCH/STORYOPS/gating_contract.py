#!/usr/bin/env python3
"""Gating contract for v3 deeper passes.

Port of nvidia-expansion `scripts/nep_learned_gating_contract.py` (v1), adapted:
- v3 is a deeper pass on a locked 363k master, not a word-count expansion program.
- Floors are quality/rubric floors (7 Quality Gates), not growth floors.
- Epistemic grammar (noesis-writer Albedo) is a first-class gate.
"""
from __future__ import annotations

from copy import deepcopy

GATING_CONTRACT: dict[str, object] = {
    "version": "v3-deeper-pass-gating-contract-v1",
    "purpose": (
        "Govern rubric-gated deeper passes on the locked v3 trilogy. Carries forward "
        "NEP-013..016 acceptance lessons and binds them to the narrative-weaver 7 Gates "
        "plus noesis-writer epistemic grammar. Canon is immutable until gates pass and "
        "the wave closes."
    ),
    "seven_quality_gates": [
        {"id": "aletheos", "deterministic": False,
         "fail_if": ["dry data without sensory life", "chaotic emotion without structure"]},
        {"id": "pubmed", "deterministic": False,
         "fail_if": ["invented technobabble where a real term exists", "pop-science imprecision"]},
        {"id": "alex_grey", "deterministic": False,
         "fail_if": ["biological process told not shown", "'the system activated' style abstraction"]},
        {"id": "opacity", "deterministic": False,
         "fail_if": ["explanatory asides that define canon terms for the reader", "simplified generics"]},
        {"id": "moral_premise", "deterministic": False,
         "fail_if": ["no blind spot operating", "purely reactive protagonist"]},
        {"id": "gardener", "deterministic": False,
         "fail_if": ["gardener sneers or gloats", "gardener enjoys suffering"]},
        {"id": "red_flag", "deterministic": True,
         "threshold_per_1000_words": 3,
         "terms": ["energy", "vibration", "quantum", "universe", "shatter", "frequency", "resonant"]},
    ],
    "stage_acceptance": {
        "must_prove": [
            "candidate preserves scene order and spine visibly",
            "preamble residue and forbidden tokens absent",
            "rubric scores do not regress on any gate",
            "at least one gate improves or the change is a targeted defect fix",
        ],
        "reject_if": [
            "word_count_only_acceptance",
            "non_additive_or_compressing_change",
            "duplicate_base_material",
            "preamble_residue",
            "unsupported_names",
            "explicit_scaffold_terms_on_page",
            "one_note_register",
        ],
        "required_evidence": [
            "before_after_rubric_scores",
            "raw_artifact_parity",
            "hard_ban_scan_clean",
            "residue_scan_clean",
            "autoresearch_trace_entry",
        ],
    },
    "style_gate_thresholds": {
        "braid_balance": 6,
        "wit_lane_distinction": 6,
        "temperature_variation": 6,
        "double_meaning_density": 6,
        "humor_pressure_release": 6,
        "preferred_lane_floor_after_acceptance_review": 7,
    },
    "epistemic_grammar": {
        "claim_modes": [
            "DIRECT-OBSERVATION", "EMPIRICAL-CORRELATE", "TRADITIONAL-SOURCE",
            "HISTORICAL-CLAIM", "HOUSE-MODEL", "DERIVED-SYNTHESIS", "DECLARED-METAPHOR",
        ],
        "rule": (
            "House cosmology (13.7s triangulation, Witness Gap, Sheldrake-as-operational, "
            "Khaloree mechanics) must wear HOUSE-MODEL framing, never empirical syntax. "
            "Categorical leaks are findings, never silently repaired."
        ),
        "matter_first_framing": "invalid unless explicitly marked as artifact under investigation",
    },
    "rejected_output_policy": {
        "reject_if": [
            "rejected_output_reuse",
            "contaminated_scratch_promotion",
            "failed_candidate_in_repair_prompt_after_hard_ban",
            "raw_insert_duplicate_only",
        ],
        "required_actions": [
            "omit hard-failed candidates from later repair prompts",
            "sanitize hard-failure notes before prompt reuse",
            "switch to control model after repeated duplicate-only or hard-ban failures",
        ],
    },
    "known_anti_patterns": [
        "word count passes while wit, humor, and sentence-temperature fail",
        "full-chapter repair compresses accepted prose",
        "explicit tarot, Crowley, Toth, Enneagram, or scaffold language leaks onto page",
        "unsupported local names or named operators appear",
        "premature descent, cure posture, or false-success language resolves pressure too early",
        "matter-first framing presented as ground truth (categorical leak)",
    ],
    "autoresearch_loop_policy": {
        "min_cycles": 3,
        "max_cycles": 9,
        "stagnation_stop": 2,
        "default_mode": "dry-run",
        "one_variable_per_cycle": True,
    },
    "source_evidence": [
        "nvidia-expansion/scripts/nep_learned_gating_contract.py",
        "nvidia-expansion/NVIDIA_EXPANSION_INIT.md",
        "skills/somatic-canticles-narrative-weaver (7 Quality Gates)",
        "skills/noesis-writer-skill (Albedo epistemic grammar)",
        "MEMORY/WORK/20260722-deep-pass/DEEP-PASS-REPORT.md",
    ],
}


def gating_contract() -> dict[str, object]:
    return deepcopy(GATING_CONTRACT)
