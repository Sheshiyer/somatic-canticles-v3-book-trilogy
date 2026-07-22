# Phase 4 Proposal — Somatic Canticles Asset Library

**Date:** 2026-06-01  
**Status:** Proposed after completion of Phases 1–3

## Current State Summary (Post Phase 3)

- Root is extremely clean (only documentation files).
- Core visual system lives in `covers/` (excellent).
- Merch, ads, quotes, bookmarks, heroes have dedicated homes.
- Videos and raw generations are separated.
- Generator script is significantly improved.
- Living plan documents have a new status header but still contain many outdated paths in their body content.

## Goals for Phase 4

1. Bring the **living documents** (generator + two plan MDs) into much better alignment with reality.
2. Resolve the remaining small inconsistencies and ambiguous placements.
3. Improve long-term maintainability and future-proofing.
4. Reduce friction for future asset generation work.

## Prioritized Recommendations

### Tier 1 — High Impact / Low Effort (Do First)

| Item | Action | Effort | Benefit |
|------|--------|--------|---------|
| **Generator script completeness** | Finish updating all remaining flat references (heroes, bookmarks, campaign main hero, any missed series variants) | Low | High |
| **Add "Structure Status" section** to both plan MDs | Create a clear mapping table of old path → new path for the most common assets | Low | High |
| **Heroes placement decision** | Officially decide and document whether `heroes/` stays at top level or moves under `covers/` or a new `promos/` folder | Low | Medium |
| **Series naming standardization** | Choose one convention (`series--` vs `series-somatic-canticles--`) and apply it consistently | Medium | Medium |
| **Marketing/ consistency pass** | Apply the same nested pattern used for `ads/` to `announcements/`, `email/`, and `events-promos/` | Medium | Medium |

### Tier 2 — Medium Impact

- Create a small `ASSETS/CHANGES.md` or "Reorganization Log" (decision record).
- Add a short `press-kit/README.md`.
- Decide on merch videos location (keep centralized or move next to PNGs).
- Improve the two manifests (add a regeneration note or simple script).

### Tier 3 — Future Proofing / Nice to Have

- Add a `sources/` or `working/` folder for raw files before they are finalized.
- Add a `finals/` or `exports/` folder for print-ready / web-optimized deliverables.
- Create a small script to help regenerate `manifest.json` + basic stats.
- Document naming conventions more formally.

## Specific Proposed Changes

### 1. Heroes Placement (Decision Needed)

**Current situation:** `heroes/` at top level with 9 files.

**Options:**

- **A (Recommended)** — Keep `heroes/` at top level.  
  Rationale: These are more marketing/product photography than the core "book cover system". Keeps `covers/` focused.

- **B** — Move into `covers/<book>/heroes/` (and `covers/series/heroes/`).  
  Rationale: Maximum consistency with the deep structure philosophy.

- **C** — Create `promos/` or `marketing/heroes/`.

**Recommendation:** Go with **Option A** and document it clearly.

### 2. Series Naming

Propose standardizing on the shorter `series--` prefix for new work, while accepting the existing `series-somatic-canticles--` files (or do a one-time rename pass).

### 3. Living Documents Strategy

Instead of doing hundreds of manual search-replaces across the plan files, the recommended approach is:

- Add a prominent "Current Structure Mapping" section near the top of both MD files.
- Keep the detailed lists as historical reference but clearly mark them.
- Treat the `generate-manual-animation-batch.sh` script as the single source of truth going forward.

## Estimated Effort

- Tier 1 items: 2–4 hours of focused work.
- Tier 2 items: 3–6 hours.
- Full cleanup: 1–2 days of careful work.

## Next Steps (if approved)

1. Confirm heroes placement decision.
2. Execute the remaining generator script updates.
3. Add the Structure Status sections to the two plan files.
4. Perform series naming + marketing consistency pass (if chosen).
5. Create `ASSETS/CHANGES.md`.

---

*Prepared after full execution of Phases 1–3.*

---

## Decisions Made During Phase 4 Execution (2026-06-01)

### Heroes Placement
**Decision:** Keep `heroes/` at the top level (not under `covers/`).

**Rationale:**
- Heroes (product-hero, campaign-hero, window-poster) are more marketing/product photography than the core "book cover visual system".
- `covers/` should remain focused on the artistic book presentation (typo-mask, editorial, modular).
- This keeps the mental model clean: `covers/` = the books themselves, `heroes/` = promotional shots.

**Action taken:** Documented. No file moves required.

### Series Naming
**Decision:** Prefer the shorter `series--` prefix for new work and future assets.

**Current state:**
- Merch uses `series--` (good)
- Most other series assets use the longer `series-somatic-canticles--`

**Action:** No mass rename performed in this pass (too many files in `covers/`). Added as a recommended cleanup item if desired.

### Marketing Subfolders
**Decision:** Accept current structure for now.

**Rationale:** `ads/` is well nested. The other folders (announcements, email, events-promos) contain very few files. Over-nesting small sets adds more friction than value.

**Future improvement:** If these categories grow significantly, apply the same `book-N-` + `series/` nesting pattern used for ads.

### Documentation Improvements Executed
- Added clear "Post Phase 3" headers to both living plan documents.
- Created `ASSETS/CHANGES.md` (reorganization log).
- Created `ASSETS/press-kit/README.md`.
- Significantly improved the generator script (heroes, bookmarks, campaign assets, etc.).
- Created this proposal document.

