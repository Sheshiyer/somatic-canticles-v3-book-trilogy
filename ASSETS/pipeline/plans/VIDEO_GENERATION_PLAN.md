# Somatic Canticles — Video Generation Plan

> **IMPORTANT (Post Phase 3 reorganization):**  
> The asset folder has been significantly restructured. Core visuals now live under `covers/`, merch under `merch/`, ads under `marketing/ads/`, etc.  
> Many example paths in this document (especially older sections) still show the old flat structure. When using these lists, mentally map them to the new locations or use the generator script as the source of truth.  
> Remote GitHub URLs point to the historical v3 mirror and are left unchanged.

### Current Structure + Old → New Path Mapping (Post Phase 3)

| Category                  | Old Flat Path Example                              | New Location                                              | Notes |
|---------------------------|----------------------------------------------------|-----------------------------------------------------------|-------|
| Core Book Covers          | `book-1-anamnesis--typo-mask--macos.png`           | `covers/book-1-anamnesis/typo-mask/...`                   | All typo-mask, editorial, modular now here |
| Series Covers             | `series-somatic-canticles--editorial--iphone.png`  | `covers/series/editorial/...`                             | — |
| Merch Mockups             | `book-1-anamnesis--merch-hoodie.png`               | `merch/book-1-anamnesis/book-1-anamnesis--merch-hoodie.png` | Nested per book + series |
| Social Ads                | `book-1-anamnesis--ad-fb-feed.png`                 | `marketing/ads/book-1-anamnesis/...`                      | — |
| Series Ads                | `series-somatic-canticles--ad-ig-story.png`        | `marketing/ads/series/series--ad-ig-story.png`            | Standardized to short `series--` prefix in Phase 4 |
| Product / Campaign Heroes | `book-1-anamnesis--product-hero.png`               | `heroes/book-1-anamnesis--product-hero.png`               | Top level (promotional, not core covers) |
| Bookmarks v2              | `book-1-anamnesis--bookmark-v2.png`                | `bookmarks/book-1-anamnesis--bookmark-v2.png`             | — |
| Quotes                    | `book-1-anamnesis--quote-1000.png`                 | `quotes/book-1-anamnesis/...`                             | — |
| Campaign Assets           | `campaign--main-hero-wide.png`                     | `marketing/events-promos/campaign--main-hero-wide.png`    | — |
| Raw AI Videos             | `video-xxxxxxxx.mp4`                               | `archive/raw-videos/`                                     | Unnamed generations |
| Curated Videos            | `book-1-anamnesis--video.mp4`                      | `videos/`                                                 | Polished clips |

**Recommendation:** Use `pipeline/scripts/generate-manual-animation-batch.sh` as the current source of truth for paths.

**Status:** 25 videos generated via API (typo-mask macOS/iPhone/iPad, covers, product group, boxset, bookmarks v1, merch some, campaign some)

**Goal:** Generate ~40-60 more high-quality image-to-video clips using your custom assets.

**How to use (manual via Grok UI or CLI):**
1. Go to https://grok.x.ai or grok.imagine.ai
2. Start image-to-video / grok-imagine-video
3. Reference or upload the image from the Raw URL below
4. Paste the exact prompt provided

**Priority:** Focus on Tier 1 first (cleanest glow/breathing animations).

---

## TIER 1 — BEST RESULTS (Clean typography + strong focal glow)

### Typo-Mask — Watch (small but excellent for subtle animation)
- **covers/book-1-anamnesis/typo-mask/book-1-anamnesis--typo-mask--watchos--198x242**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-1-anamnesis/typo-mask/book-1-anamnesis--typo-mask--watchos--198x242.png
  - Prompt: "Animate: subtle bioluminescent glow breathing gently, title shimmering softly, cinematic product shot, 5s"

- **covers/book-1-anamnesis/typo-mask/book-1-anamnesis--typo-mask--watchos--396x484**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-1-anamnesis/typo-mask/book-1-anamnesis--typo-mask--watchos--396x484.png
  - Prompt: "Animate: subtle bioluminescent glow breathing gently, title shimmering softly, cinematic product shot, 5s"

- **covers/book-1-anamnesis/typo-mask/book-1-anamnesis--typo-mask--watchos**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-1-anamnesis/typo-mask/book-1-anamnesis--typo-mask--watchos.png
  - Prompt: "Animate: subtle bioluminescent glow breathing gently, title shimmering softly, cinematic product shot, 5s"

