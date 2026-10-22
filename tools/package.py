"""Build one local bootstrap directory from trusted committed inputs; never download."""

import argparse
import json
from pathlib import Path
import sys
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from helpers import install


def build(source: Path, output: Path):
    revision, files = install.source_inputs(source)
    install.inspect_path(output.absolute())
    if output.exists():
        raise install.Conflict("Package output must not exist")
    output.mkdir(parents=True)
    exposed = {"SKILL.md": "skills/remora-bootstrap/SKILL.md",
               "helpers/install.py": "helpers/install.py",
               "templates/AGENTS.md": "templates/AGENTS.md",
               **{name: name for name in install.PAYLOAD if name.startswith("standards/")}}
    for outer, inner in exposed.items():
        install.create_file(output, outer, files[inner], [])
    with (output / install.BUNDLE).open("xb") as stream, zipfile.ZipFile(stream, "w") as archive:
        for name in sorted(files):
            item = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            item.external_attr = 0o100644 << 16
            archive.writestr(item, files[name])
    index = {"source_revision": revision, "files": {name: install.digest(data) for name, data in files.items()}}
    install.create_file(output, install.BUNDLE_INDEX,
                        (json.dumps(index, indent=2, sort_keys=True) + "\n").encode(), [])
    install.package_inputs(output)
    return revision


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=install.SOURCE_ROOT)
    parser.add_argument("--output", type=Path, required=True, help="new bootstrap skill directory")
    args = parser.parse_args(argv)
    try:
        revision = build(args.source, args.output)
        print(f"Built and checked bootstrap {revision}: {args.output}")
        return 0
    except install.Conflict as error:
        print(f"Package conflict: {error}", file=sys.stderr)
        return 1
    except (OSError, ValueError, zipfile.BadZipFile) as error:
        print(f"Package incomplete: {error}; inspect partial output", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
