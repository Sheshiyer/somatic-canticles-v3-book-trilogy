# CR-00 — Source and StoryOps readiness

Status: ready · Scope: implementation plan, not execution receipt

## Outcome

Make the existing workflow safe and truthful for this revision campaign.

## Entry and ownership

- Dependencies: Planning package verified; fresh source inventory at execution.
- Accountable owner: StoryOps maintainer + editorial lead. One writer owns a chapter within a wave. Writers are not alone in the codebase: preserve others' edits and coordinate shared files.
- Read [CONTEXT](../CONTEXT.md), [StoryOps adapter](../STORYOPS-ADAPTER.md), [rubric](../RUBRIC.md), relevant critique input and latest accepted predecessor receipts.
- Canon decisions not yet accepted remain proposals. Work that does not depend on them can proceed; fence only dependent mutations.

## Tasks

### CR-00.01 — Freeze source authority

**Action:** Record current main, all chapter hashes, critique hashes, frozen chart input revision, writer version, current exported-book differences, and dirty state. Recheck main at execution time; identify changes since d410908 without absorbing them automatically.

**Deliver:** evidence/source-baseline.json; evidence/export-parity.json

**Verify:** 27 chapter identities resolved; export differences enumerated; reference versus canon explicitly labeled.

**Depends on:** phase entry

### CR-00.02 — Reconcile the gating contract

**Action:** Produce a narrow proposed contract change removing unconditional non_additive_or_compressing_change rejection and the requirement that candidates grow. Preserve scene-spine and source-lineage protection. Explicitly permit justified compression and selective engine terms when consistent with current accepted prose.

**Deliver:** runs/<run>/contract-change.patch; contract-rationale.md

**Verify:** Contract accepts a justified cut and rejects a cut that removes a consequential choice. Historical rules remain documented as superseded, not erased.

**Depends on:** CR-00.01

### CR-00.03 — Verify runner semantics and run isolation

**Action:** Test actual help and mutation behavior. Either add isolated run IDs/output roots to the existing runner, or execute it only in a disposable git worktree with copied input; do not introduce another controller. Correct unsupported --dry-run documentation. Keep scanner candidate paths inside book_1/book_2/book_3 because register inference is path-sensitive.

**Deliver:** runs/<run>/tooling-receipt.json

**Verify:** Two runs of the same chapter retain distinct artifacts; no canonical input changes; actual cycle count recorded; explicit apply behavior tested on temporary copies.

**Depends on:** CR-00.02

### CR-00.04 — Freeze the campaign rubric

**Action:** Combine the existing seven gates with the relational and compression tests in RUBRIC.md. Distinguish deterministic proxies from independent literary judgment. Review frozen baseline WARNs without blessing them globally.

**Deliver:** runs/<run>/rubric-baseline.md

**Verify:** Every gate has evidence and a reviewer; no word-count-only acceptance or generator self-grading. Contract and reviewer setup ready before any candidate wave.

**Depends on:** CR-00.03

## Candidate and exit contract

Use existing StoryOps runs with a unique campaign/run ID after CR-00 isolation is satisfied. Preserve baseline, raw candidate, exact diff, reviewer identity, gate evidence and keep/discard rationale. A mechanical keep is not an accepted chapter. If two cycles stagnate, stop and return to diagnosis with sanitized failure lessons.

Close this phase only when each task has its named evidence and unresolved findings have explicit owners/dependency fences. Record actual execution status in STATE.md and plan.json; never mark tasks complete because this plan exists. Promotion and publication are distinct actions.
