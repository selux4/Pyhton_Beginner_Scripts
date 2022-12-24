"""
COMP.CS.100 Game of matchsticks
Crearter: Firuze Selin Arslan
Student ID Number: 150930868
"""


def main():
    player1_turn = True
    total_sticks = 21

    print("Game of sticks")
    while True:
        if player1_turn:
            player = 1
        else:
            player = 2

        player_stick = int(input(f"Player {player} enter how many sticks to remove: "))
        if player_stick < 1 or player_stick > 3:
            print("Must remove between 1-3 sticks!")
            continue

        total_sticks = total_sticks - player_stick

        if total_sticks <= 0:
            if player1_turn:
                player = 1
            else:
                player = 2
        else:
            print(f"There are {total_sticks} sticks left")
            player1_turn = not player1_turn
            continue

        print(f"Player {player} lost the game!")
        break


if __name__ == "__main__":
    main()
