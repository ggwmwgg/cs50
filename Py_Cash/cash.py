def main():
    cents = get_cents()
    quarters = get_quarters(cents)
    cents = cents - quarters * 25

    dimes = get_dimes(cents)
    cents = cents - dimes * 10

    nickels = get_nickels(cents)
    cents = cents - nickels * 5

    pennies = get_pennies(cents)
    cents = cents - pennies * 1

    coins = quarters + dimes + nickels + pennies
    print(f"{int(coins)}")


# Dollars to cents
def get_cents():
    while True:
        try:
            cents = float(input("Change owed: "))
        except:
            cents = float(input("Change owed: "))
        if cents > 0:
            return cents * 100


# Cents to quarters
def get_quarters(cents):
    qr = cents // 25
    return qr


# Cents to dimes
def get_dimes(cents):
    dr = cents // 10
    return dr


# Cents to nickels
def get_nickels(cents):
    nr = cents // 5
    return nr


# Cents to pennies
def get_pennies(cents):
    pr = cents // 1
    return pr


main()
