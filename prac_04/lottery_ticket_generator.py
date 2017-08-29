import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    quick_pick = []
    number_of_picks = int(input("How many quick picks? "))
    while number_of_picks <= 0:
        print("Invalid number of picks")
        number_of_picks = int(input("How many quick picks? "))
    for number in range(number_of_picks):
        for line in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:  # while the generated number is already in the quick picks list
                number = random.randint(MINIMUM, MAXIMUM)  # generate another
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()
