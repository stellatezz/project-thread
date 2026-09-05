---
name: make-codebase-agentic-web
description: Develop reliable, accessible web clients using the project's framework, design system, and browser support requirements. Use for web features and substantial frontend fixes, including routing, forms, async state, rendering, and performance; backend implementation and publishing are separate scopes.
---

# Web client engineering

Apply [common engineering](../make-codebase-agentic-engineering/SKILL.md), the current feature plan, and relevant business rules, architecture, Agent Notes, and cookbooks. Reuse [record ownership](../make-codebase-agentic/references/records.md) and the existing note lifecycle. Keep web decisions and evidence in those records.

## Adapt to the project

Inspect instructions, manifests, lockfiles, runtime versions, scripts, routes, rendering mode, components, styles, data access, authentication contracts, and test infrastructure. Establish supported browsers, devices, input methods, and hosting constraints. Preserve established frameworks and conventions unless evidence justifies a planned change. For a new site or application, choose the smallest stack that supports its journeys, content delivery, and maintenance needs; do not assume a universal React, Next.js, or SPA architecture.

Define observable success through a real entry URL and complete user journey. Include relevant loading, empty, validation, error, offline, authorization, and recovery states. Resolve consequential changes to product behavior or public URLs in the plan; make routine implementation choices within the agreed scope.

## Load the needed guidance

| Work | Reference |
| --- | --- |
| Feature boundaries, routing, rendering, state | [Architecture and navigation](references/architecture-and-navigation.md) |
| Visual design, responsive layouts, forms, accessibility | [Interaction quality](references/interaction-quality.md) |
| Requests, session changes, storage, browser lifecycle | [Data and browser reliability](references/data-and-browser-reliability.md) |
| Tool discovery, browser journeys, performance evidence | [Verification and performance](references/verification-and-performance.md) |

Use applicable design or hosting workflows when available and relevant. Build coherent typography, spacing, color, components, feedback, and motion using the project's design system. Inspect the running interface; screenshots support visual review, while interaction checks establish behavior.

Backend contracts are inputs. Identify missing capabilities and mocked responses explicitly. Never place server secrets in browser code to bypass an unavailable endpoint. Server rendering and framework route boundaries belong to frontend integration; building backend services or publishing requires its own task scope and existing authorization.

## Verify and hand off

Use the target project's actual commands and available browser tools. Verify the critical journey, failure recovery, navigation, and supported accessibility behavior. Distinguish static checks, unit/integration tests, browser execution, physical-device checks, and production measurements. Record unavailable verification and its next executable step. Update affected facts, acceptance evidence, Agent Notes, learned cookbooks, and checkpoint before completing the phase.
