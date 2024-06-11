import random

class Main:


    def __init__(self):
        self.run = True
        self.uh = "uh"
        self.eh = "eh"
        

    def AddUh(self, sentance):
        self.sentance = sentance
        print(sentance)





main = Main()


while main.run == True:
    type = input("How do you need the sentance (lowercase/uppercase/capitalize/title): ").lower()
    if type == "lowercase":
        sentance = input("Write your sentance (Quit to quit)").lower()
        main.AddUh(sentance)
    elif type == "uppercase":
        sentance = input("Write your sentance (Quit to quit)").upper()
        main.AddUh(sentance)
    elif type == "capitalize":
        sentance = input("Write your sentance (Quit to quit)").capitalize()
        main.AddUh(sentance)
    elif type == "title":
        sentance = input("Write your sentance (Quit to quit)").title()
        main.AddUh(sentance)
    else:
        print("Plase awswer correctly")
        print("")
        continue
        
        
    
    
    

    
    


    