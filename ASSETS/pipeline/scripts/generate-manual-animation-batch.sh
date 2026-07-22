#!/bin/bash
# generate-manual-animation-batch.sh
#
# Generates a ready-to-use manual animation batch for grok.imagine.ai
# Run this locally when you need a fresh list without asking an AI again.
#
# Usage:
#   ./generate-manual-animation-batch.sh                    # full remaining list (batches of 5)
#   ./generate-manual-animation-batch.sh --typo             # only typo-mask
#   ./generate-manual-animation-batch.sh --merch            # only merch
#   ./generate-manual-animation-batch.sh --count 12         # limit output
#   ./generate-manual-animation-batch.sh --batch-size 4     # custom batch size (4-5 recommended)

set -e

ASSETS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DONE_FILE="${HOME}/.somatic-animate-done"
REPO_BASE="https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy/main/ASSETS"

# Files the user has already manually processed (edit this list as you complete them)
ALREADY_DONE=(
    # Original reference (batches 1-3)
    "covers/book-1-anamnesis/typo-mask/book-1-anamnesis--typo-mask--watchos.png"
    "covers/book-2-myocardial/typo-mask/book-2-myocardial--typo-mask--watchos.png"
    "covers/book-3-ripening/typo-mask/book-3-ripening--typo-mask--watchos.png"
    "covers/book-1-anamnesis/editorial/book-1-anamnesis--editorial--iphone.png"
    "covers/book-2-myocardial/editorial/book-2-myocardial--editorial--iphone.png"
    "covers/book-3-ripening/editorial/book-3-ripening--editorial--iphone.png"
    "bookmarks/book-1-anamnesis--bookmark-v2.png"
    "bookmarks/book-2-myocardial--bookmark-v2.png"
    "bookmarks/book-3-ripening--bookmark-v2.png"

    # Batches 4-8 (typo-mask, editorial, early merch)
    "covers/book-1-anamnesis/typo-mask/book-1-anamnesis--typo-mask--iphone.png"
    "covers/book-2-myocardial/typo-mask/book-2-myocardial--typo-mask--iphone.png"
    "covers/book-3-ripening/typo-mask/book-3-ripening--typo-mask--iphone.png"
    "covers/book-1-anamnesis/typo-mask/book-1-anamnesis--typo-mask--ipad.png"
    "covers/book-2-myocardial/typo-mask/book-2-myocardial--typo-mask--ipad.png"
    "covers/book-3-ripening/typo-mask/book-3-ripening--typo-mask--ipad.png"
    "covers/book-1-anamnesis/typo-mask/book-1-anamnesis--typo-mask--macos.png"
    "covers/book-2-myocardial/typo-mask/book-2-myocardial--typo-mask--macos.png"
    "covers/book-3-ripening/typo-mask/book-3-ripening--typo-mask--macos.png"
    "covers/book-1-anamnesis/editorial/book-1-anamnesis--editorial--watchos.png"
    "covers/book-2-myocardial/editorial/book-2-myocardial--editorial--watchos.png"
    "covers/book-3-ripening/editorial/book-3-ripening--editorial--watchos.png"
    "covers/book-1-anamnesis/editorial/book-1-anamnesis--editorial--ipad.png"
    "covers/book-2-myocardial/editorial/book-2-myocardial--editorial--ipad.png"
    "covers/book-3-ripening/editorial/book-3-ripening--editorial--ipad.png"
    "covers/book-1-anamnesis/editorial/book-1-anamnesis--editorial--macos.png"
    "covers/book-2-myocardial/editorial/book-2-myocardial--editorial--macos.png"
    "covers/book-3-ripening/editorial/book-3-ripening--editorial--macos.png"
    "merch/book-1-anamnesis/book-1-anamnesis--merch-hoodie.png"
    "merch/book-2-myocardial/book-2-myocardial--merch-hoodie.png"
    "merch/book-3-ripening/book-3-ripening--merch-hoodie.png"
    "merch/book-1-anamnesis/book-1-anamnesis--merch-tee.png"
    "merch/book-2-myocardial/book-2-myocardial--merch-tee.png"
    "merch/book-3-ripening/book-3-ripening--merch-tee.png"
    "merch/book-1-anamnesis/book-1-anamnesis--merch-tote.png"

    # Batch 9 (merch finish)
    "merch/book-2-myocardial/book-2-myocardial--merch-tote.png"
    "merch/book-3-ripening/book-3-ripening--merch-tote.png"
    "merch/series/series--merch-hoodie.png"
    "merch/series/series--merch-tee.png"

    # Batch 10 (heroes)
    "book-1-anamnesis--product-hero.png"
    "book-2-myocardial--product-hero.png"
    "book-3-ripening--product-hero.png"
    "book-1-anamnesis--campaign-hero.png"
    "book-2-myocardial--campaign-hero.png"

    # Batch 11
    "book-3-ripening--campaign-hero.png"
    "book-1-anamnesis--window-poster.png"
    "book-2-myocardial--window-poster.png"
    "book-3-ripening--window-poster.png"
    "marketing/events-promos/campaign--main-hero-wide.png"
)

