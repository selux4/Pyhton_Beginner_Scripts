"""
COMP.CS.100 rock paper scissors
Creator: Firuze Selin Arslan
Student ID Number: 150930868
"""


def main():
    money = [10, 5, 2, 1]
    change_list = [0,0,0,0]
    i = 0

    purchase_price = int(input("Purchase price: "))
    paid_amount_of_money = int(input("Paid amount of money: "))
    change = paid_amount_of_money - purchase_price

    if paid_amount_of_money == 0:
        return

    if change <= 0:
        print("No change")
        return

    while i < len(money):
        change_list[i] = change // money[i]
        change = change % money[i]
        i += 1

    print("Offer change:")
    if change_list[0] > 0:
        print(f"{change_list[0]} ten-euro notes")
    if change_list[1] > 0:
        print(f"{change_list[1]} five-euro notes")
    if change_list[2] > 0:
        print(f"{change_list[2]} two-euro coins")
    if change_list[3] > 0:
        print(f"{change_list[3]} one-euro coins")


if __name__ == "__main__":
    main()
