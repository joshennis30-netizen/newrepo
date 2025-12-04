import random
import os
from db import read_money
from db import write_money

def bet(bet_amount, outcome, money):
    choice = "x"
    if outcome == "win":
        bet_amount = bet_amount * 1.5
        bet_amount = round(bet_amount, 2)
        money += bet_amount
        print(f"Money: {money}")
        write_money(money)
        print()
        choice = input("Play again? (y/n): ").lower()
        if choice == "n":
            print("Come back soon!")
            print("Bye!")
            exit()
    elif outcome == "lose":
        money -= bet_amount
        write_money(money)
        print(f"Money: {money}")
        print()
        choice = input("Play again? (y/n): ").lower()
        if choice == "n":
           print("Come back soon!")
           print("Bye!")
           exit()
    else:
        money += bet_amount
        print(f"Money: {money}")
        print()
        choice = input("Play again? (y/n): ").lower()
        if choice == "n":
            print("Come back soon!")
            print("Bye!")
            exit()
   
def cards_deck(deck):
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    cards = ["Hearts", "Diamonds", "Clubs", "Spades"]
    faces = ["Jack", "King", "Queen"]
    for card in cards:
        deck.append([11, "of", card])
    for card in cards:
        for value in values:
            deck.append([value, "of", card])
    for card in cards:
        for face in faces:
            deck.append([face, "of", card])

def dealer_hand(deck):
    deal_value = 0
    deal_hand = []
    while deal_value < 17:
        hand = random.randrange(0, len(deck))
        deal_hand.append(deck[hand])
        deck.pop(hand)
        for i in range(0, len(deal_hand)):
            if deal_hand[i][0] == "Jack" or deal_hand[i][0] == "King" or deal_hand[i][0] == "Queen":
                deal_value += 10
            elif deal_hand[i][0] == 11 and deal_value > 11:
                deal_value += 1
            else:
                deal_value += deal_hand[i][0]
    return deal_hand

def player_hand(deck):
    play_value = 0
    play_hand = []
    while len(play_hand) < 2:
        hand = random.randrange(0, len(deck))
        play_hand.append(deck[hand])
        deck.pop(hand)
        for i in range(0, len(play_hand)):
            if play_hand[i][0] == "Jack" or play_hand[i][0] == "King" or play_hand[i][0] == "Queen":
                play_value += 10
            elif play_hand[i][0] == 11 and play_value > 11:
                play_value += 1
            else:
                play_value += int(play_hand[i][0])
    return play_hand

def betting(money):
    while True:
        try:
            bet_amount = float(input("Bet amount: ")) 
            if bet_amount < 5 or bet_amount > 1000:
                print("Bet amount must be more than 5 and less than 1000. Try again.")
            elif bet_amount > money:
                print("Bet amount cannot be greater than current money. Try again.")
            else:
                return bet_amount
        except ValueError:
            print("Must be valid integer or float. Try again.")

def main():
    buy = "v"
    fold = "x"
    deck = []
    turn = 0
    money = 0
    outcome = "n"
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print()
    while True:
        money = read_money(money)
        print(f"Money: {money}")
        if money < 5:
            while buy != "n":
                buy = input("Not enough money to bet. Would you like to buy some chips> (y/n)").lower()
                if buy == "y":
                    money += 5
                    write_money(money)
                    break
                else:
                    break
        bet_amount = betting(money)
        print()
        cards_deck(deck)
        deal_hand = dealer_hand(deck)
        play_hand = player_hand(deck)
        deal_score = 0
        play_score = 0
        for i in range(0, len(deal_hand)):
            if deal_hand[i][0] == "Jack" or deal_hand[i][0] == "King" or deal_hand[i][0] == "Queen":
                deal_score += 10
            elif deal_hand[i][0] == 11 and deal_score > 11:
                deal_score += 1
            else:
                deal_score += deal_hand[i][0]
        print("DEALER's SHOW CARD:")
        print(deal_hand[0])
        print()
        print("YOUR CARDS:")
        print(play_hand[0])
        print(play_hand[1])
        print()
        fold = input("Hit or stand? (hit/stand): ").lower()
        while fold == "hit":
            hand = random.randrange(0, len(deck))
            play_hand.append(deck[hand])
            deck.pop(hand)
            for i in range(0, len(play_hand)):
                print(play_hand[i])
            fold = input("Hit or stand? (hit/stand): ")
        for i in range(0, len(play_hand)):
            if play_hand[i][0] == "Jack" or play_hand[i][0] == "King" or play_hand[i][0] == "Queen":
                play_score += 10
            elif play_hand[i][0] == 11 and play_score > 11:
                play_score += 1
            else:
                play_score += int(play_hand[i][0])
        fold = "x"
        print("DEALER'S CARDS:")
        for i in range(0, len(deal_hand)):
            print(deal_hand[i])
        print()
        print(f"YOUR POINTS: {play_score}")
        print(f"DEALER'S POINTS: {deal_score}")
        print()
        if play_score == 21:
            print("Congratulations! You Win.")
            outcome = "win"
        elif deal_score == 21:
            print("Sorry. You lose.")
            outcome = "lose"
        elif play_score > 21:
            print("Sorry. You lose.")
            outcome = "lose"
        elif deal_score > 21:
            print("Congratulations! You Win.")
            outcome = "win"
        elif play_score > deal_score:
            print("Congratulations! You Win.")
            outcome = "win"
        elif play_score < deal_score:
            print("Sorry. You lose.")
            outcome = "lose"
        bet(bet_amount, outcome, money)

if __name__ == "__main__":
    main()
