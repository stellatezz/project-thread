"""Storage functions for the sample editor."""

import json
import os
from pathlib import Path
import tempfile


def save_project(path: Path, project: dict) -> None:
    payload = json.dumps(project).encode("utf-8")
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as handle:
        temporary = Path(handle.name)
        try:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        except OSError:
            temporary.unlink(missing_ok=True)
            raise
    try:
        os.replace(temporary, path)
    except OSError:
        temporary.unlink(missing_ok=True)
        raise


def load_project(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))
