#!/usr/bin/env python3
"""Write a reproducible ZIP of the complete distributable bundle."""

from pathlib import Path
import json
import os
import tempfile
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from check import validate_bundle

ROOT = Path(__file__).resolve().parents[1]
ROOTS = ("skills", "scripts", "tests", "evals", "docs", ".codex-plugin", ".agents/notes", ".github")
FILES = ("README.md", "AGENTS.md", "LICENSE", "THIRD_PARTY_NOTICES.md", ".gitignore")


def package(root: Path) -> Path:
    errors = validate_bundle(root)
    if errors:
        raise ValueError("Invalid bundle:\n" + "\n".join(errors))
    version = json.loads((root / ".codex-plugin/plugin.json").read_text())["version"]
    if any(char not in "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.+-" for char in version):
        raise ValueError("Unsafe archive version")
    paths = [root / name for name in FILES]
    for name in ROOTS:
        paths.extend(path for path in (root / name).rglob("*")
                     if path.is_file() and not any(part in {"__pycache__", ".build"} for part in path.parts)
                     and path.suffix != ".pyc")
    output = root / "dist" / f"make-codebase-agentic-{version}.zip"
    output.parent.mkdir(exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=output.parent, delete=False) as handle:
        temporary = Path(handle.name)
    try:
        with ZipFile(temporary, "w", compression=ZIP_DEFLATED) as archive:
            for path in sorted(paths):
                if path.is_symlink():
                    raise ValueError(f"Distribution source must be a regular file: {path}")
                entry = ZipInfo("make-codebase-agentic/" + path.relative_to(root).as_posix(), (2026, 1, 1, 0, 0, 0))
                entry.compress_type = ZIP_DEFLATED
                entry.create_system = 3
                entry.external_attr = 0o100644 << 16
                archive.writestr(entry, path.read_bytes())
        os.replace(temporary, output)
    finally:
        temporary.unlink(missing_ok=True)
    return output


if __name__ == "__main__":
    print(package(ROOT))
