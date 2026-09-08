# CR-07 — Whole-trilogy convergence and writer integration

Status: planned · Scope: implementation plan, not execution receipt

## Outcome

Prove the revised books work together and update reusable guidance from accepted evidence.

## Entry and ownership

- Dependencies: CR-06
- Accountable owner: Series editor + independent literary/epistemic reviewer. One writer owns a chapter within a wave. Writers are not alone in the codebase: preserve others' edits and coordinate shared files.
- Read [CONTEXT](../CONTEXT.md), [StoryOps adapter](../STORYOPS-ADAPTER.md), [rubric](../RUBRIC.md), relevant critique input and latest accepted predecessor receipts.
- Canon decisions not yet accepted remain proposals. Work that does not depend on them can proceed; fence only dependent mutations.

## Tasks

### CR-07.01 — Run the full trilogy continuity pass

**Action:** Read the assembled selected chapters in order. Validate object and timeline ledgers, four arcs, six pairs, group dynamics, retained ordinary life, and non-monotonic transformations.

**Deliver:** runs/<run>/trilogy-continuity.md

**Verify:** All 27 full-read receipts updated; source-to-final changed beats traced; contradictions resolved or deliberately dramatized.

**Depends on:** CR-06

### CR-07.02 — Run compression and cold-reader review

**Action:** Review explanatory repetition, process-language leaks, biological terminology and fiction/tradition/empirical boundaries. Use cold readers across suitable familiarity levels; retain disagreement rather than manufacture consensus.

**Deliver:** runs/<run>/reader-review.md; epistemic-audit.md

**Verify:** Readers can identify motives/costs without engine dossiers; no token or word threshold stands in for literary quality.

**Depends on:** CR-07.01

### CR-07.03 — Update Noesis Writer from proven rules

**Action:** Add only generalized rules supported by accepted candidates, such as relational burden and overcorrection checks. Keep story-specific examples in StoryOps; increment version, preserve before-state, and synchronize canonical/mirror packages.

**Deliver:** runs/<run>/writer-update.patch; mirror-receipt.json

**Verify:** Required files tracked, canonical/mirror match, skill claims do not promote unaccepted plot or changed governance.

**Depends on:** CR-07.02

### CR-07.04 — Close manuscript revision

**Action:** Prepare exact selected chapter diff and all wave evidence. Author review governs promotion; publication remains separate. Rehash accepted chapter source.

**Deliver:** runs/<run>/manuscript-release-candidate.md

**Verify:** Named accepted revision is the sole input for exports and companion mapping; original and all rejects recoverable.

**Depends on:** CR-07.03

## Candidate and exit contract

Use existing StoryOps runs with a unique campaign/run ID after CR-00 isolation is satisfied. Preserve baseline, raw candidate, exact diff, reviewer identity, gate evidence and keep/discard rationale. A mechanical keep is not an accepted chapter. If two cycles stagnate, stop and return to diagnosis with sanitized failure lessons.

Close this phase only when each task has its named evidence and unresolved findings have explicit owners/dependency fences. Record actual execution status in STATE.md and plan.json; never mark tasks complete because this plan exists. Promotion and publication are distinct actions.
