# Adoption evaluation

Date: 2026-09-05. Host: this Codex task. Python: 3.14.4.

## Task outcome

The repository now has an explicit reading path, a compact documentation ownership map, an implemented adoption decision, and a resumable checkpoint. Existing product decisions, exclusive creation, and the unique Claude handoff rule are preserved. No application or test source was changed. No roadmap, platform, runtime, feature plan, or empty subsystem hierarchy was introduced.

| Action | Artifact |
| --- | --- |
| Append navigation while retaining original text | [AGENTS.md](AGENTS.md) |
| Create orientation, technical explanation, and testing reference | [docs/codebase.md](docs/codebase.md) |
| Record the adoption decision and alternatives | [Implemented process note](.agents/notes/implemented/process/2026-09-05-agentic-adoption.md) |
| Leave continuation and evidence limits | [Current checkpoint](docs/checkpoints/current.md) |
| Record this exercise | This file |

Preserved files are `TASK.md`, `CLAUDE.md`, `writer/AGENTS.md`, `docs/product.md`, `writer/main.py`, and `tests/test_cli.py`. Root rules remain in `AGENTS.md`; writer rules remain in `writer/AGENTS.md`; `CLAUDE.md` remains a portable text entry with its unique handoff instruction. No symlink, import directive, or duplicated shared rulebook was added.

## References actually used

All skill paths below are relative to `/Users/ivanchow/Documents/projects/examples/make-codebase-agentic/skills/`. These references were read, not modified or installed.

| Reference | Application |
| --- | --- |
| `make-codebase-agentic-setup/SKILL.md` | Inspect, preflight, adopt minimally, record a decision, and leave a checkpoint |
| `make-codebase-agentic/references/records.md` | Reuse current owners; combine small technical/testing references in the map |
| `make-codebase-agentic/references/checkpoints.md` | Record scope, snapshot limits, evidence, and the next executable action |
| `make-codebase-agentic-documentation/SKILL.md` | Check source claims and distinguish structural from semantic evidence |
| `make-codebase-agentic-documentation/references/instruction-hierarchy.md` | Preserve unique Claude guidance, retain local writer rules, explicitly navigate scopes, and separate host discovery from file validity |
| `make-codebase-agentic-documentation/references/document-structure.md` | Organize around maintainer tasks without unnecessary files |
| `make-codebase-agentic-documentation/references/technical-writing.md` | Preserve exclusive creation, parent-directory precondition, and failure distinctions |
| `make-codebase-agentic-documentation/references/codebase-documentation.md` | Explain the CLI entry path, ownership of the file handle, success, and meaningful failure |
| `make-codebase-agentic-agent-notes/SKILL.md` | Record the adoption rationale and genuine alternatives |
| `make-codebase-agentic-agent-notes/references/lifecycle.md` | Use one implemented process note; no superseded decision exists |
| `make-codebase-agentic-roadmap/SKILL.md` | Avoid empty roadmaps or an invented future feature sequence |

Raw repository inputs read were `TASK.md`, `AGENTS.md`, `CLAUDE.md`, `writer/AGENTS.md`, `docs/product.md`, `writer/main.py`, and `tests/test_cli.py`. No prior conversation, sibling results, memory files, Git history, or external research was used as evidence.

## Inspection and preflight commands

Commands ran from the repository root unless another directory is stated. Each completed with exit code 0.

```sh
cat TASK.md
rg --files -g '!*lock*' -g '!node_modules/**' -g '!vendor/**' -g '!dist/**' -g '!build/**'
ls -la
cat AGENTS.md
cat CLAUDE.md
cat writer/AGENTS.md
cat docs/product.md
cat writer/main.py
cat tests/test_cli.py
python3 --version
```

The file inventory contained the seven raw files above. `ls -la` showed no existing `.agents` or `.git` directory. Skills and references were read with `cat` using the absolute skill root plus each path in the reference table.

