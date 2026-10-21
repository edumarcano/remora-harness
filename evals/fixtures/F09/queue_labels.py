"""Current Queue implementation."""


def normalize_labels(labels):
    return sorted({" ".join(label.split()) for label in labels})
