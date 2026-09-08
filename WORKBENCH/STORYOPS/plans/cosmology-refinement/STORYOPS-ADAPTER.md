# How these phases use StoryOps

This is a planning adapter, not a replacement execution controller. Reuse WORKBENCH/STORYOPS scripts, source manifests, seven gates, independent critique, runs and wave-close records. No .planning project or GSD phase lifecycle is initialized by this package.

## Existing lanes

Source lattice / diagnosis → one bounded candidate hypothesis → independent critique → deterministic scan → keep/discard → wave-close editorial decision → explicit promotion → source-pinned export.

Use the Ether-First manifest builder and validator for hashed canon/skill/reference inputs. Its controller can generate evidence and structural candidates; it does not establish literary quality. Only canon/blog roles are ingested for claim extraction in the inspected controller; reference/skill entries record provenance and are not automatically fed into every pass. Supply necessary brief/canon decisions explicitly to the writer instead of assuming a manifest path causes prompt grounding.

## Preparation defects to resolve in CR-00

| Observed source behavior | Required handling |
|---|---|
| gating_contract.py rejects non_additive_or_compressing_change | Prepare a versioned exception/removal with scene-spine tests before compression work. Do not silently ignore the contract. |
| README/example mentions --dry-run; autoresearch parser has no such flag | Omit --apply for dry-run behavior. Correct documentation during the tooling task. |
| autoresearch_loop.py can copy final candidate over its supplied input | Never pass canon with --apply. Test mutation only on temporary copies; promotion remains separate. |
| Run directory keyed only by chapter stem | Repeated runs can overwrite traces and preserve a stale baseline. Add run identity to the existing runner or isolate each run in a disposable worktree before using it. |
| max-cycles clamps the limit but slices the provided transform list | Record actual cycles; one transform does not mean three experiments. No forced filler cycles. |
| Metric vector and automatic keep are lexical proxies | Separate lexical improvement from literary selection. Six non-deterministic gates remain independently reviewed. |
| Scanner derives book register from path substring | Keep copied candidates beneath book_1/book_2/book_3 or use the actual scan_file function with explicit book. |
| opacity-strip adds editorial bracket markers | Such candidates are review annotations, not publishable prose; remove review residue through an explicit candidate change and rescan. |
| Existing omnirouter matrix says planning-only and contains historical model IDs | Use current Temperance routing/availability receipts. Do not claim the historical matrix is a live router. |

## Execution ownership and routing

Hands implementation runs in the project’s authorized Superset/Claude workspace with current noesis-* routing. Phase numbers are editorial milestones, not the seven alchemical stages. Resolve current provider capacity before dispatch; retain actual provider/model and outcome, including failure. The previous review exhausted many gateway attempts, so do not repeat an unbounded dispatch or treat a resolved route as successful work.

One writer owns a chapter in a wave. Independent critics read the same frozen candidate. Parallel source research or non-overlapping chapter work is possible only after upstream beat dependencies are pinned. Integration and wave close are serial. Everyone preserves other writers’ state and avoids shared-file changes without coordination. Do not create duplicate worker branches or tasks automatically from this planning JSON.

## Per-run evidence layout

After CR-00 run isolation is available, use a unique campaign/run namespace under existing runs:

```text
runs/cosmology-refinement/<run-id>/
  source-manifest.json
  brief.md
  book_1/ch06/baseline.md
  book_1/ch06/raw/cycle-01.md
  book_1/ch06/candidates/cycle-01.md
  book_1/ch06/cycle-01.patch
  book_1/ch06/scanner-before.json
  book_1/ch06/scanner-after.json
  book_1/ch06/critic-review.md
  autoresearch-trace.json
  continuity-ledger.json
  wave-close.md
```

This directory convention is proposed input/output organization; current autoresearch does not implement the run-id option. CR-00 must reconcile that before invoking it for repeated candidates. Do not write to historical T-070 runs.

## Actual read-only commands available now

Run from the planning worktree root:

```sh
python3 WORKBENCH/STORYOPS/scripts/rubric_scan.py CHAPTERS/book_1/Chapter-06-The-Synaptic-Crossroads.md --json
python3 WORKBENCH/STORYOPS/scripts/ether_first/manifest.py validate WORKBENCH/STORYOPS/plans/cosmology-refinement/evidence/source-manifest.json
python3 WORKBENCH/STORYOPS/scripts/autoresearch_loop.py --help
python3 WORKBENCH/STORYOPS/scripts/ether_first_loop.py --help
```

Manifest validate checks schema; the planning verification also calls verify_manifest to rehash bytes. Before real execution, regenerate a manifest for that exact source revision and verify it. Evidence baseline.json supplies a fresh scanner reading from this planning run; it does not mean the tooling preparation tasks are complete.

## Stop and recovery

Stop on missing source, unexpected input changes, fabricated fact, hard-ban contamination, exhausted route, or two stagnant cycles. Preserve evidence and the baseline; sanitize failure notes before the next attempt and keep rejected prose out of repair prompts. A failed literary candidate returns to diagnosis; a broken tool gets a bounded owning-repository fix. A pending author decision blocks only dependent edits. No automatic canon rollback, reset, merge or publication follows.
