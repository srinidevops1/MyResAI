# Documentation for Testing.py

This document provides an overview of the `Testing.py` script, its functionality, and how to use it.

## Overview

`Testing.py` is a simple, interactive command-line script that performs basic arithmetic operations:
- Addition
- Multiplication
- Division
- Subtraction

The script prompts the user to enter two numbers for each operation and then prints the result to the console.

## How to Run the Script

To run the script, navigate to its directory in your terminal and execute the following command:

```bash
python Testing.py
```

The script will then guide you through each of the four arithmetic operations sequentially.

## Script Components

The script is composed of several functions that work together to perform the calculations.

### Main Functions

These are the core functions that handle the logic for each arithmetic operation.

- **`add_two_numbers()`**
  - Prompts the user for two numbers.
  - Calculates and prints their sum.

- **`multiply_two_numbers()`**
  - Prompts the user for two numbers.
  - Calculates and prints their product.

- **`divide_two_numbers()`**
  - Prompts the user for two numbers.
  - Calculates and prints their quotient.
  - Includes a check to prevent division by zero.

- **`subtract_two_numbers()`**
  - Prompts the user for two numbers.
  - Calculates and prints their difference.

### Helper Function

- **`_get_numbers_for_operation(prompt1, prompt2)`**
  - This is a private helper function used by the main functions to get and validate user input.
  - It takes two prompt strings as arguments.
  - It attempts to convert the user's input into floating-point numbers.
  - If the input is not a valid number, it prints an error message and returns `None`.

## Error Handling

The script includes robust error handling for the following scenarios:

- **Invalid Input:** If the user enters a non-numeric value when prompted for a number, the script will print an error message and skip that operation. This is handled by the `_get_numbers_for_operation` function.
- **Division by Zero:** The `divide_two_numbers` function includes a specific check to see if the second number (the divisor) is zero. If it is, the script will print an error message and avoid performing the calculation to prevent a `ZeroDivisionError`.
