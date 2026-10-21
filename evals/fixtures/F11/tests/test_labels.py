import unittest

from labels import normalize_labels
from service import handle


class DomainTests(unittest.TestCase):
    def test_normalization(self):
        self.assertEqual(normalize_labels([" b ", "a   label", " b "]),
                         ["b", "a label", "b"])

    def test_invalid_label(self):
        with self.assertRaises(TypeError):
            normalize_labels([None])


class ServiceTests(unittest.TestCase):
    def test_normalization(self):
        self.assertEqual(handle([" b ", "a   label", " b "]),
                         {"labels": ["b", "a label", "b"]})

    def test_invalid_label(self):
        self.assertEqual(handle([None]), {"error": "labels must be strings"})
