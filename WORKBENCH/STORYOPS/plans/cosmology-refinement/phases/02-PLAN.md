# CR-02 — Chapter 6 and 14 relational pilot

Status: planned · Scope: implementation plan, not execution receipt

## Outcome

Prove the new editorial method in two existing scenes before scaling.

## Entry and ownership

- Dependencies: CR-01
- Accountable owner: Prose writer + separate character/continuity critic. One writer owns a chapter within a wave. Writers are not alone in the codebase: preserve others' edits and coordinate shared files.
- Read [CONTEXT](../CONTEXT.md), [StoryOps adapter](../STORYOPS-ADAPTER.md), [rubric](../RUBRIC.md), relevant critique input and latest accepted predecessor receipts.
- Canon decisions not yet accepted remain proposals. Work that does not depend on them can proceed; fence only dependent mutations.

## Tasks

### CR-02.01 — Freeze a bounded Chapter 6 brief

**Action:** Use the shared scanner and shard vote. Preserve humor, plot spine, and object history. Define the single changed variable as who can assign the burden of carrying the shard. Give each person a wanted outcome and allow dissent.

**Deliver:** runs/<run>/book_1/ch06/brief.md

**Verify:** Source span and protected beats fixed; proposed later consequence traced; no new engine exposition required.

**Depends on:** CR-01

### CR-02.02 — Run a bounded candidate comparison

**Action:** Generate one candidate per cycle, maximum three initial experiments and up to nine only for a justified extension; stop after two stagnant cycles. Compare against the exact baseline. Retain raw output, diff, provider receipt, scanner JSON and independent review.

**Deliver:** runs/<run>/book_1/ch06/candidates/; autoresearch-trace.json

**Verify:** An objection changes an action; burden and consent distinct; humor survives; any kept candidate earns more than correct vocabulary.

**Depends on:** CR-02.01

### CR-02.03 — Test transfer in Chapter 14

**Action:** Revise only after Chapter 6 candidate selection. Preserve the differentiated readiness and first live relay; test a costly second handoff and negotiation under time pressure. Remove repetitive explanation only where action carries its meaning.

**Deliver:** runs/<run>/book_2/ch14/

**Verify:** The later scene applies learning in a different situation, retains uncertainty, and does not require identical readiness or unanimous interpretation.

**Depends on:** CR-02.02

### CR-02.04 — Close the pilot with reader evidence

**Action:** Review both complete candidate chapters plus their neighbors; ask a cold reader to name motives, objection, cost, remaining disagreement and what changed. Record conflicting reader responses. Author selects keep/revise/discard at wave close.

**Deliver:** runs/<run>/pilot-wave-close.md

**Verify:** Accepted candidate hashes and scope recorded, or explicit discard. Scaling waits for evidence that the method improves fiction; scanner success alone cannot open Phase 03.

**Depends on:** CR-02.03

## Candidate and exit contract

Use existing StoryOps runs with a unique campaign/run ID after CR-00 isolation is satisfied. Preserve baseline, raw candidate, exact diff, reviewer identity, gate evidence and keep/discard rationale. A mechanical keep is not an accepted chapter. If two cycles stagnate, stop and return to diagnosis with sanitized failure lessons.

Close this phase only when each task has its named evidence and unresolved findings have explicit owners/dependency fences. Record actual execution status in STATE.md and plan.json; never mark tasks complete because this plan exists. Promotion and publication are distinct actions.
