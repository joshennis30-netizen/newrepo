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
    
def cards_deck(deck):
    values = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    cards = ["Hearts", "Diamonds", "Clubs", "Spades"]
    faces = ["Jack", "King", "Queen"]
    for card in cards:
        deck.append([11, "of", card])
    for card in cards:
        for i in range(2, 10):
            deck.append([i, "of", card])
    for card in cards:
        for face in faces:
            deck.append([face, "of", card])

def dealer_hand(deck):
    deal_hand = []
    hand = random.randrange(1, len(deck))
    deal_hand.append(deck[hand])
    deck.pop[hand]

def player_hand(deck):
    play_hand = []
    hand = random.randrange(1, len(deck))
    play_hand.append(deck[hand])
    deck.pop[hand]



def main():
    deck = []
    turn = 0
    money = 0
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print()
    money = read_money(money)
    print(f"Money: {money}")
    bet_amount = float(input("Bet amount: "))
    if bet_amount < 5 or bet_amount > 1000:
        print("Bet amount must be more than 5 and less than 1000. Try again.")
    print()
    cards_deck(deck)
    
    

if __name__ == "__main__":
    main()
