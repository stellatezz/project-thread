# Current checkpoint

Updated: 2026-09-05

The approved Make Codebase Agentic revamp and rename are complete under the [skill-suite roadmap](../roadmaps/skill-suite/README.md), [plan](../roadmaps/skill-suite/plans/readable-agentic-codebase.md), [phase](../roadmaps/skill-suite/phases/readable-agentic-codebase/01-revamp-and-migrate.md), and [resolved issue](../roadmaps/skill-suite/issues/readable-repository-guidance.md). The [implemented decision](../../.agents/notes/implemented/process/2026-09-05-readable-agentic-codebase.md) records naming, guidance ownership, migration, and evidence limits.

The source directory is `make-codebase-agentic`, on `main`. Its origin is the public [stellatezz/make-codebase-agentic repository](https://github.com/stellatezz/make-codebase-agentic). Revamp commit `fa8890f` is pushed; this checkpoint accompanies its completion record. On recovery, compare `git status -sb`, `git rev-parse HEAD`, and `git ls-remote origin refs/heads/main` to establish current synchronization.

The suite has eleven renamed skills and twenty-one conditional references. Six new references cover document structure, technical writing, codebase documentation, instruction hierarchy, worked examples, and code organization. Setup, engineering, and review reuse those owners. Root, skills, docs, and note instructions provide relevant navigation. Plugin version 0.2.0 and package naming reflect the new identity.

All eleven user-level links under `~/.agents/skills` point to this checkout's new skill names. The migration removed only matching legacy links; a repeated preview preserves the new installation. [Migration instructions](../migration.md) cover moved checkouts and repository-level installations. Start a new Codex thread to discover the renamed skills. No marketplace registration or release publication is part of this change.

Verification passed: structural/file-link checks, 16 helper tests, all eleven skill validators, plugin validation, installed-link resolution, and unchanged historical result files. The [revamp results](../../evals/results/2026-09-05-revamp.md) retain both independent documentation/adoption outputs and their semantic review, including a successful replay of 13 storage checks and the README example. The complete 0.2.0 archive is reproducible, validates after extraction, and installs all eleven skills. The verified source is pushed to the public repository.

The [original v1 evidence](../../evals/results/2026-09-05-v1.md) remains intact, including the prior Swift fixture results. This revamp adds no iOS application, simulator journey, physical-device measurement, or Claude runtime verification. General writing and instruction guidance does not establish host-specific automatic discovery.

No required work remains in this phase. Next action: in a new Codex thread, use `$make-codebase-agentic-setup` in the selected adopting repository, or `$make-codebase-agentic` to resume its recorded work. Select an actual application and acceptance criteria before claiming app or device readiness. Keep this source path stable for installed links and preserve sibling repositories and unrelated configuration.
