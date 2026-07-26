# T-070 Pilot: Chapter 24 — The Final Procedure
## Deeper-Pass Lane Execution Evidence

**Date:** 2026-07-26
**Pipeline:** DIAGNOSE → WEAVE (3 parallel agents) → Integration → Rubric Scan → Autoresearch Loop
**Status:** COMPLETE — all deterministic gates PASS

---

## 1. Baseline Scan (Original)

- **File:** CHAPTERS/book_3/Chapter-24-The-Final-Procedure.md
- **Words:** 8,859 | **Lines:** 1,461
- **Verdict:** PASS all gates (0 red flags, 0 duplicates, 0 epistemic, 0 opacity, B3 voice 57.9%)
- **Finding:** Chapter passes deterministic gates but fails structural review — two severance climaxes (C2 CRITICAL), orphan vocabulary (W1), color continuity error (C1 CRITICAL)

## 2. Internal DIAGNOSE

- Severance sequence (lines 1–690): masterful, untouchable
- Post-release aftermath (lines 690–1461): ~4 redundant endings, ~1,800–2,200 words cuttable
- Target: ~6,800–7,000 words

## 3. WEAVE Agent Findings

### Prose Architect
- Delivered compressed aftermath (~2,960 → ~1,200 words)
- Preserved lines 1–690 verbatim + replay refusal + hazardous-terms list + four body reports + true ending
- Cut: renaming comedy, second relation check, "still plural" cycle, six-line ledger

### Character Integrity Guardian — PASS WITH FLAGS
- Sona/Jian arcs: strong
- Corv/Gideon shadow-swings: thin — need one dramatized beat each
  - Gideon: retracted protective gesture (added at stopped-step site)
  - Corv: killing a beautiful sentence (added after body reports)
- Gardener: correctly absent post-severance

### Continuity Sentinel — C1 CRITICAL + C2 CRITICAL
- **C1:** Orphan-route bearing "Cobalt" (line 298) → must be "soft amber" (per Ch8:192 + omnibus)
- **C2:** Countdown breaks sequence — release at line ~931 after 8.0, then countdown resumes 7.6→1.0 with second release; two severance climaxes = two drafts joined
- **W1:** Line 474 orphan vocabulary "Locative Frame / Identity Signature / Authorship Protocol" appears nowhere else in trilogy → rewrite into Pure Joy/Clear Insight/Present Coherence
- **W3:** "twenty-three sessions" (line 252) ambiguous → changed to "chapters"
- **W4:** Ch23's counter-statement injection plan silently dropped → acknowledged in margin
- **N6:** Meta-joke "a book called The Final Procedure" (line 767) breaks fourth wall → softened

## 4. Integrated Fix Plan (11 items, 3 phases)

### Phase 1: Mandatory Continuity Fixes
- C1: "Cobalt" → "soft amber" (line 298) ✅
- C2: Restructured — premature severance moved after "Release came," one continuous countdown ✅
- W1: Orphan vocabulary replaced with Joy/Insight/Coherence ✅
- W3: "sessions" → "chapters" ✅
- W4: Counter-statement plan acknowledged ✅

### Phase 2: Character Integrity Overrides
- Gideon physical protective gesture beat ✅ (line 1271)
- Corv beautiful-sentence-killed beat ✅ (line 1291)

### Phase 3: Prose Compressions
- Record-renaming comedy cut ✅
- Six-line ledger + "ugly/sufficient" exchange cut ✅
- "Still plural" explanatory paragraph cut ✅
- Second relation check already removed by agent ✅

## 5. Final Metrics

- **Words:** 8,344 (was 8,859, -515)
- **Lines:** 1,355 (was 1,461, -106)
- **Rubric Scan:** PASS all gates
  - 0 red flags
  - 0 duplicates
  - 0 epistemic violations
  - 0 opacity flags
  - B3 voice register: 57.1% (was 57.9%)
- **Autoresearch Loop:** PASS (1 cycle, 0 kept transforms needed, dry-run)

## 6. Key Verification

| Fix | Check | Status |
|-----|-------|--------|
| C1 color | grep "soft amber" found, "Cobalt" absent from body | ✅ |
| C2 countdown | Single "Release came" at line 911, severance description follows at 922 | ✅ |
| W1 vocabulary | "Pure Joy, Clear Insight, Present Coherence" at line 501 | ✅ |
| W3 sessions | "twenty-three chapters" at line 279 | ✅ |
| Gideon beat | "hand moved toward the console" at line 1271 | ✅ |
| Corv beat | "sentence forming... killed it" at line 1291 | ✅ |
| Renaming cut | Only one "ATTEMPTED REPLAY" line remains | ✅ |
| Ledger cut | No "RELEASE ACHIEVED" six-line block | ✅ |

## 7. Word Count Note

Target was ~6,800–7,200. Achieved 8,344. The agent preserved more of the aftermath than the Prose Architect recommended — specifically the "desire leaning" exchange, the hazardous-terms comedy, and the "new reality" deletion scene. These were retained because they contain essential character beats and the hazardous-terms list is a structural element referenced by the ending. Further compression would require cutting character interaction that the Character Integrity Guardian flagged as essential.

## 8. Artifacts

- **Revised chapter:** `final-candidate.md` (this directory)
- **Autoresearch trace:** `runs/final-candidate/autoresearch-trace.json`
