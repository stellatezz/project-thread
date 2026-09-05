---
name: make-codebase-agentic-setup
description: Adopt Make Codebase Agentic in a new or existing software repository by mapping authoritative docs, plans, Agent Notes, cookbooks, and checkpoints. Use for framework setup, not ordinary feature implementation.
---

# Set up Make Codebase Agentic

Inspect instructions, repository status, manifests, entry points, documentation, and existing decisions. Use [record ownership](../make-codebase-agentic/references/records.md) to map existing equivalents. Establish business context and distinguish confirmed facts from proposed architecture; do not select a runtime merely to fill a template. Use [instruction hierarchy](../make-codebase-agentic-documentation/references/instruction-hierarchy.md) when mapping root, subtree, or agent-specific rules, and [document structure](../make-codebase-agentic-documentation/references/document-structure.md) when existing knowledge lacks a clear owner or reading path.

## Introduce the smallest useful foundation

1. Identify existing owners for product, architecture, testing, decisions, and work tracking. Create a context map linking them and naming the real validation commands.
2. Preview missing files, preserved files, and path blockers. Do not overwrite existing instructions or records. A file or symlink blocking an intended directory must be resolved before creating the affected scaffold.
3. Within the authorized setup scope, create missing records and merge only necessary guidance into existing instructions. Empty lifecycle directories and speculative subsystem docs need not be created in advance.
4. Record the adoption decision using [Agent Notes](../make-codebase-agentic-agent-notes/SKILL.md). If an existing framework already owns notes, reuse its lifecycle instead of creating a second tree.
5. Map known product areas or major initiatives to scoped roadmaps and a lightweight index using [roadmap guidance](../make-codebase-agentic-roadmap/SKILL.md). Group new plans, issues, and phase files by roadmap where useful; link shared Agent Notes and existing issue-tracker/requirements owners. Establish the first useful vertical slice. Preserve existing boundaries; split an oversized roadmap without losing links or evidence. If the product outcome is unknown, record the missing decision rather than inventing roadmaps or empty areas.
6. Write a [checkpoint](../make-codebase-agentic/references/checkpoints.md), validate relative links and discovered commands, and report the created and preserved paths. Exercise a representative reading/task path from the intended working directory: locate the component's rules, its current behavior, and its verification. Record instruction-file validity separately from actual host discovery and task evidence; unavailable host checks remain explicit.

Installation and adoption are separate: installing skills makes them available, while adoption adds project-specific records. The Make Codebase Agentic bundle provides `scripts/install.py` at its repository root for user-level or repository-level installation; do not assume it is copied into an adopting app. A target project's own build and test tools remain authoritative.
