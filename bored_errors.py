"""
COMP.CS.100 bored
Creator: Firuze Selin Arslan
Student ID Number: 150930868
"""

def main():
    letters = {"Y","y","N","n"}
    word = True

    while word:
        word = str(input("Answer Y or N: "))
        if word not in letters:
            print("Incorrect entry.")
        else:
            print("You answered",word)
            word = False


if __name__ == "__main__":
    main()