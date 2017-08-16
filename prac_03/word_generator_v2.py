"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""


def main():
    import random
    # random generator where the user enters the format
    VOWELS = "aeiou"
    CONSONANTS = "bcdfghjklmnpqrstvwxyz"

    word_format = str(input("Enter the format you would like for your word (c = consonant, v = vowel): ")).lower()
    while is_valid_format(word_format) == False:
        print("Invalid format")
        word_format = str(input("Enter the format you would like for your word (c = consonant, v = vowel): ")).lower()
    word = ""
    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)

    print(word)


def is_valid_format(letters):
    """check if the format entered by the user conforms to the actual format"""
    for _ in letters:
        if _ not in "cv":
            return False
    return True


main()

# import random
#
# VOWELS = "aeiou"
# CONSONANTS = "bcdfghjklmnpqrstvwxyz"
# RANDOM = "bcdfghjklmnpqrstvwxyzaeiou"
#
# word = ""
# word_format = input("Enter in anything (# = random vowel, % = random constant, * = random constant or vowel): ")
# for char in word_format:
#     if char == "#":
#         word += random.choice(VOWELS)
#     elif char == "%":
#         word += random.choice(CONSONANTS)
#     elif char == "*":
#         word += random.choice(RANDOM)
#     else:
#         word += char
# print(word) random generator where the user can enter in wildcard characters


# import random
#
# VOWELS = "aeiou"
# CONSONANTS = "bcdfghjklmnpqrstvwxyz"
# RANDOM = "bcdfghjklmnpqrstvwxyzaeiou"
# FORMAT = "#%*bcdfghjklmnpqrstvwxyzaeiou"
# word = ""
# word_format = ""
#
# max_length = int(input("How long do you want the word to be?: "))
# for i in range(0, max_length, 1):
#     word_format += random.choice(FORMAT)
# for char in word_format:
#     if char == "#":
#         word += random.choice(VOWELS)
#     elif char == "%":
#         word += random.choice(CONSONANTS)
#     elif char == "*":
#         word += random.choice(RANDOM)
#     else:
#         word += char
# print(word) #random generator that random generates the word_format variable
