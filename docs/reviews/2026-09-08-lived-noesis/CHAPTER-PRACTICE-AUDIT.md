# Chapter practices and unlock rules

2026-09-08. Mapping and source audit requested by the principal. Application code and manuscript prose remain unchanged.

## Conclusion

The intended sequence is implementable from existing material, but neither app currently establishes the agreed practice-access contract. The web content source contains 12 developed practice/reflection entries and 15 placeholder/easter-egg entries. Mobile carries 27 manuscript chapters. Use manuscript source identity to connect these surfaces; equal numeric IDs do not establish equal content.

The existing developed introductions, in manuscript order, are:

1. Chapter 1 — CSF Flow Awareness (web ID 1)
2. Chapter 2 — Signal Recognition (2)
3. Chapter 3 — Boundary Awareness (3)
4. Chapter 5 — Hormonal Awareness (4)
5. Chapter 6 — Crossroads Meditation (5)
6. Chapter 8 — Compass Calibration (6)
7. Chapter 9 — Personal Sigil Creation (7)
8. Chapter 10 — Consciousness Debugging (8)
9. Chapter 13 — Heart Field Resonance (9)
10. Chapter 15 — Witness Integration (10)
11. Chapter 18 — Four-Element Synthesis (11)
12. Chapter 27 — Architecture of New Reality (12)

These are existing content names, not newly approved exercises or efficacy claims. Each has seven steps and four reflection prompts in the inspected file. The content still requires editorial review against current v3 and the internal-rendering, compassion, responsibility, and contextual-use decisions.

The other 15 manuscript chapters have no developed practice mapped by this source: 4, 7, 11, 12, 14, 16, 17, 19–26. This does not mean each needs a new practice. They may revisit, contrast, or apply already introduced practices; decide from scenes and learning needs. See the [complete 27-row map](evidence/chapter-practice-table.md).

## Current access behavior

| Surface | Inspected behavior | Difference from the agreed rule |
|---|---|---|
| Mobile pure evaluator | Current biorhythm thresholds; chapter 1 and admins bypass; absent/unparseable conditions permit access | It has no practice-introduction state and can change access as cycle values change |
| Mobile store | Re-evaluates thresholds plus book boundaries: every chapter of prior book needs at least 95% progress | Reading completion and current timing govern chapter access, not introduction of an individual practice |
| Mobile unlock events | Saves IDs already celebrated; skips duplicate events | History is used for celebration deduplication, not as an access override |
| Mobile reader | Renders reader/audio according to current `unlockStates` | A previously available chapter may become unavailable under the inspected flow; a separate freely reusable practice surface is not established |
| Mobile progress service | Re-evaluates pure threshold helper without store's book-boundary logic | Access reasoning is split between service and store; eventual practice access should have a consistent policy |
| Web reader client | Calls `/internal-api/chapters/...` when mock mode is off | This is the relevant route chain; the older `src/server` controller is not proof of this client's behavior |
| Web internal summary/detail | First two chapter orders default open; saved unlock, partial progress, or completion retains access; detail returns database content | Some persistence exists at chapter level, but not an explicit practice-introduction record |
| Web internal unlock check | Returns existing total, empty `newly_unlocked`, and `biorhythm_checked: true`; no biorhythm calculation or new unlock write in handler | It does not implement guided progression; the response flag is not evidence of a calculation |
| Web internal progress POST | Upserts progress and supplies `unlocked_at` when absent; no chapter-introduction/prerequisite check in this handler | A progress mutation is not a trustworthy substitute for the guided-introduction event; database policy effects require separate verification |

The `/api/chapters` helper/detail/check implementations also compare identically to their `/internal-api` counterparts at this inspection. The client explicitly selects the internal path for chapter operations.

## Correction to earlier source interpretation

The earlier companion pass identified static content and Practice/Reflection UI correctly, but traced the static fallback through `src/server/api/chapters/index.ts`. The current reader's internal Next route returns `chapter.content` from Supabase directly; it does not call that static fallback. Therefore the static practice map is available editorial source, not proof of the deployed database's content. No production content or migration was read or modified.

The older controller also contains `optionalValue !== null` conditions that accept `undefined`, including missing progress/prerequisite cases. This is a separate legacy-source defect, not a verified vulnerability in the current internal route or a reason to modify unrelated code during this mapping pass.

## Proposed implementation sequence

1. Reconcile the 12 developed entries and 15 unmapped chapters against current v3 scenes. Preserve source chapter IDs/revision and assign practice identity separately from app entry number. Do not replace database rows by matching position.
2. Specify the first-guided-introduction event. Persist access for the reader and practice independently of chapter progress, attempt history, reflections, and timing suggestions. The user has approved free reuse after introduction, not a particular storage schema.
3. Add an introduced-practice library and contextual selection to both companions. Later chapter introductions expand it. Changes to biorhythm recommendations must not revoke introduced practice access.
4. Wire chapter sequencing separately from reusable practice access, respecting mobile's documented backend migration and web's actual internal route chain. Preserve current user progress through an explicit migration rule; do not pretend legacy unlock timestamps prove an introduction happened.
5. Verify first introduction, later reuse under lower cycle values, reload/offline return, user isolation, later introductions, and no unauthorized introduction through progress writes. Verify database behavior and both UIs before claiming integration.

These are proposed implementation steps, not executed changes. Existing valid content can support a pilot after source reconciliation; new exercises should be driven by missing learning functions rather than a quota of one per chapter.

## Verification and source receipt

`bun docs/reviews/2026-09-08-lived-noesis/evidence/map-practices.ts` imported the actual content/evaluator and executed the exact pure web summary function isolated from framework imports. It extracted 27 entries, 12 with steps/reflections, and 15 placeholders. Mobile chapter 2 evaluated open with cycle values +1, then closed with −1. Web chapter 3 was locked without progress and accessible with persisted unlock or partial progress; order 2 defaulted open.

These are local function probes, not device, network, auth, persistence, or production tests. Source hashes and structured rows are in [practice-map.json](evidence/practice-map.json). Re-run the probe after source changes; it asserts the observed behavior and is an audit tool, not a test demanding that future implementations preserve current defects.

Mobile source was clean on `main`, HEAD `61668b282cd05d953217345225d273fff5ba6800`. Web supplied directory has no Git metadata. Current v3 reference remains snapshot `ba74a874fdc43c00b3661d026cb865584b6daaa7`; no remote refresh is claimed by this audit.

Key source paths relative to their app roots:

- Web `src/lib/lore/chapter-content.ts`, `src/lib/chapters/api.ts`, `app/internal-api/chapters/{_helpers.ts,[id]/route.ts,check-unlock/route.ts,progress/route.ts}`.
- Mobile `expo/lib/{unlock-engine.ts,unlock-events.ts}`, `expo/stores/chapters.ts`, `expo/services/chapters.ts`, `expo/app/(tabs)/chapters/[id].tsx`, `expo/assets/serpentine/data/chapters-v1.json`.
