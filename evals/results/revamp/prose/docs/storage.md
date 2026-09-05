# Project storage behavior

This reference describes [`project_store.py`](../project_store.py). The
[README](../README.md) provides prerequisites and a runnable save/reopen example.
The module owns JSON file I/O. The caller owns the in-memory project, destination
directory, save scheduling, and any user-facing error reporting.

## `save_project(path: Path, project: dict) -> None`

Pass a `pathlib.Path` with an existing, writable parent directory. A successful
call returns `None` after `os.replace` replaces the destination with the temporary
file. If no destination exists, replacement creates it. An existing destination
is replaced without merging or keeping a backup.

The `dict` annotation is not runtime validation. The function passes the value to
`json.dumps` with its defaults. Use a dictionary with string keys and values that
JSON can represent when the application expects a project object. Unsupported
values, such as a set or a custom object, raise `TypeError`; circular containers
raise `ValueError`. Tuples reload as lists, and supported non-string dictionary
keys reload as strings. Default JSON encoding also allows non-finite floats such
as `NaN`, so this module does not enforce strict JSON or a project schema.

The function does not mutate the supplied project. It does not lock it either;
callers must prevent concurrent mutation during serialization and serialize saves
to the same path if save order matters.

## Save ordering and saved work

The save sequence is:

1. Encode the complete project with `json.dumps`, then encode that text as UTF-8.
2. Create a temporary file in `path.parent`.
3. Write the payload, flush Python's buffer, and call `os.fsync` on the temporary
   file descriptor.
4. Close the temporary file and call `os.replace(temporary, path)`.

Encoding happens before creating a temporary file or touching the destination.
Keeping the temporary file beside the destination avoids a cross-filesystem move
during replacement. The old destination remains in place until replacement;
the module never streams new bytes directly into the old project file.

Syncing the temporary file and replacing the destination are separate operations.
The module does not sync the parent directory, retain a backup, or scan for orphaned
temporary files. It therefore makes no guarantee of recovering the latest save
after sudden power loss or a process crash. The replacement behavior also depends
on the operating system and filesystem. The checks in this revision did not test
those crash scenarios.

## What happens when saving fails

Errors propagate to the caller. The module does not retry, return an error status,
or change the caller's in-memory project.

| Failure point | Effect on the saved project | Temporary-file handling |
| --- | --- | --- |
| JSON serialization | Existing destination is untouched. | No temporary file has been created. |
| Creating the temporary file, including a missing parent directory | Existing destination is untouched. | The write and replacement stages do not run. |
| `OSError` from writing, flushing, or syncing | Existing destination is untouched; replacement is not attempted. | The handler attempts to unlink the temporary file before re-raising. |
| Closing the temporary file | Replacement is not attempted if closing raises. | There is no dedicated cleanup handler for this step. |
| `OSError` from `os.replace` | The call reports a failed replacement; it cannot be treated as a completed save. | The handler attempts to unlink the temporary file before re-raising. |

Cleanup can itself fail. If `unlink` raises, that exception becomes the exception
observed by the caller, with the earlier error in its exception context. The
write/flush/sync cleanup attempt happens while the file is still open, which can
matter on platforms that restrict deleting open files. Errors other than
`OSError` in the guarded sections have no explicit cleanup path. Abrupt process
termination can also leave a temporary file behind.

The caller should mark a save complete only after `save_project` returns normally.
When a save fails before replacement, the old file still contains the previous
saved state; newer edits remain the caller's responsibility. If an integration
needs export to use a particular saved revision, it must establish that ordering
and revision identity itself.

## `load_project(path: Path) -> dict`

Loading reads the file as UTF-8 text and returns `json.loads`' decoded value. It
does not create files, repair content, migrate formats, or validate project fields.
Despite the annotation, a file containing a JSON array or scalar returns a list
or scalar. A caller requiring a dictionary must validate the result.

File I/O errors such as `FileNotFoundError` propagate. Invalid UTF-8 raises
`UnicodeDecodeError`, and malformed JSON raises `json.JSONDecodeError`. The load
function does not fall back to temporary files or an earlier revision.

## Editor integration and limits

The original project documentation describes an editor that saves synchronously
and a UI layer that serializes saves for each project. No editor or UI caller is
included in this sample, so those are integration assumptions to preserve and
verify when connecting a consumer. The module itself provides no locking,
queuing, cancellation, or protection against one writer overwriting another.

There is no render/export implementation here, so matching exported videos to
saved projects cannot be verified or guaranteed by this module. For why the
prototype used files, see the
[recorded rationale](../.agents/notes/implemented/process/2026-09-05-storage-documentation.md).
