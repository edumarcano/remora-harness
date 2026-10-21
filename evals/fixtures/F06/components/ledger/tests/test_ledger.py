import unittest

from ledger import normalize_labels


class LabelTests(unittest.TestCase):
    def test_normalization_preserves_order_and_duplicates(self):
        self.assertEqual(normalize_labels([" b ", "a  label", " b "]),
                         ["b", "a label", "b"])

    def test_empty_input(self):
        self.assertEqual(normalize_labels([]), [])
