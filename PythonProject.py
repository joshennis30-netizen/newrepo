import random
from db import read_money
from db import write_money

def bet(bet_amount, outcome, money):
    if outcome == "lose":
        money -= bet_amount
    else:
        bet_amount = bet_amount * 1.5
        bet_amount = round(bet_amount, 2)
        money += bet_amount
    
def cards_deck():
    cards = ["Hearts", "Diamonds", "Clubs", "Spades"]
    deck = []
    for card in cards:
        for i in range(1, 13):
            deck.append([i, "of", card])
    print(deck[0])



def main():
    money = 0
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print()
    money = read_money(money)
    print(f"Money: {money}")
    bet_amount = float(input("Bet amount: "))
    print()
    cards_deck()
    

if __name__ == "__main__":
    main()
