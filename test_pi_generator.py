import unittest
import decimal
from pi_generator import compute_pi

class TestPiGenerator(unittest.TestCase):
    def test_compute_pi_small_n(self):
        # Test with a small number of digits
        n = 10
        expected_pi = "3.1415926535"
        pi = compute_pi(n)
        self.assertEqual(f"{pi:.{n}f}", expected_pi)

    def test_compute_pi_larger_n(self):
        # Test with a slightly larger number of digits
        n = 50
        expected_pi = "3.14159265358979323846264338327950288419716939937510"
        pi = compute_pi(n)
        self.assertEqual(f"{pi:.{n}f}", expected_pi)

    def test_compute_pi_zero(self):
        # Test with 0 digits (should return 3)
        n = 0
        expected_pi = "3"
        pi = compute_pi(n)
        self.assertEqual(f"{pi:.{n}f}", expected_pi)

if __name__ == '__main__':
    unittest.main()
