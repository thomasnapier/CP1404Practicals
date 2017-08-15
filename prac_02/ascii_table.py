LOWER = 33
UPPER = 127

character = input("Enter a character: ")
print("The ASCII code for {} is {}".format(character, ord(character)))
number = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
while number < LOWER or number > UPPER:
    number = int(input("Enter a number between {} and {}".format(LOWER, UPPER)))
print("The character for {} is {}".format(number, chr(number)))

for value in range(LOWER, UPPER + 1):
    print("{:3} {:>4}".format(value, chr(value)))