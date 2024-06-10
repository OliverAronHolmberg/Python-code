


class Main:

    def __init__(self):
        self.run = True
        self.contractions = ["hej"]


    def ReplaceCon(self, lista):
        self.lista = lista
        print(lista)
        
        





main = Main()

while main.run == True:
    mening = input("Write your sentence(write Stop to end)").capitalize()

    if mening == "Stop":
        print("Quiting")
        quit()

    else:
        
        main.ReplaceCon([mening.split()])