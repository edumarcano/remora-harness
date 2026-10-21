"""Local label formatting."""


def format_labels(labels):
    return [" ".join(label.split()) for label in labels]
