from pathlib import Path
import hashlib
import json
import math
import os
import re
import subprocess
import sys
from tempfile import TemporaryDirectory
from unittest.mock import patch
import project_store as storage

root = Path.cwd()
readme = (root / 'README.md').read_text()
example = re.search(r"```sh\npython3 - <<'PY'\n(.*?)\nPY\n```", readme, re.S).group(1)
result = subprocess.run([sys.executable, '-c', example], capture_output=True, text=True, check=True)
assert result.stdout == 'Saved and reopened First cut\n'
print('PASS: README command, copied verbatim from its Python body')

passed = 0
def verify(label, fn):
    global passed
    fn()
    passed += 1
    print('PASS:', label)

def raises(kind, fn):
    try:
        fn()
    except kind as error:
        return error
    raise AssertionError(f'Expected {kind.__name__}')

with TemporaryDirectory(dir=root) as directory:
    folder = Path(directory)
    path = folder / 'project.json'
    old = {'title': 'Saved', 'clips': []}
    def create():
        assert storage.save_project(path, old) is None
        assert storage.load_project(path) == old
        assert old == {'title': 'Saved', 'clips': []}
        assert list(folder.iterdir()) == [path]
    verify('save creates destination, round-trip matches, input unchanged, no temp left', create)
    old_bytes = path.read_bytes()
    def overwrite():
        events = []
        actual_sync = os.fsync
        actual_replace = os.replace
        def sync(fd):
            events.append('fsync')
            return actual_sync(fd)
        def replace(source, destination):
            assert events == ['fsync']
            assert Path(source).parent == path.parent
            assert path.read_bytes() == old_bytes
            assert json.loads(Path(source).read_text()) == {'title': 'New'}
            events.append('replace')
            return actual_replace(source, destination)
        with patch.object(storage.os, 'fsync', side_effect=sync), patch.object(storage.os, 'replace', side_effect=replace):
            storage.save_project(path, {'title': 'New'})
        assert events == ['fsync', 'replace']
        assert storage.load_project(path) == {'title': 'New'}
        storage.save_project(path, old)
    verify('overwrite syncs first, uses same parent, preserves old bytes until replacement', overwrite)
    def encoding_failure(value, exception):
        before = set(folder.iterdir())
        raises(exception, lambda: storage.save_project(path, value))
        assert path.read_bytes() == old_bytes
        assert set(folder.iterdir()) == before
    verify('set serialization fails before filesystem changes', lambda: encoding_failure({'bad': {1}}, TypeError))
    circular = {}
    circular['self'] = circular
    verify('circular input raises ValueError and preserves old file', lambda: encoding_failure(circular, ValueError))
    def missing_parent():
        missing = folder / 'absent' / 'project.json'
        raises(FileNotFoundError, lambda: storage.save_project(missing, old))
        assert not missing.parent.exists()
        assert path.read_bytes() == old_bytes
    verify('missing parent raises and is not created', missing_parent)
    def injected_error(operation):
        failure = OSError(f'injected {operation}')
        with patch.object(storage.os, operation, side_effect=failure):
            error = raises(OSError, lambda: storage.save_project(path, {'title': 'Unsaved'}))
        assert error is failure
        assert path.read_bytes() == old_bytes
        assert list(folder.iterdir()) == [path]
    verify('fsync OSError reaches caller, old file survives, temporary file removed', lambda: injected_error('fsync'))
    verify('replace OSError reaches caller, old file survives, temporary file removed', lambda: injected_error('replace'))
    def cleanup_failure():
        original = OSError('injected replacement error')
        cleanup = PermissionError('injected unlink error')
        with patch.object(storage.os, 'replace', side_effect=original), patch.object(Path, 'unlink', side_effect=cleanup):
            error = raises(PermissionError, lambda: storage.save_project(path, {'title': 'Unsaved'}))
        assert error is cleanup
        assert error.__context__ is original
        assert path.read_bytes() == old_bytes
        remaining = [entry for entry in folder.iterdir() if entry != path]
        assert len(remaining) == 1
        remaining[0].unlink()
    verify('cleanup failure replaces surfaced error and leaves temporary file', cleanup_failure)
    def transformations():
        storage.save_project(path, {1: ('clip',), 'number': float('nan')})
        decoded = storage.load_project(path)
        assert decoded['1'] == ['clip'] and math.isnan(decoded['number'])
    verify('JSON key and tuple conversion plus default NaN acceptance', transformations)
    def non_dict():
        storage.save_project(path, ['clip'])
        assert storage.load_project(path) == ['clip']
        path.write_text('42')
        assert storage.load_project(path) == 42
    verify('annotations do not enforce a dictionary on save or load', non_dict)
    def invalid_json():
        path.write_text('{')
        raises(json.JSONDecodeError, lambda: storage.load_project(path))
        assert path.read_text() == '{'
    verify('malformed JSON raises without repair', invalid_json)
    def invalid_utf8():
        path.write_bytes(b'\xff')
        raises(UnicodeDecodeError, lambda: storage.load_project(path))
        assert path.read_bytes() == b'\xff'
    verify('invalid UTF-8 raises without mutation', invalid_utf8)
    verify('missing file load raises FileNotFoundError', lambda: raises(FileNotFoundError, lambda: storage.load_project(folder / 'missing.json')))

expected = '125467c51bd575bb6666d867b2f0631865607206193cc6017d9dde9c351d5c93'
assert hashlib.sha256((root / 'project_store.py').read_bytes()).hexdigest() == expected
print(f'PASS: {passed} storage checks, README example, and source SHA256 unchanged')
