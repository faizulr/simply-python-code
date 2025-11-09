"""
Test file for Number Predictor
Tests various sequence types and edge cases
"""

import unittest
import math
from number_predictor import NumberPredictor


class TestNumberPredictor(unittest.TestCase):
    """Test cases for the NumberPredictor class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.predictor = NumberPredictor()
    
    def test_arithmetic_sequences(self):
        """Test arithmetic sequence predictions."""
        # Simple arithmetic sequence
        prediction, pattern, confidence = self.predictor.predict_next([1, 3, 5])
        self.assertEqual(prediction, 7)
        self.assertIn("Arithmetic", pattern)
        self.assertGreater(confidence, 0.9)
        
        # Negative differences
        prediction, pattern, confidence = self.predictor.predict_next([10, 7, 4])
        self.assertEqual(prediction, 1)
        self.assertIn("Arithmetic", pattern)
        
        # Zero differences
        prediction, pattern, confidence = self.predictor.predict_next([5, 5, 5])
        self.assertEqual(prediction, 5)
        self.assertIn("Arithmetic", pattern)
    
    def test_geometric_sequences(self):
        """Test geometric sequence predictions."""
        # Simple geometric sequence
        prediction, pattern, confidence = self.predictor.predict_next([2, 6, 18])
        self.assertEqual(prediction, 54)
        self.assertIn("Geometric", pattern)
        self.assertGreater(confidence, 0.9)
        
        # Powers of 2
        prediction, pattern, confidence = self.predictor.predict_next([1, 2, 4])
        self.assertEqual(prediction, 8)
        self.assertIn("Geometric", pattern)
        
        # Fractional ratios
        prediction, pattern, confidence = self.predictor.predict_next([8, 4, 2])
        self.assertEqual(prediction, 1)
        self.assertIn("Geometric", pattern)
    
    def test_fibonacci_sequences(self):
        """Test Fibonacci-like sequence predictions."""
        # Classic Fibonacci
        prediction, pattern, confidence = self.predictor.predict_next([1, 1, 2])
        self.assertEqual(prediction, 3)
        self.assertIn("Fibonacci", pattern)
        
        # Fibonacci starting from different numbers
        prediction, pattern, confidence = self.predictor.predict_next([2, 3, 5])
        self.assertEqual(prediction, 8)
        self.assertIn("Fibonacci", pattern)
    
    def test_polynomial_sequences(self):
        """Test polynomial sequence predictions."""
        # Quadratic sequence (squares)
        prediction, pattern, confidence = self.predictor.predict_next([1, 4, 9])
        self.assertEqual(prediction, 16)
        
        # Triangular numbers
        prediction, pattern, confidence = self.predictor.predict_next([1, 3, 6])
        self.assertEqual(prediction, 10)
    
    def test_exponential_sequences(self):
        """Test exponential sequence predictions."""
        # Natural exponential
        e = math.e
        sequence = [e**1, e**2, e**3]
        prediction, pattern, confidence = self.predictor.predict_next(sequence)
        expected = e**4
        self.assertAlmostEqual(prediction, expected, places=5)
        self.assertIn("Exponential", pattern)
    
    def test_power_sequences(self):
        """Test power sequence predictions."""
        # Powers of 2
        prediction, pattern, confidence = self.predictor.predict_next([2, 4, 8])
        self.assertEqual(prediction, 16)
        self.assertIn("Powers", pattern)
        
        # Powers of 3
        prediction, pattern, confidence = self.predictor.predict_next([3, 9, 27])
        self.assertEqual(prediction, 81)
        self.assertIn("Powers", pattern)
    
    def test_factorial_sequences(self):
        """Test factorial sequence predictions."""
        prediction, pattern, confidence = self.predictor.predict_next([1, 2, 6])
        self.assertEqual(prediction, 24)
        self.assertIn("Factorial", pattern)
        
        prediction, pattern, confidence = self.predictor.predict_next([2, 6, 24])
        self.assertEqual(prediction, 120)
        self.assertIn("Factorial", pattern)
    
    def test_harmonic_sequences(self):
        """Test harmonic sequence predictions."""
        # 1/n sequence
        prediction, pattern, confidence = self.predictor.predict_next([1, 0.5, 1/3])
        expected = 0.25
        self.assertAlmostEqual(prediction, expected, places=5)
        self.assertIn("Harmonic", pattern)
    
    def test_edge_cases(self):
        """Test edge cases and error handling."""
        # Wrong number of inputs
        with self.assertRaises(ValueError):
            self.predictor.predict_next([1, 2])
        
        with self.assertRaises(ValueError):
            self.predictor.predict_next([1, 2, 3, 4])
        
        # Zeros in sequence
        prediction, pattern, confidence = self.predictor.predict_next([0, 1, 2])
        self.assertEqual(prediction, 3)
        
        # Negative numbers
        prediction, pattern, confidence = self.predictor.predict_next([-3, -1, 1])
        self.assertEqual(prediction, 3)
    
    def test_complex_patterns(self):
        """Test more complex mathematical patterns."""
        # Alternating sequence
        prediction, pattern, confidence = self.predictor.predict_next([1, -2, 4])
        # Should detect some pattern, exact value depends on implementation
        self.assertIsInstance(prediction, (int, float))
        
        # Prime-like patterns (will likely fallback to polynomial)
        prediction, pattern, confidence = self.predictor.predict_next([2, 3, 5])
        self.assertIsInstance(prediction, (int, float))


def run_example_predictions():
    """Run some example predictions to demonstrate functionality."""
    predictor = NumberPredictor()
    
    test_cases = [
        ([1, 2, 3], "Simple arithmetic"),
        ([1, 4, 9], "Perfect squares"),
        ([1, 1, 2], "Fibonacci"),
        ([2, 6, 18], "Geometric (×3)"),
        ([1, 2, 6], "Factorial"),
        ([2, 4, 8], "Powers of 2"),
        ([1, 3, 6], "Triangular numbers"),
        ([1, 0.5, 0.25], "Halving sequence"),
        ([10, 7, 4], "Decreasing arithmetic"),
        ([1, -1, 1], "Alternating pattern"),
    ]
    
    print("🧪 TESTING NUMBER PREDICTOR")
    print("=" * 60)
    
    for sequence, description in test_cases:
        try:
            prediction, pattern, confidence = predictor.predict_next(sequence)
            print(f"📊 {description}")
            print(f"   Sequence: {sequence} → {prediction:.3g}")
            print(f"   Pattern: {pattern} (Confidence: {confidence:.1%})")
            print()
        except Exception as e:
            print(f"❌ Error with {description}: {e}")
            print()


if __name__ == "__main__":
    # Run example predictions
    run_example_predictions()
    
    # Run unit tests
    print("\n" + "="*60)
    print("🔬 RUNNING UNIT TESTS")
    print("="*60)
    unittest.main(verbosity=2)