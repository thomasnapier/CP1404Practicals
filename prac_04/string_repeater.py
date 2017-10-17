strings = []
repeated_strings = []
string = input("String: ")
while string != "":
    string = input("String: ")
    strings.append(string)
if string in strings:
    repeated_strings = [string]
else:
    print("No strings repeated")
print("Repeated strings: {}".format(repeated_strings))
