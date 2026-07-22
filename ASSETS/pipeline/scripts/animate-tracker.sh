#!/bin/bash
# animate-tracker.sh
# Tiny local helper for tracking manual grok.imagine.ai runs
# Drop this next to your doctor.sh / test-video.sh

DONE_FILE="${HOME}/.somatic-animate-done"
BATCH_FILE="../plans/ANIMATION_BATCH_REMAINING.md"

mkdir -p "$(dirname "$DONE_FILE")"
touch "$DONE_FILE"

cmd="${1:-status}"

case "$cmd" in
  done|mark)
    shift
    for name in "$@"; do
      echo "$name" >> "$DONE_FILE"
    done
    sort -u -o "$DONE_FILE" "$DONE_FILE"
    echo "Marked as done: $*"
    ;;

  status|left|remaining)
    echo "=== Remaining to animate (from $BATCH_FILE) ==="
    # Extract clean base names from the batch file (the ones still in the "Remaining" section)
    grep -A1 'https://raw.githubusercontent.com/Sheshiyer/somatic-canticles-v3-book-trilogy' "$BATCH_FILE" \
      | grep -o 'book-[0-9][^"]*\.png\|series[^"]*\.png\|campaign[^"]*\.png\|trilogy[^"]*\.png' \
      | sort | uniq \
      | comm -23 - <(sort "$DONE_FILE") || true
    ;;

  reset)
    > "$DONE_FILE"
    echo "Progress reset."
    ;;

  *)
    echo "Usage: $0 [status|done <name1> <name2>|reset]"
    echo "Examples:"
    echo "  $0 status"
    echo "  $0 done book-1-anamnesis--typo-mask--iphone.png book-2-myocardial--merch-hoodie.png"
    echo "  $0 reset"
    ;;
esac