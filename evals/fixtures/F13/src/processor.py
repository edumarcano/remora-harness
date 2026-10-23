"""Deterministic item processor utility."""


def process_items(items, limit=20):
    if limit <= 0:
        raise ValueError("limit must be positive")
    return [str(item).strip() for item in items[:limit] if str(item).strip()]
