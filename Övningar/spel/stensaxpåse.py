import random


class Game:

    def __init__(self):
        self.lista = ["rock", "scissors", "paper"]
        self.play = True
        self.spela_igen = False

    def Gissning(self, gissat):
        self.gissat = gissat
        if gissat == "rock" and self.val == "scissors":
            print("I chose scissors")
            print("You Won")
        elif gissat == "scissors" and self.val == "paper":
            print("Jag valde påse")
            print("Du vann")
        elif gissat == "paper" and self.val == "rock":
            print("Jag valde sten")
            print("Du vann")
        
        elif gissat == "scissors" and self.val == "rock":
            print("Jag valde sten")
            print("Jag vann")
        elif gissat == "paper" and self.val == "scissors":
            print("Jag valde sax")
            print("Jag vann")
        elif gissat == "rock" and self.val == "paper":
            print("Jag valde påse")
            print("Jag vann")
        else:
            print(f"Jag valde {self.val}")
            print("oavgjort")
        
        
        while self.spela_igen == "ja" or "nej":
            self.spela_igen = input("Vill du spela Ja/Nej").lower()
            if self.spela_igen == "ja":
                print("Vad kul")
                print("")
                break
            elif self.spela_igen == "nej":
                print("Hejdå")
                game.play == False
                quit()
            else:
                continue



game = Game()

print("!!Välkommen till stex/sax/påse!!")

while game.play == True:
    game.val = random.choice(game.lista)
    gissning = input("Skriv: Sten/Sax/Påse").lower()
    
    
    if gissning == "sten" or gissning == "sax" or gissning == "påse":
        gis = game.Gissning(gissning)
    
    else:
        print("Du kan inte fuska din fuskis!")

