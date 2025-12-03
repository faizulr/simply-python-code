import unittest
from palindrome_checker import is_palindrome

class TestPalindromeChecker(unittest.TestCase):
    def test_palindromes(self):
        self.assertTrue(is_palindrome('madam'))
        self.assertTrue(is_palindrome('racecar'))
        self.assertTrue(is_palindrome('A man, a plan, a canal, Panama'))
        self.assertTrue(is_palindrome('No lemon, no melon'))
        self.assertTrue(is_palindrome('Was it a car or a cat I saw?'))

    def test_non_palindromes(self):
        self.assertFalse(is_palindrome('hello'))
        self.assertFalse(is_palindrome('palindrome'))
        self.assertFalse(is_palindrome('OpenAI'))

if __name__ == "__main__":
    unittest.main()

