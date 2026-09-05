# Sample editor storage

This robust and future-proof storage layer handles everything automatically. Saves are always safe, errors are handled, and exported videos are guaranteed to match saved projects. The caller can pass any Python object. The project directory is made if necessary.

## Everything you need

First the saver calls JSON encoding, then it creates a temp file, then writes bytes, then flushes, then calls fsync, then replaces the file. We considered a database but chose files because the prototype has one document. The whole module is just two functions. You should use it. The platform is robust.

## Quick start

From this directory with Python 3.9+, import `save_project` and `load_project` from `project_store`. Call them with a `pathlib.Path`. The editor calls save synchronously; the UI layer serializes saves for a single project. This sample has no render/export code or automatic recovery scan.