# All high-value candidates worth animating (curated priority order)
CANDIDATES=(
    # === Batch 4: Typo-mask (next platforms) ===
    "covers/book-1-anamnesis/typo-mask/book-1-anamnesis--typo-mask--iphone.png"
    "covers/book-2-myocardial/typo-mask/book-2-myocardial--typo-mask--iphone.png"
    "covers/book-3-ripening/typo-mask/book-3-ripening--typo-mask--iphone.png"
    "covers/book-1-anamnesis/typo-mask/book-1-anamnesis--typo-mask--ipad.png"
    "covers/book-2-myocardial/typo-mask/book-2-myocardial--typo-mask--ipad.png"
    "covers/book-3-ripening/typo-mask/book-3-ripening--typo-mask--ipad.png"
    "covers/book-1-anamnesis/typo-mask/book-1-anamnesis--typo-mask--macos.png"
    "covers/book-2-myocardial/typo-mask/book-2-myocardial--typo-mask--macos.png"
    "covers/book-3-ripening/typo-mask/book-3-ripening--typo-mask--macos.png"

    # === Batch 5: Editorial (remaining platforms) ===
    "covers/book-1-anamnesis/editorial/book-1-anamnesis--editorial--watchos.png"
    "covers/book-2-myocardial/editorial/book-2-myocardial--editorial--watchos.png"
    "covers/book-3-ripening/editorial/book-3-ripening--editorial--watchos.png"
    "covers/book-1-anamnesis/editorial/book-1-anamnesis--editorial--ipad.png"
    "covers/book-2-myocardial/editorial/book-2-myocardial--editorial--ipad.png"
    "covers/book-3-ripening/editorial/book-3-ripening--editorial--ipad.png"
    "covers/book-1-anamnesis/editorial/book-1-anamnesis--editorial--macos.png"
    "covers/book-2-myocardial/editorial/book-2-myocardial--editorial--macos.png"
    "covers/book-3-ripening/editorial/book-3-ripening--editorial--macos.png"

    # === Batch 6: Merch (full set) ===
    "merch/book-1-anamnesis/book-1-anamnesis--merch-hoodie.png"
    "merch/book-2-myocardial/book-2-myocardial--merch-hoodie.png"
    "merch/book-3-ripening/book-3-ripening--merch-hoodie.png"
    "merch/book-1-anamnesis/book-1-anamnesis--merch-tee.png"
    "merch/book-2-myocardial/book-2-myocardial--merch-tee.png"
    "merch/book-3-ripening/book-3-ripening--merch-tee.png"
    "merch/book-1-anamnesis/book-1-anamnesis--merch-tote.png"
    "merch/book-2-myocardial/book-2-myocardial--merch-tote.png"
    "merch/book-3-ripening/book-3-ripening--merch-tote.png"
    "merch/series/series--merch-hoodie.png"
    "merch/series/series--merch-tee.png"

    # === Batch 7: Heroes, Posters, Series, Trilogy ===
    "heroes/book-1-anamnesis--product-hero.png"
    "heroes/book-2-myocardial--product-hero.png"
    "heroes/book-3-ripening--product-hero.png"
    "heroes/book-1-anamnesis--campaign-hero.png"
    "heroes/book-2-myocardial--campaign-hero.png"
    "heroes/book-3-ripening--campaign-hero.png"
    "heroes/book-1-anamnesis--window-poster.png"
    "heroes/book-2-myocardial--window-poster.png"
    "heroes/book-3-ripening--window-poster.png"
    "marketing/events-promos/campaign--main-hero-wide.png"
    "trilogy--product-hero-wide.png"
    "trilogy--product-group.png"

    # === Series typo-mask + editorial (strong unified branding) ===
    "series-somatic-canticles--typo-mask--iphone.png"
    "series-somatic-canticles--typo-mask--ipad.png"
    "series-somatic-canticles--typo-mask--macos.png"
    "series-somatic-canticles--typo-mask--watchos.png"
    "series-somatic-canticles--editorial--iphone.png"
    "series-somatic-canticles--editorial--ipad.png"
    "series-somatic-canticles--editorial--macos.png"
    "series-somatic-canticles--editorial--watchos.png"
)

