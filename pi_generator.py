import decimal
import argparse
import sys

def compute_pi(n):
    """
    Compute Pi to n decimal places using the Chudnovsky algorithm.
    """
    decimal.getcontext().prec = n + 50
    
    C = 426880 * decimal.Decimal(10005).sqrt()
    K = 6
    M = 1
    X = 1
    L = 13591409
    S = decimal.Decimal(13591409)
    
    for i in range(1, n):
        M = M * (K ** 3 - 16 * K) // (i ** 3)
        L += 545140134
        X *= -262537412640768000
        S += decimal.Decimal(M * L) / decimal.Decimal(X)
        K += 12
        
    pi = C / S
    return pi.quantize(decimal.Decimal(10)**-n, rounding=decimal.ROUND_FLOOR)

def main():
    parser = argparse.ArgumentParser(description='Generate Pi to n decimal places.')
    parser.add_argument('n', type=int, help='Number of decimal places to generate')
    args = parser.parse_args()
    
    if args.n < 0:
        print("Error: n must be a non-negative integer.")
        sys.exit(1)
        
    pi = compute_pi(args.n)
    # Format output to show exactly n decimal places
    print(f"{pi:.{args.n}f}")

if __name__ == "__main__":
    main()
