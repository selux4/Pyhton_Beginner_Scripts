"""
COMP.CS.100 rock paper scissors
Creator: Firuze Selin Arslan
Student ID Number: 150930868
"""


def main():
    player1 = str(input("Player 1, enter your choice (R/P/S): "))
    player2 = str(input("Player 2, enter your choice (R/P/S): "))
    if player1 == "S" and player2 == "P":
        print("Player 1 won!")
    elif player1 == "P" and player2 == "R":
        print("Player 1 won!")
    elif player1 == "R" and player2 == "S":
        print("Player 1 won!")
    elif player1 == player2:
        print("It's a tie!")
    else:
        print("Player 2 won!")




if __name__ == "__main__":
    main()
