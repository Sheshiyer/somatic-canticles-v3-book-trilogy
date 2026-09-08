# StoryOps Integration (v3)

**Tasks:** T-068 (integration) / T-069 (omnirouter) / T-070 (deeper rubric pilot) / T-071 (NEP port)

This workbench maps the NVIDIA expansion v2 story-ops workflow (NEP/SC_STORYOPS) onto the v3 canonical surface for
deeper, rubric-gated, autoresearch-driven passes. Canon (`CHAPTERS/`, `COMPILED/`) is read-only from this lane.

## Layout

```
WORKBENCH/STORYOPS/
├── README.md                    # this file
├── gating_contract.py           # NEP learned gating contract, adapted for v3 (port of nep_learned_gating_contract.py)
├── scripts/
│   ├── rubric_scan.py           # deterministic 7-Gate scanner (red flags, duplication, epistemic markers, dialogue shares)
│   └── autoresearch_loop.py     # bounded baseline -> one-variable -> measure -> keep/discard runner (dry-run default)
└── runs/                        # run-id/chapter artifacts (baseline scores, traces, gate evidence)
```

## Upstream lineage (nvidia-expansion v2)

- `NVIDIA_EXPANSION_INIT.md` — contract-first multi-model pipeline (omnirouter's ancestor)
- `scripts/run_nep_chapter_expansion.py` — batch chapter expansion runner (grew B2 68k, B3 106k working lanes)
- `scripts/run_nep_chapter_style_gate.py` / `run_nep_book_style_alignment_audit.py` — style gate + cross-chapter drift audit
- `scripts/nep_learned_gating_contract.py` — hard-won acceptance/rejection lessons (ported here)
- `06_WORKBENCH/SC_STORYOPS/story/` — intake surfaces, dossiers, authority registries, chapter summaries

## What changes for v3

| v2 (nvidia-expansion) | v3 (this repo) |
|---|---|
| expand 45k → 300–400k words | deeper pass on a locked 363k master — polish, not expansion |
| working lanes under 06_WORKBENCH | runs/ artifacts only; canon untouched until gates pass |
| NVIDIA NIM models | omnirouter matrix (`.context/omnirouter-matrix.md`) — model family per lane, skill-bound |
| style gate floors (tone) | full 7 Quality Gates + moral premise + epistemic grammar |

## Loop policy (autoresearch)

- Bounded: 3-9 requested cycles per batch; actual cycles are limited by the supplied transform list.
- One variable per cycle (e.g. filter-word sweep, sensory-density pass, duplication repair).
- Metrics: red-flag density, duplication paragraphs, epistemic tag coverage, voice-register marker share.
- Keep/discard recorded in `runs/<run-id>/<book>/<chapter>/autoresearch-trace.json` when `--run-id` is supplied.
- Default dry-run; omit `--apply` for dry behavior. Canon mutation only happens if a canonical chapter is passed with `--apply`, so campaign tests must use copied inputs for mutation proof and reserve promotion for wave-close review.

Example:

```sh
python3 WORKBENCH/STORYOPS/scripts/autoresearch_loop.py \
  CHAPTERS/book_1/Chapter-06-The-Synaptic-Crossroads.md \
  --transforms dedupe \
  --max-cycles 3 \
  --run-id cosmology-cr00-proof
```
