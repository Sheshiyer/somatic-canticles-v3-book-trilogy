# CR-10 — Exports, delivery and measured re-entry

Status: planned · Scope: implementation plan, not execution receipt

## Outcome

Produce faithful delivery artifacts and learn from readers without scoring their inner development.

## Entry and ownership

- Dependencies: CR-07
- Accountable owner: Publishing owner + content editor. One writer owns a chapter within a wave. Writers are not alone in the codebase: preserve others' edits and coordinate shared files.
- Read [CONTEXT](../CONTEXT.md), [StoryOps adapter](../STORYOPS-ADAPTER.md), [rubric](../RUBRIC.md), relevant critique input and latest accepted predecessor receipts.
- Canon decisions not yet accepted remain proposals. Work that does not depend on them can proceed; fence only dependent mutations.

## Tasks

### CR-10.01 — Rebuild compiled books from accepted source

**Action:** Regenerate compiled books, front/back matter and relevant audio source maps from the exact accepted chapter revision. Compare all bodies and expected ordering.

**Deliver:** COMPILED candidates; export-parity.json

**Verify:** 27 source bodies accounted for; no older compiled passage re-enters canon; no unexplained drift.

**Depends on:** CR-07

### CR-10.02 — Align wiki/audio/brand contracts

**Action:** Update only affected discovery and delivery content, correcting obsolete counts, access promises and terminology after their decisions are accepted. Regenerate media only where text changes require it.

**Deliver:** Delivery candidate manifest + provenance

**Verify:** Each artifact has source revision; no unseen asset or stale marketing statement treated as accepted.

**Depends on:** CR-10.01

### CR-10.03 — Prepare release review

**Action:** Bundle manuscript, reader evidence, export hashes and optional companion readiness. The book may release independently if complete; companion release requires Phase 09 and its own acceptance.

**Deliver:** runs/<run>/release-checklist.md

**Verify:** Explicit artifact-by-artifact scope and authorization; partial ecosystem readiness does not block a complete book or imply app release.

**Depends on:** CR-10.02

### CR-10.04 — Observe re-entry without moral scoring

**Action:** Record comprehension, voluntary return and usability feedback. Keep objections and confusion. Feed concrete findings to a new bounded StoryOps cycle rather than endlessly reopening the accepted text.

**Deliver:** runs/<run>/reader-feedback.md

**Verify:** No streak/report-depth/worldview equivalence; each new change has a concrete observed problem and a scoped hypothesis.

**Depends on:** CR-10.03

## Candidate and exit contract

Use existing StoryOps runs with a unique campaign/run ID after CR-00 isolation is satisfied. Preserve baseline, raw candidate, exact diff, reviewer identity, gate evidence and keep/discard rationale. A mechanical keep is not an accepted chapter. If two cycles stagnate, stop and return to diagnosis with sanitized failure lessons.

Close this phase only when each task has its named evidence and unresolved findings have explicit owners/dependency fences. Record actual execution status in STATE.md and plan.json; never mark tasks complete because this plan exists. Promotion and publication are distinct actions.
