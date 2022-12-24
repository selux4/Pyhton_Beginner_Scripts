"""
COMP.CS.100 bored
Creator: Firuze Selin Arslan
Student ID Number: 150930868
"""

def main():

    word = True

    while word:
        word = input("Bored? (y/n) ")
        if word == "y":
            print("Well, let's stop this, then.")
            word = False



if __name__ == "__main__":
    main()