- **covers/book-2-myocardial/typo-mask/covers/book-2-myocardial/typo-mask/book-2-myocardial--typo-mask--watchos--198x242**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-2-myocardial/typo-mask/covers/book-2-myocardial/typo-mask/book-2-myocardial--typo-mask--watchos--198x242.png
  - Prompt: "Animate: subtle bioluminescent glow breathing gently, title shimmering softly, cinematic product shot, 5s"

- **covers/book-2-myocardial/typo-mask/covers/book-2-myocardial/typo-mask/book-2-myocardial--typo-mask--watchos--396x484**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-2-myocardial/typo-mask/covers/book-2-myocardial/typo-mask/book-2-myocardial--typo-mask--watchos--396x484.png
  - Prompt: "Animate: subtle bioluminescent glow breathing gently, title shimmering softly, cinematic product shot, 5s"

- **covers/book-2-myocardial/typo-mask/covers/book-2-myocardial/typo-mask/book-2-myocardial--typo-mask--watchos**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-2-myocardial/typo-mask/covers/book-2-myocardial/typo-mask/book-2-myocardial--typo-mask--watchos.png
  - Prompt: "Animate: subtle bioluminescent glow breathing gently, title shimmering softly, cinematic product shot, 5s"

- **covers/book-3-ripening/typo-mask/covers/book-3-ripening/typo-mask/book-3-ripening--typo-mask--watchos--198x242**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-3-ripening/typo-mask/covers/book-3-ripening/typo-mask/book-3-ripening--typo-mask--watchos--198x242.png
  - Prompt: "Animate: subtle bioluminescent glow breathing gently, title shimmering softly, cinematic product shot, 5s"

- **covers/book-3-ripening/typo-mask/covers/book-3-ripening/typo-mask/book-3-ripening--typo-mask--watchos--396x484**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-3-ripening/typo-mask/covers/book-3-ripening/typo-mask/book-3-ripening--typo-mask--watchos--396x484.png
  - Prompt: "Animate: subtle bioluminescent glow breathing gently, title shimmering softly, cinematic product shot, 5s"

- **covers/book-3-ripening/typo-mask/covers/book-3-ripening/typo-mask/book-3-ripening--typo-mask--watchos**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-3-ripening/typo-mask/covers/book-3-ripening/typo-mask/book-3-ripening--typo-mask--watchos.png
  - Prompt: "Animate: subtle bioluminescent glow breathing gently, title shimmering softly, cinematic product shot, 5s"

- **covers/series/typo-mask/series-somatic-canticles--typo-mask--watchos--198x242**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/series/typo-mask/series-somatic-canticles--typo-mask--watchos--198x242.png
  - Prompt: "Animate: subtle bioluminescent glow breathing gently, title shimmering softly, cinematic product shot, 5s"

- **covers/series/typo-mask/series-somatic-canticles--typo-mask--watchos--396x484**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/series/typo-mask/series-somatic-canticles--typo-mask--watchos--396x484.png
  - Prompt: "Animate: subtle bioluminescent glow breathing gently, title shimmering softly, cinematic product shot, 5s"

- **covers/series/typo-mask/series-somatic-canticles--typo-mask--watchos**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/series/typo-mask/series-somatic-canticles--typo-mask--watchos.png
  - Prompt: "Animate: subtle bioluminescent glow breathing gently, title shimmering softly, cinematic product shot, 5s"


### Typo-Mask — iPhone / iPad variants (high res)
- **covers/book-1-anamnesis/typo-mask/book-1-anamnesis--typo-mask--iphone--1179x2556**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-1-anamnesis/typo-mask/book-1-anamnesis--typo-mask--iphone--1179x2556.png
  - Prompt: "Animate: clean glowing typography with soft breathing light, title shimmers, elegant slow cinematic movement"

- **covers/book-1-anamnesis/typo-mask/book-1-anamnesis--typo-mask--iphone--1290x2796**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-1-anamnesis/typo-mask/book-1-anamnesis--typo-mask--iphone--1290x2796.png
  - Prompt: "Animate: clean glowing typography with soft breathing light, title shimmers, elegant slow cinematic movement"

- **covers/book-2-myocardial/typo-mask/covers/book-2-myocardial/typo-mask/book-2-myocardial--typo-mask--iphone--1179x2556**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-2-myocardial/typo-mask/covers/book-2-myocardial/typo-mask/book-2-myocardial--typo-mask--iphone--1179x2556.png
  - Prompt: "Animate: clean glowing typography with soft breathing light, title shimmers, elegant slow cinematic movement"

