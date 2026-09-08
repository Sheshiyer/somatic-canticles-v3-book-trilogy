# CR-03 — Developmental and relationship architecture

Status: planned · Scope: implementation plan, not execution receipt

## Outcome

Build a causal transformation structure for the full trilogy using the successful pilot.

## Entry and ownership

- Dependencies: CR-02
- Accountable owner: Developmental editor. One writer owns a chapter within a wave. Writers are not alone in the codebase: preserve others' edits and coordinate shared files.
- Read [CONTEXT](../CONTEXT.md), [StoryOps adapter](../STORYOPS-ADAPTER.md), [rubric](../RUBRIC.md), relevant critique input and latest accepted predecessor receipts.
- Canon decisions not yet accepted remain proposals. Work that does not depend on them can proceed; fence only dependent mutations.

## Tasks

### CR-03.01 — Plan four reversible character trajectories

**Action:** For each character map useful defense, short-term benefit, hidden cost, recognition, changed attempt, relapse/overcorrection, repair and transfer. Include positive decisive action and ordinary pleasure; every person carries all sheath layers.

**Deliver:** runs/<run>/four-character-plan.md

**Verify:** Four distinct trajectories with source and proposed scene IDs; no fixed engine ownership or inevitable chart-derived motive.

**Depends on:** CR-02

### CR-03.02 — Plan six pair arcs and whole-team changes

**Action:** Specify setup, misreading, negotiated action, aftermath and later change for all six pairs. Add coalition/workload/absent-member tests the pair readings cannot supply. Do not require every character to speak in every scene.

**Deliver:** runs/<run>/six-pair-plan.md; group-dynamics.md

**Verify:** All six pairs have causal development; membership does not require emotional agreement, exposure of private thoughts, or permanent dependence.

**Depends on:** CR-03.01

### CR-03.03 — Allocate recurrence and pruning

**Action:** Assign each retained/new beat to chapters and identify what it replaces. Decide where no new practice or engine mention belongs. Ensure Chapter 16 time passage and final ordinary life carry changes without claiming irreversible growth.

**Deliver:** runs/<run>/chapter-beat-allocation.json

**Verify:** Every proposed beat has a function and owner; no duplicate moral lecture; each long arc has a traceable return.

**Depends on:** CR-03.02

### CR-03.04 — Prepare book wave packets

**Action:** Produce ordered scene packets for Phases 04–06, naming cross-book dependencies and protected downstream facts. Freeze input versions for each wave.

**Deliver:** runs/<run>/wave-packets/

**Verify:** Writer can start each packet without inventing decisions, dates, or source authority; every cross-wave edge recorded.

**Depends on:** CR-03.03

## Candidate and exit contract

Use existing StoryOps runs with a unique campaign/run ID after CR-00 isolation is satisfied. Preserve baseline, raw candidate, exact diff, reviewer identity, gate evidence and keep/discard rationale. A mechanical keep is not an accepted chapter. If two cycles stagnate, stop and return to diagnosis with sanitized failure lessons.

Close this phase only when each task has its named evidence and unresolved findings have explicit owners/dependency fences. Record actual execution status in STATE.md and plan.json; never mark tasks complete because this plan exists. Promotion and publication are distinct actions.
