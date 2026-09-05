# Refresh while loading a feed

Status: in-progress

The complete feature includes app integration. Only phase 1 is authorized and possible in this extracted fixture. The accepted scope comes from [TASK.md](../../TASK.md) and [CONTEXT.md](../../CONTEXT.md). Preserve UIKit, the injected main-actor store, iOS 16 compatibility, and Swift 6 language mode.

## Phase 1: extracted state owner

Status: complete (2026-09-05)

Acceptance and recorded evidence:

| Criterion | Deterministic evidence |
| --- | --- |
| Refresh supersedes page and refresh requests, independent of completion order | Twelve stale page/refresh cases: old success, failure, and cancellation, completing before or after fresh success |
| Stale cleanup cannot clear newer progress or set errors | Same race matrix plus an old error delivered while pagination of the new snapshot remains pending |
| Refresh retains content until success and has recovery | Pending snapshots; refresh failure and retry; failed refresh still invalidates old page |
| Cancellation leaves useful items/cursor and no alert | Page and refresh task cancellation with late success, failure, or cancellation; cancellation errors without a caller flag; URL cancellation; pre-cancelled actions |
| Page error leaves retry path using the same cursor | Failure snapshot and successful explicit retry; cancellation retry also checked |
| Stable IDs, overlaps, exhaustion, duplicate requests | Stable first-occurrence deduplication, one page while loading, initial no-op, nil exhaustion, empty pages, repeated non-nil cursor |
| Swift 6 concurrency checks and negative control | Fixed harness 29/29; original store 3/29, with 26 expected regression failures |
| iOS deployment compatibility at source level | Standalone store typechecked for arm64 iOS 16 using iPhoneOS 18.5 SDK; no app target compiled |
| Durable decision and handoff | [Decision](../../.agents/notes/implemented/behavior/2026-09-05-feed-request-ownership.md), [testing](../testing.md), [checkpoint](../checkpoints/current.md) |

Implementation choices and limitations are current facts in [CONTEXT.md](../../CONTEXT.md). No public action or API protocol is replaced. There is no added package, persistence, UI framework, automatic retry, or backend implementation.

## Phase 2: app integration

Status: pending; prerequisite is the actual app repository and its controller, networking, media, schemes, and test infrastructure. This deferral was specified by the task before work began; none of these checks count as phase 1 passes.

Next work, once the app artifacts and phase 2 authorization are available:

1. Inspect actual target settings, UIKit controller ownership, task cancellation on disappearance, rendering, and retry wiring. Apply the store change and port the controlled cases into the existing test target.
2. Verify refresh during an in-flight page through the controller: release refreshed response first, then old success/error. Assert rendered rows, visible progress, absence of stale alerts, and retry targeting. Repeat refresh failure/cancellation and overlapping IDs.
3. Build/test the discovered Xcode app scheme and run the journey on a discovered supported simulator. Check VoiceOver, loading/error announcements, Dynamic Type, and actual layouts.
4. Inspect and implement bounded media loading in its actual owner, then measure a named long-feed workload on physical hardware. Define budgets from product requirements and device baseline before making performance claims.

App compilation, live server behavior, transport cancellation completion, UI correctness, accessibility, simulator behavior, background/device lifecycle, media memory, scrolling, energy, and thermal performance remain unverified.
