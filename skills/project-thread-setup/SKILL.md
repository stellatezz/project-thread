---
name: project-thread-setup
description: Adopt Project Thread in a new or existing software repository by mapping authoritative docs, plans, Agent Notes, cookbooks, and checkpoints. Use for framework setup, not ordinary feature implementation.
---

# Set up Project Thread

Inspect instructions, repository status, manifests, entry points, documentation, and existing decisions. Use [record ownership](../project-thread/references/records.md) to map existing equivalents. Establish business context and distinguish confirmed facts from proposed architecture; do not select a runtime merely to fill a template.

## Introduce the smallest useful foundation

1. Identify existing owners for product, architecture, testing, decisions, and work tracking. Create a context map linking them and naming the real validation commands.
2. Preview missing files, preserved files, and path blockers. Do not overwrite existing instructions or records. A file or symlink blocking an intended directory must be resolved before creating the affected scaffold.
3. Within the authorized setup scope, create missing records and merge only necessary guidance into existing instructions. Empty lifecycle directories and speculative subsystem docs need not be created in advance.
4. Record the adoption decision using [Agent Notes](../project-thread-agent-notes/SKILL.md). If an existing framework already owns notes, reuse its lifecycle instead of creating a second tree.
5. Map known product areas or major initiatives to scoped roadmaps and a lightweight index using [roadmap guidance](../project-thread-roadmap/SKILL.md). Group new plans, issues, and phase files by roadmap where useful; link shared Agent Notes and existing issue-tracker/requirements owners. Establish the first useful vertical slice. Preserve existing boundaries; split an oversized roadmap without losing links or evidence. If the product outcome is unknown, record the missing decision rather than inventing roadmaps or empty areas.
6. Write a [checkpoint](../project-thread/references/checkpoints.md), validate relative links and discovered commands, and report the created and preserved paths.

Installation and adoption are separate: installing skills makes them available, while adoption adds project-specific records. The Project Thread bundle provides `scripts/install.py` at its repository root for user-level or repository-level installation; do not assume it is copied into an adopting app. A target project's own build and test tools remain authoritative.
