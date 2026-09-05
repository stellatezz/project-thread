# Agent Note: scope roadmaps to areas and initiatives

Status: implemented

## Problem

The initial record map defaulted to one `docs/roadmap.md`, leaving large projects' area boundaries and requirement ownership implicit. A detailed project-wide roadmap becomes difficult to maintain when several product areas have separate plans and shared dependencies. The user approved scoped roadmaps with a lightweight project index and asked to connect issues, separate phases, and Agent Notes.

## Decision

Each area or initiative has a folder under `docs/roadmaps/`, with an overview linking its plans, issues, phases, and relevant Agent Notes. The project index links these roadmaps and summarizes shared priorities and cross-area dependencies. Feature plans own detailed requirements and acceptance criteria or link an established requirements authority; shared business rules stay in product documentation. Every plan and issue has one primary roadmap owner. Consumers reference shared capabilities and verify their own journeys.

The default groups delivery records and keeps Agent Notes in their shared lifecycle tree, so decisions spanning several roadmaps retain one owner. Issues track concrete work and resolution; phases own bounded delivery criteria and evidence; notes preserve consequential rationale. Cross-links give one navigation path without merging these different lifecycles. Established repository layouts remain supported.

The daily, setup, planning, phase, note, and checkpoint guidance carries that ownership. [Record ownership](../../../../skills/project-thread/references/records.md) defines the shared structure, [delivery-record guidance](../../../../skills/project-thread/references/delivery-records.md) connects records and lifecycles, and [roadmap guidance](../../../../skills/project-thread-roadmap/SKILL.md) owns organization and sequencing. The suite remains eleven skills.

This repository preserves `docs/roadmap.md` as its index and moves its existing outcomes into skill-suite and iOS-adoption roadmaps. Existing v1 evidence and candidate scope are retained. The [suite foundation decision](2026-09-05-engineering-ios-suite.md) remains active: this refines planning ownership without superseding its engineering, lifecycle, installation, or evidence rules.

## Alternatives considered

A single detailed roadmap would retain the ambiguity the user identified. A roadmap per feature would duplicate the role of feature plans. Separate mandatory requirements documents for every feature would add competing owners where the plan can already carry the requirements. Copying a shared Agent Note into each roadmap would split decision authority; placing all issues, criteria, and rationale in one document would conflate their distinct statuses. Requiring all adopting projects to rename existing indexes or move useful plans would break links without improving ownership.

## Consequences

Areas can sequence work independently while exposing shared dependencies. Cross-area capabilities have one owner, and finishing a prerequisite does not certify its consumers. The index needs maintenance when shared priorities or dependency readiness changes, but detailed criteria and execution state stay with their owners. Areas and separate issue/phase files are introduced for useful work rather than speculative completeness. Existing issue trackers and short phases inside plans remain valid owners.

## Verification

The [follow-up plan](../../../../docs/roadmaps/skill-suite/plans/area-roadmaps.md) is complete and its [issue](../../../../docs/roadmaps/skill-suite/issues/roadmap-record-ownership.md) is resolved. The [phase](../../../../docs/roadmaps/skill-suite/phases/area-roadmaps/01-integrate-records.md) owns detailed evidence: structural/link checks, all six changed skill validators, plugin validation, 12 helper tests, semantic ownership review, archive extraction/install, and user-link verification passed. No app runtime or historical evaluation fixture has changed.
