"""
Number Sequence Predictor
========================
Predicts the next number in a sequence based on 3 given numbers.
Supports various sequence types: arithmetic, geometric, polynomial, fibonacci-like, etc.
"""

import math
from typing import List, Tuple, Optional


class NumberPredictor:
    """A class to predict the next number in a sequence."""
    
    def __init__(self):
        self.prediction_methods = [
            self._arithmetic_sequence,
            self._geometric_sequence,
            self._polynomial_sequence,
            self._fibonacci_like_sequence,
            self._quadratic_sequence,
            self._exponential_sequence,
            self._factorial_like_sequence,
            self._power_sequence,
            self._harmonic_sequence,
            self._custom_patterns
        ]
    
    def predict_next(self, sequence: List[float]) -> Tuple[float, str, float]:
        """
        Predict the next number in the sequence.
        
        Args:
            sequence: List of 3 numbers
            
        Returns:
            Tuple of (predicted_number, pattern_type, confidence_score)
        """
        if len(sequence) != 3:
            raise ValueError("Exactly 3 numbers are required for prediction")
        
        best_prediction = None
        best_confidence = 0
        best_pattern = "Unknown"
        
        for method in self.prediction_methods:
            try:
                prediction, pattern, confidence = method(sequence)
                if confidence > best_confidence:
                    best_prediction = prediction
                    best_confidence = confidence
                    best_pattern = pattern
            except Exception:
                continue
        
        if best_prediction is None:
            # Fallback: simple linear extrapolation
            diff1 = sequence[1] - sequence[0]
            diff2 = sequence[2] - sequence[1]
            best_prediction = sequence[2] + (diff1 + diff2) / 2
            best_pattern = "Linear Extrapolation"
            best_confidence = 0.3
        
        return best_prediction, best_pattern, best_confidence
    
    def _arithmetic_sequence(self, seq: List[float]) -> Tuple[float, str, float]:
        """Check for arithmetic sequence (constant difference)."""
        diff1 = seq[1] - seq[0]
        diff2 = seq[2] - seq[1]
        
        if abs(diff1 - diff2) < 1e-10:  # Equal differences
            next_num = seq[2] + diff1
            return next_num, "Arithmetic Sequence", 0.95
        
        # Check if it's close to arithmetic
        avg_diff = (diff1 + diff2) / 2
        if abs(diff1 - diff2) / max(abs(avg_diff), 1) < 0.1:
            next_num = seq[2] + avg_diff
            return next_num, "Approximate Arithmetic", 0.7
        
        raise ValueError("Not arithmetic")
    
    def _geometric_sequence(self, seq: List[float]) -> Tuple[float, str, float]:
        """Check for geometric sequence (constant ratio)."""
        if seq[0] == 0 or seq[1] == 0:
            raise ValueError("Cannot have zero in geometric sequence")
        
        ratio1 = seq[1] / seq[0]
        ratio2 = seq[2] / seq[1]
        
        if abs(ratio1 - ratio2) < 1e-10:  # Equal ratios
            next_num = seq[2] * ratio1
            return next_num, "Geometric Sequence", 0.95
        
        # Check if it's close to geometric
        avg_ratio = (ratio1 + ratio2) / 2
        if abs(ratio1 - ratio2) / abs(avg_ratio) < 0.1:
            next_num = seq[2] * avg_ratio
            return next_num, "Approximate Geometric", 0.7
        
        raise ValueError("Not geometric")
    
    def _polynomial_sequence(self, seq: List[float]) -> Tuple[float, str, float]:
        """Check for polynomial patterns using finite differences."""
        # First differences
        diff1_1 = seq[1] - seq[0]
        diff1_2 = seq[2] - seq[1]
        
        # Second difference
        diff2 = diff1_2 - diff1_1
        
        if abs(diff2) < 1e-10:  # Linear
            next_num = seq[2] + diff1_2
            return next_num, "Linear Polynomial", 0.9
        
        # Quadratic pattern
        next_diff1 = diff1_2 + diff2
        next_num = seq[2] + next_diff1
        return next_num, "Quadratic Polynomial", 0.8
    
    def _fibonacci_like_sequence(self, seq: List[float]) -> Tuple[float, str, float]:
        """Check for Fibonacci-like sequences (sum of previous two)."""
        if abs(seq[2] - (seq[0] + seq[1])) < 1e-10:
            next_num = seq[1] + seq[2]
            return next_num, "Fibonacci-like", 0.9
        
        # Weighted Fibonacci
        if seq[0] != 0:
            weight = seq[2] / (seq[0] + seq[1]) if (seq[0] + seq[1]) != 0 else 1
            if 0.8 <= weight <= 1.2:
                next_num = weight * (seq[1] + seq[2])
                return next_num, "Weighted Fibonacci", 0.6
        
        raise ValueError("Not Fibonacci-like")
    
    def _quadratic_sequence(self, seq: List[float]) -> Tuple[float, str, float]:
        """Check for quadratic patterns like squares, triangular numbers."""
        # Check for perfect squares
        sqrt_vals = [math.sqrt(abs(x)) for x in seq if x >= 0]
        if len(sqrt_vals) == 3 and all(abs(x - round(x)) < 1e-10 for x in sqrt_vals):
            sqrt_ints = [round(x) for x in sqrt_vals]
            if sqrt_ints[1] - sqrt_ints[0] == sqrt_ints[2] - sqrt_ints[1]:
                next_sqrt = sqrt_ints[2] + (sqrt_ints[1] - sqrt_ints[0])
                next_num = next_sqrt ** 2
                return next_num, "Perfect Squares", 0.85
        
        # Check for triangular numbers (n*(n+1)/2)
        triangular_check = []
        for x in seq:
            # Solve n*(n+1)/2 = x for n
            n = (-1 + math.sqrt(1 + 8*x)) / 2 if x > 0 else 0
            triangular_check.append(abs(n - round(n)) < 1e-10)
        
        if all(triangular_check):
            n_vals = [round((-1 + math.sqrt(1 + 8*x)) / 2) for x in seq]
            if n_vals[1] - n_vals[0] == n_vals[2] - n_vals[1]:
                next_n = n_vals[2] + (n_vals[1] - n_vals[0])
                next_num = next_n * (next_n + 1) / 2
                return next_num, "Triangular Numbers", 0.85
        
        raise ValueError("Not quadratic pattern")
    
    def _exponential_sequence(self, seq: List[float]) -> Tuple[float, str, float]:
        """Check for exponential patterns."""
        if all(x > 0 for x in seq):
            log_seq = [math.log(x) for x in seq]
            # Check if log sequence is arithmetic
            diff1 = log_seq[1] - log_seq[0]
            diff2 = log_seq[2] - log_seq[1]
            
            if abs(diff1 - diff2) < 1e-10:
                next_log = log_seq[2] + diff1
                next_num = math.exp(next_log)
                return next_num, "Exponential", 0.8
        
        raise ValueError("Not exponential")
    
    def _factorial_like_sequence(self, seq: List[float]) -> Tuple[float, str, float]:
        """Check for factorial-like patterns."""
        # Check if sequence matches factorials
        factorials = [1, 1, 2, 6, 24, 120, 720, 5040]
        
        for i in range(len(factorials) - 2):
            if (abs(seq[0] - factorials[i]) < 1e-10 and 
                abs(seq[1] - factorials[i+1]) < 1e-10 and 
                abs(seq[2] - factorials[i+2]) < 1e-10):
                next_num = factorials[i+3]
                return next_num, "Factorial", 0.9
        
        raise ValueError("Not factorial")
    
    def _power_sequence(self, seq: List[float]) -> Tuple[float, str, float]:
        """Check for power sequences like 2^n, 3^n, etc."""
        if all(x > 0 for x in seq):
            # Try different bases
            for base in [2, 3, 4, 5, 10]:
                log_base_seq = [math.log(x) / math.log(base) for x in seq]
                
                # Check if powers are consecutive integers
                if all(abs(x - round(x)) < 1e-10 for x in log_base_seq):
                    powers = [round(x) for x in log_base_seq]
                    if powers[1] - powers[0] == powers[2] - powers[1] == 1:
                        next_power = powers[2] + 1
                        next_num = base ** next_power
                        return next_num, f"Powers of {base}", 0.85
        
        raise ValueError("Not power sequence")
    
    def _harmonic_sequence(self, seq: List[float]) -> Tuple[float, str, float]:
        """Check for harmonic sequences (1/n)."""
        if all(x != 0 for x in seq):
            reciprocals = [1/x for x in seq]
            
            # Check if reciprocals form arithmetic sequence
            diff1 = reciprocals[1] - reciprocals[0]
            diff2 = reciprocals[2] - reciprocals[1]
            
            if abs(diff1 - diff2) < 1e-10:
                next_reciprocal = reciprocals[2] + diff1
                next_num = 1 / next_reciprocal if next_reciprocal != 0 else float('inf')
                return next_num, "Harmonic", 0.8
        
        raise ValueError("Not harmonic")
    
    def _custom_patterns(self, seq: List[float]) -> Tuple[float, str, float]:
        """Check for other custom patterns."""
        # Alternating signs
        if len(set([x >= 0 for x in seq])) == 2:
            # Pattern might involve alternating signs
            abs_seq = [abs(x) for x in seq]
            signs = [1 if x >= 0 else -1 for x in seq]
            
            try:
                next_abs, pattern, confidence = self._arithmetic_sequence(abs_seq)
                next_sign = -signs[2] if len(set(signs)) == 2 else signs[2]
                next_num = next_sign * next_abs
                return next_num, f"Alternating {pattern}", confidence * 0.8
            except:
                pass
        
        # Polynomial with different degrees
        x_vals = [0, 1, 2]  # Assume positions 0, 1, 2
        try:
            # Fit polynomial and predict next value
            coeffs = self._fit_polynomial(x_vals, seq, degree=2)
            next_num = self._evaluate_polynomial(coeffs, 3)
            return next_num, "Higher Order Polynomial", 0.6
        except:
            pass
        
        raise ValueError("No pattern found")
    
    def _fit_polynomial(self, x_vals: List[float], y_vals: List[float], degree: int) -> List[float]:
        """Fit polynomial of given degree to data points."""
        # Simple polynomial fitting using method of differences
        if degree == 2 and len(x_vals) == 3:
            # For quadratic: y = ax^2 + bx + c
            # System of equations for x=0,1,2
            c = y_vals[0]
            a_plus_b = y_vals[1] - c
            four_a_plus_two_b = y_vals[2] - c
            
            b = 2 * a_plus_b - (four_a_plus_two_b) / 2
            a = a_plus_b - b
            
            return [a, b, c]
        
        raise ValueError("Polynomial fitting not implemented for this degree")
    
    def _evaluate_polynomial(self, coeffs: List[float], x: float) -> float:
        """Evaluate polynomial at given x value."""
        result = 0
        for i, coeff in enumerate(coeffs):
            result += coeff * (x ** (len(coeffs) - 1 - i))
        return result


