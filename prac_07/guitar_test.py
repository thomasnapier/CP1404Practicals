from prac_07.guitar import Guitar

def main():
    L5 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print(str(L5))
    print(L5.get_age())  #  expected 95
    print(L5.is_vintage()) #  expect True


    Other = Guitar("Other Guitar", 2012, 2000)
    print(str(Other))
    print(Other.get_age())  #  expected 5
    print(Other.is_vintage())  # expect False
main()