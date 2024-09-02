#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number using recursion.

    Parameters:
    n (int): The number to calculate the factorial of. Must be a non-negative integer.

    Returns:
    int: The factorial of the number n. Returns 1 if n is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    # Get the input number from command-line arguments
    f = factorial(int(sys.argv[1]))
    
    # Print the factorial of the number
    print(f)

