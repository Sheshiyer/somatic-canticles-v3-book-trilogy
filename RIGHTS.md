# Somatic Canticles — Rights and Versioning Policy (v2 master copy)

(This is the authoritative copy synchronized from the development planning tree. See the full version at the development repo for any updates.)

**Status:** Authoritative (2026-06-03) — **v2.1** (2026-07-22)
**Applies to:** All published book editions (print, ebook, omnibus) and any derivative text.

## Absolute Source of Truth

The canonical, authoritative text for the published *Somatic Canticles* trilogy resides in this directory tree (the v2 itself):

- **Per-chapter source:** `CHAPTERS/book_1/`, `CHAPTERS/book_2/`, `CHAPTERS/book_3/` (27 files total).
- **Compiled full texts:** `COMPILED/`.
- **Chapter count for all publishing purposes:** 27 (locked by Author Decision 2026-06-03).

The development manuscript tree (elsewhere) is for iteration only.

## Versioning Policy + Propagation

See the full RIGHTS.md in the planning tree for complete rules.

**Summary for this source:**
- Books = fixed archival text from this v2 at lock time.
- Apps must import/regenerate their core chapter prose from this v2 (or tagged export).
- Add `book_version` / `source_commit` to all app chapter records.
- Drift without reconciliation violates the Work.

**How to propagate from here:**
- Lock a version of this v2.
- Mobile: run import against CHAPTERS or COMPILED snapshot.
- Webapp: regenerate data JSONs from the COMPILED or per-chapter files.
- Embed version in every published artifact.

Full policy and enforcement details live alongside the development source.
