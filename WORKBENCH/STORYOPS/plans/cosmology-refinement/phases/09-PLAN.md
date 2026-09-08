# CR-09 — Selemene and companion implementation handoffs

Status: planned · Scope: implementation plan, not execution receipt

## Outcome

Implement the approved small cross-surface slice in the owning repositories.

## Entry and ownership

- Dependencies: CR-08
- Accountable owner: Selemene owner + web/mobile owners. One writer owns a chapter within a wave. Writers are not alone in the codebase: preserve others' edits and coordinate shared files.
- Read [CONTEXT](../CONTEXT.md), [StoryOps adapter](../STORYOPS-ADAPTER.md), [rubric](../RUBRIC.md), relevant critique input and latest accepted predecessor receipts.
- Canon decisions not yet accepted remain proposals. Work that does not depend on them can proceed; fence only dependent mutations.

## Tasks

### CR-09.01 — Repair only required engine paths

**Action:** Freshly reproduce facts-in-prompts, all-subject audit/model provenance and needed retrieval failures before changes. Preserve chart-line, labels and local-time exclusions until fixed/verified. No new family-penta reuse for the team.

**Deliver:** Owning Selemene repo: bounded PRs + behavior receipts

**Verify:** A deliberately corrupted second-subject fact is detected; actual model recorded; empty retrieval is explicit; no unsupported field enters reports.

**Depends on:** CR-08

### CR-09.02 — Implement shared practice-access behavior

**Action:** Use the approved introduction contract and migration in the actual persistence layer. Separate reader state from reusable source content; avoid a second policy in each UI.

**Deliver:** Owning app/backend repos: implementation + migration evidence

**Verify:** Behavior-level production-like database tests, user isolation and version migration pass; in-memory behavior not treated as production parity.

**Depends on:** CR-09.01

### CR-09.03 — Implement web/mobile pilot end to end

**Action:** Introduce the accepted situation/practice and repertoire return flow. Test reread, reuse, decline, reload, offline return, content revision and changing cycle values. Respect current mobile backend migration.

**Deliver:** Owning web/mobile repos: UI/device evidence + source receipts

**Verify:** Both actual interfaces satisfy the same contract; no implicit native parity from shared JSON; optional reflections remain optional.

**Depends on:** CR-09.02

### CR-09.04 — Review the integrated slice

**Action:** Verify from accepted story source through content manifest, engine facts where used, persistence and both surfaces. Capture limits and deployment state separately.

**Deliver:** runs/<run>/ecosystem-pilot-receipt.md

**Verify:** No runtime claim exceeds tested behavior; deploy only under specific release authorization. Extend beyond pilot only after review.

**Depends on:** CR-09.03

## Candidate and exit contract

Use existing StoryOps runs with a unique campaign/run ID after CR-00 isolation is satisfied. Preserve baseline, raw candidate, exact diff, reviewer identity, gate evidence and keep/discard rationale. A mechanical keep is not an accepted chapter. If two cycles stagnate, stop and return to diagnosis with sanitized failure lessons.

Close this phase only when each task has its named evidence and unresolved findings have explicit owners/dependency fences. Record actual execution status in STATE.md and plan.json; never mark tasks complete because this plan exists. Promotion and publication are distinct actions.
