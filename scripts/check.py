#!/usr/bin/env python3
"""Dependency-free structural checks for the Make Codebase Agentic bundle, not an app audit."""

from __future__ import annotations

import argparse
from datetime import date
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


SKILLS = {
    "make-codebase-agentic", "make-codebase-agentic-setup", "make-codebase-agentic-roadmap",
    "make-codebase-agentic-plan", "make-codebase-agentic-phase", "make-codebase-agentic-documentation",
    "make-codebase-agentic-agent-notes", "make-codebase-agentic-review", "make-codebase-agentic-simplify",
    "make-codebase-agentic-engineering", "make-codebase-agentic-ios",
}


def scalar(text: str, key: str) -> str | None:
    """Read this bundle's single-line scalar convention, not arbitrary YAML."""
    match = re.search(rf"^\s*{re.escape(key)}: (.+)$", text, re.MULTILINE)
    return match.group(1).strip().strip('\"\'') if match else None


def without_code(text: str) -> str:
    text = re.sub(r"^```[^\n]*\n.*?^```\s*$", "", text, flags=re.MULTILINE | re.DOTALL)
    return re.sub(r"`[^`\n]+`", "", text)


def record_category(path: Path) -> str | None:
    """Recognize this bundle's record owners; retained evals are out of scope."""
    parts = path.parts
    if parts[:2] == (".agents", "notes") and len(parts) >= 5:
        return "note"
    if path.as_posix() in {"docs/roadmap.md", "docs/roadmaps/README.md"}:
        return "index"
    if parts[:2] == ("docs", "checkpoints"):
        return "checkpoint"
    if parts[:2] == ("docs", "plans"):
        return "delivery"
    if parts[:2] == ("docs", "roadmaps"):
        local = parts[2:]
        if local and local[0] == "archived":
            local = local[1:]
        if len(local) == 2 and local[1] == "README.md":
            return "roadmap"
        if len(local) >= 3 and local[1] in {"plans", "phases", "issues"}:
            return "delivery"
    return None


def validate_record(path: Path, text: str) -> tuple[list[str], bool]:
    category = record_category(path)
    if category is None:
        return [], False
    errors = []
    header = re.split(r"^##\s", without_code(text), maxsplit=1, flags=re.MULTILINE)[0]

    def field(key: str) -> str | None:
        values = re.findall(rf"^{re.escape(key)}:[ \t]*(.*)$", header, re.MULTILINE)
        if len(values) > 1:
            errors.append(f"{path}: duplicate {key} metadata")
        return values[0].strip() if values else None

    def calendar(value: str | None, key: str) -> date | None:
        try:
            if value is None or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
                raise ValueError
            return date.fromisoformat(value)
        except ValueError:
            errors.append(f"{path}: {key} must be a valid YYYY-MM-DD date")
            return None

    created = updated = None
    archived_value = field("Archived")
    archived = (category == "note" and path.parts[2] == "archived") or (
        category == "roadmap" and (path.parts[2] == "archived" or archived_value is not None))
    if category == "note":
        match = re.fullmatch(r"(\d{4}-\d{2}-\d{2})-.+\.md", path.name)
        created = calendar(match[1] if match else None, "filename date")
        if path.parts[2] not in {"proposed", "implemented", "rejected", "archived"} or field("Status") != path.parts[2]:
            errors.append(f"{path}: lifecycle and Status disagree")
        if archived_value is not None and not archived:
            errors.append(f"{path}: Archived metadata requires the archived note lifecycle")
    else:
        updated = calendar(field("Updated"), "Updated")
        if category != "checkpoint":
            value = field("Created")
            if value == "unknown":
                if not field("Date provenance"):
                    errors.append(f"{path}: unknown Created requires Date provenance")
            else:
                created = calendar(value, "Created")
            if created and updated and updated < created:
                errors.append(f"{path}: Updated precedes Created")
    if category == "roadmap":
        status = field("Status")
        if field("Kind") not in {"area", "initiative"}:
            errors.append(f"{path}: roadmap Kind must be area or initiative")
        if status not in {"draft", "active", "paused", "completed", "retired"}:
            errors.append(f"{path}: invalid roadmap Status")
        required = {"paused": ("Pause reason", "Resume when"),
                    "completed": ("Completion evidence",), "retired": ("Retirement reason",)}
        for key in required.get(status, ()):
            if not field(key):
                errors.append(f"{path}: {status} roadmap requires {key}")
        if archived:
            if status not in {"completed", "retired"}:
                errors.append(f"{path}: only completed or retired roadmaps may be archived")
            if not field("Archive reason"):
                errors.append(f"{path}: archived roadmap requires Archive reason")
    if archived:
        sealed = calendar(archived_value, "Archived")
        previous = updated or created
        if sealed and previous and sealed < previous:
            errors.append(f"{path}: Archived precedes the last known record date")
    return errors, archived


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
        if manifest.get("name") != "make-codebase-agentic" or manifest.get("skills") != "./skills/":
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
        record_errors, archived = validate_record(relative, text)
        errors.extend(record_errors)
        if archived:
            # Frozen sources may retain historical outbound links and wording.
            continue
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
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate_bundle(args.root)
    for error in errors:
        print(error)
    if not errors:
        print("make-codebase-agentic: 11 skills, metadata, file links, record dates, and lifecycle fields passed")
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
