import random

def generate_and_sum_random_numbers():
    """
    Asks the user for a count 'n', generates 'n' random numbers,
    and calculates their sum.
    """
    try:
        n_input = input("Enter the number of random numbers to generate and add: ")
        n = int(n_input)
        
        if n <= 0:
            print("Please enter a positive integer.")
            return

        print(f"Generating {n} random numbers (between 1 and 100)...")
        
        numbers = []
        for _ in range(n):
            num = random.randint(1, 100)
            numbers.append(num)
            
        print(f"Generated numbers: {numbers}")
        
        total_sum = sum(numbers)
        print(f"Sum of the generated numbers: {total_sum}")
        
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    generate_and_sum_random_numbers()
