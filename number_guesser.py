import math

def get_valid_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

def number_guesser():
    print("Welcome to the Number Guesser!")
    print("Think of a number between a range, and I will try to guess it.")
    print("I will ask you if your number is Higher (H), Lower (L), or Correct (C) compared to my guess.")

    while True:
        low = get_valid_integer("Enter the lower bound of the range: ")
        high = get_valid_integer("Enter the upper bound of the range: ")
        if low < high:
            break
        print("Lower bound must be less than upper bound.")

    print(f"\nGreat! Think of a number between {low} and {high} (inclusive).")
    input("Press Enter when you are ready...")

    attempts = 0
    possible_guesses = math.ceil(math.log2(high - low + 1))
    print(f"\nI can guess your number in at most {possible_guesses} attempts!\n")

    while low <= high:
        guess = (low + high) // 2
        attempts += 1
        
        print(f"Attempt #{attempts}: Is your number {guess}?")
        feedback = input("Enter (H) if your number is Higher, (L) if Lower, or (C) if Correct: ").strip().upper()

        if feedback == 'C':
            print(f"\nHooray! I guessed your number {guess} in {attempts} attempts.")
            return
        elif feedback == 'H':
            low = guess + 1
        elif feedback == 'L':
            high = guess - 1
        else:
            print("Invalid input. Please enter 'H', 'L', or 'C'.")
            attempts -= 1 # Don't count invalid attempts

    print("\nSomething went wrong. Are you sure you answered correctly? The range is empty now.")

if __name__ == "__main__":
    number_guesser()
