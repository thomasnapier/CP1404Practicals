"""
Thomas Napier
"""
def main():
    """Loop until valid name is given then split"""
    name = get_name()
    while name == "":
        print("Invalid name")
        name = get_name()
    print(name[1:len(name):2])


def get_name():
    """Get name from the user"""
    name = input("Enter name: ")
    return name


main()