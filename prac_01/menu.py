user_name = input("Enter name: ")
print("(H)ello")
print("(G)oodbye")
print("(Q)uit")
choice = input(">>> ")
while choice != "Q" or choice != "q":
    if choice == "H" or choice == "h":
        print("Hello " + user_name)
    elif choice == "G" or choice == "g":
        print("Goodbye " + user_name)
    elif choice == "Q" or choice == "q":
        choice = "Q"
    else:
        print("Invalid choice")
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    choice = input(">>> ")
print("Finished")