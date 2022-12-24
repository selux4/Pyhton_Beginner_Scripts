"""
COMP.CS.100 fibonacci
Creator: Firuze Selin Arslan
Student ID Number: 150930868
"""


def main():
    numbers = int(input("How many Fibonacci numbers do you want? "))
    n1, n2 = 0, 1
    count = 0

    while count < numbers:
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
        print(f"{count}.", n1)

if __name__ == "__main__":
    main()
