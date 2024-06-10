import random
import time




class Game:


    def __init__(self):
        self.cash = 100
        self.gamelist = [1, 1, 1]


    def Lottery(self, bet):
        self.bet = bet
        self.gamelist = [(1 * random.randint(1, 2)), (1 * random.randint(1, 2)), (1 * random.randint(1, 2))]
        print("")

        for x in range(3):
            print("Rolling...")
            time.sleep(1)
            x = x + 1

        print("")
        print("")
        print(self.gamelist)
        print("")
        
        
        
        if self.gamelist[0] == self.gamelist[1] and self.gamelist[0] == self.gamelist[2]:
            if self.gamelist[0] == 0: 
                print("You Won!!!")
                print(f"${bet * 2} has been deposited in your wallet")
                self.cash = self.cash + bet * 2
                print("")
                print(f"You have ${game.cash} to your name")

            if self.gamelist[0] == 1: 
                print("You Won!!!")
                print(f"${bet * 5} has been deposited in your wallet")
                self.cash = self.cash + bet * 5
                print("")
                print(f"You have ${game.cash} to your name")

            if self.gamelist[0] == 2: 
                print("You Won!!!")
                print(f"${bet * 10} has been deposited in your wallet")
                self.cash = self.cash + bet * 10
                print("")
                print(f"You have ${game.cash} to your name")
        else:
            print("You sadly lost:(")
            print(f"{bet} has been withdrawned from your wallet")
            print("")
            self.cash = self.cash - bet
            print(f"You have ${game.cash} to your name")
            
            

        notplay = True 
        while notplay == True:
            play_again = input("Do you want to bet again or leave? (Yes/No): ").lower()
            if play_again == "yes":
                print("How fun!")
                print("")
                print(f"You have ${game.cash} to your name")
                print("")
                notplay = False
                return
            elif play_again == "no":
                print(f"You left with ${game.cash}")
                quit()
            
                
                




game = Game()


print("!Welcome to the lottery!")

print("")
print(f"You have ${game.cash} to your name")

while game.cash > 0:
    
    

    bet = (input("How much do you want to bet"))
    
    
    try:
        int(bet)
        bet = int(bet)
        if bet < 1 or bet > game.cash:
            print("You cannot bet that")
            
        else:
            print("Bet Accepted")
            game.Lottery(bet)
    
    except ValueError:
        print("You cant bet that")
        print("")
        
    






