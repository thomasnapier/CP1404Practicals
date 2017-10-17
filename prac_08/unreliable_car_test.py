from prac_08.unreliable_car import UnreliableCar

old_car = UnreliableCar("Old", 100, 20)
old_car.drive(50)
print(old_car)

new_car = UnreliableCar("New", 100, 80)
new_car.drive(50)
print(new_car)

for i in range(1, 10):
    print("Attempting to drive {}km:".format(i))
    print("{:12} drove {:2}km".format(new_car.name, new_car.drive(i)))
    print("{:12} drove {:2}km".format(old_car.name, old_car.drive(i)))

print(new_car)
print(old_car)