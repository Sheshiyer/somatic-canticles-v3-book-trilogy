# ASSETS Reorganization Log

This document records major structural changes to the Somatic Canticles asset library.

---

## 2026-06-01 — Phase 3 Complete

**Goal:** Move the core book visual system out of the root into a proper nested structure.

**Changes:**
- Created `covers/` with full nested structure:
  - `book-1-anamnesis/{typo-mask, editorial, modular}/`
  - `book-2-myocardial/{typo-mask, editorial, modular}/`
  - `book-3-ripening/{typo-mask, editorial, modular}/`
  - `series/{typo-mask, editorial, modular}/`
- Moved 144 files (all typo-mask, editorial, and modular variants including all device resolutions) into `covers/`.
- Root reduced from ~148 files to only 3 documentation files.
- Updated generator script for core styles.
- Added status headers to living plan documents.

**Decisions:**
- Core "book look" assets (typo-mask, editorial, modular) now live under `covers/`.
- Heroes, bookmarks, quotes, merch, and ads kept in their own top-level category folders (not under covers).

---

## 2026-06-01 — Phase 2

**Goal:** Extract merch, ads, and supporting assets from root.

**Changes:**
- Created nested structure for `merch/` and `marketing/ads/`.
- Moved quotes, bookmarks (v2), product/campaign/window heroes into dedicated folders.
- Standardized naming for merch videos in `videos/`.
- Created initial `MANIFEST.md` and `manifest.json`.

---

## 2026-06-01 — Phase 1 (Initial Curation)

**Goal:** Basic cleanup and categorization of the original flat 293-file folder.

**Changes:**
- Quarantined 30+ raw UUID videos into `archive/raw-videos/`.
- Moved v1 design iterations to `archive/iterations/`.
- Extracted press-kit, world/venues, tarot, trilogy, and pipeline tools.
- Standardized `book1-` → `book-1-` naming across the library.
- Created `videos/` for curated clips.

---

## Ongoing Notes

- The generator script (`pipeline/scripts/generate-manual-animation-batch.sh`) is now the recommended source of truth for current asset locations.
- Many older references in `VIDEO_GENERATION_PLAN.md` and `ANIMATION_BATCH_REMAINING.md` still reflect previous structures. Use with caution or refer to the generator.

## 2026-06-01 — Phase 4 Work (High + Medium Items)

**Series Naming Standardization (Light pass)**
- Decision: Prefer short `series--` prefix for new and future series assets (cleaner and consistent with merch).
- Executed: Renamed the three series ads in `marketing/ads/series/`:
  - `series-somatic-canticles--ad-fb-feed.png` → `series--ad-fb-feed.png`
  - (same for ig-story and twitter)
- The large number of files inside `covers/series/` were left unchanged to avoid heavy reference churn.
- Updated mapping table in VIDEO_GENERATION_PLAN.md.

**Documentation & History**
- Added comprehensive "Current Structure + Old → New Path Mapping" tables to both `VIDEO_GENERATION_PLAN.md` and `ANIMATION_BATCH_REMAINING.md`.
- Created `ASSETS/CHANGES.md` (this file) as the official reorganization log.
- Added `ASSETS/press-kit/README.md`.
- Significantly cleaned up remaining flat references in the generator script (heroes, bookmarks, campaign assets, etc.).
- Heroes folder officially decided to remain at top level (not under covers/).

**Marketing Subfolders**
- `ads/` remains the best-nested example.
- Other folders (announcements, email, events-promos) left mostly as-is for now (small file counts). Future growth should follow the same book-nested pattern used for ads.