- **covers/book-2-myocardial/typo-mask/covers/book-2-myocardial/typo-mask/book-2-myocardial--typo-mask--iphone--1290x2796**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-2-myocardial/typo-mask/covers/book-2-myocardial/typo-mask/book-2-myocardial--typo-mask--iphone--1290x2796.png
  - Prompt: "Animate: clean glowing typography with soft breathing light, title shimmers, elegant slow cinematic movement"

- **covers/book-3-ripening/typo-mask/covers/book-3-ripening/typo-mask/book-3-ripening--typo-mask--iphone--1179x2556**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-3-ripening/typo-mask/covers/book-3-ripening/typo-mask/book-3-ripening--typo-mask--iphone--1179x2556.png
  - Prompt: "Animate: clean glowing typography with soft breathing light, title shimmers, elegant slow cinematic movement"

- **covers/book-3-ripening/typo-mask/covers/book-3-ripening/typo-mask/book-3-ripening--typo-mask--iphone--1290x2796**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-3-ripening/typo-mask/covers/book-3-ripening/typo-mask/book-3-ripening--typo-mask--iphone--1290x2796.png
  - Prompt: "Animate: clean glowing typography with soft breathing light, title shimmers, elegant slow cinematic movement"

- **covers/series/typo-mask/series-somatic-canticles--typo-mask--iphone--1179x2556**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/series/typo-mask/series-somatic-canticles--typo-mask--iphone--1179x2556.png
  - Prompt: "Animate: clean glowing typography with soft breathing light, title shimmers, elegant slow cinematic movement"

- **covers/series/typo-mask/series-somatic-canticles--typo-mask--iphone--1290x2796**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/series/typo-mask/series-somatic-canticles--typo-mask--iphone--1290x2796.png
  - Prompt: "Animate: clean glowing typography with soft breathing light, title shimmers, elegant slow cinematic movement"

- **covers/book-1-anamnesis/typo-mask/book-1-anamnesis--typo-mask--ipad--1668x2388**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-1-anamnesis/typo-mask/book-1-anamnesis--typo-mask--ipad--1668x2388.png
  - Prompt: "Animate: clean glowing typography with soft breathing light, title shimmers, elegant slow cinematic movement"

- **covers/book-1-anamnesis/typo-mask/book-1-anamnesis--typo-mask--ipad--2048x2732**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-1-anamnesis/typo-mask/book-1-anamnesis--typo-mask--ipad--2048x2732.png
  - Prompt: "Animate: clean glowing typography with soft breathing light, title shimmers, elegant slow cinematic movement"

- **covers/book-2-myocardial/typo-mask/covers/book-2-myocardial/typo-mask/book-2-myocardial--typo-mask--ipad--1668x2388**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-2-myocardial/typo-mask/covers/book-2-myocardial/typo-mask/book-2-myocardial--typo-mask--ipad--1668x2388.png
  - Prompt: "Animate: clean glowing typography with soft breathing light, title shimmers, elegant slow cinematic movement"

- **covers/book-2-myocardial/typo-mask/covers/book-2-myocardial/typo-mask/book-2-myocardial--typo-mask--ipad--2048x2732**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-2-myocardial/typo-mask/covers/book-2-myocardial/typo-mask/book-2-myocardial--typo-mask--ipad--2048x2732.png
  - Prompt: "Animate: clean glowing typography with soft breathing light, title shimmers, elegant slow cinematic movement"

- **covers/book-3-ripening/typo-mask/covers/book-3-ripening/typo-mask/book-3-ripening--typo-mask--ipad--1668x2388**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-3-ripening/typo-mask/covers/book-3-ripening/typo-mask/book-3-ripening--typo-mask--ipad--1668x2388.png
  - Prompt: "Animate: clean glowing typography with soft breathing light, title shimmers, elegant slow cinematic movement"

- **covers/book-3-ripening/typo-mask/covers/book-3-ripening/typo-mask/book-3-ripening--typo-mask--ipad--2048x2732**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-3-ripening/typo-mask/covers/book-3-ripening/typo-mask/book-3-ripening--typo-mask--ipad--2048x2732.png
  - Prompt: "Animate: clean glowing typography with soft breathing light, title shimmers, elegant slow cinematic movement"

