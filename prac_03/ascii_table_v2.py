"""
CP1404 Practical
ASCII table and converter with functions and docstrings
"""

LOWER = 33
UPPER = 127


def main():
    """Get and convert ASCII values and characters"""
    character = input("Enter a character: ")
    print("The ASCII code for {} is {}".format(character, ord(character)))
    number = get_number(LOWER, UPPER)
    print("The character for {} is {}".format(number, chr(number)))

    # print the ascii table with no columns
    for value in range(LOWER, UPPER + 1):
        print("{:3} {:>4}".format(value, chr(value)))


def get_number(lower=LOWER, upper=UPPER):
    """Get a number from the user between the set boundries"""
    number = int(input("Enter a number between {} and {}: ".format(lower, upper)))
    while number < lower or number > upper:
        number = int(input("Enter a number between {} and {}:".format(lower, upper)))
    return number


main()
