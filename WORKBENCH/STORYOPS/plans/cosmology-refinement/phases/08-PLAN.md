# CR-08 — Companion content identity and faithful compression

Status: planned · Scope: implementation plan, not execution receipt

## Outcome

Make one coherent meaning graph across story, short practice and deeper exploration.

## Entry and ownership

- Dependencies: CR-07
- Accountable owner: Content architect + app content owners. One writer owns a chapter within a wave. Writers are not alone in the codebase: preserve others' edits and coordinate shared files.
- Read [CONTEXT](../CONTEXT.md), [StoryOps adapter](../STORYOPS-ADAPTER.md), [rubric](../RUBRIC.md), relevant critique input and latest accepted predecessor receipts.
- Canon decisions not yet accepted remain proposals. Work that does not depend on them can proceed; fence only dependent mutations.

## Tasks

### CR-08.01 — Reconcile existing companion entries

**Action:** Map 12 developed entries and 15 placeholders against accepted 27-chapter scene identities. Distinguish chapter ID, practice ID and app entry ID; identify recurrence instead of inventing exercises to fill counts.

**Deliver:** runs/<run>/companion-manifest.json

**Verify:** Every developed entry has accepted source hash/scene; missing and retired content explicit.

**Depends on:** CR-07

### CR-08.02 — Design short and expanded forms

**Action:** Start with the accepted Chapter 6 situation. Draft mobile encounter, web exploration and optional lens context. Preserve observation, interpretation, choice, consequence and return at each scale.

**Deliver:** runs/<run>/content-pilot/

**Verify:** Short form stands alone; no required birth profile to understand the scene; symbolic prompt does not become a verdict.

**Depends on:** CR-08.01

### CR-08.03 — Specify introduction and migration behavior

**Action:** Design first guided introduction and permanent practice reuse; separate attempts, reflections, timing and reading progress. Map existing access without treating historical unlock events as verified introductions.

**Deliver:** runs/<run>/practice-access-contract.md

**Verify:** Decline, pause, return and reduced cycle values cannot revoke introduced practice; privacy is not a progress requirement.

**Depends on:** CR-08.02

### CR-08.04 — Freeze content API and source-pack handoff

**Action:** Reuse source-pack conventions where possible. Specify versioning, aliases, retirement, offline revision identity and which owning app/service stores each state.

**Deliver:** runs/<run>/companion-handoff.md

**Verify:** Web/mobile owners have reviewable behavior cases and migration proposal; no UI implementation or production content parity inferred.

**Depends on:** CR-08.03

## Candidate and exit contract

Use existing StoryOps runs with a unique campaign/run ID after CR-00 isolation is satisfied. Preserve baseline, raw candidate, exact diff, reviewer identity, gate evidence and keep/discard rationale. A mechanical keep is not an accepted chapter. If two cycles stagnate, stop and return to diagnosis with sanitized failure lessons.

Close this phase only when each task has its named evidence and unresolved findings have explicit owners/dependency fences. Record actual execution status in STATE.md and plan.json; never mark tasks complete because this plan exists. Promotion and publication are distinct actions.
