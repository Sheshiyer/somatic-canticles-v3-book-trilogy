# CR-08.03 practice access contract

Status: complete planning contract. No app code changed.

## Rules

- First guided introduction unlocks permanent reuse of that practice.
- Later chapters may introduce additional practices; they do not revoke earlier introduced practices.
- Attempts, reflections, timing recommendations, reading progress, biorhythm values, reports, and outcomes are separate facts.
- Decline, pause, return, low energy, reduced cycle values, or an unfavorable symbolic reading cannot revoke an introduced practice.
- Privacy is not a progress requirement. Reflection may be local, skipped, private, or exported only by explicit user action.
- Historical unlock events preserve legacy progress, but do not prove that guided introduction occurred.

## State model

`not_introduced -> introduced -> reusable -> retired`

Attempt states are separate: `not_attempted`, `attempted`, `paused`, `declined`, `reflected_private`, `reflected_shared`.

No attempt state changes practice access.
