# Bundle architecture

Project Thread ships eleven sibling skill folders under `skills/`. Each contains a `SKILL.md` entry point and `agents/openai.yaml` discovery metadata. Conditional detail stays in the owning skill's `references/`. Sibling relative links work in the complete plugin and in either installer destination.

The daily skill routes work. Setup maps existing records, roadmap sequences area/initiative outcomes, plan owns feature requirements and criteria, and phase executes agreed work. Engineering supplies implementation judgment; iOS adds platform-specific architecture, interaction, reliability, and verification. Documentation owns facts/procedures; Agent Notes own rationale/lifecycle. Review assesses results, while simplification investigates evidence-backed proposals.

Shared [record ownership](../skills/project-thread/references/records.md) and [checkpoints](../skills/project-thread/references/checkpoints.md) are reused across entry points. Notes have one [lifecycle owner](../skills/project-thread-agent-notes/references/lifecycle.md). A project can reuse established filenames and lifecycle equivalents without creating duplicate authority.

Substantial projects use an area or initiative folder whose overview links its plans, issues, phases, and relevant Agent Notes. A lightweight project index summarizes shared priorities and cross-area dependencies. A shared capability has one owning plan; consumers link to that owner and retain their own acceptance criteria. Feature requirements belong to their plan or existing requirements authority, while shared business rules remain in product documentation. Agent Notes stay canonical in their shared lifecycle tree; issues and phase records own work status and verification. In this repository, the existing [roadmap file](roadmap.md) serves as the index, new delivery records are grouped under `docs/roadmaps/`, and the completed v1 plan retains its established path. The [roadmap decision](../.agents/notes/implemented/process/2026-09-05-area-roadmaps.md) records this refinement.

The [iOS skill](../skills/project-thread-ios/SKILL.md) loads engineering and selects only relevant iOS references. It does not mandate a third-party state-management library, persistence engine, coverage percentage, infrastructure footprint, or arbitrary performance target. Backend contracts remain inputs; missing capabilities become explicit dependencies. The framework separates compiled, logic-tested, simulator-tested, device-tested, and unverified behavior.

## Helpers and packaging

- [install.py](../scripts/install.py) preflights every destination and creates links to this checkout. Repeated installs preserve matching links; conflicts block all planned creates. Removal touches only matching links. An unexpected create failure rolls back links made by that attempt; empty parent directories can remain. Removal is best effort if an operating-system error interrupts it and may be safely repeated.
- [check.py](../scripts/check.py) checks the exact skill inventory, the bundle's simple frontmatter/UI scalar conventions, manifest identity/path/version, inline Markdown file-link portability, unfinished scaffold markers, and active note path/status consistency. It is not a general YAML parser, anchor validator, Apple API validator, or semantic reviewer.
- [package.py](../scripts/package.py) validates and writes a deterministic ZIP from explicit distributable roots, excluding build caches and Git internals. It includes the source and evidence needed to inspect/repeat evaluation.

The plugin manifest discovers the same `skills/` tree. Direct installation does not register a marketplace; plugin UI installation is a separate distribution option. Runtime builds, simulators, signing, and device tools come from the adopting application.

The [implementation decision](../.agents/notes/implemented/process/2026-09-05-engineering-ios-suite.md) records why this structure was chosen and its evidence limitations.
