from prac_08.car import Car
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose, d)rive"

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
total_cost = 0
print("Lets drive!")
print(MENU)
menu_choice = input(">>>").lower()
while menu_choice != "q":
    if menu_choice == "c":
        print("Taxis Available:")
        for count, taxi in enumerate(taxis):
            print("{} - {}".format(count, taxi))
        taxi_choice = int(input("Choose taxi: "))
        current_taxi = taxis[taxi_choice]
    elif menu_choice == "d":
        current_taxi.start_fare()
        distance_to_drive = float(input("Drive how far? "))
        current_taxi.drive(distance_to_drive)
        trip_cost = current_taxi.get_fare()
        print("Your {} trip cost you {:.2f}".format(current_taxi.name, trip_cost))
        total_cost += trip_cost
    else:
        print("Invalid Menu Choice")
    print("Bill to date: ${:.2f}".format(total_cost))
    print(MENU)
    menu_choice = input(">>>").lower()
print("Total trip cost: {}".format(total_cost))
print("Taxis are now: ")
for count, taxi in enumerate(taxis):
    print("{} - {}".format(count, taxi))
