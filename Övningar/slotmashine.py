import random


def spin_row():
    symbols = ["@", "$", "#", "€", "£"]

    return [random.choice(symbols) for _ in range(3)]
    

def print_row(row):
    print(" | ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "@":
            return bet * 3
        elif row[0] == "$":
            return bet * 10
        elif row[0] == "#":
            return bet * 2
        elif row[0] == "€":
            return bet * 5
        elif row[0] == "£":
            return bet **bet
         
    return 0


def main():
    pass
    balance = 100

    print("Welcome to Pyslots")

    while balance > 0:
        print(f"Current balance is {balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print(f"Du kan inte betta {bet} din noob, betta ett giltigt nummer")
            continue
        
        bet = int(bet)
        if bet > balance:
            print(f"Du kan inte betta pengar du inte har, betta maximalt {balance} kr")
            continue

        if bet <= 0:
            print(f"Hörru du, du kan inte betta {bet} kr, bettal mer än 0 kr tack")
            continue


        balance -=  bet

        row = spin_row()
        print("spinning... \n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f" You Won {payout} kr")
        else:
            print(f"Du är sämst, jag slår vad om att du inte kan vinna")
        balance += payout


if __name__ == "__main__":
    main()