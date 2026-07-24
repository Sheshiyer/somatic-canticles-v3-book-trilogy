# T-070 Extended Pilot Report — Full Trilogy Baseline + B3 Deep Diagnostic

**Date:** 2026-07-24 · **Mode:** dry-run (canon untouched) · **Branch:** feature/storyops-omnirouter-T068-071

## 1. Full Trilogy Deterministic Baseline

27 chapters, ~363k words. Scanner: `WORKBENCH/STORYOPS/scripts/rubric_scan.py --book {1,2,3}`.

| Gate | B1 (8ch) | B2 (7ch) | B3 (12ch) | Trilogy |
|---|---|---|---|---|
| Red-flag density (≤3/1000) | 8/8 PASS | 7/7 PASS | 12/12 PASS | **27/27 PASS** |
| Verbatim duplication | 8/8 PASS | 7/7 PASS | 12/12 PASS | **27/27 PASS — 0 repeats** |
| Epistemic markers | 8/8 PASS | 7/7 PASS | 12/12 PASS | **27/27 PASS** |
| Opacity asides | 7 PASS / 1 WARN | 5 PASS / 2 WARN | 8 PASS / 4 WARN | 20 PASS / 7 WARN |
| Voice register | 0 PASS / 8 WARN | 5 PASS / 2 WARN | 7 PASS / 5 WARN | 12 PASS / 15 WARN |

**Key result:** No deterministic hard-fails anywhere in the trilogy. The v2-tree duplication artifacts (Ch13/19/22/27) and CJK typo are **absent** in v3 — P2 hygiene issues must re-verify against this repo before executing.

### Opacity-flagged chapters (7 total)

| Book | Chapter | Hits | Pilot result |
|---|---|---|---|
| 1 | Ch03 The Blood-Brain Barrier | 1 | keep cycle → 0 hits |
| 2 | Ch14 Three-Body Coordination | 1 | keep cycle → 0 hits |
| 2 | Ch15 Witness Integration | 2 | keep cycle → 0 hits, WARN→PASS |
| 3 | Ch16 The Wilt | 1 | keep cycle → 0 hits |
| 3 | Ch20 Convergence Point | 1 | keep cycle → 0 hits |
| 3 | Ch23 Flaw in the Code | 1 | keep cycle → 0 hits, WARN→PASS |
| 3 | Ch26 Architecture of New Reality | 1 | keep cycle → 0 hits |

All 7 opacity pilots produced keep cycles (dry-run). Candidates in `runs/<chapter>/final.candidate.md` for editorial review.

## 2. B3 Severance Sequence Deep Diagnostic (Ch24–27)

Agent: narrative-weaver DIAGNOSE mode. 44,222 words across 4 chapters.

### Critical findings

1. **Redundant alternate endings in all 4 chapters.** Each chapter contains 1–3 additional pasted-on endings after its true close, diluting the climax. ~2,000+ words of weaker restatement. Cut lines: Ch24 L1447–1495, Ch25 L1171–1221, Ch26 L468–572, Ch27 L806–858.

2. **The Gardener never appears.** The trilogy's antagonist is reduced to a "faint, receding pressure" (Ch24:1489) and a lowercase metaphor (Ch26:546). No confrontation, no temptation sequence, no reckoning. Largest unfulfilled promise of the trilogy.

3. **Amrita Protocol absent.** Named in the spec as the post-Vine creation mechanism but never appears in the text.

4. **Ch25 truncated mid-sentence** at L1221 ("Sona's"). Hard structural break.

5. **Scaffolding meta-text throughout** ("The chapter ended there," "Chapter 24 warned us," etc.) — Gardener Gate failures.

6. **Cosmology contradictions in redundant codas** — data-pads, supply drops, sidearms appear only in the to-be-deleted sections and contradict the void/creation cosmology.

7. **~20 Opacity-violating narrator-as-teacher lines** across Ch24–26 ("That was the severance," "The distinction mattered," etc.).

### Gate summary (Ch24–27)

