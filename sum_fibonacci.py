"""
Generate the first n Fibonacci numbers (1, 1, 2, 3, ...) and print their sum.

Usage:
    python sum_fibonacci.py -n 5
"""
from typing import List
import argparse
import sys

def fibonacci_list(n: int) -> List[int]:
    """Return a list of the first n Fibonacci numbers (1, 1, 2, 3, ...)."""
    if n <= 0:
        return []
    if n == 1:
        return [1]
    seq = [1, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

def sum_fibonacci(n: int) -> int:
    """Return the sum of the first n Fibonacci numbers."""
    return sum(fibonacci_list(n))

def main(argv=None):
    parser = argparse.ArgumentParser(description="Sum first n Fibonacci numbers.")
    parser.add_argument("-n", type=int, required=True, help="Number of Fibonacci integers to sum (non-negative integer).")
    args = parser.parse_args(argv)
    if args.n < 0:
        print("n must be non-negative.", file=sys.stderr)
        sys.exit(2)
    seq = fibonacci_list(args.n)
    total = sum(seq)
    print(f"First {args.n} Fibonacci numbers: {seq}")
    print(f"Sum = {total}")

if __name__ == "__main__":
    main()