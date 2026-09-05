# Current checkpoint

Updated: 2026-09-05

Objective: complete the approved Make Codebase Agentic revamp and rename under the [skill-suite roadmap](../roadmaps/skill-suite/README.md), [plan](../roadmaps/skill-suite/plans/readable-agentic-codebase.md), [phase](../roadmaps/skill-suite/phases/readable-agentic-codebase/01-revamp-and-migrate.md), and [issue](../roadmaps/skill-suite/issues/readable-repository-guidance.md). The [proposed decision](../../.agents/notes/proposed/process/2026-09-05-readable-agentic-codebase.md) records the naming, guidance ownership, and migration choices.

The source directory is `make-codebase-agentic`, on `main`. Its origin is the public [stellatezz/make-codebase-agentic repository](https://github.com/stellatezz/make-codebase-agentic). The local revamp is not yet committed or pushed; the previous source revision is `b656689`.

The suite has eleven renamed skills and twenty-one conditional references. Six new references cover document structure, technical writing, codebase documentation, instruction hierarchy, worked examples, and code organization. Setup, engineering, and review reuse those owners. Root, skills, docs, and note instructions provide relevant navigation. Plugin version 0.2.0 and package naming reflect the new identity.

All eleven user-level links under `~/.agents/skills` point to this checkout's new skill names. The migration removed only matching legacy links; a repeated preview preserves the new installation. [Migration instructions](../migration.md) cover moved checkouts and repository-level installations. Start a new Codex thread to discover the renamed skills. No marketplace registration or release publication is part of this change.

Verified so far: structural/file-link checks, 16 helper tests, all eleven skill validators, plugin validation, installed-link resolution, and unchanged historical result files. The [revamp results](../../evals/results/2026-09-05-revamp.md) retain both independent documentation/adoption outputs and their semantic review, including a successful replay of 13 storage checks and the README example. The complete 0.2.0 archive is reproducible, validates after extraction, and installs all eleven skills. Public source commit/push and final record closure remain pending.

The [original v1 evidence](../../evals/results/2026-09-05-v1.md) remains intact, including the prior Swift fixture results. This revamp adds no iOS application, simulator journey, physical-device measurement, or Claude runtime verification. General writing and instruction guidance does not establish host-specific automatic discovery.

Next action: commit and push the verified revamp, then finalize the phase, issue, and note with the publication evidence. Keep this source path stable for installed links and preserve sibling repositories and unrelated configuration.
