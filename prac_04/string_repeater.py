strings = []
string = "l"
while string != '':
    string = input("String: ")
    strings.append(string)
for string1 in strings:
    for string2 in strings:
        if strings[string1] == strings[string2]:
            print("Repeated strings: {}".format(strings[i]))
print("No repeated strings entered")
