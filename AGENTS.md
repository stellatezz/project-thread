# Working on Project Thread

This is the standalone Project Thread skill/plugin repository, not an iOS application. Read [the context map](docs/project-thread.md) and relevant skill owners before changing behavior.

- Keep exactly the eleven public skills described in [README.md](README.md), with short entry points and conditional references.
- Shared record ownership lives in `skills/project-thread/references/records.md`; note lifecycle lives with `project-thread-agent-notes`. Reuse those owners rather than copying their rules.
- Every non-trivial change adds or updates an Agent Note. Keep proposed work separate from implemented facts, and update the active plan and checkpoint when work state changes.
- Use small Python standard-library helpers for objective packaging/installation checks. Target iOS repositories own their Xcode tooling and commands; this bundle does not scaffold a universal app architecture.
- Run `python3 scripts/check.py` and `python3 -m unittest discover -s tests -v` for bundle/helper changes. Validate changed skills and plugin metadata using the available Codex validators as described in [testing](docs/testing.md).
- Preserve intentionally faulty evaluation inputs. Run fixture tasks in isolated workspaces and record actual evidence without treating logic tests as simulator/device verification.
- Keep third-party attribution accurate. Do not edit sibling repositories or user configuration outside the requested installation scope.
