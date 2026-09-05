# Working on Make Codebase Agentic

This is the standalone Make Codebase Agentic skill/plugin repository, not an application. Read [the context map](docs/codebase.md) and relevant skill owners before changing behavior.

Read [skill instructions](skills/AGENTS.md) before changing skills, [documentation instructions](docs/AGENTS.md) before changing docs, and [note instructions](.agents/notes/AGENTS.md) before changing decisions. These files add local guidance and link its canonical owner.

- Keep exactly the twelve public skills described in [README.md](README.md), with short entry points and conditional references.
- Shared record ownership lives in `skills/make-codebase-agentic/references/records.md`; note lifecycle lives with `make-codebase-agentic-agent-notes`. Reuse those owners rather than copying their rules.
- Every non-trivial change adds or updates an Agent Note. Keep proposed work separate from implemented facts, and update the active plan and checkpoint when work state changes.
- Use small Python standard-library helpers for objective packaging/installation checks. Target application repositories own their Xcode or web tooling and commands; this bundle does not scaffold a universal app architecture.
- Run `python3 scripts/check.py` and `python3 -m unittest discover -s tests -v` for bundle/helper changes. Validate changed skills and plugin metadata using the available Codex validators as described in [testing](docs/testing.md).
- Preserve intentionally faulty evaluation inputs. Run fixture tasks in isolated workspaces and record actual evidence without treating logic tests as simulator/device verification.
- Keep third-party attribution accurate. Do not edit sibling repositories or user configuration outside the requested installation scope.
