# Make Codebase Agentic

**Give coding agents the context, workflows, and checks to build reliably.**

Make Codebase Agentic helps people and coding agents understand a repository, make maintainable changes, verify behavior, and continue work across sessions. Twelve connected skills cover repository setup, readable documentation, engineering, delivery planning, and native iOS and web development.

The repository keeps instructions, current technical facts, decisions, procedures, and work status connected. Guidance is detailed where a reader needs it: short entry points lead to focused references, complete behavior descriptions, and worked examples. Installing the skills makes that workflow available; applying setup adapts it to an actual codebase.

**Recover context → plan the outcome → apply engineering and platform guidance → implement the phase → verify → update docs, notes, cookbooks, and checkpoints.**

## The bundle

| Skill | Owns |
| --- | --- |
| [make-codebase-agentic](skills/make-codebase-agentic/SKILL.md) | Daily context recovery and routing |
| [make-codebase-agentic-setup](skills/make-codebase-agentic-setup/SKILL.md) | Adoption and mapping existing records |
| [make-codebase-agentic-roadmap](skills/make-codebase-agentic-roadmap/SKILL.md) | Area/initiative roadmaps, shared priorities, and dependencies |
| [make-codebase-agentic-plan](skills/make-codebase-agentic-plan/SKILL.md) | Feature requirements, decisions, and acceptance criteria |
| [make-codebase-agentic-phase](skills/make-codebase-agentic-phase/SKILL.md) | Implementation and evidence for an agreed phase |
| [make-codebase-agentic-documentation](skills/make-codebase-agentic-documentation/SKILL.md) | Documentation structure, precise prose, code explanations, instructions, and cookbooks |
| [make-codebase-agentic-agent-notes](skills/make-codebase-agentic-agent-notes/SKILL.md) | Rationale, alternatives, and decision lifecycle |
| [make-codebase-agentic-review](skills/make-codebase-agentic-review/SKILL.md) | Assessment of behavior and evidence |
| [make-codebase-agentic-simplify](skills/make-codebase-agentic-simplify/SKILL.md) | Evidence-backed simplification proposals |
| [make-codebase-agentic-engineering](skills/make-codebase-agentic-engineering/SKILL.md) | Maintainable design, implementation, and verification |
| [make-codebase-agentic-ios](skills/make-codebase-agentic-ios/SKILL.md) | iOS architecture, interaction, reliability, and device evidence |
| [make-codebase-agentic-web](skills/make-codebase-agentic-web/SKILL.md) | Web architecture, responsive interaction, accessibility, browser reliability, and evidence |

The web skill adapts to the existing framework and covers routing/rendering, responsive design, accessible forms, async state, browser lifecycle, and measured performance. It does not prescribe one frontend stack.

The iOS skill includes conditional guidance for location/live experiences, feeds/uploads, and media creation/editing. New apps default to Swift and SwiftUI with UIKit where justified; existing apps retain established architecture. Each project selects its actual state management, persistence, budgets, and supported environments.

## Readable knowledge for people and agents

The [documentation skill](skills/make-codebase-agentic-documentation/SKILL.md) teaches document placement, technical writing, codebase documentation, instruction hierarchy, and editorial judgment through worked examples. The [engineering skill](skills/make-codebase-agentic-engineering/SKILL.md) connects that knowledge to code organization, state ownership, interfaces, failure behavior, and verification.

A repository's root instructions orient the reader and point to relevant local rules. Architecture explains how components fit together; component references describe detailed behavior; cookbooks explain proven procedures; Agent Notes preserve consequential decisions. Local API documentation retains the conditions and guarantees a caller needs, with links to extended explanations. Detail has an owner and a reading path.

The suite adapts existing `AGENTS.md`, `CLAUDE.md`, and equivalent entry files through [instruction-hierarchy guidance](skills/make-codebase-agentic-documentation/references/instruction-hierarchy.md). It preserves unique rules and separates valid file links from verified host discovery. The Codex installation below is tested; an adopting repository must verify other tools' loading behavior in its own environment.

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

Each plan and issue has one primary roadmap owner. Phases group work into verifiable delivery steps, and issues track concrete problems or work items. Agent Notes preserve decisions and link to the affected records from one canonical lifecycle tree. Other areas reference shared capabilities as dependencies. Detailed requirements and acceptance criteria have one owner in the plan or an existing requirements document; shared business rules stay in product documentation. Roadmap progress follows verified plan/phase evidence. See [delivery-record guidance](skills/make-codebase-agentic/references/delivery-records.md) for links and completion rules.

