#!/usr/bin/env python3
"""Dependency-free structural checks for the Project Thread bundle, not an app audit."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


SKILLS = {
    "project-thread", "project-thread-setup", "project-thread-roadmap",
    "project-thread-plan", "project-thread-phase", "project-thread-documentation",
    "project-thread-agent-notes", "project-thread-review", "project-thread-simplify",
    "project-thread-engineering", "project-thread-ios",
}


def scalar(text: str, key: str) -> str | None:
    """Read this bundle's single-line scalar convention, not arbitrary YAML."""
    match = re.search(rf"^\s*{re.escape(key)}: (.+)$", text, re.MULTILINE)
    return match.group(1).strip().strip('\"\'') if match else None


def without_code(text: str) -> str:
    text = re.sub(r"^```[^\n]*\n.*?^```\s*$", "", text, flags=re.MULTILINE | re.DOTALL)
    return re.sub(r"`[^`\n]+`", "", text)


def validate_bundle(root: Path) -> list[str]:
    root = root.resolve()
    errors = []
    skill_root = root / "skills"
    names = {p.name for p in skill_root.iterdir() if p.is_dir()} if skill_root.is_dir() else set()
    if names != SKILLS:
        errors.append(f"Skill inventory mismatch: missing={sorted(SKILLS - names)}, extra={sorted(names - SKILLS)}")
    for name in sorted(names):
        entry = skill_root / name / "SKILL.md"
        metadata = skill_root / name / "agents" / "openai.yaml"
        if not entry.is_file() or not metadata.is_file():
            errors.append(f"{name}: missing SKILL.md or agents/openai.yaml")
            continue
        text = entry.read_text()
        frontmatter = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
        if not frontmatter or scalar(frontmatter[1], "name") != name or not scalar(frontmatter[1], "description"):
            errors.append(f"{name}: invalid frontmatter")
        ui = metadata.read_text()
        if not scalar(ui, "display_name") or f"${name}" not in (scalar(ui, "default_prompt") or ""):
            errors.append(f"{name}: missing UI name or skill invocation")
        if not 25 <= len(scalar(ui, "short_description") or "") <= 64:
            errors.append(f"{name}: short_description must be 25-64 characters")

    try:
        manifest = json.loads((root / ".codex-plugin" / "plugin.json").read_text())
        if manifest.get("name") != "project-thread" or manifest.get("skills") != "./skills/":
            errors.append("Plugin name/skills path does not match bundle")
        if not re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.+-]+)?", manifest.get("version", "")):
            errors.append("Plugin version is missing or invalid")
    except (OSError, ValueError, TypeError, AttributeError) as error:
        errors.append(f"Invalid plugin manifest: {error}")

    for path in root.rglob("*.md"):
        relative = path.relative_to(root)
        if any(part in {".git", ".build", "__pycache__", "dist"} for part in relative.parts):
            continue
        text = path.read_text()
        if "[TODO:" in text:
            errors.append(f"{relative}: unfinished scaffold placeholder")
        # Check inline Markdown file links used by this bundle; skip external URLs and anchors.
        for href in re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", without_code(text)):
            parsed = urlsplit(href.strip("<>"))
            if parsed.scheme or not parsed.path:
                continue
            target = (path.parent / unquote(parsed.path)).resolve()
            if not target.is_relative_to(root) or not target.exists():
                errors.append(f"{relative}: broken or non-portable link: {href}")
        if relative.parts[:2] == (".agents", "notes") and len(relative.parts) >= 5:
            lifecycle = relative.parts[2]
            if lifecycle not in {"proposed", "implemented", "rejected", "archived"} or scalar(text, "Status") != lifecycle:
                errors.append(f"{relative}: lifecycle and Status disagree")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate_bundle(args.root)
    for error in errors:
        print(error)
    if not errors:
        print("project-thread: 11 skills, metadata, file links, and note statuses passed")
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
