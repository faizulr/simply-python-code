def is_palindrome(s):
    """Check if a string is a palindrome, ignoring case and non-alphanumeric characters."""
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


def main():
    user_input = input("Enter a string to check if it's a palindrome: ")
    if is_palindrome(user_input):
        print("Yes, it's a palindrome!")
    else:
        print("No, it's not a palindrome.")


if __name__ == "__main__":
    main()