Two inline Python preflight commands used `pathlib` to examine planned destinations and parents, detect symlinks, and compute SHA-256 hashes of the seven original files. They reported `CREATE` for `docs/codebase.md`, `docs/checkpoints/current.md`, `EVALUATION.md`, and `.agents/notes/implemented/process/2026-09-05-agentic-adoption.md`; every parent-blocker list was empty. No symlinks were found. `.git` presence was false; no Git command ran. The preservation hashes are included in the final verification command below.

The `apply_patch` tool appended the root navigation paragraph and created the four missing records. Existing Claude, writer, product, application, test, and task files were not rewritten.

## Executed behavior and reading evidence

Baseline command:

```sh
python3 -m unittest discover -s tests -v
```

Result: exit 0; `test_create_and_refuse_overwrite` passed; one test ran in 0.061 seconds. Python reported version 3.14.4.

Execution caveat: this first test inherited Python's default temporary-directory location. Its `TemporaryDirectory` fixture was created and cleaned outside the repository directory; the exact fixture path was not logged. Subsequent behavioral checks explicitly confined fixture directories to this workspace. No persistent external artifact or source-bundle edit was made.

After adoption, a manual reading exercise started from `writer/` and ran:

```sh
cat ../AGENTS.md
cat AGENTS.md
cat ../docs/product.md
cat ../docs/codebase.md
cat main.py
cat ../tests/test_cli.py
```

All reads completed with exit 0. The path identified the root restriction on output-path/overwrite changes, the writer's exclusive-creation invariant, the product's parent-directory requirement, the `open("x", encoding="utf-8")` implementation, and the test that asserts original content survives duplicate-output failure. The root path had already been read during inspection and is now linked explicitly through the map. This establishes a manually followed reading path in this task, not fresh-host automatic discovery.

Returning to the repository root, the post-adoption test command was:

```sh
TMPDIR="$PWD" python3 -m unittest discover -s tests -v
```

Result: exit 0; the same one test passed in 0.056 seconds. `TMPDIR` confines the existing test's temporary fixture to this workspace without modifying its source or changing the canonical test command.

The following one-time manual CLI exercise also ran from the root:

```sh
python3 - <<'PY'
from pathlib import Path
import subprocess
import sys
import tempfile
root = Path.cwd()
with tempfile.TemporaryDirectory(dir=root, prefix='cli-evaluation-') as folder:
    output = Path(folder) / 'document.txt'
    command = [sys.executable, str(root / 'writer/main.py'), str(output)]
    created = subprocess.run(command + ['Café'], capture_output=True)
    original = output.read_bytes()
    rejected = subprocess.run(command + ['replacement'], capture_output=True)
    missing = Path(folder) / 'absent' / 'document.txt'
    missing_result = subprocess.run([sys.executable, str(root / 'writer/main.py'), str(missing), 'content'], capture_output=True)
    assert created.returncode == 0
    assert original == 'Café'.encode('utf-8')
    assert rejected.returncode != 0 and output.read_bytes() == original
    assert missing_result.returncode != 0 and not missing.parent.exists()
    print(f'create exit={created.returncode}; bytes={original!r}')
    print(f'existing output exit={rejected.returncode}; original preserved=True')
    print(f'missing parent exit={missing_result.returncode}; parent created=False')
print('Manual CLI exercise: PASS; fixture directory removed')
PY
```

Result: command exit 0. Creation exited 0 with UTF-8 bytes `b'Caf\xc3\xa9'`; duplicate creation exited 1 with the original preserved; missing-parent creation exited 1 without creating the parent. The fixture directory was removed. This is executed evidence, not additional permanent test coverage.

## File validity, host discovery, and limitations

