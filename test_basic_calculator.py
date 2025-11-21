import unittest
from basic_calculator import calculate_all

class TestBasicCalculator(unittest.TestCase):
    def test_addition(self):
        res = calculate_all(2, 3)
        self.assertEqual(res['sum'], 5)
    def test_subtraction(self):
        res = calculate_all(10, 4)
        self.assertEqual(res['difference'], 6)
    def test_multiplication(self):
        res = calculate_all(5, 3)
        self.assertEqual(res['product'], 15)
    def test_division(self):
        res = calculate_all(12, 4)
        self.assertEqual(res['quotient'], 3)
    def test_division_by_zero(self):
        res = calculate_all(7, 0)
        self.assertIsNone(res['quotient'])

if __name__ == "__main__":
    unittest.main()
