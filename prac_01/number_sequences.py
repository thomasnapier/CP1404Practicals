first_num = int(input("Enter in the first number: "))
second_num = int(input("Enter in the second number: "))
if first_num < 0 or second_num < 0:
    print("Please enter in a real range")
else:
    print("1. Show the even numbers from " + str(first_num) + " to " + str(second_num))
    print("2. Show the odd numbers from " + str(first_num) + " to " + str(second_num))
    print("3. Show the squares from " + str(first_num) + " to " + str(second_num))
    print("4. Exit the program")
    choice = input(">>> ")
    while choice != "4":
        if choice == "1":
            for i in range(int(first_num), int(second_num), 2):
                print(i + 1)
        elif choice == "2":
            for i in range(int(first_num), int(second_num), 2):
                print(i)
            print()
        elif choice == "3":
            for i in range(int(first_num), int(second_num)):
                print(str(i) + " squared is " + str(i**2))
        else:
            print("Invalid number")
        print("1. Show the even numbers from " + str(first_num) + " to " + str(second_num))
        print("2. Show the odd numbers from " + str(first_num) + " to " + str(second_num))
        print("3. Show the squares from " + str(first_num) + " to " + str(second_num))
        print("4. Exit the program")
        choice = input(">>> ")
    print("Finished")
