def read_money(money):
    with open("money.txt", "r") as file:
        money = file.read()
        money = float(money)
    return money

def write_money(money):
    with open("money.txt", "w") as file:
        file.write(str(money))
