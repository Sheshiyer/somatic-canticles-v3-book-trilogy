# CR-05 — Book 2 revision: negotiated interdependence

Status: planned · Scope: implementation plan, not execution receipt

## Outcome

Revise Chapters 9–15 so shared work tests rather than erases difference.

## Entry and ownership

- Dependencies: CR-04
- Accountable owner: Book 2 writer + independent critic. One writer owns a chapter within a wave. Writers are not alone in the codebase: preserve others' edits and coordinate shared files.
- Read [CONTEXT](../CONTEXT.md), [StoryOps adapter](../STORYOPS-ADAPTER.md), [rubric](../RUBRIC.md), relevant critique input and latest accepted predecessor receipts.
- Canon decisions not yet accepted remain proposals. Work that does not depend on them can proceed; fence only dependent mutations.

## Tasks

### CR-05.01 — Resolve structural continuity in Chapters 9–12

**Action:** Read Elara/forge, station/command and repeated-ending sequences against the scene inventory. Retain only causally distinct material; do not assume unusual material is automatically non-canon. Resolve who pays for the construct and who can refuse.

**Deliver:** runs/<run>/book_2/ch09–ch12/

**Verify:** Every removal justified against dependencies; accepted adaptation preserves necessary protection and exposed vulnerability.

**Depends on:** CR-04

### CR-05.02 — Revise chorus and coordination, Chapters 13–15

**Action:** Integrate accepted Chapter 14 pilot; retain Chapter 15 suspicion of effortless merger. Keep cooperation possible without synchronized emotion, shared interior access, or a compatibility score.

**Deliver:** runs/<run>/book_2/ch13–ch15/

**Verify:** At least one consequential disagreement survives cooperative action; a private thought or refusal does not cost membership.

**Depends on:** CR-05.01

### CR-05.03 — Review relationships and book boundary

**Action:** Trace all six pairs through Books 1–2. Check who carries recurring invisible labor, who repairs, and who receives care. Verify final descent and Chapter 16 interval dependencies.

**Deliver:** runs/<run>/book_2/relationship-review.md

**Verify:** Every claimed relationship change has scenes before and after; elapsed-time assertions remain consistent.

**Depends on:** CR-05.02

### CR-05.04 — Close Book 2 wave

**Action:** Cold-read the seven chapters; reconcile scanner WARNs specifically; attach source-to-candidate diffs and author selections.

**Deliver:** runs/<run>/book_2/wave-close.md

**Verify:** Selected revision and downstream constraints pinned for Book 3; no unreviewed stitched resolution survives on metric score alone.

**Depends on:** CR-05.03

## Candidate and exit contract

Use existing StoryOps runs with a unique campaign/run ID after CR-00 isolation is satisfied. Preserve baseline, raw candidate, exact diff, reviewer identity, gate evidence and keep/discard rationale. A mechanical keep is not an accepted chapter. If two cycles stagnate, stop and return to diagnosis with sanitized failure lessons.

Close this phase only when each task has its named evidence and unresolved findings have explicit owners/dependency fences. Record actual execution status in STATE.md and plan.json; never mark tasks complete because this plan exists. Promotion and publication are distinct actions.
