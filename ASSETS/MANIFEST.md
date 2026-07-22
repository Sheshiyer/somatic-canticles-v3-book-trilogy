# Somatic Canticles — Asset Manifest

**Last reorganized:** 2026-06-01 (Phase 1 + Phase 2)  
**Root files:** 148 (mostly the core book visual system)  
**Total categorized files:** See counts below

## Structure Overview

```
ASSETS/
├── archive/
│   ├── raw-videos/          # 30 — raw AI video generations (UUID names). Review before use.
│   └── iterations/          #  6 — v1 design versions (bookmark-v1, cover-v1)
├── pipeline/
│   ├── scripts/             # generator + tracker
│   └── plans/               # VIDEO_GENERATION_PLAN.md + ANIMATION_BATCH_REMAINING.md
├── merch/                   # 11 files — product mockups
│   ├── book-1-anamnesis/
│   ├── book-2-myocardial/
│   ├── book-3-ripening/
│   └── series/
├── marketing/ads/           # 12 files — social ads (fb/ig/twitter formats)
│   ├── book-1-anamnesis/
│   ├── book-2-myocardial/
│   ├── book-3-ripening/
│   └── series/
├── quotes/                  # 12 files — quote cards (4 per book)
├── bookmarks/               #  3 files — v2 bookmarks
├── heroes/                  #  9 files — product-hero, campaign-hero, window-poster
├── videos/                  #  9 files — curated image-to-video clips (merch videos just standardized)
├── press-kit/               #  8 files — brand visuals
├── world/venues/            #  9 files — location art + atmospheric clips
├── tarot/                   # 12 files — symbolic major arcana cards
├── trilogy/                 #  7 files — boxset + product group photography
└── [core at root]           # ~120–130 files — typo-mask, editorial, modular (all device variants)
```

## Core Files Left at Root (by design)

These are the primary "book look" assets and were intentionally kept at the top level for:
- Frequent daily use
- Minimal breakage in the long animation generation plans

**Included:**
- All `book-*-*--typo-mask--*.png`
- All `book-*-*--editorial--*.png`
- All `book-*-*--modular--*.png`
- A few supporting heroes/posters that were not part of the Phase 2 sweep

If you want these moved into `covers/book-1-anamnesis/typo-mask/` etc. (Phase 3), say the word — it is a bigger reference update task.

## Videos

- `videos/` — The 9 polished clips ready for use (including the 5 merch ones, names now standardized to match PNGs).
- `archive/raw-videos/` — 30 raw/unnamed generations. Safe to delete after review.

## Naming

- `book-N-<slug>--<purpose>--<variant>.png`
- Nested folders for merch/ads/quotes use the same full descriptive names inside the per-book directories.

## How to Extend

See `pipeline/plans/VIDEO_GENERATION_PLAN.md` and run the generator from `pipeline/scripts/`.

---
*Generated as part of the Somatic Canticles asset curation.*
