"""Local service boundary."""

from labels import normalize_labels


def handle(labels):
    try:
        return {"labels": normalize_labels(labels)}
    except TypeError:
        return {"error": "labels must be strings"}
