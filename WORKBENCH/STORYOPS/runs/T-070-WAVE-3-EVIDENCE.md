# T-070 Wave 3: Chapters 16, 20, 23, 26 — Evidence Summary
## Deeper-Pass Lane Execution

**Date:** 2026-07-26
**Pipeline:** DIAGNOSE → WEAVE (Prose Architect) → Integration → Rubric Scan → Autoresearch Loop
**Status:** COMPLETE — 2 PASS, 2 WARN (voice register only, expected for Jian-heavy chapters)

---

## Chapter 16: The Wilt

| Metric | Before | After |
|--------|--------|-------|
| Words | 24,922 | 6,097 (-75.5%) |
| Lines | 935 | 357 (-61.8%) |
| Voice | 30.8% | 37.2% |
| Verdict | WARN | WARN (voice only) |

**Structural problem:** Strong core (A+B+G, ~6,000 words) buried under 5-6 stitched-on AI-generation passes (C-L, ~18,000 words). Worst case in the book.

**Fixes applied:**
- Preserved A (1–160): Discovery — Wilt detected, team converges, "pruning not relapse" insight
- Preserved B (161–199): Jian's restraint — "Waiting also teaches"
- Compressed D (281–452 → ~600 words): Houses pressure, null-field failure, ledger-of-failure
- Preserved G (611–680): Memory vigil — "Do you remember her?"
- Created ONE decision-to-descend beat (~600 words) from best of five attempts
- Cut C, E, F, H, I, J, K entirely (~18,000 words)
- Ended with L's final line (935) as closer
- Fixed: Corv pronoun corruption (section I cut), "universe" ×2 → world/field, red flags in cut sections died

**Agent findings integrated:**
- DIAGNOSE identified 12 sections, 5× repeated descent decision, Corv pronoun corruption at line 725
- Existing runs/final.candidate.md was unusable (dry-run no-op, only one opacity bracket added)

---

## Chapter 20: The Convergence Point

| Metric | Before | After |
|--------|--------|-------|
| Words | 10,376 | 8,114 (-21.8%) |
| Lines | 1,371 | ~1,250 (-8.8%) |
| Voice | 25.0% | 34.8% |
| Verdict | WARN | WARN (voice only) |

**Structural problem:** Strong core (5–1337) + grafted second draft coda (1338–1371) with contradictory props and register.

**Fixes applied:**
- Preserved lines 5–1337 with compressions:
  - Cut "I want to narrate it" encore beat (customs office exchange)
  - Cut 3rd and 4th Sona/Jian archivist gags
  - Compressed 3rd and 4th review-trace cycles
  - Trimmed READY/NO tail
- Cut graft (1338–1371) entirely — "universe" red flag died with it
- Fixed opacity: line 595 "You are looking at it like you know with only half your body" → "Gideon's gaze stayed on him a moment longer, steady and unreadable"
- Fixed opacity: line 1201 "Which means no one confuses..." → "No one confuses..."
- Ends at "It carried a cleaner burden"

**Agent findings integrated:**
- DIAGNOSE identified the graft boundary at line 1337 (true ending) + prop/register discontinuity
- "Do not make it beautiful" injunction appeared 8+ times; kept first three, cut rest
- Existing runs/final.candidate.md was unusable (dry-run no-op)

---

## Chapter 23: The Flaw in the Code

| Metric | Before | After |
|--------|--------|-------|
| Words | 9,352 | 6,592 (-29.5%) |
| Lines | 1,136 | ~1,050 (-7.6%) |
| Voice | 54.8% | 73.9% |
| Verdict | WARN | **PASS** |

**Structural problem:** Finished draft (1–1051) + two inferior grafts (1052–1136) with stock imagery and register break.

**Fixes applied:**
- Preserved lines 1–1051 verbatim (or minimal B-section tightening)
- Cut lines 1052–1136 entirely (both grafts)
- Added 7-line cut-line anchoring beat before "No severance today" — gives "the Chapter 23 cut-line" a concrete referent for Ch24's reference
- Ends at "Jian added the line."

**Ch24 dependencies preserved:**
- Cut-line: new anchoring beat provides referent
- Hidden authorship: lines 492, 641, 831 preserved
- Disproof-test method: lines 618–734 preserved
- "No severance today": line 1030 preserved
- Counter-statement injection: referenced nowhere in Ch24, safely deleted with graft

**Agent findings integrated:**
- DIAGNOSE identified three drafts, not two — Draft A (1–1051) complete, Drafts B+C (1052–1136) inferior
- Opacity flag was inside Draft C, died with it
- Existing runs/final.candidate.md was unusable (dry-run no-op)

---

## Chapter 26: The Architecture of New Reality

| Metric | Before | After |
|--------|--------|-------|
| Words | 8,304 | 3,639 (-56.2%) |
| Lines | 473 | 374 (-20.9%) |
| Voice | 36.4% | 45.9% |
| Verdict | WARN | **PASS** |

**Structural problem:** Tight core (A+B) + three duplicate passes (C+D+E) + good ending (F+G+H). Same "moss idyll" pattern as Ch27.

**Fixes applied:**
- Preserved A (5–28) and B (30–180) verbatim — threshold and four conditions
- Cut C, D, E (182–288) entirely — three duplicate passes
- Kept F (290–363) with minor trimming — merged "chair" joke
- Preserved G (365–458) verbatim — codicil
- Preserved H (460–472) verbatim — obsidian seed ending (Ch27 depends on it)
- Fixed opacity: line 23 "Which means we have to." → "So we have to."

**Ch27 dependencies preserved:**
- Obsidian seed, ninefold glyph, coordinates, "That restraint became the field's final architecture" — untouched
- Gideon's membrane, Jian's direction — preserved in section B
- Four agreements structure — preserved

**Agent findings integrated:**
- DIAGNOSE identified three duplicate passes re-describing same beats (floor forms ×3, rain scent ×3, "floor listens" joke ×3)
- Existing runs/final.candidate.md was unusable (dry-run no-op)

---

## Voice Register Note

Chapters 16 and 20 WARN on voice register (37.2% and 34.8% B3) because they are Jian-heavy chapters — his register is inherently B1 (system, protocol, diagnostic, measure, calibrat, signal, data, vector). The deterministic scanner counts B3 markers (perceiv, witness, author, see, perception, authorship, lens, frame) which are sparse in technical-protocol chapters. The WARN is expected and acceptable for these chapters' content.

---

## Autoresearch Loop Results

| Chapter | Cycles | Kept | Verdict |
|---------|--------|------|---------|
| Ch16 | 1 | 0 | WARN (voice) |
| Ch20 | 1 | 0 | WARN (voice) |
| Ch23 | 1 | 0 | **PASS** |
| Ch26 | 1 | 0 | **PASS** |

No transforms needed — all four chapters pass red-flag, duplication, epistemic, and opacity gates on first scan.

---

## Files

- `runs/Chapter-16-The-Wilt/final-candidate.md`
- `runs/Chapter-20-The-Convergence-Point/final-candidate.md`
- `runs/Chapter-23-The-Flaw-in-the-Code/final-candidate.md`
- `runs/Chapter-26-The-Architecture-of-New-Reality/final-candidate.md`
- `runs/final-candidate/autoresearch-trace.json` (overwritten by each run; last trace is Ch26)
