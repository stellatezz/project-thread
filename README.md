# Project Thread

Eleven connected skills for building software in verified phases, with native iOS client guidance for ambitious products. Keep product intent, current technical facts, decisions, procedures, and session handoffs connected.

**Recover context → plan the outcome → apply engineering and iOS guidance → implement the phase → verify → update docs, notes, cookbooks, and checkpoints.**

## The bundle

| Skill | Owns |
| --- | --- |
| [project-thread](skills/project-thread/SKILL.md) | Daily context recovery and routing |
| [project-thread-setup](skills/project-thread-setup/SKILL.md) | Adoption and mapping existing records |
| [project-thread-roadmap](skills/project-thread-roadmap/SKILL.md) | Area/initiative roadmaps, shared priorities, and dependencies |
| [project-thread-plan](skills/project-thread-plan/SKILL.md) | Feature requirements, decisions, and acceptance criteria |
| [project-thread-phase](skills/project-thread-phase/SKILL.md) | Implementation and evidence for an agreed phase |
| [project-thread-documentation](skills/project-thread-documentation/SKILL.md) | Current facts and learned cookbooks |
| [project-thread-agent-notes](skills/project-thread-agent-notes/SKILL.md) | Rationale, alternatives, and decision lifecycle |
| [project-thread-review](skills/project-thread-review/SKILL.md) | Assessment of behavior and evidence |
| [project-thread-simplify](skills/project-thread-simplify/SKILL.md) | Evidence-backed simplification proposals |
| [project-thread-engineering](skills/project-thread-engineering/SKILL.md) | Maintainable design, implementation, and verification |
| [project-thread-ios](skills/project-thread-ios/SKILL.md) | iOS architecture, interaction, reliability, and device evidence |

The iOS skill includes conditional guidance for location/live experiences, feeds/uploads, and media creation/editing. New apps default to Swift and SwiftUI with UIKit where justified; existing apps retain established architecture. Each project selects its actual state management, persistence, budgets, and supported environments.

## Organize a substantial project

Use roadmaps for cohesive product areas or major initiatives, connected by a lightweight project index:

```text
Roadmap index: shared priorities and cross-area dependencies
├── Account and identity roadmap
│   └── Feature plans: requirements → acceptance criteria → phases
├── Feed and discovery roadmap
│   └── Feature plans: requirements → acceptance criteria → phases
└── Media editing roadmap
    └── Feature plans: requirements → acceptance criteria → phases
```

Each roadmap normally has a folder under `docs/roadmaps/<area-or-initiative>/`. Its `README.md` links the overview, plans, issues, phase files, and relevant Agent Notes. The project index is normally `docs/roadmaps/README.md`; this repository preserves [docs/roadmap.md](docs/roadmap.md) as its existing index. Reuse established paths, including existing plans or issue trackers.

```text
docs/roadmaps/media-editor/
  README.md
  plans/trim-and-export.md
  phases/trim-and-export/01-project-recovery.md
  issues/export-cancellation.md
.agents/notes/implemented/architecture/export-ownership.md
```

Each plan and issue has one primary roadmap owner. Phases group work into verifiable delivery steps, and issues track concrete problems or work items. Agent Notes preserve decisions and link to the affected records from one canonical lifecycle tree. Other areas reference shared capabilities as dependencies. Detailed requirements and acceptance criteria have one owner in the plan or an existing requirements document; shared business rules stay in product documentation. Roadmap progress follows verified plan/phase evidence. See [delivery-record guidance](skills/project-thread/references/delivery-records.md) for links and completion rules.

## Install in Codex

Requires Python 3.9+ and a filesystem with symlink support. Keep this checkout at a stable path. Install the complete bundle so companion references resolve.

```sh
# Preview, then install for your user.
python3 scripts/install.py --user --dry-run
python3 scripts/install.py --user

# Or install only for an existing repository.
python3 scripts/install.py --repo /path/to/app --dry-run
python3 scripts/install.py --repo /path/to/app
```

The installer links all eleven skills into `~/.agents/skills` or the target repository's `.agents/skills`, following Codex's [skill discovery locations](https://learn.chatgpt.com/docs/build-skills). Repeating installation preserves the same links. Conflicting files/directories/links and blocked parent paths stop installation before any skill is added. Existing unrelated skills remain untouched. It does not modify app code, project documentation, or plugin marketplace settings.

Start a new Codex thread in the app repository, then invoke:

```text
Use $project-thread-setup to adopt this framework using our existing documentation.
Use $project-thread to resume the next agreed feature phase.
Use $project-thread-ios to implement and verify this iOS journey.
```

Skills support automatic discovery as well as explicit invocation. Updating this checkout updates linked skill content; use a new thread to pick it up. Remove only links owned by this checkout with `python3 scripts/install.py --user --remove` or the corresponding `--repo` command. Remove links before moving/deleting the checkout, then reinstall from its new location; conflicting old links are preserved for inspection.

## Plugin and distribution

The repository is also a skill-only Codex plugin with [.codex-plugin/plugin.json](.codex-plugin/plugin.json). It supplies no MCP servers, external account connections, hooks, or automatic deployment. Direct skill installation above is the tested default; plugin marketplace registration is optional and separate.

```sh
python3 scripts/check.py
python3 -m unittest discover -s tests -v
python3 scripts/package.py
```

Packaging writes a complete, reproducible ZIP under `dist/` containing the plugin, skills, helpers, docs, and evaluation fixtures. Extract it to a stable location and run its installer, or use it as a source for your chosen Codex plugin marketplace. See [testing](docs/testing.md) for validator and behavioral evidence limits.

## Operating boundaries

Current facts belong in authoritative docs, repeatable project procedures in cookbooks, and every non-trivial change adds or updates an Agent Note. Notes retain proposed, implemented, rejected, and archived lifecycles. Plans and phases track intended work and verified progress; checkpoints support continuation without the original conversation. [Record ownership](skills/project-thread/references/records.md) defines the shared rules.

Uber, Instagram, and CapCut illustrate demanding client journeys, not prescribed architectures. V1 focuses on native iOS clients, excellent launch quality, and growth in phases. Android, backend implementation, automatic publishing, and production-scale claims without measurements are outside this version's scope. Simplification remains an investigation/proposal workflow, not an audit after every edit.

See the [architecture](docs/architecture.md), [context map](docs/project-thread.md), [evaluation fixtures](evals/README.md), and [source acknowledgments](THIRD_PARTY_NOTICES.md).
