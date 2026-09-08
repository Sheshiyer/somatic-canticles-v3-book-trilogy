# CR-01 — Full scene inventory and canon reconciliation

Status: planned · Scope: implementation plan, not execution receipt

## Outcome

Replace sampled assumptions with a full reading and explicit cosmological decisions.

## Entry and ownership

- Dependencies: CR-00
- Accountable owner: Canon editor + continuity editor. One writer owns a chapter within a wave. Writers are not alone in the codebase: preserve others' edits and coordinate shared files.
- Read [CONTEXT](../CONTEXT.md), [StoryOps adapter](../STORYOPS-ADAPTER.md), [rubric](../RUBRIC.md), relevant critique input and latest accepted predecessor receipts.
- Canon decisions not yet accepted remain proposals. Work that does not depend on them can proceed; fence only dependent mutations.

## Tasks

### CR-01.01 — Read all 27 chapters in full

**Action:** Build a scene-by-scene map with exact anchors, point of view, setting, time, object continuity, choice, cost, unresolved remainder, and voice. Start from the 27-row critique map but mark each observation confirmed, narrowed, or rejected.

**Deliver:** runs/<run>/scene-inventory.json; critique-reconciliation.md

**Verify:** Every chapter has a full-read receipt and all scenes accounted for; no sampled finding becomes a whole-chapter verdict without evidence.

**Depends on:** CR-00

### CR-01.02 — Reconcile the foundational meanings

**Action:** Prepare old/new passages for Lens 13, perfect coherence, View from Nowhere, post-ripening edges, internal reality rendering, Kha-Ba-La, sheaths, and destiny/choice. Treat all-person layered sheaths as a proposal, not a Selemene output or traditional equivalence.

**Deliver:** runs/<run>/canon-decisions.md

**Verify:** Each conflict has a proposed interpretation, affected passages, retained constraints, and author decision or explicit defer; deferred decisions fence dependent edits only.

**Depends on:** CR-01.01

### CR-01.03 — Trace time and objects

**Action:** Trace shard, obsidian seed, orphan routes, consent watermark, Mira/Verath lineage, and the six-week interval; separate similar artifacts rather than assume identity. Identify entry/exit and recurrence requirements before designing consequences.

**Deliver:** runs/<run>/continuity-ledger.json

**Verify:** Every pilot-related object has source-linked appearances; no invented date, identity merger, or unexplained disappearance.

**Depends on:** CR-01.02

### CR-01.04 — Map all characters and relationships

**Action:** Create four character state histories, six pair histories, and a group history of coalition, decision rights, invisible labor, and received care. Record ordinary wants and pleasures as well as ethical dilemmas.

**Deliver:** runs/<run>/character-arcs.json; relationship-arcs.json

**Verify:** Each proposed gap checked against full scene evidence; cross-context recurrence distinguishes insight, changed action, habit, and inferred worldview.

**Depends on:** CR-01.03

## Candidate and exit contract

Use existing StoryOps runs with a unique campaign/run ID after CR-00 isolation is satisfied. Preserve baseline, raw candidate, exact diff, reviewer identity, gate evidence and keep/discard rationale. A mechanical keep is not an accepted chapter. If two cycles stagnate, stop and return to diagnosis with sanitized failure lessons.

Close this phase only when each task has its named evidence and unresolved findings have explicit owners/dependency fences. Record actual execution status in STATE.md and plan.json; never mark tasks complete because this plan exists. Promotion and publication are distinct actions.
