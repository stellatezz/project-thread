from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class CliTests(unittest.TestCase):
    def test_create_and_refuse_overwrite(self):
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder) / "document.txt"
            command = [sys.executable, str(ROOT / "writer/main.py"), str(output)]
            subprocess.run(command + ["first"], check=True, capture_output=True)
            rejected = subprocess.run(command + ["second"], capture_output=True)
            self.assertNotEqual(rejected.returncode, 0)
            self.assertEqual(output.read_text(), "first")
