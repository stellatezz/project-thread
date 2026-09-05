# Scope repository instructions deliberately

Use this reference during adoption or when existing agent instructions are missing, conflicting, or difficult to navigate. Instruction loading belongs to the coding agent's host. Inspect the actual agent, working directory, and configuration before claiming that a particular filename, symlink, import, or nested file loads automatically.

## Inspect existing instruction owners

Find root and relevant subtree instructions, including `AGENTS.md`, `CLAUDE.md`, and project-specific equivalents. Read them before editing. Resolve symlinks and imports deliberately so a shared target is not mistaken for an independent copy. Check for uncommitted user changes and preserve unrelated instructions.

Record the intended scope of each file and its relationship to the others. When rules conflict, identify their owners and resolve the concrete contradiction against current product requirements and user instructions. Do not silently delete a more specific rule or rely on an assumed universal precedence order across coding tools.

## Put rules where they apply

| Location | Appropriate content |
| --- | --- |
| Root instructions | Repository orientation, common development rules, real validation commands or their owner, links to specialized guidance |
| Product feature or subsystem | Additional local responsibilities, invariants, dependencies, generated-code boundaries, and relevant verification |
| Documentation tree | Documentation placement, prose standards, generation, and link maintenance |
| Agent Notes tree | Link to the canonical lifecycle and rules for active decisions |
| Existing archive tree | Historical status and preservation rules that apply to archived records |

Add a subtree file when it communicates a meaningful local rule or resolves repeated navigation mistakes. An ordinary folder does not automatically need one. Keep inherited guidance at its owner and link there when useful. Do not fill empty directories with speculative rules.

A repository may use a root map that explicitly asks an agent to read relevant subtree instructions before touching those paths. This provides a navigation path when nested discovery depends on the host. It still needs a real task exercise to establish that the path works.

## Share instructions across coding tools

Prefer one maintained source for rules shared by several tools. A supported import, a symlink, or a small tool-specific entry file can point to it. Choose the mechanism against the repository's operating systems, checkout/package behavior, and verified host support. Keep genuinely tool-specific settings separate.

Never replace an existing `CLAUDE.md` or `AGENTS.md` with a link without examining unique content and inbound consumers. A copied second rulebook needs a defined synchronization mechanism; otherwise its instructions can drift. A distribution archive must preserve the chosen link/import behavior or provide an equivalent portable entry file. Installing this skill bundle alone does not establish Claude compatibility in an adopting app.

## Keep instructions actionable

Rules should identify the relevant operation, constraint, and authoritative explanation. Use exact file and command names that exist in the repository. Put lengthy architecture, rationale, and procedures in their owners. Do not embed credentials, disposable local paths, or a transcript of the session that produced the instructions.

Prefer instructions such as “Before changing export persistence, read the project format reference and run its save/reopen checks” when those paths and checks exist. Avoid broad quality slogans that provide no way to decide or verify an action. Rules supplement the agent's judgment and remain subordinate to the user's authorized task and higher-priority instructions.

## Verify adoption

Inspect the resulting instruction tree for broken references, duplicate authority, and contradictory rules. Then start a fresh task or session in the intended host and working directory. Ask it to identify the applicable local rules and perform a small representative change or read-only exercise. Check which files it actually read and whether its actions follow the required rule and verification path.

A valid symlink proves filesystem resolution. It does not prove automatic instruction loading. Record file validity, host discovery, and behavioral evidence separately. If the target host is unavailable, retain a clear manual reading path and mark automatic discovery unverified.
