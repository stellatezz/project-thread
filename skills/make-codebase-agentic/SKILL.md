---
name: make-codebase-agentic
description: Carry software work forward using repository instructions, current documentation, feature plans, and verified checkpoints. Use for daily work or resuming a project with Make Codebase Agentic; route specialized work to the matching skill.
---

# Make Codebase Agentic

Recover context → plan the outcome → apply engineering and platform guidance → implement the phase → verify → update repository records.

## Recover the thread

Read applicable `AGENTS.md`, the repository's context map, current checkpoint, and linked active plan, phase, issues, and owning roadmap. For a substantial project, use the roadmap index to locate the relevant area or initiative and its dependencies. Inspect the working tree and relevant code before trusting recorded progress. Read only the business rules, architecture, cookbooks, and Agent Notes needed for the next outcome. A checkpoint is a navigation aid; current code and verification establish what exists.

Use the repository's established paths. For a new adoption, use [setup](../make-codebase-agentic-setup/SKILL.md). The [record ownership reference](references/records.md) defines the suite's shared boundaries; all companion skills reuse it.

## Route by the work

| Need | Skill |
| --- | --- |
| Adopt the framework or map existing records | [make-codebase-agentic-setup](../make-codebase-agentic-setup/SKILL.md) |
| Sequence area/initiative outcomes and cross-area dependencies | [make-codebase-agentic-roadmap](../make-codebase-agentic-roadmap/SKILL.md) |
| Own feature requirements, resolve behavior, and define phases | [make-codebase-agentic-plan](../make-codebase-agentic-plan/SKILL.md) |
| Execute or resume an agreed phase | [make-codebase-agentic-phase](../make-codebase-agentic-phase/SKILL.md) |
| Design and implement substantial software changes | [make-codebase-agentic-engineering](../make-codebase-agentic-engineering/SKILL.md) |
| Develop a native iOS client | [make-codebase-agentic-ios](../make-codebase-agentic-ios/SKILL.md) |
| Maintain current facts or cookbooks | [make-codebase-agentic-documentation](../make-codebase-agentic-documentation/SKILL.md) |
| Preserve rationale or transition a note | [make-codebase-agentic-agent-notes](../make-codebase-agentic-agent-notes/SKILL.md) |
| Assess a change and its evidence | [make-codebase-agentic-review](../make-codebase-agentic-review/SKILL.md) |
| Investigate opportunities to remove complexity | [make-codebase-agentic-simplify](../make-codebase-agentic-simplify/SKILL.md) |

Load only the needed skills. Small local fixes need proportionate planning. A feature with consequential business or public-contract choices needs those choices resolved in its plan; routine implementation choices stay with the engineer. Existing user authorization carries forward. Do not insert a mandatory simplification audit after every edit.

## Leave a resumable result

Verify through the actual application entry path where relevant. Keep proposed work distinct from implemented behavior. Every non-trivial change adds or updates an Agent Note. Update affected facts, learned cookbooks, phase evidence, and the [checkpoint](references/checkpoints.md) before handing off. If verification is unavailable, record the gap and the next executable action instead of claiming completion.