# Prompt templates (book-specific motion signatures)
prompt_for() {
    local file="$1"
    case "$file" in
        *book-1-anamnesis*)
            echo "subtle golden glow breathing, title shimmering, cinematic product"
            ;;
        *book-2-myocardial*)
            echo "red glow pulsing like heartbeat, title shimmering, cinematic"
            ;;
        *book-3-ripening*)
            echo "warm golden light radiating, title shimmering, cinematic"
            ;;
        *series*|*trilogy*|*campaign*)
            echo "elegant unified cinematic light, slow breathing glow, title shimmer, cinematic product"
            ;;
        *)
            echo "cinematic product, subtle breathing light, title shimmer"
            ;;
    esac
}

# Filter logic
FILTER=""
LIMIT=999
BATCH_SIZE=5

while [[ $# -gt 0 ]]; do
    case "$1" in
        --typo) FILTER="typo-mask" ;;
        --editorial) FILTER="editorial" ;;
        --merch) FILTER="merch" ;;
        --hero) FILTER="hero|poster|campaign|trilogy" ;;
        --count) LIMIT="$2"; shift ;;
        --batch-size|-b) BATCH_SIZE="$2"; shift ;;
        *) ;;
    esac
    shift
done

echo "# Somatic Canticles — Manual Animation Batches (4-5 per batch)"
echo ""
echo "**For manual processing via grok.imagine.ai**"
echo ""
echo "Batches are sized small (4-5 items) for comfortable manual runs without exhausting credits on doctor.sh / test-video.sh."
echo ""
echo "Your first 9 (reference): Watch typo-mask + Editorial iPhone + Bookmarks v2"
echo ""

count=0
batch_num=4

for f in "${CANDIDATES[@]}"; do
    # Skip already done
    skip=false
    for done in "${ALREADY_DONE[@]}"; do
        if [[ "$f" == "$done" ]]; then skip=true; break; fi
    done
    [[ "$skip" == true ]] && continue

    # Apply filter if set
    if [[ -n "$FILTER" ]] && ! echo "$f" | grep -qiE "$FILTER"; then
        continue
    fi

    # Apply limit
    ((count++))
    if (( count > LIMIT )); then break; fi

    url="${REPO_BASE}/${f}"
    prompt=$(prompt_for "$f")

    # Batch grouping (user prefers 4-5 per batch for manual grok.imagine.ai work)
    if (( count == 1 || (count-1) % BATCH_SIZE == 0 )); then
        echo ""
        echo "### Batch ${batch_num}"
        ((batch_num++))
    fi

    echo ""
    echo '```'
    echo "$url"
    echo "→ Animate: $prompt"
    echo '```'
done

echo ""
echo "---"
echo "**Total in this output:** $count   |   Batch size: ${BATCH_SIZE}"
echo "Edit the ALREADY_DONE array in this script as you finish items."