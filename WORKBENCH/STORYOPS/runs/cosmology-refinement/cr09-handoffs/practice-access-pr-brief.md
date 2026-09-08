# CR-09.02 shared practice-access PR brief

Status: bounded implementation handoff. No app/backend repo files changed.

## Goal

Implement the CR-08 access contract in the actual persistence layer: first guided introduction unlocks permanent reuse; attempts/reflections/timing/progress/outcomes remain separate facts.

## Required behavior cases

1. First introduction creates a durable `introduced` event and grants reusable access.
2. Decline, pause, failed attempt, skipped reflection, private reflection, low biorhythm, or changing cycle value does not revoke introduced practice.
3. Legacy chapter unlock preserves historical access but marks guided introduction as unknown when no event exists.
4. User isolation: one reader's introduction/reuse state never grants another reader access.
5. Content revision: source content can change version without deleting historical attempts/reflections.

## Data shape

Separate tables/collections or records for:

- source content identity
- guided introduction events
- practice access/reuse state
- attempts
- reflections
- timing/context signals
- reports

Do not implement a second policy per UI. Web and mobile should consume the same contract.
