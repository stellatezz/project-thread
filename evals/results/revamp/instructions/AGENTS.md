# Repository rules

This is a Python CLI that writes plain text documents. Read `docs/product.md` before changing behavior. Use `python3 -m unittest discover -s tests -v` from the root. Changes under `writer/` also follow `writer/AGENTS.md`. Do not change output paths or overwrite behavior without a feature plan.

Start with the [codebase map](docs/codebase.md) for documentation owners and the [current checkpoint](docs/checkpoints/current.md) to resume work. Before touching `writer/`, explicitly read [its local rules](writer/AGENTS.md); do not rely on a host discovering nested instructions automatically. Keep shared repository rules here and writer-specific rules in their existing owner. Preserve the separate Claude handoff requirement in [CLAUDE.md](CLAUDE.md).
