# Sample editor storage

[`project_store.py`](project_store.py) saves one project as a UTF-8 JSON file and
loads it again. Both functions run synchronously and use only the Python standard
library. Use Python 3.9 or newer and a `pathlib.Path` whose parent directory exists.

`save_project` encodes the project before writing a temporary file, then replaces
the destination after flushing and syncing the temporary file. A failure before
replacement leaves the existing project file untouched. Exceptions reach the
caller; the caller must decide how to report a failed save and retain unsaved work.
This sample has no render/export code or automatic recovery scan.

## Save and reopen a project

Run this command from the directory containing `project_store.py`. It creates an
isolated temporary directory, saves a small project, checks the loaded value, and
removes the directory when finished:

```sh
python3 - <<'PY'
from pathlib import Path
from tempfile import TemporaryDirectory
from project_store import load_project, save_project

with TemporaryDirectory(dir=".") as directory:
    path = Path(directory) / "project.json"
    project = {"title": "First cut", "clips": []}
    save_project(path, project)
    assert load_project(path) == project
    print("Saved and reopened First cut")
PY
```

For a persistent project, choose a lasting location and create its parent directory
before saving. The storage functions do not create directories. Prefer dictionaries
with string keys and JSON values; arbitrary Python objects cannot be serialized.

## Find the behavior you need

The [storage reference](docs/storage.md) owns the API contracts, save ordering,
failure consequences, and integration limits. Start there before changing storage
or connecting it to an editor. The
[documentation decision](.agents/notes/implemented/process/2026-09-05-storage-documentation.md)
preserves the documentation layout choice and the original file-storage rationale.

Run the example above as a basic save/reopen check after documentation changes.
The [evaluation record](EVALUATION.md) lists the additional checks actually run for
this revision and their limits.
