# Preserve instruction owners during agentic adoption

Status: implemented

## Problem

The repository already defines product behavior, root rules, local writer rules, and a unique Claude handoff rule, but lacks a context map and resumable work record. Adoption must improve navigation without changing application behavior or replacing those owners.

## Decision

The [root instructions](../../../../AGENTS.md) retain their original content and add links to the [context map](../../../../docs/codebase.md), [checkpoint](../../../../docs/checkpoints/current.md), and existing instruction owners. The map contains the small technical and testing reference because separate architecture and testing pages would add navigation without useful depth. [Product behavior](../../../../docs/product.md), [writer rules](../../../../writer/AGENTS.md), and [CLAUDE.md](../../../../CLAUDE.md) remain unchanged.

Claude's existing text entry directs readers to shared rules and retains its unique exact-command-and-exit-result handoff requirement. No symlink, copied second rulebook, or host-specific import is introduced. Readers explicitly follow the local instruction path instead of assuming automatic nested discovery.

No prior notes or decision lifecycle exist in this snapshot, so this is the first implemented process note in the shared lifecycle tree. No decision is superseded. No roadmap, feature plan, phase, or issue owner applies: the product has no planned feature change, and this task authorizes documentation adoption only.

## Alternatives and consequences

Leaving the repository unchanged would preserve its rules but leave continuation and technical orientation implicit. Replacing `CLAUDE.md` with a link would discard its unique rule. Copying shared rules into both entry files would create a synchronization burden. A full scaffold would create empty delivery records for work that has not been requested.

The compact map requires manual maintenance when source or verification changes. The plain text Claude entry is portable as a file, but no Claude runtime is available to establish its automatic loading or behavior. Revisit the sharing mechanism if a real host exercise demonstrates a navigation failure, and split reference pages only when their subjects need independent depth.

## Verification

On 2026-09-05, the root unittest command passed on Python 3.14.4 before adoption. [The evaluation record](../../../../EVALUATION.md) owns executed structural checks, preservation checks, and the post-adoption reading and CLI exercise. Those checks distinguish file validity, manually followed instructions, and unavailable automatic host discovery; they do not establish Claude runtime compatibility. [The checkpoint](../../../../docs/checkpoints/current.md) records the handoff and remaining evidence limits.
