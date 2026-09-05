# Agent Note: engineering and iOS client suite

Status: implemented

The [readable repository guidance decision](2026-09-05-readable-agentic-codebase.md) refines the bundle identity and documentation standards. This foundation remains active for engineering, iOS, lifecycle, and evidence boundaries.

## Problem

Substantial iOS client work needs maintainable implementation discipline, complete interaction journeys, reliable data/lifetimes, and credible evidence across sessions. The implementation target initially contained only an unfinished daily-skill scaffold, although the supplied plan assumed a nine-skill foundation.

## Decision

Make Codebase Agentic contains eleven sibling skills. The foundation handles context, adoption, roadmap, planning, phases, documentation, notes, review, and simplification. Engineering owns design/implementation judgment; iOS applies it to platform-specific work using conditional references. Shared record ownership, lifecycle, and checkpoints retain a single authority. The [architecture](../../../../docs/architecture.md) describes the implemented boundaries.

The complete bundle installs as sibling symlinks at user or repository scope and also includes Codex plugin metadata. Small standard-library helpers check structure, preserve existing installations, and package an inspectable archive. iOS build/test commands come from the adopting project, not a framework-owned wrapper.

## Alternatives considered

Adding only two skills would leave their assumed companion dependencies absent. Completing the foundation satisfies the user's requested bundle. A monolithic iOS guide would load unrelated specialist guidance for every feature; conditional references keep each task focused. A universal architecture or state library would conflict with existing apps and different deployment floors. Mandatory simplification after edits would turn DeepSeek's investigation workflow into unrelated process overhead.

A custom app generator or Xcode automation layer would add maintenance and imply unsupported toolchain conventions. Direct symlink installation keeps all resources available and permits repeatable updates; copying isolated skills would break their sibling dependencies. Plugin marketplace registration is optional rather than a prerequisite for local skill availability.

## Consequences

The source checkout must stay at a stable location while linked installations are in use. All eleven skills travel together. Project authors still resolve their actual business contracts, architecture, data guarantees, budgets, and device matrix. Structural validation cannot prove good engineering judgment, and fixture logic checks cannot prove app/device or release readiness.

The note is the initial decision owner; no earlier active Make Codebase Agentic note existed to supersede. DeepSeek-derived principles are adapted without copying its project-specific tools or bilingual artifacts. See [source acknowledgments](../../../../THIRD_PARTY_NOTICES.md).

The subsequent [area-roadmap decision](2026-09-05-area-roadmaps.md) refines requirement and planning ownership while retaining this foundation.

## Verification

The [v1 result](../../../../evals/results/2026-09-05-v1.md) records successful structural checks, all eleven skill validators, plugin validation, 12 helper tests, user installation, and archive round-trip installation. Independent evaluation covers all ten scenario decisions, an executed Swift fixture (29 passing checks; 26 regressions exposed in the original), and a fresh-session recovery from repository records. The primary agent independently reproduced the Swift results and verified preserved source hashes. The [implementation plan](../../../../docs/plans/engineering-ios-v1.md) is complete. No iOS application/device certification is claimed.
