"""Preservation and integrity checks using disposable source and target repositories."""

from contextlib import redirect_stderr, redirect_stdout
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from helpers import install as installer


ROOT = Path(__file__).resolve().parents[1]
DESTINATION = ".remora/standards/engineering.md"


class InstallationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="remora-install-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.source = self.root / "source checkout"
        self.target = self.root / "target project"
        self.source.mkdir()
        self.target.mkdir()
        for name in installer.INPUTS:
            path = self.source / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes((ROOT / name).read_bytes().replace(b"\r\n", b"\n"))
        # Disable checkout conversion for fixture construction only, not globally.
        self.git(self.source, "init", "--quiet")
        self.git(self.source, "config", "core.autocrlf", "false")
        self.git(self.source, "add", "--", *installer.INPUTS)
        self.commit()
        self.git(self.target, "init", "--quiet")
        self.source_patch = patch.object(installer, "SOURCE_ROOT", self.source)
        self.source_patch.start()
        self.addCleanup(self.source_patch.stop)

    def git(self, directory, *arguments):
        return subprocess.run(["git", "-C", str(directory), *arguments],
                              capture_output=True, check=True).stdout

    def commit(self):
        self.git(self.source, "-c", "user.name=Fixture", "-c",
                 "user.email=fixture@example.invalid", "-c", "commit.gpgsign=false",
                 "commit", "--quiet", "-m", "fixture input")

    def run_install(self, *arguments, target=None):
        output = io.StringIO()
        argv = ["--target", str(target or self.target), *arguments]
        if "--check" not in arguments:
            argv.extend(("--environment", "codex"))
        with redirect_stdout(output), redirect_stderr(output):
            code = installer.main(argv)
        return code, output.getvalue()

    def write(self, name, data=b"project-owned\r\n"):
        path = self.target / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        return path

    def snapshot(self):
        return {path.relative_to(self.target).as_posix():
                (path.read_bytes(), path.stat().st_mtime_ns)
                for path in self.target.rglob("*") if path.is_file() and
                ".git" not in path.relative_to(self.target).parts}

    def manifest(self):
        return json.loads((self.target / installer.MANIFEST).read_text(encoding="utf-8"))

    def change_manifest(self, value):
        (self.target / installer.MANIFEST).write_text(json.dumps(value), encoding="utf-8")

    def test_empty_unborn_target_preview_apply_and_check(self):
        head = subprocess.run(["git", "-C", str(self.target), "rev-parse", "--verify", "HEAD"],
                              capture_output=True, check=False)
        self.assertNotEqual(head.returncode, 0)
        self.assertEqual(self.run_install()[0], 0)
        self.assertEqual(set(self.target.iterdir()), {self.target / ".git"})
        self.assertEqual(self.run_install("--apply")[0], 0)
        self.assertEqual(set(self.snapshot()), {DESTINATION, installer.MANIFEST})
        self.assertEqual(self.run_install("--check")[0], 0)
        manifest = self.manifest()
        self.assertEqual(manifest["source_revision"],
                         self.git(self.source, "rev-parse", "HEAD").decode().strip())
        self.assertEqual(manifest["schema_version"], 1)
        self.assertEqual(manifest["remora_version"], "development")
        self.assertEqual(manifest["selected_profiles"], [])
        self.assertEqual(manifest["managed_files"],
                         {DESTINATION: installer.digest((self.target / DESTINATION).read_bytes())})

    def test_specification_and_custom_guidance_are_preserved(self):
        specification = (ROOT / "evals/fixtures/F02/SPEC.md").read_bytes()
        self.write("SPEC.md", specification)
        for name in ("AGENTS.md", "nested/AGENTS.md", ".remora/project.md",
                     ".agents/skills/review/SKILL.md",
                     ".agents/skills/remora-bootstrap/SKILL.md", "application.py"):
            self.write(name)
        before = self.snapshot()
        self.assertEqual(self.run_install()[0], 0)
        self.assertEqual(self.snapshot(), before)
        self.assertEqual(self.run_install("--apply")[0], 0)
        after = self.snapshot()
        self.assertEqual({name: after[name] for name in before}, before)
        self.assertEqual(set(after) - set(before), {DESTINATION, installer.MANIFEST})
        self.assertEqual((self.target / "SPEC.md").read_bytes(), specification)

    def test_identical_reruns_preserve_bytes_and_modification_times(self):
        self.assertEqual(self.run_install("--apply", "--environment", "cursor",
                                          "--environment", "cursor")[0], 0)
        self.assertEqual(self.manifest()["target_environments"], ["codex", "cursor"])
        before = self.snapshot()
        for arguments in (("--apply", "--environment", "cursor"),
                          ("--environment", "cursor"), ("--check",)):
            self.assertEqual(self.run_install(*arguments)[0], 0)
            self.assertEqual(self.snapshot(), before)

    def test_unmanaged_identical_payload_is_never_adopted(self):
        data = (self.source / "standards/engineering.md").read_bytes()
        self.write(DESTINATION, data)
        before = self.snapshot()
        for arguments in ((), ("--apply",)):
            code, output = self.run_install(*arguments)
            self.assertEqual(code, 1)
            self.assertIn("Unmanaged destination", output)
            self.assertEqual(self.snapshot(), before)
        self.assertFalse((self.target / installer.MANIFEST).exists())

    def test_all_destinations_are_preflighted_before_writing(self):
        self.write(installer.MANIFEST, b"not a manifest")
        before = self.snapshot()
        self.assertEqual(self.run_install("--apply")[0], 1)
        self.assertEqual(self.snapshot(), before)
        self.assertFalse((self.target / DESTINATION).exists())

    def test_non_directory_ancestor_and_directory_destinations_are_conflicts(self):
        for name in (".remora", DESTINATION, installer.MANIFEST):
            with self.subTest(name=name), tempfile.TemporaryDirectory() as temporary:
                target = Path(temporary)
                path = target / name
                path.parent.mkdir(parents=True, exist_ok=True)
                if name == ".remora":
                    path.write_bytes(b"owned")
                else:
                    path.mkdir()
                self.assertEqual(self.run_install("--apply", target=target)[0], 1)

    def test_modified_and_missing_managed_files_are_not_repaired(self):
        self.assertEqual(self.run_install("--apply")[0], 0)
        managed = self.target / DESTINATION
        managed.write_bytes(b"local edits")
        before = self.snapshot()
        self.assertEqual(self.run_install("--apply")[0], 1)
        self.assertEqual(self.run_install("--check")[0], 1)
        self.assertEqual(self.snapshot(), before)
        managed.unlink()
        before = self.snapshot()
        self.assertEqual(self.run_install("--apply")[0], 1)
        self.assertEqual(self.run_install("--check")[0], 1)
        self.assertEqual(self.snapshot(), before)

    def test_invalid_metadata_and_unsafe_inventory_are_rejected(self):
        self.assertEqual(self.run_install("--apply")[0], 0)
        original = self.manifest()
        for field, bad in (("schema_version", True), ("schema_version", 2),
                           ("remora_version", "latest"), ("source_revision", "main"),
                           ("selected_profiles", ["python"]), ("target_environments", []),
                           ("target_environments", ["unknown"]),
                           ("target_environments", ["codex", "codex"]),
                           ("managed_files", {DESTINATION: "invalid"})):
            with self.subTest(field=field, bad=bad):
                self.change_manifest({**original, field: bad})
                before = self.snapshot()
                self.assertEqual(self.run_install("--check")[0], 1)
                self.assertEqual(self.snapshot(), before)
        for name in ("../outside", "/absolute", "C:/absolute", "a\\b", ".remora/../owned"):
            with self.subTest(path=name):
                self.change_manifest({**original, "managed_files": {name: "0" * 64}})
                self.assertEqual(self.run_install("--check")[0], 1)
        for data in (b"{", b"\xff", b"[]", b'{"schema_version":1,"schema_version":1}'):
            with self.subTest(data=data):
                self.write(installer.MANIFEST, data)
                self.assertEqual(self.run_install("--check")[0], 1)

    def test_locally_rehashed_file_still_fails_pinned_source_comparison(self):
        self.assertEqual(self.run_install("--apply")[0], 0)
        data = b"modified standard"
        self.write(DESTINATION, data)
        manifest = self.manifest()
        manifest["managed_files"][DESTINATION] = installer.digest(data)
        self.change_manifest(manifest)
        self.assertEqual(self.run_install("--check")[0], 1)

    def test_selection_and_source_revision_changes_require_future_update_workflow(self):
        self.assertEqual(self.run_install("--apply")[0], 0)
        before = self.snapshot()
        self.assertEqual(self.run_install("--apply", "--environment", "cursor")[0], 1)
        self.git(self.source, "-c", "user.name=Fixture", "-c",
                 "user.email=fixture@example.invalid", "-c", "commit.gpgsign=false",
                 "commit", "--quiet", "--allow-empty", "-m", "next revision")
        self.assertEqual(self.run_install("--check")[0], 1)
        self.assertEqual(self.run_install("--apply")[0], 1)
        self.assertEqual(self.snapshot(), before)

    def test_dirty_source_inputs_are_rejected_but_unrelated_edits_are_allowed(self):
        self.source.joinpath("README.md").write_text("unrelated", encoding="utf-8")
        self.assertEqual(self.run_install()[0], 0)
        for name in installer.INPUTS:
            with self.subTest(name=name):
                path = self.source / name
                original = path.read_bytes()
                path.write_bytes(original + b"\nmodified\n")
                self.assertEqual(self.run_install("--apply")[0], 1)
                self.assertFalse((self.target / ".remora").exists())
                path.write_bytes(original)

    def test_checkout_crlf_does_not_change_installed_git_object_bytes(self):
        self.git(self.source, "config", "core.autocrlf", "true")
        for name in installer.INPUTS:
            path = self.source / name
            path.write_bytes(path.read_bytes().replace(b"\n", b"\r\n"))
        self.assertEqual(self.run_install("--apply")[0], 0)
        committed = self.git(self.source, "show", "HEAD:standards/engineering.md")
        self.assertEqual((self.target / DESTINATION).read_bytes(), committed)
        self.assertNotIn(b"\r\n", committed)

    def test_index_flags_cannot_hide_modified_source_bytes(self):
        name = "standards/engineering.md"
        path = self.source / name
        original = path.read_bytes()
        for flag in ("assume-unchanged", "skip-worktree"):
            with self.subTest(flag=flag):
                self.git(self.source, "update-index", "--" + flag, "--", name)
                path.write_bytes(b"hidden local modifications")
                self.assertEqual(self.run_install("--apply")[0], 1)
                self.assertFalse((self.target / ".remora").exists())
                path.write_bytes(original)
                self.git(self.source, "update-index", "--no-" + flag, "--", name)

    def test_staged_source_changes_are_rejected_even_with_restored_working_bytes(self):
        name = "standards/engineering.md"
        path = self.source / name
        original = path.read_bytes()
        path.write_bytes(b"staged modifications")
        self.git(self.source, "add", "--", name)
        path.write_bytes(original)
        self.assertEqual(self.run_install("--apply")[0], 1)
        self.assertFalse((self.target / ".remora").exists())

    def test_interruption_before_manifest_preserves_created_files_and_refuses_adoption(self):
        create = installer.create_file

        def interrupt(target, name, data, created):
            if name == installer.MANIFEST:
                raise OSError("simulated write interruption")
            return create(target, name, data, created)

        with patch.object(installer, "create_file", side_effect=interrupt):
            code, output = self.run_install("--apply")
        self.assertEqual(code, 2)
        self.assertIn(DESTINATION, output)
        self.assertFalse((self.target / installer.MANIFEST).exists())
        self.assertTrue((self.target / DESTINATION).is_file())
        before = self.snapshot()
        self.assertEqual(self.run_install("--apply")[0], 1)
        self.assertEqual(self.snapshot(), before)

    def test_partial_payload_write_never_publishes_manifest(self):
        create = installer.create_file

        def partial(target, name, data, created):
            create(target, name, data[:10], created)
            raise OSError("simulated partial write")

        with patch.object(installer, "create_file", side_effect=partial):
            self.assertEqual(self.run_install("--apply")[0], 2)
        self.assertFalse((self.target / installer.MANIFEST).exists())
        self.assertEqual(self.run_install("--apply")[0], 1)

    def test_destination_created_after_preflight_is_preserved(self):
        create = installer.create_file

        def race(target, name, data, created):
            self.write(name, b"new user edit")
            return create(target, name, data, created)

        with patch.object(installer, "create_file", side_effect=race):
            self.assertEqual(self.run_install("--apply")[0], 1)
        self.assertEqual((self.target / DESTINATION).read_bytes(), b"new user edit")
        self.assertFalse((self.target / installer.MANIFEST).exists())

    def test_payload_changed_before_publication_prevents_completion(self):
        create = installer.create_file

        def race(target, name, data, created):
            create(target, name, data, created)
            if name == DESTINATION:
                self.write(name, b"newer edit")

        with patch.object(installer, "create_file", side_effect=race):
            self.assertEqual(self.run_install("--apply")[0], 1)
        self.assertEqual((self.target / DESTINATION).read_bytes(), b"newer edit")
        self.assertFalse((self.target / installer.MANIFEST).exists())

    def test_missing_target_manifest_and_unavailable_source_are_distinguished(self):
        self.assertEqual(self.run_install(target=self.root / "missing")[0], 2)
        self.assertEqual(self.run_install("--check")[0], 1)
        with patch.object(installer, "SOURCE_ROOT", self.target):
            self.assertEqual(self.run_install()[0], 2)

    def test_command_line_from_another_working_directory_and_invalid_arguments(self):
        script = self.source / "helpers/install.py"
        command = [sys.executable, str(script), "--target", str(self.target)]
        result = subprocess.run([*command, "--environment", "antigravity", "--apply"],
                                cwd=self.root, capture_output=True, check=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.manifest()["target_environments"], ["antigravity"])
        result = subprocess.run([*command, "--check"], cwd=self.target,
                                capture_output=True, check=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        for arguments in ([], ["--check", "--apply"], ["--environment", "unknown"],
                          ["--check", "--environment", "codex"]):
            result = subprocess.run([*command, *arguments], cwd=self.root,
                                    capture_output=True, check=False)
            self.assertEqual(result.returncode, 2)

    def test_symlink_destinations_and_ancestors_are_rejected(self):
        outside = self.root / "outside"
        outside.mkdir()
        link = self.target / ".remora"
        try:
            link.symlink_to(outside, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest("symlink creation unavailable in this environment")
        self.assertEqual(self.run_install("--apply")[0], 1)
        self.assertEqual(list(outside.iterdir()), [])
        link.unlink()
        link.symlink_to(self.root / "absent", target_is_directory=True)
        self.assertEqual(self.run_install("--apply")[0], 1)
        link.unlink()
        alias = self.root / "alias"
        alias.symlink_to(self.target, target_is_directory=True)
        self.assertEqual(self.run_install("--apply", target=alias)[0], 1)
        # Lexical '..' must not hide a link from the safety inspection.
        self.assertEqual(self.run_install("--apply", target=alias / ".." / self.target.name)[0], 1)

    @unittest.skipUnless(os.name == "nt", "Windows junction test")
    def test_windows_junction_is_rejected_without_changing_its_target(self):
        outside = self.root / "outside"
        outside.mkdir()
        junction = self.target / ".remora"
        result = subprocess.run(["cmd", "/c", "mklink", "/J", str(junction), str(outside)],
                                capture_output=True, check=False)
        if result.returncode:
            self.skipTest("junction creation unavailable in this environment")
        try:
            self.assertEqual(self.run_install("--apply")[0], 1)
            self.assertEqual(list(outside.iterdir()), [])
        finally:
            # Remove only the test junction, never recursively traverse its target.
            junction.rmdir()


if __name__ == "__main__":
    unittest.main()