- **covers/series/typo-mask/series-somatic-canticles--typo-mask--ipad--1668x2388**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/series/typo-mask/series-somatic-canticles--typo-mask--ipad--1668x2388.png
  - Prompt: "Animate: clean glowing typography with soft breathing light, title shimmers, elegant slow cinematic movement"

- **covers/series/typo-mask/series-somatic-canticles--typo-mask--ipad--2048x2732**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/series/typo-mask/series-somatic-canticles--typo-mask--ipad--2048x2732.png
  - Prompt: "Animate: clean glowing typography with soft breathing light, title shimmers, elegant slow cinematic movement"


### Product Heroes + Covers (very strong focal points)
- **book-1-anamnesis--product-hero**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/book-1-anamnesis--product-hero.png
  - Prompt: "Animate: the central glowing element pulses with soft bioluminescence, gentle camera drift, cinematic book trailer quality"

- **book-2-myocardial--product-hero**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/book-2-myocardial--product-hero.png
  - Prompt: "Animate: the central glowing element pulses with soft bioluminescence, gentle camera drift, cinematic book trailer quality"

- **book-3-ripening--product-hero**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/book-3-ripening--product-hero.png
  - Prompt: "Animate: the central glowing element pulses with soft bioluminescence, gentle camera drift, cinematic book trailer quality"

- **trilogy--product-hero-wide**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/trilogy--product-hero-wide.png
  - Prompt: "Animate: the central glowing element pulses with soft bioluminescence, gentle camera drift, cinematic book trailer quality"


### Merch (hoodies, tees, totes) — fabric + logo glow
- **book-1-anamnesis--merch-hoodie**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/book-1-anamnesis--merch-hoodie.png
  - Prompt: "Animate: subtle fabric movement, soft logo glow breathing, gentle product showcase, cinematic lighting"

- **book-2-myocardial--merch-hoodie**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/book-2-myocardial--merch-hoodie.png
  - Prompt: "Animate: subtle fabric movement, soft logo glow breathing, gentle product showcase, cinematic lighting"

- **book-3-ripening--merch-hoodie**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/book-3-ripening--merch-hoodie.png
  - Prompt: "Animate: subtle fabric movement, soft logo glow breathing, gentle product showcase, cinematic lighting"

- **series--merch-hoodie**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/series--merch-hoodie.png
  - Prompt: "Animate: subtle fabric movement, soft logo glow breathing, gentle product showcase, cinematic lighting"

- **book-1-anamnesis--merch-tee**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/book-1-anamnesis--merch-tee.png
  - Prompt: "Animate: subtle fabric movement, soft logo glow breathing, gentle product showcase, cinematic lighting"

- **book-2-myocardial--merch-tee**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/book-2-myocardial--merch-tee.png
  - Prompt: "Animate: subtle fabric movement, soft logo glow breathing, gentle product showcase, cinematic lighting"

- **book-3-ripening--merch-tee**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/book-3-ripening--merch-tee.png
  - Prompt: "Animate: subtle fabric movement, soft logo glow breathing, gentle product showcase, cinematic lighting"

- **series--merch-tee**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/series--merch-tee.png
  - Prompt: "Animate: subtle fabric movement, soft logo glow breathing, gentle product showcase, cinematic lighting"

- **book-1-anamnesis--merch-tote**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/book-1-anamnesis--merch-tote.png
  - Prompt: "Animate: subtle fabric movement, soft logo glow breathing, gentle product showcase, cinematic lighting"

- **book-2-myocardial--merch-tote**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/book-2-myocardial--merch-tote.png
  - Prompt: "Animate: subtle fabric movement, soft logo glow breathing, gentle product showcase, cinematic lighting"

- **book-3-ripening--merch-tote**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/book-3-ripening--merch-tote.png
  - Prompt: "Animate: subtle fabric movement, soft logo glow breathing, gentle product showcase, cinematic lighting"


---

## TIER 2 — STILL VERY GOOD (Editorial, Bookmarks, Campaign)

### Editorial (clean book presentation)
- **covers/book-1-anamnesis/editorial/book-1-anamnesis--editorial--iphone--1179x2556**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-1-anamnesis/editorial/book-1-anamnesis--editorial--iphone--1179x2556.png
  - Prompt: "Animate: soft atmospheric glow around the book, gentle light breathing, elegant slow zoom, premium product video"

