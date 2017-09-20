from prac_07.car import Car

MENU = """Menu:
d) drive
r) refuel
q) quit"""


def main():
    print("Lets Drive!")
    car_name = input("Enter your car name: ")
    the_bomb = Car(100, car_name)
    print(str(the_bomb))
    print(MENU)
    choice = input("Enter your choice: ").lower()
    while choice != "q":
        if choice == "d":
            distance_to_drive = int(input("How many km do you wish to drive? "))
            while is_invalid(distance_to_drive):
                print("Distance must be >= 0")
                distance_to_drive = int(input("How many km do you wish to drive? "))
            distance_driven = the_bomb.drive(distance_to_drive)
            print("The car drove {}km".format(distance_driven), end="")
            if the_bomb.fuel == 0:
                print(" and ran out of fuel. ")
        elif choice == "r":
            refuel_amount = int(input("How many units of fuel do you want to add to the car? "))
            while is_invalid(refuel_amount):
                print("Fuel amount must be > = 0")
                refuel_amount = int(input("How many units of fuel do you want to add to the car? "))
            the_bomb.add_fuel(refuel_amount)
            print("Added {} units of fuel.".format(refuel_amount))
        else:
            print("Invalid Choice")
        print(str(the_bomb))
        print(MENU)
        choice = input("Enter your choice: ").lower()
    print("Goodbye {}'s driver.".format(car_name))


def is_invalid(value):
    """Checks to see if value entered is less than 0"""
    if int(value) < 0:
        return True
    return False


if __name__ == '__main__':
    main()
