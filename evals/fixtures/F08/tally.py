"""Collect labels without network or persistence."""

DEFAULT_LIMIT = 40


def collect(labels, limit=DEFAULT_LIMIT):
    if limit <= 0:
        raise ValueError("limit must be positive")
    return list(labels)[:limit]