- **covers/book-1-anamnesis/editorial/book-1-anamnesis--editorial--iphone--1290x2796**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-1-anamnesis/editorial/book-1-anamnesis--editorial--iphone--1290x2796.png
  - Prompt: "Animate: soft atmospheric glow around the book, gentle light breathing, elegant slow zoom, premium product video"

- **covers/book-1-anamnesis/editorial/book-1-anamnesis--editorial--iphone**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-1-anamnesis/editorial/book-1-anamnesis--editorial--iphone.png
  - Prompt: "Animate: soft atmospheric glow around the book, gentle light breathing, elegant slow zoom, premium product video"

- **covers/book-2-myocardial/editorial/book-2-myocardial--editorial--iphone--1179x2556**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-2-myocardial/editorial/book-2-myocardial--editorial--iphone--1179x2556.png
  - Prompt: "Animate: soft atmospheric glow around the book, gentle light breathing, elegant slow zoom, premium product video"

- **covers/book-2-myocardial/editorial/book-2-myocardial--editorial--iphone--1290x2796**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-2-myocardial/editorial/book-2-myocardial--editorial--iphone--1290x2796.png
  - Prompt: "Animate: soft atmospheric glow around the book, gentle light breathing, elegant slow zoom, premium product video"

- **covers/book-2-myocardial/editorial/book-2-myocardial--editorial--iphone**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-2-myocardial/editorial/book-2-myocardial--editorial--iphone.png
  - Prompt: "Animate: soft atmospheric glow around the book, gentle light breathing, elegant slow zoom, premium product video"

- **covers/book-3-ripening/editorial/book-3-ripening--editorial--iphone--1179x2556**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-3-ripening/editorial/book-3-ripening--editorial--iphone--1179x2556.png
  - Prompt: "Animate: soft atmospheric glow around the book, gentle light breathing, elegant slow zoom, premium product video"

- **covers/book-3-ripening/editorial/book-3-ripening--editorial--iphone--1290x2796**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-3-ripening/editorial/book-3-ripening--editorial--iphone--1290x2796.png
  - Prompt: "Animate: soft atmospheric glow around the book, gentle light breathing, elegant slow zoom, premium product video"

- **covers/book-3-ripening/editorial/book-3-ripening--editorial--iphone**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-3-ripening/editorial/book-3-ripening--editorial--iphone.png
  - Prompt: "Animate: soft atmospheric glow around the book, gentle light breathing, elegant slow zoom, premium product video"

- **covers/series/editorial/series-somatic-canticles--editorial--iphone--1179x2556**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/series/editorial/series-somatic-canticles--editorial--iphone--1179x2556.png
  - Prompt: "Animate: soft atmospheric glow around the book, gentle light breathing, elegant slow zoom, premium product video"

- **covers/series/editorial/series-somatic-canticles--editorial--iphone--1290x2796**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/series/editorial/series-somatic-canticles--editorial--iphone--1290x2796.png
  - Prompt: "Animate: soft atmospheric glow around the book, gentle light breathing, elegant slow zoom, premium product video"

- **covers/series/editorial/series-somatic-canticles--editorial--iphone**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/series/editorial/series-somatic-canticles--editorial--iphone.png
  - Prompt: "Animate: soft atmospheric glow around the book, gentle light breathing, elegant slow zoom, premium product video"

- **covers/book-1-anamnesis/editorial/book-1-anamnesis--editorial--ipad--1668x2388**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-1-anamnesis/editorial/book-1-anamnesis--editorial--ipad--1668x2388.png
  - Prompt: "Animate: soft atmospheric glow around the book, gentle light breathing, elegant slow zoom, premium product video"

- **covers/book-1-anamnesis/editorial/book-1-anamnesis--editorial--ipad--2048x2732**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-1-anamnesis/editorial/book-1-anamnesis--editorial--ipad--2048x2732.png
  - Prompt: "Animate: soft atmospheric glow around the book, gentle light breathing, elegant slow zoom, premium product video"

- **covers/book-1-anamnesis/editorial/book-1-anamnesis--editorial--ipad**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-1-anamnesis/editorial/book-1-anamnesis--editorial--ipad.png
  - Prompt: "Animate: soft atmospheric glow around the book, gentle light breathing, elegant slow zoom, premium product video"

