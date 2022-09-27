import random

def main():
    """Start an element guessing game."""
    print("Guess a random element!")
    """jawapan yang ada dalam guess random element"""
    elements = [
        "hydrogen",
        "helium",
        "lithium",
        "berylium",
        "boron",
        "carbon",
        "nitrogen",
        "oxygen",
        "fluorine",
        "neon",
        ]
    """untuk menghasilkan jawapan random untuk diteka"""
    x = random.choice(elements)
    print(x)
    guess = None

    """memberi hint untuk pemain meneka jawapan"""
    while x != guess:

        guess = str(input("What element am i thinking of? "))

        if x == guess:
            print("You guessed {}.Congratulation you guessed it right!".format(guess))
        elif x == "hydrogen":
            print("HINT:lightest atom")
        elif x =="helium":
            print("HINT:colorless,odorless,tasteless,non-toxic")
        elif x =="lithium":
            print("HINT:three protons,three or four neutrons,three electrons")
        elif x =="berylium":
            print("HINT:neodymium magnets,the strongest of permanent magnet")
        elif x =="boron":
            print("HINT:the strongest type of permanent magnet")
        elif x =="carbon":
            print("HINT:4 electrons to form a covalent bond,has numbers of allotropes and other forms if existence")
        elif x =="nitrogen":
            print("HINT:odorless,colorless,tasteless gas that makes up 80% of the air we breathe")
        elif x =="oxygen":
            print("HINT:a gas without color,taste or smell")
        elif x =="fluorine":
            print("HINT:pale yellow,corrosive gas,react with organic and inorganic substances")
        elif x =="neon":
            print("HINT:colorless,odorless,inert monatomic gas under standard condition")

main()
