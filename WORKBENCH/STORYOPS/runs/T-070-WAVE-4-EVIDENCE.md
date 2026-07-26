# T-070 Wave 4 Evidence — Book 1 (Ch01–08) + Book 2 (Ch14 pending, Ch15)

**Date:** 2026-07-26
**Lane:** DIAGNOSE → WEAVE (Prose Architect) → rubric_scan → autoresearch dry-run
**Scope:** Book 1 Ch01–08, Book 2 Ch15. Book 2 Ch14 remains (last unprocessed WARN chapter).

## Pattern Confirmed (Same as Book 3)

Every WARN chapter = strong core + stitched AI re-passes retelling the same beats (echo passes, appendix grafts, duplicate climaxes, register collapse, name drift). Fix = preserve core verbatim, salvage best lines from cut zone, cut passes, graft true ending.

## Results

| Ch | Book | Before (w) | After (w) | Δ | Verdict | Notes |
|----|------|-----------|-----------|---|---------|-------|
| 01 | 1 | 10,898 | 7,986 | -26.7% | WARN voice-only | F compressed 2,400→950; H+I+J merged 4,000→2,000; L cut; timers reconciled to one (5:42); Mira paid off; duplicate "mineral and patient" removed |
| 02 | 1 | 10,308 | 3,945 | -61.7% | WARN voice-only | Draft A (1–169) verbatim + ~550w salvage (Rule 9.2, garnet vein, Vexian algae, cortisol banter); exits canonized to ONE; D (foreign lab pass) cut; file was truncated mid-sentence at 439 |
| 03 | 1 | 13,595 | 7,422 | -45.4% | WARN voice-only | A–E+G+I+M verbatim; F compressed ~3,000→1,300; H/K/L cut; J (present-tense coda) cut; ONE recorder close kept; opacity aside fixed ("Which means"→"So") |
| 04 | 1 | 16,475 | 7,636 | -53.6% | WARN voice-only | Seam at 537; palace-heist draft cut ("Corb" typo, Gardener-as-jokey-mentor violation); ends "kept the receipt." |
| 05 | 1 | 16,383 | 7,965 | -51.4% | WARN voice-only | A–D preserved, E salvaged (silence treaty, black-silk collateral, blood-drop threshold), F–I cut (Mira/nanites); sparrow/bell closer grafted; 1 legitimate "counter-frequency" |
| 06 | 1 | 15,974 | 2,970 | -81.4% | WARN voice-only | Draft A (1–119) + ~330w salvage; name drift purged (Jara/Tamsin/Kade/Amri) |
| 07 | 1 | 15,000 | 10,442 | -30.4% | WARN voice-only | Seams 312/465/718 merged; ends at calibration ring; 1 legitimate "frequency" |
| 08 | 1 | 21,130 | 4,317 | -79.6% | **PASS** | 43.8% B1 register; 12 stitched passes cut; all 19 Ch24 dependencies preserved exactly once (soft amber 192, cobalt 40/208, 0.97 trust coherence, seed coords `9.3.4N \| 12.7.2E \| -0.47 depth`, `AM-38-orphan-routes`) |
| 15 | 2 | 22,884 | 2,925 | -87.2% | WARN voice by design | Two-chapters-stitched at 168; tech-thriller cut; ~1,100w Wilt-bridge ending written to set up Book 3 (ends on dissonance: "The cost of witness is the willingness to remain answerable, even when the field offers to carry the answer for you."); canon file was truncated mid-sentence |

**Book 1 total:** 127,762 → 52,683 words (-58.8%)
**Ch15 (Book 2):** 22,884 → 2,925 (-87.2%)

## Gate Results (all revised candidates)

- red_flag: PASS (0.0–0.48/1000)
- duplication: PASS (0 verbatim repeats)
- epistemic: PASS (0 markers)
- opacity(asides): PASS (0 hits, after Ch03 fix)
- voice register: WARN on Ch01–07 (expected), PASS on Ch08

## Voice WARN Assessment

Book 1 voice WARNs are the documented scanner-limitation pattern, not revision failures:

1. **Scanner detects register by path substring** — candidates scanned via `/tmp/book_1/` copy so Book 1 markers (system/protocol/signal/data/vector) are used. All chapters scored against the correct register set.
2. **Jian-heavy technical chapters score low on B1 markers** — Ch01–07 are dominated by Jian/Corv technical dialogue and field-procedure prose; the B1 lexicon ("system", "protocol", "signal") is present but sparse relative to total register words. Same pattern as Book 3 Ch16/18/19/20 (voice-only WARNs accepted and pushed).
3. **Sona-heavy somatic chapters score B2 resonance markers** instead of B1 — Ch04 (15% B1) is Sona-POV; register shift is diegetic, not drift.
4. **"frequency" red flags in Ch05/Ch07** are legitimate technical usage (counter-frequency, calibration), not violations.
5. **Ch15 voice WARN is by design** — the new Wilt-bridge ending deliberately uses Book 3 register (witness/author/perception) as a bridge into Book 3's concerns.

## Autoresearch Loop (dry-run)

- Ch01: 1 cycle, 0 kept, no improvement (baseline already clean)
- Ch02: 1 cycle, 0 kept, no improvement
- Ch03: 1 cycle, 0 kept, 1 opacity aside → fixed manually, re-scan PASS
- Traces: `runs/Chapter-0{1,2,3}-*/autoresearch-trace.json`

## Cross-Chapter Dependencies Honored

- Ch08:192 "soft amber, two-second cadence" — orphan-route bearing (Ch24 dependency)
- Ch23 cut-line anchoring beat retained for Ch24:9 reference
- Ch26 obsidian-seed ending preserved verbatim for Ch27
- Ch15 new Wilt-bridge ending sets up Book 3 opening
- Ch08 seed coordinates salvaged from cut zone and grafted exactly once

## Remaining

- **Ch14** (Book 2, 14,818w, 47.9% voice, 5 flags, 1 opacity) — last unprocessed WARN chapter; existing runs/ candidate is a dry-run no-op (canon + opacity bracket only), needs full deeper-pass treatment.
