# Repository record ownership

Keep one authoritative home for each fact. Adapt existing equivalents before creating these default paths; do not rename a working documentation system just to adopt this suite.

| Record | Owns | Default location |
| --- | --- | --- |
| Context map | Links to current authorities, commands, and active work | `docs/codebase.md` |
| Business reference | Current product behavior, rules, user needs, constraints | `docs/product.md` |
| Technical reference | Current architecture, contracts, state ownership, persistence | `docs/architecture.md` and focused references |
| Testing reference | Supported environments, actual commands, test strategy | `docs/testing.md` |
| Roadmap index | Links to area/initiative roadmaps, shared priorities, cross-area dependencies | `docs/roadmaps/README.md` or an existing `docs/roadmap.md` |
| Area or initiative roadmap | Scoped outcomes, priorities, milestones, dependencies, and links to its delivery records | `docs/roadmaps/<area-or-initiative>/README.md` |
| Feature plan | Feature requirements, acceptance criteria, decisions to resolve, ordered phase links | `docs/roadmaps/<area>/plans/<feature>.md` |
| Phase | A bounded delivery step, related issues, acceptance criteria, status, and verification | `docs/roadmaps/<area>/phases/<feature>/<phase>.md` |
| Issue | A concrete problem or work item, expected outcome, owner links, status, and resolution evidence | `docs/roadmaps/<area>/issues/<issue>.md` |
| Agent Note | Problem, decision rationale, genuine alternatives, consequences | `.agents/notes/<lifecycle>/<kind>/<date>-<topic>.md` |
| Cookbook | A repeatable procedure learned in this repository | `docs/cookbooks/<procedure>.md` |
| Checkpoint | Work state and evidence needed by the next session | `docs/checkpoints/current.md` |

Feature-specific requirements have one owner, normally the feature plan. Link existing requirements records when they already own that behavior; keep shared business rules in the business reference. Plans own intended behavior until it ships. Current reference docs describe implemented reality; an explicit limitation is a fact too.

For a substantial project, area/initiative roadmaps sequence those requirements and plans, and a lightweight project index connects them. Each plan and issue has one primary roadmap owner; other areas reference it as a dependency. Roadmap status derives from linked plan/phase evidence. The index summarizes shared priorities and dependency readiness without becoming another detailed execution ledger. Read [roadmap guidance](../../make-codebase-agentic-roadmap/SKILL.md) when organizing or splitting these records.

Group delivery records in the roadmap folder so its overview is the entry point for plans, phases, issues, and relevant Agent Notes. Agent Notes retain one canonical copy in the shared lifecycle tree and link to affected delivery records. Existing layouts such as `docs/plans/<feature>.md`, external issue trackers, or short phases within a plan remain valid; map and link their owners instead of duplicating or relocating them automatically. Use [delivery-record guidance](delivery-records.md) when creating or connecting issue and phase files.

Agent Notes explain why; references explain what; cookbooks explain how. Avoid parallel engineering documents for every feature.

Suggested plan states are `draft`, `ready`, `in-progress`, `blocked`, and `complete`. A phase can be complete only when its acceptance criteria are met, relevant checks have run, and affected records are current. An unavailable required check leaves an evidence gap; a separately authorized deferral must change the criteria explicitly, preserving the reason. Never turn a gap into a pass.

Every non-trivial change adds or updates an Agent Note, including a durable finding that changes engineering direction. Search for the current owner first. Use [Agent Notes](../../make-codebase-agentic-agent-notes/SKILL.md) for lifecycle and supersession; do not duplicate those rules in plans. Trivial spelling, formatting, and mechanically obvious edits do not need ceremonial notes.

Repository instructions describe local conventions and entry paths. Skills supply reusable judgment and procedures; they do not override product requirements or authorize new external actions.

The documentation skill owns [document structure](../../make-codebase-agentic-documentation/references/document-structure.md), [technical writing](../../make-codebase-agentic-documentation/references/technical-writing.md), and [instruction hierarchy](../../make-codebase-agentic-documentation/references/instruction-hierarchy.md). Reuse those references when creating or reviewing records. One maintained explanation can support multiple readers; retain essential local behavior where a caller needs it and link extended rationale to its owner.
