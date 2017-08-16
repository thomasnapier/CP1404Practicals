"""
Thomas Napier
"""


def main():
    """Get and print name using functions."""
    name = get_name()
    print_parts(name, 3)


def print_parts(name, step=2):
    """Display every step character of name"""
    print(name[::step])


def get_name():
    """Get a non-empty name"""
    name = input("Name: ")
    while name == "":
        print("Invalid name.")
        name = input("Name: ")
    return name


main()
