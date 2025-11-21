# basic_calculator.py

def calculate_all(num1, num2):
    result = {
        "sum": num1 + num2,
        "difference": num1 - num2,
        "product": num1 * num2,
        "quotient": None if num2 == 0 else num1 / num2
    }
    return result


def print_results(num1, num2):
    res = calculate_all(num1, num2)
    print(f"Sum: {num1} + {num2} = {res['sum']}")
    print(f"Difference: {num1} - {num2} = {res['difference']}")
    print(f"Product: {num1} * {num2} = {res['product']}")
    if res["quotient"] is not None:
        print(f"Quotient: {num1} / {num2} = {res['quotient']}")
    else:
        print("Quotient: Division by zero is undefined.")


def main():
    print("Enter two numbers:")
    try:
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    print_results(num1, num2)

if __name__ == "__main__":
    main()
