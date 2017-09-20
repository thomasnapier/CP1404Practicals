from prac_07.date import Date

def main():
    print("Current Date: ")
    date = Date(20, 9, 2017)
    print(str(date))

    number_of_days = int(input("Enter the number of days you wish to add: "))
    print("In {} days the date will be".format(number_of_days))
    date.add_days(number_of_days)
    print(str(date))
main()