def main():
    """Interactive number sequence predictor."""
    predictor = NumberPredictor()
    
    print("🔮 NUMBER SEQUENCE PREDICTOR")
    print("=" * 50)
    print("Enter 3 numbers and I'll predict the next one!")
    print("Supports: arithmetic, geometric, polynomial, Fibonacci, and more patterns")
    print("-" * 50)
    
    while True:
        try:
            print("\n📝 Enter 3 numbers (or 'quit' to exit):")
            user_input = input("Numbers (space-separated): ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("👋 Thanks for using the Number Predictor!")
                break
            
            # Parse input
            numbers = [float(x) for x in user_input.split()]
            
            if len(numbers) != 3:
                print("❌ Please enter exactly 3 numbers.")
                continue
            
            # Make prediction
            prediction, pattern, confidence = predictor.predict_next(numbers)
            
            print(f"\n🎯 PREDICTION RESULTS:")
            print(f"📊 Sequence: {numbers[0]} → {numbers[1]} → {numbers[2]} → ?")
            print(f"🔮 Next number: {prediction:.6g}")
            print(f"🧠 Pattern detected: {pattern}")
            print(f"📈 Confidence: {confidence:.1%}")
            
            if confidence < 0.5:
                print("⚠️  Low confidence - the pattern might not be reliable")
            elif confidence > 0.8:
                print("✅ High confidence - strong pattern detected!")
            
            # Show additional info for some patterns
            if "Arithmetic" in pattern:
                diff = numbers[1] - numbers[0]
                print(f"ℹ️  Common difference: {diff:.6g}")
            elif "Geometric" in pattern and numbers[0] != 0:
                ratio = numbers[1] / numbers[0]
                print(f"ℹ️  Common ratio: {ratio:.6g}")
            
        except ValueError as e:
            print(f"❌ Error: {e}")
            print("Please enter valid numbers.")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")


if __name__ == "__main__":
    main()