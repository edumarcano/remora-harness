"""Domain normalization."""


def normalize_labels(labels):
    if any(not isinstance(label, str) for label in labels):
        raise TypeError("labels must be strings")
    return [" ".join(label.split()) for label in labels]
