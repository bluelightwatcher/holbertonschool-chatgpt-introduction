#!/usr/bin/python3
import sys

def factorial(n):
    """Return the factorial of a given number n."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    f = factorial(int(sys.argv[1]))
    print(f)
