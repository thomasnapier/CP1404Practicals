from prac_07.guitar import Guitar


def main():
    guitars = []
    print("My guitars!")
    # name = input("Name: ")
    # while name != "":
    #     year = int(input("Year: "))
    #     cost = float(input("Cost: $"))
    #     new_guitar = Guitar(name, year, cost)
    #     guitars.append(new_guitar)
    #     print(new_guitar, "added.")
    #     name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("These are my guitars: ")
    for count, guitar in enumerate(guitars):
        # TODO: replace next 4 lines with ternary operator
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        # if guitar.is_vintage():
        #     vintage_string = "(vintage)"
        # else:
        #     vintage_string = ""
        print("Guitar {0}: {self.name:>20} ({self.year}), worth ${self.cost:10,.2f} {1}".format(count + 1, vintage_string, self=guitar))


main()