- **covers/book-2-myocardial/editorial/book-2-myocardial--editorial--ipad--1668x2388**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-2-myocardial/editorial/book-2-myocardial--editorial--ipad--1668x2388.png
  - Prompt: "Animate: soft atmospheric glow around the book, gentle light breathing, elegant slow zoom, premium product video"

- **covers/book-2-myocardial/editorial/book-2-myocardial--editorial--ipad--2048x2732**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-2-myocardial/editorial/book-2-myocardial--editorial--ipad--2048x2732.png
  - Prompt: "Animate: soft atmospheric glow around the book, gentle light breathing, elegant slow zoom, premium product video"

- **covers/book-2-myocardial/editorial/book-2-myocardial--editorial--ipad**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-2-myocardial/editorial/book-2-myocardial--editorial--ipad.png
  - Prompt: "Animate: soft atmospheric glow around the book, gentle light breathing, elegant slow zoom, premium product video"

- **covers/book-3-ripening/editorial/book-3-ripening--editorial--ipad--1668x2388**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-3-ripening/editorial/book-3-ripening--editorial--ipad--1668x2388.png
  - Prompt: "Animate: soft atmospheric glow around the book, gentle light breathing, elegant slow zoom, premium product video"

- **covers/book-3-ripening/editorial/book-3-ripening--editorial--ipad--2048x2732**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-3-ripening/editorial/book-3-ripening--editorial--ipad--2048x2732.png
  - Prompt: "Animate: soft atmospheric glow around the book, gentle light breathing, elegant slow zoom, premium product video"

- **covers/book-3-ripening/editorial/book-3-ripening--editorial--ipad**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-3-ripening/editorial/book-3-ripening--editorial--ipad.png
  - Prompt: "Animate: soft atmospheric glow around the book, gentle light breathing, elegant slow zoom, premium product video"

- **covers/series/editorial/series-somatic-canticles--editorial--ipad--1668x2388**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/series/editorial/series-somatic-canticles--editorial--ipad--1668x2388.png
  - Prompt: "Animate: soft atmospheric glow around the book, gentle light breathing, elegant slow zoom, premium product video"

- **covers/series/editorial/series-somatic-canticles--editorial--ipad--2048x2732**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/series/editorial/series-somatic-canticles--editorial--ipad--2048x2732.png
  - Prompt: "Animate: soft atmospheric glow around the book, gentle light breathing, elegant slow zoom, premium product video"

- **covers/series/editorial/series-somatic-canticles--editorial--ipad**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/series/editorial/series-somatic-canticles--editorial--ipad.png
  - Prompt: "Animate: soft atmospheric glow around the book, gentle light breathing, elegant slow zoom, premium product video"

- **covers/book-1-anamnesis/editorial/book-1-anamnesis--editorial--watchos--198x242**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-1-anamnesis/editorial/book-1-anamnesis--editorial--watchos--198x242.png
  - Prompt: "Animate: soft atmospheric glow around the book, gentle light breathing, elegant slow zoom, premium product video"

- **covers/book-1-anamnesis/editorial/book-1-anamnesis--editorial--watchos--396x484**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-1-anamnesis/editorial/book-1-anamnesis--editorial--watchos--396x484.png
  - Prompt: "Animate: soft atmospheric glow around the book, gentle light breathing, elegant slow zoom, premium product video"

- **covers/book-1-anamnesis/editorial/book-1-anamnesis--editorial--watchos**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-1-anamnesis/editorial/book-1-anamnesis--editorial--watchos.png
  - Prompt: "Animate: soft atmospheric glow around the book, gentle light breathing, elegant slow zoom, premium product video"

- **covers/book-2-myocardial/editorial/book-2-myocardial--editorial--watchos--198x242**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-2-myocardial/editorial/book-2-myocardial--editorial--watchos--198x242.png
  - Prompt: "Animate: soft atmospheric glow around the book, gentle light breathing, elegant slow zoom, premium product video"

- **covers/book-2-myocardial/editorial/book-2-myocardial--editorial--watchos--396x484**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-2-myocardial/editorial/book-2-myocardial--editorial--watchos--396x484.png
  - Prompt: "Animate: soft atmospheric glow around the book, gentle light breathing, elegant slow zoom, premium product video"

- **covers/book-2-myocardial/editorial/book-2-myocardial--editorial--watchos**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-2-myocardial/editorial/book-2-myocardial--editorial--watchos.png
  - Prompt: "Animate: soft atmospheric glow around the book, gentle light breathing, elegant slow zoom, premium product video"

