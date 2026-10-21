"""Normalize whitespace without changing sequence identity."""


def normalize_labels(labels):
    return [" ".join(label.split()) for label in labels]
