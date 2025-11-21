def generate_fibonacci_up_to_n_digits(max_digits):
    """
    Generates Fibonacci series numbers that have up to `max_digits` digits.
    """
    fib_series = [0, 1]
    
    while True:
        next_fib = fib_series[-1] + fib_series[-2]
        if len(str(next_fib)) > max_digits:
            break
        fib_series.append(next_fib)
        
    return fib_series

if __name__ == "__main__":
    MAX_DIGITS = 10
    print(f"Generating Fibonacci series with numbers up to {MAX_DIGITS} digits:")
    series = generate_fibonacci_up_to_n_digits(MAX_DIGITS)
    
    # Print the series
    print(series)
    
    # Print some stats to verify
    print(f"\nTotal numbers generated: {len(series)}")
    print(f"Largest number: {series[-1]}")
    print(f"Digits in largest number: {len(str(series[-1]))}")