- **covers/book-3-ripening/editorial/book-3-ripening--editorial--watchos--198x242**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-3-ripening/editorial/book-3-ripening--editorial--watchos--198x242.png
  - Prompt: "Animate: soft atmospheric glow around the book, gentle light breathing, elegant slow zoom, premium product video"

- **covers/book-3-ripening/editorial/book-3-ripening--editorial--watchos--396x484**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-3-ripening/editorial/book-3-ripening--editorial--watchos--396x484.png
  - Prompt: "Animate: soft atmospheric glow around the book, gentle light breathing, elegant slow zoom, premium product video"

- **covers/book-3-ripening/editorial/book-3-ripening--editorial--watchos**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/book-3-ripening/editorial/book-3-ripening--editorial--watchos.png
  - Prompt: "Animate: soft atmospheric glow around the book, gentle light breathing, elegant slow zoom, premium product video"

- **covers/series/editorial/series-somatic-canticles--editorial--watchos--198x242**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/series/editorial/series-somatic-canticles--editorial--watchos--198x242.png
  - Prompt: "Animate: soft atmospheric glow around the book, gentle light breathing, elegant slow zoom, premium product video"

- **covers/series/editorial/series-somatic-canticles--editorial--watchos--396x484**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/series/editorial/series-somatic-canticles--editorial--watchos--396x484.png
  - Prompt: "Animate: soft atmospheric glow around the book, gentle light breathing, elegant slow zoom, premium product video"

- **covers/series/editorial/series-somatic-canticles--editorial--watchos**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/covers/series/editorial/series-somatic-canticles--editorial--watchos.png
  - Prompt: "Animate: soft atmospheric glow around the book, gentle light breathing, elegant slow zoom, premium product video"


### Bookmarks v2
- **book-1-anamnesis--bookmark-v2**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/book-1-anamnesis--bookmark-v2.png
  - Prompt: "Animate: the bookmark glows with soft bioluminescent light, subtle pulsing, clean product shot"

- **book-2-myocardial--bookmark-v2**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/book-2-myocardial--bookmark-v2.png
  - Prompt: "Animate: the bookmark glows with soft bioluminescent light, subtle pulsing, clean product shot"

- **book-3-ripening--bookmark-v2**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/book-3-ripening--bookmark-v2.png
  - Prompt: "Animate: the bookmark glows with soft bioluminescent light, subtle pulsing, clean product shot"


### Campaign Hero + Window Posters (good if not too busy)
- **book-1-anamnesis--campaign-hero**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/book-1-anamnesis--campaign-hero.png
  - Prompt: "Animate: main glowing elements pulse gently, atmospheric cinematic movement, premium feel"

- **book-2-myocardial--campaign-hero**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/book-2-myocardial--campaign-hero.png
  - Prompt: "Animate: main glowing elements pulse gently, atmospheric cinematic movement, premium feel"

- **book-3-ripening--campaign-hero**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/book-3-ripening--campaign-hero.png
  - Prompt: "Animate: main glowing elements pulse gently, atmospheric cinematic movement, premium feel"

- **book-1-anamnesis--window-poster**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/book-1-anamnesis--window-poster.png
  - Prompt: "Animate: main glowing elements pulse gently, atmospheric cinematic movement, premium feel"

- **book-2-myocardial--window-poster**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/book-2-myocardial--window-poster.png
  - Prompt: "Animate: main glowing elements pulse gently, atmospheric cinematic movement, premium feel"

- **book-3-ripening--window-poster**
  - URL: https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS/book-3-ripening--window-poster.png
  - Prompt: "Animate: main glowing elements pulse gently, atmospheric cinematic movement, premium feel"


---

## How to Run These Quickly

**Recommended workflow:**
1. Open https://grok.x.ai (or grok.imagine.ai)
2. Use the image-to-video / video generation feature
3. For each entry:
   - Paste the Raw URL or upload the local file
   - Paste the exact prompt
   - Generate (usually 5-8s clips)
4. Download and rename to match the pattern: `bookX-xxx--video.mp4`

**Tip:** Start with all the **typo-mask--watchos** and **typo-mask--iphone** ones — they are small, clean, and produce beautiful subtle animations.

**Next batch suggestion after these:** Venues (soma-cathedral, anamnesis-lab, etc.) for atmospheric world-building clips.

---

*Generated: $(date)*
*Total recommended in this plan: ~45-55 clips*