Roadmaps have an independent [lifecycle](skills/make-codebase-agentic-roadmap/references/lifecycle.md): draft, active, paused, completed, or retired. An ongoing area can remain active after its current milestones finish; a bounded initiative completes against its defined acceptance criteria. Archive completed or retired roadmaps later while retaining their delivery status and links. Linked Agent Notes keep their own lifecycle.

[Record dates](skills/make-codebase-agentic/references/record-dates.md) define `Created` and `Updated` for roadmaps, indexes, plans, separate phases, and Markdown issues. Agent Notes keep their original date in the filename; archival adds an explicit sealing date. Unknown legacy creation dates remain explicit rather than being guessed.

## Install in Codex

Requires Python 3.9+ and a filesystem with symlink support. Keep this checkout at a stable path. Install the complete bundle so companion references resolve.

```sh
git clone https://github.com/stellatezz/make-codebase-agentic.git
cd make-codebase-agentic

# Preview, then install for your user.
python3 scripts/install.py --user --dry-run
python3 scripts/install.py --user

# Or install only for an existing repository.
python3 scripts/install.py --repo /path/to/app --dry-run
python3 scripts/install.py --repo /path/to/app
```

The installer links all twelve skills into `~/.agents/skills` or the target repository's `.agents/skills`, following Codex's [skill discovery locations](https://learn.chatgpt.com/docs/build-skills). Repeating installation preserves the same links. Conflicting files/directories/links and blocked parent paths stop installation before any skill is added. Existing unrelated skills remain untouched. It does not modify app code, project documentation, or plugin marketplace settings.

Start a new Codex thread in the app repository, then invoke:

```text
Use $make-codebase-agentic-setup to adopt this framework using our existing documentation.
Use $make-codebase-agentic to resume the next agreed feature phase.
Use $make-codebase-agentic-ios to implement and verify this iOS journey.
Use $make-codebase-agentic-web to implement and verify this web journey.
```

Skills support automatic discovery as well as explicit invocation. Updating this checkout updates linked skill content; use a new thread to pick it up. Remove only links owned by this checkout with `python3 scripts/install.py --user --remove` or the corresponding `--repo` command. Remove links before moving/deleting the checkout, then reinstall from its new location; conflicting old links are preserved for inspection.

Upgrading from Project Thread: follow [the migration guide](docs/migration.md) to replace the old skill links after moving or updating the checkout. The eleven invocation names now use `make-codebase-agentic` in place of `project-thread`.

## Plugin and distribution

The repository is also a skill-only Codex plugin with [.codex-plugin/plugin.json](.codex-plugin/plugin.json). It supplies no MCP servers, external account connections, hooks, or automatic deployment. Direct skill installation above is the tested default; plugin marketplace registration is optional and separate.

```sh
python3 scripts/check.py
python3 -m unittest discover -s tests -v
python3 scripts/package.py
```

Packaging writes a complete, reproducible ZIP under `dist/` containing the plugin, skills, helpers, docs, and evaluation fixtures. Extract it to a stable location and run its installer, or use it as a source for your chosen Codex plugin marketplace. See [testing](docs/testing.md) for validator and behavioral evidence limits.

## Operating boundaries

Current facts belong in authoritative docs, repeatable project procedures in cookbooks, and every non-trivial change adds or updates an Agent Note. Notes retain proposed, implemented, rejected, and archived lifecycles. Plans and phases track intended work and verified progress; checkpoints support continuation without the original conversation. [Record ownership](skills/make-codebase-agentic/references/records.md) defines the shared rules.

Uber, Instagram, and CapCut illustrate demanding client journeys, not prescribed architectures. Common repository and engineering guidance applies across software projects; the specialist platform guidance covers native iOS and web clients, excellent launch quality, and growth in phases. Android-specific guidance, backend implementation, automatic publishing, and production-scale claims without measurements are outside this version's scope. Simplification remains an investigation/proposal workflow, not an audit after every edit.

See the [architecture](docs/architecture.md), [context map](docs/codebase.md), [evaluation fixtures](evals/README.md), and [source acknowledgments](THIRD_PARTY_NOTICES.md).
