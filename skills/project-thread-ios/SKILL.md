---
name: project-thread-ios
description: Develop polished, reliable native iOS clients, adapting architecture and verifying interactions, concurrency, data, lifecycle, and device behavior. Use for iOS features and substantial fixes, including location, feeds, uploads, or media editing; backend implementation and publishing are separate scopes.
---

# Build a substantial iOS client in phases

Read [common engineering guidance](../project-thread-engineering/SKILL.md) and the project's current plan, business/technical facts, relevant decisions, and cookbooks. Reuse the framework's record ownership, note lifecycle, and checkpoint rules.

Inspect before choosing conventions: deployment target, Swift language mode and concurrency settings, Xcode requirements, targets/schemes, dependencies, navigation, state ownership, persistence, API contracts, and test infrastructure. Preserve an existing app's architecture unless evidence justifies a change. For a new app, default to Swift and SwiftUI, integrating UIKit where the interaction or platform capability calls for it. Establish one verified vertical slice before growing the product.

## Load guidance for the feature

| Current work | Read |
| --- | --- |
| New app, feature boundaries, state/navigation, concurrency | [Architecture and concurrency](references/architecture-and-concurrency.md) |
| Screens, navigation, design system, accessibility | [Interaction quality](references/interaction-quality.md) |
| Auth, networking, storage, interruptions, system integration | [Data and lifecycle](references/data-and-lifecycle.md) |
| Build/test discovery, measurements, release preparation | [Toolchain and verification](references/toolchain-and-verification.md) |
| Location, maps, live status or streams | [Location and real-time experiences](references/location-and-realtime.md) |
| Feed, pagination, media loading or uploads | [Feeds and uploads](references/feeds-and-uploads.md) |
| Persistent media projects, editing, playback, export | [Media creation and editing](references/media-editing.md) |

Load only relevant references. The reference products Uber, Instagram, and CapCut illustrate demanding client journeys; they impose no universal architecture or initial infrastructure footprint.

## Implement complete journeys

Make interaction quality part of acceptance: relevant loading, empty, error, offline, permission-denied, and recovery states. Use a project-specific design system and verify supported accessibility, localization, and device layouts. Inspect the running app; screenshots complement behavioral tests.

Use explicit concurrency isolation, structured task lifetimes, and cancellation. Recheck state assumptions across `await`; actor isolation does not make a multi-step asynchronous sequence atomic. Keep expensive work from blocking interaction under the target toolchain's execution rules.

Backend contracts are inputs. Name missing capabilities as dependencies or issues and label mocked behavior. V1 covers native iOS client engineering; Android, backend implementation, automatic deployment, and unmeasured production-scale claims are outside this skill's scope.

## Verify and hand off

Use the target project's Xcode tools and discovered commands. Build and exercise simulator journeys. Track physical-device evidence separately for hardware, background execution, energy, thermal behavior, and performance claims. Set budgets against named devices and workloads; do not invent targets.

When requested, prepare signing, configuration, archive validation, diagnostics, and release documentation. Publishing is a separately authorized action. Finish the accepted phase, update its evidence and owning records, and leave an honest checkpoint for the next session.
