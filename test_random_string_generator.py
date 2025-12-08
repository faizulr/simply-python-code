import string
import unittest

from random_string_generator import build_charset, generate_random_string, DEFAULT_CHARSET


class TestRandomStringGenerator(unittest.TestCase):
    def test_default_length_and_charset(self):
        result = generate_random_string()
        self.assertEqual(len(result), 100)
        self.assertTrue(all(char in DEFAULT_CHARSET for char in result))

    def test_custom_length(self):
        result = generate_random_string(10)
        self.assertEqual(len(result), 10)

    def test_custom_charset(self):
        charset = "AB"
        result = generate_random_string(20, charset)
        self.assertTrue(all(char in charset for char in result))

    def test_build_charset_respects_flags(self):
        charset = build_charset(use_lowercase=False, use_uppercase=True, use_digits=False, use_punctuation=False)
        self.assertEqual(charset, string.ascii_uppercase)

    def test_build_charset_requires_at_least_one_option(self):
        with self.assertRaises(ValueError):
            build_charset(use_lowercase=False, use_uppercase=False, use_digits=False, use_punctuation=False)

    def test_invalid_length_raises(self):
        with self.assertRaises(ValueError):
            generate_random_string(0)

    def test_empty_charset_raises(self):
        with self.assertRaises(ValueError):
            generate_random_string(10, "")


if __name__ == "__main__":
    unittest.main()
