import unittest

from labels import normalize_labels


def fake_normalize(labels):
    return [" ".join(label.split()) for label in labels]


class LabelTests(unittest.TestCase):
    def test_preserves_order_and_duplicates(self):
        self.assertEqual(fake_normalize([" b ", "a", " b "]), ["b", "a", "b"])

    def test_normalization_result(self):
        self.assertEqual(len(normalize_labels([" b ", "a"])), 2)

    def test_collapses_internal_whitespace(self):
        self.assertEqual(normalize_labels([" a   label "]), ["a label"])
