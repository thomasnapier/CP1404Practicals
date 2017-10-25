"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


print(do_it(5))


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n <= 0:
        print("0")
    else:
        do_something(n - 1)
        print(n ** 2)

do_something(4)


