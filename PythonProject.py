import random

def read_money():
    money = 0
    with open("money.txt") as file:
        money = file.read()
    print(money)
    return money

def write_money(money):
    with open("money.txt") as file:
        file.write(money)




def main():
    money = 0
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print()
    money = read_money()
    print(f"Money: {money}")
    write_money(money)
    

if __name__ == "__main__":
    main()
