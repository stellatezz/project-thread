# Upgrade from Project Thread

Make Codebase Agentic 0.2.0 renames the Project Thread bundle and expands its documentation and codebase guidance. The GitHub repository is [stellatezz/make-codebase-agentic](https://github.com/stellatezz/make-codebase-agentic). The eleven skill names use `make-codebase-agentic` in place of `project-thread`; for example, `$project-thread-ios` becomes `$make-codebase-agentic-ios`.

## Migrate a linked installation

Keep or move the checkout to a stable location, update its source, and run the installer there. Supply the previous checkout path even if that directory has already moved and its old skill links are broken:

```sh
python3 scripts/install.py --user --migrate-from /previous/path/project-thread --dry-run
python3 scripts/install.py --user --migrate-from /previous/path/project-thread
```

For an installation scoped to an app repository, replace `--user` with `--repo /path/to/app`. If only the source changed and the checkout stayed at the same path, pass that path to `--migrate-from`.

The installer validates the new bundle and preflights every new destination. It creates the complete new set before removing old `project-thread*` symlinks that point to the supplied checkout's old skill paths. It preserves other sources and regular files. A creation failure rolls back links created by that attempt and leaves old links intact. An operating-system failure during legacy cleanup leaves the new installation usable; repeating the command completes remaining cleanup. This migration cannot be combined with `--remove`.

Review any preserved legacy entries before removing them manually. They may contain user-owned content. The helper does not search for other installations, rewrite application records, or edit marketplace settings. If a separate plugin marketplace owns an installation, update it using that marketplace's supported workflow; this source checkout uses direct skill links.

Start a new Codex thread and invoke `$make-codebase-agentic` or the relevant specialized skill. Update current project instructions that explicitly name old invocations. Existing project documents such as `docs/project-thread.md` remain valid context owners; rename them only when doing so improves that project's navigation and repair their incoming links.

## Historical evidence

The retained v1 evaluations under `evals/results/` preserve their original names, task text, paths, hashes, and logs. They describe the earlier run. Current source and guides use the new identity; the license retains the original contributor attribution. Historical evidence is not rewritten to suggest that the renamed skills were tested before they existed.
