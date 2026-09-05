# Interaction quality

Begin with the user's task, content hierarchy, and the existing design system. Define the success, pending, empty, invalid, unavailable, and recovery presentations alongside the happy path. Preserve entered data when a recoverable failure occurs. Use precise feedback that explains the next available action.

Prefer native links, buttons, inputs, and form semantics. Give fields associated labels and instructions; connect errors to affected controls and announce meaningful status changes without flooding assistive technology. Group related fields and make submission outcomes understandable. The [W3C forms tutorial](https://www.w3.org/WAI/tutorials/forms/) explains these relationships and notifications.

Design keyboard paths and visible focus. For dialogs, menus, and other custom widgets, use established accessible components or verify the relevant interaction pattern. Check entry focus, dismissal, focus return, and route-change focus as applicable. Pointer interaction alone is insufficient. Automated accessibility scans supplement keyboard and screen-reader journeys; they cannot establish complete accessibility.

Use content-driven responsive layouts across the supported device range. Check long text, localization and directionality when supported, zoom and text enlargement, contrast, reduced motion, touch targets, and overflow. Test mobile viewport and on-screen keyboard effects on critical forms. Avoid relying on hover, color, or motion as the sole indication of an action or state.

Inspect actual rendered screens at representative widths, with real content and failure states. Evaluate hierarchy, spacing, legibility, visual consistency, focus, and interaction feedback. Record the browser and viewport for screenshots. A screenshot proves neither keyboard behavior nor screen-reader announcements. For a new visual direction, use the available design workflow and keep the resulting decisions in the feature's acceptance criteria.
