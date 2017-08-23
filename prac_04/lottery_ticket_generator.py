import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    number_of_picks = int(input("How many quick picks? "))
    while number_of_picks <= 0:
        print("Invalid number of picks")
        number_of_picks = int(input("How many quick picks? "))

    for number in range(number_of_picks):
        for line in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            print("{:3}".format(number), end="")
        print()


main()