- Instruction files are ordinary readable files with separate shared, writer-local, and Claude-specific responsibilities. The final structural/preservation check is recorded below.
- The current Codex task explicitly read the applicable files and followed their behavioral constraints. No fresh Codex session was launched after the changes, so automatic root or nested discovery is unverified.
- No Claude runtime is available. Its entry file and unique instruction are preserved and manually inspected; automatic loading and task behavior remain unverified. No Claude-compatibility claim follows from the file check.
- No symlink/import mechanism or distribution archive was introduced, so there is no runtime or packaging evidence for such a mechanism.
- No `.git` metadata exists in this snapshot. Revision, branch, and pre-existing uncommitted changes cannot be established.
- The unittest covers creation and overwrite rejection. Missing-parent and UTF-8 behavior received the separate manual exercise above. Exact diagnostics, other operating systems, and permission-error cases were not tested.
- The checkpoint records a read-only host exercise that can close the remaining host-discovery gap without inventing product work.

## Final structural and preservation verification

The following command validates preserved content, Markdown link targets, and note metadata, and removes the bytecode generated by the existing test. It does not validate host loading or all Markdown syntax.

```sh
python3 - <<'PY'
from pathlib import Path
import hashlib
import re
root = Path.cwd()
expected = {
    'TASK.md': '4b37730fb52b572121b1215fbbbcd23299bd7d50fab69d515337a3cdefc51237',
    'CLAUDE.md': '79b876b394857128aff756293a626378cfbe48dc4f70eba5b3ad407d716ca530',
    'writer/AGENTS.md': '178a80a00e4e5f5bf28b919f77d4f82d19ac2b2d7950217841bfb99ebf1f389d',
    'docs/product.md': '3bad40f500c4102d01b9e5948cc3d4dc5b789ba6883eab67284c9a6064fe4009',
    'writer/main.py': 'b614af8e0d0258d246e320875da19dd2094526c7ab1bfa4890c0250b74ad96ab',
    'tests/test_cli.py': 'ef5a66b6e53ff824cf27f66d7864f945f4b62cede9fbbf6a1f9bf759afc53a38',
}
for name, digest in expected.items():
    assert hashlib.sha256((root / name).read_bytes()).hexdigest() == digest, name
    print(f'UNCHANGED {name}')
original_root = (root / 'AGENTS.md').read_bytes()[:315]
assert hashlib.sha256(original_root).hexdigest() == 'd070a82fa7801f6d828c896640ea9b0070b7fa09a181375eacf3a9e77d4fa3e7'
print('PRESERVED original 315-byte AGENTS.md content')
links = 0
markdown = sorted(root.rglob('*.md'))
for path in markdown:
    text = re.sub(r'\x60{3}.*?\x60{3}', '', path.read_text(), flags=re.S)
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
        target = target.split('#', 1)[0]
        if not target or '://' in target:
            continue
        assert (path.parent / target).exists(), (path, target)
        links += 1
print(f'PASS {links} local Markdown links across {len(markdown)} Markdown files')
note = root / '.agents/notes/implemented/process/2026-09-05-agentic-adoption.md'
assert 'Status: implemented' in note.read_text()
assert not any(p.is_symlink() for p in root.rglob('*'))
assert not (root / 'docs/roadmaps').exists()
assert not (root / '.git').exists()
print('PASS note lifecycle, plain-file instructions, no invented roadmap, no Git metadata')
cache = root / 'tests/__pycache__/test_cli.cpython-314.pyc'
if cache.exists():
    cache.unlink()
    if not any(cache.parent.iterdir()):
        cache.parent.rmdir()
    print('REMOVED generated unittest bytecode')
print('Final files:')
for path in sorted(root.rglob('*')):
    if path.is_file():
        print(path.relative_to(root))
PY
```

Result: exit 0. All six preserved files matched their original SHA-256 hashes; the original 315 bytes of `AGENTS.md` matched their baseline hash. All 41 local Markdown links across nine Markdown files resolved. Note lifecycle metadata, absence of symlinks, absence of invented roadmap directories, and absence of Git metadata passed. The generated unittest bytecode was removed. The final inventory contained the seven original files plus the four new records listed above.

One JavaScript orchestration attempt before this command failed with `SyntaxError: Unexpected token '*'` because a Markdown fence terminated a template literal. No nested tool ran and no file changed in that failed attempt; the command preparation was corrected.