| Gate | Ch24 | Ch25 | Ch26 | Ch27 |
|---|---|---|---|---|
| Aletheos | PASS | PASS | WARN | PASS |
| PubMed | PASS | PASS | PASS | PASS |
| Alex Grey | WARN | PASS | WARN | PASS |
| Opacity | FAIL | FAIL | FAIL | WARN |
| Moral Premise | PASS | PASS | PASS | PASS |
| Gardener | WARN | PASS | PASS | WARN |
| Red Flag | PASS | PASS | PASS | PASS |

**Moral Premise is the strongest gate** — all 4 chapters pass cleanly. The thematic architecture (coherence-through-integration vs control) is sound. The problems are structural (redundant endings) and editorial (opacity, scaffolding), not thematic.

## 3. Trilogy-Wide Continuity Diagnostic

Agent: narrative-weaver continuity mode. All 27 chapters cross-checked against chapter-registry, moral-premise-framework, style-voice-guide.

### Character arc verdicts

| Character | Arc | Verdict |
|---|---|---|
| Corv (Type 9, Bell Vector) | narrative → dialogue → witness without interpretation | **COHERENT** |
| Sona (Type 4, Note Vector) | sponge → lighthouse → channel not container | **COHERENT — strongest arc** |
| Jian (Type 5, Map Vector) | precision → compassion → exactness + astonishment | **COHERENT** (Ch23 discovery under-dramatized) |
| Gideon (Type 8, Coherence Vector) | containment → passage-guardian | **COHERENT — Ch24 near-abort best payoff** |
| The Gardener | pruning function → full encounter → evaporates | **COHERENT in B3; W1 contradiction Ch4 vs Ch17** |
| Aurora | warning voice → vanishes | **DANGLING** |
| Node Quoril | external antagonist → never returns | **DANGLING** |
| Anvel Verath | appears at climax with zero setup | **UNSUPPORTED BACKSTORY** |

### Critical world-rule violations

