# Interaction quality is acceptance behavior

Read the product journey and existing design system before designing screens. Maintain project-specific typography, spacing, semantic color, reusable components, navigation, feedback, and motion. Introduce a new component when its role warrants it; avoid imposing a branded template unrelated to the product.

Define the supported states of each critical journey: initial load, incremental work, empty results, recoverable and permanent errors, offline/stale content, permission denial, interruption, and successful recovery. Preserve useful work while showing errors. Retry should operate on the intended item/operation and avoid accidental duplicate submission.

Verify navigation and gestures: back/dismiss, cancellation, keyboard and focus, deep-link entry, destructive changes, long-running progress, and returning from Settings where relevant. Explain delayed work and provide appropriate cancellation/recovery. Do not claim progress beyond what the underlying operation actually knows.

## Inspect supported accessibility and layouts

- Dynamic Type: test large accessibility sizes for clipping, truncation, scroll reachability, and meaningful reflow; avoid fixed dimensions that hide primary actions.
- VoiceOver: labels, values, traits, order, grouping, focus after transitions, and accessible alternatives to custom gestures. Complete the critical journey using it.
- Color and contrast: convey state without color alone; inspect light/dark appearances and increased contrast where supported.
- Reduce Motion: preserve state feedback with reduced or replaced animation; avoid making essential information depend on movement.
- Localization: use the project's string resources and locale-aware formatting; exercise expansion, plurals, and right-to-left layout when supported. Do not confuse translated literals with a verified localized journey.
- Devices: test appropriate compact/large layouts, safe areas, keyboard, rotation, and iPad multitasking when those are supported product surfaces.

Use [Apple accessibility guidance](https://developer.apple.com/design/human-interface-guidelines/accessibility) when selecting platform interactions. Record the actual settings, device/simulator, route, and result. Automated accessibility audits and screenshots can find some defects; they do not substitute for completing the journey in the running application.

Screenshots are useful evidence for visual regressions and design discussion. Inspect the rendered app and exercise transitions as well as steady states. Record unavailable VoiceOver/device/visual checks explicitly instead of inferring success from accessible labels in source.
