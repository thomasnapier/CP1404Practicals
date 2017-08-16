"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    """Get number from user and display their standing"""
    score = float(input("Enter score: "))
    print(determine_standing(score))

def determine_standing(number):
    """determine the status of the entered score"""
    if number < 0 or number > 100:
        return "Invalid Score"
    elif number >= 90:
        return "Excellent"
    elif number >= 50:
        return "Good"
    else:
        return "Bad"


main()
