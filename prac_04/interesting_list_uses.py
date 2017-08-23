def main():
    numbers = []
    number_count = 1
    number = 0
    while number >= 0:
        number = int(input("Number {}: ".format(number_count)))
        numbers.append(number)
        number_count += 1
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    average = sum(numbers) / len(numbers)
    print("The average of the numbers is {}".format(average))

main()