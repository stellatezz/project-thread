#!/usr/bin/env python3
"""Install the whole skill bundle as links, preserving all unrelated files."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

from check import validate_bundle


BUNDLE = Path(__file__).resolve().parents[1]


def install(bundle: Path, base: Path, *, dry_run: bool = False, remove: bool = False) -> list[str]:
    """Preflight every link before writing; removal only touches this bundle's links."""
    errors = validate_bundle(bundle)
    if errors:
        raise ValueError("Invalid source bundle:\n" + "\n".join(errors))
    base = base.expanduser().resolve()
    if not base.is_dir():
        raise ValueError(f"Installation base must be an existing directory: {base}")
    target = base / ".agents" / "skills"
    for parent in (base / ".agents", target):
        if parent.is_symlink() or (parent.exists() and not parent.is_dir()):
            raise ValueError(f"Blocked parent path: {parent}")

    actions = []
    blockers = []
    for source in sorted((bundle / "skills").iterdir()):
        if not source.is_dir():
            continue
        source = source.resolve()
        destination = target / source.name
        owned = destination.is_symlink() and destination.resolve() == source
        if remove:
            action = "remove" if owned else "preserve"
        elif owned:
            action = "preserve"
        elif destination.exists() or destination.is_symlink():
            blockers.append(str(destination))
            continue
        else:
            action = "create"
        actions.append((action, source, destination))
    if blockers:
        raise ValueError("Conflicting skills; no files changed:\n" + "\n".join(blockers))

    report = [f"{action}: {destination}" for action, _, destination in actions]
    if dry_run:
        return report
    created = []
    try:
        for action, source, destination in actions:
            if action == "create":
                target.mkdir(parents=True, exist_ok=True)
                destination.symlink_to(source, target_is_directory=True)
                created.append(destination)
            elif action == "remove":
                destination.unlink()
    except OSError:
        # Roll back only links this attempt created; leave concurrent changes alone.
        for destination in reversed(created):
            source = bundle / "skills" / destination.name
            if destination.is_symlink() and destination.resolve() == source.resolve():
                destination.unlink()
        raise
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    scope = parser.add_mutually_exclusive_group(required=True)
    scope.add_argument("--user", action="store_true", help="Install in ~/.agents/skills")
    scope.add_argument("--repo", type=Path, help="Install in REPO/.agents/skills")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--remove", action="store_true", help="Remove only links to this checkout")
    args = parser.parse_args()
    try:
        for line in install(BUNDLE, Path.home() if args.user else args.repo,
                            dry_run=args.dry_run, remove=args.remove):
            print(line)
    except (ValueError, OSError) as error:
        print(f"project-thread: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
