import random


class Game:


    def __init__(self):
        self.tal = random.randint(1, 100)
        self.gameplay = True
        self.spela_igen = True
        self.antalet = 1

    def Gissa(self, gissningar):
        antalet = self.antalet
        if gissningar < self.tal:
            print("To low of a number, guess again:")
            self.antalet = self.antalet + 1
        elif gissningar > self.tal:
            print("To high of a number, guess again: ")
            self.antalet = self.antalet + 1
        else:
            print(f"You got it in {antalet} guesses")
            while self.spela_igen != "no" or self.spela_igen != "yes":
                self.spela_igen = input(("Do you want to play again Yes/No:")).lower()
                if self.spela_igen == "no":
                    print("")
                    print("*****************************")
                    self.antalet = 1
                    return
                elif self.spela_igen == "yes":
                    print("")
                    print("Bye!")
                    quit()
                else:
                    print("Please write Yes or No")
                    
            



game = Game()
print("*****************************")
print("!!Welcome to Guess a Number!!")
print("*****************************")

while game.gameplay == True:
    
    gissning = input("Guess a number from 0-100: ")
    if gissning.isdigit():
        gissning = int(gissning)
        game.Gissa(gissning)

    elif gissning >= 100:
        print("Please guess lower than 100")
    
    elif gissning < 0:
        print("Please guess higher than 0")

    else:
        print("Guess a number please")
        


    



