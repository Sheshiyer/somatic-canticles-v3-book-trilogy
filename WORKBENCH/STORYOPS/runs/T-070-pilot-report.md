# T-070 Pilot Report — Deeper Rubric Pass (Book 3 Sample)

**Date:** 2026-07-24 · **Mode:** dry-run (canon untouched) · **Branch:** feature/storyops-omnirouter-T068-071

## Scope

Baseline deterministic rubric scan across all 12 Book 3 chapters, then bounded autoresearch loops
(one variable per cycle, dry-run) on the 4 chapters with unflagged opacity asides:
Ch16 (The Wilt), Ch20 (The Convergence Point), Ch23 (The Flaw in the Code), Ch26 (The Architecture of New Reality).

## Baseline (full Book 3 scan — `book3-baseline-scan.txt`)

| Metric | Result |
|---|---|
| Red-flag terms (energy/vibration/quantum/universe/shatter/frequency/resonant) | 12/12 PASS — worst density 0.16/1000 (floor 3.0) |
| Verbatim duplicate paragraphs (NEP residue check) | 12/12 PASS — **0 repeats** (the Ch13/19/22/27 duplication artifacts from the v2 deep-pass report are NOT present in the v3 canonical tree) |
| Epistemic (house-cosmology terms in empirical syntax) | 12/12 PASS — 0 empirical-adjacent hits |
| Opacity (explanatory asides) | 4 WARN — 1 hit each in Ch16, Ch20, Ch23, Ch26 |
| Voice register (B3 perception markers dominant) | 7 PASS / 5 WARN (heuristic; B3 mixes systems + perception vocabulary by design) |

## Autoresearch cycles (dry-run, artifacts in `runs/<chapter>/`)

| Chapter | Cycle 1: dedupe | Cycle 2: opacity-strip | Verdict |
|---|---|---|---|
| Ch16 | discard (no-op) | **keep** — asides 1→0 (flagged for editorial review) | WARN→WARN (register heuristic only) |
| Ch20 | discard (no-op) | **keep** — asides 1→0 | WARN→WARN |
| Ch23 | discard (no-op) | **keep** — asides 1→0 | WARN→**PASS** |
| Ch26 | discard (no-op) | **keep** — asides 1→0 | WARN→WARN |

Loop contract honored: one variable per cycle, before/after metrics recorded, keep/discard by
strict improvement (better on ≥1 metric, worse on none), traces in `autoresearch-trace.json`.

## Findings

1. **v3 canon is cleaner than the v2 deep-pass baseline.** The duplication artifacts and CJK typo
   flagged in the local v2 tree do not exist here — P2 hygiene tasks (T-014..T-021) should re-verify
   against this repo rather than the local v2 before executing fixes.
2. **Opacity asides are the only deterministic defects in Book 3** — 4 instances, all single-hit,
   now flagged in candidates for editorial review (not auto-removed: Opacity Gate requires human/critic
   judgment on whether the aside is intentional register).
3. **Voice-register heuristic needs calibration.** B3 deliberately braids perception vocabulary with
   systems/protocol vocabulary (the Severance chapters are procedural). The marker-share heuristic
   WARNs are expected-by-design, not defects — fold into gating contract as "braid expected in B3."
4. Critic-model gates (Aletheos, PubMed, Alex Grey, Moral Premise, Gardener) were not executed in this
   pilot — they require the omnirouter PROSE/CRITIQUE lanes (T-069 matrix) with a live critic model.

## Next

- [ ] T-069: ratify omnirouter matrix; pick concrete critic + prose models for B3 wave
- [ ] T-070 follow-up: run weaver WEAVE agents (prose/character/continuity) on Ch24-27 Severance sequence
- [ ] T-071: port remaining NEP runners (style alignment audit, dossier population) as needed
- [ ] P2 reconciliation: confirm v3-vs-v2 duplication delta and restate those issues
