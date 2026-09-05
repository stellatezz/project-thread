# Current checkpoint

Date: 2026-09-05

## Objective and scope

Adopt useful Make Codebase Agentic documentation and instruction structure while preserving established decisions and unique instructions. Application behavior is unchanged. No external writes, Git operations, new product roadmap, or runtime installation are authorized by this exercise. There is no active area roadmap, feature plan, phase, or issue owner; the [product reference](../product.md) records no planned feature change.

## Repository state

The snapshot has no `.git` metadata, so branch, revision, and pre-existing uncommitted changes cannot be established. No Git command was run. Original application, test, product, task, local writer instructions, and Claude instructions are preserved byte for byte. The root instruction's original content remains intact, with an appended navigation paragraph.

Created records are the [codebase map](../codebase.md), [adoption note](../../.agents/notes/implemented/process/2026-09-05-agentic-adoption.md), this checkpoint, and [EVALUATION.md](../../EVALUATION.md). There are no behavior changes or pending feature implementation steps. Preserve these records and all existing rules on continuation.

## Evidence and limitations

The canonical command is `python3 -m unittest discover -s tests -v` from the root. Its baseline run and post-adoption run each passed one test with exit 0 on Python 3.14.4 on 2026-09-05. The latter used `TMPDIR="$PWD"` to confine test fixtures to the workspace. A separate CLI exercise passed UTF-8 creation, duplicate-output rejection with original bytes preserved, and missing-parent rejection. All 41 local Markdown links resolved, preserved files matched their baseline hashes, and the original root instruction text remained intact. See [EVALUATION.md](../../EVALUATION.md) for exact commands, the baseline temporary-fixture caveat, and the manual reading exercise through root rules, writer rules, product behavior, source, and verification.

The current Codex task reads files explicitly; it does not prove automatic discovery in a fresh Codex session. Claude runtime discovery and task behavior are unverified because no Claude runtime is available. No symlink/import loading claim is made. The [adoption note](../../.agents/notes/implemented/process/2026-09-05-agentic-adoption.md) explains the portable reading path and why unique instructions remain separate.

## Next executable action

For the next code task, start with [the codebase map](../codebase.md), compare its claims with the current tree, and read the applicable local instructions before editing. An output-path or overwrite change first requires an agreed feature plan under the existing rules.

To close the host-discovery evidence gap when a fresh host session is available, launch it at the repository root and give a read-only task: identify the writer's no-overwrite rule, trace successful creation and duplicate-output failure, then run the root test command. Record which instruction files the host actually loads versus reads manually, the exact command and exit result, and whether the original content survives. Repeat in Claude when available, checking its unique handoff rule. Host verification is a remaining evidence gap, not an approved product feature or a claimed pass.
