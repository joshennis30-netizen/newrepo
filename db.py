def read_money(money):
    try:
        with open("money.txt", "r") as file:
            money = file.read()
            money = float(money)
        return money
    except FileNotFoundError:
        print("Could not find money file!")
        print("Creating new money file.")
        money = 100.0
        with open("money.txt", "w") as file:
            file.write(str(money))
        return money

def write_money(money):
    with open("money.txt", "w") as file:
        file.write(str(money))
