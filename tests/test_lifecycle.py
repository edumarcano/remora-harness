"""Operational boundaries through real disposable repositories and packages."""

from contextlib import redirect_stdout, redirect_stderr
import io
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import zipfile
from unittest import TestCase
from unittest.mock import patch

from helpers import install
from tools import package
import test_install as existing


class LifecycleTests(TestCase):
    setUp = existing.InstallationTests.setUp
    git = existing.InstallationTests.git
    commit = existing.InstallationTests.commit
    write = existing.InstallationTests.write
    snapshot = existing.InstallationTests.snapshot
    manifest = existing.InstallationTests.manifest

    def run_install(self, *arguments, target=None):
        output = io.StringIO()
        argv = ["--target", str(target or self.target), *map(str, arguments)]
        if not any(mode in arguments for mode in ("--check", "--update", "--remove")):
            argv.extend(("--environment", "codex"))
        with redirect_stdout(output), redirect_stderr(output):
            code = install.main(argv)
        return code, output.getvalue()

    def preview(self, mode="--update", previous=None, *args):
        argv = [mode, "--previous-source", str(previous or self.source), *args]
        code, output = self.run_install(*argv)
        self.assertEqual(code, 0, output)
        return argv, re.search(r"Plan SHA-256: ([a-f0-9]+)", output)[1]

    def apply(self, argv, token, backup="backup"):
        return self.run_install(*argv, "--apply", "--expect-plan", token,
                                "--backup", self.root / backup)

    def test_profiles_and_relocated_offline_package(self):
        bundle = self.root / "personal" / "remora-bootstrap"
        revision = package.build(self.source, bundle)
        self.assertEqual([p.relative_to(bundle).as_posix() for p in bundle.rglob("SKILL.md")], ["SKILL.md"])
        relocated = self.root / "relocated bootstrap"
        shutil.move(str(bundle), relocated)
        self.source.rename(self.root / "unavailable source")
        with patch.object(install, "SOURCE_ROOT", relocated), patch.object(subprocess, "run", side_effect=AssertionError("Git invoked")):
            self.assertEqual(self.run_install("--apply", "--profile", "python", "--profile", "local")[0], 0)
            self.assertEqual(self.run_install("--check")[0], 0)
        self.assertEqual(self.manifest()["source_revision"], revision)
        self.assertEqual(self.manifest()["selected_profiles"], ["local", "python"])
        self.assertTrue((self.target / ".remora/profiles/python.md").is_file())
        self.assertFalse((self.target / ".remora/profiles/web.md").exists())
        result = subprocess.run([sys.executable, str(self.target / ".remora/helpers/install.py"),
                                 "--check", "--target", str(self.target)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("provenance NOT checked", result.stdout)

    def test_archive_inventory_and_outer_tampering_are_rejected(self):
        bundle = self.root / "bootstrap"
        package.build(self.source, bundle)
        before = self.snapshot()
        helper = bundle / "helpers/install.py"
        original = helper.read_bytes()
        helper.write_bytes(original + b"\n# changed\n")
        with self.assertRaises(install.Conflict):
            install.package_inputs(bundle)
        helper.write_bytes(original)
        with zipfile.ZipFile(bundle / install.BUNDLE, "a") as archive:
            archive.writestr("../outside", b"never extracted")
        with self.assertRaises(install.Conflict):
            install.package_inputs(bundle)
        self.assertEqual(self.snapshot(), before)
        self.assertFalse((self.root / "outside").exists())

    def test_checkout_cannot_be_shadowed_by_untracked_package_metadata(self):
        (self.source / install.BUNDLE_INDEX).write_text("{}")
        before = self.snapshot()
        self.assertEqual(self.run_install("--apply")[0], 1)
        self.assertEqual(self.snapshot(), before)

    def test_new_source_revision_invalidates_prepared_update(self):
        self.assertEqual(self.run_install("--apply")[0], 0)
        previous = self.root / "previous"
        shutil.copytree(self.source, previous)
        argv, token = self.preview("--update", previous, "--profile", "python")
        self.git(self.source, "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                 "-c", "commit.gpgsign=false", "commit", "--quiet", "--allow-empty", "-m", "source moved")
        before = self.snapshot()
        self.assertEqual(self.apply(argv, token)[0], 1)
        self.assertEqual(self.snapshot(), before)

    def test_interrupted_removal_does_not_look_complete(self):
        self.write("AGENTS.md", b"preserve guidance")
        self.assertEqual(self.run_install("--apply")[0], 0)
        argv, token = self.preview("--remove")
        unlink = Path.unlink
        def interrupt(path, *args, **kwargs):
            if path == self.target / ".remora/helpers/install.py":
                raise OSError("removal interrupted")
            return unlink(path, *args, **kwargs)
        with patch.object(Path, "unlink", autospec=True, side_effect=interrupt):
            self.assertEqual(self.apply(argv, token)[0], 2)
        self.assertFalse((self.target / install.MANIFEST).exists())
        self.assertTrue((self.root / "backup" / install.MANIFEST).is_file())
        self.assertEqual((self.target / "AGENTS.md").read_bytes(), b"preserve guidance")

    def test_explicit_upgrade_and_removal_preserve_project_files(self):
        self.write("AGENTS.md", b"project guidance\r\n")
        self.write("notes/local.txt", b"unrelated")
        self.assertEqual(self.run_install("--apply")[0], 0)
        old_source = self.root / "old source"
        shutil.copytree(self.source, old_source)
        standard = self.source / "standards/engineering.md"
        standard.write_bytes(standard.read_bytes() + b"\nNew reviewed instruction.\n")
        self.git(self.source, "add", "standards/engineering.md")
        self.commit()
        argv, token = self.preview("--update", old_source, "--profile", "python", "--environment", "cursor")
        before = self.snapshot()
        self.assertEqual(self.run_install(*argv, "--apply")[0], 1)
        self.assertEqual(self.snapshot(), before)
        code, output = self.apply(argv, token)
        self.assertEqual(code, 0, output)
        self.assertEqual(self.run_install("--check")[0], 0)
        self.assertEqual(self.manifest()["target_environments"], ["cursor"])
        self.assertEqual((self.target / "AGENTS.md").read_bytes(), b"project guidance\r\n")
        argv, token = self.preview("--remove")
        self.assertEqual(self.apply(argv, token, "remove backup")[0], 0)
        self.assertEqual(self.snapshot(), {name: value for name, value in before.items()
                                          if name in {"AGENTS.md", "notes/local.txt"}})

    def test_preview_digest_detects_drift_source_changes_and_collisions(self):
        self.assertEqual(self.run_install("--apply")[0], 0)
        argv, token = self.preview("--update", None, "--profile", "python")
        self.write(".remora/profiles/python.md", b"unmanaged")
        before = self.snapshot()
        self.assertEqual(self.apply(argv, token)[0], 1)
        self.assertEqual(self.snapshot(), before)
        (self.target / ".remora/profiles/python.md").unlink()
        argv, token = self.preview("--remove")
        path = self.target / ".remora/standards/engineering.md"
        path.write_bytes(path.read_bytes() + b"newer edit")
        before = self.snapshot()
        self.assertEqual(self.apply(argv, token)[0], 1)
        self.assertEqual(self.snapshot(), before)

    def test_interruption_retains_before_images_and_no_completion_manifest(self):
        self.assertEqual(self.run_install("--apply")[0], 0)
        argv, token = self.preview("--update", None, "--profile", "python")
        create = install.create_file
        def interrupt(target, name, data, created):
            if target == self.target and name == ".remora/profiles/python.md":
                raise OSError("interrupted")
            return create(target, name, data, created)
        with patch.object(install, "create_file", side_effect=interrupt):
            self.assertEqual(self.apply(argv, token)[0], 2)
        self.assertFalse((self.target / install.MANIFEST).exists())
        backup = self.root / "backup"
        self.assertTrue((backup / install.MANIFEST).is_file())
        record = json.loads((backup / "operation.json").read_text())
        self.assertEqual(record["before"][install.MANIFEST], install.digest((backup / install.MANIFEST).read_bytes()))
        # Recovery inspection must flag a newer edit rather than overwrite it.
        self.write(".remora/standards/engineering.md", b"newer work")
        self.assertNotIn(install.digest(b"newer work"),
                         {record["before"][".remora/standards/engineering.md"],
                          record["after"][".remora/standards/engineering.md"]})
        self.assertEqual(self.run_install("--apply")[0], 1)

    def test_backup_cannot_overlap_target_or_existing_directory(self):
        self.assertEqual(self.run_install("--apply")[0], 0)
        argv, token = self.preview("--remove")
        before = self.snapshot()
        for destination in (self.target / "backup", self.target.parent, self.source):
            code, output = self.run_install(*argv, "--apply", "--expect-plan", token, "--backup", destination)
            self.assertEqual(code, 1, output)
            self.assertEqual(self.snapshot(), before)

    def test_local_rehash_is_consistency_only_and_trusted_source_still_rejects_it(self):
        self.assertEqual(self.run_install("--apply")[0], 0)
        name = ".remora/standards/engineering.md"
        self.write(name, b"local edit")
        manifest = self.manifest()
        manifest["managed_files"][name] = install.digest(b"local edit")
        self.write(install.MANIFEST, (json.dumps(manifest) + "\n").encode())
        with patch.object(install, "SOURCE_ROOT", self.target / ".remora"):
            code, output = self.run_install("--check")
            self.assertEqual(code, 0, output)
            self.assertIn("provenance NOT checked", output)
            self.assertEqual(self.run_install("--check", "--source", self.source)[0], 1)

    def test_known_legacy_inventory_requires_real_matching_source(self):
        # Represent the actual pre-helper Milestone 4 distribution, not a forged manifest.
        old_source = self.root / "legacy source"
        shutil.copytree(self.source, old_source)
        helper = old_source / "helpers/install.py"
        helper.write_text("# trusted legacy installer\n", encoding="utf-8")
        self.git(old_source, "add", "helpers/install.py")
        self.git(old_source, "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                 "-c", "commit.gpgsign=false", "commit", "--quiet", "-m", "legacy")
        revision = self.git(old_source, "rev-parse", "HEAD").decode().strip()
        payload = {target: self.git(old_source, "show", f"HEAD:{source}")
                   for source, target in install.PAYLOAD.items() if source != "helpers/install.py"}
        manifest = install.expected_manifest(revision, payload, ["codex"])
        install.install(self.target, payload, manifest, [])
        self.assertEqual(self.run_install("--check")[0], 1)
        argv, token = self.preview("--update", old_source)
        self.assertEqual(self.apply(argv, token)[0], 0)
        self.assertEqual(self.run_install("--check")[0], 0)
