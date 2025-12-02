import random

def read_money(money):
    with open("money.txt", "r") as file:
        money = file.read()
    print(money)
    return money

def write_money(money):
    with open("money.txt", "w") as file:
        file.write(str(money))




def main():
    money = 0
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print()
    money = read_money(money)
    money = float(money)
    print(f"Money: {money}")
    money = money - 10
    write_money(money)
    

if __name__ == "__main__":
    main()
