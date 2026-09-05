---
name: project-thread
description: Resume and carry forward a software project using its recorded context, feature plans, phase evidence, and checkpoints. Use for daily work or continuing a previous session; route specialized tasks to the matching Project Thread skill.
---

# Project Thread

Recover context → plan the outcome → apply engineering and platform guidance → implement the phase → verify → update repository records.

## Recover the thread

Read applicable `AGENTS.md`, the repository's context map, current checkpoint, and linked active plan, phase, issues, and owning roadmap. For a substantial project, use the roadmap index to locate the relevant area or initiative and its dependencies. Inspect the working tree and relevant code before trusting recorded progress. Read only the business rules, architecture, cookbooks, and Agent Notes needed for the next outcome. A checkpoint is a navigation aid; current code and verification establish what exists.

Use the repository's established paths. For a new adoption, use [setup](../project-thread-setup/SKILL.md). The [record ownership reference](references/records.md) defines the suite's shared boundaries; all companion skills reuse it.

## Route by the work

| Need | Skill |
| --- | --- |
| Adopt the framework or map existing records | [project-thread-setup](../project-thread-setup/SKILL.md) |
| Sequence area/initiative outcomes and cross-area dependencies | [project-thread-roadmap](../project-thread-roadmap/SKILL.md) |
| Own feature requirements, resolve behavior, and define phases | [project-thread-plan](../project-thread-plan/SKILL.md) |
| Execute or resume an agreed phase | [project-thread-phase](../project-thread-phase/SKILL.md) |
| Design and implement substantial software changes | [project-thread-engineering](../project-thread-engineering/SKILL.md) |
| Develop a native iOS client | [project-thread-ios](../project-thread-ios/SKILL.md) |
| Maintain current facts or cookbooks | [project-thread-documentation](../project-thread-documentation/SKILL.md) |
| Preserve rationale or transition a note | [project-thread-agent-notes](../project-thread-agent-notes/SKILL.md) |
| Assess a change and its evidence | [project-thread-review](../project-thread-review/SKILL.md) |
| Investigate opportunities to remove complexity | [project-thread-simplify](../project-thread-simplify/SKILL.md) |

Load only the needed skills. Small local fixes need proportionate planning. A feature with consequential business or public-contract choices needs those choices resolved in its plan; routine implementation choices stay with the engineer. Existing user authorization carries forward. Do not insert a mandatory simplification audit after every edit.

## Leave a resumable result

Verify through the actual application entry path where relevant. Keep proposed work distinct from implemented behavior. Every non-trivial change adds or updates an Agent Note. Update affected facts, learned cookbooks, phase evidence, and the [checkpoint](references/checkpoints.md) before handing off. If verification is unavailable, record the gap and the next executable action instead of claiming completion.
