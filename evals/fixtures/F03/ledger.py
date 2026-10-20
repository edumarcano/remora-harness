"""Normalize labels for the local Ledger utility."""


def normalize_labels(labels: list[str]) -> list[str]:
    return [" ".join(label.split()) for label in labels]
