"""Exercise installation as a user operation and structural failures as negative controls."""

from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from check import SKILLS, validate_bundle
from install import install
from package import package
from zipfile import ZipFile


class InstallationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.base = Path(self.temp.name).resolve()
        self.target = self.base / ".agents" / "skills"

    def tearDown(self):
        self.temp.cleanup()

    def test_cli_installs_complete_bundle_and_can_be_repeated(self):
        command = [sys.executable, str(ROOT / "scripts/install.py"), "--repo", str(self.base)]
        subprocess.run(command + ["--dry-run"], check=True, capture_output=True)
        self.assertFalse(self.target.exists())
        subprocess.run(command, check=True, capture_output=True)
        subprocess.run(command, check=True, capture_output=True)
        self.assertEqual({p.name for p in self.target.iterdir()}, SKILLS)
        for name in SKILLS:
            link = self.target / name
            self.assertTrue(link.is_symlink())
            self.assertEqual(link.resolve(), ROOT / "skills" / name)
            self.assertTrue((link / "SKILL.md").is_file())
        reference = self.target / "project-thread-ios" / ".." / "project-thread-engineering" / "SKILL.md"
        self.assertTrue(reference.is_file())

    def test_conflict_blocks_every_write(self):
        self.target.mkdir(parents=True)
        existing = self.target / "project-thread-ios"
        existing.mkdir()
        (existing / "mine.txt").write_text("keep")
        with self.assertRaises(ValueError):
            install(ROOT, self.base)
        self.assertEqual(list(self.target.iterdir()), [existing])
        self.assertEqual((existing / "mine.txt").read_text(), "keep")

    def test_broken_link_is_a_conflict(self):
        self.target.mkdir(parents=True)
        broken = self.target / "project-thread-ios"
        broken.symlink_to(self.base / "missing")
        with self.assertRaises(ValueError):
            install(ROOT, self.base)
        self.assertEqual(list(self.target.iterdir()), [broken])

    def test_parent_file_and_parent_symlink_block(self):
        parent = self.base / ".agents"
        parent.write_text("keep")
        with self.assertRaises(ValueError):
            install(ROOT, self.base)
        self.assertEqual(parent.read_text(), "keep")
        parent.unlink()
        other = self.base / "other"
        other.mkdir()
        parent.symlink_to(other, target_is_directory=True)
        with self.assertRaises(ValueError):
            install(ROOT, self.base)
        self.assertEqual(list(other.iterdir()), [])

    def test_remove_preserves_unrelated_skill_and_replacement(self):
        install(ROOT, self.base)
        unrelated = self.target / "my-skill"
        unrelated.mkdir()
        replacement = self.target / "project-thread-ios"
        replacement.unlink()
        replacement.mkdir()
        install(ROOT, self.base, remove=True, dry_run=True)
        self.assertTrue((self.target / "project-thread").is_symlink())
        install(ROOT, self.base, remove=True)
        self.assertEqual(set(self.target.iterdir()), {unrelated, replacement})

    def test_failure_rolls_back_created_links(self):
        original = Path.symlink_to
        calls = 0

        def fail_second(destination, *args, **kwargs):
            nonlocal calls
            calls += 1
            if calls == 2:
                raise OSError("simulated write failure")
            return original(destination, *args, **kwargs)

        with patch.object(Path, "symlink_to", fail_second):
            with self.assertRaises(OSError):
                install(ROOT, self.base)
        self.assertEqual(list(self.target.iterdir()), [])


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.bundle = Path(self.temp.name) / "project-thread"
        shutil.copytree(ROOT, self.bundle, ignore=shutil.ignore_patterns(".git", "__pycache__", ".build", "dist"))

    def tearDown(self):
        self.temp.cleanup()

    def test_bundle_passes(self):
        self.assertEqual(validate_bundle(self.bundle), [])

    def test_missing_required_skill_fails(self):
        shutil.rmtree(self.bundle / "skills/project-thread-engineering")
        self.assertTrue(any("inventory" in e for e in validate_bundle(self.bundle)))

    def test_broken_conditional_reference_fails(self):
        (self.bundle / "skills/project-thread-ios/references/media-editing.md").unlink()
        self.assertTrue(any("media-editing.md" in e for e in validate_bundle(self.bundle)))

    def test_nonportable_absolute_link_fails(self):
        (self.bundle / "bad.md").write_text("[host-only file](/etc/hosts)\n")
        self.assertTrue(any("non-portable" in e for e in validate_bundle(self.bundle)))

    def test_placeholder_and_lifecycle_mismatch_fail(self):
        note = self.bundle / ".agents/notes/implemented/process/bad.md"
        note.parent.mkdir(parents=True, exist_ok=True)
        note.write_text("# Decision\nStatus: proposed\n[TODO: unfinished]\n")
        errors = validate_bundle(self.bundle)
        self.assertTrue(any("placeholder" in e for e in errors))
        self.assertTrue(any("lifecycle" in e for e in errors))

    def test_archive_roundtrip_and_reproducibility(self):
        archive = package(self.bundle)
        original = archive.read_bytes()
        self.assertEqual(package(self.bundle).read_bytes(), original)
        extracted = Path(self.temp.name) / "extracted"
        with ZipFile(archive) as zipped:
            self.assertTrue(all(name.startswith("project-thread/") for name in zipped.namelist()))
            self.assertFalse(any("/.git/" in name or "__pycache__" in name for name in zipped.namelist()))
            zipped.extractall(extracted)
        unpacked = extracted / "project-thread"
        self.assertEqual(validate_bundle(unpacked), [])
        destination = Path(self.temp.name) / "app"
        destination.mkdir()
        install(unpacked, destination)
        self.assertEqual({p.name for p in (destination / ".agents/skills").iterdir()}, SKILLS)


if __name__ == "__main__":
    unittest.main()
