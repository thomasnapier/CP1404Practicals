"""
Thomas Napier
"""
def main():
    name = get_name()
    while name == "":
        print("Invalid name")
        name = get_name()
    print(name[1:len(name):2])


def get_name():
    name = input("Enter name: ")
    return name


main()