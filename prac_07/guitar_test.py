from prac_07.guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print(str(gibson))
    print(gibson.get_age())  # expected 95. got 95
    print(gibson.is_vintage())  # expect True. got True

    other = Guitar("Other Guitar", 2012, 2000)
    print(str(other))
    print(other.get_age())  # expected 5. got 5
    print(other.is_vintage())  # expect False. got False


main()
