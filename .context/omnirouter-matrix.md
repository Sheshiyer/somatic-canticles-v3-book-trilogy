# Omnirouter — Model + Skill Combo Routing Matrix (v1)

**Task:** T-069 · **Repo:** somatic-canticles-v3-book-trilogy · **Status:** planning matrix (no code router yet)

The "omnirouter" is the explicit, contract-first assignment of **lane → skill → model family → rubric → loop policy**
for every deeper pass on the trilogy. It generalizes the multi-model pipeline proven in the NVIDIA expansion v2
(`NVIDIA_EXPANSION_INIT.md`: gpt-oss-120b synthesis, nemotron-omni multimodal/reasoning, kimi reasoning/prose,
minimax tooling, control-model review) with the PAI skill stack (narrative-weaver, autoresearch, noesis-writer,
retrieval, visual-prompt).

No lane may begin until its rubric and loop bounds are frozen (contract-first parallelism).

---

## Lane 1 — RESEARCH / Source Lattice

| Field | Value |
|---|---|
| Purpose | Vault + repo source mining, dossier population, claim grounding |
| Skill | retrieval-skill (Meru semantic search) + noesis-writer Phase 2 (source lattice) |
| Model combo | reasoning model for synthesis (`gpt-oss-120b` / `kimi-k2-thinking`); `nv-embed-v1` for retrieval index |
| Rubric | Source Lattice Score ≥ 60/100; ≥3 distinct traced sources per section; citation audit clean |
| Loop | bounded intake → dossier → authority check (no canon touch) |
| Anti-drift | NEVER reference "the vault" in reader-facing output; sources = authors/works |

## Lane 2 — PROSE / Weave

| Field | Value |
|---|---|
| Purpose | Chapter/scene prose deepening, editorial transmutation |
| Skill | somatic-canticles-narrative-weaver (WEAVE mode: Prose Architect + Character Integrity Guardian + Continuity Sentinel) |
| Model combo | prose model (`kimi-k2-instruct` or equivalent long-form); control model for gate review |
| Rubric | 7 Quality Gates (see §4); PubMed precision; Alex Grey multi-sensory; Book voice register (B1 systems / B2 resonance / B3 perception) |
| Loop | internal DIAGNOSE → parallel agents → integrate (character flags override prose) |
| Anti-drift | NEVER alter plot beats/character decisions without moral-premise justification; opacity (no dumbing down) |

## Lane 3 — CRITIQUE / Rubric + Autoresearch

| Field | Value |
|---|---|
| Purpose | Score candidates, run keep/discard experiment loops |
| Skill | autoresearch (bounded batch: baseline → one variable → measure → keep/discard) + noesis-writer Albedo epistemic grammar + this repo's `WORKBENCH/STORYOPS/scripts/rubric_scan.py` |
| Model combo | critic/control model (separate from prose model — never self-grade); deterministic scanners for hard metrics |
| Rubric | 7 Gates + NEP learned gating contract (see §5) + epistemic claim modes (HOUSE-MODEL / TRADITIONAL-SOURCE / etc.) |
| Loop | 3–9 cycles max; stop after 2 stagnant cycles; `--dry-run` default; mutation requires opt-in |
| Anti-drift | Categorical leaks (matter-first framing, unsupported substrate claims) are findings, never silently repaired |

## Lane 4 — VISUAL / Editorial Image

| Field | Value |
|---|---|
| Purpose | Covers, section plates, marketing visual assets |
| Skill | visual-prompt-skill → brandmint provider pipeline |
| Model combo | image model (nano-banana / flux-2 family); Goethe palette + Amir Musich typographic style anchors |
| Rubric | brand palette (Void Black #070B1D, Sacred Gold #C5A017); aspect ratio contract; no lore-visual contradictions |
| Loop | plan images from converged text only (headlines from committed draft) |

## Lane 5 — MULTIMODAL EXTRACTION (conditional)

| Field | Value |
|---|---|
| Purpose | Extract lore/visual evidence from images, diagrams, video frames |
| Skill | NEP-005 lineage (visual seed) + media enrichment |
| Model combo | `nemotron-3-nano-omni-30b-a3b-reasoning` (multimodal reasoning) + vision captioning + `llama-nemotron-embed-vl-1b-v2` |
| Rubric | only runs when a visual candidate exists; otherwise route = "not selected yet" |
| Loop | extraction → dossier section 8 (Multimodal Evidence) |

---

## 4. The 7 Quality Gates (narrative-weaver) — the master rubric

1. **Aletheos Gate** — structural clarity (Aletheia) × embodied vitality (Pichet); fail on dry data or chaotic emotion.
2. **PubMed Gate** — every bio/science term real and correctly used.
3. **Alex Grey Gate** — bio processes rendered as multi-sensory visionary experience (show, not tell).
4. **Opacity Gate** — nothing dumbed down; reader learns by immersion.
5. **Moral Premise Gate** — at least one character's blind spot actively operating; Active Protagonist Loop running.
6. **Gardener Gate** — if Gardener appears: "sorrowful necessity," never villainy/gloating.
7. **Red Flag Gate** — energy/vibration/quantum/universe/shatter/frequency/resonant each ≤ 3× per 1000 words without specificity.

Gates 1, 5, 7 are partially deterministic → automated in `rubric_scan.py`. Gates 2–4, 6 require critic-model review.

## 5. NEP learned gating lessons carried forward (port: T-071)

From `nep_learned_gating_contract.py` (v1 → adapted as `WORKBENCH/STORYOPS/gating_contract.py`):
- Stage-draft acceptance: candidate must grow materially AND preserve spine; reject hard-ban contamination.
- Control-model style gate: braid balance, wit-lane distinction, temperature variation, double meanings, humor pressure-release — floor 6, post-acceptance floor 7.
- Additive repair fallback: insertion-only; raw insert saved before dedupe; never compress accepted prose.
- Voice acceptance repair: surgical, not plot-generating; control gate re-run after repair.
- Rejected-output policy: never reuse hard-failed candidates in later prompts; sanitize failure notes; switch to control model after repeated failures.
- Known anti-patterns: word-count-only acceptance, full-chapter repair compressing prose, scaffold terms (tarot/Enneagram) leaking onto page, false-success language resolving pressure early.

## 6. Example routing — Book 3 chapter deeper pass (T-070 pilot)

1. RESEARCH lane → dossier refresh for the chapter (sources, lenses, territory mechanics).
2. PROSE lane → weaver WEAVE with 3 parallel agents (prose / character-integrity / continuity).
3. CRITIQUE lane → `rubric_scan.py` baseline → critic model on Gates 2–4, 6 → autoresearch loop: one variable per cycle (e.g. filter-word sweep, then sensory density) → keep/discard by metric.
4. Record: before/after rubric deltas + autoresearch trace + gate evidence into `WORKBENCH/STORYOPS/runs/<chapter>/`.
5. MULTIMODAL lane only if visual candidates exist for the chapter's territory.

## 7. Contract-first rules (swarm-architect)

- Freeze this matrix before dispatching parallel work.
- One lane → one owner; critic model ≠ prose model.
- Canon (CHAPTERS/, COMPILED/) is read-only until a candidate passes all gates + wave close.
- Every run writes evidence; no evidence = not done.
