# Somatic Canticles — Assets

Curated visual library for the trilogy (book covers, marketing, world-building, and production assets).

## Quick Layout (Current Structure)

**Root level (only 3 files)** — Purely documentation:
- `README.md`
- `MANIFEST.md`
- `manifest.json`

All visual assets have been moved into proper subfolders (Phase 3 completed the core covers system).

**Organized categories (moved in Phases 1–2):**

- **merch/** (11 files, nested per book + series)
- **marketing/ads/** (12 files, nested per book + series)
- **quotes/** (12 files, nested per book)
- **bookmarks/** (3 files — v2)
- **heroes/** (9 files — product-hero, campaign-hero, window-poster)
- **videos/** (9 curated clips — merch video names standardized in latest pass)
- **archive/**
  - `raw-videos/` (30 unnamed UUID generations)
  - `iterations/` (6 old v1 designs)
- **pipeline/** — scripts + living plans
- **press-kit/**, **world/venues/**, **tarot/**, **trilogy/** (already extracted in Phase 1)

See `MANIFEST.md` and `manifest.json` for the complete machine- and human-readable inventory.

## Naming Convention (current)

- `book-N-<title>--<purpose>--<variant>.png`
- Double dash (`--`) separates logical segments.
- `book-1-anamnesis`, `book-2-myocardial`, `book-3-ripening`, `series-somatic-canticles`
- v2 is the current design; v1 files live in `archive/iterations/`.

## Regenerating / Extending

See `pipeline/plans/VIDEO_GENERATION_PLAN.md` for the current prioritized list of images worth animating, with exact prompts and source URLs.

Run the generator locally from the `pipeline/scripts/` directory when you need a fresh batch list:

```bash
cd pipeline/scripts
./generate-manual-animation-batch.sh --count 20 --batch-size 5
# or filter: --typo, --merch, --hero, etc.
```

Mark completed work with the tracker (it reads the plans):

```bash
./animate-tracker.sh status
./animate-tracker.sh done book-1-anamnesis--typo-mask--macos.png
```

## Notes

- This is a working production library, not a final static export.
- Many assets were generated via Grok Imagine (image + image-to-video).
- External references in the plan docs may still point at the v3 GitHub mirror (historical).

*Maintained as part of the Somatic Canticles living manuscript.*
