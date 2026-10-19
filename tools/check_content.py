"""Check the bounded Markdown file-link subset documented in evals/README.md."""

import argparse
import os
from pathlib import Path, PureWindowsPath
import re
import sys
from urllib.parse import unquote, urlsplit


LINK = re.compile(r"!?\[[^\[\]\n]*\]\((<[^<>\n]*>|[^()\n]*)\)")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")


def documents(root: Path) -> list[Path]:
    """Scan authored Markdown, never fixture payloads or arbitrary checkouts."""
    paths = [path for path in root.iterdir() if path.suffix == ".md"]
    fixtures = root / "evals" / "fixtures"

    def scan_error(error):
        raise error

    for directory in ("docs", "evals", "standards"):
        start = root / directory
        if not start.exists():
            continue
        for parent, children, files in os.walk(start, onerror=scan_error):
            children[:] = [name for name in children if Path(parent) / name != fixtures]
            paths.extend(Path(parent) / name for name in files if name.endswith(".md"))
    return sorted(paths)


def check_document(root: Path, document: Path) -> list[str]:
    location = document.relative_to(root).as_posix()
    if not document.resolve().is_relative_to(root):
        return [f"{location}: source resolves outside repository"]
    lines = document.read_text(encoding="utf-8").splitlines()
    errors = []
    fence = None
    for number, line in enumerate(lines, 1):
        marker = FENCE.match(line)
        if fence:
            if (marker and marker[1][0] == fence[0]
                    and len(marker[1]) >= len(fence) and not marker[2].strip()):
                fence = None
            continue
        if marker:
            fence = marker[1]
            continue
        for match in LINK.finditer(line):
            destination = match[1]
            angled = destination.startswith("<")
            destination = destination[1:-1] if angled else destination
            prefix = f"{location}:{number}"
            if not destination:
                errors.append(f"{prefix}: empty link destination")
                continue
            if not angled and any(char.isspace() for char in destination):
                errors.append(f"{prefix}: use <...> for spaces; link titles are unsupported")
                continue
            url = urlsplit(destination)
            if url.scheme.lower() in ("http", "https", "mailto"):
                continue
            if destination.startswith("#"):
                continue
            path = unquote(url.path)
            if (url.scheme or url.netloc or path.startswith("/")
                    or PureWindowsPath(path).drive or "\\" in path):
                errors.append(f"{prefix}: expected a relative forward-slash file path: {destination}")
                continue
            if url.query:
                errors.append(f"{prefix}: local link queries are unsupported: {destination}")
                continue
            target = (document.parent / path).resolve()
            if not target.is_relative_to(root):
                errors.append(f"{prefix}: link escapes repository: {destination}")
            elif not target.is_file():
                errors.append(f"{prefix}: missing file target: {destination}")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1],
                        help="repository root (default: this script's repository)")
    root = parser.parse_args(argv).root.resolve()
    if not root.is_dir():
        print("Content check incomplete: root is not a directory", file=sys.stderr)
        return 2
    try:
        sources = documents(root)
        if not sources:
            print("Content check incomplete: no authored Markdown found", file=sys.stderr)
            return 2
        errors = [error for source in sources for error in check_document(root, source)]
    except (OSError, UnicodeError, ValueError) as error:
        print(f"Content check incomplete: {error}", file=sys.stderr)
        return 2
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        print(f"Content check failed: {len(errors)} issue(s)", file=sys.stderr)
        return 1
    print(f"Content check passed: {len(sources)} Markdown file(s); file targets only")
    return 0


if __name__ == "__main__":
    sys.exit(main())
