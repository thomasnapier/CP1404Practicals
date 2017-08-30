COLOUR_CODES = {"Aliceblue": "#f0f8ff", "Blanchedalmond": "#ffebcd", "Blueviolet": "#8a2be2", "Cadetblue": "#5f9ea0",
                "Blue": "#0000ff", "Cyan": "00ffff", "Darkgreen": "#006400", "Dodgerblue": "#1e90ff"}

colour = input("Enter colour name: ").capitalize()
while colour != "":
    if colour in COLOUR_CODES:
        print(colour, "is", COLOUR_CODES[colour])
    else:
        print("Invalid colour name")
    colour = input("Enter colour name: ").capitalize()



