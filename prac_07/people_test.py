from operator import itemgetter
from prac_07.people import People



def main():
    people = []

    first_name = input("First Name: ")
    while first_name != "":
        last_name = input("Last Name:")
        age = int(input("Age: "))
        new_person = People(first_name, last_name, age)
        people.append(new_person)
        print(new_person)
        first_name = input("First Name: ")

    for person in people:
        print(person)
main()