- **W1 CRITICAL:** Ch4 shows team watching Gardener prune; Ch17 stages "first encounter" — unreconciled
- **W2 CRITICAL:** Anamnesis Engine goes from team's instrument (B1) to adversarial jurisdiction (B3) with no marked transition
- **W3 WARNING:** Khalorēē used 3 ways (field/personal/person) never disambiguated
- **W5 WARNING:** "Trideca" never appears in manuscript text
- **W6 WARNING:** 13 Symbolic Lenses (registry's per-chapter system) almost entirely absent from prose

### Setup/payoff ledger highlights

**Best plant-and-payoff:** Entropy Plague (Ch1:49 → Ch16) — planted page 1, fired page 1 of Book 3.

**Dangling guns (deliberately planted, never fired):**
- S5: Obsidian seed with ninefold glyph + memorized coordinates (Ch8)
- S6: Jian's anomaly bearing in AM-38-orphan-routes (Ch8)
- S7: Node Quoril / Luminth filings market pressure (Ch8)
- S8: Aurora (Ch2, Ch4, Ch10 — vanishes from B3)
- S11: Corv's obsidian shard "for later" (Ch6)

**Unsupported payoffs (appear with full weight, zero prior setup):**
- P1 CRITICAL: Anvel Verath — emotional fulcrum of the Bell climax, first named inside the climax (Ch24:376)
- P2 CRITICAL: Mira Verath as trilogy through-subject — 23 sessions asserted in Ch16, never named in B1–B2
- P6: Review queue as active chamber participant

### Timeline flags

- **T1 CRITICAL:** Ch16 opens 6 weeks after B2 with 23 Verath sessions behind them, but B1+B2 depict ~15 unnumbered descents never named Verath — subject-identity gap
- **T2 WARNING:** Engine activation staged 3 times (Ch1 boots, Ch3 ignites, Ch8 registry claims boot)

### Voice register flags

- **V2 CRITICAL:** B2 Ch12 back half slides into B1 procedural register + duplicate seams
- **V5 CRITICAL:** B3 Ch27 grafted coda in hard-SF camping idiom contradicts post-Vine creation frame
- **V4 NOTE:** B3 Ch16 opens in B1 register — likely intentional (instruments failing is the story) but should be verified

## 4. Merged Prioritized Fix List (B3 diagnostic + continuity diagnostic, severity-ranked)

### CRITICAL — structural integrity

| # | Fix | Source | Effort |
|---|---|---|---|
| 1 | Delete redundant alternate endings (Ch24 L1447–1495, Ch25 L1171–1221, Ch26 L468–572, Ch27 L806–858) | B3 diag | Cut-only, ~2000w |
| 2 | Fix Ch25 truncation (L1221 "Sona's" mid-sentence) | B3 diag | 1 line |
| 3 | Cut Ch27 grafted coda (L806+, supply-drop/sidearm contradicts void cosmology) | Both | Overlaps #1 |
| 4 | Reconcile B2 Ch12 register collapse + duplicate seams (L150–251) | Continuity | Re-cut ~100 lines |

### CRITICAL — content gaps

| # | Fix | Source | Effort |
|---|---|---|---|
| 5 | Write Gardener confrontation/temptation sequence (Ch24 or Ch25) — 4 cages offered and refused | B3 diag | New prose, ~2000w |
| 6 | Subject-identity bridge: name "Verath" in B1 Ch1 + once in B2 (≤3 lines) | Continuity | 2-3 lines |
| 7 | Anvel Verath setup: seed in Ch16 + Ch17 (1 paragraph each) | Continuity | 2 paragraphs |
| 8 | Gardener "first encounter" reconciliation (Ch4 local function vs Ch17 source) | Continuity | 1-2 lines in Ch17 |
| 9 | Engine agency drift: mark transition from instrument to adversarial jurisdiction (Ch21/22) | Continuity | 1 beat |

### HIGH — editorial quality

| # | Fix | Source | Effort |
|---|---|---|---|
| 10 | Remove scaffolding meta-text throughout 24–27 | B3 diag | ~15 line cuts |
| 11 | Reduce Opacity-violating narrator-as-teacher lines (~20 instances in 24–26) | B3 diag | Cut/rewrite |
| 12 | Obsidian seed + orphan-route bearing: pay off or cut (Ch8 plants) | Continuity | Decision + execution |
| 13 | Node Quoril / Luminth filings: thread into B3 review-queue or excise | Continuity | Decision + execution |
| 14 | Gardener interiority violation: recast as inference-through-effect (Ch17–18) | Continuity | Rewrite ~5 lines |

### MEDIUM — polish

| # | Fix | Source | Effort |
|---|---|---|---|
| 15 | De-duplicate recycled imagery in Ch26/27 (8+ near-identical beats) | B3 diag | Selective cuts |
| 16 | Khalorēē semantic disambiguation (Ch16 definitional touchstone) | Continuity | 1-2 lines |
| 17 | The Wilt resolution line in Ch26/27 | B3 diag | 1 line |
| 18 | Amrita Protocol: anchor or consciously cut | Both | Decision |
| 19 | Trideca / 13-Lens: strip from bible or seed into prose | Continuity | Decision |

## 5. What's Genuinely Strong (do not touch)

- Entropy Plague plant-and-payoff (Ch1→Ch16)
- Sona's full enantiodromia (strongest arc in trilogy)
- Gideon's Ch24 near-abort
- B2 Ch15 standardization demand inverting into Ch24 replay refusal
- 13.7-second countdown as braided register
- Ch27's four truth moments (before grafted coda)
- Moral Premise gate: all 4 Severance chapters PASS cleanly

## 6. Next Actions

- [x] Continuity agent report (complete)
- [ ] Create GitHub issues for the 4 CRITICAL structural fixes
- [ ] Create GitHub issues for the 5 CRITICAL content gaps
- [ ] Create GitHub issues for HIGH editorial items
- [ ] Decide: merge redundant-ending cuts as single PR or per-chapter PRs
- [ ] Commission Gardener confrontation sequence (weaver WEAVE mode)
- [ ] Voice-register heuristic calibration (B1/B3 braid expected by design)
