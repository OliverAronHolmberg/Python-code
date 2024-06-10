import random


class Game:

    def __init__(self):
        self.lista = ["sten", "sax", "påse"]
        self.play = True
        self.spela_igen = False

    def Gissning(self, gissat):
        self.gissat = gissat
        if gissat == "sten" and self.val == "sax":
            print("I chose scissors")
            print("You Won")
        elif gissat == "sax" and self.val == "påse":
            print("Jag valde påse")
            print("Du vann")
        elif gissat == "påse" and self.val == "sten":
            print("Jag valde sten")
            print("Du vann")
        
        elif gissat == "sax" and self.val == "sten":
            print("Jag valde sten")
            print("Jag vann")
        elif gissat == "påse" and self.val == "sax":
            print("Jag valde sax")
            print("Jag vann")
        elif gissat == "sten" and self.val == "påse":
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
    gissning = input("Skriv antingen: Sten/Sax/Påse").lower()
    
    
    if gissning == "sten" or gissning == "sax" or gissning == "påse":
        gis = game.Gissning(gissning)
    
    else:
        print("Du kan inte fuska din fuskis!")

