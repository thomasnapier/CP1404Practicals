import random

CHARACTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWSYZ"
NUMBERS = "1234567890"
SPECIAL = "!@#$%^&*()_-=+`~,./'[]<>?{}|"
FORMAT = "#%*"
password = ""
password_format = ""

length_of_password = int(input("How many characters in your password?"))
number = input("Do you want a number in your password?").upper()
upper = input("Do you want an upper letter in your password?").upper()
special = input("Do you want a special character in your password?").upper()
for i in range(0, length_of_password, 1):
    if number == "Y":
        password += random.choice(NUMBERS)
    else:
        password += random.choice(CHARACTERS)
    if upper == "Y":
        password += random.choice(UPPER_CHARACTERS)
    else:
        password += CHARACTERS
    if special == "Y":
        password += random.choice(SPECIAL)
    else:
        password += CHARACTERS
print(password)
