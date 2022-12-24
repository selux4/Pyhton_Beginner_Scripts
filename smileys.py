"""
COMP.CS.100 Smileys
Crearter: Firuze Selin Arslan
Student ID Number: 150930868
"""


def main():
    try:
        feel = int(input("How do you feel? (1-10) "))
    except Exception as e:
        print(e)
        print("Bad input!")
        return

    if feel == 10:
        face = ":-D"
    elif 10 > feel > 7:
        face = ":-)"
    elif 7 >= feel >= 4:
        face = ":-|"
    elif 4 > feel > 1:
        face = ":-("
    elif feel == 1:
        face = ":'("
    else:
        print("Bad input!")
        return
    print("A suitable smiley would be", face)


if __name__ == "__main__":
    main()
