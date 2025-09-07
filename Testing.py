
"""
A simple script to perform basic arithmetic operations based on user input.
"""


def _get_numbers_for_operation(prompt1, prompt2):
    """Helper function to get two numbers from the user and handle errors."""
    try:
        num1 = float(input(prompt1))
        num2 = float(input(prompt2))
        return num1, num2
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return None, None


def add_two_numbers():
    """Takes two numbers from user input and prints their sum."""
    num1, num2 = _get_numbers_for_operation(
        "Enter the first number: ",
        "Enter the second number: "
    )
    if num1 is not None and num2 is not None:
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is: {result}")


def multiply_two_numbers():
    """Takes two numbers from user input and prints their product."""
    num1, num2 = _get_numbers_for_operation(
        "Enter the first number for multiplication: ",
        "Enter the second number for multiplication: "
    )
    if num1 is not None and num2 is not None:
        result = num1 * num2
        print(f"The product of {num1} and {num2} is: {result}")


def divide_two_numbers():
    """Takes two numbers from user input and prints their quotient."""
    num1, num2 = _get_numbers_for_operation(
        "Enter the first number for division: ",
        "Enter the second number for division: "
    )
    if num1 is not None and num2 is not None:
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The quotient of {num1} and {num2} is: {result}")


def subtract_two_numbers():
    """Takes two numbers from user input and prints their difference."""
    num1, num2 = _get_numbers_for_operation(
        "Enter the first number for subtraction: ",
        "Enter the second number for subtraction: "
    )
    if num1 is not None and num2 is not None:
        result = num1 - num2
        print(f"The difference of {num1} and {num2} is: {result}")


if __name__ == "__main__":
    add_two_numbers()
    print("\n--- Now for multiplication ---")
    multiply_two_numbers()
    print("\n--- Now for division ---")
    divide_two_numbers()
    print("\n--- Now for subtraction ---")
    subtract_two_numbers()
