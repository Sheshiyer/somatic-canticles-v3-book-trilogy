# T-070 Wave 2: Chapters 18, 19, 27 — Evidence Summary
## Deeper-Pass Lane Execution

**Date:** 2026-07-26
**Pipeline:** DIAGNOSE → WEAVE (Prose Architect + Character Integrity + Continuity Sentinel) → Integration → Rubric Scan → Autoresearch Loop
**Status:** COMPLETE — 1 PASS, 2 WARN (voice register only, expected for Jian-heavy chapters)

---

## Chapter 18: The Synthesis Protocol

| Metric | Before | After |
|--------|--------|-------|
| Words | 10,534 | 3,338 (-7,196) |
| Lines | 547 | 349 (-198) |
| Voice | 16.2% | 30.9% |
| Verdict | WARN | WARN (voice only) |

**Structural problem:** Tight opening (1–182) + redundant expansion (183–547) with generic prose, contradictory numbers, duplicated crisis scenes, and engine-naming errors.

**Fixes applied:**
- Preserved lines 1–182 verbatim (three-vector frame, first timing test, 13.7s threshold)
- Extracted best material from expansion: four-conditions frame, "STABILIZED" critique, 6.6s semantic-correction discovery
- Cut: redundant test sequences, generic prose, duplicated paragraphs, "Anamnesis Engine" errors, bioluminescent/haptic drift
- Fixed: "Four separate pressures" → three vectors + Map as frame (continuity with Ch19 setup)

**Agent findings integrated:**
- Character Integrity: opening is arc-clean; expansion had two good islands (303–345, 367–485) surrounded by violations
- Continuity Sentinel: 6 CRITICAL issues found and resolved (4.2s record contradiction, 6.6s vs 8.9s ledger, engine naming, sternum marker migration, "fourth pressure" language, duplicated crisis scenes)

---

## Chapter 19: The Three-Point Problem

| Metric | Before | After |
|--------|--------|-------|
| Words | 9,897 | 7,766 (-2,131) |
| Lines | 1,146 | 1,058 (-88) |
| Voice | 27.8% | 28.0% |
| Verdict | WARN | WARN (voice only) |

**Structural problem:** Clean core (5–1125) + 1,900-word appendix graft (1126–1146) that re-explains everything already dramatized.

**Fixes applied:**
- Cut appendix entirely (1,900 words)
- Cut second House-pressure explanation (419–445)
- Compressed Gideon's wall discovery (363–383 → 3 lines)
- Cut four-column table (redundant with six constraints)
- Cut worktable move justification
- Merged ugly-map passages
- Tightened enemy view setup
- Cut "Useful. Not sufficient." echo

**Agent findings integrated:**
- DIAGNOSE identified the appendix graft as a completely different text with timeline contradictions, vocabulary breaks, and near-verbatim internal duplication
- All contradictions isolated to appendix block; core chapter internally consistent

---

## Chapter 27: The New Beginning

| Metric | Before | After |
|--------|--------|-------|
| Words | 8,102 | 4,996 (-3,106) |
| Lines | 805 | 709 (-96) |
| Voice | 39.4% | 41.1% |
| Verdict | WARN | **PASS** |

**Structural problem:** Two strong sections (S1: 5–260, S3: 384–805) separated by 2,500-word moss idyll (S2: 262–382) that dilutes voice register and pre-spends Corv's thematic payoff.

**Fixes applied:**
- Preserved S1 verbatim (habitability signal, first law, ground/tree/home)
- Replaced S2 with 182-word bridge (keeps only the fissure of light at tree's base)
- Preserved S3 verbatim (Corv's renunciation, Gideon's conversion, first rain, habitability definition, open ending)
- Fixed L260 seam ("that was enough for the night to begin")
- Cut pre-echo at L328 (protected L448's "Observation is enough" payoff)
- Deduped stars motif (kept L209–213 and L646, cut L290 and L314)

**Agent findings integrated:**
- DIAGNOSE identified S2 as the sole major redundancy problem — a 120-line interpolated idyll sitting between two strong registers
- S2's removal resolves the voice register WARN entirely

---

## Voice Register Note

Chapters 18 and 19 WARN on voice register (30.9% and 28.0% B3) because they are Jian-heavy chapters — his register is inherently B1 (system, protocol, diagnostic, measure, calibrat, signal, data, vector). The deterministic scanner counts B3 markers (perceiv, witness, author, see, perception, authorship, lens, frame) which are sparse in technical-protocol chapters. The WARN is expected and acceptable for these chapters' content.

---

## Autoresearch Loop Results

| Chapter | Cycles | Kept | Verdict |
|---------|--------|------|---------|
| Ch18 | 1 | 0 | WARN (voice) |
| Ch19 | 1 | 0 | WARN (voice) |
| Ch27 | 1 | 0 | **PASS** |

No transforms needed — all three chapters pass red-flag, duplication, epistemic, and opacity gates on first scan.

---

## Files

- `runs/Chapter-18-The-Synthesis-Protocol/final-candidate.md`
- `runs/Chapter-19-The-Three-Point-Problem/final-candidate.md`
- `runs/Chapter-27-The-New-Beginning/final-candidate.md`
- `runs/final-candidate/autoresearch-trace.json` (overwritten by each run; last trace is Ch27)
