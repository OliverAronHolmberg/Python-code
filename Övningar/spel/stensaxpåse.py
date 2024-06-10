import random


class Game:

    def __init__(self):
        self.lista = ["rock", "scissors", "paper"]
        self.play = True
        self.spela_igen = False

    def Gissning(self, gissat):
        self.gissat = gissat

        print("")

        if gissat == "rock" and self.val == "scissors":
            print("I chose Scissors")
            print("You Won")
        elif gissat == "scissors" and self.val == "paper":
            print("I chose Paper")
            print("You Won")
        elif gissat == "paper" and self.val == "rock":
            print("I chose Rock")
            print("You Won")
        
        elif gissat == "scissors" and self.val == "rock":
            print("I chose Rock")
            print("I won!")
        elif gissat == "paper" and self.val == "scissors":
            print("I chose Scissors")
            print("I won!")
        elif gissat == "rock" and self.val == "paper":
            print("I chose Paper")
            print("I won!")
        else:
            print(f"I chose {self.val.title()}")
            print("It was a draw")
        
        print("")
        while self.spela_igen == "yes" or "no":
            self.spela_igen = input("Do you want to play more? Yes/No").lower()
            if self.spela_igen == "yes":
                print("How fun")
                print("")
                print("**********************************")
                break
            elif self.spela_igen == "no":
                print("See you next time!")
                game.play == False
                quit()
            else:
                continue



game = Game()
print("**********************************")
print("!!Welcome to Rock/Paper/Scissors!!")
print("**********************************")
while game.play == True:
    game.val = random.choice(game.lista)
    gissning = input("Please write either: Rock/Paper/Scissors").lower()
    
    
    if gissning == "rock" or gissning == "scissors" or gissning == "paper":
        gis = game.Gissning(gissning)
    
    else:
        print("You cannot cheat you cheater")
        print("")

