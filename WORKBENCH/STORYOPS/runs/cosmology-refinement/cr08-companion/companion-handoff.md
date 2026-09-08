# CR-08.04 companion handoff

Status: complete handoff. No UI, API, database, mobile, web, or Selemene code changed.

## Content API shape

Each companion content record should carry:

- `situation_id`
- `manuscript_chapter_id`
- `source_revision_id`
- `practice_id`
- `app_entry_id`
- `surface`: mobile, web, source-pack, or Selemene-context
- `status`: developed, placeholder, retired, migrated, review-only
- `aliases`
- `introduced_by`
- `reusable_after_intro`
- `privacy_policy`
- `retirement_reason`

## Owning states

- Book workspace owns accepted manuscript source revision and StoryOps evidence.
- Web app owns expanded chapter/practice content, route/database rendering, and web entry IDs.
- Mobile app owns local/native chapter authority, offline access, and practice reuse state.
- Selemene engine owns optional symbolic context and witness prompts, not practice completion or canon proof.
- Source packs own portable provenance and offline revision identity.

## Behavior cases for app owners

1. Reader finishes Chapter 6 introduction and declines the practice: practice becomes reusable; no reflection required.
2. Reader has legacy Chapter 6 unlock but no introduction event: preserve access, mark introduction unknown, offer gentle guided intro without revoking use.
3. Reader receives an unfavorable timing/biorhythm signal: can still open an introduced practice; signal is context, not revocation.
4. Reader opens web exploration without mobile app: book situation is understandable without account, report, or birth profile.
5. Practice is retired/replaced: aliases remain; historical reflections are not reinterpreted as moral progress.

## Migration proposal

Create an owner-reviewed migration that separates chapter progress, introduction events, practice attempts, reflections, symbolic timing, and reports. Do not infer production parity from static bundled content or source comments. Verify current live routes before deployment.
