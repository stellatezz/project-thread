# Session checkpoints

Update the existing checkpoint at a phase boundary, before a long interruption, or when handing off incomplete work. Keep enough concrete information to resume without the conversation; link to durable owners rather than pasting the whole plan.

Record:

- Objective, owning area/initiative roadmap, active plan and phase file/section, linked issues and blockers, acceptance criteria still open, and agreed scope or authorization limits. Link other areas' dependency owners and relevant Agent Notes when they affect the next step.
- Repository branch/revision when available, meaningful uncommitted changes, and any other work that must be preserved.
- Implemented behavior and affected paths; separate attempted or proposed changes.
- Verification command or manual journey, result, environment, date, and artifact path. Distinguish compilation, automated logic tests, simulator journeys, physical-device checks, and unverified claims.
- Decisions and their Agent Notes; backend dependencies, mocks, unavailable tools, and unresolved questions.
- The next executable action, its prerequisites, and how to verify it. Include a reproducer for a known failure.

On recovery, compare the checkpoint with the working tree, current docs, and results. Resolve drift before continuing. Do not rerun an expensive check solely because a session changed if the artifact still covers the same code and environment. Do rerun when code, configuration, or the underlying claim changed.

Keep checkpoints free of credentials, private user data, and disposable transcript detail. Retain older checkpoints only when they add useful history; never use them as current business authority.
