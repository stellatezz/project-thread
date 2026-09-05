# Codebase map

Use this map to find the rules, implementation, and verification for the plain text CLI. The repository uses Python and the standard library; it has no dependency manifest or build configuration.

## Read before changing the writer

Read [repository rules](../AGENTS.md), [writer rules](../writer/AGENTS.md), and [product behavior](product.md), then inspect [the CLI](../writer/main.py) and [its test](../tests/test_cli.py). Read [the checkpoint](checkpoints/current.md) when resuming work. Claude contributors also read [CLAUDE.md](../CLAUDE.md), which retains its unique handoff requirement and directs them to the shared rules. These are explicit reading paths; automatic loading depends on the host and remains unverified.

## Documentation owners

| Subject | Owner |
| --- | --- |
| Business behavior and scope | [Product reference](product.md) |
| Common rules and canonical test command | [Root instructions](../AGENTS.md) |
| Writer invariant | [Writer instructions](../writer/AGENTS.md) |
| Claude-specific handoff | [Claude entry](../CLAUDE.md) |
| Technical composition and test coverage | The sections below; source and tests establish implemented behavior |
| Adoption rationale | [Implemented process note](../.agents/notes/implemented/process/2026-09-05-agentic-adoption.md) |
| Current work state and evidence | [Checkpoint](checkpoints/current.md) |

There is no active feature plan, issue tracker, or product roadmap in this snapshot. The product reference explicitly records no planned feature change. The existing useful slice is creating a document while refusing to overwrite existing work. Adoption does not introduce a future feature sequence or new platform.

## How the CLI works

[`writer/main.py`](../writer/main.py) is the executable entry point. `argparse` requires an output path and content argument. `main()` opens the path in exclusive creation mode (`"x"`) with UTF-8 encoding and writes the content inside a context manager. It does not create parent directories. File errors propagate and produce a failed CLI process; there is no overwrite fallback. The [product reference](product.md) owns these user-facing constraints.

## Verify a writer change

From the repository root, run the command maintained in [AGENTS.md](../AGENTS.md):

```sh
python3 -m unittest discover -s tests -v
```

[`tests/test_cli.py`](../tests/test_cli.py) invokes the actual CLI in a temporary directory. It verifies that the first write succeeds, a second write to the same path returns nonzero, and the original text survives. No application package installation is required. The current test does not assert missing-parent behavior, UTF-8 content, or exact error text. Source inspection and a one-time manual check are separate evidence; see [the checkpoint](checkpoints/current.md) for what was run.

For a task that starts inside `writer/`, first read `../AGENTS.md`, `AGENTS.md`, and `../docs/product.md`; return to the repository root to run the canonical test command.
