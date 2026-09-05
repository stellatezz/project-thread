# Project context

Make Codebase Agentic is a standalone skill bundle for readable repository knowledge, maintainable engineering, and native iOS and web client development. It has no application runtime or backend.

| Authority | Location |
| --- | --- |
| Product scope, public skills, installation | [README](../README.md) |
| Bundle architecture and ownership | [Architecture](architecture.md) |
| Validation commands and evidence limits | [Testing](testing.md) |
| Shared priorities and cross-area dependencies | [Roadmap index](roadmap.md) |
| Bundle outcomes and delivery records | [Skill-suite roadmap](roadmaps/skill-suite/README.md) |
| Candidate application evaluation | [iOS-adoption roadmap](roadmaps/ios-adoption/README.md) |
| Current implementation plan and inline phase | [Web client guidance](roadmaps/skill-suite/plans/web-client.md) |
| Previous completed phase | [Revamp and migrate](roadmaps/skill-suite/phases/readable-agentic-codebase/01-revamp-and-migrate.md) |
| Previous resolved work item | [Readable repository guidance](roadmaps/skill-suite/issues/readable-repository-guidance.md) |
| Upgrade instructions | [Project Thread migration](migration.md) |
| Completed foundation | [Engineering and iOS v1](plans/engineering-ios-v1.md) |
| Current continuation state | [Checkpoint](checkpoints/current.md) |
| Shared adopter records | [Record ownership](../skills/make-codebase-agentic/references/records.md) |
| Decision index | [Agent Notes](../.agents/notes/README.md) |
| Evaluation inputs and method | [Behavioral fixtures](../evals/README.md) |

Run commands from the repository root. The primary check is `python3 scripts/check.py`; helper regressions use `python3 -m unittest discover -s tests -v`. iOS and web application commands belong in each adopting project's testing reference and cookbooks.
