# Marketing Assets

This folder contains campaign, email, announcement, and social assets.

## Current Structure

- **ads/** — Social media ads (Facebook feed, Instagram Story, Twitter).  
  Best organized folder: nested by book (`book-1-anamnesis/`, `book-2-myocardial/`, etc.) + `series/`.

- **announcements/** — Launch announcements, pre-order graphics, limited edition, etc. (currently flat).

- **email/** — Email campaign graphics (welcome, prelaunch, launch day, thank you).

- **events-promos/** — Event graphics and wide campaign heroes (book launch, readings, signings, main hero).

## Recommended Pattern (for future assets)

When adding new book-specific marketing assets, prefer the same nesting style used in `ads/`:

```
marketing/
├── ads/
│   ├── book-1-anamnesis/
│   ├── book-2-myocardial/
│   ├── book-3-ripening/
│   └── series/
├── announcements/
├── email/
└── events-promos/
```

## Notes

- The `ads/` folder is currently the most mature example of good organization.
- If `announcements/`, `email/`, or `events-promos/` grow significantly, consider applying book-level nesting for consistency.

See the root `CHANGES.md` and `PHASE4_PROPOSAL.md` for reorganization history and future plans.
