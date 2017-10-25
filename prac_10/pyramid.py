"""
CP1404/CP5632 Practical
Recursion (Pyramid)
"""

number_of_rows = int(input("How many rows? "))
total = 0
for number in range(number_of_rows + 1):
    total += number
print(total)


def number_of_blocks(rows):
    if int(rows) <= 0:
        return 0
    return int(rows) + number_of_blocks(int(rows) - 1)

print(number_of_blocks(number_of_rows))
