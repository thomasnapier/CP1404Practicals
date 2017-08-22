numbers = []
for number in range(1, 6):
    num = int(input("Number: "))
    numbers.append(num)
print("The first number is {}".format(numbers[0]))
print("The second number is {}".format(numbers[4]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
average = sum(numbers) / len(numbers)
print("The average of the numbers is {}".format(average))