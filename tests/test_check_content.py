"""Behavioral checks for the authored-content link checker."""

from contextlib import redirect_stderr, redirect_stdout
import io
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from tools.check_content import main


class ContentCheckTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)

    def write(self, path, content, newline="\n"):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content.replace("\n", newline).encode("utf-8"))
        return target

    def run_check(self, root=None):
        output = io.StringIO()
        with redirect_stderr(output), redirect_stdout(output):
            code = main(["--root", str(root or self.root)])
        return code, output.getvalue()

    def test_relative_targets_spaces_encoding_and_unchecked_fragments(self):
        self.write("docs/target file.md", "# Target\n")
        self.write("README.md", "[file](<docs/target file.md#unknown>)\n"
                   "[encoded](docs/target%20file.md)\n")
        self.write("docs/guide.md", "[relative](target%20file.md)\n")
        self.assertEqual(self.run_check()[0], 0)

    def test_missing_target_reports_source_line(self):
        self.write("docs/guide.md", "# Guide\n\n[missing](absent.md)\n")
        code, output = self.run_check()
        self.assertEqual(code, 1)
        self.assertIn("docs/guide.md:3: missing file target: absent.md", output)

    def test_fenced_examples_are_not_checked(self):
        self.write("README.md", "````markdown\n[example](absent.md)\n```\n"
                   "[still example](absent.md)\n````\n"
                   "~~~text\n[example](absent.md)\n~~~\n")
        self.assertEqual(self.run_check()[0], 0)
        self.write("README.md", "```\n[example](absent.md)\n```\n[real](missing.md)\n")
        self.assertEqual(self.run_check()[0], 1)

    def test_fixture_payload_is_excluded_but_its_link_is_checked(self):
        self.write("evals/fixtures/F02/SPEC.md", "[deliberate input](missing.md)\n")
        self.write("evals/README.md", "[fixture](fixtures/F02/SPEC.md)\n")
        self.assertEqual(self.run_check()[0], 0)
        self.write("evals/README.md", "[missing fixture](fixtures/F02/absent.md)\n")
        self.assertEqual(self.run_check()[0], 1)

    def test_external_urls_and_heading_anchors_are_not_checked(self):
        self.write("README.md", "[web](https://invalid.example/no-page)\n"
                   "[email](mailto:nobody@example.invalid)\n[anchor](#missing)\n")
        self.assertEqual(self.run_check()[0], 0)

    def test_escaping_and_absolute_targets_are_rejected(self):
        for target in ("../outside.md", "%2e%2e/outside.md", "/README.md",
                       "C:/README.md", "C:\\README.md", "//server/file.md"):
            with self.subTest(target=target):
                self.write("README.md", f"[unsafe]({target})\n")
                self.assertEqual(self.run_check()[0], 1)

    def test_symlink_escape_is_rejected_when_symlinks_available(self):
        with tempfile.TemporaryDirectory() as outside:
            target = Path(outside) / "outside.md"
            target.write_text("outside", encoding="utf-8")
            try:
                (self.root / "link.md").symlink_to(target)
            except (OSError, NotImplementedError):
                self.skipTest("symlink creation unavailable in this environment")
            self.write("README.md", "[escape](link.md)\n")
            code, output = self.run_check()
            self.assertEqual(code, 1)
            self.assertIn("link escapes repository", output)

    def test_lf_and_crlf_have_the_same_outcome(self):
        for newline in ("\n", "\r\n"):
            with self.subTest(newline=newline):
                self.write("README.md", "# Guide\n[bad](missing.md)\n", newline)
                code, output = self.run_check()
                self.assertEqual(code, 1)
                self.assertIn("README.md:2:", output)

    def test_invalid_root_empty_scope_and_invalid_utf8_are_incomplete(self):
        self.assertEqual(self.run_check(self.root / "absent")[0], 2)
        self.assertEqual(self.run_check()[0], 2)
        (self.root / "README.md").write_bytes(b"\xff")
        self.assertEqual(self.run_check()[0], 2)

    def test_unreadable_guidance_directory_cannot_silently_pass(self):
        self.write("README.md", "# Valid root document\n")
        self.write("docs/guide.md", "[broken](absent.md)\n")
        scandir = os.scandir
        # main() resolves the root, including Windows short-path aliases.
        unreadable = (self.root / "docs").resolve()

        def restricted(path):
            if Path(path) == unreadable:
                raise PermissionError("guidance directory unavailable")
            return scandir(path)

        with patch("tools.check_content.os.scandir", side_effect=restricted):
            code, output = self.run_check()
        self.assertEqual(code, 2)
        self.assertIn("guidance directory unavailable", output)

        code, output = self.run_check()
        self.assertEqual(code, 1)
        self.assertIn("docs/guide.md:1: missing file target: absent.md", output)

    def test_directory_and_unsupported_destinations_fail(self):
        (self.root / "docs").mkdir()
        for target in ("docs", "", 'README.md "title"', "README.md?raw=1"):
            with self.subTest(target=target):
                self.write("README.md", f"[link]({target})\n")
                self.assertEqual(self.run_check()[0], 1)

    def test_command_line_is_independent_of_working_directory(self):
        self.write("README.md", "[missing](absent.md)\n")
        script = Path(__file__).resolve().parents[1] / "tools" / "check_content.py"
        result = subprocess.run([sys.executable, str(script), "--root", str(self.root)],
                                cwd=self.root, capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 1)
        self.assertIn("README.md:1: missing file target", result.stderr)

        # Without --root, resolve the checkout from the script rather than cwd.
        copied = self.root / "tools" / "check_content.py"
        copied.parent.mkdir()
        copied.write_bytes(script.read_bytes())
        elsewhere = self.root / "elsewhere"
        elsewhere.mkdir()
        result = subprocess.run([sys.executable, str(copied)], cwd=elsewhere,
                                capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 1)
        self.assertIn("README.md:1: missing file target", result.stderr)


if __name__ == "__main__":
    unittest.main()
