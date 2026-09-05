# Validation

Run from the Make Codebase Agentic root with Python 3.9+:

```sh
python3 scripts/check.py
python3 -m unittest discover -s tests -v
python3 scripts/package.py
git diff --check
```

The 16 helper tests exercise complete installation and repeat installation, dry-run behavior, collision preflight, parent blockers, broken links, rollback after a create failure, ownership-limited removal, invalid bundle/reference/lifecycle negative controls, and archive round-trip discovery. Legacy migration checks cover broken old links, preserved other sources, conflict preflight, create rollback, cleanup retry, and incompatible CLI options. These tests do not evaluate engineering judgment by matching phrases in skill prose.

When Codex's skill-creator and plugin-creator are available, run their validators too. Resolve their paths from the current skill catalog; for a standard installation:

```sh
for entry in skills/*/SKILL.md; do
  python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" "${entry%/SKILL.md}" || exit 1
done
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/plugin-creator/scripts/validate_plugin.py" .
```

These external validators may have their own Python dependencies (the current skill validator uses PyYAML). They are authoring checks, not bundled runtime dependencies. Keep the bundle's standard-library check usable independently.

## Behavioral evaluation

Use [the fixture procedure](../evals/README.md) and [rubric](../evals/rubric.md). Ten scenario tasks exercise architecture preservation, new-app scope, feed races, upload recovery, location, editing, concurrency, accessibility, continuity, and evidence classification. The extracted Swift feed exercise additionally supports executed regression evidence.

Record evaluator input, references loaded, output artifacts, commands/results, and limits. Review actual artifacts, and where useful run regression checks against the original faulty fixture. Preserve failed checks and follow-up corrections. A fixture exercise cannot certify an absent iOS application, backend, simulator journey, physical device, or release.

The [revamp result](../evals/results/2026-09-05-revamp.md) records the documentation and instruction exercises, with retained outputs and replayable storage checks. The [v1 result](../evals/results/2026-09-05-v1.md) retains the earlier engineering/iOS fixture evidence. Required app/device verification remains the responsibility of each adopting project's acceptance criteria.
