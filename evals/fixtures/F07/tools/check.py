"""Check Harbor without writing files or using external services."""

from pathlib import Path
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from harbor import format_labels

assert format_labels([" a  b ", "a b"]) == ["a b", "a b"]
print("Harbor check passed")
