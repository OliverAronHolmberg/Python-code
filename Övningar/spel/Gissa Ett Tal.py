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
            print("För lågt, gissa igen")
            self.antalet = self.antalet + 1
        elif gissningar > self.tal:
            print("För högt, gissa igen")
            self.antalet = self.antalet + 1
        else:
            print(f"Du gissade rätt på {antalet} gissningar")
            while self.spela_igen != "ja" or self.spela_igen != "nej":
                self.spela_igen = input(("Vill du spela igen Ja/Nej:")).lower()
                if self.spela_igen == "ja":
                    print("")
                    self.antalet = 1
                    return
                elif self.spela_igen == "nej":
                    print("")
                    print("Hejdå!")
                    quit()
                else:
                    print("skriv Ja eller Nej")
                    
            



game = Game()
print("Välkommen till Gissa ett Tal!")


while game.gameplay == True:
    
    gissning = input("Gissa ett tal")
    if gissning.isdigit():
        gissning = int(gissning)
        game.Gissa(gissning)

    

    else:
        print("Gissa ett tal är du snäll")
        


    



